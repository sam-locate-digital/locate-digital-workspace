"""Build the edit decision list: chosen takes -> pause-cut pieces -> output timeline + caption words.

Usage: python -I edl.py <work_dir>
Rule: no pause longer than 0.1 s survives (Sam's instruction for this reel).
"""
import json
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
data = json.loads((WORK / "clips.json").read_text(encoding="utf-8"))

MAX_GAP = 0.10   # longest pause allowed to remain
PAD_IN = 0.05    # keep a little air before a word's onset
PAD_OUT = 0.07   # and after its tail
SIL_KEEP = 0.03  # when cutting a detected silence, leave this much each side
MIN_PIECE = 0.08

# (clip, source range start, end, beat label)
SELECT = [
    ("IMG_1923", 0.0, 4.6, "hook"),
    ("IMG_1923", 4.9, 6.2, "receipts"),
    ("IMG_1926", 6.85, 10.3, "auto1"),
    ("IMG_1928", 10.7, 12.7, "auto2"),
    ("IMG_1928", 13.5, 15.6, "auto3"),
    ("IMG_1928", 33.4, 36.75, "total"),
    ("IMG_1935", 0.9, 3.97, "how"),
    ("IMG_1932", 15.0, 19.3, "step1"),
    ("IMG_1932", 22.3, 26.6, "step1b"),
    ("IMG_1932", 26.7, 29.5, "step1c"),
    ("IMG_1932", 33.85, 35.95, "step2"),
    ("IMG_1932", 41.6, 43.2, "comments"),
    ("IMG_1932", 44.6, 49.0, "step3"),
    ("IMG_1934", 11.75, 18.6, "step4"),
    ("IMG_1932", 49.2, 50.6, "outro"),
]

# Caption text fixes (spoken form -> caption form). Digits for numbers, product names spelled right.
FIX = {"three": "3", "six": "6", "two": "2", "12": "12"}


# Word timings re-measured on a short slice where the full-clip pass merged two takes
OVERRIDE = {
    ("IMG_1932", 15.0): [
        ("First", 15.18, 15.56), ("off,", 15.56, 15.76), ("you're", 15.84, 15.90), ("gonna", 15.90, 16.10),
        ("need", 16.10, 16.34), ("a", 16.34, 16.36), ("CRM", 16.36, 16.70), ("that", 16.70, 16.94),
        ("triggers", 16.94, 17.16), ("these", 17.16, 17.34), ("automations", 17.34, 17.82), ("based", 17.82, 18.06),
        ("off", 18.06, 18.32), ("the", 18.32, 18.46), ("last", 18.46, 18.66), ("visit.", 18.66, 19.04),
    ],
    # v2: the full-clip pass hid false starts inside stretched words; these are the clean takes only
    ("IMG_1926", 6.85): [
        ("Here's", 6.97, 7.12), ("an", 7.12, 7.20), ("automation", 7.20, 7.46), ("that", 7.46, 7.74),
        ("triggers", 7.74, 8.00), ("to", 8.00, 8.22), ("customers", 8.22, 8.60), ("who", 8.60, 8.84),
        ("haven't", 8.84, 9.08), ("visited", 9.08, 9.30), ("in", 9.30, 9.54), ("the", 9.54, 9.56),
        ("last", 9.56, 9.72), ("three", 9.72, 9.90), ("months.", 9.90, 10.12),
    ],
    ("IMG_1928", 33.4): [
        ("These", 33.46, 33.60), ("three", 33.60, 33.78), ("automations", 33.78, 34.36), ("are", 34.36, 34.50),
        ("totalling", 34.50, 34.78), ("over", 34.78, 34.96), ("$200", 34.96, 35.34), (",000", 35.34, 35.90),
        ("this", 35.90, 36.12), ("year", 36.12, 36.34), ("alone.", 36.34, 36.66),
    ],
    ("IMG_1934", 11.75): [
        ("Make", 11.83, 11.92), ("sure", 11.92, 12.04), ("you", 12.04, 12.14), ("update", 12.14, 12.34),
        ("these", 12.34, 12.56), ("email", 12.56, 12.84), ("promotions", 12.84, 13.28), ("every", 13.28, 13.54),
        ("3", 13.54, 13.74), ("to", 13.74, 13.84), ("6", 13.84, 14.04), ("months", 14.04, 14.22),
        ("just", 14.22, 14.42), ("so", 14.42, 14.56), ("that", 14.56, 14.72), ("they", 14.72, 14.84),
        ("have", 14.84, 14.96), ("a", 14.96, 15.08), ("different", 15.08, 15.28), ("look", 15.28, 15.42),
        ("and", 15.42, 15.58), ("feel", 15.58, 15.78), ("or", 15.78, 16.24), ("offer", 16.24, 16.46),
        ("different", 16.46, 16.68), ("promotions", 16.68, 17.10), ("while", 17.10, 17.36), ("you're", 17.36, 17.52),
        ("at", 17.52, 17.64), ("it.", 17.64, 17.94),
    ],
    ("IMG_1932", 33.85): [
        ("Then", 33.87, 34.16), ("you're", 34.16, 34.38), ("going", 34.38, 34.54), ("to", 34.54, 34.68),
        ("code", 34.68, 34.90), ("and", 34.90, 35.06), ("type", 35.06, 35.24), ("in", 35.24, 35.38),
        ("this", 35.38, 35.56), ("prompt.", 35.56, 35.86),
    ],
}


