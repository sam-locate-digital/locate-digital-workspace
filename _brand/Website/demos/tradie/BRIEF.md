> **Note:** this is the original brief, kept for reference. Several things changed during the design (new business name, no fixed-price angle, no pricing on service pages, removed hero chips and stepper overlays). **HANDOFF.md is the current source of truth.**

# Hartley & Co. — Claude Design brief (tradie demo site)

**Opening prompt to paste:**

```markdown
Act as an award-winning web designer with a $50,000 budget. Build a full, working demo website for a fictional Melbourne eastern-suburbs plumbing and electrical business called Hartley & Co. It will be shown to real tradies as a sales demo, so it must feel finished and real: working booking form, click-to-call, mobile call bar, and smooth but restrained motion.

Use the attached brief as the single source of truth for brand, copy, layout, motion and imagery. The look borrows Opendoor's warm, tactile feel (soft off-white canvas, brown-tinted neutrals, one royal-blue accent, bevelled "pressable" buttons) but the content is a local trades business.

Rules that override anything else: no Inter, Poppins, DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk, Figtree, Fraunces or Instrument Serif anywhere. No stock "STEP 1" cards or generic icon-in-circle cards. No dark full-width bands. Every number marked [PLACEHOLDER] stays visibly swappable. Respect prefers-reduced-motion. Mobile first, up to 1440px.

Start with the homepage, then build the page templates in the order listed.
```

The placeholder business, numbers and reviews are all made up for the demo. They are marked so you can swap in a real tradie's details before showing them their own version.

## The business (placeholder)

Hartley & Co. is a family-run plumbing and electrical business based in Blackburn, serving homeowners and landlords across Melbourne's eastern suburbs. Every detail below is fictional.

| Item | Placeholder value |
| --- | --- |
| Name | Hartley & Co. (wordmark), full name Hartley & Co. Plumbing + Electrical |
| Trades | Plumbing, gas fitting, hot water, drains, electrical, switchboards, lighting, smoke alarms |
| Base | Blackburn VIC 3130 |
| Service area | Box Hill, Blackburn, Mitcham, Nunawading, Vermont, Forest Hill, Ringwood, Croydon, Doncaster, Templestowe, Balwyn, Camberwell, Surrey Hills, Glen Waverley, Burwood, Mont Albert |
| Phone | (03) 5550 4127 (a reserved fictional number) |
| Email | jobs@hartleyandco.example |
| Hours | Mon to Fri 7am to 5pm, emergency call-outs 24/7 |
| Licences | Plumbing licence [PLACEHOLDER], REC [PLACEHOLDER], ABN [PLACEHOLDER] |
| Customers | Homeowners first; landlords and property managers second |
| Founded | [PLACEHOLDER: 1998] |

**The offer (replaces Opendoor's cash offer):** a fixed price before any work starts. The price is agreed on the spot, in writing, so the bill never grows. Supporting promises: no weekday call-out fee when the job goes ahead, and a text when the tradie is 30 minutes away.

**Landlord angle:** one booking covers plumbing and electrical, the tenant is contacted directly, and invoices and compliance photos go straight to the landlord or property manager.

**Promo bar offer:** "Summer's coming: free switchboard safety check with any electrical job this month."

## Design decisions

Keep Opendoor's warmth and tactile UI, but follow the human-web-design standard wherever the two disagree. The competitors (O'Shea, Ruttley) have strong proof buried in long, cluttered pages; this site wins by being calm, fast to act on and obviously local.

| Conflict | design.md said | Decision | Why |
| --- | --- | --- | --- |
| Body font | Graphik, fallback Inter | Schibsted Grotesk | Inter is on the avoid list, and Graphik is paid so Inter would be what shows |
| Hero serif | DM Serif Display | Young Serif | Less common, sturdier, suits a trade business; still serif on the H1 only |
| Stats | Invented figures (311,337) | Visible [PLACEHOLDER] figures | Never invent numbers; each swaps for the real tradie's data |
| Stepper | Grey icon tiles | Large numerals + hairline progress rule | Avoids the stock step-card look |
| Testimonials | Video carousel | Review cards (your choice) | Easier for a real tradie to supply; reads like Google reviews |
| Hero eyebrow | None | None | Headline starts the page |
| Accent | One royal blue | One deep blue, used for the brush underline too | One accent only, no emergency red |

