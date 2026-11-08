"""Print each clip's transcript as timed lines, so takes and mistakes are easy to spot. Also writes lines.txt.

Usage: python -I lines.py <work_dir> [clip_id]

A new line starts at a pause of 0.6 s or more, or at a sentence end followed by 0.25 s or more.
Flags:
  RETAKE?  the line starts like one of the previous few lines (a restart), so the earlier one is probably dead
  AGAIN    the line has "again", "redo", "let me try" or "take two": the speaker marked a mistake
  (gap)    a silence of 3 s or more before the line, shown on screen pieces as something to speed up or cut
"""
import json
import re
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
ONLY = sys.argv[2] if len(sys.argv) > 2 else None
data = json.loads((WORK / "clips.json").read_text(encoding="utf-8"))
MARK = re.compile(r"\b(again|redo|re-do|let me try|take two|start over|scratch that)\b", re.I)


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


def lines_for(words):
    out, cur = [], []
    for i, w in enumerate(words):
        if cur:
            gap = w["s"] - cur[-1]["e"]
            if gap >= 0.6 or (cur[-1]["w"].endswith((".", "?", "!")) and gap >= 0.25):
                out.append(cur); cur = []
        cur.append(w)
    if cur:
        out.append(cur)
    return out


report = []
for cid, info in data.items():
    if ONLY and cid != ONLY:
        continue
    words = info.get("words") or []
    report.append(f"== {cid} ({info['kind']}, {info['duration']:.1f}s)")
    prev = []
    last_end = 0.0
    for ln in lines_for(words):
        text = " ".join(w["w"] for w in ln)
        key = [norm(w["w"]) for w in ln[:3]]
        flags = []
        if len(key) >= 2 and any(p[:len(key)] == key for p in prev[-6:]):
            flags.append("RETAKE?")
        if MARK.search(text):
            flags.append("AGAIN")
        if ln[0]["s"] - last_end >= 3:
            flags.append(f"(gap {ln[0]['s'] - last_end:.1f}s)")
        low = [w["w"] for w in ln if w["p"] < 0.5]
        if low:
            flags.append("unsure: " + ", ".join(low[:4]))
        report.append(f"  [{ln[0]['s']:7.2f}-{ln[-1]['e']:7.2f}] {text}" + (f"   << {' | '.join(flags)}" if flags else ""))
        prev.append(key)
        last_end = ln[-1]["e"]
    if info.get("duration", 0) - last_end >= 3:
        report.append(f"  (silent tail {info['duration'] - last_end:.1f}s)")
txt = "\n".join(report)
(WORK / "lines.txt").write_text(txt + "\n", encoding="utf-8")
print(txt)
