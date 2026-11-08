"""Resize a Higgsfield carousel render to 1080x1350 and composite the real MOSIC logo.

Usage:
  python compose.py <raw.png> <out.png> [--logo navy|white] [--pos top-left|bottom-center]

top-left is the carousel position; bottom-center is the single-post position.
"""
import argparse
from pathlib import Path

from PIL import Image

W, H = 1080, 1350
LOGO_W = 400          # logo width on the final slide
LOGO_X, LOGO_Y = 86, 90  # top-left, inside the 8% / 7% margins
BOTTOM_LOGO_W = 280   # smaller sign-off logo for single posts
BOTTOM_MARGIN = 70
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--logo", choices=["navy", "white"])
    ap.add_argument("--pos", choices=["top-left", "bottom-center"], default="top-left")
    args = ap.parse_args()

    slide = Image.open(args.src).convert("RGB")
    # Crop to exact 4:5 before resizing in case the model returned a slightly different ratio
    sw, sh = slide.size
    if abs(sw / sh - W / H) > 0.005:
        if sw / sh > W / H:
            nw = round(sh * W / H)
            slide = slide.crop(((sw - nw) // 2, 0, (sw - nw) // 2 + nw, sh))
        else:
            nh = round(sw * H / W)
            slide = slide.crop((0, (sh - nh) // 2, sw, (sh - nh) // 2 + nh))
    slide = slide.resize((W, H), Image.LANCZOS)

    if args.logo:
        logo = Image.open(ASSETS / f"logo-{args.logo}.png").convert("RGBA")
        lw = LOGO_W if args.pos == "top-left" else BOTTOM_LOGO_W
        lh = round(logo.height * lw / logo.width)
        logo = logo.resize((lw, lh), Image.LANCZOS)
        if args.pos == "top-left":
            xy = (LOGO_X, LOGO_Y)
        else:
            xy = ((W - lw) // 2, H - BOTTOM_MARGIN - lh)
        slide.paste(logo, xy, logo)

    Path(args.dst).parent.mkdir(parents=True, exist_ok=True)
    slide.save(args.dst, optimize=True)
    print(f"saved {args.dst}")


if __name__ == "__main__":
    main()
