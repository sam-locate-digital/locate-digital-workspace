"""
Pull March + April 2026 data from APIs for the MOSIC monthly report.

Writes to data.json next to this file. The PPTX builder reads from there.
For each metric we record either:
   { "value": ..., "source": "ga4|cliniko|google_ads" }
or { "value": null, "missing": "reason text" }
so the PPTX builder knows what to flag.
"""
from __future__ import annotations
import json
import os
import sys
import traceback
from calendar import monthrange
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
SKILL_DIR = AGENCY_ROOT / "_skills" / "monthly-report"
sys.path.insert(0, str(SKILL_DIR))

import cliniko_client
import ga4_client

CLIENT_ENV = AGENCY_ROOT / "clients" / "MOSIC" / ".env"
load_dotenv(CLIENT_ENV)


# ---------- date helpers ----------
def month_window(year, month):
    last_day = monthrange(year, month)[1]
    start = datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc)
    end   = datetime(year, month, last_day, 23, 59, 59, tzinfo=timezone.utc)
    return start, end

def ymd(d): return d.strftime("%Y-%m-%d")

# Months to backfill (chrono): we want a 12-month series ending Apr 2026.
MONTHS = [
    (2025, 5),  (2025, 6),  (2025, 7),  (2025, 8),
    (2025, 9),  (2025, 10), (2025, 11), (2025, 12),
    (2026, 1),  (2026, 2),  (2026, 3),  (2026, 4),
]
LABEL = {
    (2025, 5):  "May 25",  (2025, 6):  "Jun 25",  (2025, 7):  "Jul 25",  (2025, 8):  "Aug 25",
    (2025, 9):  "Sep 25",  (2025, 10): "Oct 25",  (2025, 11): "Nov 25",  (2025, 12): "Dec 25",
    (2026, 1):  "Jan 26",  (2026, 2):  "Feb 26",  (2026, 3):  "Mar 26",  (2026, 4):  "Apr 26",
}


out = {
    "period_label":  "March + April 2026",
    "period_short":  "Mar + Apr 2026",
    "highlight":     ["Mar 26", "Apr 26"],
    "months_chrono": [LABEL[m] for m in MONTHS],
    "errors":        [],
    "missing":       [],
}


# ---------- GA4 ----------
print("=== GA4 ===")
ga4 = None
try:
    ga4 = ga4_client.make_client(
        client_id=os.environ["GOOGLE_ADS_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_ADS_CLIENT_SECRET"],
        refresh_token=os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
    )
    property_id = os.environ["GA4_PROPERTY_ID"]
except Exception as e:
    msg = f"GA4 client init failed: {e}"
    print(msg); out["errors"].append(msg)


def ga4_metric_by_month(dim_filters_metric, metric_name, *, country=None):
    """Run one GA4 query per month — returns list of (label, value)."""
    series = []
    for (y, m) in MONTHS:
        s, e = month_window(y, m)
        try:
            req_kwargs = dict(
                client=ga4, property_id=property_id,
                start=ymd(s), end=ymd(e),
                dimensions=["country"] if country else [],
                metrics=[metric_name],
            )
            resp = ga4_client.run(**req_kwargs)
            rows = ga4_client.to_rows(resp)
            if country:
                v = sum(int(r.get(metric_name, 0)) for r in rows
                        if r.get("country") == country)
            else:
                v = int(rows[0].get(metric_name, 0)) if rows else 0
            series.append((LABEL[(y, m)], v))
        except Exception as e:
            print(f"  GA4 {metric_name} {y}-{m:02d} FAILED: {e}")
            out["errors"].append(f"GA4 {metric_name} {y}-{m:02d}: {e}")
            series.append((LABEL[(y, m)], None))
    return series


