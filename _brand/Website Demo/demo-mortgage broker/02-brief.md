# Harlow Home Loans — Claude Design brief (mortgage broker demo site)

The brokerage, numbers, lenders and reviews are all made up for the demo. They are marked so a real broker's details can be swapped in. Have the broker's compliance contact (usually their aggregator) check the final wording before it goes live.

Words written as <brush>word</brush> get the brush underline described in the Visual system.

## The brokerage (placeholder)

Harlow Home Loans is a small, family-run mortgage broking team in Box Hill, helping buyers and homeowners across Melbourne's eastern suburbs. Every detail below is fictional and also lives in config.js.

| Item | Placeholder value |
| --- | --- |
| Name | Harlow Home Loans (wordmark "Harlow") |
| Who they help | First home buyers, upgraders and next-home buyers, refinancers, property investors, self-employed borrowers |
| Loans | Home loans, refinancing, investment loans, construction loans, bridging loans, self-employed and low-doc loans |
| Office | Box Hill VIC 3128, plus home and video appointments |
| Main area | Box Hill, Blackburn, Doncaster, Balwyn, Camberwell, Surrey Hills, Mont Albert, Mitcham, Ringwood, Glen Waverley, Burwood, Vermont |
| Phone | (03) 5550 2861 (a reserved fictional number) |
| Email | hello@harlowhomeloans.example |
| Hours | Mon to Fri 8:30am to 6pm, Saturday by appointment, evening video calls |
| Lenders | [PLACEHOLDER 30+] banks and non-bank lenders |
| Credit licence | Credit Representative [PLACEHOLDER] of [Aggregator PLACEHOLDER] Pty Ltd, Australian Credit Licence [PLACEHOLDER] |
| Founded | [PLACEHOLDER 2011] |
| Team | Claire Harlow (principal broker), Tom Nguyen (broker, Vietnamese), Priya Shah (broker, Hindi and Gujarati), Mia Chen (client support, Mandarin) |

**The offer:** a free 20-minute "where do I stand?" chat that ends with a clear answer on roughly what you could borrow and your best next step. No obligation, no hard credit check.

**How they're paid (said plainly on the site):** "Our service is usually free to you. Lenders pay us a commission when your loan settles, and we'll show you exactly how much before you choose." [PLACEHOLDER: confirm with the real broker]

**After settlement:** a free loan review every year, so the client isn't left on an old rate.

**Promo bar:** "Fixed rate ending soon? Book a free rate review before it rolls onto a higher variable rate."

## Design decisions

Keep Opendoor's warmth and tactile UI, follow the human-web-design standard wherever they disagree, and make every claim compliant by default. Good broker sites win on trust and clarity; most bury both under long menus, logo walls and SEO copy.

**What the example sites do well, and what we take**

| Site | What works | How we use it |
| --- | --- | --- |
| axtonfinance.com.au | Two intent buttons in the hero, working calculators, annual reviews, a clear credit-licence footer | Hero "what's your next move?" picker, three working calculators, annual review promise, compliance footer |
| intuitivefinance.com.au | Situation links (first home, upsizing, refinancing, self-employed), per-broker booking, FAQ on how brokers are paid | Situation-led navigation, per-broker booking on the team strip, plain "how we're paid" answer |
| ausunfinance.com.au | Proof stats up front, team filterable by language, numbered FAQ | One stats row (placeholders), languages shown on each broker |
| aptwealth.com.au | Confident human headline, short qualifying enquiry form, clear general-advice warning | Short qualifying enquiry form and general information disclaimer |

**Avoid:** 20-plus item mega menus, scrolling lender-logo walls, award-seal grids, unverifiable claims like approval rates, keyword-stuffed copy.

**Conflicts with the Opendoor design.md, resolved**

| Conflict | design.md said | Decision | Why |
| --- | --- | --- | --- |
| Body font | Graphik, fallback Inter | Hanken Grotesk | Inter is on the avoid list, Graphik is paid |
| Hero serif | DM Serif Display | Gloock | Elegant and calm, suits finance; serif on H1 and wordmark only |
| Stats | Invented figures | Visible [PLACEHOLDER] figures | Never invent numbers |
| Stepper | Grey icon tiles | Large numerals + hairline progress rule | Avoids the stock step-card look |
| Testimonials | Video carousel | Review cards | Easier for a real broker to supply |
| Accent | One royal blue | One deep blue, also used for the brush underline | One accent only |

**Compliance guardrails (non-negotiable)**

