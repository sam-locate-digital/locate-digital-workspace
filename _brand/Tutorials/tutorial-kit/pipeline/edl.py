"""Turn the chosen takes into a frame-exact edit decision list for the base cut.

Usage: python -I edl.py <work_dir>
Reads <work_dir>/select.json (see examples/select.json) and clips.json. Writes edl.json.

select.json:
  max_gap      longest pause left in, per kind ({"face": 0.3, "screen": 0.6})
  select       the takes in story order. Each: clip, in, out (source seconds), section, plus optional
                 cut   [[a, b], ...]       source ranges to remove (a fluffed step, a client name on screen)
                 keep  [[a, b], ...]       ranges kept whole even when silent (a result appearing)
                 fast  [[a, b, speed]]     silent stretches sped up (typing, loading); their audio is dropped
                 gap   number              this take's own max pause
  override     {"<clip>@<in>": [[word, start, end], ...]}  word timings for a take Whisper got wrong

Times are snapped to the 30 fps frame grid, so the cut video and voice stay in sync over any length.
"""
import json
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
FPS = 30
clips = json.loads((WORK / "clips.json").read_text(encoding="utf-8"))
cfg = json.loads((WORK / "select.json").read_text(encoding="utf-8"))
MAX_GAP = {"face": 0.3, "screen": 0.6, **cfg.get("max_gap", {})}
PAD_IN, PAD_OUT = 0.08, 0.12   # air kept before a word's onset and after its tail
SIL_KEEP = 0.04                # when cutting a silence, leave this much each side
MIN_PIECE = 0.1


def snap(t):
    return round(t * FPS) / FPS


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


def union(intervals):
    out = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [tuple(x) for x in out]


pieces, words_out, sections = [], [], []
frame = 0  # running position in the base, in frames
for sel in cfg["select"]:
    cid = sel["clip"]
    info = clips[cid]
    kind = info["kind"]
    a, b = sel["in"], min(sel["out"], info["duration"])
    gap = sel.get("gap", MAX_GAP[kind])
    key = f"{cid}@{sel['in']}"
    if key in cfg.get("override", {}):
        ws = [{"w": w, "s": s, "e": e, "p": 1.0} for w, s, e in cfg["override"][key]]
    else:
        ws = [w for w in info.get("words", []) if w["s"] >= a - 0.02 and w["e"] <= b + 0.25]
    cuts = [tuple(c) for c in sel.get("cut", [])]
    fast = [tuple(f) for f in sel.get("fast", [])]
    # 1. word islands, padded and merged where the pause is allowed
    islands = []
    for w in ws:
        s, e = max(a, w["s"] - PAD_IN), min(b, w["e"] + PAD_OUT)
        if islands and s - islands[-1][1] <= gap:
            islands[-1][1] = max(islands[-1][1], e)
        else:
            islands.append([s, e])
    # 2. cut detected silences longer than the gap inside the islands, add keep ranges, remove cut and fast ranges
    sil = [(s + SIL_KEEP, e - SIL_KEEP) for s, e in info["silences"] if e - s > gap]
    normal = subtract([tuple(x) for x in islands], sil)
    normal = union(normal + [(max(a, s), min(b, e)) for s, e in sel.get("keep", [])])
    normal = subtract(normal, cuts + [(f[0], f[1]) for f in fast])
    plan = [(s, e, 1.0) for s, e in normal] + [(max(a, f[0]), min(b, f[1]), float(f[2])) for f in fast]
    plan.sort()
    sec_start = frame
    placed = set()
    for s, e, speed in plan:
        fin, fout = round(s * FPS), round(e * FPS)
        n = round((fout - fin) / speed)
        if n < 2:
            continue
        p = {"clip": cid, "kind": kind, "in": fin / FPS, "out": fout / FPS, "speed": speed,
             "t": frame / FPS, "frames": n, "section": sel.get("section", "")}
        pieces.append(p)
        if speed == 1.0:
            # a word joins the first piece it overlaps (Whisper often stretches a first word over the silence
            # before it, so its midpoint can fall in a cut part), clamped inside that piece
            for w in ws:
                if id(w) in placed or min(w["e"], p["out"]) - max(w["s"], p["in"]) <= 0.02:
                    continue
                placed.add(id(w))
                ts = p["t"] + max(0.0, w["s"] - p["in"])
                te = min(p["t"] + n / FPS, p["t"] + (w["e"] - p["in"]))
                txt = w["w"]
                if words_out and txt.startswith(",") and txt[1:4].isdigit() and words_out[-1]["w"][-1:].isdigit():
                    words_out[-1]["w"] += txt; words_out[-1]["e"] = round(max(te, ts + 0.05), 3)   # "$200" ",000"
                    continue
                words_out.append({"w": txt, "s": round(ts, 3), "e": round(max(te, ts + 0.05), 3)})
        frame += n
    name = sel.get("section", "")
    if sections and sections[-1]["name"] == name:
        sections[-1]["e"] = frame / FPS
    else:
        sections.append({"name": name, "s": sec_start / FPS, "e": frame / FPS})

# segments: runs of the same clip, with the screen's picture box inside the 2560x1440 base
segments = []
for p in pieces:
    if segments and segments[-1]["clip"] == p["clip"] and abs(segments[-1]["e"] - p["t"]) < 1e-3:
        segments[-1]["e"] = round(p["t"] + p["frames"] / FPS, 4)
        continue
    info = clips[p["clip"]]
    seg = {"s": round(p["t"], 4), "e": round(p["t"] + p["frames"] / FPS, 4), "kind": p["kind"], "clip": p["clip"]}
    if p["kind"] == "screen":
        k = min(2560 / info["w"], 1440 / info["h"])
        w, h = int(info["w"] * k) // 2 * 2, int(info["h"] * k) // 2 * 2
        seg["box"] = [(2560 - w) // 2, (1440 - h) // 2, w, h]
    segments.append(seg)

total = frame / FPS
for s in sections:
    s["s"], s["e"] = round(s["s"], 4), round(s["e"], 4)
(WORK / "edl.json").write_text(json.dumps({"fps": FPS, "frames": frame, "total": round(total, 4), "pieces": pieces,
                                           "segments": segments, "sections": sections, "words": words_out},
                                          indent=1, ensure_ascii=False), encoding="utf-8")
fast_n = sum(1 for p in pieces if p["speed"] != 1)
print(f"total {int(total // 60)}:{total % 60:05.2f} | {len(pieces)} pieces ({fast_n} sped up) | "
      f"{len(segments)} segments | {len(words_out)} words")
for s in sections:
    print(f"  {s['s']:8.2f}-{s['e']:8.2f}  {s['name']}")
short = [p for p in pieces if p["frames"] < 9]
if short:
    print(f"note: {len(short)} pieces under 0.3 s (fine inside a sentence, odd at a section start)")
