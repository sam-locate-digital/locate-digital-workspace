# Claude Design prompt: MOSIC Hyrox Injury landing page

Paste everything below the line into Claude Design, and attach the three JPGs from `clients/MOSIC/assets/hyrox-landing/` (hyrox-hero, hyrox-treatment, hyrox-prehab). The full-resolution PNGs are in the same folder.

---

## The task

Design and build a single conversion landing page for **MOSIC (Melbourne Osteopathy Sports Injury Centre)**. It targets people training for Hyrox who are carrying an injury, or worried about getting one, ahead of the **Melbourne Hyrox race week, 9–13 December**.

- **Traffic:** Google Ads search only. These visitors have just searched for something like "hyrox knee pain", "injured before hyrox" or "hyrox physio melbourne". They already know their problem. The page needs to confirm fast that MOSIC treats exactly this, then get them booked.
- **One conversion goal:** online booking through Cliniko.
  - Every primary button links to `https://melbourne-osteopathy-sports-injury-centre.cliniko.com/bookings`.
  - Phone `(03) 9663 6202` is a secondary, lower-weight option only.
- **No site navigation.** It's a standalone ad landing page with no menu links out. The only exits are booking and phone.

## Look and feel

Match MOSIC's existing clinical website style: clean, light, professional and trustworthy. Give it a bit of athletic energy through layout, iconography and copy, not through colour. Use the house colours only:

| Token | Value | Use |
|---|---|---|
| Navy | `#1c2674` | Primary buttons, headings accents, links |
| Navy hover | `#141a56` | Button hover |
| Purple | `#8b68b3` | CTA band background, icons, highlights |
| Body text | `#333f4b` | Headings and body |
| Muted text | `#555555` | Paragraphs |
| Light band | `#f5f6fb` | Alternating section backgrounds |
| Border | `#e8e8e8` | Cards, dividers |
| White | `#ffffff` | Page background |

- **Fonts:** Ubuntu for headings (weights 300/500; section titles are light 300), Roboto for body. Load from Google Fonts.
- **Buttons:** pill-shaped, `border-radius: 25px`, navy fill, white Ubuntu 500 text, slight lift on hover.
- **Cards:** white, 1px `#e8e8e8` border, 6px radius, purple line icons (stroke 1.5, no fill).
- **Background:** fully light page. The only solid colour block is the purple CTA band.
- **Motion:** subtle micro-interactions (fade-up on scroll, button hover lift, accordion open). Respect `prefers-reduced-motion`.
- **Do not** use Hyrox's black and yellow, their logo, or anything implying MOSIC is an official Hyrox partner. Use the word "Hyrox" descriptively only, e.g. "Hyrox injury treatment".

## Imagery

Three images are attached. Use them in these slots:

1. **`hyrox-hero.jpg` (16:9), hero:** an athlete in a navy singlet doing a sandbag lunge in a bright gym. The subject is on the right and the left third is empty wall and window space, so place the H1 and CTA over or beside that space. Add a soft white-to-transparent gradient from the left if text sits on the image. On mobile, crop to roughly 4:5 with `object-position: 70% center` so the athlete stays in frame.
2. **`hyrox-treatment.jpg` (4:3), "How MOSIC helps" or "First visit":** an osteopath in a navy polo assessing a patient's knee on a treatment table.
3. **`hyrox-prehab.jpg` (4:3), "Injured with weeks to go?" or prehab:** an athlete doing a banded split squat while an exercise physiologist with a tablet coaches.

Use each image once. Everywhere else, use typography, inline SVG icons and the light bands. Give the images descriptive, keyword-aware alt text (e.g. "Osteopath assessing a Hyrox athlete's knee pain at MOSIC Melbourne").

## Page structure and copy direction

Write all copy in Australian English (e.g. "specialised", "centre"). Keep it plain, warm, confident and specific to Hyrox. Avoid hype, avoid guarantees ("fix", "cure", "pain-free by race day"), and don't overuse em dashes. Keep paragraphs short, because visitors are skimming on mobile.

### 1. Slim header
MOSIC logo (left, placeholder `MOSIC_LOGO`), "Book online" pill button (right), and the phone number on desktop only. It should stay sticky once the visitor scrolls past the hero.

### 2. Hero
- **H1** includes "Hyrox injury" and "Melbourne". Direction: *Hyrox injury treatment in Melbourne, so you can still make race day.*
- **Sub-line:** sports-injury osteopaths who understand running plus functional strength load, with a plan built around your race date.
- **Urgency chip:** "Melbourne race week: 9–13 December". Optionally add a live "X weeks to race week" counter calculated from today's date (hide it after 13 December).
- **Primary CTA:** "Book a Hyrox injury assessment" → Cliniko. Secondary text link: "or call (03) 9663 6202".
- **Trust row** (small icons + text): AHPRA-registered osteopaths · No referral needed · Private health fund rebates · CBD & Essendon clinics.

