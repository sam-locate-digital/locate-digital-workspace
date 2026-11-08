# Hyrox Injury campaign — Google Ads Editor import

Account: Osteopathy (190-328-0865). The campaign imports **paused**. Full plan and reasoning: `../hyrox-injury-campaign-2026-10.md`.
To regenerate the files (e.g. once the landing page URL is final): `python ../build_hyrox_editor_import.py https://<final-url>`

## 1. Import (in this order)

In Google Ads Editor: **Get recent changes** for the Osteopathy account, then for each file **Account → Import → From file…**:

1. `01-campaign.csv` — campaign: $30/day, Maximise clicks, Search only, ends 31 Dec, paused
2. `02-ad-groups.csv` — 4 ad groups
3. `03-keywords.csv` — 32 phrase + 3 exact
4. `04-negative-keywords.csv` — 92 campaign-level negatives
5. `05-ads.csv` — 4 responsive search ads (headline 1 pinned to position 1, headline 2 to position 2, description 1 to position 1)

After each file, Editor shows a review screen. If it reports an unmapped column, map it by hand. The usual one is `Criterion Type` on the negatives, which should map to campaign-level negative phrase/exact. Then **Finish and review changes**.

## 2. Settings to set by hand in Editor (2–3 minutes)

These are faster to click than to import reliably:

- [ ] **Bid strategy:** Maximise clicks → **Maximum CPC bid limit $6.00**
- [ ] **Networks:** untick Search Partners and Display Network (check this even though the import sets it)
- [ ] **Locations:** remove any country-level target, then add a radius of **10 km around Bourke St, Melbourne VIC 3000** and a radius of **8 km around Essendon VIC 3040**
- [ ] **Location options:** Target = **Presence: people in or regularly in your targeted locations**
- [ ] **Devices:** Mobile bid adjustment **+20%**
- [ ] **Ad rotation:** Optimise
- [ ] **Assets** (campaign level):
  - Call: (03) 9663 6202
  - Callouts: Sports Injury Osteopaths · Exercise Physiologist · Online Booking · CBD and Essendon Clinics · Race Day Planning
  - Structured snippet, header *Services*: Osteopathy, Exercise Physiology, Sports Injury, Prehab
  - Location: check the account's Google Business Profile link covers both clinics

## 3. Before you enable

- [ ] Landing page is live, and the final URL in all 4 ads matches it (placeholder: `https://melbourneosteopathycentre.com.au/hyrox-injury/`)
- [ ] Every Book button on the page goes to Cliniko, so the `make_a_booking` conversion fires
- [ ] **Post** from Editor, then check the ads pass policy review in the Google Ads UI. If they're disapproved for the Hyrox trademark, swap in the backup headlines from the plan
- [ ] Enable the campaign

## 4. Conversion tracking (done 22 Oct 2026 through Adspirer)

Moved to **secondary** (no longer counted as conversions):

- GA4 `GA4_M`, `GA4_B`, `GA4_P` and `GA4_E` (93% of the inflated count)
- GA4 `subscribe`

Changed: Cliniko `make_a_booking` value set to $120 AUD.

**Still to do by hand in the Google Ads UI** (Goals → Conversions → Summary):

- [ ] `Local actions - Menu views` and `Clicks to call`: set to secondary. These are Google-hosted actions and the API won't change them.
- [ ] Cliniko `make_a_booking`: check **"Use the same value for each conversion"** is on at $120
- [ ] Cliniko `appointment` (17 vs 42 bookings): check whether it double-counts `make_a_booking`. If it does, set it to secondary.
- [ ] `Call` (calls from ads): set the call length to count to **60 seconds**
- [ ] Optional tidy-up: the old Universal Analytics goals stopped recording in 2024, so they can be set to secondary or removed
