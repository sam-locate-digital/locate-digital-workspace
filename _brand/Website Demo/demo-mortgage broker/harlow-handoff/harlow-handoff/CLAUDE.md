# Harlow Home Loans: demo website

A demo marketing site for a fictional Melbourne mortgage broker, Harlow Home Loans. It is used as a sales demo for real brokers. It was designed in a Claude design canvas and is being rebuilt here as a static Astro site.

## What is in this folder

- `canvas/` is the design source: 27 `.dc.html` files plus `canvas.json` (the board layout). Treat these as the spec. Do not edit them.
- `assets/site.css` is the shared stylesheet. All pages use it. Later rules at the end of the file override earlier ones on purpose.
- `assets/icons/` holds 12 illustrated icons (WebP, transparent).
- `assets/underline-amber.svg` is the brush underline used under key words.
- `assets/asset-map.json` maps every `/_blob/<id>` URL in the canvas files to a file in this folder.
- `photos/PHOTO-LIST.md` lists the 16 photos to add to `photos/`.

## How to read a `.dc.html` file

- The page markup sits inside `<x-dc> … </x-dc>`. Ignore `<helmet>` except for font links.
- `{{name}}` is a value from the `renderVals()` method in the `<script type="text/x-dc">` block at the bottom.
- `<sc-if value="{{x}}">` means render only when x is true.
- `<sc-for list="{{items}}" as="it">` repeats its contents for each item.
- `<dc-import name="Header" some-prop="…">` includes another file as a component. Attribute names are kebab-case and become camelCase props (`h-lead` → `hLead`).
- `hint-size`, `hint-placeholder-*` and `support.js` are canvas-only. Drop them.
- Event attributes like `onClick="{{open}}"` point to functions in `renderVals()`.

## Pages (21) and components (6)

- Pages: Main (home), FirstHome, NextHome, Refinancing, Investing, SelfEmployed, Building, HealthCheck, Team, Claire, Tom, Priya, Mia, Reviews, Guides, Book, Thanks, CreditGuide, Privacy, Complaints, Terms.
- Components: Header (promo bar, sticky header, dropdown, mobile menu, call bar), Footer (with the compliance block), Enquiry (slide-in drawer with focus trap), EnquiryForm (3-step form), ReviewRail (carousel or filterable grid), CtaBand (closing call to action).
- Routes: Main → `/`, FirstHome → `/first-home`, NextHome → `/next-home`, and so on in kebab-case. Update every internal link that points at a `.dc.html` file.

## Rules that must not be broken

- Fonts: Hanken Grotesk for all text, Gloock only for the "Harlow" wordmark. Never use Inter, Poppins, DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk, Figtree, Fraunces or Instrument Serif.
- Colours: navy ink #14204A, slate body #46506A, royal blue #1F45D6 for buttons and links, amber #F5A524 as the accent (underlines, small ticks). Keep the clean, light look. No dark full-width bands.
- No stock "STEP 1" cards and no icon-in-a-circle cards.
- No interest rates, savings figures or approval promises shown as fact. Every number stays marked `[PLACEHOLDER]` until the client supplies a real one. Do not remove or invent placeholder values.
- Respect `prefers-reduced-motion`: reveals, the odometer, the step auto-advance and the carousel must all stop or jump to their end state.
- Mobile first, tested from 360px to 1440px wide.
- Reviews are illustrative. Keep the "Illustrative reviews for this demo" note until real, permitted reviews replace them.
- Compliance text (credit licence, general advice warning, Credit Guide, complaints/AFCA) stays as placeholders for the aggregator to supply.

## Behaviour to keep

- Scroll reveal: elements with `.rv` and `.ul` get the class `in` when they enter the viewport (IntersectionObserver), gated by `html.js-rv`. See `harlowReveal()` in the canvas scripts.
- Header: after you scroll past the hero, the header gets `is-past`, the "What are you planning?" pill appears and the mobile call bar shows.
- Homepage situations list: hovering a row crossfades the photo on the right.
- "How we work" steps: auto-advance with a progress bar, pause on hover or focus, arrow keys move between steps.
- Enquiry form: 3 steps, inline validation, aria-live messages, a short "sending" state, an `HL-` reference number and an .ics calendar download on the thanks step. Prefill comes from the button that opened it.
- FAQ uses `<details name="faq">` so only one answer is open at a time.

## Checks before calling a page done

- `npm run build` passes with no warnings about missing files.
- No `/_blob/` URLs, `.dc.html` links or `{{` left in the output.
- Keyboard: every control reachable, visible focus, drawer traps focus and closes on Esc.
- Lighthouse accessibility 95+ on the homepage.
