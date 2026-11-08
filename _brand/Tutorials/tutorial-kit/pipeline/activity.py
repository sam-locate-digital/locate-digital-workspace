"""Suggest screen zooms by finding where the screen changes, and make contact sheets to check them by eye.

Usage: python -I activity.py <work_dir>
Writes:
  zooms_suggested.json   [{s, e, x, y, z, why}]: x, y = focus centre as a fraction of the screen box, z = zoom
  zooms.jpg              one frame per suggestion with the changed area boxed (number = index in the json)
  screens.jpg            every screen segment, one frame every 6 s, timestamped, to read what's on screen

How it works: the screen box of base.mp4 is sampled 4 times a second at 320 px wide. Areas that change (typing,
a menu opening, a result appearing) become candidate zooms; a change over 30% of the screen (a new page) ends one.
Tiny changes (the cursor moving) are ignored. These are suggestions: copy the good ones into plan.json "zooms",
fix the focus where the box is off, and drop any that would zoom on something unimportant.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

WORK = Path(sys.argv[1])
edl = json.loads((WORK / "edl.json").read_text(encoding="utf-8"))
RATE, W = 4, 320
BLOCK, THRESH = 4, 22
MIN_COMP = 4          # connected changed blocks needed to count (the cursor is about 2-4)
PAGE = 0.30           # changed share of the screen that means a new page
FILL = 0.60           # zoom so the changed area fills about this much of the frame
ZMIN, ZMAX = 1.3, 2.2


def frames(seg):
    x, y, w, h = seg["box"]
    hh = int(round(W * h / w / 2)) * 2
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{seg['s']:.3f}", "-to", f"{seg['e']:.3f}",
           "-i", str(WORK / "base.mp4"), "-vf", f"crop={w}:{h}:{x}:{y},scale={W}:{hh},fps={RATE},format=gray",
           "-f", "rawvideo", "-"]
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    size = W * hh
    i = 0
    while True:
        buf = pr.stdout.read(size)
        if len(buf) < size:
            break
        yield seg["s"] + i / RATE, np.frombuffer(buf, np.uint8).reshape(hh, W)
        i += 1
    pr.wait()


def components(mask):
    h, w = mask.shape
    seen = np.zeros_like(mask, bool)
    comps = []
    for sy, sx in zip(*np.nonzero(mask)):
        if seen[sy, sx]:
            continue
        stack, cells = [(sy, sx)], []
        seen[sy, sx] = True
        while stack:
            cy, cx = stack.pop()
            cells.append((cy, cx))
            for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1), (cy + 1, cx + 1), (cy - 1, cx - 1)):
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True; stack.append((ny, nx))
        comps.append(cells)
    return comps


events = []   # (t, kind, bbox as fractions [x0, y0, x1, y1])
grabs = {}    # t -> small RGB frame for the contact sheets
for seg in [s for s in edl["segments"] if s["kind"] == "screen"]:
    prev = None
    for t, f in frames(seg):
        if round(t * RATE) % (6 * RATE) == 0 or prev is None:
            grabs[round(t, 2)] = f
        if prev is not None:
            d = np.abs(f.astype(np.int16) - prev.astype(np.int16)) > THRESH
            hb, wb = d.shape[0] // BLOCK, d.shape[1] // BLOCK
            blocks = d[:hb * BLOCK, :wb * BLOCK].reshape(hb, BLOCK, wb, BLOCK).sum(axis=(1, 3)) >= 2
            share = blocks.mean()
            if share >= PAGE:
                events.append((t, "page", None))
            elif share > 0:
                comps = [c for c in components(blocks) if len(c) >= MIN_COMP]
                if comps:
                    big = max(comps, key=len)
                    near = [c for c in comps if len(c) >= len(big) * 0.3]
                    ys = [p[0] for c in near for p in c]; xs = [p[1] for c in near for p in c]
                    bb = [min(xs) / wb, min(ys) / hb, (max(xs) + 1) / wb, (max(ys) + 1) / hb]
                    events.append((t, "local", bb))
                    grabs[round(t, 2)] = f
        prev = f
    events.append((seg["e"], "end", None))

# group nearby local changes into zoom windows
sugg, cur = [], None


def close(c):
    if not c:
        return
    x0, y0, x1, y1 = c["bb"]
    bw, bh = max(x1 - x0, 0.04), max(y1 - y0, 0.04)
    z = min(FILL / bw, FILL / bh, ZMAX)
    if z >= ZMIN and (c["last"] - c["first"] >= 0.25 or bw * bh >= 0.03):
        s, e = c["first"] - 0.5, c["last"] + 1.5
        if e - s < 2.5:
            e = s + 2.5
        sugg.append({"s": round(s, 2), "e": round(e, 2), "x": round((x0 + x1) / 2, 3), "y": round((y0 + y1) / 2, 3),
                     "z": round(z, 2), "why": f"{c['n']} changes in a {bw:.0%} x {bh:.0%} area", "t_mid": c["mid"]})


for t, kind, bb in events:
    if kind != "local":
        close(cur); cur = None; continue
    if cur and t - cur["last"] <= 1.5:
        u = [min(cur["bb"][0], bb[0]), min(cur["bb"][1], bb[1]), max(cur["bb"][2], bb[2]), max(cur["bb"][3], bb[3])]
        if u[2] - u[0] <= FILL and u[3] - u[1] <= FILL:
            cur.update(bb=u, last=t, n=cur["n"] + 1); continue
        close(cur)
    cur = {"first": t, "last": t, "bb": bb, "n": 1, "mid": round(t, 2)}
close(cur)

# keep windows inside their segment and apart from each other
segs = [s for s in edl["segments"] if s["kind"] == "screen"]
out = []
for z in sugg:
    seg = next(s for s in segs if s["s"] <= z["t_mid"] <= s["e"])
    z["s"], z["e"] = max(z["s"], seg["s"] + 0.3), min(z["e"], seg["e"] - 0.2)
    if out and z["s"] < out[-1]["e"] + 0.4:
        z["s"] = out[-1]["e"] + 0.4
    if z["e"] - z["s"] >= 1.8:
        out.append(z)
(WORK / "zooms_suggested.json").write_text(json.dumps([{k: v for k, v in z.items() if k != "t_mid"} for z in out],
                                                      indent=1), encoding="utf-8")


def sheet(items, path, cols=4):
    if not items:
        return
    tw = 320
    th = max(img.shape[0] for _, img, _ in items)
    canvas = Image.new("RGB", (cols * (tw + 8) + 8, ((len(items) + cols - 1) // cols) * (th + 30) + 8), (24, 24, 24))
    dr = ImageDraw.Draw(canvas)
    for i, (label, img, bb) in enumerate(items):
        x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 30)
        canvas.paste(Image.fromarray(img).convert("RGB"), (x, y + 22))
        dr.text((x, y + 4), label, fill=(255, 255, 255))
        if bb:
            h = img.shape[0]
            dr.rectangle([x + bb[0] * tw, y + 22 + bb[1] * h, x + bb[2] * tw, y + 22 + bb[3] * h], outline=(0, 160, 255), width=2)
    canvas.save(path, quality=85)


def nearest(t):
    k = min(grabs, key=lambda g: abs(g - t))
    return grabs[k]


zi = []
for i, z in enumerate(out):
    hw, hh = 0.5 / z["z"], 0.5 / z["z"]
    zi.append((f"#{i} {z['s']:.1f}-{z['e']:.1f}s z{z['z']}", nearest(z["t_mid"]),
               [z["x"] - hw, z["y"] - hh, z["x"] + hw, z["y"] + hh]))
sheet(zi, WORK / "zooms.jpg")
starts = {round(s["s"], 2) for s in segs}
overview = [(f"{t // 60:.0f}:{t % 60:04.1f}", img, None) for t, img in sorted(grabs.items())
            if round(t * RATE) % (6 * RATE) == 0 or t in starts]
sheet(overview, WORK / "screens.jpg", cols=5)
print(f"{len(out)} zoom suggestions -> zooms_suggested.json, zooms.jpg (the blue box is what the zoom shows); "
      f"screen overview -> screens.jpg")
for i, z in enumerate(out):
    print(f"  #{i:<2} {z['s']:7.2f}-{z['e']:7.2f}  x {z['x']:.2f} y {z['y']:.2f} z {z['z']}  {z['why']}")