- No interest rates anywhere unless shown with a comparison rate and the comparison rate warning. Default: show no rates at all.
- No "guaranteed approval", "best rate", "lowest rate" or approval-percentage claims. Use "we compare [PLACEHOLDER 30+] lenders" instead.
- Every calculator result sits beside: "This is an estimate only, based on the figures you entered and the assumptions shown. It isn't a loan offer or credit advice."
- Footer carries the credit representative and licence line, the general information disclaimer, and links to the Credit Guide, Privacy Policy and Complaints page.
- Reviews are marked as illustrative in the demo build; the real version only uses genuine reviews with permission.
- Government schemes (first home guarantee, stamp duty concessions, grants) are mentioned only as "we'll check what you're eligible for", never with dollar amounts.

## Visual system

Warm off-white canvas, brown-tinted neutrals, one deep blue accent and bevelled buttons. All values go in CSS custom properties on `:root`.

**Colours**

| Token | Value | Use |
| --- | --- | --- |
| --canvas | #FBF9F9 | Page background |
| --card | #FFFFFF | Cards, inputs, calculator panels |
| --warm-1 / 2 / 3 | #EDE8E8 / #EFEAE9 / #E6E2E0 | Alternate bands, chips, arrow buttons, sticky pill, slider tracks |
| --ink | #23201D | Headings, calculator results |
| --body | #5E564E | Body copy |
| --brown / --brown-deep | #806D63 / #43352E | Captions, suburbs, disclaimers |
| --accent | #1F45D6 | Buttons, links, slider thumbs, brush underline, promo bar |
| --accent-hover / --accent-active | #1633A6 / #1A3CC4 | Button states |
| --accent-bevel | #1229B8 | Inset bevel on primary buttons |
| --focus | #8AA4F0 | 3px focus ring |
| --success | #5F8944 | Form success and the "pre-approved" tick only |

**Type** (Google Fonts, `font-display: swap`)

- Hero H1 and wordmark only: Gloock, 64px/66px desktop, 40px/44px mobile, tracking -0.02em, fallback Georgia, serif.
- Everything else: Hanken Grotesk, fallback "Helvetica Neue", Arial, sans-serif.
- H2: 48px/50px weight 600, tracking -0.04em (32px/36px mobile). H3: 24px/28px weight 600.
- Body 18px/27px; UI and buttons 16px weight 600; captions and disclaimers 14px (never below 13px).
- Calculator results: Hanken Grotesk 44px weight 600, `font-variant-numeric: tabular-nums`.

**Radii:** buttons and inputs 12px, photo cards 20px, hero frame 24px, chips 8 to 10px, review and calculator cards 16px.

**Bevels**

- Primary button: `box-shadow: 0 0 0 1px var(--accent), inset 0 0 0 1px rgba(255,255,255,.25), inset 0 -4px 0 var(--accent-bevel)`; on press translateY(1px), bevel to -2px.
- Secondary button: `0 0 0 1px rgba(88,64,50,.16), inset 0 0 0 1px rgba(255,255,255,.3), inset 0 -4px 0 rgba(88,64,50,.1)`.
- Hero picker panel: `0 0 0 1px rgba(88,64,50,.16), 0 16px 20px -9px rgba(88,64,50,.19), 0 37px 37px 3px rgba(88,64,50,.12), inset 0 -3px 0 rgba(88,64,50,.1)`.

**Brush underline:** one accent word per H2 (and "move" in the hero H1) gets a tapered, hand-drawn brush stroke in --accent at 28% opacity, drawn as an SVG background on the inline span so it wraps, sitting just below the baseline and clear of the letters, angled -1.5deg. It paints left to right in 700ms when the heading enters view.

**Icons:** 1.5px line icons (Lucide or Phosphor style, inlined SVG), never inside tinted circles. No lender logos.

## Motion

Motion sits at 2 to 3 out of 5: calm and confident. Each section gets a different reveal and background so no two neighbours match.

| Section | Background | Reveal | Live motion |
| --- | --- | --- | --- |
| Hero | Photo frame on canvas | Photo eases from scale 1.04 to 1 over 1.2s; copy fades up 12px, staggered 80ms | Odometer stat rolls once |
| Situations | Canvas | Rows fade in turn, 60ms apart | Row arrow nudges right on hover |
| How it works | --card white band | Soft focus: blur 6px to 0 with fade | Auto-advancing stepper (4.5s per step) |
| Calculators | --warm-2 band | Rise 16px with fade | Results count to new values in 300ms |
| Reviews | Canvas | Cards slide in from 24px right, staggered | Arrow-driven carousel, no autoplay |
| Why Harlow | --warm-1 band | Brush underline paints, list rows fade in turn | None |
| Team | Canvas | Slide from left 24px | Portrait lifts 4px on hover |
| FAQ | --card white band | Plain fade | Accordion height transition 250ms |
| Final CTA + enquiry | --warm-2 band | Rise 16px | Button press bevel |

