"""Render the style-menu preview clips: each style applied to the matching moment of a reel.

Usage: python -I style_previews.py <remotion_dir> <out_dir> [only_id ...]
Each preview: half size (540x960), muted, looping-friendly MP4, plus a poster JPG.
"""
import json
import subprocess
import sys
from pathlib import Path

R = Path(sys.argv[1])
OUT = Path(sys.argv[2])
ONLY = set(sys.argv[3:])
OUT.mkdir(parents=True, exist_ok=True)

# id: (props, first frame, last frame) — frames at 30 fps on the reel's timeline
PRESETS = {
    "cap-outline": ({"captionStyle": "outline"}, 0, 140),
    "cap-box": ({"captionStyle": "box"}, 0, 140),
    "cap-highlight": ({"captionStyle": "highlight"}, 0, 140),
    "cap-bold": ({"captionStyle": "bold"}, 0, 140),
    "cap-editorial": ({"captionStyle": "editorial"}, 0, 140),
    "cap-keyword": ({"captionStyle": "keyword"}, 0, 140),
    "shots-glass": ({}, 141, 336),
    "shots-float": ({"shotStyle": "float"}, 141, 336),
    "card-proof": ({}, 336, 436),
    "card-steps": ({}, 690, 830),
    "logos-pop": ({}, 740, 835),
    "logos-row": ({"logoStyle": "row"}, 740, 835),
    "cta-none": ({}, 1110, 1186),
    "cta-endcard": ({"endCard": True}, 1110, 1260),
}

props_dir = OUT / "_props"
props_dir.mkdir(exist_ok=True)
for pid, (props, a, b) in PRESETS.items():
    if ONLY and pid not in ONLY:
        continue
    pf = props_dir / f"{pid}.json"
    pf.write_text(json.dumps(props), encoding="utf-8")
    mp4 = OUT / f"{pid}.mp4"
    cmd = ["npx.cmd", "remotion", "render", "src/index.jsx", "Reel", str(mp4), f"--props={pf}", f"--frames={a}-{b}",
           "--scale=0.5", "--codec=h264", "--crf=26", "--muted", "--concurrency=2", "--overwrite", "--log=error"]
    r = subprocess.run(cmd, cwd=R, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print("FAILED", pid, r.stderr[-800:], flush=True)
        continue
    # poster from the middle of the clip
    mid = (b - a) / 60
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{mid:.2f}", "-i", str(mp4),
                    "-frames:v", "1", "-q:v", "4", str(OUT / f"{pid}.jpg")])
    print("done", pid, f"{mp4.stat().st_size / 1e6:.1f} MB", flush=True)
