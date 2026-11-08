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
- Straight-talking clinician: short sentences, "you", root cause over symptoms, hedged outcomes, specific Melbourne references, soft CTAs. AHPRA advertising rules apply (no testimonials, no guaranteed outcomes).
- Full guide: `.claude/skills/mosic-carousel/references/brand-voice.md`

## Social
- Instagram @melbosteo. Carousels and single-image posts via the `mosic-carousel` skill (Higgsfield-rendered, text-led with anatomy highlights). Each post is saved in its own dated folder: `Social Media Post/YYYY-MM-DD-<slug>/`.
- Weekly post runs as a Cowork scheduled task in "scheduled mode": topics come from `content/social-topics.md` (Sam adds them), output is a draft for Sam to review. Nothing is published automatically.

## Landing pages
- Reference template: `mosic-template.html` in the `landing-page` skill's folder (`~/.claude/skills/landing-page/`)
- Built for WPBakery — paste Custom HTML block into WordPress
- CTA band uses `div.as-cta-band` directly (no row wrapper) for edge-to-edge width
- Colors: navy `#1c2674`, purple `#8b68b3`, fonts: Ubuntu (headings) + Roboto (body)

## Notes
- API keys live in `clients/MOSIC/.env` (gitignored at root)
