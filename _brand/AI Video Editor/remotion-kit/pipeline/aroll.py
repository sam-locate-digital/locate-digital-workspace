"""Cut the a-roll from the EDL: trims each piece from the 1440p working copies and joins them.

Usage: python -I aroll.py <work_dir>
Each audio piece gets an 8 ms fade in and out so the joins don't click.
"""
import json
import subprocess
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
clips = sorted({p["clip"] for p in edl["pieces"]})
inputs = []
for c in clips:
    inputs += ["-i", str(WORK / "media" / f"{c}.mp4")]
idx = {c: i for i, c in enumerate(clips)}
parts, labels = [], []
for k, p in enumerate(edl["pieces"]):
    i = idx[p["clip"]]
    d = p["out"] - p["in"]
    f = min(0.008, d / 4)
    parts.append(f"[{i}:v]trim=start={p['in']}:end={p['out']},setpts=PTS-STARTPTS[v{k}]")
    parts.append(f"[{i}:a]atrim=start={p['in']}:end={p['out']},asetpts=PTS-STARTPTS,"
                 f"afade=t=in:d={f},afade=t=out:st={d - f:.4f}:d={f}[a{k}]")
    labels.append(f"[v{k}][a{k}]")
parts.append("".join(labels) + f"concat=n={len(labels)}:v=1:a=1[v][a]")
cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(parts),
       "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-r", "30",
       "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", "-ar", "48000", str(WORK / "aroll.mov")]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stderr[-3000:] if r.returncode else "aroll ok")
