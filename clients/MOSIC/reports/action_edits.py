"""
Action Sam's edits on the canonical Mar + Apr 2026 deck.

Edit 1 (slide 5): drop the GA4 screenshot + manual-update banner + Sam's
inline comment. Replace with a hero stat card: big "742" with caption,
matching the Locate Digital brand palette.

Edit 2 (slide 8): replace the top-10 (global) table with top-20 AUS-only.

Edits 3 + 4 (slides 9 + 10): revert to single-series clustered columns
(no stacking — too few Paid Search bookings to be visually useful here).
Inline comments removed; API SUBSTITUTION banner removed since attribution
now lives on a dedicated slide.

NEW slide 11 (07c · ATTRIBUTION): bookings by digital source. Stacked
column showing GA4 `appointment_bookings` per month, broken down by
sessionDefaultChannelGroup. Each channel labelled. Inserted between the
existing Locations slide and Automations slide; footers on bumped slides
renumbered.

Output: "March and April report.v2.pptx" (canonical original untouched).
"""
from __future__ import annotations
import json
import re
from copy import deepcopy
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION

from lxml import etree

HERE = Path(__file__).resolve().parent
SRC = HERE / "March and April report.pptx"
DST = HERE / "March and April report.v2.pptx"
BRAND_PATH = HERE.parents[2] / "_brand" / "brand.json"

BRAND = json.loads(BRAND_PATH.read_text(encoding="utf-8"))
C = {k: RGBColor.from_string(v.lstrip("#")) for k, v in BRAND["colours"].items()}
C["white"] = RGBColor(0xFF, 0xFF, 0xFF)
C["sky"]   = RGBColor(0xE5, 0xF2, 0xFF)
C["sky_2"] = RGBColor(0xCF, 0xE6, 0xFF)
C["grey"]  = RGBColor(0xC8, 0xCC, 0xD0)
C["grey_2"] = RGBColor(0x90, 0x94, 0x98)

FONT = "Poppins"


# ---------- helpers ----------

def remove_shape(shape):
    sp = shape._element
    sp.getparent().remove(sp)


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


def add_oval(slide, x, y, w, h, fill, *, transparency=0.0):
    s = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.fill.background()
    s.shadow.inherit = False
    if transparency:
        sp = s.fill._xPr.find(qn("a:solidFill"))
        srgb = sp.find(qn("a:srgbClr"))
        alpha = etree.SubElement(srgb, qn("a:alpha"))
        alpha.set("val", str(int((1 - transparency) * 100000)))
    return s


def add_text(slide, x, y, w, h, text, *,
             size=14, bold=False, colour=None, font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    if colour is None:
        colour = C["ink"]
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top = tf.margin_bottom = Emu(0)
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


def remove_banner_and_comment(slide, comment_prefix):
    """Remove the orange API SUBSTITUTION banner + Sam's inline comment."""
    to_drop = []
    for sh in slide.shapes:
        if sh.name == "Rounded Rectangle 13" and sh.top is not None:
            if 1.65 < sh.top / 914400 < 1.75:
                to_drop.append(sh)
                continue
        if sh.has_text_frame:
            text = " ".join(p.text for p in sh.text_frame.paragraphs).strip()
            if text.startswith("ⓘ"):
                to_drop.append(sh)
            elif text.startswith(comment_prefix):
                to_drop.append(sh)
    for sh in to_drop:
        remove_shape(sh)
    return len(to_drop)


def add_clustered_chart(slide, x, y, w, h, categories, values, *,
                        title=None, highlight_set=None):
    """Single-series clustered column with optional period highlight."""
    cd = CategoryChartData()
    cd.categories = categories
    cd.add_series("Value", values)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, w, h, cd,
    ).chart
    if title:
        chart.has_title = True
        chart.chart_title.text_frame.text = title
        for r in chart.chart_title.text_frame.paragraphs[0].runs:
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.name = FONT
            r.font.color.rgb = C["primary"]
    else:
        chart.has_title = False
    chart.has_legend = False
    plot = chart.plots[0]
    plot.gap_width = 70
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.font.size = Pt(9)
    dl.font.name = FONT
    dl.font.color.rgb = C["ink"]
    dl.font.bold = True
    series = plot.series[0]
    series.format.fill.solid()
    series.format.fill.fore_color.rgb = C["primary"]
    if highlight_set:
        for i, cat in enumerate(categories):
            if cat in highlight_set:
                pt = series.points[i]
                pt.format.fill.solid()
                pt.format.fill.fore_color.rgb = C["accent"]
    for axis in (chart.category_axis, chart.value_axis):
        axis.tick_labels.font.size = Pt(9)
        axis.tick_labels.font.name = FONT
        axis.tick_labels.font.color.rgb = C["muted"]
    chart.value_axis.visible = False
    return chart


