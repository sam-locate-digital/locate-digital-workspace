"""Flag hidden repeats in a cut: Whisper stretches one word over a false start it doesn't write down.

Usage: python -I longwords.py <audio> [max_word_seconds]
"""
import sys

import whisper

limit = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
m = whisper.load_model("small.en")
r = m.transcribe(sys.argv[1], fp16=False, language="en", word_timestamps=True, condition_on_previous_text=False)
print(r["text"].strip())
flags = 0
for s in r["segments"]:
    for w in s["words"]:
        d = w["end"] - w["start"]
        # money figures are long when spoken ("two hundred thousand"), so only flag ordinary words
        if d > limit and not any(ch.isdigit() for ch in w["word"]):
            flags += 1
            print(f"  LONG {w['word'].strip()!r} {w['start']:.2f}-{w['end']:.2f} ({d:.2f}s)")
print(f"{flags} long word(s)")