def ga4_organic_by_month():
    """Organic search sessions per month, filtered to Australia."""
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Metric, RunReportRequest,
    )
    series = []
    for (y, m) in MONTHS:
        s, e = month_window(y, m)
        try:
            req = RunReportRequest(
                property=f"properties/{property_id}",
                dimensions=[
                    Dimension(name="sessionDefaultChannelGroup"),
                    Dimension(name="country"),
                ],
                metrics=[Metric(name="sessions")],
                date_ranges=[DateRange(start_date=ymd(s), end_date=ymd(e))],
            )
            resp = ga4.run_report(req)
            rows = ga4_client.to_rows(resp)
            v = sum(int(r.get("sessions", 0)) for r in rows
                    if r.get("sessionDefaultChannelGroup") == "Organic Search"
                    and r.get("country") == "Australia")
            series.append((LABEL[(y, m)], v))
        except Exception as e:
            print(f"  GA4 organic {y}-{m:02d} FAILED: {e}")
            out["errors"].append(f"GA4 organic {y}-{m:02d}: {e}")
            series.append((LABEL[(y, m)], None))
    return series


def ga4_top_pages(start, end):
    try:
        resp = ga4_client.run(
            ga4, property_id, ymd(start), ymd(end),
            dimensions=["pagePath"],
            metrics=["screenPageViews", "totalUsers"],
            order_by="screenPageViews",
            limit=10,
        )
        rows = ga4_client.to_rows(resp)
        return [(r.get("pagePath", "?"),
                 int(r.get("screenPageViews", 0)),
                 int(r.get("totalUsers", 0))) for r in rows]
    except Exception as e:
        print(f"  GA4 top pages FAILED: {e}")
        out["errors"].append(f"GA4 top pages: {e}")
        return None


if ga4:
    print("Visitors (AUS) by month...")
    out["website_visitors_aus"] = ga4_metric_by_month(
        None, "totalUsers", country="Australia",
    )

    print("Organic search sessions by month...")
    out["organic_search"] = ga4_organic_by_month()

    print("Top pages — Mar + Apr 2026 combined...")
    s_mar, _ = month_window(2026, 3)
    _, e_apr = month_window(2026, 4)
    out["top_pages"] = ga4_top_pages(s_mar, e_apr)

    # YoY (Mar + Apr 2025) — for KPI comparison
    print("YoY visitors (Mar + Apr 2025)...")
    s25, _   = month_window(2025, 3)
    _, e25   = month_window(2025, 4)
    try:
        from google.analytics.data_v1beta.types import (
            DateRange, Dimension, Metric, RunReportRequest,
        )
        req = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name="country")],
            metrics=[Metric(name="totalUsers"), Metric(name="sessions")],
            date_ranges=[DateRange(start_date=ymd(s25), end_date=ymd(e25))],
        )
        resp = ga4.run_report(req)
        rows = ga4_client.to_rows(resp)
        out["yoy_visitors_aus"] = sum(int(r.get("totalUsers", 0)) for r in rows
                                       if r.get("country") == "Australia")
    except Exception as e:
        out["yoy_visitors_aus"] = None
        out["errors"].append(f"GA4 YoY visitors: {e}")
else:
    out["website_visitors_aus"] = None
    out["organic_search"] = None
    out["top_pages"] = None


# ---------- Cliniko ----------
print("\n=== Cliniko ===")
try:
    cli = cliniko_client.ClinikoClient(
        api_key=os.environ["CLINIKO_API_KEY"],
        shard=os.environ["CLINIKO_SHARD"],
    )
    businesses = {b["id"]: b["business_name"] for b in cli.businesses()}
    print(f"  Businesses: {list(businesses.values())}")
except Exception as e:
    cli = None
    msg = f"Cliniko init failed: {e}"
    print(msg); out["errors"].append(msg)


def _id(field):
    link = (field or {}).get("links", {}).get("self") or ""
    return link.rsplit("/", 1)[-1] if link else None


