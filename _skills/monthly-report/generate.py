"""Generate a monthly client report combining GA4 + Cliniko data.

Usage:
    python generate.py <client-env-path> [YYYY-MM]

If YYYY-MM is omitted, generates for the previous full calendar month.
Output: clients/<client>/reports/YYYY-MM/report.md (+ branded report.html)
"""
import base64
import json
import mimetypes
import os
import re
import sys
from collections import Counter, defaultdict
from calendar import monthrange
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
import markdown

sys.path.insert(0, str(Path(__file__).parent))
import cliniko_client
import ga4_client


AGENCY_ROOT = Path(__file__).resolve().parents[2]
BRAND_DIR = AGENCY_ROOT / "_brand"
TEMPLATE_DIR = AGENCY_ROOT / "_templates" / "report"


def load_brand() -> dict:
    return json.loads((BRAND_DIR / "brand.json").read_text(encoding="utf-8"))


def logo_data_uri(brand: dict, key: str = "body") -> str:
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


def md_to_html(md_text: str, client_name: str, period_label: str) -> str:
    brand = load_brand()
    body_html = markdown.markdown(md_text, extensions=["tables"])
    # Strip the markdown title block — the cover header replaces it.
    body_html = re.sub(
        r"^\s*<h1>[^<]*</h1>\s*<h2>[^<]*</h2>\s*(<hr\s*/?>)?",
        "",
        body_html,
        count=1,
    )
    # Promote the headline list (first <ul> after Headline heading) to KPI cards.
    body_html = re.sub(
        r'(<h2>Headline</h2>\s*)<ul>',
        r'\1<ul class="kpi">',
        body_html,
        count=1,
    )
    # Drop the trailing "Generated ..." paragraph — the footer shows it.
    body_html = re.sub(r"<p><em>Generated[^<]*</em></p>\s*$", "", body_html)

    template = (TEMPLATE_DIR / "template.html").read_text(encoding="utf-8")
    fields = {
        "title":                  f"{client_name} — {period_label}",
        "client_name":            client_name,
        "period_label":           period_label,
        "heading_font_url":       brand["fonts"]["heading"]["google_url"],
        "body_font_url":          brand["fonts"]["body"]["google_url"],
        "css":                    render_css(brand),
        "logo_inverse_data_uri":  logo_data_uri(brand, "inverse"),
        "body":                   body_html,
        "generated_at":           datetime.now(tz=timezone.utc).strftime("%-d %b %Y") if os.name != "nt"
                                  else datetime.now(tz=timezone.utc).strftime("%#d %b %Y"),
    }
    out = template
    for k, v in fields.items():
        out = out.replace("{{" + k + "}}", v)
    return out


def parse_args():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    env_path = Path(sys.argv[1])
    if not env_path.exists():
        print(f"ERROR: env file not found: {env_path}")
        sys.exit(1)
    if len(sys.argv) >= 3:
        year, month = map(int, sys.argv[2].split("-"))
    else:
        today = datetime.now()
        first_this = today.replace(day=1)
        last_prev = (first_this.replace(day=1)).replace(day=1)
        # previous month
        if first_this.month == 1:
            year, month = first_this.year - 1, 12
        else:
            year, month = first_this.year, first_this.month - 1
    return env_path, year, month


def month_window(year: int, month: int):
    last_day = monthrange(year, month)[1]
    start = datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc)
    end = datetime(year, month, last_day, 23, 59, 59, tzinfo=timezone.utc)
    return start, end


def prev_month(year: int, month: int):
    if month == 1:
        return year - 1, 12
    return year, month - 1


def delta(curr: float, prev: float) -> str:
    """Return an HTML span with up/down arrow + percent. Empty if no prev baseline."""
    if not prev:
        return ""
    pct = (curr - prev) / prev * 100
    if pct > 0:
        return f'<span class="up">↑ {abs(pct):.1f}% vs prev</span>'
    if pct < 0:
        return f'<span class="down">↓ {abs(pct):.1f}% vs prev</span>'
    return '<span class="flat">→ flat</span>'


def fmt_int(n) -> str:
    return f"{int(n):,}"


def bar_chart(rows, mono_label: bool = False) -> str:
    """rows: list of (label, value). Returns raw HTML for a horizontal bar chart."""
    rows = [(str(lbl), int(val)) for lbl, val in rows if val is not None]
    if not rows:
        return ""
    max_v = max(v for _, v in rows) or 1
    out = ['<div class="chart">']
    for lbl, val in rows:
        pct = (val / max_v) * 100
        label_html = f"<code>{lbl}</code>" if mono_label else lbl
        out.append(
            f'<div class="row">'
            f'<div class="label">{label_html}</div>'
            f'<div class="bar"><div class="fill" style="width:{pct:.1f}%"></div></div>'
            f'<div class="value">{fmt_int(val)}</div>'
            f'</div>'
        )
    out.append('</div>')
    return "\n".join(out)


