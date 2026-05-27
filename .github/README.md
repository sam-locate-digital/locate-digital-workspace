# Locate Digital — agency workspace

Private repo. Internal use only.

Locate Digital is a digital marketing agency for service businesses — accountants, physios, dentists, osteos, salons, lawyers — typically $1–3M revenue.

---

## Folder structure

```
.
├── _skills/          # Reusable Claude skills (prompts + scripts)
├── _templates/       # Report and ad copy templates
├── _brand/           # Logos, brand.json, posting calendars
├── _ops/             # SOPs, contracts, access guides, Supabase schema
└── clients/          # One subfolder per client
    ├── MOSIC/
    ├── BrightenHomeLoans/
    └── GlossHairStudio/
```

Underscore-prefixed folders are agency-wide. Everything client-specific lives under `clients/`.

---

## Skills

Skills are Claude Code prompts stored as `SKILL.md` files. Load one into a session and Claude follows the instructions inside it.

| Skill | What it does |
|---|---|
| `humanizer` | Strips AI writing patterns — em dashes, filler phrases, rule of three, AI vocab |
| `social-post` | Writes Instagram/Facebook posts for service business clients |
| `reels-script` | Short-form video scripts with hook, body, CTA |
| `seo-audit` | Page-level SEO audit with action items |
| `landing-page` | Landing page copy briefs and drafts |
| `meta-ad-copy` | Meta Ads copy (primary text, headlines, descriptions) |
| `google-ads-copy` | Google Ads RSAs and ad copy |
| `monthly-report` | Pulls GA4 + Cliniko + Google Ads data → Markdown/HTML report |
| `monthly-report-narrative` | Writes the narrative summary for a monthly report |
| `client-onboarding` | Onboarding checklist and CLAUDE.md scaffold for new clients |
| `competitor-research` | Competitor analysis across organic, paid, and social channels |
| `email-campaign` | Email campaign copy (welcome, reactivation, nurture sequences) |
| `mosic-blog-post` | Blog post writer for MOSIC (osteopathy clinic, Melbourne) |
| `mosic-gmb-post` | Google Business Profile post writer for MOSIC |

The `_skills/SKILL.md` file covers how to create and iterate on new skills.

---

## Monthly report

The `_skills/monthly-report/` folder has a working Python pipeline:

```bash
python generate.py "clients/MOSIC/.env"          # previous full month
python generate.py "clients/MOSIC/.env" 2026-04  # specific month
```

Outputs `report.md` + `report.html` into `clients/<client>/reports/YYYY-MM/`. Open the HTML in a browser and print to PDF for the client.

Data sources: GA4, Cliniko, Google Ads (pending dev token).

---

## Client folders

Each client has:

```
clients/<name>/
├── CLAUDE.md          # Client context: industry, channels, voice, tooling, compliance
├── .env               # API keys — gitignored
├── reports/           # Monthly reports by period (YYYY-MM)
├── content/           # Blog posts, GMB posts, social copy
├── google-ads/        # RSA docs, scripts
├── meta-ads/          # Ad copy docs, creative briefs
└── assets/            # Research, audits, exported data
```

New client → create `CLAUDE.md` first so future sessions have full context.

---

## Conventions

- `clients/<name>/.env` holds all API keys — never committed
- Report outputs go in `reports/YYYY-MM/`
- Sentence case headings everywhere (AU English throughout)
- Commit message format: `<scope>: <what changed>` — e.g. `mosic: add May 2026 report`

---

## Stack

Instagram · TikTok · Meta Ads · Facebook · Google Ads · GA4 · GTM · Cliniko · Cliniqapps
