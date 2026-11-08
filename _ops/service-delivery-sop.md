# Service delivery SOP — Locate Digital

How every line on the rate card actually gets done. One entry per service, with the steps, what "finished" looks like, and the skill to run. Use this so delivery is the same every time, no matter who's doing it.

Rate cards: [physio/osteo](../_brand/launch/rate-card.html) · [generic](../_brand/launch/rate-card-generic.html).

## How to read this

Each service has:
- **Delivered** — what the client actually gets
- **Steps** — the work, in order
- **Done when** — the standard. Don't tick it off until this is true
- **Skill** — the Locate skill to run (or ⚠ if there's no skill yet and you work from the steps here)
- **Cadence** — once-off, monthly, etc.

---

## Package → service matrix

| Service | Starter | Growth | Scale |
|---|:---:|:---:|:---:|
| Onboarding + setup | ✓ | ✓ | ✓ |
| Account audit | ✓ | ✓ | ✓ |
| Conversion tracking | GA4 | GA4 + GTM | Server-side |
| Google Ads | one channel option | ✓ | ✓ |
| Meta Ads | one channel option | ✓ | ✓ |
| Extra platform (YouTube/LinkedIn) | — | — | ✓ |
| Audience targeting + segmentation | basic | advanced | advanced + retargeting |
| Ad creative + copy | ✓ | ✓ | full production |
| A/B testing | — | ✓ | ✓ |
| CRO | — | — | ✓ |
| Landing pages | add-on | add-on | ✓ |
| On-page SEO | add-on | up to 5 pages | up to 10 pages |
| Blog content | add-on | 1/month | 2/month |
| Link building | — | — | ✓ |
| Email marketing | add-on | add-on | add-on |
| Monthly report + call | report + 1 call | report + strategy call | report + fortnightly calls |

---

## 1. Onboarding + setup

- **Delivered:** full client workspace, access to all accounts, a kickoff call, the month-one build plan.
- **Steps:**
  1. Run the onboarding skill to create the client folder, `CLAUDE.md`, and `.env`.
  2. Get access: Google Ads, Meta Business, GA4, GTM, website, Google Business Profile.
  3. Confirm goals and a baseline (current leads/bookings per month). Write the baseline into `CLAUDE.md` — you'll measure everything against it.
  4. Agree the reporting date and the single point of contact.
- **Done when:** every account is connected, the baseline is recorded, and the client knows what month one looks like.
- **Skill:** `client-onboarding`
- **Cadence:** once-off (covered by the $1,500 setup fee)

## 2. Account audit

- **Delivered:** a short findings doc — what's wrong now, what it's costing them, what we'll fix first.
- **Steps:**
  1. Pull the existing ad account(s), GA4, and Google Business Profile.
  2. Note wasted spend, missing tracking, weak targeting, off-catchment clicks.
  3. Rank findings by impact. Lead with the money leaks.
- **Done when:** the client has a plain-English list of fixes, ranked.
- **Skill:** ⚠ no `_skills` audit yet — use the `.claude/skills/ads-audit` library, or work from these steps. *(Gap: a Locate `ad-audit` skill would standardise this.)*
- **Cadence:** once-off at setup, then quarterly

## 3. Conversion tracking

- **Delivered:** every lead action (call, form, booking) tracked back to the ad that drove it.
- **Steps:**
  1. **Starter — GA4:** events for calls, form submits, booking clicks.
  2. **Growth — GA4 + GTM:** the above via Tag Manager, plus the ad platform pixels (Google tag, Meta pixel) firing on the right events.
  3. **Scale — server-side:** server-side GTM / CAPI so tracking survives ad blockers and iOS.
  4. Test every event fires before launch. No campaign goes live on broken tracking.
- **Done when:** a test lead shows up correctly in GA4 and the ad platform.
- **Skill:** `tracking-setup` (references `.claude/skills/ads-server-side-tracking` and `ads-attribution` for the deep server-side detail).
- **Cadence:** once-off at setup; recheck quarterly

## 4. Google Ads

- **Delivered:** built and managed search (and display, on higher tiers) campaigns targeting their catchment.
- **Steps:**
  1. Keyword + intent research for the service and area.
  2. Campaign + ad group structure; set location and audience targeting.
  3. Write RSA copy with the ad-copy skill.
  4. Launch, then optimise monthly: search terms, negatives, bids, budget.
- **Done when:** campaigns are live, tracking conversions, and reviewed every month.
- **Skill:** `google-ads-copy` for the copy. *(Deeper analysis: `.claude/skills/ads-google`.)*
- **Cadence:** build once, manage monthly

## 5. Meta Ads

- **Delivered:** built and managed Facebook + Instagram campaigns.
- **Steps:**
  1. Set the objective (leads or calls), audiences, and placements.
  2. Produce creative + copy with the Meta skill.
  3. Launch, watch frequency and creative fatigue, refresh on a cycle.
- **Done when:** campaigns are live, tracked, and creative is refreshed before it fatigues.
- **Skill:** `meta-ad-copy`. *(Deeper analysis: `.claude/skills/ads-meta`.)*
- **Cadence:** build once, manage monthly

## 6. Extra platform — YouTube / LinkedIn (Scale only)

- **Delivered:** a third channel matched to the client (YouTube for reach, LinkedIn for B2B service businesses).
- **Steps:** mirror the paid-media build — objective, audience, creative, tracking, optimise.
- **Done when:** the third channel is live and pulling its weight in the report.
- **Skill:** ⚠ use `.claude/skills/ads-youtube` or `ads-linkedin`.
- **Cadence:** build once, manage monthly

## 7. Audience targeting + segmentation

- **Delivered:** spend pointed at the right people in the right area, not the whole city.
- **Steps:** define catchment, demographics, and intent signals; on Growth+ split audiences so you can see what converts; on Scale add retargeting of site visitors and past enquiries.
- **Done when:** no budget is going to clearly out-of-area or irrelevant audiences.
- **Skill:** built into `google-ads-copy` / `meta-ad-copy` setup.
- **Cadence:** set at build, review monthly

## 8. Ad creative + copy

- **Delivered:** the actual headlines, descriptions, images and (on Scale) video.
- **Steps:** write to the offer and the audience; produce variations for testing; keep it on-brand and in plain Australian English.
- **Done when:** each campaign has enough variations to test, all on-brand.
- **Skill:** `google-ads-copy`, `meta-ad-copy`. Run output through `humanizer`.
- **Cadence:** at build, then refresh monthly

## 9. A/B testing (Growth + Scale)

- **Delivered:** structured tests that tell you what actually works.
- **Steps:** one variable at a time (headline, creative, audience, landing page); set a hypothesis and a sample size; run to significance before calling it.
- **Done when:** the test reached significance and the winner is rolled out.
- **Skill:** ⚠ use `.claude/skills/ads-test`. *(Gap: a Locate `ab-test` skill.)*
- **Cadence:** ongoing

## 10. CRO (Scale only)

- **Delivered:** more of the existing traffic turning into enquiries.
- **Steps:** find the drop-off (heatmaps, form analytics), fix the page, test the change.
- **Done when:** conversion rate on the target page improves and holds.
- **Skill:** `landing-page` (audit mode). *(Reference `.claude/skills/ads-landing`.)*
- **Cadence:** ongoing

## 11. Landing pages

- **Delivered:** a purpose-built page for the campaign, matched to the ad.
- **Steps:** write with the landing-page skill; match message to ad; one clear call to action; build mobile-first.
- **Done when:** the page is live, tracked, and the message matches the ad.
- **Skill:** `landing-page`
- **Cadence:** per campaign / as an add-on

## 12. SEO — on-page, technical, keywords, meta tags

- **Delivered:** pages that rank for local "near me" searches.
- **Steps:**
  1. Run the SEO audit skill for the technical and on-page state.
  2. Keyword research for the service + suburb.
  3. Fix titles, meta descriptions, headings, internal links.
  4. Page count by tier: Growth up to 5, Scale up to 10.
- **Done when:** target pages are optimised and the audit's red flags are cleared.
- **Skill:** `seo-audit`
- **Cadence:** audit once, implement, recheck quarterly

## 13. Blog content

- **Delivered:** SEO-friendly blog posts, written and posted.
- **Steps:** pick topics from keyword gaps and patient/customer questions; write in the client's voice; run through humanizer; publish and internally link.
- **Done when:** the post is live, on-brand, and reads like a human wrote it.
- **Skill:** `mosic-blog-post` (blog) and `mosic-gmb-post` (Google Business posts). Adapt per client from the client's `CLAUDE.md`.
- **Cadence:** Growth 1/month, Scale 2/month

## 14. Link building (Scale only)

- **Delivered:** quality local + industry backlinks.
- **Steps:** local directories and associations, partner sites, digital PR; track new links and domain authority.
- **Done when:** new relevant links are earned and logged.
- **Skill:** ⚠ none. *(Gap: a `link-building` SOP/skill.)*
- **Cadence:** ongoing

## 15. Email marketing (add-on)

- **Delivered:** a full campaign or sequence — every email, design, automation, segmentation.
- **Steps:** run the email skill; set the segments and automation triggers; A/B the subject lines.
- **Done when:** the sequence is built, segmented, and scheduled.
- **Skill:** `email-campaign`
- **Cadence:** monthly (count by package: 1–3 campaigns)

## 16. Monthly report + call

- **Delivered:** a plain-English report — leads/new patients, cost per lead, what changed, what's next — plus the call.
- **Steps:** pull the numbers, run the narrative skill, hold the call (Starter monthly, Scale fortnightly).
- **Done when:** the client understands their results and the next month's plan.
- **Skill:** `monthly-report-narrative`
- **Cadence:** monthly

## 17. Strategy consulting (add-on, $200/hr)

- **Delivered:** bespoke advice — planning, market entry, channel strategy.
- **Steps:** scope the question, do the thinking, hand over clear recommendations.
- **Done when:** the client has a decision they can act on.
- **Skill:** none — this is your expertise, billed by the hour.
- **Cadence:** as booked

---

## Skill gaps worth filling

These services have no dedicated Locate skill yet. Right now you lean on the `.claude/skills/ads-*` library or these manual steps. Worth building, in priority order:

1. ~~`tracking-setup`~~ — ✓ built. GA4 + GTM + server-side.
2. **`ad-audit`** — standardise the setup + quarterly audit.
3. **`link-building`** — Scale only, lowest volume.

A/B testing and CRO are covered well enough by the `.claude` library for now. Blog and Google Business posts are covered by `mosic-blog-post` / `mosic-gmb-post`.

---

## The one rule

Nothing goes live on broken tracking. If you can't measure the lead, you can't prove the result, and the result is the whole product.
