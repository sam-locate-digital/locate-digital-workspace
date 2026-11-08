"""Check the base cut: re-transcribe it and flag repeats, stretched words and leftover pauses.

Usage: python -I check_cut.py <work_dir> [--max-pause 0.7]

Prints the cut's transcript in timed lines (base time), then:
  REPEAT    the same 4 words twice within 20 s: a retake that survived
  LONG      an ordinary word over 0.6 s: often a hidden false start (check it with segwords.py on the source)
  PAUSE     a silence longer than --max-pause that isn't a sped-up stretch
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import whisper

WORK = Path(sys.argv[1])
MAXP = float(sys.argv[sys.argv.index("--max-pause") + 1]) if "--max-pause" in sys.argv else 0.7
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
fast = [(p["t"], p["t"] + p["frames"] / edl["fps"]) for p in edl["pieces"] if p["speed"] != 1]

m = whisper.load_model("small.en")
res = m.transcribe(str(WORK / "base.wav"), word_timestamps=True, fp16=False, language="en",
                   condition_on_previous_text=False, verbose=None)
words = [{"w": w["word"].strip(), "s": w["start"], "e": w["end"]} for s in res["segments"] for w in s.get("words", [])]
(WORK / "cut_words.json").write_text(json.dumps(words, indent=0), encoding="utf-8")


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


line, issues = [], []
for i, w in enumerate(words):
    if line and (w["s"] - line[-1]["e"] > 0.5 or line[-1]["w"].endswith((".", "?", "!"))):
        print(f"[{line[0]['s']:7.2f}] " + " ".join(x["w"] for x in line)); line = []
    line.append(w)
if line:
    print(f"[{line[0]['s']:7.2f}] " + " ".join(x["w"] for x in line))

seen = {}
for i in range(len(words) - 3):
    gram = tuple(norm(w["w"]) for w in words[i:i + 4])
    if gram in seen and words[i]["s"] - seen[gram] < 20:
        issues.append(f"REPEAT {words[i]['s']:7.2f}  \"{' '.join(w['w'] for w in words[i:i + 4])}\" (also at {seen[gram]:.2f})")
    seen[gram] = words[i]["s"]
for w in words:
    if w["e"] - w["s"] > 0.6 and len(norm(w["w"])) <= 8:
        issues.append(f"LONG   {w['s']:7.2f}  \"{w['w']}\" {w['e'] - w['s']:.2f}s")
sd = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(WORK / "base.wav"), "-af",
                     f"silencedetect=noise=-38dB:d={MAXP}", "-f", "null", "-"], capture_output=True, text=True).stderr
for s, e in zip(re.findall(r"silence_start: ([\d.]+)", sd), re.findall(r"silence_end: ([\d.]+)", sd)):
    s, e = float(s), float(e)
    if not any(a - 0.2 <= s and e <= b + 0.2 for a, b in fast):
        issues.append(f"PAUSE  {s:7.2f}  {e - s:.2f}s")
print("\n" + ("\n".join(sorted(issues, key=lambda x: float(x.split()[1]))) if issues else "no issues found"))
