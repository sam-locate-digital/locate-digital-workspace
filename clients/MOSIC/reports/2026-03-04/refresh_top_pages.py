"""
One-off: pull top-20 most-viewed pages, AUS-only, for Mar + Apr 2026.
Updates data.json in place.
"""
from __future__ import annotations
import json
import os
import sys
from calendar import monthrange
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
SKILL_DIR = AGENCY_ROOT / "_skills" / "monthly-report"
sys.path.insert(0, str(SKILL_DIR))

import ga4_client
load_dotenv(AGENCY_ROOT / "clients" / "MOSIC" / ".env")


def month_window(y, m):
    last = monthrange(y, m)[1]
    return (datetime(y, m, 1, tzinfo=timezone.utc),
            datetime(y, m, last, 23, 59, 59, tzinfo=timezone.utc))


def ymd(d): return d.strftime("%Y-%m-%d")


ga4 = ga4_client.make_client(
    client_id=os.environ["GOOGLE_ADS_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_ADS_CLIENT_SECRET"],
    refresh_token=os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
)
property_id = os.environ["GA4_PROPERTY_ID"]

s, _ = month_window(2026, 3)
_, e = month_window(2026, 4)

# Query with country dim, then filter Australia, then take top 20.
# Need a generous limit to ensure we get >20 AUS rows after filtering.
resp = ga4_client.run(
    ga4, property_id, ymd(s), ymd(e),
    dimensions=["pagePath", "country"],
    metrics=["screenPageViews", "totalUsers"],
    order_by="screenPageViews",
    limit=500,
)
rows = ga4_client.to_rows(resp)

aus = [r for r in rows if r.get("country") == "Australia"]

# Some pages will appear once per (path,country) — since we already filter to AUS,
# one row per path. Sort by views desc, take top 20.
aus.sort(key=lambda r: int(r.get("screenPageViews", 0)), reverse=True)
top20 = aus[:20]

print(f"Total AUS rows: {len(aus)}  |  Returning top 20:")
for r in top20:
    print(f"  {r['screenPageViews']:>6}  {r['totalUsers']:>5}  {r['pagePath']}")

# Update data.json
data_path = HERE / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
data["top_pages"] = [
    [r["pagePath"], int(r["screenPageViews"]), int(r["totalUsers"])]
    for r in top20
]
data["top_pages_country_filter"] = "Australia"
data["cliniko_booking_page_entries"] = {
    "value": 742,
    "period": "Mar + Apr 2026",
    "source": "GA4 Key Events (AUS only)",
    "note": "Manually confirmed by Sam 2026-05-17. Wire up to GA4 Key Event name when known.",
}
data_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
print(f"\nUpdated {data_path}")
