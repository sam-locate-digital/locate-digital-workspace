"""
Probe GA4 to find candidate booking conversion events + see what Google Ads
attribution looks like per month.
"""
from __future__ import annotations
import os
import sys
from calendar import monthrange
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
SKILL_DIR = AGENCY_ROOT / "_skills" / "monthly-report"
sys.path.insert(0, str(SKILL_DIR))

import ga4_client
load_dotenv(AGENCY_ROOT / "clients" / "MOSIC" / ".env")

from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, OrderBy, RunReportRequest, Filter,
    FilterExpression, FilterExpressionList,
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


print("=" * 70)
print("1. ALL KEY EVENTS (Mar + Apr 2026) — sorted by count")
print("=" * 70)
s_mar, _ = month_window(2026, 3)
_, e_apr = month_window(2026, 4)

req = RunReportRequest(
    property=prop,
    dimensions=[Dimension(name="eventName")],
    metrics=[Metric(name="keyEvents"), Metric(name="eventCount")],
    date_ranges=[DateRange(start_date=ymd(s_mar), end_date=ymd(e_apr))],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="keyEvents"), desc=True)],
)
resp = ga4.run_report(req)
print(f"\n{'EVENT NAME':<50} {'KEY EVENTS':>12} {'EVENT COUNT':>12}")
print("-" * 76)
for row in resp.rows:
    name = row.dimension_values[0].value
    keys = int(float(row.metric_values[0].value or 0))
    cnt = int(float(row.metric_values[1].value or 0))
    if keys > 0 or "book" in name.lower() or "convert" in name.lower():
        print(f"{name:<50} {keys:>12,} {cnt:>12,}")

print("\n" + "=" * 70)
print("2. KEY EVENTS BY CHANNEL (Mar + Apr 2026)")
print("=" * 70)

req = RunReportRequest(
    property=prop,
    dimensions=[
        Dimension(name="sessionDefaultChannelGroup"),
        Dimension(name="eventName"),
    ],
    metrics=[Metric(name="keyEvents")],
    date_ranges=[DateRange(start_date=ymd(s_mar), end_date=ymd(e_apr))],
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="keyEvents"), desc=True)],
)
resp = ga4.run_report(req)
by_channel = defaultdict(lambda: defaultdict(int))
for row in resp.rows:
    ch = row.dimension_values[0].value or "(none)"
    ev = row.dimension_values[1].value
    keys = int(float(row.metric_values[0].value or 0))
    if keys > 0:
        by_channel[ch][ev] = keys

for ch in sorted(by_channel, key=lambda c: -sum(by_channel[c].values())):
    total = sum(by_channel[ch].values())
    print(f"\n  {ch}  — total {total:,} key events")
    for ev, n in sorted(by_channel[ch].items(), key=lambda x: -x[1])[:5]:
        print(f"    {n:>6,}  {ev}")

print("\n" + "=" * 70)
print("3. PAID SEARCH KEY EVENTS PER MONTH (last 12 months)")
print("=" * 70)
print("(filter: sessionDefaultChannelGroup = 'Paid Search')")
print()

MONTHS = [(2025, m) for m in range(5, 13)] + [(2026, m) for m in range(1, 5)]
LABELS = {(y, m): f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} {str(y)[2:]}" for y, m in MONTHS}

print(f"{'MONTH':<8} {'KEY EVENTS':>12}  TOP EVENT NAMES (key event counts)")
print("-" * 70)
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
    total = 0
    by_event = defaultdict(int)
    for row in resp.rows:
        ch = row.dimension_values[0].value or ""
        ev = row.dimension_values[1].value
        n = int(float(row.metric_values[0].value or 0))
        if ch == "Paid Search" and n > 0:
            total += n
            by_event[ev] += n
    top_ev = ", ".join(f"{v}×{k}" for k, v in sorted(by_event.items(), key=lambda x: -x[1])[:3])
    print(f"{LABELS[(y, m)]:<8} {total:>12,}  {top_ev}")
