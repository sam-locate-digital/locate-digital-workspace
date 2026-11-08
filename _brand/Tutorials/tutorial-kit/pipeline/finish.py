"""Finish the tutorial: mux the render with the mix, write the chapter list and captions, run the checks.

Usage: python -I finish.py <work_dir> <export_stem>
  <export_stem> is the path without extension, e.g. ".../Tutorials/Exports/2026-11-20_connect-inbox_v1"
Inputs: <work_dir>/remotion/out/video.mp4 (render.mjs), mix.wav (mix.py), timeline.json, edl.json, plan.json
Writes: <stem>.mp4 (H.264 1920x1080 30 fps, AAC 256 kbps, faststart), <stem>_chapters.txt, <stem>.srt, <stem>.vtt,
        and <work_dir>/contact.jpg (one frame every 10 s) for a last look.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
STEM = Path(sys.argv[2])
STEM.parent.mkdir(parents=True, exist_ok=True)
tl = json.loads((WORK / "remotion" / "src" / "timeline.json").read_text(encoding="utf-8"))
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
plan = json.loads((WORK / "plan.json").read_text(encoding="utf-8"))
VIDEO = WORK / "remotion" / "out" / "video.mp4"
mp4 = STEM.with_suffix(".mp4")
if mp4.exists():
    sys.exit(f"{mp4} already exists: bump the version number instead of overwriting")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.stderr[-3000:])
    return r


run(["ffmpeg", "-hide_banner", "-y", "-i", str(VIDEO), "-i", str(WORK / "mix.wav"), "-map", "0:v", "-map", "1:a",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(mp4)])


def clock(s, ms=False, sep=","):
    if ms:
        t = round(s * 1000); h, t = divmod(t, 3600000); m, t = divmod(t, 60000); sec, t = divmod(t, 1000)
        return f"{h:02d}:{m:02d}:{sec:02d}{sep}{t:03d}"
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


# chapter list for the Circle lesson description
chap = [f"0:00 {plan.get('intro_label', 'Introduction')}"] + [f"{clock(c['s'])} {c['title']}" for c in tl["chapters"]]
if tl["chapters"] and tl["chapters"][0]["s"] < 1:
    chap = chap[1:]
STEM.with_name(STEM.name + "_chapters.txt").write_text("\n".join(chap) + "\n", encoding="utf-8")

# captions: sentence-sized cues, at most 2 lines of 42 characters and 6 s each
rep = plan.get("replace", {})
words = []
for w in edl["words"]:
    txt = w["w"]
    core = re.sub(r"[^\w$%'-]", "", txt)
    if core.lower() in {k.lower() for k in rep}:
        fix = next(v for k, v in rep.items() if k.lower() == core.lower())
        txt = txt.replace(core, fix)
    words.append({**w, "w": txt})
cues, cur = [], []
for i, w in enumerate(words):
    if cur:
        text = " ".join(x["w"] for x in cur + [w])
        if (len(text) > 84 or w["e"] - cur[0]["s"] > 6 or w["s"] - cur[-1]["e"] > 0.6
                or (cur[-1]["w"].endswith((".", "?", "!")) and len(" ".join(x["w"] for x in cur)) > 25)):
            cues.append(cur); cur = []
    cur.append(w)
if cur:
    cues.append(cur)


def two_lines(text):
    if len(text) <= 42:
        return text
    mid = len(text) // 2
    spaces = [i for i, ch in enumerate(text) if ch == " "]
    cut = min(spaces, key=lambda i: abs(i - mid))
    return text[:cut] + "\n" + text[cut + 1:]


srt, vtt = [], ["WEBVTT", ""]
for n, c in enumerate(cues, 1):
    s = c[0]["s"]
    e = max(c[-1]["e"], s + 1.0)
    if n < len(cues):
        e = min(e, cues[n][0]["s"] - 0.04)
    text = two_lines(" ".join(x["w"] for x in c))
    srt += [str(n), f"{clock(s, True)} --> {clock(e, True)}", text, ""]
    vtt += [f"{clock(s, True, '.')} --> {clock(e, True, '.')}", text, ""]
STEM.with_suffix(".srt").write_text("\n".join(srt), encoding="utf-8")
STEM.with_suffix(".vtt").write_text("\n".join(vtt), encoding="utf-8")

# checks
pr = run(["ffprobe", "-v", "error", "-show_entries", "format=duration,bit_rate:stream=codec_name,profile,width,height,r_frame_rate",
          "-of", "json", str(mp4)])
js = json.loads(pr.stdout)
v = next(s for s in js["streams"] if s["codec_name"] == "h264")
dur = float(js["format"]["duration"])
loud = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp4), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
i_l = re.findall(r"I:\s+(-?[\d.]+) LUFS", loud)[-1]
tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", loud)[-1]
n = max(1, int(dur // 10))
run(["ffmpeg", "-hide_banner", "-y", "-i", str(mp4), "-vf",
     f"fps=1/10,scale=384:-2,tile=5x{(n + 4) // 5}:padding=4", "-frames:v", "1", str(WORK / "contact.jpg")])
ok = abs(dur - tl["length"]) < 0.15
print(f"{mp4.name}: {clock(dur)} ({dur:.2f}s, timeline {tl['length']:.2f}s{'' if ok else ' << LENGTH MISMATCH'}), "
      f"{v['width']}x{v['height']} {v['profile']} {v['r_frame_rate']} fps, {int(js['format']['bit_rate']) / 1e6:.1f} Mbps, "
      f"{i_l} LUFS, true peak {tp} dBTP")
print(f"{len(cues)} caption cues -> {STEM.name}.srt / .vtt | chapters -> {STEM.name}_chapters.txt | contact sheet -> {WORK / 'contact.jpg'}")
print("\n".join(chap))
