"""Re-transcribe with domain hints and print a word timeline per clip.

Usage: python -I retranscribe.py <work_dir>
"""
import json
import sys
from pathlib import Path

import whisper

WORK = Path(sys.argv[1])
data = json.loads((WORK / "clips.json").read_text(encoding="utf-8"))
model = whisper.load_model("small.en")
HINT = ("A business owner explains marketing automations in GoHighLevel, a CRM. "
        "Email campaigns trigger for patients who haven't visited in three, six or 12 months. "
        "Open Claude and type in this prompt. The prompt is in the comments. $200,000.")
for stem in data:
    res = model.transcribe(str(WORK / "media" / f"{stem}.wav"), word_timestamps=True, fp16=False, language="en",
                           initial_prompt=HINT, condition_on_previous_text=False, verbose=None)
    words = [{"w": w["word"].strip(), "s": round(w["start"], 3), "e": round(w["end"], 3),
              "p": round(w.get("probability", 0), 2)} for s in res["segments"] for w in s.get("words", [])]
    data[stem]["text2"] = res["text"].strip()
    data[stem]["words2"] = words
    print(f"== {stem}")
    print("  ", res["text"].strip())
    line = []
    for w in words:
        line.append(f"{w['w']}@{w['s']:.2f}" + ("?" if w["p"] < 0.5 else ""))
    print("   " + " ".join(line))
(WORK / "clips.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
