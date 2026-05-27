"""Smoke test for GA4 connection via OAuth refresh token."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2.credentials import Credentials

if len(sys.argv) < 2:
    print("Usage: python test_ga4.py <path-to-client-env>")
    sys.exit(1)

env_path = Path(sys.argv[1])
load_dotenv(env_path)

property_id = os.getenv("GA4_PROPERTY_ID")
client_id = os.getenv("GOOGLE_ADS_CLIENT_ID")
client_secret = os.getenv("GOOGLE_ADS_CLIENT_SECRET")
refresh_token = os.getenv("GOOGLE_ADS_REFRESH_TOKEN")

print(f"Property ID: {property_id}")

missing = [n for n, v in {
    "GA4_PROPERTY_ID": property_id,
    "GOOGLE_ADS_CLIENT_ID": client_id,
    "GOOGLE_ADS_CLIENT_SECRET": client_secret,
    "GOOGLE_ADS_REFRESH_TOKEN": refresh_token,
}.items() if not v]
if missing:
    print(f"ERROR: missing in .env: {', '.join(missing)}")
    sys.exit(1)

credentials = Credentials(
    token=None,
    refresh_token=refresh_token,
    client_id=client_id,
    client_secret=client_secret,
    token_uri="https://oauth2.googleapis.com/token",
    scopes=["https://www.googleapis.com/auth/analytics.readonly"],
)

client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[Dimension(name="date")],
    metrics=[Metric(name="sessions"), Metric(name="totalUsers")],
    date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
)

try:
    response = client.run_report(request)
    print("\n--- LAST 7 DAYS ---")
    print(f"{'Date':<12} {'Sessions':>10} {'Users':>10}")
    for row in response.rows:
        date = row.dimension_values[0].value
        sessions = row.metric_values[0].value
        users = row.metric_values[1].value
        print(f"{date:<12} {sessions:>10} {users:>10}")
    print("\nSUCCESS — OAuth credentials can read GA4 data.")
except Exception as e:
    print(f"\nFAILED: {type(e).__name__}: {e}")
    sys.exit(1)
