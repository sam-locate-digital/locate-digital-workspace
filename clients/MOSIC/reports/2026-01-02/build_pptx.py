"""
Renders MOSIC's January + February 2026 report as a PPTX deck
in Locate Digital branding (Poppins everywhere).

Editable in PowerPoint — native charts, real tables, no images for text.
"""
from __future__ import annotations
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
sys.path.insert(0, str(HERE))
import build as src

# ---------- brand ----------
BRAND = src.load_brand()
C = {k: RGBColor.from_string(v.lstrip("#")) for k, v in BRAND["colours"].items()}
C["primary_2"] = RGBColor(0x00, 0x84, 0xFF)
C["white"]     = RGBColor(0xFF, 0xFF, 0xFF)
C["sky"]       = RGBColor(0xE5, 0xF2, 0xFF)
C["sky_2"]     = RGBColor(0xCF, 0xE6, 0xFF)

# Single font for everything per user request
FONT = "Poppins"

LOGO_BLUE  = src.BRAND_DIR / BRAND["logo"]["body"]      # blue logo on transparent
LOGO_WHITE = src.BRAND_DIR / BRAND["logo"]["inverse"]   # white logo on transparent

# ---------- canvas ----------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]


# ---------- low-level helpers ----------

def add_slide():
    return prs.slides.add_slide(BLANK)

def _no_line(shape):
    shape.line.fill.background()
    return shape

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
        # Set fill transparency via XML (python-pptx has no direct API)
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


# ---------- chrome (background, header, footer) ----------

def add_background(slide, *, decorate=True):
    """Subtle off-white background + corner blob for visual depth."""
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, C["bg_soft"])
    if decorate:
        # Top-right blob (very subtle)
        add_oval(slide, Inches(10.5), Inches(-2.5), Inches(6), Inches(6),
                 C["secondary"], transparency=0.92)
        # Bottom-left blob
        add_oval(slide, Inches(-2), Inches(5.5), Inches(4.5), Inches(4.5),
                 C["primary"], transparency=0.95)