**Competitor lessons used:** O'Shea's guarantee and longevity story is borrowed as an editorial "why us" list. Ruttley's postcode check and "we text when we're 30 minutes away" become the hero suburb check and the stepper's SMS demo. Their 20-item dropdown menus are replaced with a two-column Services mega panel.

## Visual system

Warm off-white canvas, brown-tinted neutrals, one deep blue accent, and bevelled buttons that look pressable. All values below go in CSS custom properties on `:root` so a new tradie's brand is a one-file change.

**Colours**

| Token | Value | Use |
| --- | --- | --- |
| --canvas | #FBF9F9 | Page background |
| --card | #FFFFFF | Cards, inputs, review cards |
| --warm-1 / 2 / 3 | #EDE8E8 / #EFEAE9 / #E6E2E0 | Alternate section bands, chips, arrow buttons, sticky search pill |
| --ink | #23201D | Headings |
| --body | #5E564E | Body copy |
| --brown / --brown-deep | #806D63 / #43352E | Captions, suburbs, small labels |
| --accent | #1F45D6 | Buttons, links, brush underline, promo bar |
| --accent-hover / --accent-active | #1633A6 / #1A3CC4 | Button states |
| --accent-bevel | #1229B8 | Inset bevel on primary buttons |
| --focus | #8AA4F0 | 3px focus ring |
| --success | #5F8944 | Form success, "tradie on the way" tick only |

**Type** (Google Fonts, `font-display: swap`)

- Hero H1 only: Young Serif, 64px/66px desktop, 40px/44px mobile, tracking -0.03em, fallback Georgia, serif.
- Everything else: Schibsted Grotesk, fallback "Helvetica Neue", Arial, sans-serif.
- H2: 48px/50px weight 600, tracking -0.04em (32px/36px mobile). H3: 24px/28px weight 600, tracking -0.02em.
- Body 18px/26px tracking -0.01em; UI and buttons 16px weight 600; captions 14px.
- Alternatives if the client wants to compare: Gloock + Hanken Grotesk, or Libre Caslon Display + Public Sans.

**Radii:** buttons and inputs 12px, photo cards 20px, hero frame 24px, chips 8 to 10px, review cards 16px.

**Bevels**

- Primary button: `box-shadow: 0 0 0 1px var(--accent), inset 0 0 0 1px rgba(255,255,255,.25), inset 0 -4px 0 var(--accent-bevel)`; on press, translateY(1px) and bevel drops to -2px.
- Secondary button: `0 0 0 1px rgba(88,64,50,.16), inset 0 0 0 1px rgba(255,255,255,.3), inset 0 -4px 0 rgba(88,64,50,.1)`.
- Hero search field: `0 0 0 1px rgba(88,64,50,.16), 0 16px 20px -9px rgba(88,64,50,.19), 0 37px 37px 3px rgba(88,64,50,.12), inset 0 -3px 0 rgba(88,64,50,.1)`.

**Brush underline:** one accent word per H2 (and "price" in the hero H1) gets a tapered, hand-drawn brush stroke in --accent at 28% opacity. Draw it as an SVG background-image on the inline span so it wraps across lines, sitting just below the baseline and clear of the letters, slightly angled (-1.5deg). It paints left to right (background-size 0% → 100%, 700ms ease-out) when the heading enters view.

In this brief, a word written as `<brush>word</brush>` marks the word that gets the brush underline.

**Icons:** simple 1.5px line icons (Lucide or Phosphor style, inlined as SVG), never inside tinted circles.

## Motion