- Timings 300 to 700ms, easing `cubic-bezier(.2,.7,.2,1)`. Nothing bounces, flips or parallaxes.
- Scroll reveals use IntersectionObserver with a scroll-position fallback; content is never left hidden if JS fails or the page prints.
- Anything that plays on its own (stepper, odometer, auto-typing, hero video) pauses on hover, keyboard focus, off screen and hidden tab, and shows its full content while paused.
- `prefers-reduced-motion: reduce` turns off movement, shows end states and stops the stepper auto-advance.

## Imagery (made with Higgsfield)

All 12 photos are in the `images` folder (run download-images.ps1 first). Serve as WebP with `loading="lazy"` below the fold. The hero gets a soft dark gradient on its top 40% (rgba(35,32,29,.45) to transparent) for readable white text.

| File | Where it goes | Alt text |
| --- | --- | --- |
| hero.png | Home hero (16:9) | A couple playing with their toddler in the living room of their new home |
| why-harlow.png | Why Harlow / About / Self-employed (4:3) | A Harlow broker talking through loan options with a couple at their dining table |
| situation-first-home.png | Situation: First home (4:3) | First home buyers holding their new keys |
| situation-refinance.png | Situation: Refinance (4:3) | A homeowner relaxed after reviewing his home loan |
| situation-next-home.png | Situation: Next home (4:3) | A family exploring the backyard of their next home |
| situation-investing.png | Situation: Investing (4:3) | A woman looking at new townhouses as an investment |
| step-1.png | Stepper step 1 (4:5) | A woman on a first call with her broker |
| step-2.png | Stepper step 2 (4:5) | A broker comparing loan options at his desk |
| step-3.png | Stepper step 3 (4:5) | A couple reading good news on their phone |
| step-4.png | Stepper step 4 (4:5) | A couple carrying boxes into their new home |
| team.png | Team strip (3:2) | The Harlow Home Loans team outside their Box Hill office |
| area.png | Local area band (16:9) | A tree-lined street of period homes at golden hour |

## Homepage, section by section

### 1. Promo bar

40px, --accent background, white 14px centred: "Fixed rate ending soon? Book a free rate review before it rolls onto a higher variable rate." A small white circular arrow opens the enquiry drawer with "Refinance" selected; × dismisses it for the session.

### 2. Header (72px, canvas)

- Left: wordmark "Harlow" in Gloock 24px, with "Home Loans" in 12px Hanken Grotesk caps beside it.
- Nav (15px, weight 600): Buying, Refinancing, Investing, Calculators, About. Buying opens a small two-column panel: First home, Next home, Building, Self-employed.
- Right: phone "(03) 5550 2861" as a text link, then primary button "Book a free chat" (44px).
- After the hero, the header gains a 1px warm border and a compact --warm-1 pill "What are you planning?" appears in the centre.
- Mobile: wordmark + menu button; sticky bottom bar with "Call" (secondary) and "Book a free chat" (primary), safe-area padded.

### 3. Hero

Full-width photo frame (hero.png), inset 12px, 24px radius, 640px desktop / 580px mobile. White copy centred over the top half:

- H1 (Gloock): "Your next <brush>move</brush>, made simple."
- Sub (18px, two lines): "Mortgage brokers for Melbourne's east. / We compare [PLACEHOLDER 30+] lenders and do the legwork, usually at no cost to you."
- **Picker panel** (600px wide, white, picker bevel, 12px radius): four segmented chips, "Buy my first home", "Buy my next home", "Refinance", "Invest"; a second row with "Roughly how much? $" (formatted as you type) and "Suburb", and a 48px blue square arrow button. The money label reads "Property price" for buying and investing, "Current loan balance" for refinancing.
- Microcopy 14px white/80%: "Takes 2 minutes │ No credit check │ Your details stay private".
- Stats row along the bottom edge, numbers 32px/600, captions 14px: "4.9 ★ from [PLACEHOLDER 280] Google reviews" · odometer "$[PLACEHOLDER 640]m in home loans settled" · "[PLACEHOLDER 30+] lenders compared".

