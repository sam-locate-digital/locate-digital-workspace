# Locate Digital — Agency Workspace

Root folder for Locate Digital agency work. Global config lives at `C:\Users\Sam\.claude\CLAUDE.md` — defer to it for tone, git, and safety rules.

## Folder layout

- `_skills/` — the central home of every general Claude skill (see [Skills](#skills)). Nothing else goes here.
- `_templates/` — reusable templates: ad copy, landing pages, briefs, proposals
- `_brand/` — Locate Digital's own brand assets, pricing, decks
- `_ops/` — internal SOPs, contracts, invoicing, agency admin. Also `_ops/tools/` (non-skill toolkits such as the `monthly-report` Python pipeline), `_ops/skill-tests/` (skill eval runs) and `_ops/skill-packages/` (`.skill` files for uploading to the Claude app).
- `clients/<client-name>/` — one subfolder per client. Each has its own `CLAUDE.md` for client-specific context (industry, voice, channels, CRM).

## Conventions

- Underscore-prefixed folders are agency-wide; everything client-specific lives under `clients/`.
- Per-client subfolders (`meta-ads/`, `google-ads/`, `landing-pages/`, `reports/`, `assets/`) are a template — only create the ones a client actually uses.
- New client → create `clients/<name>/CLAUDE.md` first so future sessions have context.

## Skills

Every skill is a slash command. There are exactly two homes:

- **Central: `_skills/`** in this workspace (Google Drive, tracked in git). `C:\Users\samue\.claude\skills` is a Windows junction pointing here, so Claude Code loads these as user-level skills, available as `/skill-name` from any project. Edit skills in `_skills/`; never replace the junction with a real folder. `_skills/synced/` is managed by the Claude app and is git-ignored. Every skill that isn't tied to one client lives here:
  - Session memory: startup, wrapup (load and save session records in Supabase; keys in the workspace `.env`).
  - Locate delivery: client-onboarding, service-delivery, tracking-setup, landing-page, google-ads-copy, meta-ad-copy, social-post, email-campaign, seo-audit, monthly-report-narrative, competitor-research, market-research, meeting-prep, client-report-call, discovery-call, check-in-call, humanizer.
  - Demo websites: design-to-site (Claude Design handoff → static demo in `_brand/Website/demos/<industry>/`, checked and published), publish-demo (commit + push the demos subtree → demo.locatedigital.io). The prompt to paste into Claude Design is `_brand/Website/claude-design-handoff-prompt.md`.
  - Locate brand: locate-content (weekly @locatingsam Instagram plan, hands reels to reels-script), reels-script, edit-reel (raw footage in `_brand/Content/Raw Footage/` → finished reel in `Exports/`, plus CapCut packs and change requests; drives `_brand/Content/remotion-kit/`), locate-voice (Facebook and the caption voice rules), human-web-design. Everything they read and write (weekly plans, profile, insights log, research, scripts, footage, exports) lives in `_brand/Content/`.
  - Ads audit suite: ads and ads-* (google, meta, linkedin, tiktok, youtube, microsoft, apple, amazon, audit, plan, budget, creative, landing, attribution, server-side-tracking and more).
  - Design: frontend-design, banner-design, brand, design-system, slides, ui-styling, ui-ux-pro-max.
  - SEO, CRO and research: aeo, schema-markup, keyword-research, serp-analyzer, search-console, semrush-research, ahrefs-research, the geo-* skills, the *-cro skills and others.
- **Client folders: `clients/<client>/.claude/skills/`** — skills that only make sense for one client. They're directory-scoped commands, listed with the client's prefix when working in this workspace:
  - RAM: ram-precinct-post
  - MOSIC: mosic-blog-post, mosic-gmb-post, mosic-carousel
  - MaxiFinancial: loan-doc-review

Rules for new and edited skills:
- General skill → `_skills/<name>/SKILL.md` (same folder as `~/.claude/skills/<name>/` through the junction). Client-specific → `clients/<client>/.claude/skills/<name>/SKILL.md`.
- New skills can take a minute to appear in an already-open session, because Google Drive is slow to signal file changes. A new session always loads them.
- On a new computer, recreate the link once: `cmd /c mklink /J "%USERPROFILE%\.claude\skills" "G:\My Drive\Claude Code.Locate\_skills"`. Keep `_skills` set to "Available offline" in Google Drive.
- The file must be named exactly `SKILL.md` with `name` and `description` frontmatter. Not `SKILL (1).md`, not a loose `SKILL.md` in a parent folder — those never load as commands.
- Never keep skill copies in `.agents/`, this workspace's `.claude/skills/` or anywhere else. One copy per skill, in its home. Test runs go in `_ops/skill-tests/`, `.skill` packages in `_ops/skill-packages/`.
- Inside a skill, point to its own files as `$HOME/.claude/skills/<name>/...` (use `$HOME`, not `~`, inside quotes), never a workspace-relative `.claude/skills/...` path.
- Third-party toolkits keep their own skills where the toolkit expects them (e.g. `G:\My Drive\claude-code-video-toolkit\.claude\skills`).
