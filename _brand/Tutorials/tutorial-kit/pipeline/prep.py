"""Prepare a tutorial's raw footage: 2560x1440 working copies, wav, silence map, Whisper word timings.

Usage: python -I prep.py <raw_dir> <work_dir> [--hint "names and terms Whisper should spell right"]

<raw_dir> holds face/ (camera clips) and screen/ (screen recordings). Loose files in <raw_dir> are sorted by
shape: portrait or iPhone-rotated clips count as face, everything else as screen. Check the printout.

Face clips are scaled and cropped to fill 2560x1440 (FACE_Y sets where a portrait clip's 16:9 crop sits).
Screen clips keep their own aspect ratio, fitted inside 2560x1600; base.py pads them later.
Re-running skips clips that are already prepped. Delete <work_dir>/clips.json entries to redo one.
"""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAW = Path(sys.argv[1])
WORK = Path(sys.argv[2])
HINT = sys.argv[sys.argv.index("--hint") + 1] if "--hint" in sys.argv else ""
FACE_Y = 0.30   # portrait test clips only: top of the 16:9 crop as a fraction of the spare height
VIDEO_EXT = (".mov", ".mp4", ".m4v", ".mkv", ".webm")
(WORK / "media").mkdir(parents=True, exist_ok=True)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height:stream_side_data=rotation:stream_tags=rotate:format=duration",
             "-of", "json", str(path)])
    js = json.loads(r.stdout or "{}")
    st = (js.get("streams") or [{}])[0]
    w, h = st.get("width", 0), st.get("height", 0)
    rot = 0
    for sd in st.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(sd["rotation"])
    if not rot and st.get("tags", {}).get("rotate"):
        rot = int(st["tags"]["rotate"])
    if abs(rot) % 180 == 90:
        w, h = h, w
    return w, h, float(js.get("format", {}).get("duration", 0) or 0)


def find_clips():
    found = []
    for kind in ("face", "screen"):
        d = RAW / kind
        if d.is_dir():
            found += [(kind, p) for p in sorted(d.iterdir()) if p.suffix.lower() in VIDEO_EXT]
    for p in sorted(RAW.iterdir()):
        if p.is_file() and p.suffix.lower() in VIDEO_EXT:
            w, h, _ = probe(p)
            found.append(("face" if h > w or p.suffix.lower() == ".mov" else "screen", p))
    return found


def prep_one(kind, src):
    cid = f"{kind}_{re.sub(r'[^A-Za-z0-9_-]+', '-', src.stem)}"
    mez, wav = WORK / "media" / f"{cid}.mp4", WORK / "media" / f"{cid}.wav"
    w, h, dur = probe(src)
    if kind == "face":
        if w / max(h, 1) < 16 / 9:   # taller than 16:9 (portrait test footage): fill the width, crop the height
            vf = f"scale=2560:-2:flags=lanczos,crop=2560:1440:0:(ih-1440)*{FACE_Y}"
        else:
            vf = "scale=-2:1440:flags=lanczos,crop=2560:1440"
        ow, oh = 2560, 1440
    else:
        s = min(2560 / w, 1600 / h, 1.0) if w and h else 1.0
        ow, oh = int(w * s) // 2 * 2, int(h * s) // 2 * 2
        vf = f"scale={ow}:{oh}:flags=lanczos"
    if not mez.exists():
        r = run(["ffmpeg", "-hide_banner", "-y", "-i", str(src), "-vf", vf + ",fps=30", "-c:v", "libx264",
                 "-preset", "fast", "-crf", "16", "-g", "30", "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart",
                 str(mez)])
        if r.returncode:
            print(r.stderr[-2000:]); sys.exit(1)
    if not wav.exists():
        run(["ffmpeg", "-hide_banner", "-y", "-i", str(src), "-vn", "-ac", "1", "-ar", "48000", str(wav)])
    sd = run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "silencedetect=noise=-38dB:d=0.1", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", sd.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", sd.stderr)]
    if len(ends) < len(starts):
        ends.append(dur)
    print(f"prepped {cid}: {kind}, {w}x{h} -> {ow}x{oh}, {dur:.1f}s", flush=True)
    return cid, {"kind": kind, "src": str(src), "w": ow, "h": oh, "duration": round(dur, 3),
                 "silences": [[round(max(s, 0), 3), round(e, 3)] for s, e in zip(starts, ends)]}


def main():
    clips_path = WORK / "clips.json"
    data = json.loads(clips_path.read_text(encoding="utf-8")) if clips_path.exists() else {}
    todo = find_clips()
    if not todo:
        sys.exit(f"no video files in {RAW} (expected face/ and screen/ folders)")
    with ThreadPoolExecutor(2) as ex:
        for cid, info in ex.map(lambda a: prep_one(*a), todo):
            data[cid] = {**data.get(cid, {}), **info}
    clips_path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")

    import whisper
    model = whisper.load_model("small.en")
    for cid, info in data.items():
        if info.get("words") is not None and "--redo" not in sys.argv:
            continue
        res = model.transcribe(str(WORK / "media" / f"{cid}.wav"), word_timestamps=True, fp16=False, language="en",
                               initial_prompt=HINT or None, condition_on_previous_text=False, verbose=None)
        info["words"] = [{"w": w["word"].strip(), "s": round(w["start"], 3), "e": round(w["end"], 3),
                          "p": round(w.get("probability", 0), 2)}
                         for s in res["segments"] for w in s.get("words", [])]
        info["text"] = res["text"].strip()
        clips_path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
        print("transcribed", cid, f"({len(info['words'])} words)", flush=True)
    print("next: python -I lines.py", WORK)


if __name__ == "__main__":
    main()