# ---------- load ----------
prs = Presentation(str(SRC))


# ========================================================================
# Edit 1: slide 5 — hero stat for the 742 figure
# ========================================================================
slide5 = prs.slides[4]
to_remove = []
for sh in slide5.shapes:
    name = sh.name or ""
    if name == "Rounded Rectangle 13" and sh.top is not None:
        if 1.65 < sh.top / 914400 < 1.75:
            to_remove.append(sh)
            continue
    if name == "Rounded Rectangle 15":
        to_remove.append(sh)
        continue
    if name == "Picture 20":
        to_remove.append(sh)
        continue
    if sh.has_text_frame:
        text = " ".join(p.text for p in sh.text_frame.paragraphs).strip()
        if text.startswith("⚠"):
            to_remove.append(sh)
        elif text.startswith("-The number of people"):
            to_remove.append(sh)

print(f"Slide 5: removing {len(to_remove)} shapes")
for sh in to_remove:
    remove_shape(sh)

hero_x = Inches(0.6)
hero_y = Inches(2.0)
hero_w = Inches(12.1)
hero_h = Inches(4.85)
add_rect(slide5, hero_x, hero_y, hero_w, hero_h, C["primary"], rounded=True)
add_oval(slide5, hero_x + hero_w - Inches(3.2), hero_y - Inches(1.5),
         Inches(4.8), Inches(4.8), C["secondary"], transparency=0.72)
add_oval(slide5, hero_x - Inches(1.0), hero_y + hero_h - Inches(2.0),
         Inches(3.0), Inches(3.0), C["accent"], transparency=0.88)
add_text(slide5, hero_x + Inches(0.7), hero_y + Inches(0.55),
         Inches(10.7), Inches(0.4),
         "CLINIKO BOOKING PAGE ENTRIES",
         size=13, bold=True, colour=C["sky"])
add_text(slide5, hero_x + Inches(0.7), hero_y + Inches(1.0),
         Inches(10.7), Inches(2.8),
         "742", size=180, bold=True, colour=C["white"])
add_text(slide5, hero_x + Inches(0.7), hero_y + Inches(3.55),
         Inches(10.7), Inches(0.45),
         "people entered the Cliniko booking page",
         size=20, bold=False, colour=C["sky"])
add_text(slide5, hero_x + Inches(0.7), hero_y + Inches(4.05),
         Inches(10.7), Inches(0.4),
         "Mar + Apr 2026  ·  Australia only  ·  Source: GA4 Key Events",
         size=11, colour=C["sky_2"])


# ========================================================================
# Edit 2: slide 8 — top 20 AUS pages
# ========================================================================
data_path = HERE / "2026-03-04" / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
top_pages = data["top_pages"]
assert len(top_pages) == 20, f"Expected 20 top pages, got {len(top_pages)}"
country = data.get("top_pages_country_filter", "Australia")