def stacked_bar(segments) -> str:
    """segments: list of (label, value, hex_colour). Returns a single horizontal stacked bar."""
    segments = [(lbl, int(v), c) for lbl, v, c in segments if v is not None]
    total = sum(v for _, v, _ in segments) or 1
    bars = []
    legend = []
    for lbl, v, colour in segments:
        pct = (v / total) * 100
        bars.append(f'<div class="seg" style="width:{pct:.2f}%; background:{colour}"></div>')
        legend.append(
            f'<span class="leg-item">'
            f'<span class="leg-dot" style="background:{colour}"></span>'
            f'{lbl} <strong>{fmt_int(v)}</strong>'
            f'</span>'
        )
    return (
        '<div class="stacked-bar">'
        f'<div class="track">{"".join(bars)}</div>'
        f'<div class="legend">{"".join(legend)}</div>'
        '</div>'
    )


# --- Cliniko aggregation ---

def cliniko_summary(client: cliniko_client.ClinikoClient, start: datetime, end: datetime):
    appts = client.appointments_in_range(start, end)
    cancellations = client.cancellations_in_range(start, end)
    patients = client.patients_created_in_range(start, end)
    businesses = {b["id"]: b["business_name"] for b in client.businesses()}
    practitioners = {
        p["id"]: f"{p.get('first_name','').strip()} {p.get('last_name','').strip()}".strip()
        for p in client.practitioners()
    }

    def _id(field):
        link = (field or {}).get("links", {}).get("self") or ""
        return link.rsplit("/", 1)[-1] if link else None

    no_show = sum(1 for a in appts if a.get("did_not_arrive"))
    held = len(appts) - no_show

    by_business = Counter()
    by_practitioner = Counter()
    for a in appts:
        bid = _id(a.get("business"))
        pid = _id(a.get("practitioner"))
        if bid in businesses:
            by_business[businesses[bid]] += 1
        if pid in practitioners:
            by_practitioner[practitioners[pid]] += 1

    return {
        "appointments_held": held,
        "appointments_cancelled": len(cancellations),
        "appointments_no_show": no_show,
        "new_patients": len(patients),
        "by_business": dict(by_business.most_common()),
        "by_practitioner": dict(by_practitioner.most_common()),
    }


# --- GA4 aggregation ---

def ga4_summary(client, property_id: str, start: str, end: str):
    totals = ga4_client.run(
        client, property_id, start, end,
        dimensions=[],
        metrics=["sessions", "totalUsers", "newUsers", "engagedSessions", "conversions"],
    )
    totals_row = ga4_client.to_rows(totals)
    totals_data = totals_row[0] if totals_row else {
        "sessions": 0, "totalUsers": 0, "newUsers": 0, "engagedSessions": 0, "conversions": 0,
    }

    sources = ga4_client.run(
        client, property_id, start, end,
        dimensions=["sessionDefaultChannelGroup"],
        metrics=["sessions"],
        order_by="sessions",
        limit=10,
    )
    pages = ga4_client.run(
        client, property_id, start, end,
        dimensions=["landingPagePlusQueryString"],
        metrics=["sessions"],
        order_by="sessions",
        limit=10,
    )
    return {
        "totals": totals_data,
        "channels": ga4_client.to_rows(sources),
        "top_pages": ga4_client.to_rows(pages),
    }


# --- Report rendering ---