### 3. "Where Hyrox hurts": injuries by station
This is the signature section. Show a grid of station cards, each mapping a Hyrox movement to the injuries it commonly causes:
- **Running (8 × 1 km):** shin splints, Achilles, calf strain, plantar fasciitis
- **Sandbag lunges:** knee pain (front of knee), hip flexor
- **Wall balls:** knee and shoulder overload
- **Sled push & pull:** lower back, calf, hamstring
- **Farmers carry:** lower back, grip and forearm, neck/traps
- **Burpee broad jumps:** knee, shoulder, wrist
- **Row & SkiErg:** lower back, shoulder

Each card has a station icon, a station name, a one-line injury list and a small "Book for [area]" link → Cliniko. Under the grid add one line: "Not listed? If it hurts when you train, we'll assess it."

### 4. "Injured with weeks to go?": the honest answer
A short, reassuring section speaking to the "can I still race?" fear. Most training injuries can be managed so you keep training in a modified way rather than stopping completely. The earlier you're assessed, the more options you have. Show a simple horizontal timeline (vertical on mobile):

**Assess → Modify training → Treat & strengthen → Taper → Race day → Recover**

### 5. How MOSIC helps
Three to five service cards, pulling only from services MOSIC actually offers:
- **Osteopathy:** hands-on assessment and treatment of the injured area and what's loading it
- **Exercise physiology / prehab:** strength and loading plan to get you race-ready (we have an Exercise Physiologist on staff)
- **Remedial massage & myotherapy:** pre-race and post-race recovery (30, 45 or 60 min)
- **Dry needling:** for tight, overloaded muscles
- **Podiatry & gait assessment:** for running-related foot, shin and knee issues

### 6. What happens at your first visit
Three steps with numbered circles:
1. **Assessment** (45–60 min initial consult): history, training load, movement testing
2. **Treatment**: hands-on care starts the same session
3. **Your race plan**: what to keep, what to modify, and when to come back before race week

### 7. Mid-page CTA band
Full-bleed purple `#8b68b3` band with white text, e.g. "Race week is 9–13 December. Get assessed while there's time to adjust." Navy pill button → Cliniko.

### 8. Locations
Two clean cards with name, address, a "Book at this clinic" button → Cliniko, and an optional embedded map placeholder:
- **Bourke Street (CBD):** Suite 903, Level 9, 140 Bourke St, Melbourne VIC 3000
- **Essendon:** 320–324 Keilor Rd, Essendon North VIC 3041

### 9. FAQ
A two-column accordion on desktop, one column on mobile, using `<details>`/`<summary>`. Write the answers too. Questions:
- Should I keep training for Hyrox with an injury?
- How close to race day is too late to get treated?
- Do I need a GP referral? (No.)
- Can I claim on private health insurance? (Yes, depending on your fund and level of cover; check with your insurer.)
- Osteo or physio for a Hyrox injury? (Both treat sports injuries; our osteopaths specialise in sports and training injuries.)
- Do you do pre-race or post-race massage?
- What should I bring or wear?

Add FAQPage JSON-LD schema for these.

### 10. Final CTA + footer
Repeat the primary CTA. Minimal footer with clinic name, phone, email `info@melbourneosteopathycentre.com.au`, and a small disclaimer: "Hyrox is a trademark of its respective owner. MOSIC is not affiliated with Hyrox."

### Mobile
On mobile, show a sticky bottom bar with a full-width "Book online" button, plus a call icon button. Design mobile-first, because most ad traffic will be on phones.

## Keywords to work in naturally
Use these in the H1, H2s, FAQ and alt text without stuffing: *hyrox injury, hyrox physio melbourne, hyrox osteopath, hyrox knee pain, hyrox lunges knee pain, hyrox lower back pain, hyrox achilles, shin splints before hyrox, injured before hyrox, hyrox injury prevention, hyrox prehab, massage after hyrox.*

## Technical requirements

The page is a standalone landing page, but it will be pasted into WordPress (blank page template) as a single Custom HTML block. So:
- Output **one self-contained HTML file**. Put all CSS in one `<style>` block and any JS in one small vanilla `<script>`. No frameworks, no build step, no external JS libraries.
- Clearly mark the paste-able section with `<!-- ▼ START -->` and `<!-- ▲ END -->` comments. Anything outside them (preview-only body styles) is not needed in WordPress.
- **Scope every style** under one wrapper class, `.hx-wrap`, and prefix all classes `hx-`. Use no global selectors (`body`, `h1`, `*`) inside the paste-able section, so it can't clash with the WordPress theme.
- Full-bleed bands use the `width: 100vw; left: 50%; margin-left: -50vw` technique so they break out of the theme container.
- Every booking link has the class `hx-book` and a `data-cta="<location-on-page>"` attribute (e.g. `hero`, `station-knee`, `cta-band`, `sticky-mobile`) for GTM click tracking. The phone link uses `tel:+61396636202` with the class `hx-call`.
- In the preview, image `src` values point at the attached files (`hyrox-hero.jpg` etc.). Mark each one with a comment such as `<!-- REPLACE with WP media URL -->` so they're easy to swap after upload to the WordPress media library.
- Accessibility: semantic headings (one H1), WCAG AA contrast, visible focus states, and tap targets ≥ 44px.
- Performance: keep it light. Use inline SVG icons, lazy-load images below the fold, and no heavy animation libraries.

## Deliverable
One polished, responsive HTML page following the brief above. Show the desktop and mobile designs, and keep all copy final (no lorem ipsum).
