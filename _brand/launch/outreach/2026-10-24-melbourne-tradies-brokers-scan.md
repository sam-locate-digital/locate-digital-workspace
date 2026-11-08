# Melbourne tradies & mortgage brokers: marketing and website scan

24 October 2026 · Melbourne metro

## How "popular" was measured

- **Tradies:** the top of ProductReview.com.au's Victorian plumber and electrician rankings (sorted by review activity), checked against the review counts each business puts on its own site.
- **Brokers:** Google review counts the brokerages claim (500+ tier), plus RateMyAgent's most-reviewed Melbourne brokers.
- **Marketing stack:** I loaded each homepage in a real browser and logged every third-party script that fired (ad tags, pixels, call tracking, CRM, chat). I also scanned the raw HTML and searched the Meta Ad Library (AU, active ads) by business name.
- **Website quality:** a desktop screenshot review of the above-the-fold area, the title and H1, load time in the browser, and any visible bugs.

Scores out of 10 are my judgement. **Site** is design, clarity and conversion. **Marketing** is how sophisticated their tracking and acquisition is.

---

## Tradies

| # | Business | Popularity signal | Site | Marketing |
|---|---|---|---|---|
| 1 | **HomeFirst Services** (plumbing, HVAC, electrical) | ~4,040 ProductReview reviews (4.6); 766+ Google | 8 | 9 |
| 2 | **O'Shea Plumbing** (since 1978) | "3,000+ 5-star reviews", 42,000+ homeowners; 4.9 PR + 2026 award | 7 | 9 |
| 3 | **Irwin's Plumbing** | 4.9 PR, #2 on ProductReview list | 8 | 8 |
| 4 | **Darebin** (Darebin Gas / Trade Services, since 1985) | 888 reviews claimed; 4.9 PR + 2026 award | 4 | 6 |
| 5 | **Ruttley Services** (plumbing & electrical) | 446 reviews; 4.5 PR | 6 | 7 |
| 6 | **GHS Plumbing & Electrical** (Narre Warren) | 4.8 PR + 2026 award | 0 | ? |

**HomeFirst Services**: homefirstservices.com.au
- Site: modern and confident. Real team-and-van photo, a big "Call us" CTA, Google rating in the hero, a sticky "Book now". There's a typo in the meta description ("Trdaie"), and it took ~5.4s to load.
- Marketing: the most complete stack of the tradies. GTM, GA4, Google Ads conversion and remarketing, Meta pixel (1 active Meta ad), dynamic call tracking (trkcall), ServiceTitan online scheduler, Trustindex review widget and Microsoft Clarity. It also loads an OpenAI script that looks like ChatGPT ads conversion tracking, which makes it an early adopter.

**O'Shea Plumbing**: osheaplumbing.com.au
- Site: the SEO title is spot on ("Plumber Melbourne: 3,000+ 5-Star Reviews"), with a "Click to book" panel (book / emergency / enquiry). The header is cluttered: two stacked bars, and the star-rating line is nearly invisible on navy.
- Marketing: very mature. ServiceTitan booking plus dynamic number insertion, Google Ads, Meta pixel with Conversions API automation, Pinterest tag, LiveChat, Clarity, and NitroPack for speed. No active Meta ads turned up under the name.

**Irwin's Plumbing**: irwinsplumbing.com.au
- Site: the strongest brand of the group. Bold yellow and blue, a "No leaks. No worries" line, a founder-voice quote, an offer bar ($85 off first service), trust badges and a Wistia video. Bug: the header phone number is cut off ("1300 152 3…") at laptop and tablet widths. It's heavy, with 142 requests and ~6.5s to load.
- Marketing: Google Ads plus **Microsoft/Bing Ads**, and **ClickCease** click-fraud protection (a sign of meaningful Google spend). Also GA4, GTM and Clarity. No Meta pixel and no Meta ads found, so social is a gap.

**Darebin**: darebin.com.au
- Site: weak for its reputation. The hero has no headline and no CTA, just a dark-overlaid team photo. The H1 is "Providing end-to-end solutions to a diverse clientele!", which says nothing. The nav is cramped and the load took ~7.4s.
- Marketing: GA4, Google Ads tag, Birdeye reviews, Clarity. No Meta pixel.
- **Good prospect:** huge review base, poor site.

**Ruttley Services**: ruttleyservices.com.au
- Site: a dated gradient template. It has a useful postcode checker, "Book online now" and a "Text us" button. It's very heavy (250 requests, ~8.5s).
- Marketing: GA4 and GTM in the HTML, but every request is served first-party, so it's likely server-side tagging or a proxy. 2 active Meta ads.

**GHS Plumbing & Electrical**: generalhomeservices.com.au
- **The website returns a blank page** (HTTP 200, zero bytes, last modified 1 Sep 2026). That's an award-winning, highly rated tradie with no working site for nearly two months. Reviews mention letter-box drops, so their marketing is offline.
- **Hottest prospect on the list.**

---

## Mortgage brokers

