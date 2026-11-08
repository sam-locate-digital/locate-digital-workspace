"""Build the Remotion timeline from the cut (edl.json) and the graphics plan (plan.json), and check it.

Usage: python -I timeline.py <work_dir>
Reads <work_dir>/edl.json, <work_dir>/plan.json (see examples/plan.json) and, if plan zooms is "auto",
zooms_suggested.json. Writes <work_dir>/remotion/src/timeline.json and prints the beat list and any problems.

Times in plan.json can be written as:
  12.5                    seconds in the cut
  "section:s2"            start of a section (from select.json); "end:s2" for its end; add "+1.5" or "-0.5"
  "inbox@40"              the first time the word "inbox" (or a phrase: "your inbox@40") is said at or after 40 s
"""
import json
import re
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
plan = json.loads((WORK / "plan.json").read_text(encoding="utf-8"))
PUBLIC = WORK / "remotion" / "public"
OUT = WORK / "remotion" / "src" / "timeline.json"
TOTAL = edl["total"]
words = edl["words"]
sections = {s["name"]: s for s in edl["sections"]}
problems = []


def norm(w):
    return re.sub(r"[^a-z0-9$%']", "", w.lower())


def resolve(spec, what=""):
    if isinstance(spec, (int, float)):
        return float(spec)
    m = re.match(r"^(section|end):(.+?)([+-][\d.]+)?$", spec)
    if m:
        sec = sections.get(m.group(2))
        if not sec:
            problems.append(f"{what}: no section named {m.group(2)!r}"); return 0.0
        return (sec["s"] if m.group(1) == "section" else sec["e"]) + float(m.group(3) or 0)
    m = re.match(r"^(.+?)@([\d.]+)([+-][\d.]+)?$", spec)
    if m:
        target = [norm(x) for x in m.group(1).split()]
        after = float(m.group(2))
        for i, w in enumerate(words):
            if w["s"] >= after and [norm(x["w"]) for x in words[i:i + len(target)]] == target:
                return w["s"] + float(m.group(3) or 0)
        problems.append(f"{what}: {m.group(1)!r} isn't said after {after}s"); return after
    problems.append(f"{what}: can't read time {spec!r}"); return 0.0


def span(item, what, dur):
    s = resolve(item.get("at", item.get("s", 0)), what)
    e = resolve(item["e"], what) if "e" in item else s + item.get("dur", dur)
    if e > TOTAL + 0.01 or s < 0:
        problems.append(f"{what}: {s:.2f}-{e:.2f} runs outside the cut (0-{TOTAL:.2f})")
    return round(s, 3), round(min(e, TOTAL), 3)


segments = [{k: v for k, v in s.items() if k != "clip"} for s in edl["segments"]]


def seg_at(t):
    for s in segments:
        if s["s"] <= t < s["e"]:
            return s
    return segments[-1]


# full-frame cards: lesson title, chapter cards, points/statement cards
full = []
intro = None
if plan.get("intro"):
    it = plan["intro"]
    s, e = span(it, "intro", 3.2)
    intro = {"s": s, "e": e, "title": plan.get("title", ""), "kicker": plan.get("kicker", ""), "sub": it.get("sub", ""),
             "em": it.get("em", "")}
    full.append(("intro", s, e))
chapters = []
for i, ch in enumerate(plan.get("chapters", [])):
    what = f"chapter {i + 1}"
    at = ch.get("at", f"section:{ch['section']}") if "section" in ch or "at" in ch else 0
    s, e = span({**ch, "at": at}, what, 2.6)
    chapters.append({"s": s, "e": e, "n": i + 1, "title": ch["title"], "em": ch.get("em", "")})
    full.append((what, s, e))
for c in chapters:
    c["count"] = len(chapters)
cards = []
for i, c in enumerate(plan.get("cards", [])):
    what = f"card {i + 1}"
    s, e = span(c, what, 5)
    card = {**{k: v for k, v in c.items() if k not in ("at", "dur")}, "s": s, "e": e}
    if c.get("items"):
        card["items"] = [{"text": it["text"] if isinstance(it, dict) else it,
                          "at": round(resolve(it.get("at"), what) if isinstance(it, dict) and it.get("at") else s + 0.5 + 0.6 * k, 3)}
                         for k, it in enumerate(c["items"])]
    cards.append(card)
    full.append((what, s, e))
