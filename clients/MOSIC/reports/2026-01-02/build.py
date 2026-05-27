"""
Renders MOSIC's January + February 2026 report from PPTX-extracted data
through the Locate Digital branded report template.

Self-contained — uses _brand/brand.json and _templates/report/ for styling.
"""
from __future__ import annotations
import base64
import json
import mimetypes
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
BRAND_DIR = AGENCY_ROOT / "_brand"
TEMPLATE_DIR = AGENCY_ROOT / "_templates" / "report"

CLIENT_NAME = "Melbourne Osteopathy Sports Injury Centre"
PERIOD_LABEL = "January + February 2026"
PERIOD_TITLE = f"MOSIC — Monthly Update — {PERIOD_LABEL}"


# ---------- helpers ----------

def load_brand() -> dict:
    return json.loads((BRAND_DIR / "brand.json").read_text(encoding="utf-8"))

def logo_data_uri(brand: dict, key: str = "inverse") -> str:
    logo_path = BRAND_DIR / brand["logo"][key]
    mime = mimetypes.guess_type(logo_path.name)[0] or "image/png"
    data = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"

def render_css(brand: dict) -> str:
    css = (TEMPLATE_DIR / "style.css").read_text(encoding="utf-8")
    tokens = {
        **brand["colours"],
        "heading_font":     brand["fonts"]["heading"]["family"],
        "heading_fallback": brand["fonts"]["heading"]["fallback"],
        "body_font":        brand["fonts"]["body"]["family"],
        "body_fallback":    brand["fonts"]["body"]["fallback"],
    }
    for k, v in tokens.items():
        css = css.replace("{{" + k + "}}", v)
    return css

def fmt_int(n) -> str:
    if n is None or n == "":
        return "—"
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)

def delta(curr, prev) -> str:
    if not prev or curr is None:
        return ""
    pct = (curr - prev) / prev * 100
    if pct > 0:
        return f'<span class="up">↑ {abs(pct):.1f}% YoY</span>'
    if pct < 0:
        return f'<span class="down">↓ {abs(pct):.1f}% YoY</span>'
    return '<span class="flat">→ flat</span>'

def bar_chart(rows, highlight=None) -> str:
    """rows: list of (label, value). highlight: set of labels to mark in accent."""
    rows = [(str(lbl), v) for lbl, v in rows if v is not None]
    if not rows:
        return ""
    max_v = max(v for _, v in rows) or 1
    out = ['<div class="chart">']
    for lbl, val in rows:
        pct = (val / max_v) * 100
        is_hi = highlight and lbl in highlight
        fill_style = (
            f"width:{pct:.1f}%;"
            + (" background: linear-gradient(90deg, #ff5900 0%, #ff8a4a 120%);" if is_hi else "")
        )
        out.append(
            f'<div class="row"><div class="label">{lbl}</div>'
            f'<div class="bar"><div class="fill" style="{fill_style}"></div></div>'
            f'<div class="value">{fmt_int(val)}</div></div>'
        )
    out.append('</div>')
    return "\n".join(out)

def kpi_grid(items) -> str:
    """items: list of (label, big_value, sub_html)."""
    out = ['<ul class="kpi">']
    for label, value, sub in items:
        out.append(f'<li><strong>{value}</strong>{label}<div style="margin-top:8px;font-size:12.5px">{sub}</div></li>')
    out.append('</ul>')
    return "\n".join(out)

def render_table(headers, rows) -> str:
    out = ['<table>', '<thead><tr>']
    for h in headers:
        out.append(f'<th>{h}</th>')
    out.append('</tr></thead><tbody>')
    for r in rows:
        out.append('<tr>')
        for cell in r:
            out.append(f'<td>{cell if cell not in (None, "") else "—"}</td>')
        out.append('</tr>')
    out.append('</tbody></table>')
    return "\n".join(out)


# ---------- source data (extracted from PPTX) ----------