Motion sits at 2 to 3 out of 5: noticeable on first look, never showing off. Each section gets a different reveal and background so no two neighbours match.

| Section | Background | Reveal | Live motion |
| --- | --- | --- | --- |
| Hero | Photo frame on canvas | Photo eases from scale 1.04 to 1 over 1.2s; copy fades up 12px, staggered 80ms | Odometer stat rolls once, digit by digit |
| Reviews | Canvas | Cards slide in from 24px right, staggered | Arrow-driven carousel, no autoplay |
| How it works | --card white band | Soft focus: blur 6px to 0 with fade | Auto-advancing stepper (4.5s per step) |
| Services | --warm-2 band | Rise 16px with fade | Photo zooms 1.03 on hover |
| Why us | Canvas | Brush underline paints, list rows fade in turn | None |
| Service areas | --warm-1 band | Scale 0.98 to 1 | Suburb chips highlight on hover |
| Team | Canvas | Slide from left 24px | None |
| FAQ | --card white band | Plain fade | Accordion opens with height transition 250ms |
| Final CTA + form | --warm-2 band | Rise 16px | Button press bevel |

**Rules**

- Timings 300 to 700ms, easing `cubic-bezier(.2,.7,.2,1)`. Nothing bounces, flips or parallaxes.
- Scroll reveals use IntersectionObserver with a scroll-position fallback, and content is never left hidden: if JS fails or the page prints, everything shows.
- Anything that plays on its own (stepper, odometer, auto-typing) pauses on hover and keyboard focus, when off screen and when the tab is hidden. While paused on hover, show the full content rather than a half-typed state. Clicking a step jumps there and carries on.
- `prefers-reduced-motion: reduce` turns off all movement, shows end states (underlines drawn, numbers final, step 1 open) and stops the stepper auto-advance.

## Imagery (made with Higgsfield)

Ten photos were generated for this demo. Serve them as WebP with `loading="lazy"` below the fold, and give each a plain alt text.

| # | Where it goes | Image | Alt text |
| --- | --- | --- | --- |
| 0 | Home hero (16:9) | Plumber at kitchen sink with homeowner | A Hartley plumber fixing a kitchen sink while the homeowner chats |
| 1 | Services: Electrical (4:3) | Electrician at switchboard | Electrician working on a home switchboard |
| 2 | Services: Hot water (4:3) | Hot water install on brick wall | New continuous-flow hot water unit being installed |
| 3 | Services: Bathrooms (4:3) | Finished bathroom | Renovated bathroom with terrazzo floor and green tiles |
| 4 | Stepper step 1 (4:5) | Homeowner on phone, dripping tap | Homeowner booking a plumber on her phone |
| 5 | Stepper step 2 (4:5) | Work ute outside weatherboard | Work ute parked outside an Edwardian home |
| 6 | Stepper step 3 (4:5) | Quote shown on tablet at front door | Tradie showing a fixed-price quote to a couple |
| 7 | Stepper step 4 (4:5) | Tradie cleaning up after the job | Tradie wiping down the bench after finishing |
| 8 | Team strip / About (3:2) | Team beside the van | The Hartley & Co. team beside their van |
| 9 | Service areas (16:9) | Eastern suburbs rooftops | Rooftops of Melbourne's eastern suburbs at golden hour |

The hero gets a soft dark gradient on its top 40% (rgba(35,32,29,.45) to transparent) so white text stays readable.

## Homepage, section by section

The homepage runs top to bottom in this order. Copy is final placeholder copy; brackets mark what a real tradie swaps in.

### 1. Promo bar

40px, --accent background, white 14px centred: "Summer's coming: free switchboard safety check with any electrical job this month." Small white circular arrow button links to the booking form; × on the right dismisses it for the session.

### 2. Header (72px, canvas)