full.sort(key=lambda x: x[1])
for (n1, s1, e1), (n2, s2, e2) in zip(full, full[1:]):
    if s2 < e1 - 0.01:
        problems.append(f"{n1} ({s1:.2f}-{e1:.2f}) overlaps {n2} ({s2:.2f}-{e2:.2f})")

splits = []
for i, sp in enumerate(plan.get("splits", [])):
    what = f"split {i + 1}"
    s, e = span(sp, what, 6)
    if seg_at(s)["kind"] != "face" or seg_at(max(s, e - 0.05))["kind"] != "face":
        problems.append(f"{what} ({s:.2f}-{e:.2f}) isn't all on face footage: splits need you on camera")
    panel = sp.get("panel", {})
    if panel.get("items"):
        panel["items"] = [{"text": it["text"] if isinstance(it, dict) else it,
                           "at": round(resolve(it.get("at"), what) if isinstance(it, dict) and it.get("at") else s + 0.5 + 0.7 * k, 3)}
                          for k, it in enumerate(panel["items"])]
    if panel.get("kind") == "image" and not (PUBLIC / panel.get("src", "")).exists():
        problems.append(f"{what}: image public/{panel.get('src')} not found")
    splits.append({"s": s, "e": e, "side": sp.get("side", "right"), "panel": panel})

labels = []
for i, lb in enumerate(plan.get("labels", [])):
    what = f"label {lb.get('text', i)}"
    s, e = span(lb, what, 4)
    if lb.get("logo") and not (PUBLIC / "logos" / f"{lb['logo']}-mark.svg").exists():
        problems.append(f"{what}: no logo public/logos/{lb['logo']}-mark.svg (add the brand's real mark, and its tile "
                        f"colour to TILE_BG in tkit.jsx if it isn't white)")
    labels.append({"s": s, "e": e, "text": lb["text"], "sub": lb.get("sub", ""), "logo": lb.get("logo", "")})
for a, b in zip(labels, labels[1:]):
    if b["s"] < a["e"]:
        problems.append(f"labels {a['text']!r} and {b['text']!r} overlap")


def covered(t):
    return any(s <= t < e for _, s, e in full) or any(sp["s"] <= t < sp["e"] for sp in splits)


# face shots: alternate wide and punch-in at natural breaks, every face.min-face.max seconds
fc = {"min": 5.0, "max": 11.0, **plan.get("face", {})}
breaks = sorted({round(w["e"], 3) for i, w in enumerate(words[:-1])
                 if words[i + 1]["s"] - w["e"] >= 0.15 or w["w"].endswith((".", "?", "!", ","))})
shots = []
for seg in [s for s in segments if s["kind"] == "face"]:
    t, mode = seg["s"], "wide"
    while t < seg["e"] - 0.01:
        cands = [b for b in breaks if t + fc["min"] <= b <= min(t + fc["max"], seg["e"] - 2)]
        nxt = cands[0] if cands else (seg["e"] if seg["e"] - t <= fc["max"] + 2 else t + fc["max"])
        nxt = min(nxt, seg["e"])
        shots.append({"s": round(t, 3), "e": round(nxt, 3), "mode": mode})
        t, mode = nxt, ("punch" if mode == "wide" else "wide")

# screen camera: keyframes per screen segment from the zooms
zooms = plan.get("zooms", [])
if zooms == "auto":
    p = WORK / "zooms_suggested.json"
    zooms = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
zooms = sorted(({**z, "s": resolve(z.get("at", z.get("s")), "zoom"), "e": resolve(z["e"], "zoom") if "e" in z else
                 resolve(z.get("at", z.get("s")), "zoom") + z.get("dur", 3)} for z in zooms), key=lambda z: z["s"])