# Reverse-chronological as in the deck. Top = most recent = Feb 2026.
# We render charts oldest → newest (so trends read left → right naturally).

def chrono(rows):
    """Reverse so charts read oldest → newest."""
    return list(reversed(rows))

def last_n(rows, n=12):
    """Take last n entries (most recent), preserving order."""
    return rows[-n:] if len(rows) > n else rows

CONFIRMED_BOOKINGS = chrono([
    ("Feb 26", 66), ("Jan 26", 88),
    ("Dec 25", 98), ("Nov 25", 63), ("Oct 25", 85), ("Sep 25", 56),
    ("Aug 25", 86), ("Jul 25", 87), ("Jun 25", 88), ("May 25", 96),
    ("Apr 25", 95), ("Mar 25", 65),
    ("Feb 25", 68), ("Jan 25", 101), ("Dec 24", 63),
])

ENTERED_BOOKING_PAGE = chrono([
    ("Feb 26", 260), ("Jan 26", 366),
    ("Dec 25", 370), ("Nov 25", 330), ("Oct 25", 365), ("Sep 25", 354),
    ("Aug 25", 469), ("Jul 25", 371), ("Jun 25", 367), ("May 25", 385),
    ("Apr 25", 447), ("Mar 25", 375),
    ("Feb 25", 368), ("Jan 25", 406), ("Dec 24", 236),
])

GADS_PHONE_CALLS = chrono([
    ("Feb 26", 23), ("Jan 26", 29),
    ("Dec 25", 8),  ("Nov 25", 23), ("Oct 25", 27), ("Sep 25", 37),
    ("Aug 25", 24), ("Jul 25", 31), ("Jun 25", 30), ("May 25", 29),
    ("Apr 25", 24), ("Mar 25", 25),
    ("Feb 25", 31), ("Jan 25", 53), ("Dec 24", 23),
])

WEBSITE_VISITORS = chrono([
    ("Feb 26", 1515), ("Jan 26", 1799),
    ("Dec 25", 1500), ("Nov 25", 1584), ("Oct 25", 1786), ("Sep 25", 1275),
    ("Aug 25", 1307), ("Jul 25", 1345), ("Jun 25", 1144), ("May 25", 1264),
    ("Apr 25", 1322), ("Mar 25", 1332),
    ("Feb 25", 1511), ("Jan 25", 1411),
])

ORGANIC_SEARCH = chrono([
    ("Feb 26", 713), ("Jan 26", 744),
    ("Dec 25", 600), ("Nov 25", 713), ("Oct 25", 795), ("Sep 25", 652),
    ("Aug 25", 601), ("Jul 25", 626), ("Jun 25", 588), ("May 25", 638),
    ("Apr 25", 668), ("Mar 25", 638),
    ("Feb 25", 629), ("Jan 25", 751),
])

NEW_PATIENTS_GOOGLE = chrono([
    ("Feb 26", 2), ("Jan 26", 2),
    ("Dec 25", 9), ("Nov 25", 4), ("Oct 25", 6), ("Sep 25", 14),
    ("Aug 25", 15), ("Jul 25", 14), ("Jun 25", 11), ("May 25", 14),
    ("Apr 25", 8), ("Mar 25", 2),
    ("Feb 25", 22), ("Jan 25", 7),
])

TOTAL_NEW_PATIENTS = chrono([
    ("Feb 26", 13), ("Jan 26", 7),
    ("Dec 25", 18), ("Nov 25", 20), ("Oct 25", 22), ("Sep 25", 41),
    ("Aug 25", 37), ("Jul 25", 38), ("Jun 25", 24), ("May 25", 45),
    ("Apr 25", 27), ("Mar 25", 8),
    ("Feb 25", 47), ("Jan 25", 27),
])

