# MOSIC — Hyrox Injury Search campaign (October 2026)

Built from `hyrox-injury-keywords-2026-10.csv` and `hyrox-injury-negatives-2026-10.txt`. Account: Osteopathy (190-328-0865).

## Campaign settings

| Setting | Value | Why |
|---|---|---|
| Name | `MOSIC Hyrox Injury Search 2026` | Matches the live campaign's naming |
| Budget | $30/day (≈ $1,050 to 31 Dec) | Agreed budget. Hyrox search volume is niche, so expect underspend early |
| Dates | Start when the landing page is live, end 31 Dec 2026 | Race week 9–13 Dec, then two weeks of post-race recovery |
| Network | Search only (no Display, no Search Partners) | Booking intent lives on Google Search. Revisit Partners at 60 days |
| Bidding | Maximise Clicks, max CPC $6 | No Hyrox conversion history, and the account's conversion data is polluted (see Tracking). Switch to Maximise Conversions only after clean tracking shows 30+ bookings/month |
| Locations | 10 km radius around Bourke St (Melbourne 3000), 8 km around Essendon 3040 | Covers inner Melbourne and the north-west catchment for both clinics |
| Location option | Presence: people in or regularly in the targeted area | The default ("presence or interest") pays for people outside Melbourne |
| Ad schedule | All hours | No opening hours supplied. Review after 2 weeks of data |
| Devices | All, mobile +20% | Injury and "near me" searches skew mobile, and mobile is where call taps happen |
| Ad rotation | Optimise | Lets Google favour the RSA combinations that convert |
| Final URL | Hyrox landing page (in build) — `https://melbourneosteopathycentre.com.au/hyrox-injury/` placeholder, confirm slug | A dedicated page matches the search and converts better than the homepage |
| Display path | `/hyrox-injury` | Mirrors the query |

## Ad groups and keywords

Phrase match throughout, plus exact match on the three highest-intent terms. No broad match: there's no clean conversion signal for Smart Bidding to steer it.

**1. Hyrox Injury Treatment**
`"hyrox physio"` · `"hyrox physiotherapist"` · `"hyrox osteo"` · `"hyrox osteopath"` · `"hyrox injury"` · `"hyrox injuries"` · `"hyrox training injury"` · `"hyrox training injuries"` · `"hyrox melbourne injury"` · `[hyrox injury]` · `[hyrox physio]`

**2. Hyrox Knee and Back**
`"hyrox knee pain"` · `"hyrox knee injury"` · `"hyrox and knee pain"` · `"hyrox training knee pain"` · `"hyrox lunges knee pain"` · `"hyrox with knee injury"` · `"hyrox bad knees"` · `"hyrox back pain"` · `"hyrox lower back pain"` · `"hyrox back injury"` · `"hyrox with back pain"` · `[hyrox knee pain]`

**3. Hyrox Lower Leg**
`"hyrox achilles"` · `"hyrox achilles tendonitis"` · `"hyrox shin splints"` · `"shin splints before hyrox"` · `"calf strain hyrox"` · `"hyrox plantar fasciitis"`

**4. Hyrox Pre and Post Race**
`"injured before hyrox"` · `"injury before hyrox"` · `"hyrox prehab"` · `"hyrox injury prevention"` · `"sore after hyrox"` · `"lower back pain after hyrox"`

