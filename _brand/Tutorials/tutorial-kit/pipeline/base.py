"""Cut the base video (2560x1440, 30 fps) and the voice track from edl.json.

Usage: python -I base.py <work_dir> [--jobs 4]
Writes <work_dir>/base.mp4 (no audio) and base.wav (48 kHz mono voice, exactly as long as the video).

Each piece is encoded on its own and cached in <work_dir>/pieces/ under a name made from its settings, so after a
change to select.json only the changed pieces are re-encoded. Screen pieces are scaled into the 2560x1440 frame and
padded with black; Remotion only ever shows the box inside the padding.
"""
import hashlib
import json
import subprocess
import sys
import wave
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

WORK = Path(sys.argv[1])
JOBS = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 4
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
FPS, SR = edl["fps"], 48000
SPF = SR // FPS  # audio samples per video frame
PIECES = WORK / "pieces"
PIECES.mkdir(exist_ok=True)
box_of = {}
for seg in edl["segments"]:
    if seg["kind"] == "screen":
        box_of[seg["clip"]] = seg["box"]


def encode(p):
    box = box_of.get(p["clip"])
    key = json.dumps([p["clip"], p["in"], p["out"], p["speed"], p["frames"], box])
    out = PIECES / (hashlib.sha1(key.encode()).hexdigest()[:16] + ".mp4")
    if out.exists():
        return out
    vf = []
    if p["speed"] != 1.0:
        vf += [f"setpts=PTS/{p['speed']}", f"fps={FPS}"]
    if box:
        x, y, w, h = box
        vf += [f"scale={w}:{h}:flags=lanczos", f"pad=2560:1440:{x}:{y}:black"]
    vf += ["setsar=1", "format=yuv420p"]
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{p['in']:.4f}"]
    if p["speed"] != 1.0:
        cmd += ["-t", f"{p['out'] - p['in'] + 0.2:.4f}"]
    cmd += ["-i", str(WORK / "media" / f"{p['clip']}.mp4"), "-frames:v", str(p["frames"]), "-vf", ",".join(vf),
            "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "15", "-g", "30", "-an",
            str(out.with_suffix(".tmp.mp4"))]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-1500:])
    out.with_suffix(".tmp.mp4").replace(out)
    return out


def read_wav(path):
    with wave.open(str(path), "rb") as w:
        assert w.getframerate() == SR and w.getnchannels() == 1, f"{path} must be 48 kHz mono"
        return np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768


with ThreadPoolExecutor(JOBS) as ex:
    files = list(ex.map(encode, edl["pieces"]))
lst = WORK / "pieces.txt"
lst.write_text("".join(f"file '{f.as_posix()}'\n" for f in files), encoding="utf-8")
r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", "-movflags", "+faststart", str(WORK / "base.mp4")], capture_output=True, text=True)
if r.returncode:
    sys.exit(r.stderr[-2000:])

# Voice: exact sample counts per piece, 8 ms fades at every join so cuts don't click. Sped-up pieces are silent.
cache, parts = {}, []
for p in edl["pieces"]:
    n = p["frames"] * SPF
    if p["speed"] != 1.0:
        parts.append(np.zeros(n, np.float32)); continue
    if p["clip"] not in cache:
        cache[p["clip"]] = read_wav(WORK / "media" / f"{p['clip']}.wav")
    src = cache[p["clip"]]
    i = round(p["in"] * SR)
    seg = src[i:i + n].copy()
    if len(seg) < n:
        seg = np.pad(seg, (0, n - len(seg)))
    f = min(int(0.008 * SR), n // 4)
    seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    parts.append(seg)
voice = np.concatenate(parts)
with wave.open(str(WORK / "base.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(voice, -1, 1) * 32767).astype("<i2").tobytes())

# Remotion reads the cut from remotion/public/base.mp4: hard-link it there (same drive, no copy), or copy if it can't
pub = WORK / "remotion" / "public"
if pub.is_dir():
    dst = pub / "base.mp4"
    dst.unlink(missing_ok=True)
    try:
        import os
        os.link(WORK / "base.mp4", dst)
    except OSError:
        import shutil
        shutil.copyfile(WORK / "base.mp4", dst)

probe = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                        "stream=nb_read_frames", "-of", "csv=p=0", str(WORK / "base.mp4")], capture_output=True, text=True)
got = int(probe.stdout.strip() or 0)
print(f"base.mp4 {got} frames (expected {edl['frames']}), base.wav {len(voice) / SR:.2f}s"
      + ("" if got == edl["frames"] else "  << FRAME COUNT MISMATCH"))