# Location data — deck shows Sep 2025 back to Dec 2024 only (different source cutoff)
NEW_PATIENTS_BOURKE = chrono([
    ("Sep 25", 21), ("Aug 25", 17), ("Jul 25", 15), ("Jun 25", 15),
    ("May 25", 34), ("Apr 25", 28), ("Mar 25", 22),
    ("Feb 25", 40), ("Jan 25", 37), ("Dec 24", 25),
])
NEW_PATIENTS_ESSENDON = chrono([
    ("Sep 25", 2), ("Aug 25", 10), ("Jul 25", 6), ("Jun 25", 6),
    ("May 25", 8), ("Apr 25", 8), ("Mar 25", 1),
    ("Feb 25", 5), ("Jan 25", 11), ("Dec 24", 7),
])

# Cliniqapps automation: (month, patients_booked, appointments_booked)
DNA_REBOOKER = [
    ("Feb 26", 3, 4), ("Jan 26", 6, 10), ("Dec 25", 4, 6),
    ("Nov 25", 5, 10), ("Oct 25", 4, 11), ("Sep 25", 4, 13), ("Aug 25", 6, 13),
]
CANCEL_REBOOKER = [
    ("Feb 26", 10, 20), ("Jan 26", 12, 24), ("Dec 25", 10, 22),
    ("Nov 25", 13, 27), ("Oct 25", 16, 56), ("Sep 25", 14, 30), ("Aug 25", 23, 50),
]
REACT_3_6 = [
    ("Feb 26", 5, 6), ("Jan 26", 10, 14), ("Dec 25", 3, 3),
    ("Nov 25", 9, 15), ("Oct 25", 14, 25), ("Sep 25", 6, 10), ("Aug 25", 6, 8),
]
REACT_6_12 = [
    ("Feb 26", 3, 4), ("Jan 26", 3, 3), ("Dec 25", 1, 1),
    ("Nov 25", 4, 7), ("Oct 25", 11, 25), ("Sep 25", None, None), ("Aug 25", 4, 11),
]
REACT_12_PLUS = [
    ("Feb 26", 2, 4), ("Jan 26", 2, 6), ("Dec 25", 3, 4),
    ("Nov 25", 2, 2), ("Oct 25", 2, 2), ("Sep 25", 1, 1), ("Aug 25", 3, 5),
]

# Cliniqapps broadcast email: (month, with_apt sends, open%, click%, without_apt sends, open%, click%)
EMAIL_BROADCAST = [
    ("Dec 25 (EOY email)", 4475, 33.97, 0.83, 3004, 21.47, 1.53),
    ("Nov 25",             None, None,  None, None, None,  None),
    ("Oct 25",             4456, 36.94, 0.79, 3023, 23.55, 0.63),
    ("Sep 25",             4467, 34.21, 0.76, 3044, 22.37, 0.66),
    ("Aug 25",             4452, 44.41, 0.58, 3067, 27.19, 0.39),
    ("Jul 25",             4435, 36.78, 0.72, 3084, 23.09, 0.49),
    ("Jun 25",             None, None,  None, None, None,  None),
    ("May 25",             4398, 34.61, 0.89, 3089, 22.05, 0.65),
    ("Apr 25",             4411, 40.81, 0.79, 3107, 24.72, 0.39),
    ("Mar 25",             4404, 33.22, 0.70, 3123, 22.29, 0.61),
    ("Feb 25",             4405, 32.85, 3.27, 3148, 23.06, 3.11),
    ("Jan 25",             4449, 33.56, 0.92, 3232, 23.95, 0.50),
]

# GA4 Top Pages screenshot (slide 6) - representative top results from the table image
TOP_PAGES = [
    ("Home page", 4076, 2982),
    ("/melbourne-osteopath-sports-injury-cbd", 1276, 1148),
    ("/dr-karl-mclachlan", 779, 681),
    ("/about", 1306, 1148),
    ("/booknow", 1276, 1083),
    ("/dr-corey-fitzgerald", 779, 612),
    ("/services", 769, 690),
    ("/dr-andrew-ellis", 605, 524),
    ("/dr-jordan-pratt", 522, 471),
    ("/dr-zac-hussey", 459, 402),
]

