# Eastside Trades: tradie demo site handoff

This folder holds everything needed to rebuild the Eastside Trades demo website as a real static site in Claude Code. The design was built and refined on a Claude Design canvas. This file is the **current source of truth**. Where it disagrees with `BRIEF.md` (the original brief), this file wins.

## What's in this folder

| Path | What it is |
| --- | --- |
| `design/Main.dc.html` | The working prototype from the canvas: every page, all copy, styles and interactions in one file. Image paths are already rewritten to `../images/…`. |
| `images/` | 19 photos (WebP) and 2 brush-underline SVGs, named as below. |
| `BRIEF.md` | The original brief, kept for reference. |
| `PROMPT.md` | The prompt to paste into Claude Code. |
| `*.png` (folder root) | The original full-size Higgsfield exports. The WebPs in `images/` are the versions to use. |

## How to read `design/Main.dc.html`

It is a canvas component file, not plain HTML, so it won't run on its own in a browser.

- **Styles:** everything inside `<helmet><style>` is ordinary CSS. Design tokens are custom properties on `:root`.
- **Markup:** everything inside `<x-dc>` is the page markup, with a small template syntax:
  - `{{name}}` is a value supplied by the script.
  - `<sc-if value="{{x}}">` shows its contents only when `x` is true.
  - `<sc-for list="{{items}}" as="item">` repeats its contents once per item.
  - Event attributes such as `onClick="{{fn}}"` bind to functions from the script.
- **Logic:** the `<script type="text/x-dc">` block holds a `Component` class.
  - `CONFIG` sits at the top, along with the data arrays: `REVIEWS`, `SERVICES`, `SERVICE_PAGES`, `SUBURB_DETAIL`, `NEARBY`, `STEPS`, `LANDLORD` and `TEAM`.
  - `renderVals()` computes everything the markup reads.
- **Routing:** the whole site is a single-page prototype with internal routing (`state.page` and `state.slug`). Each `<sc-if value="{{is.xxx}}">` block is one page. In the real build, each becomes its own HTML file.

## Business details (all fictional, stored in `CONFIG`)

- **Name:** Eastside Trades (full name: Eastside Trades Plumbing + Electrical). The wordmark is set in Young Serif.
- **Phone:** (03) 5550 4127, a reserved fictional number. **Email:** jobs@eastsidetrades.example
- **Base:** Blackburn VIC 3130. **Hours:** Mon–Fri 7am–5pm, emergencies 24/7.
- **Suburbs:** Box Hill, Blackburn, Mitcham, Nunawading, Vermont, Forest Hill, Ringwood, Croydon, Doncaster, Templestowe, Balwyn, Camberwell, Surrey Hills, Glen Waverley, Burwood, Mont Albert.
- **Placeholders** (visibly highlighted in the prototype when `showPlaceholders` is on):
  - rating 4.9, 612 reviews, 18,400 jobs done
  - founded 1998, 10-year guarantee, reply within "1 business hour"
  - licence, REC and ABN numbers, street address
- **Team:** Pete Morgan (founder, plumber and gas fitter), Jake Morgan (electrician), Tom Nguyen (plumber), Mia Russo (bookings and accounts).
- **Reviews:** the six reviews are samples for the demo. Replace them with the tradie's real reviews.

## Changes made after the original brief (these override BRIEF.md)

1. **Renamed:** Hartley & Co. is now **Eastside Trades** everywhere. The founders are the Morgans.
2. **No fixed-price angle anywhere, and no prices on service pages.** Messaging is trust-led instead: licensed, local, on time, the job explained in plain English, the mess cleaned up.
   - Hero H1: "Fixed right, *first time*." (brush underline on "first time").
   - Hero sub: "Plumbers and electricians for Melbourne's east. / Licensed, local and on time, with the mess cleaned up before we leave."
   - Hero micro line: "Licensed plumbers and electricians │ Local to Melbourne's east".
   - Stepper step 3: "We explain before we start".
   - Why-us item 1: "Explained in plain English."
   - FAQ: the call-out fee and price questions are replaced with "How quickly can you come out?" and "Will you explain what needs doing first?"
   - Hub pages have no "from $" column. The service page button reads "Book a time".
3. **Hero quick chips row removed** (Hot water · Blocked drain · …). It overlapped the search dropdown.
4. **Stepper demo overlays removed.** The frosted cards that played a mini demo per step are gone. The stepper keeps the photo, numerals, rows and the 4.5s progress line.
5. **Hero stats are centred**, both horizontally and vertically, in each of the three columns.
6. **Hero readability:**
   - The top shading is stronger: rgba(35,32,29,.68) → .5 at 42% → transparent at 78% height.
   - The hero brush underline is a thinner stroke, `brush-hero.svg` at 78% opacity, placed below the letters.
   - The sub copy is 19px weight 500 with a tight text shadow.
