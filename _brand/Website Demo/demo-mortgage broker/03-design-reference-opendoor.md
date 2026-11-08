# Design reference: Opendoor-style look and feel

This is the original design.md the demo's look is based on. Where it conflicts with 02-brief.md (fonts, stats, stepper style, testimonials, content), follow the brief.

Build the top of a landing page for a home-selling / instant cash-offer real-estate service, recreating the look and feel of opendoor.com. Include only three sections: a **photo hero with an address search**, a **video-testimonial carousel**, and a **"Sell your home the easy way" stepper**. Use semantic HTML, modern CSS and vanilla JS. Make it responsive (mobile → 1440px) and respect `prefers-reduced-motion`. Use a placeholder brand name, your own placeholder photos, and fictional families.

## Visual language

- **Feel:** warm, homey and trustworthy, with tactile UI. It has a soft warm-white canvas and brown-tinted neutrals, with one strong royal-blue accent. The buttons and inputs have a subtle "pressable" 3D bevel.
- **Colours:**
  - canvas `#FBF9F9`
  - card `#FFFFFF`
  - warm greys `#EDE8E8` / `#EFEAE9` / `#E6E2E0`
  - ink `#23201D`
  - body `#5E564E`
  - brown accent text `#806D63` / `#43352E`
  - primary blue `#0042E6` (hover `#002B96`, active `#002EDE`)
  - focus `#81A2F2`
  - success green `#5F8944`
  - promo banner `#0042E6` with white text
- **Fonts:**
  - The **hero H1 only** uses "DM Serif Display" at 60px/64px, tracking -0.03em.
  - Everything else uses "Graphik" (fallback "Inter"). H2 48px/50px weight 500 with tracking -0.05em (very tight); body 18px/24px with tracking -0.02em; UI 16px/500.
- **Radii:** buttons and inputs 12px, photo cards 20px, the hero frame about 24px, small chips 8–10px.
- **Signature bevels** (use exactly):
  - primary button: `box-shadow: 0 0 0 1px #0042E6, inset 0 0 0 1px rgba(255,255,255,.25), inset 0 -4px 0 #0021D9`
  - secondary button: `0 0 0 1px rgba(88,64,50,.16), inset 0 0 0 1px rgba(255,255,255,.3), inset 0 -4px 0 rgba(88,64,50,.1)`
  - address field: `0 0 0 1px rgba(88,64,50,.16), 0 16px 20px -9px rgba(88,64,50,.19), 0 37px 37px 3px rgba(88,64,50,.12), inset 0 -3px 0 rgba(88,64,50,.1)`

## Section 1 — Hero

- **Promo bar:** full width, 40px tall, `#0042E6`, centered white 14px text "Make your move now: Get 4.99% 5/6 ARM on select [Brand] homes." with a small white circular arrow button, and an × on the right.
- **Header** (72px, on the canvas colour):
  - Left: the wordmark "[Brand]" in a serif at 20px.
  - Right: "Sell", "Buy", "Agents" and "Mortgage" in 15px/500, then a white "Sign in" button (12px radius, 44px tall, secondary bevel).
- **Hero frame:** a full-width photo frame inset 12px from the edges, about 24px radius, about 620px tall. It shows a warm lifestyle photo of a family playing on a sofa in a sunlit living room (a dad lifting a toddler). Add a subtle dark gradient at the top for text legibility.
- **Centered copy over the photo** (white):
  - H1 serif "Your home. Your options."
  - Two lines of 18px: "Get a cash offer by entering your address. / Discover how we can simplify your home sale."
- **Address search bar:** about 520px wide, 56px tall, white, 12px radius, with the address-field bevel. A location-pin icon and placeholder "Enter your home address", and a **blue square search button** (44px, 10px radius, primary bevel) with a magnifier icon on the right.
- **Microcopy:** "Takes 5 minutes │ Your information stays private" in 14px white/80%.
- **Stats row** along the bottom of the photo, three columns in white:
  - "★★★★★ on Trustpilot"
  - "**311,337** customers served", where the number is an odometer that rolls up digit by digit
  - "**2x** faster to sell to [Brand]"
  - Numbers are 32px/500 with 14px captions.
- **Sticky search:** after scrolling past the hero, a compact address search pill (grey `#EDE8E8`) appears inside the sticky header.

## Section 2 — Testimonial carousel

- **Header row:** the H2 "Hear from families / who moved with [Brand]" on the left (48px/500, tight tracking). On the right, two square arrow buttons ← → (grey `#EDE8E8`, 10px radius, 36px).
- **Carousel:** a horizontal scroll-snap row of video cards. The first card is about 560px wide and the following ones about 340px, so the next one peeks in.
- **Each card:**
  - A 20px-radius video thumbnail (an outdoor family photo in front of a home) with small glass controls in the corner (captions "Tt" and mute).
  - Below it, an 18px quote in ink: "We've been here for 15 years and we wanted it to be perfect—[Brand] just eliminated all that, and we got to focus on the next chapter."
  - Then the name in 16px/500 ("The Watson family") and the location in 14px brown ("Temecula, CA").
- **Video:** videos autoplay muted on hover.

## Section 3 — "Sell your home the easy way"

- **Layout:** two columns.
- **Left:** a 20px-radius photo of a brick suburban house with a lawn. Overlaid at the bottom is a frosted white address input (`rgba(255,255,255,.9)`, blur, 12px radius) that **auto-types "123…"**. Then a status line cycles through:
  - "Retrieving info on the address"
  - "Looking at similar houses in the neighbourhood"
  - "Checking housing market data for comparisons"
  - "Preparing a preliminary offer"
- **Right:** the H2 "Sell your home the easy way", then a **vertical accordion stepper** of 4 rows separated by 1px warm dividers. Each row has a small grey icon tile (32px, 8px radius) and an 18px/500 title.
  1. **Get an estimated cash offer** (active): it expands to show "Enter your address and a few details about the home." with a thin progress bar under it that fills over about 4s.
  2. Show us your home — "Take a photo tour in our app, or we can send an agent to do it for you."
  3. Get the final offer — "Review the cash offer, fees, and net proceeds."
  4. Review and accept — "Pick your close date, sign, and move when you are ready."
- **Auto-advance:** the steps advance automatically, and the left image and overlay change to match each step.

## Do / Don't

- **Do:** use a warm off-white canvas, brown-tinted neutrals, one royal-blue accent, a serif only for the hero H1, very tight Graphik headings, tactile bevelled buttons and inputs, real lifestyle photography, and autoplaying micro-demos.
- **Don't:** use pure grey neutrals, flat shadowless buttons, gradients, or more than one accent colour, and don't put the serif on anything except the hero headline.
