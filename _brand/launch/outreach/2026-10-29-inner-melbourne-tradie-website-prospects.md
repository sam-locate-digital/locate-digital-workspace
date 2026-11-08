# Inner Melbourne tradies with bad websites: prospect list

29 October 2026 · Inner suburbs (Fitzroy, Collingwood, Richmond, Brunswick, Northcote, South Yarra, Prahran, St Kilda, Footscray, Hawthorn and neighbours)

## How this was built

1. I pulled every plumber, electrician, painter, carpenter and roofer listed on Yellow Pages across 10 inner suburbs, kept only businesses whose address is in an inner suburb, and kept only those with a website. That left 58 sites.
2. A script checked each site for red flags: down or parked, no HTTPS, no mobile viewport, old copyright year, very old HTML or CMS, DIY builders, no click-to-call link, no form, no analytics, and leftover placeholder text.
3. I opened the worst ~25 in a browser to confirm what a customer actually sees, and dropped any false alarms.

Your pitch tool: the tradie demo at **demo.locatedigital.io/tradie**.

---

## Tier 1: Website broken or gone (easiest pitch, "did you know your site is down?")

| # | Business | Suburb | Trade | Website | What a customer sees |
|---|---|---|---|---|---|
| 1 | **Baxter Electric** | Brunswick | Electrician | baxterelectric.com.au | "Error establishing a database connection". The WordPress site is broken. |
| 2 | **Caffyn Plumbing** | Brunswick | Plumber | caffynplumbing.com.au | The hosting company's "Default Web Site Page". No site at all. |
| 3 | **My Plumber** | Footscray | Plumber | myplumber.biz | A blank white page (0 bytes). |
| 4 | **New Era Electrical** | St Kilda | Electrician | neweraelectrical.com.au | Redirects to an error domain and never loads. |
| 5 | **Project Developments** (plumbing) | Abbotsford | Plumber | projectdevelopments.com.au | One line of text: "The URL … does not have a redirection page". |
| 6 | **CJM Plumbing** | Richmond | Plumber | cjmplumbing.melbourne | Times out and never loads. |
| 7 | **RS Roof & Building Maintenance** | Kew | Roofer / maintenance | rsbuilding.com.au | A "Coming Soon…" page with a broken logo image and a bare contact form. No HTTPS, not mobile-friendly. |
| 8 | **Melbourne 24 Hour Plumbing** | South Yarra | Plumber | melbourne24hourplumbing.com.au | A parked "Your Domains" page. *(It may be a lead-gen domain rather than a real business, so check before calling.)* |

## Tier 2: Live but badly dated (pitch: "you're losing jobs to better-looking competitors")

| # | Business | Suburb | Trade | Website | Problems (confirmed visually) |
|---|---|---|---|---|---|
| 9 | **ComSec Technologies** | Seddon | Electrical / security | comsectec.com.au | A genuine late-90s site: table layout, clip-art photos, red tartan sidebar. Not mobile-friendly, no phone link, no form, no analytics. |
| 10 | **AKA Plus Plumbing & Electrical** | Coburg | Plumber + electrician | akaplus.com.au | WordPress 3.8 (2013) with © 2010 and a wood-grain background. No click-to-call. |
| 11 | **Arek Painting & Decorating** | Northcote | Painter | arekdecorating.com.au | © 2015 and not mobile-friendly (no viewport tag). Old CMS (SilverStripe) and jQuery, no click-to-call, no H1. |
| 12 | **Ben Dixon Plumbing** | Elwood | Plumber | bendixonplumbing.com.au | One page of plain text and bullet points, no photos. The page title is "HELLO" and there's no HTTPS ("Not secure"). |
| 13 | **P Smith Plumbing** (est. 1982) | Cremorne | Plumber | psmithplumbing.com.au | A bare Wix page, just a heading and three buttons. No photos, no phone link, page title "Home \| psmithplumbing". |
| 14 | **The Plumbing Company** | St Kilda | Plumber | theplumbingcompany.com.au | © 2017. The hero is a stock photo of a woman in a shower, with no headline and no call to action. No H1. |
| 15 | **Treated With Colour** | Abbotsford | Painter / signage | treatedwithcolour.com.au | **"Lorem ipsum" template text left in the portfolio seven times** ("Use this area to describe your project…"). Stock paint-splash hero, no click-to-call. |
| 16 | **PT Electrical Services** | St Kilda West | Electrician | ptelectrical.com.au | GoDaddy DIY builder. The hero's only button is "Check out our Instagram", with no headline, no quote button and no analytics. |
| 17 | **L & A Petruccelli** (since 1960) | Abbotsford | Painter | petruccelli.com.au | DIY builder (Webs) with a dated layout. No enquiry form, no click-to-call, no analytics. |

## Tier 3: Fine-ish but improvable (lower priority)

- **Silaforts Painting** (Richmond): a GoDaddy builder site that looks decent. No form and no analytics.
- **WDFA Plumbing Solutions** (Northcote): Wix, niche dental-surgery plumbing, vague hero.
- **Your Pro Plumber** (Carlton): © 2015 in the footer, otherwise modern.

---

## Bonus: inner-suburb tradies with NO website on their listing

These Yellow Pages listings had no website link. Some may have a site the listing doesn't show, so do a quick Google before calling.

- **Plumbers:** Piceno Plumbing & Gas (Collingwood), Holmes Hydronics & Plumbing (Fitzroy), C B S Plumbing and M.A. Ball Plumbing (Abbotsford), Fresh Flow Plumbing, AFL Plumbing Services, Greg Salter Contract Plumbing (Richmond), McGrath Plumbing (Burnley), A Plus Plumbing & Gas, Go Go Gas Plumbing, Drizzle Plumbing (Brunswick)
- **Electricians:** NPJ Electrical, Proton Electrical, Dalton Electrical, Chisholm Electrical, Richmond Hill Electrical (Richmond), Next Generation Electrical, Pod Electrical (Cremorne), Convex Electrics, Waratah Electrical, Orbital Electrical, Trend Electrics (Brunswick), Your Electrician Collingwood

## Suggested order to approach

1. **Tier 1, 1–7.** A broken site is an urgent, undeniable problem. Open with a screenshot of what their customers see right now.
2. **Tier 2, 9–15.** Show their site next to the tradie demo. Lead with the concrete fault: not mobile-friendly, "Not secure", lorem ipsum, no call button.
3. **The no-website list.** Lead with "people searching '[trade] Richmond' can't find you."

## Caveats

- The source is Yellow Pages listings, so businesses that aren't on Yellow Pages are missed. I can run Google Maps or hipages next to widen the net.
- "Down" was checked on 29 Oct 2026. Some sites (especially CJM, which timed out) may be temporarily offline, so re-check on the day you call.
- I didn't look up phone numbers or owner names. Their Yellow Pages listings have the phone numbers.