slide8 = prs.slides[7]
old_tbl = None
to_remove_s8 = []
caption_box = None
for sh in slide8.shapes:
    if sh.shape_type == 19:
        old_tbl = sh
    if sh.has_text_frame:
        text = " ".join(p.text for p in sh.text_frame.paragraphs).strip()
        if text.startswith("Update to top 20 pages"):
            to_remove_s8.append(sh)
        elif text.startswith("Top 10 pages by total views"):
            caption_box = sh

assert old_tbl is not None
tbl_x, tbl_y = old_tbl.left, old_tbl.top
tbl_w, tbl_h = old_tbl.width, old_tbl.height
remove_shape(old_tbl)
for sh in to_remove_s8:
    remove_shape(sh)
print(f"Slide 8: rebuilding top-20 table")


def add_top_pages_table(slide, x, y, w, h, rows):
    headers = ["Page", "Views", "Active users"]
    rcount, ccount = len(rows) + 1, len(headers)
    tbl = slide.shapes.add_table(rcount, ccount, x, y, w, h).table
    total = tbl_w
    tbl.columns[0].width = int(total * 0.66)
    tbl.columns[1].width = int(total * 0.17)
    tbl.columns[2].width = int(total * 0.17)
    row_h = int(h / rcount)
    for row in tbl.rows:
        row.height = row_h
    for j, hdr in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = C["primary"]
        tf = cell.text_frame; tf.text = ""
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
        r = p.add_run(); r.text = hdr
        r.font.size = Pt(9); r.font.bold = True
        r.font.color.rgb = C["white"]; r.font.name = FONT
        cell.margin_left = cell.margin_right = Emu(70000)
        cell.margin_top = cell.margin_bottom = Emu(30000)
    for i, (path, views, users) in enumerate(rows, start=1):
        for j, val in enumerate([path, f"{views:,}", f"{users:,}"]):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C["row_alt"] if i % 2 == 0 else C["bg"]
            tf = cell.text_frame; tf.text = ""
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
            r = p.add_run(); r.text = str(val)
            r.font.size = Pt(9); r.font.name = FONT
            r.font.color.rgb = C["ink"]
            cell.margin_left = cell.margin_right = Emu(70000)
            cell.margin_top = cell.margin_bottom = Emu(20000)
    return tbl


add_top_pages_table(slide8, tbl_x, tbl_y, tbl_w, tbl_h, top_pages)
if caption_box is not None:
    tf = caption_box.text_frame
    p = tf.paragraphs[0]
    for r in list(p.runs):
        r.text = ""
    run = p.runs[0] if p.runs else p.add_run()
    run.text = f"Top 20 pages by total views, Mar + Apr 2026. Source: GA4 ({country} only)."
    run.font.size = Pt(10); run.font.name = FONT
    run.font.color.rgb = C["muted"]


# ========================================================================
# Edits 3 + 4: slides 9 + 10 — revert to single-series clustered
# ========================================================================
months = [lbl for lbl, _ in data["total_new_patients"]]
total_new_patients = [(lbl, v) for lbl, v in data["total_new_patients"]]
bourke = [(lbl, v) for lbl, v in data["appointments_bourke"]]
essn = [(lbl, v) for lbl, v in data["appointments_essendon"]]
HIGHLIGHT = set(data.get("highlight", []))

# --- slide 9 ---
slide9 = prs.slides[8]
n = remove_banner_and_comment(
    slide9, "In the bar, make it show the amount that is coming from google ads",
)
print(f"Slide 9: removed {n} shape(s); rebuilding clustered chart")

for sh in list(slide9.shapes):
    if sh.has_chart:
        geom = (sh.left, sh.top, sh.width, sh.height)
        remove_shape(sh)
        add_clustered_chart(
            slide9, *geom,
            categories=[lbl for lbl, _ in total_new_patients],
            values=[v for _, v in total_new_patients],
            highlight_set=HIGHLIGHT,
        )
        break

