# Locate Digital — Agency Workspace

Root folder for Locate Digital agency work. Global config lives at `C:\Users\Sam\.claude\CLAUDE.md` — defer to it for tone, git, and safety rules.

## Folder layout

- `_skills/` — Claude skills reusable across clients (audits, ad-copy generators, report builders, etc.)
- `_templates/` — reusable templates: ad copy, landing pages, briefs, proposals
- `_brand/` — Locate Digital's own brand assets, pricing, decks
- `_ops/` — internal SOPs, contracts, invoicing, agency admin
- `clients/<client-name>/` — one subfolder per client. Each has its own `CLAUDE.md` for client-specific context (industry, voice, channels, CRM).

## Conventions

- Underscore-prefixed folders are agency-wide; everything client-specific lives under `clients/`.
- Per-client subfolders (`meta-ads/`, `google-ads/`, `landing-pages/`, `reports/`, `assets/`) are a template — only create the ones a client actually uses.
- New client → create `clients/<name>/CLAUDE.md` first so future sessions have context.
