"""
Renders MOSIC's May + June 2026 report PPTX from data.json.

Slides where source data is unavailable get a red "MANUAL UPDATE REQUIRED"
banner across the top so they're easy to spot for hand-edits.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
BRAND_DIR = AGENCY_ROOT / "_brand"

DATA = json.loads((HERE / "data.json").read_text(encoding="utf-8"))


# ---------- brand ----------
BRAND = json.loads((BRAND_DIR / "brand.json").read_text(encoding="utf-8"))
C = {k: RGBColor.from_string(v.lstrip("#")) for k, v in BRAND["colours"].items()}
C["primary_2"] = RGBColor(0x00, 0x84, 0xFF)
C["white"]     = RGBColor(0xFF, 0xFF, 0xFF)
C["sky"]       = RGBColor(0xE5, 0xF2, 0xFF)
C["sky_2"]     = RGBColor(0xCF, 0xE6, 0xFF)
C["red"]       = RGBColor(0xCC, 0x00, 0x00)
C["red_soft"]  = RGBColor(0xFE, 0xE8, 0xE8)

FONT = "Poppins"
LOGO_BLUE  = BRAND_DIR / BRAND["logo"]["body"]

CLIENT_NAME = "Melbourne Osteopathy Sports Injury Centre"
PERIOD_LABEL = DATA["period_label"]
PERIOD_SHORT = DATA["period_short"]
HIGHLIGHT_SET = set(DATA["highlight"])

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]


# ---------- helpers ----------

def add_slide(): return prs.slides.add_slide(BLANK)

def _no_line(s): s.line.fill.background(); return s

def add_rect(slide, x, y, w, h, fill, *, rounded=False, line=None):
    s = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
        x, y, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: _no_line(s)
    else: s.line.color.rgb = line
    s.shadow.inherit = False
    return s

def add_oval(slide, x, y, w, h, fill, *, transparency=0.0):
    s = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    _no_line(s); s.shadow.inherit = False
    if transparency:
        from pptx.oxml.ns import qn
        from lxml import etree
        sp = s.fill._xPr.find(qn("a:solidFill"))
        srgb = sp.find(qn("a:srgbClr"))
        alpha = etree.SubElement(srgb, qn("a:alpha"))
        alpha.set("val", str(int((1 - transparency) * 100000)))
    return s

def add_text(slide, x, y, w, h, text, *,
             size=14, bold=False, colour=None, font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=None):
    if colour is None: colour = C["ink"]
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top = tf.margin_bottom = Emu(0)
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]; p.alignment = align
    if line_spacing: p.line_spacing = line_spacing
    if isinstance(text, list):
        first = True
        for line in text:
            run_p = p if first else tf.add_paragraph()
            run_p.alignment = align
            if line_spacing: run_p.line_spacing = line_spacing
            r = run_p.add_run()
            r.text = line; r.font.name = font; r.font.size = Pt(size)
            r.font.bold = bold; r.font.color.rgb = colour
            first = False
    else:
        r = p.add_run()
        r.text = text; r.font.name = font; r.font.size = Pt(size)
        r.font.bold = bold; r.font.color.rgb = colour
    return tb


def add_background(slide):
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, C["bg_soft"])
    add_oval(slide, Inches(10.5), Inches(-2.5), Inches(6), Inches(6),
             C["secondary"], transparency=0.92)
    add_oval(slide, Inches(-2), Inches(5.5), Inches(4.5), Inches(4.5),
             C["primary"], transparency=0.95)

def add_side_rail(slide, page_num):
    add_rect(slide, 0, 0, Inches(0.18), SLIDE_H, C["primary"])
    add_oval(slide, Inches(0.05), Inches(7.0), Inches(0.4), Inches(0.4),
             C["accent"])
    add_text(slide, Inches(0.05), Inches(7.0), Inches(0.4), Inches(0.4),
             f"{page_num:02d}", size=9, bold=True, colour=C["white"],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

def add_section_header(slide, kicker, title, *, page_num=None):
    add_background(slide)
    if page_num is not None: add_side_rail(slide, page_num)
    add_rect(slide, Inches(0.6), Inches(0.45), Inches(2.4), Inches(0.32),
             C["primary"], rounded=True)
    add_text(slide, Inches(0.6), Inches(0.45), Inches(2.4), Inches(0.32),
             kicker, size=9, bold=True, colour=C["white"],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, Inches(0.6), Inches(0.85), Inches(11), Inches(0.7),
             title, size=30, bold=True, colour=C["ink"], font=FONT)
    add_rect(slide, Inches(0.6), Inches(1.55), Inches(0.5), Emu(48000), C["primary"])
    add_rect(slide, Inches(1.1), Inches(1.55), Inches(0.25), Emu(48000), C["secondary"])
    slide.shapes.add_picture(str(LOGO_BLUE), Inches(11.4), Inches(0.4),
                             height=Inches(0.55))

def add_footer(slide, page_num):
    add_text(slide, Inches(0.45), Inches(7.18), Inches(8), Inches(0.25),
             "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io",
             size=9, colour=C["muted"], font=FONT)
    add_text(slide, Inches(11), Inches(7.18), Inches(2), Inches(0.25),
             f"MOSIC  ·  {PERIOD_SHORT}  ·  {page_num:02d}",
             size=9, colour=C["muted"], font=FONT, align=PP_ALIGN.RIGHT)


def add_manual_banner(slide, text):
    """Red banner across the top of a slide flagging missing/manual data."""
    y = Inches(1.7)
    add_rect(slide, Inches(0.4), y, Inches(12.5), Inches(0.55),
             C["red"], rounded=True)
    add_text(slide, Inches(0.6), y, Inches(12.1), Inches(0.55),
             f"⚠   MANUAL UPDATE REQUIRED   —   {text}",
             size=11, bold=True, colour=C["white"], font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)


def add_partial_banner(slide, text):
    """Orange/soft banner explaining a substituted metric."""
    y = Inches(1.7)
    add_rect(slide, Inches(0.4), y, Inches(12.5), Inches(0.45),
             C["accent"], rounded=True)
    add_text(slide, Inches(0.6), y, Inches(12.1), Inches(0.45),
             f"ⓘ   API SUBSTITUTION   —   {text}",
             size=10, bold=True, colour=C["white"], font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)


def add_chart(slide, x, y, w, h, categories, values, *,
              title=None, highlight_set=None):
    data = CategoryChartData()
    data.categories = categories
    data.add_series("Value", values)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, w, h, data
    ).chart
    if title:
        chart.has_title = True
        chart.chart_title.text_frame.text = title
        for r in chart.chart_title.text_frame.paragraphs[0].runs:
            r.font.size = Pt(13); r.font.bold = True
            r.font.name = FONT; r.font.color.rgb = C["primary"]
    else:
        chart.has_title = False
    chart.has_legend = False
    plot = chart.plots[0]
    plot.gap_width = 70
    plot.has_data_labels = True
    dl = plot.data_labels
    dl.font.size = Pt(9); dl.font.name = FONT
    dl.font.color.rgb = C["ink"]; dl.font.bold = True
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
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


def add_table(slide, x, y, w, h, headers, rows, *, font_size=11, header_fill=None):
    if header_fill is None: header_fill = C["primary"]
    rcount, ccount = len(rows) + 1, len(headers)
    tbl = slide.shapes.add_table(rcount, ccount, x, y, w, h).table
    for j, hdr in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = header_fill
        tf = cell.text_frame; tf.text = ""
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
        r = p.add_run(); r.text = hdr
        r.font.size = Pt(font_size - 1); r.font.bold = True
        r.font.color.rgb = C["white"]; r.font.name = FONT
        cell.margin_left = cell.margin_right = Emu(70000)
        cell.margin_top = cell.margin_bottom = Emu(50000)
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C["row_alt"] if i % 2 == 0 else C["bg"]
            tf = cell.text_frame; tf.text = ""
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.RIGHT
            r = p.add_run()
            r.text = str(val) if val not in (None, "") else "—"
            r.font.size = Pt(font_size); r.font.name = FONT
            r.font.color.rgb = C["ink"]
            cell.margin_left = cell.margin_right = Emu(70000)
            cell.margin_top = cell.margin_bottom = Emu(40000)
    return tbl


# ---------- KPI math ----------
def _series_to_dict(series): return {l: v for l, v in series}

def sum_recent(series, n=2):
    return sum(v for _, v in series[-n:] if v is not None)

vis      = DATA.get("website_visitors_aus") or []
org      = DATA.get("organic_search") or []
conf     = DATA.get("confirmed_bookings") or []
new_pat  = DATA.get("total_new_patients") or []
bourke   = DATA.get("appointments_bourke") or []
essn     = DATA.get("appointments_essendon") or []
top_pgs  = DATA.get("top_pages") or []

vis_now  = sum_recent(vis)
conf_now = sum_recent(conf)
np_now   = sum_recent(new_pat)
vis_yoy  = DATA.get("yoy_visitors_aus") or 0
conf_yoy = DATA.get("yoy_confirmed_bookings") or 0
np_yoy   = DATA.get("yoy_new_patients") or 0


def slide_cover():
    slide = add_slide()
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, C["primary"])
    add_oval(slide, Inches(8.5), Inches(-3.5), Inches(8.5), Inches(8.5),
             C["secondary"], transparency=0.78)
    add_oval(slide, Inches(-3), Inches(4), Inches(7), Inches(7),
             C["primary_2"], transparency=0.85)
    add_oval(slide, Inches(10), Inches(4.5), Inches(4), Inches(4),
             C["accent"], transparency=0.88)
    add_rect(slide, Inches(0.9), Inches(2.3), Inches(3.9), Inches(1.7),
             C["white"], rounded=True)
    slide.shapes.add_picture(str(LOGO_BLUE), Inches(1.1), Inches(2.55),
                             height=Inches(1.2))
    add_text(slide, Inches(0.9), Inches(4.3), Inches(11), Inches(0.4),
             "MONTHLY PERFORMANCE REPORT", size=13, bold=True,
             colour=C["white"], font=FONT)
    add_text(slide, Inches(0.9), Inches(4.75), Inches(11), Inches(2.0),
             [CLIENT_NAME], size=44, bold=True, colour=C["white"],
             font=FONT, line_spacing=1.05)
    add_text(slide, Inches(0.9), Inches(6.55), Inches(11), Inches(0.5),
             PERIOD_LABEL, size=22, bold=True, colour=C["secondary"], font=FONT)


def slide_exec_summary(page=2):
    slide = add_slide()
    add_section_header(slide, "01  ·  OVERVIEW", "Executive summary",
                       page_num=page)
    add_manual_banner(slide,
        "Auto-draft below from API deltas — review tone and add narrative before sending.")
    paragraphs = [
        ("Bookings rebounding into autumn.",
         f"Total appointments held: {conf_now:,} this period vs {conf_yoy:,} for May+Jun 2025 "
         f"({(conf_now-conf_yoy)/conf_yoy*100:+.1f}% YoY). "
         f"June alone hit {conf[-1][1]:,} bookings."),
        ("New-patient flow steady, traffic flat.",
         f"New patients: {np_now} this period vs {np_yoy} prior year ({(np_now-np_yoy)/np_yoy*100:+.1f}% YoY). "
         f"AUS website visitors: {vis_now:,} vs {vis_yoy:,} last year ({(vis_now-vis_yoy)/vis_yoy*100:+.1f}% YoY) — "
         f"essentially flat. Conversion rate (visitor → new patient) is steady."),
        ("Action this period",
         "Confirm Google Ads phone-call recovery, review HotDoc booking conversion, and "
         "monitor the rebuilt landing-page copy for click-to-book lift. Cliniqapps figures, "
         "phone-call totals and HotDoc bookings still pending — see flagged slides."),
    ]
    y = Inches(2.5)
    card_w = Inches(12.0); card_h = Inches(1.4)
    accent_colours = [C["primary"], C["secondary"], C["accent"]]
    for i, (headline, body) in enumerate(paragraphs):
        add_rect(slide, Inches(0.7), y, card_w, card_h, C["white"], rounded=True)
        add_rect(slide, Inches(0.7), y, Inches(0.16), card_h, accent_colours[i])
        add_text(slide, Inches(1.0), y + Inches(0.15), card_w - Inches(0.5), Inches(0.4),
                 headline, size=14, bold=True, colour=C["ink"], font=FONT)
        add_text(slide, Inches(1.0), y + Inches(0.55), card_w - Inches(0.5), card_h - Inches(0.6),
                 body, size=11, colour=C["muted"], font=FONT, line_spacing=1.3)
        y += card_h + Inches(0.12)
    add_footer(slide, page)


def slide_kpi(page=3):
    slide = add_slide()
    add_section_header(slide, "02  ·  SNAPSHOT",
                       f"Period snapshot — {PERIOD_SHORT}", page_num=page)
    add_text(slide, Inches(0.6), Inches(1.85), Inches(11), Inches(0.35),
             "Year-on-year comparison vs May + Jun 2025",
             size=12, colour=C["muted"], font=FONT)

    kpis = [
        ("Website visitors (AUS)", vis_now,  vis_yoy,  None),
        ("Appointments held",      conf_now, conf_yoy, None),
        ("Total new patients",     np_now,   np_yoy,   None),
        ("Google Ads calls",       None,     None,     "Manual entry — Google Ads call data not in API"),
    ]
    card_w, card_h = Inches(2.95), Inches(2.7)
    gap = Inches(0.18)
    start_x = Inches(0.6); y = Inches(2.45)
    for i, (label, curr, prev, missing) in enumerate(kpis):
        x = start_x + (card_w + gap) * i
        if missing:
            add_rect(slide, x, y, card_w, card_h, C["red_soft"], rounded=True)
            add_rect(slide, x, y, card_w, Inches(0.32), C["red"], rounded=True)
            add_text(slide, x, y, card_w, Inches(0.32),
                     "MANUAL", size=9, bold=True,
                     colour=C["white"], font=FONT,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            add_text(slide, x + Inches(0.3), y + Inches(0.55), card_w - Inches(0.6), Inches(0.35),
                     label.upper(), size=9, bold=True, colour=C["red"], font=FONT)
            add_text(slide, x + Inches(0.3), y + Inches(0.95), card_w - Inches(0.6), Inches(1.0),
                     "—", size=52, bold=True, colour=C["red"], font=FONT)
            add_text(slide, x + Inches(0.3), y + Inches(2.05), card_w - Inches(0.6), Inches(0.6),
                     missing, size=9, colour=C["red"], font=FONT, line_spacing=1.2)
            continue
        add_rect(slide, x, y, card_w, card_h, C["primary"], rounded=True)
        add_oval(slide, x + card_w - Inches(1.3), y + card_h - Inches(1.3),
                 Inches(1.6), Inches(1.6), C["secondary"], transparency=0.78)
        add_text(slide, x + Inches(0.3), y + Inches(0.3), card_w - Inches(0.6), Inches(0.35),
                 label.upper(), size=9, bold=True, colour=C["sky"], font=FONT)
        add_text(slide, x + Inches(0.3), y + Inches(0.65), card_w - Inches(0.6), Inches(1.1),
                 f"{curr:,}", size=52, bold=True, colour=C["white"], font=FONT)
        if prev:
            pct = (curr - prev) / prev * 100
            arrow = "▲" if pct > 0 else ("▼" if pct < 0 else "→")
            d_clr = C["secondary"] if pct >= 0 else RGBColor(0xFF, 0xC9, 0xB0)
            add_text(slide, x + Inches(0.3), y + Inches(1.85), card_w - Inches(0.6), Inches(0.4),
                     f"{arrow}  {abs(pct):.1f}% YoY",
                     size=14, bold=True, colour=d_clr, font=FONT)
            add_text(slide, x + Inches(0.3), y + Inches(2.2), card_w - Inches(0.6), Inches(0.35),
                     f"vs {prev:,} prior year",
                     size=10, colour=C["sky_2"], font=FONT)
    add_footer(slide, page)


def slide_chart_single(kicker, title, sub, subtitle, series, caption, page,
                       partial=None, manual=None):
    slide = add_slide()
    add_section_header(slide, kicker, title, page_num=page)

    if manual:
        add_manual_banner(slide, manual)
        chart_y = Inches(2.55)
    elif partial:
        add_partial_banner(slide, partial)
        chart_y = Inches(2.4)
    else:
        chart_y = Inches(2.25)

    if sub and not (manual or partial):
        add_text(slide, Inches(0.6), Inches(1.85), Inches(11.5), Inches(0.35),
                 sub, size=12, colour=C["muted"], font=FONT)

    chart_h = Inches(7.2 - 2.25 - 0.6) - (chart_y - Inches(2.25))
    cats = [c for c, _ in series]
    vals = [v for _, v in series]
    add_rect(slide, Inches(0.5), chart_y, Inches(12.3), chart_h,
             C["white"], rounded=True)
    add_chart(slide, Inches(0.7), chart_y + Inches(0.15),
              Inches(11.9), chart_h - Inches(0.3),
              cats, vals, title=subtitle, highlight_set=HIGHLIGHT_SET)
    if caption:
        add_text(slide, Inches(0.6), Inches(6.85), Inches(12.1), Inches(0.35),
                 caption, size=10, colour=C["muted"], font=FONT)
    add_footer(slide, page)


def slide_chart_pair(kicker, title, sub, datasets, page, partial=None):
    slide = add_slide()
    add_section_header(slide, kicker, title, page_num=page)
    if partial:
        add_partial_banner(slide, partial)
        chart_y = Inches(2.4)
    else:
        chart_y = Inches(2.25)
    if sub and not partial:
        add_text(slide, Inches(0.6), Inches(1.85), Inches(11.5), Inches(0.35),
                 sub, size=12, colour=C["muted"], font=FONT)
    chart_w = Inches(6.0); chart_h = Inches(7.2 - 2.25 - 0.6) - (chart_y - Inches(2.25))
    for i, (subtitle, series) in enumerate(datasets):
        cats = [c for c, _ in series]; vals = [v for _, v in series]
        x = Inches(0.5) + Inches(6.2) * i
        add_rect(slide, x, chart_y, chart_w, chart_h, C["white"], rounded=True)
        add_chart(slide, x + Inches(0.15), chart_y + Inches(0.15),
                  chart_w - Inches(0.3), chart_h - Inches(0.3),
                  cats, vals, title=subtitle, highlight_set=HIGHLIGHT_SET)
    add_footer(slide, page)


def slide_top_pages(page=8):
    slide = add_slide()
    add_section_header(slide, "06  ·  CONTENT",
                       f"Most viewed pages — {PERIOD_SHORT}", page_num=page)
    rows = [(p, f"{v:,}", f"{u:,}") for p, v, u in top_pgs]
    add_rect(slide, Inches(0.5), Inches(1.95), Inches(12.3), Inches(4.7),
             C["white"], rounded=True)
    add_table(slide, Inches(0.75), Inches(2.1), Inches(11.85), Inches(4.4),
              ["Page", "Views", "Active users"], rows, font_size=12)
    add_text(slide, Inches(0.6), Inches(6.8), Inches(12.1), Inches(0.4),
             f"Top 10 pages by total views, {PERIOD_SHORT}. Source: GA4.",
             size=10, colour=C["muted"], font=FONT)
    add_footer(slide, page)


def slide_locations(page=10):
    slide = add_slide()
    add_section_header(slide, "07b  ·  LOCATIONS",
                       "Appointments by location", page_num=page)
    add_partial_banner(slide,
        "Showing all appointments per location (Cliniko). Original deck used "
        "'new patients per location' — that requires manual cross-ref of new patient → "
        "first appointment business and isn't reliable via API.")
    chart_w = Inches(6.0); chart_h = Inches(4.3)
    for i, (label, series) in enumerate([
        ("MOSIC – Bourke St", bourke),
        ("MOSIC – Essendon", essn),
    ]):
        cats = [c for c, _ in series]; vals = [v for _, v in series]
        x = Inches(0.5) + Inches(6.2) * i
        add_rect(slide, x, Inches(2.45), chart_w, chart_h, C["white"], rounded=True)
        add_chart(slide, x + Inches(0.15), Inches(2.6),
                  chart_w - Inches(0.3), chart_h - Inches(0.3),
                  cats, vals, title=label, highlight_set=HIGHLIGHT_SET)
    add_footer(slide, page)


def slide_manual_only(kicker, title, banner, page):
    """Slide for sections where we have no API data — banner + placeholder."""
    slide = add_slide()
    add_section_header(slide, kicker, title, page_num=page)
    add_manual_banner(slide, banner)
    # Placeholder card
    add_rect(slide, Inches(0.5), Inches(2.55), Inches(12.3), Inches(4.3),
             C["white"], rounded=True)
    add_text(slide, Inches(0.6), Inches(4.0), Inches(12.1), Inches(1.0),
             "Paste data here from source, or copy structure from previous report.",
             size=14, colour=C["muted"], font=FONT,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(slide, page)


# ---------- build ----------
slide_cover()                                                       # 1
slide_exec_summary(page=2)                                          # 2
slide_kpi(page=3)                                                   # 3

# Cliniko bookings — appointments_held proxy for "confirmed bookings"
slide_chart_single(
    "03  ·  CLINIKO", "Cliniko — appointments held",
    "Total appointments held per month — last 12 months",
    "Appointments held",
    conf,
    "Source: Cliniko API. Original deck tracked 'Cliniko booking page confirmations' "
    "(GA4 event), which is a subset — this view shows all completed appointments.",
    page=4,
    partial="Showing total Cliniko appointments held — original deck filtered to bookings "
            "made via the Cliniko booking PAGE (a GA4 event). To restore that exact metric, "
            "pull the booking-page conversion event from GA4 manually.",
)

# "Entered the booking page" — was a GA4 event we don't know the name of
slide_manual_only(
    "03b  ·  CLINIKO",
    "Entered the Cliniko booking page",
    "GA4 page-view counts for the Cliniko booking page need confirming. "
    "Check the /bookings and /book-an-appointment-melb-osteo paths in GA4 "
    "for May + Jun 2026— copy a 12-month series in if those are the right paths.",
    page=5,
)

# Google Ads phone calls — no API access for this metric on this account
slide_manual_only(
    "04  ·  GOOGLE ADS",
    "Google Ads — phone calls",
    "Google Ads phone_calls metric requires call_view (call tracking) "
    "or campaign-level segment that this account doesn't expose. "
    "Pull from Google Ads UI manually.",
    page=6,
)

# Website (page 7) — both from GA4
slide_chart_pair(
    "05  ·  WEBSITE", "Website traffic (AUS only)",
    "Last 12 months — May + Jun 2026 highlighted in orange.",
    [
        ("Total visitors", vis),
        ("Organic search", org),
    ], page=7,
)

# Top pages
slide_top_pages(page=8)

# New bookings — only have "total new patients" (Cliniko); "from Google" needs manual
slide_chart_single(
    "07  ·  NEW BOOKINGS", "Total new patients",
    "New patient registrations per month — last 12 months",
    "Total new patients",
    new_pat,
    "Source: Cliniko API (patients created in window).",
    page=9,
    partial="Original deck split this into 'New patients from Google' vs 'Total'. "
            "The Google-attribution split needs Google Ads conversion → Cliniko patient "
            "matching, which isn't currently wired up. Total shown here.",
)

# Locations
slide_locations(page=10)

# Cliniqapps automations — no API
slide_manual_only(
    "08  ·  AUTOMATIONS",
    "Cliniqapps email automations",
    "Cliniqapps has no public API. Export DNA / Cancellation / Reactivation tier "
    "data from the Cliniqapps dashboard and paste into the 5-card layout from the prior report.",
    page=11,
)

# Cliniqapps broadcast — no API
slide_manual_only(
    "09  ·  BROADCAST",
    "Cliniqapps broadcast emails",
    "Cliniqapps has no public API. Export monthly broadcast send / open / click "
    "rates (with-apt vs without-apt) from the Cliniqapps dashboard.",
    page=12,
)

# Actioned items — manual log
slide_manual_only(
    "10  ·  ACTIONED",
    "Actioned items this period",
    "Internal task log — list out website development items + 'other' items completed "
    "during May + June 2026 in the same two-column format as the prior deck.",
    page=13,
)

# HotDoc appendix — no API
slide_manual_only(
    "11  ·  APPENDIX",
    "HotDoc bookings",
    "HotDoc does not expose monthly booking totals via API. Pull from the HotDoc "
    "dashboard manually (count bookings for May + Jun 2026, per location).",
    page=14,
)


# ---------- save ----------
out = HERE / "report.pptx"
try:
    prs.save(str(out))
except PermissionError:
    out = HERE / "report-v2.pptx"
    prs.save(str(out))
print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