**Dropped from the research list:** all massage terms (MOSIC doesn't offer massage), and the low-intent research terms (calf cramp, hamstrings, hip/knee replacement, post-race recovery, shoulder).

**Negatives:** the full `hyrox-injury-negatives-2026-10.txt` list, plus `massage`, `free`, `jobs`, `course`, `certification`.

## Responsive search ads

One RSA per ad group. Headlines 1–4 are specific to the ad group, and 5–15 are shared across all four. Character counts are in brackets.

### Ad group headlines

| Ad group | H1 (pin pos 1) | H2 | H3 | H4 |
|---|---|---|---|---|
| Treatment | Hyrox Injury Treatment (22) | Hyrox Osteo Melbourne (21) | Hyrox Injury Melbourne (22) | Injured Training for Hyrox? (27) |
| Knee and Back | Hyrox Knee Pain Treatment (25) | Hyrox Back Pain Treatment (25) | Knee Pain From Lunges? (22) | Sled Push Back Pain? (20) |
| Lower Leg | Hyrox Achilles and Calf Pain (28) | Shin Splints Before Hyrox? (26) | Running Injury Treatment (24) | Plantar Fascia Pain Help (24) |
| Pre and Post Race | Injured Before Hyrox? (21) | Hyrox Prehab Melbourne (22) | Sore After Hyrox? (17) | Weeks Out From Race Day? (24) |

### Shared headlines (5–15)

5. Melbourne CBD and Essendon (26) — **pin position 2**
6. Hyrox Injury Assessment (23)
7. Book Your Hyrox Assessment (26)
8. Sports Injury Osteopaths (24)
9. Exercise Physiologist On Staff (30)
10. Melbourne Race Week 9-13 Dec (28)
11. Plan Built Around Race Day (26)
12. Modified Training Plans (23)
13. Running and Station Injuries (28)
14. Call (03) 9663 6202 (19)
15. Book Online Today (17)

**Backup headlines if "Hyrox" in ad text gets disapproved:** Functional Fitness Race Injury (30) · Fitness Race Injury Treatment (29). Keywords can stay as they are.

### Descriptions (max 80 characters, Adspirer's limit)

| # | Text | Chars |
|---|---|---|
| D1 (pin pos 1, all groups) | Book a Hyrox injury assessment online, or call our CBD clinic on (03) 9663 6202. | 80 |
| D2 (all groups) | 8 osteopaths and an exercise physiologist across Melbourne CBD and Essendon. | 76 |
| D3 (all groups, until 13 Dec) | Race week is 9-13 December. Get assessed now and keep more training options. | 76 |
| D4 Treatment | Osteo care for Hyrox running and stations, with a plan built around race day. | 77 |
| D4 Knee and Back | Knee pain from lunges or back pain from sleds? Get assessed before race day. | 76 |
| D4 Lower Leg | Achilles, calf, shin or foot pain from rising run volume? Get it assessed early. | 80 |
| D4 Pre and Post Race | Prehab with our exercise physiologist, or treatment if you're carrying a niggle. | 80 |
| D3 swap from 14 Dec | Sore or niggly after race day? Get assessed and plan your recovery properly. | 76 |

**Pinning:** H1 to position 1 so the ad group's query always shows, "Melbourne CBD and Essendon" to position 2 for a local signal, and D1 to description 1 so the booking and phone line always shows. If Ad Strength drops to "Average", remove the position 2 pin first.

**AHPRA check:** no testimonials, no outcome promises ("fix", "pain-free by race day"), no superiority claims, no price or discount. Hyrox is used descriptively only, and nothing implies MOSIC is an official partner.

## Assets

- **Call:** (03) 9663 6202, AU, with Google forwarding number for call tracking
- **Callouts:** Sports Injury Osteopaths · Exercise Physiologist · Online Booking · CBD and Essendon Clinics · Race Day Planning
- **Structured snippet (Services):** Osteopathy, Exercise Physiology, Sports Injury, Prehab
- **Location:** link the Google Business Profile for both clinics (account-level)
- **Sitelinks:** add once the landing page and its anchor sections are live (Google requires the same domain as the final URL, so the Cliniko booking link can't be a sitelink)

## Tracking

Audit of the account's conversion actions (90 days to 21 Oct 2026):

- 862.9 "conversions" recorded. **93% of them come from four GA4 events named `GA4_M`, `GA4_B`, `GA4_P` and `GA4_E`**, worth $1 each. They fire on most visits, which means they're page activity, not bookings.
- **Real bookings:** the Cliniko GA4 `make_a_booking` event recorded 42, plus `appointment` 17 (probably counting the same bookings). Calls from ads recorded 1.
- The live campaign's "294 conversions from 497 clicks" (30 days) is therefore inflated. Its true cost per booking is closer to $50–75 than the reported $3.66.

**Recommended clean primary set:** Cliniko `make_a_booking` (Book appointment, $120 value), `Call` (calls from ads, 60-second minimum), GA4 `phone` tap. Demote the four `GA4_*` events, Menu views, Clicks to call, the `subscribe` events and the dead Universal Analytics goals to secondary. Note that this changes what the live osteo campaign counts as a conversion.

**Done 22 Oct 2026 (Adspirer):** the four `GA4_*` events and GA4 `subscribe` are now secondary, and `make_a_booking` is valued at $120. The remaining manual steps are in `editor-import/README.md`. From now on, the live osteo campaign's conversion count will drop to real bookings and calls. That's expected and it's the true figure, not a fall in performance.
