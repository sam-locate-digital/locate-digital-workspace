# Locate Digital — Agency Workspace

Root folder for Locate Digital agency work. Global config lives at `C:\Users\Sam\.claude\CLAUDE.md` — defer to it for tone, git, and safety rules.

## Folder layout

- `_skills/` — client content archives and non-skill toolkits only (e.g. `monthly-report/` Python pipeline, MOSIC post archives, skill test workspaces). No skills live here — see [Skills](#skills) below.
- `_templates/` — reusable templates: ad copy, landing pages, briefs, proposals
- `_brand/` — Locate Digital's own brand assets, pricing, decks
- `_ops/` — internal SOPs, contracts, invoicing, agency admin
- `clients/<client-name>/` — one subfolder per client. Each has its own `CLAUDE.md` for client-specific context (industry, voice, channels, CRM).

## Conventions

- Underscore-prefixed folders are agency-wide; everything client-specific lives under `clients/`.
- Per-client subfolders (`meta-ads/`, `google-ads/`, `landing-pages/`, `reports/`, `assets/`) are a template — only create the ones a client actually uses.
- New client → create `clients/<name>/CLAUDE.md` first so future sessions have context.

## Skills

Every skill is a slash command. There are exactly two homes:

- **Central: `~/.claude/skills/`** (user-level) — every skill that isn't tied to one client, available as `/skill-name` from any project:
  - Locate delivery: client-onboarding, service-delivery, tracking-setup, landing-page, google-ads-copy, meta-ad-copy, social-post, email-campaign, seo-audit, monthly-report-narrative, competitor-research, market-research, meeting-prep, humanizer.
  - Locate brand: locate-voice, reels-script, human-web-design.
  - Ads audit suite: ads and ads-* (google, meta, linkedin, tiktok, youtube, microsoft, apple, amazon, audit, plan, budget, creative, landing, attribution, server-side-tracking and more).
  - Design: frontend-design, banner-design, brand, design-system, slides, ui-styling, ui-ux-pro-max.
  - SEO, CRO and research: aeo, schema-markup, keyword-research, serp-analyzer, search-console, semrush-research, ahrefs-research, the geo-* skills, the *-cro skills and others.
- **Client folders: `clients/<client>/.claude/skills/`** — skills that only make sense for one client. They're directory-scoped commands, listed with the client's prefix when working in this workspace:
  - RAM: ram-precinct-post
  - MOSIC: mosic-blog-post, mosic-gmb-post
  - MaxiFinancial: loan-doc-review

Rules for new and edited skills:
- General skill → `~/.claude/skills/<name>/SKILL.md`. Client-specific → `clients/<client>/.claude/skills/<name>/SKILL.md`.
- The file must be named exactly `SKILL.md` with `name` and `description` frontmatter. Not `SKILL (1).md`, not a loose `SKILL.md` in a parent folder — those never load as commands.
- Never keep skill copies in `_skills/`, `.agents/` or this workspace's `.claude/skills/`. One copy per skill, in its home.
- Inside a skill, point to its own files as `$HOME/.claude/skills/<name>/...` (use `$HOME`, not `~`, inside quotes), never a workspace-relative `.claude/skills/...` path.
- Third-party toolkits keep their own skills where the toolkit expects them (e.g. `G:\My Drive\claude-code-video-toolkit\.claude\skills`).
