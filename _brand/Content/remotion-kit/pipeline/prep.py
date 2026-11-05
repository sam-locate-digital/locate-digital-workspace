"""Prepare raw clips: 1440x2560 working copies, wav audio, silence map, Whisper word timings.

Usage: python -I prep.py <raw_dir> <work_dir>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

RAW = Path(sys.argv[1])
WORK = Path(sys.argv[2])
(WORK / "media").mkdir(parents=True, exist_ok=True)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main():
    clips = sorted(p for p in RAW.iterdir() if p.suffix.lower() in (".mov", ".mp4", ".m4v"))
    out = {}
    for c in clips:
        stem = c.stem
        mez = WORK / "media" / f"{stem}.mp4"
        wav = WORK / "media" / f"{stem}.wav"
        if not mez.exists():
            # ffmpeg auto-rotates the iPhone -90 rotation to portrait
            r = run(["ffmpeg", "-hide_banner", "-y", "-i", str(c), "-vf", "scale=1440:2560:flags=lanczos,fps=30",
                     "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p",
                     "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", str(mez)])
            if r.returncode:
                print(r.stderr[-2000:]); sys.exit(1)
        if not wav.exists():
            run(["ffmpeg", "-hide_banner", "-y", "-i", str(c), "-vn", "-ac", "1", "-ar", "48000", str(wav)])
        sd = run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "silencedetect=noise=-38dB:d=0.1", "-f", "null", "-"])
        starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", sd.stderr)]
        ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", sd.stderr)]
        vol = run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "volumedetect", "-f", "null", "-"])
        mean = re.search(r"mean_volume: (-?[\d.]+)", vol.stderr)
        peak = re.search(r"max_volume: (-?[\d.]+)", vol.stderr)
        out[stem] = {"silences": [[round(max(s, 0), 3), round(e, 3)] for s, e in zip(starts, ends)],
                     "mean_db": float(mean.group(1)) if mean else None,
                     "peak_db": float(peak.group(1)) if peak else None}
        print("prepped", stem, flush=True)

    import whisper
    model = whisper.load_model("small.en")
    for c in clips:
        stem = c.stem
        res = model.transcribe(str(WORK / "media" / f"{stem}.wav"), word_timestamps=True, fp16=False,
                               language="en", condition_on_previous_text=False, verbose=None)
        words = [{"w": w["word"].strip(), "s": round(w["start"], 3), "e": round(w["end"], 3),
                  "p": round(w.get("probability", 0), 2)}
                 for s in res["segments"] for w in s.get("words", [])]
        out[stem]["text"] = res["text"].strip()
        out[stem]["words"] = words
        print("transcribed", stem, flush=True)
    (WORK / "clips.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