def words_in(clip, a, b):
    if (clip, a) in OVERRIDE:
        return [{"w": w, "s": s, "e": e, "p": 1.0} for w, s, e in OVERRIDE[(clip, a)]]
    return [w for w in data[clip]["words2"] if w["s"] >= a - 0.02 and w["e"] <= b + 0.25]


def subtract(intervals, cuts):
    out = []
    for s, e in intervals:
        segs = [(s, e)]
        for cs, ce in cuts:
            nxt = []
            for x, y in segs:
                if ce <= x or cs >= y:
                    nxt.append((x, y)); continue
                if cs > x: nxt.append((x, cs))
                if ce < y: nxt.append((ce, y))
            segs = nxt
        out.extend(segs)
    return [(s, e) for s, e in out if e - s >= MIN_PIECE]


pieces, captions, beats = [], [], []
t_out = 0.0
for clip, a, b, beat in SELECT:
    ws = words_in(clip, a, b)
    if not ws:
        print("no words for", clip, a, b); continue
    # 1. word islands, padded, merged where the gap is allowed
    islands = []
    for w in ws:
        s, e = max(a, w["s"] - PAD_IN), min(b, w["e"] + PAD_OUT)
        if islands and s - islands[-1][1] <= MAX_GAP:
            islands[-1][1] = max(islands[-1][1], e)
        else:
            islands.append([s, e])
    # 2. cut detected silences longer than MAX_GAP that fall inside the islands
    sil = [(s + SIL_KEEP, e - SIL_KEEP) for s, e in data[clip]["silences"] if e - s > MAX_GAP]
    keep = subtract([tuple(x) for x in islands], sil)
    beat_start = t_out
    sel_pieces = []
    for s, e in keep:
        p = {"clip": clip, "in": round(s, 3), "out": round(e, 3), "t": round(t_out, 3), "beat": beat}
        pieces.append(p); sel_pieces.append(p)
        t_out += e - s
    # map every word to the piece it overlaps most (or the nearest one), clamped inside that piece
    for w in ws:
        best, score = None, None
        for p in sel_pieces:
            ov = min(w["e"], p["out"]) - max(w["s"], p["in"])
            dist = 0 if ov > 0 else min(abs(w["s"] - p["out"]), abs(p["in"] - w["e"]))
            key = (ov if ov > 0 else -dist)
            if score is None or key > score:
                best, score = p, key
        p = best
        s_src = min(max(w["s"], p["in"]), p["out"])
        e_src = min(max(w["e"], p["in"]), p["out"])
        ws_s = p["t"] + (s_src - p["in"])
        ws_e = max(ws_s + 0.06, p["t"] + (e_src - p["in"]))
        captions.append({"w": FIX.get(w["w"].lower().strip(".,"), w["w"]), "s": round(ws_s, 3),
                         "e": round(ws_e, 3), "beat": beat})
    beats.append({"beat": beat, "start": round(beat_start, 3), "end": round(t_out, 3), "clip": clip,
                  "text": " ".join(w["w"] for w in ws)})

total = round(t_out, 3)
# merge "$200" + ",000"
merged = []
for c in captions:
    if merged and c["w"].startswith(",") and merged[-1]["w"].startswith("$"):
        merged[-1]["w"] += c["w"].rstrip("."); merged[-1]["e"] = c["e"]
    else:
        merged.append(c)
(WORK / "edl.json").write_text(json.dumps({"total": total, "pieces": pieces, "beats": beats, "words": merged},
                                          indent=1, ensure_ascii=False), encoding="utf-8")
print(f"total {total:.2f}s | pieces {len(pieces)} | words {len(merged)}")
for bt in beats:
    print(f"{bt['start']:6.2f}-{bt['end']:6.2f} {bt['beat']:9s} {bt['text']}")
gaps = [p for p in pieces if p["out"] - p["in"] < 0.3]
print("short pieces (<0.3s):", len(gaps))
