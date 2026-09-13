# RAM — Client Context

Onboarded: 2026-06-28
Engagement: **Social media management** for the retail precincts held under RAM's listed REIT.

## Business
- **RAM Group** — Australian funds manager (ramgroup.com).
- **The fund:** RAM Essential Services Property Fund, **ASX: REP** — a stapled REIT investing in medical and essential-retail property.
- **What we manage:** organic social media for the fund's **7 retail precincts** — supermarket-anchored (Woolworths/Coles) neighbourhood/convenience shopping centres. Each is a local community shopping destination with its own retailers, food, services and catchment.
- **Note:** several REP assets are being divested (term-sheet sale of Coomera Square, Springfield Fair, Coles Rutherford, Keppel Bay Plaza, Mowbray Marketplace per HY26 updates). **Confirm the live list of 7 with the client — don't assume from public data.**

## The 7 precincts (confirmed 2026-06-28, full briefs in `precincts/`)

| Precinct | Location | Anchor | Existing IG |
|----------|----------|--------|-------------|
| Ballina Central | Ballina, NSW | IGA SUPA VALU + Big W | TBD |
| The Broadway Plaza | Punchbowl, NSW (SW Sydney) | Woolworths | TBD |
| Rutherford Shopping Centre | Rutherford, NSW (Maitland) | Coles | FB only |
| Mowbray Marketplace | Mowbray, TAS (Launceston) | Woolworths + Target | @mowbraymarketplace ✅ |
| Coomera Square | Upper Coomera, QLD (Gold Coast) | Woolworths | @coomerasquare ✅ |
| Springfield Fair | Springfield, QLD (Ipswich) | Coles | @springfieldfairshoppingcentre ✅ |
| Keppel Bay Plaza | Yeppoon, QLD | Coles + Target | FB only ("Bay Plaza Yeppoon") |

**Flags:**
- 3 centres already have active IG (Mowbray, Coomera, Springfield) — get account access, audit the existing feed, keep continuity.
- **Keppel Bay Plaza** trades publicly as **"Bay Plaza Yeppoon"** — confirm which name to use on social.
- **Ballina Central** ≠ Ballina Fair; **Coomera Square** ≠ Upper Coomera Shopping Centre. Don't mix them up.
- Benchmark/strategy notes from peer research (Westfield etc): `sop/social-benchmarks.md`.

## Audience & voice (TO CONFIRM)
- Primary audience is **local shoppers / community** around each precinct (not investors — that's REP's corporate channel, separate).
- Each precinct likely has its own social presence and light brand. Posts are warm, local, community-first — what's on, who's in store, what's new, seasonal moments.
- Australian English. Plain, friendly, never corporate-stiff. Humanizer always on.

## Post themes (working set — refine with client)
- Retailer spotlights (a store, a new opening, a local favourite)
- Offers / promotions / "what's on special"
- Events & activations (school holidays, seasonal, community days)
- Seasonal / calendar moments (Easter, Mother's Day, Christmas, EOFY)
- Community & convenience ("everything you need in one stop")
- New tenants / centre news / trading-hours updates

## Workflow (confirmed 2026-06-28)
- **Platform: Instagram** (feed + Stories). Not FB/LinkedIn at this stage.
- **Cadence: 2–3 posts per precinct per week** (~14–21/week, ~60–90/month total).
- **Voice: each precinct as its own local community brand** (not a unified corporate look).
- **Design: Canva brand templates** — one master set, reskinned per precinct (swap logo + 2 colours). Canva MCP is connected.
- Approval: TBD (who signs off per precinct, lead time) — capture in each precinct brief.
- Asset source: TBD (RAM supplies photos/offers vs we source) — capture in each precinct brief.

## How we produce posts (system built 2026-06-28)
- **Skill:** `ram-precinct-post` (in `~/.claude/skills/`) — generates caption + hashtags + visual direction + Canva template, per precinct + pillar. Reads this file + the precinct brief.
- **SOP:** `clients/RAM/sop/social-media-sop.md` — the repeatable monthly batch process.
- **Designs:** `clients/RAM/sop/post-templates-showcase.html` — the 8-template set (spec for the Canva masters).
- **Calendar:** `clients/RAM/sop/content-calendar.xlsx` — monthly planner with pillar rotation + status tracking.
- **Precinct briefs:** `clients/RAM/precincts/<precinct>.md` (copy `_TEMPLATE.md`, one per centre).
- **Output:** `clients/RAM/content/<precinct>/<YYYY-MM>/`.

## Status
System built 2026-06-28 (skill, SOP, templates, calendar, brief template). **Blocked on client inputs:** the 7 precinct names/details (fill the briefs), each precinct's logo + brand colours (for Canva skins), and approval/asset-source per centre.