WEBSITE_DEV_ITEMS = [
    "Uploaded — <em>What to expect at your first osteopathy appointment</em>",
    "Uploaded — <em>Australian Open 2026 is here</em>",
    "Uploaded — <em>How Osteopathy Supports Better Movement</em>",
    "Uploaded — <em>Low Impact Exercise to Support your golf journey</em>",
    "Updated landing pages to align with target search keywords",
]

OTHER_ITEMS = [
    "Created the Marketing Calendar for MOSIC — <strong>Q1 complete</strong>",
    "Updated Google security",
    "Ongoing Google Ads optimisation",
    "Ongoing social media creation and posting",
    "Ongoing GMB posting",
    "Update and renew all automation rework (testimonials and reviews)",
    "Google Ads — created new campaigns and adjusted copy",
    "Created the HotDoc account for MOSIC",
]


# ---------- aggregations ----------

def sum_window(series, labels):
    return sum(v for lbl, v in series if lbl in labels and v is not None)

JF_2026 = {"Jan 26", "Feb 26"}
JF_2025 = {"Jan 25", "Feb 25"}

confirmed_now  = sum_window(CONFIRMED_BOOKINGS, JF_2026)   # 154
confirmed_prev = sum_window(CONFIRMED_BOOKINGS, JF_2025)   # 169
entered_now    = sum_window(ENTERED_BOOKING_PAGE, JF_2026) # 626
entered_prev   = sum_window(ENTERED_BOOKING_PAGE, JF_2025) # 774
calls_now      = sum_window(GADS_PHONE_CALLS, JF_2026)     # 52
calls_prev     = sum_window(GADS_PHONE_CALLS, JF_2025)     # 84
visitors_now   = sum_window(WEBSITE_VISITORS, JF_2026)     # 3314
visitors_prev  = sum_window(WEBSITE_VISITORS, JF_2025)     # 2922
organic_now    = sum_window(ORGANIC_SEARCH, JF_2026)       # 1457
organic_prev   = sum_window(ORGANIC_SEARCH, JF_2025)       # 1380
new_g_now      = sum_window(NEW_PATIENTS_GOOGLE, JF_2026)  # 4
new_g_prev     = sum_window(NEW_PATIENTS_GOOGLE, JF_2025)  # 29
new_total_now  = sum_window(TOTAL_NEW_PATIENTS, JF_2026)   # 20
new_total_prev = sum_window(TOTAL_NEW_PATIENTS, JF_2025)   # 74


# ---------- body assembly ----------