- Left: wordmark "Hartley & Co." in Young Serif 22px (the one other place the serif appears, as the logo).
- Centre-right: Plumbing, Electrical, Landlords, Reviews, About (15px, weight 600). Plumbing and Electrical open one shared mega panel with two columns of services and a photo.
- Right: phone "(03) 5550 4127" as a text link with a phone icon, then a primary "Book a job" button (44px).
- After scrolling past the hero, the header gains a 1px warm border and a compact --warm-1 search pill "What needs fixing?" appears in the centre.
- Mobile: wordmark + menu button; a sticky bottom bar with two equal buttons, "Call now" (secondary) and "Book a job" (primary), safe-area padded.

### 3. Hero

Full-width photo frame (image 0), inset 12px, 24px radius, 640px tall desktop / 560px mobile. White copy centred over the top half:

- H1 (Young Serif): "Fixed right. Fixed <brush>price</brush>."
- Sub (18px, two lines): "Plumbers and electricians for Melbourne's east. / You'll know the price before we pick up a tool."
- **Job search bar** (560px wide, 60px tall, white, search-field bevel): a wrench icon, the field "What needs fixing? e.g. hot water, blocked drain", a divider, a suburb field "Suburb" with a location pin, and a 44px blue square button with an arrow. Typing in the job field suggests: Blocked drain, Hot water not working, Leaking tap or toilet, Gas heater service, Power out or tripping, New lights or power points, Switchboard upgrade, Smoke alarms.
- Under the bar, quick chips (white at 16% with blur): Hot water · Blocked drain · Power out · Leaking tap.
- Microcopy 14px white/80%: "Licensed plumbers and electricians │ Fixed price before we start".
- Stats row along the photo's bottom edge, three columns, numbers 32px/600, captions 14px: "4.9 ★ from [PLACEHOLDER 612] Google reviews" · odometer "[PLACEHOLDER 18,400] jobs done in the east" · "Same day for most call-outs".

### 4. Reviews carousel

Header row: H2 "Neighbours who've <brush>already</brush> called us" on the left; on the right a 14px "4.9 average on Google [PLACEHOLDER]" and two 40px --warm-1 square arrow buttons. Scroll-snap row of white review cards, the first 520px wide, the rest 340px so the next one peeks. Each card: five small stars, the quote in 18px ink, then name (16px/600), suburb and job (14px brown), and a small "Google review" label with date.

| Name | Suburb | Job | Quote |
| --- | --- | --- | --- |
| Priya S. | Box Hill | Hot water replacement | "Hot water died on a Sunday. They texted the price before coming out, had a new unit in by lunch, and the price didn't move." |
| Mark & Jen T. | Blackburn | Switchboard upgrade | "Our 1960s board was a worry. They explained it in plain English, did it in a day and left the hallway cleaner than they found it." |
| Daniel O. | Ringwood | Blocked drain | "Got a text when they were 30 minutes away, which never happens. Drain cleared, camera footage sent to me after." |
| Helen W. | Camberwell | Bathroom reno plumbing | "Plumbing and electrical in one booking for our bathroom. One quote, one invoice, no chasing two trades." |
| Raj K., landlord | Doncaster | Smoke alarms + leak | "I manage four rentals. They deal with the tenant directly and send me photos and the invoice. Saves me hours." |
| Sophie L. | Mitcham | Gas heater service | "Booked online at 9pm, confirmed by text the next morning. Friendly, on time, fixed price." |

### 5. How it works (stepper)

Two columns. Left: the photo for the active step (images 4 to 7) in a 20px-radius frame, with a frosted overlay card at the bottom (white 90%, backdrop blur 12px, 12px radius) that plays a small demo per step. Right: H2 "How a job <brush>works</brush>" then four rows separated by 1px --warm-3 rules. Each row: a large numeral (40px, --brown at 60%), an 18px/600 title, and when active, the body line plus a 2px accent progress line that fills across the rule in 4.5s.