def render(client_name: str, year: int, month: int, ga4: dict, ga4_prev: dict, cli: dict, cli_prev: dict) -> str:
    month_label = datetime(year, month, 1).strftime("%B %Y")
    t = ga4["totals"]
    tp = ga4_prev["totals"]

    lines = []
    lines.append(f"# {client_name} — Monthly Report")
    lines.append(f"## {month_label}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Headline
    lines.append("## Headline")
    lines.append("")
    def _kpi(value, label, d):
        suffix = f" {d}" if d else ""
        return f"- **{value}** {label}{suffix}"
    lines.append(_kpi(fmt_int(t['sessions']),            "website sessions",  delta(t['sessions'],   tp.get('sessions', 0))))
    lines.append(_kpi(fmt_int(t['totalUsers']),          "unique visitors",   delta(t['totalUsers'], tp.get('totalUsers', 0))))
    lines.append(_kpi(fmt_int(cli['new_patients']),      "new patients",      delta(cli['new_patients'],      cli_prev['new_patients'])))
    lines.append(_kpi(fmt_int(cli['appointments_held']), "appointments held", delta(cli['appointments_held'], cli_prev['appointments_held'])))
    lines.append("")

    # Website
    lines.append("## Website (GA4)")
    lines.append("")
    lines.append("| Metric | This month | Prev month | Change |")
    lines.append("|---|---:|---:|---:|")
    for label, key in [
        ("Sessions", "sessions"),
        ("Users", "totalUsers"),
        ("New users", "newUsers"),
        ("Engaged sessions", "engagedSessions"),
        ("Conversions", "conversions"),
    ]:
        curr = t.get(key, 0)
        prev = tp.get(key, 0)
        lines.append(f"| {label} | {fmt_int(curr)} | {fmt_int(prev)} | {delta(curr, prev) or '—'} |")
    lines.append("")

    lines.append("### Traffic by channel")
    lines.append("")
    lines.append(bar_chart(
        [(r.get("sessionDefaultChannelGroup", "(unknown)"), int(r.get("sessions", 0))) for r in ga4["channels"]]
    ))
    lines.append("")

    lines.append("### Top landing pages")
    lines.append("")
    lines.append(bar_chart(
        [(r.get("landingPagePlusQueryString", "(unknown)"), int(r.get("sessions", 0))) for r in ga4["top_pages"]],
        mono_label=True,
    ))
    lines.append("")

    # Bookings
    lines.append("## Bookings (Cliniko)")
    lines.append("")
    lines.append("### Booking outcomes this month")
    lines.append("")
    lines.append(stacked_bar([
        ("Held",         cli["appointments_held"],       "#007ae8"),
        ("Cancelled",    cli["appointments_cancelled"],  "#75dfee"),
        ("No-shows",     cli["appointments_no_show"],    "#ff5900"),
    ]))
    lines.append("")
    lines.append("| Metric | This month | Prev month | Change |")
    lines.append("|---|---:|---:|---:|")
    for label, key in [
        ("New patients", "new_patients"),
        ("Appointments held", "appointments_held"),
        ("Cancellations", "appointments_cancelled"),
        ("No-shows", "appointments_no_show"),
    ]:
        curr = cli.get(key, 0)
        prev = cli_prev.get(key, 0)
        lines.append(f"| {label} | {fmt_int(curr)} | {fmt_int(prev)} | {delta(curr, prev) or '—'} |")
    lines.append("")

    lines.append("### Appointments by location")
    lines.append("")
    lines.append(bar_chart(list(cli["by_business"].items())))
    lines.append("")

    lines.append("### Appointments by practitioner")
    lines.append("")
    lines.append(bar_chart(list(cli["by_practitioner"].items())))
    lines.append("")

    lines.append(f"*Generated {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by Locate Digital.*")
    lines.append("")
    return "\n".join(lines)


def main():
    env_path, year, month = parse_args()
    load_dotenv(env_path)
    client_name = env_path.parent.name

    # Cliniko
    cli = cliniko_client.ClinikoClient(
        api_key=os.environ["CLINIKO_API_KEY"],
        shard=os.environ["CLINIKO_SHARD"],
    )
    start, end = month_window(year, month)
    py, pm = prev_month(year, month)
    pstart, pend = month_window(py, pm)

    print(f"Generating {client_name} report for {year}-{month:02d}...")
    print("  Pulling Cliniko (current month)...")
    cli_summary = cliniko_summary(cli, start, end)
    print("  Pulling Cliniko (prev month)...")
    cli_prev_summary = cliniko_summary(cli, pstart, pend)

    # GA4
    ga4 = ga4_client.make_client(
        client_id=os.environ["GOOGLE_ADS_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
    )
    property_id = os.environ["GA4_PROPERTY_ID"]
    print("  Pulling GA4 (current month)...")
    ga4_curr = ga4_summary(ga4, property_id, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))
    print("  Pulling GA4 (prev month)...")
    ga4_prev = ga4_summary(ga4, property_id, pstart.strftime("%Y-%m-%d"), pend.strftime("%Y-%m-%d"))

    # Render + write
    md = render(client_name, year, month, ga4_curr, ga4_prev, cli_summary, cli_prev_summary)

    out_dir = env_path.parent / "reports" / f"{year}-{month:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_file = out_dir / "report.md"
    html_file = out_dir / "report.html"
    md_file.write_text(md, encoding="utf-8")
    period_label = datetime(year, month, 1).strftime("%B %Y")
    html_file.write_text(md_to_html(md, client_name, period_label), encoding="utf-8")
    print(f"\nReport saved:")
    print(f"  Markdown: {md_file}")
    print(f"  HTML:     {html_file}")


if __name__ == "__main__":
    main()
