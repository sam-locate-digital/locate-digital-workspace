---
name: service-delivery
description: Route Locate Digital client work to the right delivery skill and SOP. Use when asked what to do for a client package, how to deliver a service line, what's included in Starter/Growth/Scale, which skill to run for a task, or to plan a month of fulfilment. Maps every rate-card service to its skill and the service delivery SOP.
---

# Service delivery — Locate Digital

The router for getting client work done. Given a package, a service line, or a task, this points you to the right skill and the matching SOP section so delivery is consistent every time.

Full detail lives in [`_ops/service-delivery-sop.md`](G:/My%20Drive/Claude%20Code.Locate/_ops/service-delivery-sop.md) in the Claude Code.Locate workspace. Read it for the steps and the "done when" standard. This skill is the index over the top of it.

## When this triggers

- "What's included in the Growth package?"
- "What do I need to do for [client] this month?"
- "Which skill writes the Google ads?"
- "Set up a new client's fulfilment plan."
- "How do we deliver conversion tracking / SEO / email?"

## How to use it

1. Work out what's being asked: a whole **package**, a single **service line**, or a **monthly plan** for one client.
2. Look it up in the map below.
3. Run the named skill. If it's marked ⚠, there's no Locate skill yet — open the SOP section and work from the steps, or use the `.claude/skills/ads-*` library noted there.
4. Always read the client's `clients/<name>/CLAUDE.md` first for voice and context.

## Service → skill map

| Service line | Skill to run | SOP § |
|---|---|---|
| Onboarding + setup | `client-onboarding` | 1 |
| Account audit | ⚠ `.claude/ads-audit` | 2 |
| Conversion tracking (GA4/GTM/server-side) | `tracking-setup` | 3 |
| Google Ads build + copy | `google-ads-copy` | 4 |
| Meta / Instagram Ads | `meta-ad-copy` | 5 |
| Extra platform (YouTube/LinkedIn) | ⚠ `.claude/ads-youtube` / `ads-linkedin` | 6 |
| Audience targeting + segmentation | within ad-copy skills | 7 |
| Ad creative + copy | `google-ads-copy` / `meta-ad-copy` + `humanizer` | 8 |
| A/B testing | ⚠ `.claude/ads-test` | 9 |
| CRO | `landing-page` (audit mode) | 10 |
| Landing pages | `landing-page` | 11 |
| SEO (on-page, technical, keywords, meta) | `seo-audit` | 12 |
| Blog content | `mosic-blog-post` | 13 |
| Google Business posts | `mosic-gmb-post` | 13 |
| Link building | ⚠ none yet | 14 |
| Email marketing | `email-campaign` | 15 |
| Monthly report + call | `monthly-report-narrative` | 16 |
| Strategy consulting | none — billed expertise | 17 |
| Market research | `market-research` | — |
| Competitor research | `competitor-research` | — |

## Package → what to deliver

**Starter ($1,800/mo)** — one channel (Google *or* Meta), basic targeting, GA4 tracking, monthly optimisation, monthly report + 1 call. SEO/email/blog are add-ons.

**Growth ($3,500/mo)** — both channels, advanced targeting + segmentation, ad creative, A/B testing, GA4 + GTM tracking, on-page SEO up to 5 pages, 1 blog/month, monthly report + strategy call.

**Scale ($6,500/mo+)** — multi-platform (+1 channel), retargeting, full creative + A/B, CRO, dedicated landing pages, server-side tracking, on-page SEO up to 10 pages, 2 blogs/month + link building, fortnightly calls + priority.

## Planning a client's month

1. Read their package and `CLAUDE.md`.
2. List every service line in that package from the matrix in the SOP.
3. For each, run the named skill or work the SOP steps.
4. Finish with the monthly report (`monthly-report-narrative`).
5. Never launch on broken tracking — § 3 is a hard gate.

## Open gaps

No Locate skill yet for: ad audit, link building. The SOP names the `.claude` fallbacks. Build order if you want to close them: `ad-audit` → `link-building`. (Conversion tracking → `tracking-setup`; blog + Google Business posts → `mosic-blog-post` / `mosic-gmb-post`.)
