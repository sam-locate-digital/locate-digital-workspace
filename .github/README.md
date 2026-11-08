# Locate Digital: agency workspace

Private repo, internal use only. This is Locate Digital's working folder: client work, Locate's own brand and marketing, the website and demo sites, and the Claude skills that do most of the delivery. It lives in Google Drive at `G:\My Drive\Claude Code.Locate` and is backed up here.

Locate Digital does websites, Google and Meta ads, SEO and practical AI training, mainly for Australian financial service providers and local service businesses.

The full working rules for Claude are in [`CLAUDE.md`](../CLAUDE.md). This page is the short version.

## Folder layout

```
.
├── _brand/        Locate's own brand: guidelines, logos, photos, website, demo sites, launch kit, Instagram content, tutorials
├── _guides/       Industry marketing checklists site (its own repo too)
├── _ops/          SOPs, client guides, website-launch process, tools, skill tests and packages
├── _services/     Service lines and their sales material (e.g. AI training)
├── _skills/       Every general Claude skill, loaded from any project through a junction
├── _templates/    Proposal, report and copy templates
├── clients/       One folder per client, each with its own CLAUDE.md
├── _inbox/        Files with no home yet (git-ignored)
└── _to-delete/    Holding folder for anything being removed (git-ignored)
```

## Where things are published

| What | Source here | Repo | Live at |
|---|---|---|---|
| Locate website | `_brand/site/` | Locate-Digital-Website (remote `site`) | www.locatedigital.io |
| Prospect demo sites | `_brand/Website Demo/demos/` | Locate-digital-demos (remote `demos`) | demo.locatedigital.io/&lt;industry&gt; |
| Paying-client sites | `clients/<client>/website/` (git-ignored clone) | site-&lt;client&gt;, one per client | client's own domain |
| Industry checklists | `_guides/checklists/` | locate-digital-checklists | Vercel |

The processes are in `_ops/website-launch.md` and the `/publish-demo` and `/launch-site` skills.

## Clients

| Folder | Client |
|---|---|
| `MOSIC` | Melbourne Osteopathy Sports Injury Centre: Google Ads, SEO, blog, Google Business and social posts |
| `BrightenHomeLoans` | Non-bank mortgage lender |
| `MaxiFinancial` | Mortgage broker |
| `RAM` | Social media for the retail precincts in RAM's listed REIT |
| `MedCannabis` | Onboarding; business name to be confirmed |
| `GlossHairStudio` | Early stage, content only |
| `SnapperOnline` | Demo client with made-up data, for practice and testing |

## Skills

Every skill is a slash command. General skills live in `_skills/` (the user-level skills folder `~/.claude/skills` is a Windows junction pointing there). Skills for a single client live in `clients/<client>/.claude/skills/`. The full list and the rules for writing skills are in `CLAUDE.md`.

## Memory and secrets

- Claude's session log lives in Supabase (`session_memories`), saved with `/wrapup` and loaded with `/startup`. Schema: `_ops/supabase-memory-schema.sql`.
- Keys live in `.env` files (the workspace one, plus one per client for data sources), all git-ignored. `.env.example` lists the workspace key names.

## Monthly report pipeline

`_ops/tools/monthly-report/` pulls GA4, Cliniko and Google Ads data into a Markdown and HTML report:

```bash
python generate.py "clients/MOSIC/.env"          # previous full month
python generate.py "clients/MOSIC/.env" 2026-04  # a specific month
```

The output goes to `clients/<client>/reports/YYYY-MM/`. `/monthly-report-narrative` then writes the commentary.

## Conventions

- Australian English and sentence-case headings everywhere.
- Commit messages: `<type>(<scope>): <what changed>`, e.g. `feat(skills): add publish-demo`.
- Large media (raw footage, exports, photos, video) stays in Google Drive and out of git.
- Never run npm inside Google Drive (it fails with EBADF). Build on the local disk.
