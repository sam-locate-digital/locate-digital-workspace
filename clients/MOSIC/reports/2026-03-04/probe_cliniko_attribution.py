"""
Probe Cliniko for any field/tag that might indicate Google Ads attribution.
Look at recent patients + appointments to see what's there.
"""
from __future__ import annotations
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
AGENCY_ROOT = HERE.parents[3]
SKILL_DIR = AGENCY_ROOT / "_skills" / "monthly-report"
sys.path.insert(0, str(SKILL_DIR))

import cliniko_client
load_dotenv(AGENCY_ROOT / "clients" / "MOSIC" / ".env")

cli = cliniko_client.ClinikoClient(
    api_key=os.environ["CLINIKO_API_KEY"],
    shard=os.environ["CLINIKO_SHARD"],
)

# Pull a small sample of recent patients (created Mar+Apr 2026)
start = datetime(2026, 3, 1, tzinfo=timezone.utc)
end = datetime(2026, 4, 30, 23, 59, 59, tzinfo=timezone.utc)

print("=== Sampling 5 recent patients (Mar+Apr 2026) ===")
patients = cli.patients_created_in_range(start, end)
print(f"Total patients in window: {len(patients)}")

if patients:
    print("\n--- Field names on first patient ---")
    p0 = patients[0]
    for k in sorted(p0.keys()):
        v = p0[k]
        v_str = json.dumps(v)[:80] if v is not None else "None"
        print(f"  {k}: {v_str}")

# Hunt for source-related fields
print("\n=== Source/referral field distribution across all Mar+Apr patients ===")
source_fields = ['referral_source', 'referral_source_id', 'referral_source_other',
                 'referral_source_other_text', 'how_did_you_find_out', 'source',
                 'first_referral_source', 'first_appointment_referral_source']
for field in source_fields:
    vals = Counter()
    for p in patients:
        v = p.get(field)
        if isinstance(v, dict):
            v = v.get('name') or v.get('description') or str(v)[:40]
        vals[str(v) if v else "<empty>"] += 1
    if any(k != "<empty>" for k in vals):
        print(f"\n  '{field}':")
        for k, n in vals.most_common(10):
            print(f"    {n:4d}  {k}")

# Also check referral_sources endpoint
print("\n=== /referral_sources endpoint ===")
try:
    sources = cli.paginate("/referral_sources")
    print(f"Found {len(sources)} referral sources:")
    for s in sources:
        print(f"  id={s.get('id')}  name={s.get('name')!r}")
except Exception as e:
    print(f"  ERROR: {e}")

# Check patient tags
print("\n=== /patient_tags endpoint (top tags) ===")
try:
    tags_url = "/patient_tags"
    tags = cli.paginate(tags_url, key="patient_tags")
    print(f"Found {len(tags)} patient tags (first 30):")
    for t in tags[:30]:
        print(f"  id={t.get('id')}  name={t.get('name')!r}")
except Exception as e:
    print(f"  ERROR: {e}")
