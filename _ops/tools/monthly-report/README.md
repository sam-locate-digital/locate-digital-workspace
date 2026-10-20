# Monthly Report Skill

Generates a Markdown monthly report for a Locate Digital client by combining:

- **GA4** — sessions, users, traffic channels, top landing pages
- **Cliniko** — new patients, appointments held / cancelled / no-show, breakdown by location and practitioner
- **Google Ads** — *(not yet wired in — pending dev token)*

## Usage

```bash
# Generate for the previous full calendar month (default)
python generate.py "G:/My Drive/Claude Code.Locate/clients/MOSIC/.env"

# Generate for a specific month
python generate.py "G:/My Drive/Claude Code.Locate/clients/MOSIC/.env" 2026-04
```

Output: `clients/<client>/reports/YYYY-MM/report.md` and `report.html` (with embedded styles, print-friendly — open in browser, Cmd/Ctrl+P → Save as PDF for a client-ready file).

## Required env vars

In the client's `.env`:

```
CLINIKO_API_KEY=
CLINIKO_SHARD=

GOOGLE_ADS_CLIENT_ID=
GOOGLE_ADS_CLIENT_SECRET=
GOOGLE_ADS_REFRESH_TOKEN=

GA4_PROPERTY_ID=
```

GA4 reuses the Google Ads OAuth client (same scopes flow).

## Files

- `generate.py` — main entry point
- `cliniko_client.py` — Cliniko API helpers
- `ga4_client.py` — GA4 Data API helpers
- `test_cliniko.py` — connection smoke test
- `test_ga4.py` — connection smoke test

## What's missing

- **Google Ads section** — add once dev token is approved. Reuses same OAuth refresh token.
- **PDF export** — currently outputs Markdown. Convert to PDF via Pandoc or a Google Docs upload step when ready.
- **Email metrics** — Cliniqapps has no public API. If client moves to Mailchimp/Klaviyo later, wire that in.
