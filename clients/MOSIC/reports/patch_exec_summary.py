"""
Patch slide 2 (Executive Summary) of March and April report.v2.pptx:
- Remove MANUAL UPDATE banner
- Replace 3 existing point blocks with data-driven copy (resized to 1.05in each)
- Add a 4th Recommendations block
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = Path(__file__).resolve().parent
SRC  = HERE / "March and April report.v2.pptx"
DST  = HERE / "March and April report.v2.pptx"
BRAND_PATH = HERE.parents[2] / "_brand" / "brand.json"

BRAND = json.loads(BRAND_PATH.read_text(encoding="utf-8"))
C = {k: RGBColor.from_string(v.lstrip("#")) for k, v in BRAND["colours"].items()}
C["white"] = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Poppins"


def remove_shape(shape):
    shape._element.getparent().remove(shape._element)


def add_rect(slide, x, y, w, h, fill, *, rounded=False):
    s = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
        x, y, w, h,
    )
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.fill.background()
    s.shadow.inherit = False
    return s


def add_text(slide, x, y, w, h, text, *,
             size=12, bold=False, colour=None, font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    if colour is None:
        colour = C["ink"]
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top  = tf.margin_bottom = Emu(0)
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = colour
    return tb


# ── load ──────────────────────────────────────────────────────────────────────
prs   = Presentation(str(SRC))
slide = prs.slides[1]

# ── remove banner + old blocks ────────────────────────────────────────────────
REMOVE_NAMES = {
    "Rounded Rectangle 13", "TextBox 14",          # manual-update banner
    "Rounded Rectangle 15", "Rectangle 16",        # block 1
    "TextBox 17",           "TextBox 18",
    "Rounded Rectangle 19", "Rectangle 20",        # block 2
    "TextBox 21",           "TextBox 22",
    "Rounded Rectangle 23", "Rectangle 24",        # block 3
    "TextBox 25",           "TextBox 26",
}
removed = 0
for sh in list(slide.shapes):
    if sh.name in REMOVE_NAMES:
        remove_shape(sh)
        removed += 1
print(f"Removed {removed} shapes from slide 2")

# ── block content ─────────────────────────────────────────────────────────────
BLOCKS = [
    {
        "title": "April strong — YoY down 5.4% on a softer March",
        "body":  (
            "1,598 appointments held across Mar + Apr (vs 1,689 prior year, −5.4% YoY). "
            "March came in at 727, recovering from the Jan–Feb trough. "
            "April rebounded to 871 — the highest month in the trailing 12-month window."
        ),
        "accent": C["primary"],
    },
    {
        "title": "New-patient growth outpacing flat traffic",
        "body":  (
            "95 new patients this period vs 89 last year (+6.7% YoY). "
            "AUS website visitors essentially flat: 2,579 (+0.2% YoY). "
            "Organic search averaging 776 sessions/month — SEO holding consistent. "
            "Visitor-to-new-patient conversion is improving."
        ),
        "accent": C["primary"],
    },
    {
        "title": "Google Ads attribution gap — 4 bookings tracked, more likely untagged",
        "body":  (
            "GA4 records 4 appointment_bookings attributed to Paid Search across Mar + Apr. "
            "Direct channel accounts for ~96% of tracked bookings — typical when Google Ads "
            "campaigns run without UTM parameters. Actual paid-search contribution is likely higher."
        ),
        "accent": C["primary"],
    },
    {
        "title": "Recommendations",
        "body":  (
            "1.  Add UTM parameters to all Google Ads campaigns — closes the attribution gap and "
            "surfaces true paid performance. "
            "2.  New-patient growth outpacing traffic signals improving on-site conversion; "
            "test stronger CTAs on the top 3 booking pages. "
            "3.  April’s 871 appointments confirms healthy demand — focus on lifting the "
            "March floor in the next planning cycle."
        ),
        "accent": C["accent"],
    },
]

# ── layout constants ──────────────────────────────────────────────────────────
BX      = Inches(0.70)
BW      = Inches(12.00)
BHEIGHT = Inches(1.05)
GAP     = Inches(0.14)
START_Y = Inches(1.75)
ACC_W   = Inches(0.16)
TEXT_X  = BX + Inches(0.30)
TEXT_W  = Inches(11.50)

for i, block in enumerate(BLOCKS):
    by = START_Y + i * (BHEIGHT + GAP)

    # outer card (rounded, soft background)
    rr = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, BX, by, BW, BHEIGHT)
    rr.fill.solid()
    rr.fill.fore_color.rgb = C["bg_soft"]
    rr.line.color.rgb = C["line"]
    rr.line.width = Pt(0.5)
    rr.shadow.inherit = False

    # left accent bar
    add_rect(slide, BX, by, ACC_W, BHEIGHT, block["accent"])

    # title
    add_text(slide, TEXT_X, by + Inches(0.10), TEXT_W, Inches(0.33),
             block["title"], size=13, bold=True, colour=C["ink"])

    # body
    add_text(slide, TEXT_X, by + Inches(0.44), TEXT_W, Inches(0.58),
             block["body"], size=10.5, colour=C["muted"])


# ── save ──────────────────────────────────────────────────────────────────────
try:
    prs.save(str(DST))
    print(f"Saved: {DST}")
except PermissionError:
    print("ERROR: File is open in PowerPoint. Close it and re-run.", file=sys.stderr)
    sys.exit(1)