7. **Search dropdown sits in front.** `.search` has `z-index: 20` and the suggestions list `z-index: 30`, so it overlaps the micro line and stats.
8. **Buttons use click handlers, not form submits.** The hero search arrow, suburb "Check" and "Send booking request" buttons are click handlers, with Enter handled on the inputs, because the canvas preview blocked form submits. In the real site, normal `<form>` submit handling is fine and preferred.
9. **Extra photos on inner pages:**
   - Plumbing and Electrical hubs have a three-photo mosaic under the intro.
   - Landlords has a photo beside the intro and a two-photo row above the benefits list.
   - The Blocked drains and Smoke alarms service pages have their own photos.
10. **Arrow buttons are 44px** (not 40px) to meet tap size. Success text uses a darker green (`--success-ink: #476B32`). Form errors are dark brown, not red.

## Design system

**Colours** (on `:root`):

| Token | Value | Use |
| --- | --- | --- |
| `--canvas` | #FBF9F9 | Page background |
| `--card` | #FFFFFF | Cards, inputs, white bands |
| `--warm-1` / `--warm-2` / `--warm-3` | #EDE8E8 / #EFEAE9 / #E6E2E0 | Alternate bands, chips, rules |
| `--ink` | #23201D | Headings |
| `--body` | #5E564E | Body copy |
| `--brown` / `--brown-deep` | #806D63 / #43352E | Captions and labels (use `--brown-deep` on warm bands for contrast) |
| `--accent` | #1F45D6 | Buttons, links, brush underline, promo bar |
| `--accent-hover` / `--accent-active` / `--accent-bevel` | #1633A6 / #1A3CC4 / #1229B8 | Button states |
| `--focus` | #8AA4F0 | 3px focus ring |
| `--success` / `--success-ink` | #5F8944 / #476B32 | Ticks / success text |

**Type** (Google Fonts):
- Young Serif is used only for the hero H1 (64/70 desktop, 40/44 mobile) and the wordmark.
- Everything else is Schibsted Grotesk:
  - H2: 48/50, weight 600, tracking −0.04em (32/36 on mobile)
  - H3: 24/28
  - Body: 18/26
  - UI and buttons: 16px, weight 600
- Never use Inter, Poppins, DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk, Figtree, Fraunces or Instrument Serif.

**Radii:** buttons and inputs 12px, photos 20px, hero 24px, chips 10px, review cards 16px.

**Bevels:** primary and secondary buttons and the search field use the inset bottom-bevel box-shadows in the CSS (`.btn-primary`, `.btn-secondary`, `.search`). On press, the button moves down 1px and the bevel shrinks from 4px to 2px.

**Brush underline:** one accent word per H2 (`<span class="brush">`) gets `images/brush.svg` as a background image. It paints left to right (background-size 0% → 100%, 700ms) when the section enters view, and wraps across lines with `box-decoration-break: clone`. Note: the SVG has the blue baked in, so a new accent colour needs a recoloured SVG.

**Motion:** subtle, with timings of 300–700ms and easing `cubic-bezier(.2,.7,.2,1)`. Each section has its own reveal:

| Section | Reveal |
| --- | --- |
| Hero | Image scales from 1.04 to 1, copy fades up with a stagger, odometer rolls once |
| Reviews | Cards slide in from the right |
| How it works | Soft focus (blur → sharp) |
| Services | Rise 16px |
| Why us | Rows fade in turn |
| Areas | Scale .98 → 1 |
| Team | Slide in from the left |
| FAQ | Plain fade |
| Booking | Rise 16px |

The stepper pauses on hover, keyboard focus, when off screen and when the tab is hidden. Reduced motion shows every end state. Content is never left hidden without JS, and everything shows when printing.

## Pages (one HTML file each in the real build)

| Page | URL | Notes |
| --- | --- | --- |
| Home | `/` | 12 sections: promo bar, header + mega panel, hero + search, reviews carousel, stepper, services, why us, service areas + suburb checker, team, FAQ, booking form, footer |
| Plumbing / Electrical hubs | `/plumbing`, `/electrical` | Text hero, photo mosaic, service list (Details + Book this), filtered reviews, FAQ, form |
| Service pages | `/plumbing/hot-water`, `/plumbing/blocked-drains`, `/electrical/switchboards`, `/electrical/smoke-alarms` | Photo + H1, signs you need us, what's included, explainer note, 3 reviews, related services, FAQ, form pre-filled with the job |
| Suburb pages | `/areas/<slug>` | All 16 suburbs. Box Hill, Blackburn, Ringwood, Doncaster, Camberwell and Glen Waverley have their own local copy; the rest use generic copy. Nearby chips, local reviews, form pre-filled with the suburb |
| Landlords | `/landlords` | Results-led page; the form opens with "I'm a landlord" ticked (property address + tenant fields) |
| Reviews | `/reviews` | Grid with filter chips (All, Plumbing, Electrical, by suburb) |
| About | `/about` | Story, team photo, team rows, licences |
| Emergency | `/emergency` | Big phone number, what to do while you wait (burst pipe, gas smell, power fault) |
| Book | `/book` | Booking form on its own, full width |
| Thanks | `/thanks` | Booking reference and what happens next |
| Privacy, Terms | `/privacy`, `/terms` | Placeholder text |