# --- slide 10 ---
slide10 = prs.slides[9]
n = remove_banner_and_comment(
    slide10, "In the bar, make it show the amount that is coming from google ads",
)
print(f"Slide 10: removed {n} shape(s); rebuilding two clustered charts")

chart_shapes = [sh for sh in list(slide10.shapes) if sh.has_chart]
chart_shapes.sort(key=lambda s: s.left)
assert len(chart_shapes) == 2
geoms = []
for sh in chart_shapes:
    geoms.append((sh.left, sh.top, sh.width, sh.height))
    remove_shape(sh)
left_geom, right_geom = geoms
add_clustered_chart(
    slide10, *left_geom,
    categories=[lbl for lbl, _ in bourke],
    values=[v for _, v in bourke],
    title="MOSIC – Bourke St", highlight_set=HIGHLIGHT,
)
add_clustered_chart(
    slide10, *right_geom,
    categories=[lbl for lbl, _ in essn],
    values=[v for _, v in essn],
    title="MOSIC – Essendon", highlight_set=HIGHLIGHT,
)


# ========================================================================
# NEW slide: 07c · ATTRIBUTION — bookings by digital source
# ========================================================================
print(f"\nBuilding new attribution slide (slide 11)")
channel_blob = data["bookings_by_channel_monthly"]
chan_months = channel_blob["months"]
chan_data = channel_blob["data"]

# Channel order: Paid Search first (visually highlighted at bar bottom),
# then Direct (largest), then smaller channels. Drop channels with zero in all months.
CHANNEL_DISPLAY = [
    ("Paid Search",     "Paid Search (Google Ads)", C["accent"]),
    ("Direct",          "Direct",                   C["primary"]),
    ("Organic Search",  "Organic Search (SEO)",     C["secondary"]),
    ("Organic Social",  "Organic Social",           RGBColor(0x9B, 0x59, 0xB6)),
    ("Referral",        "Referral",                 C["grey_2"]),
    ("Unassigned",      "Unassigned",               C["grey"]),
]
series_for_chart = []
for ga_name, label, colour in CHANNEL_DISPLAY:
    vals = [chan_data.get(m, {}).get(ga_name, 0) for m in chan_months]
    if any(v > 0 for v in vals):
        series_for_chart.append((label, vals, colour))


SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
BLANK = prs.slide_layouts[6]
new_slide = prs.slides.add_slide(BLANK)

# --- background (matches existing decks) ---
add_rect(new_slide, 0, 0, SLIDE_W, SLIDE_H, RGBColor.from_string(BRAND["colours"]["bg_soft"].lstrip("#")))
add_oval(new_slide, Inches(10.5), Inches(-2.5), Inches(6), Inches(6),
         C["secondary"], transparency=0.92)
add_oval(new_slide, Inches(-2), Inches(5.5), Inches(4.5), Inches(4.5),
         C["primary"], transparency=0.95)

# --- side rail (matches existing) ---
add_rect(new_slide, 0, 0, Inches(0.18), SLIDE_H, C["primary"])

# --- section header ---
add_rect(new_slide, Inches(0.6), Inches(0.45), Inches(2.4), Inches(0.32),
         C["primary"], rounded=True)
