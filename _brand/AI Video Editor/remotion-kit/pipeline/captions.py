"""Turn the EDL word list into caption cues (1–3 words, emphasis cues with a setup line).

Usage: python -I captions.py <work_dir> <out_json>
"""
import json
import re
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
OUT = Path(sys.argv[2])
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
END_CARD = round(edl["total"], 3)       # speech ends here
TOTAL = round(END_CARD + 0.3, 3)        # v2: no end card, just a short tail after the last word
BRANDS = {"GoHighLevel": "highlevel", "Claude": "claude"}  # spoken brand names become logo cues

# Confirmed fixes and house style (Australian spelling, digits, product names)
REPLACE = {"code": "Claude", "totaling": "totalling", "two": "2", "three": "3", "six": "6"}

words = []
for w in edl["words"]:
    txt = w["w"].strip()
    core = txt.strip(".,?")
    if core.lower() in REPLACE:
        txt = txt.replace(core, REPLACE[core.lower()])
    words.append({**w, "w": txt})

# merge "high" + "level." -> "GoHighLevel" (spoken as "go high level")
merged = []
for w in words:
    if merged and w["w"].lower().startswith("level") and merged[-1]["w"].lower() == "high":
        prev = merged.pop()
        if merged and merged[-1]["w"].lower() == "go":
            prev = merged.pop() | {"e": prev["e"]}
        merged.append({**prev, "w": "GoHighLevel" + w["w"][5:], "e": w["e"]})
    else:
        merged.append(w)
words = merged

# Sentence case: capitalise the first word of each sentence (start, or after a full stop / new take)
prev_beat = None
for k, w in enumerate(words):
    starts_sentence = k == 0 or words[k - 1]["w"].endswith((".", "?")) or w["beat"] != prev_beat
    if starts_sentence and w["w"][:1].islower():
        w["w"] = w["w"][0].upper() + w["w"][1:]
    prev_beat = w["beat"]


def clean(t):
    return re.sub(r"[.,]+$", "", t)


UNITS = {"months", "month", "hours", "hour", "days", "weeks", "years"}


def is_num(t):
    return bool(re.fullmatch(r"\$?[\d,]+", clean(t)))


# Emphasis: (beat, emphasis words, number of setup words before them)
EMPH = [("hook", ["$200,000"], 2), ("how", ["2", "hours"], 1),
        ("step1b", ["best", "practice"], 1), ("comments", ["in", "the", "comments"], 3),
        ("step4", ["3", "to", "6", "months"], 1)]

starts = {}
for beat, em, n_setup in EMPH:
    for i in range(len(words)):
        seq = [clean(x["w"]).lower() for x in words[i + n_setup:i + n_setup + len(em)]]
        if words[i]["beat"] == beat and seq == [e.lower() for e in em]:
            starts[i] = (n_setup, len(em))
            break
    else:
        print("emphasis not found:", beat, em)

cues, i = [], 0
while i < len(words):
    if i in starts:
        n_setup, n_em = starts[i]
        setup = words[i:i + n_setup]
        em = words[i + n_setup:i + n_setup + n_em]
        cues.append({"s": setup[0]["s"], "setup": " ".join(clean(x["w"]) for x in setup),
                     "em": " ".join(clean(x["w"]) for x in em), "emAt": em[0]["s"]})
        i += n_setup + n_em
        continue
    if clean(words[i]["w"]) in BRANDS:
        name = clean(words[i]["w"])
        cues.append({"s": words[i]["s"], "text": name, "logo": BRANDS[name]})
        i += 1
        continue
    chunk = [words[i]]
    j = i + 1
    while j < len(words) and len(chunk) < 3 and j not in starts and clean(words[j]["w"]) not in BRANDS:
        prev = chunk[-1]["w"]
        if prev.endswith((".", ",", "?")):
            break
        # a money figure closes its chunk ("over $200,000" / "this year alone")
        if prev.startswith("$"):
            break
        # keep a number with its unit: don't start "3" as the last slot when "months" follows
        in_range = len(chunk) == 2 and is_num(chunk[0]["w"]) and clean(chunk[1]["w"]).lower() == "to"
        if (len(chunk) == 2 and not in_range and is_num(words[j]["w"]) and j + 1 < len(words)
                and clean(words[j + 1]["w"]).lower() in UNITS | {"to"}):
            break
        # a unit closes its chunk ("3 to 6 months" / "just so that")
        if clean(prev).lower() in UNITS:
            break
        nxt = " ".join(clean(x["w"]) for x in chunk + [words[j]])
        if len(nxt) > 18:
            break
        chunk.append(words[j]); j += 1
    cues.append({"s": chunk[0]["s"], "text": " ".join(clean(x["w"]) for x in chunk)})
    i = j

# Fold one-word flashes (< 0.3 s on screen) into the plain cue before them, up to 22 characters
folded = []
for k, c in enumerate(cues):
    nxt = cues[k + 1]["s"] if k + 1 < len(cues) else END_CARD
    prev = folded[-1] if folded else None
    if (prev and "text" in c and "logo" not in c and " " not in c["text"] and nxt - c["s"] < 0.3
            and "text" in prev and "logo" not in prev and len(prev["text"]) + 1 + len(c["text"]) <= 22):
        prev["text"] += " " + c["text"]
        continue
    folded.append(c)
cues = folded

for k, c in enumerate(cues):
    c["e"] = cues[k + 1]["s"] if k + 1 < len(cues) else TOTAL
    c["s"] = round(c["s"], 3); c["e"] = round(c["e"], 3)

OUT.write_text(json.dumps({"total": TOTAL, "endCard": END_CARD, "cues": cues}, indent=1, ensure_ascii=False),
               encoding="utf-8")
print(f"{len(cues)} cues, total {TOTAL}s, end card at {END_CARD}s")
for c in cues:
    print(f"{c['s']:6.2f} {c.get('text') or (c['setup'] + ' / *' + c['em'] + '*')}")