IN, OUTT = 0.8, 0.7
cam = []
for si, seg in enumerate(segments):
    if seg["kind"] != "screen":
        continue
    zs = [z for z in zooms if seg["s"] <= z["s"] < seg["e"]]
    for z in zooms:
        if z["s"] < seg["e"] and z["e"] > seg["s"] and z not in zs:
            problems.append(f"zoom {z['s']:.2f}-{z['e']:.2f} starts outside a screen segment")
    kf = [{"t": seg["s"], "z": 1, "x": 0.5, "y": 0.5}]
    for k, z in enumerate(zs):
        e = min(z["e"], seg["e"])
        zin = min(IN, (e - z["s"]) / 3)
        st = {"z": round(float(z["z"]), 3), "x": round(float(z["x"]), 3), "y": round(float(z["y"]), 3)}
        if kf[-1]["t"] < z["s"] - 0.01:
            kf.append({"t": round(z["s"], 3), **{k2: kf[-1][k2] for k2 in ("z", "x", "y")}})
        kf.append({"t": round(z["s"] + zin, 3), **st})
        nxt = zs[k + 1]["s"] if k + 1 < len(zs) else None
        if nxt is not None and nxt - e < 1.2:
            kf.append({"t": round(max(e - 0.05, z["s"] + zin + 0.05), 3), **st})   # hold, then pan straight to the next
        else:
            kf.append({"t": round(max(e - OUTT, z["s"] + zin + 0.05), 3), **st})
            kf.append({"t": round(e, 3), "z": 1, "x": 0.5, "y": 0.5})
        if e - z["s"] < 1.8:
            problems.append(f"zoom {z['s']:.2f}-{e:.2f} is under 1.8 s: it will feel jumpy")
    kf.append({"t": seg["e"], "z": 1, "x": 0.5, "y": 0.5})
    cam.append({"seg": si, "keys": kf})

end = None
if plan.get("end"):
    end = {**plan["end"], "s": TOTAL, "e": round(TOTAL + plan["end"].get("dur", 4.0), 3)}
length = end["e"] if end else TOTAL

tl = {"fps": edl["fps"], "total": TOTAL, "length": length, "title": plan.get("title", ""), "kicker": plan.get("kicker", ""),
      "segments": segments, "shots": shots, "cam": cam, "labels": labels, "chapters": chapters, "intro": intro,
      "cards": cards, "splits": splits, "end": end, "sections": edl["sections"], "music": plan.get("music", "bookends"),
      "face": {"punch": fc.get("punch", 1.14), "fx": fc.get("fx", 0.5), "fy": fc.get("fy", 0.4)},
      "screen": {"inset": plan.get("screen", {}).get("inset", 0.9)}}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(tl, indent=1, ensure_ascii=False), encoding="utf-8")

beats = ([(intro["s"], intro["e"], "TITLE", intro["title"])] if intro else []) + \
        [(c["s"], c["e"], "CHAPTER", f"{c['n']}. {c['title']}") for c in chapters] + \
        [(c["s"], c["e"], "CARD", c.get("title") or c.get("text", "")) for c in cards] + \
        [(s["s"], s["e"], "SPLIT", s["panel"].get("title") or s["panel"].get("text") or s["panel"].get("label") or s["panel"].get("src", "")) for s in splits] + \
        [(l["s"], l["e"], "LABEL", l["text"]) for l in labels] + \
        [(z["s"], z["e"], "ZOOM", f"x{z['x']:.2f} y{z['y']:.2f} z{z['z']}") for z in zooms]
print(f"length {int(length // 60)}:{length % 60:05.2f} | {len(segments)} segments | {len(shots)} face shots | "
      f"{len(zooms)} zooms | {len(labels)} labels | {len(chapters)} chapters | {len(cards)} cards | {len(splits)} splits")
for s, e, kind, text in sorted(beats):
    print(f"  {int(s // 60)}:{s % 60:05.2f}-{int(e // 60)}:{e % 60:05.2f}  {kind:8s} {text}")
# longest stretch with nothing changing on screen (no cut, card, label or zoom start)
marks = sorted({0.0, TOTAL} | {x["s"] for x in shots} | {s["s"] for s in segments} | {b[0] for b in beats} | {b[1] for b in beats})
still = max(((b - a), a) for a, b in zip(marks, marks[1:]))
print(f"longest unchanged stretch: {still[0]:.1f}s at {int(still[1] // 60)}:{still[1] % 60:05.2f}")
print("\n".join("PROBLEM: " + p for p in problems) if problems else "no problems")