1. **Tell us what's wrong** — "Book online or call. Tell us the problem and when suits." Overlay: a booking field auto-types "Hot water's gone cold…", then shows "Thursday · 8–10am" selected.
2. **We confirm by text** — "You'll get a booking text, and another when we're 30 minutes away." Overlay: two SMS bubbles appear in turn: "Hi Sarah, Jake's booked for Thu 8–10am." then "Jake is 30 mins away."
3. **Fixed price before we start** — "We look, explain the options and give you one price in writing. Nothing starts until you say yes." Overlay: a quote card "Replace hot water unit — $[PLACEHOLDER] fixed" with an Approve button that ticks green.
4. **Fixed, cleaned up, explained** — "We clean up, walk you through what we did and send photos with the invoice." Overlay: SMS "All done. Photos and invoice attached." with two small photo thumbnails.

Mobile: the photo sits above the list and changes with the step.

### 6. Services

H2 "Plumbing and electrical, <brush>one</brush> call" spanning the full content width, with a line under it: "One booking covers both trades, so jobs that need a plumber and an electrician get done in one visit." Below, a two-column editorial list rather than cards: a Plumbing column and an Electrical column, each with a 4:3 photo (images 2 and 1) above a hairline-separated list of services. Each row is a link with the service name (18px/600), a one-line plain description and an arrow that nudges right on hover.

- Plumbing: Hot water repairs and replacement · Blocked drains and CCTV inspection · Leaking taps, toilets and showers · Gas fitting and heater servicing · Burst pipes and emergencies · Bathroom and kitchen renovations.
- Electrical: Power faults and emergencies · Switchboard upgrades · Lights, power points and fans · Smoke alarms and safety checks · Split system installs · Appliance installs.

A wide image 3 strip under the columns links to "Bathroom and kitchen renovations".

### 7. Why Hartley

H2 "Work we put our <brush>name</brush> on". An editorial numbered list in two columns, no boxes; each item a 14px brown numeral, an 18px/600 heading, two lines of body.

1. **A fixed price, in writing, before we start.** The price you approve is the price you pay.
2. **On time, or we tell you first.** A text when we're booked and another when we're 30 minutes away.
3. **[PLACEHOLDER 10]-year workmanship guarantee.** If our work fails, we come back and fix it.
4. **Licensed, insured, local.** Every plumber and electrician is licensed and based in the east.
5. **We leave it cleaner.** Drop sheets down, mess gone, a walk-through before we leave.
6. **Built for landlords too.** We deal with tenants directly and send photos and invoices to you.

### 8. Service areas

Image 9 as a wide 20px-radius banner, with H2 "Local to Melbourne's <brush>east</brush>" beside it and a suburb checker: an input "Check your suburb" and button. A match shows "Yes, we're in [Suburb] most days." in --success; no match shows "We may still come out. Call us on (03) 5550 4127." Below, the suburbs as --card chips, each linking to its suburb page.

### 9. Team strip

Image 8 left (3:2), right side: H3 "A family business since [PLACEHOLDER 1998]", two lines: "Started in a Blackburn garage, still run from Blackburn. The person who quotes your job is the one who does it." Secondary button "Meet the team".

### 10. FAQ

H2 "Questions people <brush>ask</brush> us", accordion of six, one open at a time:

- **Do you charge a call-out fee?** No weekday call-out fee if you go ahead with the job. After-hours call-outs have a fixed fee, waived if the job goes ahead [PLACEHOLDER].
- **Will the price change once you start?** No. You approve a fixed price in writing first. If we find something else, we stop and ask before doing more.
- **Can you do plumbing and electrical in one visit?** Yes. One booking, one quote, one invoice.
- **Do you work with landlords and property managers?** Yes. We contact tenants directly and send you photos, invoices and compliance certificates.
- **Are you licensed?** Yes, every tradesperson is licensed and insured. Licence numbers are in the footer.
- **Do you do emergencies?** Yes, 24/7 for burst pipes, gas leaks, no hot water and power faults. Call (03) 5550 4127.

### 11. Final call to action + booking form

