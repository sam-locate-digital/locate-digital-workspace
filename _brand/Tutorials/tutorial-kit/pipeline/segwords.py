"""Transcribe a slice of a wav and print word timings in the source clip's time.

Usage: python -I segwords.py <wav> <start> <end>
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import whisper

wav, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
tmp = Path(tempfile.mkdtemp()) / "slice.wav"
subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(a), "-to", str(b), "-i", wav, str(tmp)],
               check=True)
m = whisper.load_model("small.en")
r = m.transcribe(str(tmp), fp16=False, language="en", word_timestamps=True, condition_on_previous_text=False)
for s in r["segments"]:
    print(" ".join(f"{w['word'].strip()}@{w['start'] + a:.2f}-{w['end'] + a:.2f}" for w in s["words"]))
sd = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(tmp), "-af", "silencedetect=noise=-38dB:d=0.1", "-f", "null", "-"],
                    capture_output=True, text=True).stderr
import re
st = [float(x) + a for x in re.findall(r"silence_start: (-?[\d.]+)", sd)]
en = [float(x) + a for x in re.findall(r"silence_end: ([\d.]+)", sd)]
print("silences:", " ".join(f"{s:.2f}-{e:.2f}" for s, e in zip(st, en)))