def cliniko_month(y, m):
    """Return dict of summary stats for a month."""
    s, e = month_window(y, m)
    appts = cli.appointments_in_range(s, e)
    cancellations = cli.cancellations_in_range(s, e)
    patients = cli.patients_created_in_range(s, e)

    no_show = sum(1 for a in appts if a.get("did_not_arrive"))
    held = len(appts) - no_show

    # Per-location
    by_business = Counter()
    for a in appts:
        bid = _id(a.get("business"))
        if bid in businesses:
            by_business[businesses[bid]] += 1

    # New patients per location: take their first appointment location
    new_patients_by_business = Counter()
    for p in patients:
        # patient first_appointment_at + business — try via appointments search
        # easier: first appointment of each new patient — pull from /patients/{id}/appointments?per_page=1&order=...
        # but that's expensive. Just count new-patient appointments per location instead
        pass
    # Approximation: appointments where the patient was *created* this month
    new_patient_ids = {p["id"] for p in patients}
    for a in appts:
        pid = _id(a.get("patient"))
        if pid and int(pid) in new_patient_ids:
            bid = _id(a.get("business"))
            if bid in businesses:
                new_patients_by_business[businesses[bid]] += 1

    return {
        "appointments_held":      held,
        "appointments_cancelled": len(cancellations),
        "no_show":                no_show,
        "new_patients":           len(patients),
        "by_business":            dict(by_business.most_common()),
        "new_patients_by_business": dict(new_patients_by_business.most_common()),
    }


if cli:
    cliniko_results = {}
    # Add Mar+Apr 2025 for YoY comparison
    yoy_months = [(2025, 3), (2025, 4)]
    for (y, m) in MONTHS + yoy_months:
        if (y, m) in yoy_months:
            label = f"{['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][m-1]} 25"
        else:
            label = LABEL[(y, m)]
        try:
            print(f"  Cliniko {y}-{m:02d}...")
            cliniko_results[label] = cliniko_month(y, m)
        except Exception as e:
            print(f"  Cliniko {y}-{m:02d} FAILED: {e}")
            out["errors"].append(f"Cliniko {y}-{m:02d}: {e}")
            cliniko_results[label] = None
    out["cliniko_by_month"] = cliniko_results
    # YoY comparison values (Mar+Apr 2025)
    out["yoy_confirmed_bookings"] = (
        (cliniko_results.get("Mar 25", {}) or {}).get("appointments_held", 0)
      + (cliniko_results.get("Apr 25", {}) or {}).get("appointments_held", 0)
    )
    out["yoy_new_patients"] = (
        (cliniko_results.get("Mar 25", {}) or {}).get("new_patients", 0)
      + (cliniko_results.get("Apr 25", {}) or {}).get("new_patients", 0)
    )

    # Build flat series
    out["confirmed_bookings"] = [
        (LABEL[(y, m)],
         cliniko_results[LABEL[(y, m)]]["appointments_held"]
         if cliniko_results[LABEL[(y, m)]] else None)
        for (y, m) in MONTHS
    ]
    out["total_new_patients"] = [
        (LABEL[(y, m)],
         cliniko_results[LABEL[(y, m)]]["new_patients"]
         if cliniko_results[LABEL[(y, m)]] else None)
        for (y, m) in MONTHS
    ]
    # Per-location new-patient series (approximation)
    bourke_key = next((b for b in businesses.values() if "bourke" in b.lower()), None)
    essendon_key = next((b for b in businesses.values() if "essendon" in b.lower()), None)
    out["bourke_label"] = bourke_key
    out["essendon_label"] = essendon_key

    def loc_series(loc_label):
        return [
            (LABEL[(y, m)],
             (cliniko_results[LABEL[(y, m)]]["by_business"].get(loc_label, 0)
              if cliniko_results[LABEL[(y, m)]] else None))
            for (y, m) in MONTHS
        ]
    # NOTE: switched from "new patients per location" to "all appointments per location"
    # — matching new patient IDs to appointments wasn't reliable via the API; total
    # appointments per location is a closer signal anyway.
    out["appointments_bourke"]   = loc_series(bourke_key)   if bourke_key   else None
    out["appointments_essendon"] = loc_series(essendon_key) if essendon_key else None
else:
    out["cliniko_by_month"] = None
    out["confirmed_bookings"] = None
    out["total_new_patients"] = None
    out["new_patients_bourke"] = None
    out["new_patients_essendon"] = None


# ---------- Google Ads (best-effort) ----------
print("\n=== Google Ads ===")
try:
    from google.ads.googleads.client import GoogleAdsClient  # type: ignore
    has_gads_lib = True