H2 "Tell us what needs <brush>fixing</brush>" with a short line: "We'll text you a time within [PLACEHOLDER 1 business hour]." Left: the booking form (see Interactions). Right: "Rather talk?" with the big phone number, hours, and an emergency line.

### 12. Footer (--warm-1)

Four columns: wordmark + one-line description; Plumbing links; Electrical links; Contact (phone, email, hours, Blackburn address [PLACEHOLDER]). Bottom row: licence numbers [PLACEHOLDER], ABN [PLACEHOLDER], Privacy, Terms, "© 2026 Hartley & Co."

## Other pages and templates

Build these after the homepage, reusing its components. Each page ends with the same booking form and footer.

| Page | URL | What's on it |
| --- | --- | --- |
| Plumbing hub | /plumbing | Short hero (no photo frame, H1 in Schibsted 56px), the plumbing service list from the homepage expanded with prices "from $[PLACEHOLDER]", reviews filtered to plumbing, FAQ |
| Electrical hub | /electrical | Same layout as Plumbing, electrical content |
| Service template | /plumbing/hot-water | Photo + H1 "Hot water fixed or replaced, often same day", signs you need us, what's included, fixed-price note, 3 matching reviews, related services, form pre-filled with "Hot water" |
| Suburb template | /areas/box-hill | H1 "Plumber and electrician in Box Hill", one local paragraph, jobs we often do there, nearby suburbs as chips, reviews from that suburb, form pre-filled with the suburb |
| Landlords | /landlords | Results-led page for property managers: tenant contact, photo reports, compliance certificates, one invoice per property, smoke alarm and gas safety checks, a "Add a property" form variant |
| Reviews | /reviews | All review cards in a grid with filter chips (Plumbing, Electrical, suburb) |
| About | /about | Team photo (image 8), short story, the team as four simple name + role rows, licences |
| Emergency | /emergency | Stripped-back page: big phone number, "What to do while you wait" steps for burst pipes, gas smell and power faults, then call button |
| Book | /book | The booking form on its own, full width |
| Thanks | /thanks | Confirmation state with booking reference and what happens next |
| Privacy, Terms | /privacy, /terms | Plain text placeholder pages |

Generate 6 suburb pages from the template (Box Hill, Blackburn, Ringwood, Doncaster, Camberwell, Glen Waverley) and 4 service pages (Hot water, Blocked drains, Switchboard upgrades, Smoke alarms) to show the system works.

## Interactions and working forms

The demo must behave like a live site: every button goes somewhere and the form completes end to end in the browser.

**Booking form** (used on home, service, suburb and /book pages)

- Fields: What needs fixing (select with the 8 job types + Other), Describe the problem (textarea, optional), Suburb (text with autocomplete from the service list), Preferred time (chips: ASAP, This week, Pick a date → date input), Name, Mobile (Australian format, 04XX XXX XXX), Email (optional), "I'm a landlord or property manager" checkbox (reveals Tenant name and Tenant mobile), photo upload (optional, up to 3 images, previews shown).
- Validation on blur and on submit, with inline plain-English errors ("Add a mobile so we can text you a time"), focus moved to the first error, and `aria-live` announcements.
- Submit shows a pressed button with a spinner for ~900ms, then swaps the form for a success panel: a --success tick, "Thanks, [Name]. We'll text [mobile] with a time shortly.", a booking reference (HC- + 5 random digits), and a mock SMS bubble preview of the confirmation.
- Data is saved in memory for the session and, if configured, POSTed to `CONFIG.formEndpoint` (Formspree, Make or a webhook). With no endpoint set it stays a front-end demo and logs the payload to the console.
- The hero job search, quick chips, sticky header pill and service "Book this" links all open the form with the job and suburb pre-filled: on desktop as a right-side drawer (480px), on mobile as a full-height sheet. Esc and the close button dismiss it; focus is trapped while open and returned afterwards.

**Other interactions**

