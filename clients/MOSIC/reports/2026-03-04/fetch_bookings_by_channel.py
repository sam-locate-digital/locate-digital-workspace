"""
Pull `appointment_bookings` key event counts per month, split by
sessionDefaultChannelGroup. All digital channels — labelled.
Writes per-channel series into data.json under `bookings_by_channel_monthly`.
"""
from __future__ import annotations
import json
import os
import sys
from calendar import monthrange
from collections import defaultdict
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

EVENT = "appointment_bookings"

per_month = {}  # label -> {channel: count}
all_channels = set()
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
    month_counts = defaultdict(int)
    for row in resp.rows:
        ch = row.dimension_values[0].value or "(none)"
        ev = row.dimension_values[1].value
        n = int(float(row.metric_values[0].value or 0))
        if ev == EVENT and n > 0:
            month_counts[ch] += n
            all_channels.add(ch)
    per_month[LABEL[(y, m)]] = dict(month_counts)

# Print table
channels_ordered = sorted(all_channels)
print(f"\n{'MONTH':<8} " + " ".join(f"{c:>16}" for c in channels_ordered) + f"  {'TOTAL':>8}")
print("-" * (10 + 17 * len(channels_ordered) + 10))
for (y, m) in MONTHS:
    lbl = LABEL[(y, m)]
    row = per_month[lbl]
    vals = [row.get(c, 0) for c in channels_ordered]
    total = sum(vals)
    print(f"{lbl:<8} " + " ".join(f"{v:>16,}" for v in vals) + f"  {total:>8,}")

# Save
data_path = HERE / "data.json"
data = json.loads(data_path.read_text(encoding="utf-8"))
data["bookings_by_channel_monthly"] = {
    "months": [LABEL[m] for m in MONTHS],
    "channels": channels_ordered,
    "data": per_month,
    "event": EVENT,
    "methodology": (
        f"GA4 key event '{EVENT}' grouped by sessionDefaultChannelGroup. "
        "Each booking attributed to its acquisition channel."
    ),
}
data_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
print(f"\nUpdated {data_path}")