except ImportError:
    has_gads_lib = False
    print("  google-ads library not installed — skipping (will install)")
    out["missing"].append({
        "metric": "google_ads_phone_calls",
        "reason": "google-ads Python library not installed in this env",
    })

SKIP_GADS = True  # phone_calls metric is not selectable on customer-level reports;
                  # per-call view requires call-tracking enabled. Mark missing.
if has_gads_lib and not SKIP_GADS:
    try:
        cfg = {
            "developer_token":  os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
            "client_id":        os.environ["GOOGLE_ADS_CLIENT_ID"],
            "client_secret":    os.environ["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token":    os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            "use_proto_plus":   True,
        }
        gads_client = GoogleAdsClient.load_from_dict(cfg)
        customer_id = os.environ["GOOGLE_ADS_CUSTOMER_ID"].replace("-", "")
        ga_service = gads_client.get_service("GoogleAdsService")

        # Phone calls — count rows from customer_call_view in window
        phone_calls = []
        for (y, m) in MONTHS:
            s, e = month_window(y, m)
            query = f"""
                SELECT customer_call_view.resource_name
                FROM customer_call_view
                WHERE segments.date BETWEEN '{ymd(s)}' AND '{ymd(e)}'
            """
            try:
                resp = ga_service.search_stream(customer_id=customer_id, query=query)
                total = 0
                for batch in resp:
                    for _row in batch.results:
                        total += 1
                phone_calls.append((LABEL[(y, m)], total))
            except Exception as e:
                # Fallback: try campaign-level phone_calls metric
                try:
                    q2 = f"""
                        SELECT metrics.phone_calls
                        FROM campaign
                        WHERE segments.date BETWEEN '{ymd(s)}' AND '{ymd(e)}'
                    """
                    r2 = ga_service.search_stream(customer_id=customer_id, query=q2)
                    total = 0
                    for batch in r2:
                        for row in batch.results:
                            total += int(row.metrics.phone_calls)
                    phone_calls.append((LABEL[(y, m)], total))
                except Exception as e2:
                    phone_calls.append((LABEL[(y, m)], None))
                    out["errors"].append(
                        f"GoogleAds phone_calls {y}-{m:02d}: {e2}"
                    )
        out["google_ads_phone_calls"] = phone_calls
    except Exception as e:
        print(f"  Google Ads FAILED: {e}")
        traceback.print_exc()
        out["errors"].append(f"Google Ads: {e}")
        out["google_ads_phone_calls"] = None
        out["missing"].append({
            "metric": "google_ads_phone_calls",
            "reason": f"Google Ads call failed: {e}",
        })
else:
    out["google_ads_phone_calls"] = None
    if SKIP_GADS:
        out["missing"].append({
            "metric": "google_ads_phone_calls",
            "reason": "Google Ads phone_calls metric not queryable at customer level; "
                      "needs call_view (requires call tracking) or campaign-level segment.",
        })


# ---------- mark unavailable sources ----------
out["missing"].extend([
    {"metric": "entered_booking_page",
     "reason": "Source unknown — was likely Cliniko booking-page analytics from "
               "an embed/property different from main site GA4. Need confirmation."},
    {"metric": "new_patients_from_google",
     "reason": "Requires Google Ads conversion attribution mapped to Cliniko "
               "patient creation — no current automated source."},
    {"metric": "cliniqapps_automations",
     "reason": "Cliniqapps has no public API. Manual export from dashboard."},
    {"metric": "cliniqapps_broadcast",
     "reason": "Cliniqapps has no public API. Manual export from dashboard."},
    {"metric": "hotdoc_bookings",
     "reason": "HotDoc does not expose monthly booking totals via public API."},
    {"metric": "actioned_items",
     "reason": "Internal log — must be entered manually each period."},
    {"metric": "executive_summary",
     "reason": "Requires human judgement on what the period meant — "
               "draft generated from raw deltas; review before sending."},
])


# ---------- save ----------
out_path = HERE / "data.json"
out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
print(f"\nWrote {out_path}")
print(f"Errors: {len(out['errors'])}")
print(f"Missing markers: {len(out['missing'])}")