add_text(new_slide, Inches(0.6), Inches(0.45), Inches(2.4), Inches(0.32),
         "07c  ·  ATTRIBUTION",
         size=9, bold=True, colour=C["white"],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
add_text(new_slide, Inches(0.6), Inches(0.85), Inches(11), Inches(0.7),
         "Bookings by digital source",
         size=30, bold=True, colour=C["ink"])
add_rect(new_slide, Inches(0.6), Inches(1.55), Inches(0.5), Emu(48000), C["primary"])
add_rect(new_slide, Inches(1.1), Inches(1.55), Inches(0.25), Emu(48000), C["secondary"])

# Logo
brand_dir = HERE.parents[2] / "_brand"
logo_path = brand_dir / BRAND["logo"]["body"]
if logo_path.exists():
    new_slide.shapes.add_picture(str(logo_path), Inches(11.4), Inches(0.4),
                                 height=Inches(0.55))

# --- subtitle ---
add_text(new_slide, Inches(0.6), Inches(1.85), Inches(12), Inches(0.35),
         "12-month rolling — GA4 ‘appointment_bookings’ key event, grouped by acquisition channel.",
         size=12, colour=C["muted"])

# --- chart card ---
add_rect(new_slide, Inches(0.5), Inches(2.3), Inches(12.3), Inches(4.4),
         C["white"], rounded=True)

# --- stacked chart ---
cd = CategoryChartData()
cd.categories = chan_months
for label, vals, _ in series_for_chart:
    cd.add_series(label, vals)
chart = new_slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_STACKED,
    Inches(0.7), Inches(2.45), Inches(11.9), Inches(4.1),
    cd,
).chart
chart.has_title = False
chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM
chart.legend.include_in_layout = False
chart.legend.font.size = Pt(10)
chart.legend.font.name = FONT
chart.legend.font.color.rgb = C["ink"]

plot = chart.plots[0]
plot.gap_width = 80
plot.has_data_labels = False
for ser, (_, _, colour) in zip(plot.series, series_for_chart):
    ser.format.fill.solid()
    ser.format.fill.fore_color.rgb = colour

for axis in (chart.category_axis, chart.value_axis):
    axis.tick_labels.font.size = Pt(9)
    axis.tick_labels.font.name = FONT
    axis.tick_labels.font.color.rgb = C["muted"]
chart.value_axis.visible = False

# --- source caption ---
add_text(new_slide, Inches(0.6), Inches(6.78), Inches(12.1), Inches(0.35),
         "Source: GA4. Each booking attributed to its session’s default channel "
         "group. ‘Direct’ is typically untagged or returning-visitor sessions.",
         size=10, colour=C["muted"])

# --- footer ---
add_text(new_slide, Inches(0.45), Inches(7.18), Inches(8), Inches(0.25),
         "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io",
         size=9, colour=C["muted"])
add_text(new_slide, Inches(11), Inches(7.18), Inches(2), Inches(0.25),
         "MOSIC  ·  Mar + Apr 2026  ·  11",
         size=9, colour=C["muted"], align=PP_ALIGN.RIGHT)


# ========================================================================
# Reorder: move the new slide (currently last) into position 11 (index 10)
# ========================================================================
sld_lst = prs.slides._sldIdLst
slides_xml = list(sld_lst)
new_slide_elem = slides_xml[-1]  # the one we just appended
sld_lst.remove(new_slide_elem)
sld_lst.insert(10, new_slide_elem)


# ========================================================================
# Renumber footers on bumped slides (indices 11..15 in the new order)
# ========================================================================
FOOTER_RE = re.compile(r"^MOSIC\s+·\s+Mar \+ Apr 2026\s+·\s+\d+\s*$")

for new_idx, slide in enumerate(prs.slides, start=1):
    if new_idx <= 10:
        continue  # slides 1-10 unchanged
    if new_idx == 11:
        continue  # the new attribution slide already has correct footer
    # Find the footer text box and rewrite the page number
    for sh in slide.shapes:
        if not sh.has_text_frame:
            continue
        text = sh.text_frame.text.strip()
        if FOOTER_RE.match(text):
            tf = sh.text_frame
            p = tf.paragraphs[0]
            for r in list(p.runs):
                r.text = ""
            run = p.runs[0] if p.runs else p.add_run()
            run.text = f"MOSIC  ·  Mar + Apr 2026  ·  {new_idx:02d}"
            run.font.size = Pt(9)
            run.font.name = FONT
            run.font.color.rgb = C["muted"]
            run.font.bold = False
            break


# ---------- save ----------
prs.save(str(DST))
print(f"\nWrote {DST}")
print(f"Total slides: {len(prs.slides)}  ·  Size: {DST.stat().st_size:,} bytes")