def build_body() -> str:
    parts = []

    # ---- Executive summary ----
    parts.append('<h2>Executive summary</h2>')
    parts.append(
        '<p>Traffic is up, but conversion is the bottleneck. Total website '
        'visitors grew <strong>+13.4% YoY</strong> and organic search '
        '<strong>+5.6% YoY</strong> — both healthy signals. The booking funnel '
        'is leaking after the click: confirmed Cliniko bookings dropped '
        '<strong>−8.9% YoY</strong>, Google Ads phone calls <strong>−38.1% '
        'YoY</strong>, and total new patients <strong>−73.0% YoY</strong>.</p>'
    )
    parts.append(
        '<p>Diagnosis: people are reaching the site but the landing pages '
        'aren\'t closing the deal. The fix is already in motion — search '
        'campaigns are being rebuilt and landing-page copy revised this '
        'period. Q1 marketing calendar is complete; four new articles '
        'shipped; a HotDoc account was opened (15 bookings already booked '
        'at Essendon).</p>'
    )
    parts.append(
        '<p>Watch next month: phone-call recovery from the rebuilt Google Ads '
        'campaigns, and whether the new landing-page copy lifts the '
        'click-to-booking rate.</p>'
    )

    # ---- Snapshot (KPI grid) ----
    parts.append('<h2>Period snapshot — Jan + Feb 2026</h2>')
    parts.append('<p>Year-on-year comparison against Jan + Feb 2025.</p>')
    parts.append(kpi_grid([
        ("Website visitors",   fmt_int(visitors_now),  delta(visitors_now, visitors_prev)),
        ("Confirmed bookings", fmt_int(confirmed_now), delta(confirmed_now, confirmed_prev)),
        ("Total new patients", fmt_int(new_total_now), delta(new_total_now, new_total_prev)),
        ("Google Ads calls",   fmt_int(calls_now),     delta(calls_now, calls_prev)),
    ]))

    # ---- Cliniko booking page ----
    parts.append('<h2>Cliniko booking page</h2>')
    parts.append('<h3>Confirmed appointment bookings</h3>')
    parts.append(bar_chart(last_n(CONFIRMED_BOOKINGS), highlight=JF_2026))
    parts.append('<h3>Entered the booking page</h3>')
    parts.append(bar_chart(last_n(ENTERED_BOOKING_PAGE), highlight=JF_2026))
    parts.append(
        '<p><em>Steady booking-page entries across the quarter; '
        'December 2025 outperformed December 2024 (370 vs 236, +56.8%).</em></p>'
    )

    # ---- Google Ads ----
    parts.append('<h2>Google Ads</h2>')
    parts.append('<h3>Phone calls</h3>')
    parts.append(bar_chart(last_n(GADS_PHONE_CALLS), highlight=JF_2026))
    parts.append(
        '<p><em>Click volume is healthy but call conversion has dropped — '
        'landing-page copy needs to be more compelling. Action: rebuild search '
        'campaigns and revise landing-page messaging.</em></p>'
    )

    # ---- Website traffic ----
    parts.append('<h2>Website traffic (AUS)</h2>')
    parts.append('<h3>Total visitors</h3>')
    parts.append(bar_chart(last_n(WEBSITE_VISITORS), highlight=JF_2026))
    parts.append('<h3>Organic search</h3>')
    parts.append(bar_chart(last_n(ORGANIC_SEARCH), highlight=JF_2026))
    parts.append(
        '<p><em>Significantly more traffic this quarter compared to the '
        'same quarter last year. A large portion is paid; direct traffic '
        'has grown noticeably.</em></p>'
    )

    # ---- Most viewed pages ----
    parts.append('<h2>Most viewed pages — Jan + Feb 2026</h2>')
    parts.append(render_table(
        ["Page", "Views", "Active users"],
        [(p, fmt_int(v), fmt_int(u)) for p, v, u in TOP_PAGES],
    ))
    parts.append(
        '<p><em>Practitioner pages continue to drive a meaningful share of '
        'traffic; Dr Jordan Pratt and Dr Zac Hussey both still ranking in the '
        'top 10.</em></p>'
    )

    # ---- New bookings ----
    parts.append('<h2>New bookings</h2>')
    parts.append('<h3>New patients from Google</h3>')
    parts.append(bar_chart(last_n(NEW_PATIENTS_GOOGLE), highlight=JF_2026))
    parts.append('<h3>Total new patients</h3>')
    parts.append(bar_chart(last_n(TOTAL_NEW_PATIENTS), highlight=JF_2026))
    parts.append(
        '<p><em>Conversion rate has fallen off — consistent with the Google '
        'Ads call-volume drop. Same root cause: landing-page conversion.</em></p>'
    )

    parts.append('<h3>New patients by location <span style="font-weight:500;color:#63666b;text-transform:none;letter-spacing:0">(latest 10 months from individual-counts source — does not yet include Jan/Feb 2026)</span></h3>')
    parts.append('<h4 style="margin:14px 0 6px;color:#0d0d0d;font-family:Plus Jakarta Sans;font-size:13px;letter-spacing:0.4px">Bourke St</h4>')
    parts.append(bar_chart(last_n(NEW_PATIENTS_BOURKE)))
    parts.append('<h4 style="margin:14px 0 6px;color:#0d0d0d;font-family:Plus Jakarta Sans;font-size:13px;letter-spacing:0.4px">Essendon</h4>')
    parts.append(bar_chart(last_n(NEW_PATIENTS_ESSENDON)))

    # ---- Cliniqapps automations ----
    parts.append('<h2>Cliniqapps email automations</h2>')

    def auto_table(rows):
        return render_table(
            ["Month", "Patients", "Apts"],
            [(m, fmt_int(p), fmt_int(a)) for m, p, a in rows],
        )

    automations = [
        ("DNA rebooker — all patients",      DNA_REBOOKER),
        ("Cancellation rebooker — all",      CANCEL_REBOOKER),
        ("Reactivation 3 – 6 months",        REACT_3_6),
        ("Reactivation 6 – 12 months",       REACT_6_12),
        ("Reactivation 12 months +",         REACT_12_PLUS),
    ]

    parts.append('<div class="auto-grid">')
    for title, rows in automations:
        parts.append(
            '<div class="auto-card">'
            f'<h3>{title}</h3>'
            f'{auto_table(rows)}'
            '</div>'
        )
    parts.append('</div>')

    parts.append(
        '<p><em>October was a strong reactivation month overall. '
        'The 12-months+ reactivation segment continues to underperform the '
        'shorter-window segments — worth A/B testing the message.</em></p>'
    )

    # ---- Cliniqapps broadcast ----
    parts.append('<h2>Cliniqapps broadcast emails</h2>')
    def fmt_pct(p):
        if p is None:
            return "—"
        return f"{p:.2f}%"
    parts.append(render_table(
        ["Month", "With apt — sends", "Open", "Click", "Without apt — sends", "Open", "Click"],
        [
            (m, fmt_int(ws), fmt_pct(wo), fmt_pct(wc),
                fmt_int(xs), fmt_pct(xo), fmt_pct(xc))
            for m, ws, wo, wc, xs, xo, xc in EMAIL_BROADCAST
        ],
    ))

    # ---- Actioned items ----
    parts.append('<h2>Actioned items</h2>')
    parts.append('<h3>Website development</h3>')
    parts.append('<ul>' + "".join(f'<li>{x}</li>' for x in WEBSITE_DEV_ITEMS) + '</ul>')
    parts.append('<h3>Other</h3>')
    parts.append('<ul>' + "".join(f'<li>{x}</li>' for x in OTHER_ITEMS) + '</ul>')

    # ---- Appendix ----
    parts.append('<h2>Appendix — HotDoc bookings</h2>')
    parts.append('<p><strong>15 bookings</strong> via HotDoc — Essendon location.</p>')

    return "\n".join(parts)


def render() -> str:
    brand = load_brand()
    template = (TEMPLATE_DIR / "template.html").read_text(encoding="utf-8")

    fields = {
        "title":                 PERIOD_TITLE,
        "client_name":           CLIENT_NAME,
        "period_label":          PERIOD_LABEL,
        "css":                   render_css(brand),
        "body":                  build_body(),
        "logo_inverse_data_uri": logo_data_uri(brand, "body"),  # Logo flat white/Transparent Logo.png — sits on white pill in header
        "heading_font_url":      brand["fonts"]["heading"]["google_url"],
        "body_font_url":         brand["fonts"]["body"]["google_url"],
        "generated_at":          datetime.now().strftime("%d %B %Y").lstrip("0"),
    }

    out = template
    for k, v in fields.items():
        out = out.replace("{{" + k + "}}", v)
    return out


if __name__ == "__main__":
    html = render()
    out_path = HERE / "report.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path} ({len(html):,} chars)")
