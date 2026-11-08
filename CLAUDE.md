# Locate Digital — Agency Workspace

Root folder for Locate Digital agency work. This file is the main instruction set: there's no global `~/.claude/CLAUDE.md` on this computer. Brand voice lives in `_brand/brand-guidelines.html`, client voice in each client's `CLAUDE.md`.

## Folder layout

- `_skills/` — the central home of every general Claude skill (see [Skills](#skills)). Nothing else goes here.
- `_templates/` — reusable templates: ad copy, landing pages, briefs, proposals
- `_brand/` — Locate Digital's own brand assets, pricing, decks
- `_ops/` — internal SOPs, contracts, invoicing, agency admin. Also `_ops/tools/` (non-skill toolkits such as the `monthly-report` Python pipeline), `_ops/skill-tests/` (skill eval runs) and `_ops/skill-packages/` (`.skill` files for uploading to the Claude app).
- `_services/` — Locate's service lines and their sales material (e.g. `_services/ai-adoption/`, the AI training offer, with its own `CLAUDE.md`)
- `_guides/` — the industry marketing checklists site. `_guides/checklists/` is also its own repo (locate-digital-checklists); the build scripts use absolute paths, so don't move it.
- `clients/<client-name>/` — one subfolder per client. Each has its own `CLAUDE.md` for client-specific context (industry, voice, channels, CRM).
- `_inbox/` — drop spot for files with no home yet. Git-ignored. Sort it every so often; never leave loose files at the workspace root.
- `_to-delete/` — holding folder for anything being removed (see Conventions). Git-ignored. Sam empties it after a look.

## Conventions

- **Never delete outright.** Move anything being removed into `_to-delete/` and add a line to its `README.md` (what, where it was, why). Sam deletes it after checking.
- The workspace root holds only the folders above plus `CLAUDE.md`, `.env`, `.env.example` and `.gitignore`.
- Large media stays out of git: raw footage, reel and tutorial exports, reference clips, video, audio, raw image renders and `node_modules` are git-ignored (see `.gitignore`). Google Drive keeps them. Commit text, code, documents and the finished images used in deliverables.
- Client personal data (borrower documents, IDs, payslips, patient details) never goes in git, and ideally not in this workspace at all.
- Underscore-prefixed folders are agency-wide; everything client-specific lives under `clients/`.
- Per-client subfolders (`meta-ads/`, `google-ads/`, `landing-pages/`, `reports/`, `assets/`) are a template — only create the ones a client actually uses.
- New client → create `clients/<name>/CLAUDE.md` first so future sessions have context.
- Never run npm inside Google Drive (it fails with EBADF): build site copies on the local disk.
- Git remotes: `origin` is this workspace (locate-digital-workspace), `site` is the public website (`_brand/site`, published with the `site-deploy` subtree branch), `demos` is the prospect demos (`/publish-demo`). Commit and push only when Sam asks.

## Memory

Three layers, each with one job:
- **CLAUDE.md files** — rules and folder conventions (this file, plus one per client and in some folders such as `_brand/Content/`).
- **Claude's auto-memory** — durable facts, decisions and preferences, kept outside the workspace in `~/.claude/projects/`.
- **Supabase `session_memories`** — one row per session, written by `/wrapup` and read by `/startup`. Schema in `_ops/supabase-memory-schema.sql`. If Supabase can't be reached, say so; don't quietly save a local file instead.

## Secrets

- API keys, passwords and credentials go only in a `.env` file: the workspace `.env` for agency-wide keys (Supabase), or `clients/<client>/.env` for one client's data sources (the monthly-report pipeline reads these). All are git-ignored. `.env.example` lists the workspace key names without values.
- Never print a value from `.env`. To check a key, confirm it's set with `[ -n "$VAR" ]`. Never `echo` it, `cat` the file or use `${VAR:-...}`.
- Keys go into `.env` by hand in a text editor, never through the chat.

## Skills

Every skill is a slash command. There are exactly two homes:

- **Central: `_skills/`** in this workspace (Google Drive, tracked in git). `C:\Users\samue\.claude\skills` is a Windows junction pointing here, so Claude Code loads these as user-level skills, available as `/skill-name` from any project. Edit skills in `_skills/`; never replace the junction with a real folder. `_skills/synced/` is managed by the Claude app and is git-ignored. Every skill that isn't tied to one client lives here:
  - Session memory: startup, wrapup (load and save session records in Supabase; see [Memory](#memory)).
  - Locate delivery: client-onboarding, service-delivery, tracking-setup, landing-page, google-ads-copy, meta-ad-copy, social-post, email-campaign, seo-audit, monthly-report-narrative, competitor-research, market-research, meeting-prep, client-report-call, discovery-call, check-in-call, humaniser (strips AI writing patterns; most writing skills run it last), plain-english.
  - Demo websites: design-to-site (Claude Design handoff → static demo in `_brand/Website Demo/demos/<industry>/`, checked and published), publish-demo (commit + push a snapshot of the demos folder → demo.locatedigital.io), launch-site (paying client: own private repo `site-<client>` + own Vercel project, WordPress migration, go-live, Pages CMS editors, later edits; process in `_ops/website-launch.md`, local clone in `clients/<client>/website/`). The prompt to paste into Claude Design is `_brand/Website Demo/claude-design-handoff-prompt.md`.
  - Locate brand: locate-content (weekly @locatingsam Instagram plan, hands reels to reels-script), reels-script, edit-reel (raw footage in `_brand/Content/Raw Footage/` → finished reel in `Exports/`, plus CapCut packs and change requests; drives `_brand/Content/remotion-kit/`), locate-voice (Facebook and the caption voice rules), human-web-design. Everything they read and write (weekly plans, profile, insights log, research, scripts, footage, exports) lives in `_brand/Content/`.
  - Long-form tutorials for Circle: edit-tutorial (face clips + screen recordings in `_brand/Tutorials/Raw Footage/` → 16:9 lesson, chapter list and captions in `_brand/Tutorials/Exports/`; drives `_brand/Tutorials/tutorial-kit/`). How Sam films them: `_brand/Tutorials/filming-guide.md`.
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
- Never write a dollar sign followed directly by a digit in a SKILL.md body (like a dollar-one figure). Claude Code reads it as an argument placeholder and swaps in the text typed after the command. Write "a grand" or "one to three million" instead.
- Third-party toolkits keep their own skills where the toolkit expects them (e.g. `G:\My Drive\claude-code-video-toolkit\.claude\skills`).