## Interactions to keep

- **Booking form:**
  - Fields: job select (8 jobs + Other), description, preferred time chips (ASAP / This week / Pick a date → date input), suburb (autocomplete from the suburb list), name, mobile (AU format 04XX XXX XXX), optional email, landlord checkbox (reveals property address, tenant name and tenant mobile), photo upload (up to 3, with previews).
  - Validation runs on blur and on submit, with plain-English errors, focus moved to the first error, and `aria-live` announcements.
  - On submit, the button shows a spinner for about 900ms, then a success panel shows the HC-XXXXX reference and an SMS preview.
  - The data is POSTed to `CONFIG.formEndpoint` when one is set; otherwise it's logged to the console.
- **Booking drawer:** the hero search, header pill, promo arrow and every Book button open the form pre-filled, as a 480px right-hand drawer on desktop or a full-height sheet on mobile. Focus is trapped while it's open, Esc closes it, and focus returns to the button that opened it.
- **Header:** the mega panel for Plumbing and Electrical; a sticky search pill after scrolling past the hero; copy-to-clipboard on the phone number; on mobile, a menu and a sticky call bar after 300px of scroll.
- **Reviews carousel:** arrows, drag, keyboard and scroll-snap; the arrows disable at the ends.
- **Stepper:** auto-advances every 4.5s; click or arrow keys jump between steps.
- **FAQ:** one open at a time, with a height animation on open.
- **Suburb checker:** "Yes, we're in X most days" or "We may still come out. Call us…".
- **Tweaks** worth turning into config:
  - accent colour
  - trades (`['plumbing','electrical']`, plumbing only or electrical only, which rewrites copy and hides the other column, nav and pages)
  - placeholder highlighting on or off

## Images

| File | Used for | Alt text |
| --- | --- | --- |
| `hero.webp` | Home hero (16:9) | A plumber fixing a kitchen sink while the homeowner chats |
| `step-1.webp` … `step-4.webp` | Stepper steps 1–4 (4:5) | Homeowner booking on her phone · Work ute outside an Edwardian home · Tradie talking a couple through the job on a tablet · Tradie wiping down the bench after finishing |
| `hot-water.webp` | Services: plumbing column, Hot water page, mega panel | New continuous-flow hot water unit being installed |
| `electrical.webp` | Services: electrical column, Switchboards page | Electrician working on a home switchboard |
| `bathroom.webp` | Renovations strip under Services | Renovated bathroom with terrazzo floor and green tiles |
| `areas.webp` | Service areas banner | Rooftops of Melbourne's eastern suburbs at golden hour |
| `team.webp` | Team strip and About | The team beside their work van |
| `tap.webp`, `gas-heater.webp`, `drain-cam.webp` | Plumbing hub mosaic | Plumber replacing a vanity tap · Gas fitter servicing a wall heater · Plumber running a camera through a backyard drain |
| `pendant.webp`, `smoke-alarm.webp`, `power-point.webp` | Electrical hub mosaic (smoke alarm also on the Smoke alarms page) | Electrician fitting a pendant light · Electrician testing a ceiling smoke alarm · Electrician installing a double power point |
| `drain-jet.webp` | Blocked drains page | A plumber jetting a blocked outdoor drain |
| `tenant-door.webp` | Landlords intro | A tradesman greeting a tenant at a rental townhouse |
| `photo-report.webp` | Landlords photo row (with `step-3.webp`) | A plumber photographing finished pipework for the job report |
| `brush.svg`, `brush-hero.svg` | Brush underlines (28% and 78% opacity) | decorative |

## Still open

- **Property manager photo missing:** the Landlords photo row uses `step-3.webp` until a "property manager with tablet" photo is supplied.
- **Form endpoint not set:** `CONFIG.formEndpoint` is `null`. Add a Formspree, Make or webhook URL to receive bookings.
- **Placeholders to swap:** sample reviews, stats, licence numbers, address and founding year all need the real tradie's details.
- **Brush colour:** the brush underline SVGs are blue; recolour them if the accent changes.
