"""
Update blocks 3 + 4 on slide 2:
- Block 3: swap attribution gap for booking funnel insight
- Block 4: swap UTM recommendation for booking widget audit + conversion advice
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

HERE = Path(__file__).resolve().parent
SRC  = HERE / "March and April report.v2.pptx"
DST  = HERE / "March and April report.v2.pptx"
BRAND_PATH = HERE.parents[2] / "_brand" / "brand.json"

BRAND = json.loads(BRAND_PATH.read_text(encoding="utf-8"))
C = {k: RGBColor.from_string(v.lstrip("#")) for k, v in BRAND["colours"].items()}
FONT = "Poppins"

UPDATES = {
    "TextBox 39": (
        "Booking funnel converting at 12.8% — room to improve",
        13, True, C["ink"]
    ),
    "TextBox 40": (
        "742 people entered the Cliniko booking page across Mar + Apr (AUS, GA4 Key Events). "
        "95 became new patients — a 12.8% booking-page-to-new-patient rate. "
        "The visit-to-booking-page rate is 28.8% (742 of 2,579 AUS visitors). "
        "Both steps have meaningful room to improve.",
        10.5, False, C["muted"]
    ),
    "TextBox 43": (
        "Recommendations",
        13, True, C["ink"]
    ),
    "TextBox 44": (
        "1.  Audit GA4 cross-domain tracking for the Cliniko booking widget — "
        "UTMs are active but Direct still accounts for ~96% of tracked bookings, "
        "pointing to session breakage in the booking step. "
        "Check Cliniko referral exclusions in GA4. "
        "2.  Booking page conversion at 12.8% has clear upside — "
        "test reducing friction on the top 3 booking pages "
        "(/bookings, /book-an-appointment-melb-osteo/, /book-an-appointment-pain-relief/). "
        "3.  April at 871 is the strongest month on record; March at 727 was the weak point. "
        "Allocate budget to lift March in the next planning cycle.",
        10.5, False, C["muted"]
    ),
}


def set_text(tb, text, size, bold, colour):
    tf = tb.text_frame
    tf.clear()
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = text
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = colour


prs   = Presentation(str(SRC))
slide = prs.slides[1]

updated = 0
for sh in slide.shapes:
    if sh.name in UPDATES and sh.has_text_frame:
        set_text(sh, *UPDATES[sh.name])
        updated += 1
        print(f"Updated {sh.name}")

if updated != len(UPDATES):
    print(f"WARNING: expected {len(UPDATES)} updates, got {updated}", file=sys.stderr)

try:
    prs.save(str(DST))
    print(f"Saved: {DST}")
except PermissionError:
    print("ERROR: File is open in PowerPoint. Close it and re-run.", file=sys.stderr)
    sys.exit(1)
