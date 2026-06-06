# MOSIC — Client Context

Onboarded: 2026-05-09

## Business
- Industry: Osteopathy
- Locations: Bourke St (Melbourne CBD), Essendon, plus Telehealth
- 8 practitioners on staff (osteopaths; one also Exercise Physiologist)
- ~12k patient base, ~870 appointments/month, ~48 new patients/month (April 2026 baseline)
- Key contact: TBD

## Channels active
- **Google Ads** — direct
- **SEO** — direct
- **Email** — handled via Cliniko + Cliniqapps (practice management + patient comms)

## Tooling & data sources
- **Cliniko** (practice management) — API key required for appointment/patient/revenue data
- **Cliniqapps** — API key required for email send/open/click/conversion data
- **Google Ads** — API access required for spend, clicks, conversions
- (Optional) **GA4** — for SEO traffic + on-site behaviour

## Reporting
- Monthly client report: pulls Google Ads + SEO traffic + Cliniko booking outcomes + Cliniqapps email metrics → consolidated PDF/doc
- Output lives in `reports/YYYY-MM/`

## Voice & tone
- TBD (osteopathy clinic — likely warm, professional, patient-trust focused)

## Landing pages
- Reference template: `_skills/landing-page/mosic-template.html`
- Built for WPBakery — paste Custom HTML block into WordPress
- CTA band uses `div.as-cta-band` directly (no row wrapper) for edge-to-edge width
- Colors: navy `#1c2674`, purple `#8b68b3`, fonts: Ubuntu (headings) + Roboto (body)

## Notes
- API keys live in `clients/MOSIC/.env` (gitignored at root)