def add_side_rail(slide, page_num):
    """Thin coloured rail on the left edge with page number."""
    add_rect(slide, 0, 0, Inches(0.18), SLIDE_H, C["primary"])
    # Page number badge
    add_oval(slide, Inches(0.05), Inches(7.0), Inches(0.4), Inches(0.4),
             C["accent"])
    add_text(slide, Inches(0.05), Inches(7.0), Inches(0.4), Inches(0.4),
             f"{page_num:02d}", size=9, bold=True, colour=C["white"],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

def add_section_header(slide, kicker, title, *, page_num=None):
    """Page chrome: rail, header text, logo, divider."""
    add_background(slide)
    if page_num is not None: add_side_rail(slide, page_num)

    # Kicker pill
    pill_text = kicker
    pill_w = Inches(2.4)
    add_rect(slide, Inches(0.6), Inches(0.45), pill_w, Inches(0.32),
             C["primary"], rounded=True)
    add_text(slide, Inches(0.6), Inches(0.45), pill_w, Inches(0.32),
             pill_text, size=9, bold=True, colour=C["white"],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # Title
    add_text(slide, Inches(0.6), Inches(0.85), Inches(11), Inches(0.7),
             title, size=30, bold=True, colour=C["ink"], font=FONT)

    # Coloured underline accent (gradient-ish using two stacked rects)
    add_rect(slide, Inches(0.6), Inches(1.55), Inches(0.5), Emu(48000), C["primary"])
    add_rect(slide, Inches(1.1), Inches(1.55), Inches(0.25), Emu(48000), C["secondary"])

    # Logo top-right
    slide.shapes.add_picture(str(LOGO_BLUE), Inches(11.4), Inches(0.4),
                             height=Inches(0.55))

def add_footer(slide, page_num):
    add_text(slide, Inches(0.45), Inches(7.18), Inches(8), Inches(0.25),
             "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io",
             size=9, colour=C["muted"], font=FONT)
    add_text(slide, Inches(11), Inches(7.18), Inches(2), Inches(0.25),
             f"MOSIC  ·  Jan + Feb 2026  ·  {page_num:02d}",
             size=9, colour=C["muted"], font=FONT, align=PP_ALIGN.RIGHT)


# ---------- chart helper ----------

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


# ---------- table helper ----------

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


# ---------- slides ----------

def slide_cover():
    slide = add_slide()
    # Solid blue background
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, C["primary"])
    # Decorative blobs
    add_oval(slide, Inches(8.5), Inches(-3.5), Inches(8.5), Inches(8.5),
             C["secondary"], transparency=0.78)
    add_oval(slide, Inches(-3), Inches(4), Inches(7), Inches(7),
             C["primary_2"], transparency=0.85)
    add_oval(slide, Inches(10), Inches(4.5), Inches(4), Inches(4),
             C["accent"], transparency=0.88)

    # Logo white pill
    add_rect(slide, Inches(0.9), Inches(2.3), Inches(3.9), Inches(1.7),
             C["white"], rounded=True)
    slide.shapes.add_picture(str(LOGO_BLUE),
                             Inches(1.1), Inches(2.55),
                             height=Inches(1.2))

    # Kicker
    add_text(slide, Inches(0.9), Inches(4.3), Inches(11), Inches(0.4),
             "MONTHLY PERFORMANCE REPORT",
             size=13, bold=True, colour=C["white"], font=FONT)
    # Big client
    add_text(slide, Inches(0.9), Inches(4.75), Inches(11), Inches(2.0),
             [src.CLIENT_NAME], size=44, bold=True, colour=C["white"],
             font=FONT, line_spacing=1.05)
    # Period in secondary cyan
    add_text(slide, Inches(0.9), Inches(6.55), Inches(11), Inches(0.5),
             src.PERIOD_LABEL,
             size=22, bold=True, colour=C["secondary"], font=FONT)


def slide_exec_summary(page=2):
    slide = add_slide()
    add_section_header(slide, "01  ·  OVERVIEW", "Executive summary",
                       page_num=page)

    # Three callout cards stacked
    paragraphs = [
        ("Traffic is up — conversion is the bottleneck.",
         "Total website visitors grew +13.4% YoY and organic search +5.6% YoY — both healthy signals. "
         "The booking funnel is leaking after the click: confirmed Cliniko bookings dropped −8.9% YoY, "
         "Google Ads phone calls −38.1% YoY, and total new patients −73.0% YoY."),
        ("People are reaching the site — landing pages aren't closing the deal.",
         "The fix is already in motion: search campaigns rebuilt, landing-page copy revised this period, "
         "Q1 marketing calendar complete, four new articles shipped, HotDoc account opened "
         "(15 bookings already booked at Essendon)."),
        ("Watch next month",
         "Phone-call recovery from the rebuilt Google Ads campaigns, "
         "and whether the new landing-page copy lifts the click-to-booking rate."),
    ]
    y = Inches(1.95)
    card_w = Inches(12.0)
    card_h = Inches(1.55)
    accent_colours = [C["primary"], C["secondary"], C["accent"]]
    for i, (headline, body) in enumerate(paragraphs):
        # Card with rounded background
        add_rect(slide, Inches(0.7), y, card_w, card_h, C["white"], rounded=True)
        # Left accent strip
        add_rect(slide, Inches(0.7), y, Inches(0.16), card_h, accent_colours[i])
        # Headline
        add_text(slide, Inches(1.0), y + Inches(0.18), card_w - Inches(0.5), Inches(0.45),
                 headline, size=15, bold=True, colour=C["ink"], font=FONT)
        # Body
        add_text(slide, Inches(1.0), y + Inches(0.62), card_w - Inches(0.5), card_h - Inches(0.7),
                 body, size=12, colour=C["muted"], font=FONT, line_spacing=1.3)
        y += card_h + Inches(0.15)

    add_footer(slide, page)


def slide_kpi(page=3):
    slide = add_slide()
    add_section_header(slide, "02  ·  SNAPSHOT",
                       "Period snapshot — Jan + Feb 2026", page_num=page)
    add_text(slide, Inches(0.6), Inches(1.85), Inches(11), Inches(0.35),
             "Year-on-year comparison vs Jan + Feb 2025",
             size=12, colour=C["muted"], font=FONT)

    kpis = [
        ("Website visitors",   src.visitors_now,  src.visitors_prev),
        ("Confirmed bookings", src.confirmed_now, src.confirmed_prev),
        ("Total new patients", src.new_total_now, src.new_total_prev),
        ("Google Ads calls",   src.calls_now,     src.calls_prev),
    ]
    card_w, card_h = Inches(2.95), Inches(2.7)
    gap = Inches(0.18)
    start_x = Inches(0.6)
    y = Inches(2.45)

    for i, (label, curr, prev) in enumerate(kpis):
        x = start_x + (card_w + gap) * i
        # Main card
        add_rect(slide, x, y, card_w, card_h, C["primary"], rounded=True)
        # Decorative inner blob
        add_oval(slide, x + card_w - Inches(1.3), y + card_h - Inches(1.3),
                 Inches(1.6), Inches(1.6), C["secondary"], transparency=0.78)
        # Top label
        add_text(slide, x + Inches(0.3), y + Inches(0.3), card_w - Inches(0.6), Inches(0.35),
                 label.upper(), size=9, bold=True,
                 colour=C["sky"], font=FONT)
        # Big value
        add_text(slide, x + Inches(0.3), y + Inches(0.65), card_w - Inches(0.6), Inches(1.1),
                 f"{curr:,}", size=52, bold=True,
                 colour=C["white"], font=FONT)
        # Delta
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


def _cats_vals(series, n=12):
    series = src.last_n(series, n)
    return [str(c) for c, _ in series], [int(v) for _, v in series]


def slide_chart_single(kicker, title, sub, subtitle, series, highlight,
                       caption, page):
    slide = add_slide()
    add_section_header(slide, kicker, title, page_num=page)
    if sub:
        add_text(slide, Inches(0.6), Inches(1.85), Inches(11.5), Inches(0.35),
                 sub, size=12, colour=C["muted"], font=FONT)
    cats, vals = _cats_vals(series)
    # Chart card backdrop
    add_rect(slide, Inches(0.5), Inches(2.25), Inches(12.3), Inches(4.45),
             C["white"], rounded=True)
    add_chart(slide, Inches(0.7), Inches(2.4), Inches(11.9), Inches(4.15),
              cats, vals, title=subtitle, highlight_set=highlight)
    if caption:
        add_text(slide, Inches(0.6), Inches(6.8), Inches(12.1), Inches(0.4),
                 caption, size=11, colour=C["muted"], font=FONT)
    add_footer(slide, page)


def slide_chart_pair(kicker, title, sub, datasets, page):
    slide = add_slide()
    add_section_header(slide, kicker, title, page_num=page)
    if sub:
        add_text(slide, Inches(0.6), Inches(1.85), Inches(11.5), Inches(0.35),
                 sub, size=12, colour=C["muted"], font=FONT)
    chart_w = Inches(6.0); chart_h = Inches(4.45)
    for i, (subtitle, series, hi) in enumerate(datasets):
        cats, vals = _cats_vals(series)
        x = Inches(0.5) + Inches(6.2) * i
        add_rect(slide, x, Inches(2.25), chart_w, chart_h, C["white"], rounded=True)
        add_chart(slide, x + Inches(0.15), Inches(2.4), chart_w - Inches(0.3), chart_h - Inches(0.3),
                  cats, vals, title=subtitle, highlight_set=hi)
    add_footer(slide, page)


def slide_top_pages(page=8):
    slide = add_slide()
    add_section_header(slide, "06  ·  CONTENT",
                       "Most viewed pages — Jan + Feb 2026", page_num=page)

    rows = [(p, f"{v:,}", f"{u:,}") for p, v, u in src.TOP_PAGES]
    # Card
    add_rect(slide, Inches(0.5), Inches(1.95), Inches(12.3), Inches(4.7),
             C["white"], rounded=True)
    add_table(slide, Inches(0.75), Inches(2.1), Inches(11.85), Inches(4.4),
              ["Page", "Views", "Active users"], rows, font_size=12)
    add_text(slide, Inches(0.6), Inches(6.8), Inches(12.1), Inches(0.4),
             "Practitioner pages still drive a meaningful share of traffic — Dr Jordan Pratt and Dr Zac Hussey both ranking top 10.",
             size=11, colour=C["muted"], font=FONT)
    add_footer(slide, page)


def slide_locations(page=10):
    slide = add_slide()
    add_section_header(slide, "07b  ·  LOCATIONS",
                       "New patients by location", page_num=page)
    add_text(slide, Inches(0.6), Inches(1.85), Inches(12), Inches(0.4),
             "Last 10 months from individual-counts source — does not yet include Jan/Feb 2026.",
             size=11, colour=C["muted"], font=FONT)

    chart_w = Inches(6.0); chart_h = Inches(4.45)
    for i, (label, series) in enumerate([
        ("Bourke St", src.NEW_PATIENTS_BOURKE),
        ("Essendon",  src.NEW_PATIENTS_ESSENDON),
    ]):
        cats, vals = _cats_vals(series)
        x = Inches(0.5) + Inches(6.2) * i
        add_rect(slide, x, Inches(2.3), chart_w, chart_h, C["white"], rounded=True)
        add_chart(slide, x + Inches(0.15), Inches(2.45), chart_w - Inches(0.3), chart_h - Inches(0.3),
                  cats, vals, title=label)
    add_footer(slide, page)


def slide_automations(page=11):
    slide = add_slide()
    add_section_header(slide, "08  ·  AUTOMATIONS",
                       "Cliniqapps email automations", page_num=page)
    add_text(slide, Inches(0.6), Inches(1.85), Inches(12), Inches(0.35),
             "Patients booked / appointments booked, last 7 months.",
             size=11, colour=C["muted"], font=FONT)

    automations = [
        ("DNA rebooker",              src.DNA_REBOOKER),
        ("Cancellation rebooker",     src.CANCEL_REBOOKER),
        ("Reactivation 3 – 6 mo",     src.REACT_3_6),
        ("Reactivation 6 – 12 mo",    src.REACT_6_12),
        ("Reactivation 12 mo +",      src.REACT_12_PLUS),
    ]
    col_w = Inches(4.0); col_h = Inches(2.35)
    gap_x = Inches(0.15); gap_y = Inches(0.2)
    start_x = Inches(0.45); start_y = Inches(2.3)
    for idx, (title, rows) in enumerate(automations):
        col = idx % 3; row = idx // 3
        x = start_x + (col_w + gap_x) * col
        y = start_y + (col_h + gap_y) * row
        # Card
        add_rect(slide, x, y, col_w, col_h, C["white"], rounded=True)
        # Title bar (small accent)
        add_rect(slide, x + Inches(0.15), y + Inches(0.18), Inches(0.16), Inches(0.16),
                 C["primary"], rounded=True)
        add_text(slide, x + Inches(0.4), y + Inches(0.12), col_w - Inches(0.5), Inches(0.3),
                 title, size=11, bold=True, colour=C["primary"], font=FONT)
        body_rows = [(m, str(p) if p is not None else "—",
                         str(a) if a is not None else "—") for m, p, a in rows]
        add_table(slide, x + Inches(0.15), y + Inches(0.5),
                  col_w - Inches(0.3), col_h - Inches(0.65),
                  ["Month", "Patients", "Apts"], body_rows, font_size=9)

    add_text(slide, Inches(0.45), Inches(7.0), Inches(12.4), Inches(0.3),
             "October was a strong reactivation month overall. The 12-months+ segment continues to underperform — worth A/B testing the message.",
             size=10, colour=C["muted"], font=FONT)
    add_footer(slide, page)


def slide_broadcast(page=12):
    slide = add_slide()
    add_section_header(slide, "09  ·  BROADCAST",
                       "Cliniqapps broadcast emails", page_num=page)

    def fmt_pct(p): return f"{p:.2f}%" if p is not None else "—"
    def fmt_int(n): return f"{n:,}" if n is not None else "—"

    rows = []
    for m, ws, wo, wc, xs, xo, xc in src.EMAIL_BROADCAST:
        rows.append((m, fmt_int(ws), fmt_pct(wo), fmt_pct(wc),
                        fmt_int(xs), fmt_pct(xo), fmt_pct(xc)))
    add_rect(slide, Inches(0.4), Inches(1.85), Inches(12.5), Inches(5.05),
             C["white"], rounded=True)
    add_table(slide, Inches(0.6), Inches(2.0), Inches(12.1), Inches(4.85),
              ["Month", "With apt — sends", "Open", "Click",
                       "Without apt — sends", "Open", "Click"],
              rows, font_size=10)
    add_footer(slide, page)


def slide_actioned(page=13):
    slide = add_slide()
    add_section_header(slide, "10  ·  ACTIONED",
                       "Actioned items this period", page_num=page)

    cols = [("Website development", src.WEBSITE_DEV_ITEMS, C["primary"]),
            ("Other",                src.OTHER_ITEMS,        C["accent"])]
    col_w = Inches(5.95); col_h = Inches(4.85)
    xs = [Inches(0.6), Inches(6.85)]
    for i, (title, items, accent) in enumerate(cols):
        x = xs[i]
        # Card
        add_rect(slide, x, Inches(1.95), col_w, col_h, C["white"], rounded=True)
        # Accent stripe
        add_rect(slide, x, Inches(1.95), Inches(0.16), col_h, accent)
        # Title
        add_text(slide, x + Inches(0.4), Inches(2.1), col_w - Inches(0.5), Inches(0.4),
                 title, size=15, bold=True, colour=accent, font=FONT)
        # Items
        y = Inches(2.65)
        for raw in items:
            text = (raw.replace("<em>", "").replace("</em>", "")
                       .replace("<strong>", "").replace("</strong>", ""))
            # Bullet dot
            add_oval(slide, x + Inches(0.45), y + Inches(0.1),
                     Inches(0.13), Inches(0.13), accent)
            add_text(slide, x + Inches(0.7), y, col_w - Inches(0.85), Inches(0.5),
                     text, size=12, colour=C["ink"], font=FONT,
                     line_spacing=1.25)
            y += Inches(0.42)
    add_footer(slide, page)


def slide_appendix(page=14):
    slide = add_slide()
    add_section_header(slide, "11  ·  APPENDIX",
                       "HotDoc bookings", page_num=page)

    # Big stat card
    card_x = Inches(3.5); card_y = Inches(2.3)
    card_w = Inches(6.3); card_h = Inches(3.7)
    add_rect(slide, card_x, card_y, card_w, card_h, C["primary"], rounded=True)
    # Inner blob
    add_oval(slide, card_x + Inches(4.5), card_y - Inches(1),
             Inches(4), Inches(4), C["secondary"], transparency=0.8)
    # Big number
    add_text(slide, card_x, card_y + Inches(0.5), card_w, Inches(1.8),
             "15", size=110, bold=True,
             colour=C["white"], font=FONT, align=PP_ALIGN.CENTER)
    add_text(slide, card_x, card_y + Inches(2.4), card_w, Inches(0.4),
             "BOOKINGS VIA HOTDOC",
             size=14, bold=True, colour=C["secondary"],
             font=FONT, align=PP_ALIGN.CENTER)
    add_text(slide, card_x, card_y + Inches(2.85), card_w, Inches(0.4),
             "Essendon location",
             size=15, colour=C["white"], font=FONT, align=PP_ALIGN.CENTER)

    add_text(slide, Inches(0.6), Inches(6.45), Inches(12.1), Inches(0.4),
             "HotDoc account opened this period — 15 patients booked through the channel at Essendon.",
             size=12, colour=C["muted"], font=FONT, align=PP_ALIGN.CENTER)
    add_footer(slide, page)


# ---------- build ----------

slide_cover()
slide_exec_summary(page=2)
slide_kpi(page=3)

slide_chart_single(
    "03  ·  CLINIKO", "Cliniko booking page",
    "Confirmed appointment bookings — last 12 months",
    "Confirmed bookings",
    src.CONFIRMED_BOOKINGS, src.JF_2026,
    "Jan + Feb 2026 highlighted in orange.", page=4,
)
slide_chart_single(
    "03b  ·  CLINIKO", "Cliniko booking page",
    "Entered the booking page — last 12 months",
    "Entered booking page",
    src.ENTERED_BOOKING_PAGE, src.JF_2026,
    "December 2025 outperformed December 2024 (370 vs 236, +56.8%).", page=5,
)
slide_chart_single(
    "04  ·  GOOGLE ADS", "Google Ads — phone calls",
    "Click volume healthy but call conversion has dropped.",
    "Phone calls",
    src.GADS_PHONE_CALLS, src.JF_2026,
    "Action: rebuild search campaigns, revise landing-page copy.", page=6,
)
slide_chart_pair(
    "05  ·  WEBSITE", "Website traffic (AUS)",
    "Last 12 months — Jan + Feb 2026 highlighted in orange.",
    [
        ("Total visitors", src.WEBSITE_VISITORS, src.JF_2026),
        ("Organic search", src.ORGANIC_SEARCH,   src.JF_2026),
    ], page=7,
)
slide_top_pages(page=8)
slide_chart_pair(
    "07  ·  NEW BOOKINGS", "New bookings",
    "From Google vs total — last 12 months.",
    [
        ("New patients from Google", src.NEW_PATIENTS_GOOGLE, src.JF_2026),
        ("Total new patients",       src.TOTAL_NEW_PATIENTS,  src.JF_2026),
    ], page=9,
)
slide_locations(page=10)
slide_automations(page=11)
slide_broadcast(page=12)
slide_actioned(page=13)
slide_appendix(page=14)


# ---------- save ----------
out = HERE / "report.pptx"
try:
    prs.save(str(out))
except PermissionError:
    out = HERE / "report-v2.pptx"
    prs.save(str(out))
print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