- Every phone number is a `tel:` link; on desktop it also offers a copy-to-clipboard tooltip.
- Mobile sticky call bar appears after 300px of scroll and hides while the booking sheet is open.
- Suburb checker matches case-insensitively against the service-area list.
- Reviews carousel: arrows, drag/swipe, keyboard arrows when focused; arrows disable at the ends.
- Stepper: rows are buttons; arrow keys move between them; the active row has `aria-expanded`.
- FAQ: native `<details>`/`<summary>` enhanced with the height transition.
- Promo bar dismissal and header state use in-memory state only.
- All hit areas at least 44px; visible 3px --focus ring on every focusable element.

## Making it reusable for other tradies

One config object and one set of CSS variables drive every page, so a new tradie's demo takes about 30 minutes: swap the config, the accent colour and the photos.

```javascript
const CONFIG = {
  brand: { name: "Hartley & Co.", fullName: "Hartley & Co. Plumbing + Electrical", founded: 1998 },
  trades: ["plumbing", "electrical"],
  contact: { phone: "(03) 5550 4127", email: "jobs@hartleyandco.example", base: "Blackburn VIC 3130" },
  hours: { weekdays: "7am–5pm", emergency: "24/7" },
  suburbs: ["Box Hill", "Blackburn", "Mitcham", "Nunawading", "Vermont", "Forest Hill", "Ringwood", "Croydon", "Doncaster", "Templestowe", "Balwyn", "Camberwell", "Surrey Hills", "Glen Waverley", "Burwood", "Mont Albert"],
  stats: { rating: 4.9, reviewCount: 612, jobsDone: 18400 },   // PLACEHOLDER
  guaranteeYears: 10,                                            // PLACEHOLDER
  promo: "Summer's coming: free switchboard safety check with any electrical job this month.",
  formEndpoint: null
};
```

- Text that mentions the business, phone, suburbs or stats reads from CONFIG, never hard-coded.
- Single-trade tradies: setting `trades: ["plumbing"]` hides the Electrical column, nav item and pages, and rewrites "Plumbing and electrical, one call" to "Plumbing done properly".
- Brand colour: changing `--accent`, `--accent-hover`, `--accent-active` and `--accent-bevel` restyles buttons, links, underline and promo bar together.
- Photos live in one `/images` folder with fixed names (hero.webp, step-1.webp … team.webp, areas.webp) so they can be replaced without touching markup.
- Reviews come from a `reviews.json` array (name, suburb, job, trade, rating, date, quote).

## Build and QA checklist

**Build**

- [ ] Semantic HTML (header, nav, main, section, footer), modern CSS, vanilla JS, no framework
- [ ] Breakpoints at 390, 768, 1024 and 1440px; no sideways scroll at any width
- [ ] Lighthouse 90+ for performance and accessibility on mobile
- [ ] Images in WebP with width/height set; hero preloaded
- [ ] LocalBusiness / Plumber / Electrician schema with the placeholder details

**Human-web-design review**

- [ ] No avoided font anywhere, including buttons, labels and form fields
- [ ] Serif only on the hero H1 and the wordmark
- [ ] No two neighbouring sections share a background or reveal style
- [ ] Brush underline on one word per H2, clear of the letters, wrapping correctly
- [ ] Stepper, odometer and auto-typing pause on hover, focus, off screen and hidden tab
- [ ] Reduced motion shows every end state; nothing stays hidden with JS off or when printing
- [ ] No STEP badges, icon-in-circle cards, breadcrumbs or hero eyebrow
- [ ] Light page throughout, no dark full-width bands
- [ ] Section intros span the full content width
- [ ] Copy is plain English and results-led; every figure is marked [PLACEHOLDER] or sourced

**Working demo**

- [ ] Booking form validates, submits and shows the success panel with a reference
- [ ] Hero search, chips, header pill and service links pre-fill the form
- [ ] Every phone link dials; mobile call bar shows after scroll
- [ ] Suburb checker returns both the yes and the "call us" messages
- [ ] Every nav and footer link reaches a real page; no console errors on any page
