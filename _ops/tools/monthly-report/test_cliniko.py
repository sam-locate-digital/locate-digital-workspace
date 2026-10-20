"""Smoke test for Cliniko API connection."""
import os
import sys
from pathlib import Path
from base64 import b64encode
from datetime import datetime, timedelta
import urllib.request
import urllib.parse
import json
from dotenv import load_dotenv

if len(sys.argv) < 2:
    print("Usage: python test_cliniko.py <path-to-client-env>")
    sys.exit(1)

env_path = Path(sys.argv[1])
load_dotenv(env_path)

api_key = os.getenv("CLINIKO_API_KEY")
shard = os.getenv("CLINIKO_SHARD")

if not api_key or not shard:
    print("ERROR: CLINIKO_API_KEY or CLINIKO_SHARD missing in .env")
    sys.exit(1)

base_url = f"https://api.{shard}.cliniko.com/v1"
auth = b64encode(f"{api_key}:".encode()).decode()
headers = {
    "Authorization": f"Basic {auth}",
    "Accept": "application/json",
    "User-Agent": "Locate Digital Reports (sam@locatedigital.io)",
}


def get(path, params=None):
    url = f"{base_url}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


try:
    biz = get("/businesses", {"per_page": 5})
    print("--- BUSINESSES ---")
    for b in biz.get("businesses", []):
        print(f"  - {b.get('business_name')} ({b.get('country')}, {b.get('time_zone')})")

    pracs = get("/practitioners", {"per_page": 5})
    print("\n--- PRACTITIONERS ---")
    for p in pracs.get("practitioners", []):
        print(f"  - {p.get('first_name')} {p.get('last_name')} ({p.get('designation') or 'no title'})")

    fmt = "%Y-%m-%dT%H:%M:%SZ"
    now = datetime.utcnow().replace(microsecond=0)
    week_ago = now - timedelta(days=7)
    appts = get("/appointments", {
        "q[]": [f"starts_at:>{week_ago.strftime(fmt)}", f"starts_at:<{now.strftime(fmt)}"],
        "per_page": 1,
    })
    total = appts.get("total_entries", "?")
    print("\n--- APPOINTMENTS (last 7 days) ---")
    print(f"  Total: {total}")

    patients = get("/patients", {"per_page": 1})
    print("\n--- PATIENTS ---")
    print(f"  Total in system: {patients.get('total_entries', '?')}")

    print("\nSUCCESS - Cliniko API key works.")
except urllib.error.HTTPError as e:
    body = e.read().decode(errors="replace")
    print(f"\nFAILED: HTTP {e.code} {e.reason}")
    print(body[:500])
    sys.exit(1)
except Exception as e:
    print(f"\nFAILED: {type(e).__name__}: {e}")
    sys.exit(1)