| # | Business | Popularity signal | Site | Marketing |
|---|---|---|---|---|
| 1 | **Entourage** | 1,500+ 5-star Google reviews; $5B+ settled | 7 | 7 |
| 2 | **Natloans** (Cheltenham/Hampton) | 750–800+ 5-star Google reviews | 5 | 7 |
| 3 | **AUSUN Finance** | 700+ Google reviews; $6B+ settled, $100M/month | 8 | 3 |
| 4 | **AXTON Finance** | 595 Google reviews | 8 | 7 |
| 5 | **Mel Finance** | 190+ Google reviews; LMG 2025 Platinum | 5 | 7 |
| 6 | **Travis Love / Infinity Group** | #1 RateMyAgent broker in Melbourne (305 reviews, VIC State Top 5 2026) | 2 | 1 |

**Entourage**: entourage.com.au
- Site: premium dark editorial look and the fastest load (~1.3s). The hero says "Your Complete Entourage" and the CTA is a vague "Let's Talk", so it's not obvious it's a broker until the subline.
- Marketing: HubSpot, LinkedIn Insight and GTM are in the HTML, but none of them fired on page load. They're probably held until cookie consent, so they lose data from anyone who ignores the banner. Its positioning is B2B and professional (finance, property and legal under one roof).

**Natloans**: natloans.com.au
- Site: **the nav breaks into a plain bulleted list at tablet width** and pushes the hero headline off-screen. It's multi-product (car, personal, business, home), so its focus is diluted.
- Marketing: Google Ads tag, Meta pixel, Trustindex reviews and an AI chatbot (Chatbase). No active Meta ads found under the name.

**AUSUN Finance**: ausunfinance.com.au
- Site: one of the best looking. Black and gold premium styling, a stats bar ($6B settled, 5,000+ clients), lender logos and a review badge.
- Marketing: **only GA4.** No Google Ads tag, no Meta pixel, no call tracking. It's a strong brand running entirely on organic and referral.
- **Best broker prospect:** paid acquisition would sit on top of a site that already converts.

**AXTON Finance**: axtonfinance.com.au
- Site: the best conversion design of all 12. CTAs are split by intent ("I want to refinance" / "How much can I borrow?"), with a Book button, a review badge and borrowing calculators (LoanTools). Loads in ~3.4s.
- Marketing: GoHighLevel CRM and chat, Google Ads conversion tag, GA4. No Meta pixel.

**Mel Finance**: melfinance.com.au
- Site: **the hero image fails to render** (a flat grey block), and the LMG award badge sits on top of the "Book now" button. The sticky "Free consultation / phone" bar is good.
- Marketing: Meta pixel, CallRail call tracking, GA4, Clarity, Trustindex.

**Travis Love / Infinity Group**: infinity.com.au
- The most-reviewed individual broker in Melbourne on RateMyAgent, but the company site is a webinar funnel for a "Money Mentor" masterclass. It has no phone link and no analytics or ad tags at all, and he has no broker site of his own.

---

## Patterns worth knowing

1. **The big tradies are more sophisticated marketers than the brokers.** Every top tradie runs Google Ads conversion tracking, and most run call tracking and online booking. ServiceTitan plus dynamic call tracking is the standard at the top end.
2. **Review volume is the main weapon in both trades.** Everyone puts their count in the hero, and some put it in the title tag.
3. **Meta is underused.** Only HomeFirst and Ruttley had active Meta ads findable by name. Irwin's, Darebin, AXTON and AUSUN have no Meta pixel at all.
4. **Popularity doesn't mean a good website.** GHS (blank site), Darebin (no hero message), Natloans (broken nav) and Mel Finance (broken hero) all have strong review bases and visible site faults.

## Best prospects (if you want to approach any)

1. **GHS Plumbing & Electrical:** website down, strong reviews.
2. **AUSUN Finance:** premium brand, zero paid tracking.
3. **Darebin:** 888 reviews, the weakest site of the established tradies.
4. **Travis Love:** a top-reviewed broker with no web presence of his own.

## Caveats

- "Your area" is read as Melbourne metro. Tell me a suburb or region and I'll re-run it tighter.
- Tags loaded through GTM after cookie consent, or server-side, can be missed (see Entourage and Ruttley).
- The Meta Ad Library name search only catches ads that mention the brand, so "no ads found" is low-confidence.
- Load times come from one desktop browser load. Google PageSpeed's free quota was exhausted, so there are no Lighthouse scores.
- Review counts are mostly self-reported on each business's own site.

Sources: [ProductReview – VIC plumbers](https://www.productreview.com.au/c/plumbers/l/victoria_au), [ProductReview – VIC electricians](https://www.productreview.com.au/c/electricians/l/victoria_au), [RateMyAgent – Melbourne brokers](https://www.ratemyagent.com.au/finance/melbourne-vic-3000/mortgage-brokers), [Meta Ad Library](https://www.facebook.com/ads/library/), [MFAA 2026 VIC/TAS winners](https://www.mfaa.com.au/news/vic-tas-winners-announced-at-the-2026-mfaa-excellence-awards), and each business's homepage.