### 4. Situations

H2 "Where are you <brush>at</brush>?" across the full width, with "Every situation needs a different loan. Start with yours." Two columns: a hairline-separated list of five link rows (20px/600 title, one plain line, arrow) on the left; a 4:3 photo on the right that crossfades to match the hovered or focused row.

- **Buying my first home** — "Deposits, schemes, pre-approval, and what to do on auction day." (situation-first-home.png)
- **Buying my next home** — "Buying before you sell, bridging finance and moving your equity." (situation-next-home.png)
- **Refinancing** — "Check your rate, cut fees, or free up equity for a renovation." (situation-refinance.png)
- **Investing** — "Structuring a loan for your first or next investment property." (situation-investing.png)
- **Self-employed** — "Lenders who understand business income, even with a short trading history." (why-harlow.png)

### 5. How it works (stepper)

Left: the active step's photo (step-1 to step-4) in a 20px frame, with a frosted overlay card (white 90%, blur 12px, 12px radius) playing a small demo. Right: H2 "How we <brush>work</brush> with you", then four rows separated by 1px --warm-3 rules: a large numeral (40px, --brown at 60%), an 18px/600 title, and when active the body line plus a 2px accent progress line filling in 4.5s.

1. **A free 20-minute chat** — "Phone, video or our Box Hill office. We work out where you stand and what's possible." Overlay: time chips, "Tue · 6:30pm · Video call" being selected with a tick.
2. **We compare lenders for you** — "We shortlist loans that fit your situation and show you the trade-offs side by side." Overlay: rows "Lender A / B / C" that re-order, with tags like "Offset account", "Fits a 10% deposit", "Low fees" (no rates).
3. **Pre-approval in hand** — "We handle the application and keep you posted, so you can bid with confidence." Overlay: card "Pre-approval received" with a --success tick and "Up to $[PLACEHOLDER]".
4. **Settled, then reviewed every year** — "We line up settlement with your solicitor, then check your loan every year." Overlay: SMS "Settled! The keys are yours.", then chip "Next loan review: Oct 2027".

Mobile: the photo sits above the list and changes with the step.

### 6. Calculators

H2 "Run the <brush>numbers</brush> first" with "Quick estimates to get a feel for it. We'll confirm the real figures in your free chat." A --card panel with three tabs: Borrowing power, Repayments, Refinance check. Inputs left, large result right, disclaimer under the result, and a "Talk this through with a broker" button that opens the enquiry drawer pre-filled with the figures.

### 7. Reviews

H2 "Clients who've <brush>made</brush> their move" left; right: "4.9 average on Google [PLACEHOLDER]" and two 40px --warm-1 arrow buttons. Scroll-snap row of white review cards from reviews.json, the first 520px wide and the rest 340px so the next one peeks. Each card: five stars, quote (18px ink), name (16px/600), suburb and situation (14px brown), "Google review" label and date. Small "Illustrative reviews" note in the section footer.

### 8. Why Harlow

why-harlow.png on the left (4:3); right: H2 "Advice you can <brush>trust</brush>" and an editorial numbered list, no boxes (14px brown numeral, 18px/600 heading, two lines of body):

1. **Your interests come first, by law.** Brokers must act in your best interests, and we'll show you why we recommend a loan.
2. **We show you how we're paid.** Usually the lender pays us. You'll see the amount before you choose.
3. **A shortlist, not a sales pitch.** We compare [PLACEHOLDER 30+] lenders and explain the trade-offs side by side.
4. **After hours when you need it.** Evening video calls and Saturday appointments.
5. **We don't disappear after settlement.** A free loan review every year.
6. **In your language.** Appointments in English, Mandarin, Hindi, Gujarati and Vietnamese.

### 9. Team strip

team.png on top (3:2, 20px radius), then four simple rows: name (18px/600), role, languages (14px brown) and a "Book with Claire" style link that opens the enquiry drawer with that broker pre-selected.

### 10. Local band

area.png as a wide 20px banner with H2 "Local to Melbourne's <brush>east</brush>" and "Meet at our Box Hill office, at your kitchen table, or on video." Suburb chips below link to the suburb pages.

### 11. FAQ

H2 "Questions we <brush>hear</brush> a lot", accordion, one open at a time:

