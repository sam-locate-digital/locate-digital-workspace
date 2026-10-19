# Locate Digital — Agency Workspace

Root folder for Locate Digital agency work. Global config lives at `C:\Users\Sam\.claude\CLAUDE.md` — defer to it for tone, git, and safety rules.

## Folder layout

- `_skills/` — client content archives and non-skill toolkits (e.g. `monthly-report/` Python pipeline). Reusable Claude skills themselves live user-level in `~/.claude/skills/` so they're available as `/skill-name` from any project — see [Skills](#skills) below.
- `_templates/` — reusable templates: ad copy, landing pages, briefs, proposals
- `_brand/` — Locate Digital's own brand assets, pricing, decks
- `_ops/` — internal SOPs, contracts, invoicing, agency admin
- `clients/<client-name>/` — one subfolder per client. Each has its own `CLAUDE.md` for client-specific context (industry, voice, channels, CRM).

## Conventions

- Underscore-prefixed folders are agency-wide; everything client-specific lives under `clients/`.
- Per-client subfolders (`meta-ads/`, `google-ads/`, `landing-pages/`, `reports/`, `assets/`) are a template — only create the ones a client actually uses.
- New client → create `clients/<name>/CLAUDE.md` first so future sessions have context.

## Skills

Agency skills live in two places:
- `.claude/skills/` (this project) — the ads-* audit suite and design/creative skills.
- `~/.claude/skills/` (user-level) — agency delivery skills (client-onboarding, tracking-setup, landing-page, google-ads-copy, meta-ad-copy, social-post, reels-script, seo-audit, email-campaign, monthly-report-narrative, competitor-research, service-delivery, humanizer, ram-precinct-post, frontend-design, human-web-design). These are Locate-Digital-specific and expect to be run with this workspace as the working directory, but are discoverable as `/skill-name` from anywhere since they live user-level.
