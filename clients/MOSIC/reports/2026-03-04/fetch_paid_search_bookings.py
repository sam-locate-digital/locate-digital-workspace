"""
Pull `appointment_bookings` key event counts per month, filtered to
sessionDefaultChannelGroup = 'Paid Search'. Writes the per-month series
into data.json under `paid_search_bookings_monthly`.
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

from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest,
)

ga4 = ga4_client.make_client(
    client_id=os.environ["GOOGLE_ADS_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_ADS_CLIENT_SECRET"],
    refresh_token=os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
)
prop = f"properties/{os.environ['GA4_PROPERTY_ID']}"


def month_window(y, m):
    last = monthrange(y, m)[1]
    return (datetime(y, m, 1, tzinfo=timezone.utc),
            datetime(y, m, last, 23, 59, 59, tzinfo=timezone.utc))


def ymd(d): return d.strftime("%Y-%m-%d")


MONTHS = [(2025, m) for m in range(5, 13)] + [(2026, m) for m in range(1, 5)]
LABEL = {(y, m): f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} {str(y)[2:]}" for y, m in MONTHS}

print(f"{'MONTH':<8} {'PAID SEARCH':>12}")
print("-" * 24)
series = []
for (y, m) in MONTHS:
    s, e = month_window(y, m)
    req = RunReportRequest(
        property=prop,
        dimensions=[
            Dimension(name="sessionDefaultChannelGroup"),
            Dimension(name="eventName"),
        ],
        metrics=[Metric(name="keyEvents")],
        date_ranges=[DateRange(start_date=ymd(s), end_date=ymd(e))],
    )
    resp = ga4.run_report(req)
    count = 0
    for row in resp.rows:
        ch = row.dimension_values[0].value or ""
        ev = row.dimension_values[1].value
        n = int(float(row.metric_values[0].value or 0))
        if ch == "Paid Search" and ev == "appointment_bookings":
            count += n
    series.append((LABEL[(y, m)], count))
    print(f"{LABEL[(y, m)]:<8} {count:>12,}")

# Save to data.json
data_path = HERE / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
data["paid_search_bookings_monthly"] = series
data["paid_search_event"] = "appointment_bookings"
data["paid_search_methodology"] = (
    "GA4 key event 'appointment_bookings' filtered to "
    "sessionDefaultChannelGroup='Paid Search'. Counts each event "
    "attributed to a paid Google Ads session."
)
data_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
print(f"\nUpdated {data_path}")