- **What does a mortgage broker cost?** Usually nothing. Lenders pay us a commission when your loan settles, and we'll show you how much before you choose. [PLACEHOLDER: confirm fee policy]
- **How much can I borrow?** It depends on your income, expenses, debts, deposit and each lender's rules. Use the calculator for a rough idea, then we'll check it properly.
- **Will talking to you affect my credit score?** No. A first chat and estimate don't involve a credit check.
- **What deposit do I need?** Often 5 to 20% of the price, depending on the lender and any scheme you qualify for. We'll check what applies to you.
- **When should I refinance?** When a fixed rate is ending, your rate hasn't been reviewed in a while, or you want to access equity. We'll tell you if it isn't worth it.
- **How long does pre-approval take?** Often a few days to two weeks, depending on the lender and your paperwork.
- **Do you work with self-employed people?** Yes, including sole traders and new businesses.

### 12. Final call to action + enquiry

H2 "Let's work out your next <brush>step</brush>" with "Book a free 20-minute chat. We'll call you back within [PLACEHOLDER 1 business day]." Left: the enquiry form. Right: "Rather talk now?", the big phone number, hours, office address and a map placeholder.

### 13. Footer (--warm-1)

Four columns: wordmark + one-line description; Buying links; Refinancing and investing links; Contact. Then the compliance block in 13px --brown:

> Harlow Home Loans Pty Ltd ABN [PLACEHOLDER] (Credit Representative [PLACEHOLDER]) is authorised under Australian Credit Licence [PLACEHOLDER] held by [Aggregator PLACEHOLDER] Pty Ltd. The information on this website is general only and doesn't take into account your objectives, financial situation or needs. Your full financial situation will need to be reviewed before any loan offer. Calculator results are estimates only.

Bottom row: Credit Guide, Privacy Policy, Complaints, Terms, "© 2026 Harlow Home Loans".

## Other pages and templates

Build these after the homepage, reusing its components. Every page ends with the enquiry form, compliance block and footer.

| Page | URL | What's on it |
| --- | --- | --- |
| Situation template | /buying/first-home | Photo + H1 "Buying your first home, step by step", what to expect, timeline from savings to settlement, "we'll check which schemes you qualify for", borrowing calculator, 3 matching reviews, FAQ, enquiry pre-set to First home |
| Situation pages | /buying/next-home, /refinancing, /investing, /self-employed, /building | Same template with their own photo, copy and calculator |
| Calculators hub | /calculators | All three calculators full width, assumptions spelled out, disclaimer |
| Refinance health check | /refinancing/health-check | 5-question flow (lender, balance, rate, fixed or variable, when it ends) ending in "Worth a review" / "Looks OK for now" plus booking |
| Broker profile template | /team/claire-harlow | Portrait, short story, specialities, languages, credentials, reviews that mention them, "Book with Claire" |
| Team | /team | team.png, the four broker rows, support team |
| Suburb template | /areas/doncaster | H1 "Mortgage broker in Doncaster", local paragraph, nearby suburbs, office and home visit options, reviews from that area |
| Reviews | /reviews | All review cards in a grid with filters (First home, Refinance, Investing, Self-employed) |
| Guides | /guides | Three placeholder articles: "First home buyer checklist", "What happens when your fixed rate ends", "How lenders look at self-employed income" |
| Book | /book | The enquiry form on its own, with broker and time picker |
| Thanks | /thanks | Confirmation with reference number, what happens next, document checklist |
| Credit Guide, Privacy, Complaints, Terms | /credit-guide etc. | Plain text placeholder pages, labelled to be replaced by the aggregator's versions |

Generate the six situation pages, one profile per team member, and four suburb pages (Doncaster, Box Hill, Glen Waverley, Camberwell).

## Interactions, calculators and working forms

**Enquiry and booking form** (three short steps in a drawer or inline)

1. **Your situation:** First home, Next home, Refinance, Invest, Self-employed, Something else (large chips).
2. **The numbers (all optional):** property price or loan balance, deposit or equity, household income, suburb. Money fields format as you type.
3. **Your details:** name, mobile (04XX XXX XXX), email, best way to reach you, preferred time (chips for the next five weekdays with morning, lunchtime and evening slots, plus Saturday), broker preference (Any, Claire, Tom, Priya), language, and a required consent box: "I'm happy for Harlow Home Loans to contact me about my enquiry. I've read the Privacy Policy."

