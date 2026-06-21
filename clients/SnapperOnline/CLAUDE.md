# Snapper Online — Client Context

> **⚠ DEMO CLIENT — pretend scenario. All data below is fictional, invented at onboarding for practice/testing. Do not report, publish, or bill against any of it.**

Onboarded: 2026-06-10

## Business
- **Industry:** Wedding photography
- **Locations:** Home studio — 14 Crown St, Surry Hills NSW 2010 (shoots on location across Greater Sydney, Blue Mountains, Hunter Valley, Southern Highlands)
- **Phone:** 0412 384 756
- **Website:** snapperonline.com.au
- **Staff:** Solo operator (second shooter contracted per wedding as needed)
- **Years operating:** 15+ (established 2010)
- **Scale:** ~25–30 weddings/year, plus ~15 engagement/elopement shoots
- **Key contact:** Andre Kong, andre@snapperonline.com.au

## Services
Primary (prioritise in all copy and campaigns):
- Full-day wedding photography (8–10 hr coverage)
- Elopement & micro-wedding packages

Secondary:
- Engagement shoots
- Wedding albums & fine-art prints
- Pre-wedding (tea ceremony / cultural events) coverage

## Target audience
Engaged couples 26–38 in Greater Sydney, household income $150k+, typically 9–15 months out from their date. Skew toward inner-city professionals planning venues in the Eastern Suburbs, Southern Highlands, and Hunter Valley. They research heavily on Instagram, care about candid/documentary style over posed formals, and decide based on portfolio consistency and how relaxed the photographer makes them feel. Strong secondary segment: Chinese-Australian couples wanting tea ceremony coverage (Andre is bilingual, Cantonese/English).

## Channels
| Channel | Status | Notes |
|---|---|---|
| Google Ads | Setting up | New — Locate Digital to build from scratch |
| SEO | Setting up | Site has weak local rankings; venue-page strategy planned |
| Meta Ads | Setting up | New — IG-led creative, engagement-season push |
| Google Business Profile | Needs work | Exists, 23 reviews, rarely posted to |
| Email | Not in scope | Enquiry follow-up handled in Studio Ninja |
| Social (organic) | Active (client-run) | IG @snapperonline ~4.2k followers; Andre posts, we advise |

## Tooling & integrations
| Tool | Purpose | Status |
|---|---|---|
| Studio Ninja | CRM / bookings / invoicing | API key TBD — in .env |
| Pixieset | Gallery delivery & client proofing | No API needed |
| GA4 | Website analytics | Property ID TBD — in .env |
| Google Ads | Paid search | Customer ID TBD — in .env |
| Meta Business Manager | Paid social | Ad account ID TBD — in .env |

## Baseline metrics (at onboarding — June 2026)
Document before touching anything. Used to prove ROI.
- Monthly enquiries/leads: ~8/month (peaks ~15 in Nov–Feb engagement season)
- Bookings: ~25–30 weddings/year (~2.5/month average)
- Average job value: $4,800 (full-day) / $2,200 (elopement) — blended ~$4,100
- Conversion rate (enquiry → booking): ~30%
- Google reviews: 23 reviews, 4.9 stars
- Monthly website sessions: ~1,100 (GA4, fictional baseline)
- Current ad spend: $0 — no paid history
- Current cost per lead: n/a (organic/referral only)

## Proof points
- Shooting Sydney weddings since 2010 — 400+ weddings photographed
- 4.9-star Google rating
- Featured (fictionally) in Hello May and Polka Dot Wedding
- Bilingual coverage: English + Cantonese (tea ceremonies, family formals)

## Competitors
- gezelligphotography.com.au (fictional)
- lanternandlace.com.au (fictional)
- tomhuntphoto.com.au (fictional)

## What's worked / what hasn't
Worked: word-of-mouth and venue referrals (about 60% of bookings); Instagram reels of candid first-look moments.
Hasn't worked: a 2024 wedding-expo stand (high cost, low-quality leads); a brief Groupon-style discount run that attracted budget shoppers who haggled.

## Existing assets
- Photos: extensive — 15 years of portfolio, full-res library in Pixieset
- Video: limited (BTS reels only, no videography service)
- Brand guidelines: no formal doc; logo + serif/sans pairing in use
- Logo files: TBD — request from Andre, store in `assets/`
- Email list: ~350 past clients/enquiries in Studio Ninja
- Testimonials/reviews available for use: yes — 23 Google reviews + Pixieset gallery comments

## Voice & tone
Warm, unhurried, quietly confident. First person ("I shoot…", not "we"). Romantic but never gushing — no "magical", "fairytale", "capture your special day" clichés. Plain Australian English, sentence case. Speaks to couples like a calm friend who's done 400 of these.

## Compliance & restrictions
- **Australian Consumer Law:** no misleading claims ("Sydney's best wedding photographer" needs substantiation — avoid superlatives)
- **Privacy Act (APPs):** client photos used in marketing require signed model/usage release — confirm Andre's contract includes one before repurposing galleries in ads
- **Copyright:** Andre retains copyright; usage terms in client contract — fine for our ads
- No industry licensing body (not AHPRA/legal/financial) — standard ACL rules only

## Engagement scope
What Locate Digital is responsible for:
- Google Ads build + management (search: "wedding photographer sydney" cluster)
- Meta Ads (engagement-season campaigns, Nov–Feb push)
- SEO: venue-page content strategy + GBP optimisation
- Monthly performance report

Not in scope (to prevent scope creep):
- Website redesign/development
- Organic Instagram posting (Andre runs it; we advise only)
- Email marketing

## Account access
| Platform | Access granted | Notes |
|---|---|---|
| Google Analytics 4 | Pending | Request Editor for sam@locatedigital.io |
| Google Ads | Pending | New account — create under Locate MCC |
| Meta Business Manager | Pending | Andre has personal IG/FB; BM may need creating |
| Google Business Profile | Pending | Request Manager access |
| Studio Ninja | Pending | API key for enquiry/booking data |
| Website / CMS | Pending | Squarespace (fictional) — admin invite |

## Reporting
- Cadence: monthly
- Format: HTML + PPTX
- Output path: `reports/YYYY-MM/`
- Sent to: Andre Kong, andre@snapperonline.com.au

## Goals
Lift enquiries from ~8/month to 20+/month within 6 months, holding cost per enquiry under $80, to fill the 2027 calendar (target: 35 weddings booked). Secondary: grow elopement/midweek bookings to smooth seasonality.

## Notes
- API keys and credentials in `.env` (gitignored)
- **DEMO CLIENT — all metrics, contacts, and competitors above are fictional**
- Peak enquiry season: Nov–Feb (post-engagement-season). Ad budgets should weight there.
- Monthly ad spend budget (fictional): $1,500/month ($900 Google / $600 Meta), scaling to $2,500 in season
