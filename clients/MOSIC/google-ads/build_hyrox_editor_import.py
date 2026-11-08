"""Build Google Ads Editor import CSVs for the MOSIC Hyrox Injury Search campaign.

Usage: python build_hyrox_editor_import.py [final_url]

Writes editor-import/01-campaign.csv ... 05-ads.csv next to this script.
Source of truth for copy and keywords: hyrox-injury-campaign-2026-10.md.
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "editor-import"
CAMPAIGN = "MOSIC Hyrox Injury Search 2026"
FINAL_URL = sys.argv[1] if len(sys.argv) > 1 else "https://melbourneosteopathycentre.com.au/hyrox-injury/"

AD_GROUPS = {
    "Hyrox Injury Treatment": {
        "path2": "treatment",
        "phrase": ["hyrox physio", "hyrox physiotherapist", "hyrox osteo", "hyrox osteopath",
                   "hyrox injury", "hyrox injuries", "hyrox training injury",
                   "hyrox training injuries", "hyrox melbourne injury"],
        "exact": ["hyrox injury", "hyrox physio"],
        "headlines": ["Hyrox Injury Treatment", "Hyrox Osteo Melbourne",
                      "Hyrox Injury Melbourne", "Injured Training for Hyrox?"],
        "description": "Osteo care for Hyrox running and stations, with a plan built around race day.",
    },
    "Hyrox Knee and Back": {
        "path2": "knee-back",
        "phrase": ["hyrox knee pain", "hyrox knee injury", "hyrox and knee pain",
                   "hyrox training knee pain", "hyrox lunges knee pain", "hyrox with knee injury",
                   "hyrox bad knees", "hyrox back pain", "hyrox lower back pain",
                   "hyrox back injury", "hyrox with back pain"],
        "exact": ["hyrox knee pain"],
        "headlines": ["Hyrox Knee Pain Treatment", "Hyrox Back Pain Treatment",
                      "Knee Pain From Lunges?", "Sled Push Back Pain?"],
        "description": "Knee pain from lunges or back pain from sleds? Get assessed before race day.",
    },
    "Hyrox Lower Leg": {
        "path2": "lower-leg",
        "phrase": ["hyrox achilles", "hyrox achilles tendonitis", "hyrox shin splints",
                   "shin splints before hyrox", "calf strain hyrox", "hyrox plantar fasciitis"],
        "exact": [],
        "headlines": ["Hyrox Achilles and Calf Pain", "Shin Splints Before Hyrox?",
                      "Running Injury Treatment", "Plantar Fascia Pain Help"],
        "description": "Achilles, calf, shin or foot pain from rising run volume? Get it assessed early.",
    },
    "Hyrox Pre and Post Race": {
        "path2": "race-prep",
        "phrase": ["injured before hyrox", "injury before hyrox", "hyrox prehab",
                   "hyrox injury prevention", "sore after hyrox", "lower back pain after hyrox"],
        "exact": [],
        "headlines": ["Injured Before Hyrox?", "Hyrox Prehab Melbourne",
                      "Sore After Hyrox?", "Weeks Out From Race Day?"],
        "description": "Prehab with our exercise physiologist, or treatment if you're carrying a niggle.",
    },
}

# Headline 2 is pinned to position 2; the rest float.
LOCATION_HEADLINE = "Melbourne CBD and Essendon"
SHARED_HEADLINES = ["Hyrox Injury Assessment", "Book Your Hyrox Assessment", "Sports Injury Osteopaths",
                    "Exercise Physiologist On Staff", "Melbourne Race Week 9-13 Dec",
                    "Plan Built Around Race Day", "Modified Training Plans",
                    "Running and Station Injuries", "Call (03) 9663 6202", "Book Online Today"]
# Description 1 is pinned to position 1.
SHARED_DESCRIPTIONS = [
    "Book a Hyrox injury assessment online, or call our CBD clinic on (03) 9663 6202.",
    "8 osteopaths and an exercise physiologist across Melbourne CBD and Essendon.",
    "Race week is 9-13 December. Get assessed now and keep more training options.",
]
EXTRA_NEGATIVES = ["massage", "free", "jobs", "course", "certification"]


def load_negatives():
    """Phrase negatives from the research file; the non-English block is exact."""
    phrase, exact, section = [], [], ""
    lines = (HERE / "hyrox-injury-negatives-2026-10.txt").read_text(encoding="utf-8").splitlines()[2:]
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            section = line
            continue
        (exact if "Non-English" in section else phrase).append(line)
    return phrase + EXTRA_NEGATIVES, exact


def write(name, header, rows):
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def main():
    OUT.mkdir(exist_ok=True)
    problems = []

    write("01-campaign.csv",
          ["Campaign", "Campaign Type", "Networks", "Budget", "Budget type", "Bid Strategy Type",
           "Campaign Status", "End Date", "Language"],
          [[CAMPAIGN, "Search", "Google search", "30.00", "Daily", "Maximize clicks",
            "Paused", "2026-12-31", "en"]])

    write("02-ad-groups.csv", ["Campaign", "Ad Group", "Max CPC", "Ad Group Status"],
          [[CAMPAIGN, ag, "6.00", "Enabled"] for ag in AD_GROUPS])

    kw_rows = []
    for ag, d in AD_GROUPS.items():
        kw_rows += [[CAMPAIGN, ag, k, "Phrase", "Enabled"] for k in d["phrase"]]
        kw_rows += [[CAMPAIGN, ag, k, "Exact", "Enabled"] for k in d["exact"]]
    write("03-keywords.csv", ["Campaign", "Ad Group", "Keyword", "Criterion Type", "Status"], kw_rows)

    phrase_neg, exact_neg = load_negatives()
    write("04-negative-keywords.csv", ["Campaign", "Ad Group", "Keyword", "Criterion Type"],
          [[CAMPAIGN, "", k, "Negative Phrase"] for k in phrase_neg]
          + [[CAMPAIGN, "", k, "Negative Exact"] for k in exact_neg])

    header = ["Campaign", "Ad Group", "Ad type", "Status", "Final URL", "Path 1", "Path 2"]
    header += [f"Headline {i}" for i in range(1, 16)] + ["Headline 1 position", "Headline 2 position"]
    header += [f"Description {i}" for i in range(1, 5)] + ["Description 1 position"]
    ad_rows = []
    for ag, d in AD_GROUPS.items():
        own = d["headlines"]
        headlines = [own[0], LOCATION_HEADLINE] + own[1:] + SHARED_HEADLINES
        descriptions = SHARED_DESCRIPTIONS + [d["description"]]
        if len(headlines) != 15 or len(set(headlines)) != 15:
            problems.append(f"{ag}: need 15 unique headlines, got {len(set(headlines))}")
        problems += [f"{ag}: headline over 30 ({len(h)}): {h}" for h in headlines if len(h) > 30]
        problems += [f"{ag}: description over 90 ({len(x)}): {x}" for x in descriptions if len(x) > 90]
        problems += [f"{ag}: path over 15: {p}" for p in ("hyrox-injury", d["path2"]) if len(p) > 15]
        ad_rows.append([CAMPAIGN, ag, "Responsive search ad", "Enabled", FINAL_URL,
                        "hyrox-injury", d["path2"], *headlines, "1", "2", *descriptions, "1"])
    write("05-ads.csv", header, ad_rows)

    if problems:
        print("\nPROBLEMS:\n" + "\n".join(problems))
        sys.exit(1)
    print(f"\nAll checks passed. Final URL: {FINAL_URL}")


if __name__ == "__main__":
    main()