- Progress line shows step 1 of 3; Back keeps answers; validation on blur and submit with plain-English errors and `aria-live` announcements.
- Submit: pressed button with spinner ~900ms, then a success panel: --success tick, "Thanks, [Name]. [Broker] will call you on [day, time].", reference (HL- + 5 digits), a working "Add to calendar" button that downloads an .ics file, and "What to have ready": payslips, ID, bank statements, current loan statement.
- Data stays in memory and POSTs to `CONFIG.formEndpoint` if set; otherwise logs to the console.
- Hero picker, header pill, situation rows, calculator buttons, team links and promo bar all open the drawer pre-filled. Desktop: right drawer 520px; mobile: full-height sheet. Esc closes, focus trapped and returned.

**Calculators** (assumptions in CONFIG.calculator, printed under each result)

| Calculator | Inputs | Output | Method |
| --- | --- | --- | --- |
| Borrowing power | Applicants (1 or 2), gross income each, other income, dependants, monthly living expenses, monthly debt repayments, credit card limits | "You could borrow around $X" plus a ±10% range | After-tax income from CONFIG tax brackets; expenses = larger of entered or CONFIG minimum per household; 3% of card limits counted as a repayment; loan sized so repayments at (example rate + buffer) over 30 years fit the surplus |
| Repayments | Loan amount, interest rate (pre-filled with CONFIG example rate, labelled "example"), term, frequency, P&I or interest only | Repayment per period, total interest, small SVG balance line | Standard amortisation |
| Refinance check | Balance, current rate, years left, a new rate to compare, switching costs | Change per month, break-even in months, change in total interest | Two amortisation runs; "Not worth switching" when break-even exceeds 24 months |

- Sliders and number inputs stay in sync; results animate in 300ms (instant with reduced motion).
- Disclaimer under every result. The example rate shows as "Example rate only, not a current offer".

**Other interactions**

- Every phone number is a `tel:` link; mobile call bar appears after 300px and hides while the drawer is open.
- Situations list: hover, focus or tap swaps the photo; on mobile each row shows its own photo.
- Reviews carousel: arrows, swipe, keyboard; arrows disable at the ends.
- Stepper rows are buttons with arrow-key movement and `aria-expanded`.
- FAQ uses native `<details>`/`<summary>` with the height transition.
- Hit areas at least 44px; visible 3px --focus ring on every focusable element.

## Making it reusable for other brokers

config.js and the CSS variables drive every page, so a new broker's demo is a swap of config, accent colour, photos and compliance line.

- Every mention of the business, team, phone, suburbs, stats and compliance text reads from CONFIG, never hard-coded.
- Turning a situation off in `situations` removes its row, nav link, page and form chip.
- The footer compliance block is built from `CONFIG.compliance`.
- Brand colour: change the four `--accent` tokens. Photos keep the fixed file names above.
- Reviews come from reviews.json and filter automatically on situation and broker pages.

## Build, compliance and QA checklist

**Build**

- [ ] Semantic HTML, modern CSS, vanilla JS, no framework
- [ ] Breakpoints 390, 768, 1024, 1440px; no sideways scroll
- [ ] Lighthouse 90+ performance and accessibility on mobile
- [ ] Images in WebP with width/height set; hero preloaded
- [ ] FinancialService / LocalBusiness schema with placeholder details

**Compliance**

- [ ] No interest rates shown as offers; example rate labelled as an example
- [ ] No "best rate", "guaranteed" or approval-percentage claims
- [ ] Disclaimer directly under every calculator result
- [ ] Footer has licence line, general information disclaimer, Credit Guide, Privacy and Complaints links
- [ ] "How we're paid" appears in the FAQ and Why Harlow
- [ ] Consent checkbox required on every form
- [ ] Demo reviews marked as illustrative

**Human-web-design review**

- [ ] No avoided font anywhere, including inputs and calculator numbers
- [ ] Serif only on the hero H1 and wordmark
- [ ] No two neighbouring sections share a background or reveal style
- [ ] Brush underline on one word per H2, clear of the letters, wrapping correctly
- [ ] Auto-playing elements pause on hover, focus, off screen and hidden tab
- [ ] Reduced motion shows every end state; nothing hidden with JS off or when printing
- [ ] No STEP badges, icon-in-circle cards, lender logo walls, breadcrumbs or hero eyebrow
- [ ] Light page throughout, no dark full-width bands
- [ ] Plain English, results-led copy; every figure marked [PLACEHOLDER] or sourced

**Working demo**

- [ ] Enquiry completes all three steps, shows the reference and downloads a working .ics
- [ ] All entry points pre-fill the form
- [ ] All three calculators give sensible results and update live
- [ ] Every phone link dials; mobile call bar shows after scroll
- [ ] Every nav and footer link reaches a real page; no console errors
