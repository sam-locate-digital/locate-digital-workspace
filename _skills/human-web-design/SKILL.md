---
name: human-web-design
description: Design standard for websites, landing pages and page sections that should not look AI-built. Use whenever building, redesigning or reviewing any web page or section for Locate Digital or a client — choosing fonts, adding motion or animation, laying out steps/cards/heroes, or writing page copy. Covers AI-default fonts to avoid, subtle motion rules, layout patterns to avoid, plain-English results-led copy, and the preview-then-rollout way of working.
---

# Human web design

The standard Locate Digital uses so websites read as designed by people, not generated. Apply it to Locate's own site and to client pages alike. Each rule below came from real feedback on locatedigital.io; the reason is given so edge cases can be judged rather than followed blindly.

Read `references/fonts.md` before choosing type, `references/motion-patterns.md` before adding animation, and `references/testing.md` before verifying in a browser.

## 1. Fonts: never the AI defaults

Never use these for any text on a page:

- **AI-builder defaults:** Inter, Plus Jakarta Sans, Poppins, Manrope, DM Sans, Space Grotesk, Figtree, Fraunces, Instrument Serif. Prospects have seen them on hundreds of generated sites, and they read as "made by a tool".
- **AI-company brand fonts:** Styrene and Tiempos (Anthropic), Söhne (OpenAI). They make a page look like an AI product.

If a client brand or an existing site already uses one of these, flag it and offer alternatives rather than silently keeping it. Pick from the less common pairings in `references/fonts.md`, and show the options side by side before deciding (see section 5).

## 2. Motion: subtle, varied, considerate

- **Subtle, not dramatic.** Gentle fades, short rises, soft focus, small hover responses. No flying word-by-word headlines, 3D card flips, heavy parallax or full-page cursor glows. Sam compared a dramatic version side by side and chose subtle every time; dramatic motion reads as a template showing off.
- **No repeats side by side.** Neighbouring sections never share the same background graphic or the same reveal animation. Identical bubble backgrounds in three stacked sections "looks bad". Rotate background treatments and reveal styles (rise, focus, slide, scale) section by section, and check the whole page order after any change.
- **Brush underline on accent words.** When a heading highlights a word in the accent colour, give it a tapered hand-drawn brush underline that paints in left to right as it enters view. Draw it as a background so a wrapped phrase is underlined on both lines, and keep it clear of the letters. Bold and slightly angled, not a thin line.
- **Considerate autoplay.** Anything that plays or loops on its own (workflow demos, carousels, counters) pauses on hover and keyboard focus, when off screen and in a background tab. While someone hovers to read, show the content in full rather than freezing it half-animated. Clicking a control jumps there and carries on.
- **Reduced motion always works.** With `prefers-reduced-motion`, skip the movement but keep the end state visible: content shown, underlines drawn, loops off.
- **Never leave content hidden.** Anything pre-hidden for a scroll reveal needs a fallback (a scroll-position check alongside the IntersectionObserver), and must show when printing.

## 3. Layout: avoid the generic generated patterns

- **No stock step cards.** Avoid rounded cards with a coloured bar along the top and a small "STEP 1" badge. Prefer editorial treatments: a large numeral, a hairline rule (which can carry a progress line), a heading and body, with no box.
- **Be suspicious of the generic "AI card"** in general: rounded white box, faint border, icon in a tinted circle, title, two lines of copy, repeated three or four times. If a section looks like that, find a layout that belongs to the content.
- **No breadcrumbs or hero eyebrows** by default. Drop "Section / Page" breadcrumbs and the small label above a hero headline unless they carry real meaning. The headline should start the page.
- **Light pages.** Light-first layouts; no stacked dark full-width bands. A single contained dark element is fine as an accent.
- **Text spans the content width.** Section intros and closing lines run the full width of the section's content area, lined up with the grid below, rather than sitting in a narrow column on the left.

## 4. Copy: plain, results-led, honest

- **Plain English for non-technical readers.** Say outright when no technical skills are needed. Cut jargon: "data flows", "prompts", "Skills", "Projects", "private models", "operating system", "integrations layer". If a smart person outside the industry wouldn't use the word, replace it.
- **Results-led.** Spell out what changes in the reader's week: hours back, faster replies, marketing that actually goes out, room to grow without hiring. Features support results; they don't lead.
- **Never invent numbers.** Use only figures with a real source (pitch decks, research files, client data). If a stat's scope gets widened (for example "brokers" to "finance professionals"), flag that it may overstate the source. Where no number exists yet, describe the outcome ("Same day", "Weekly") instead of making up a percentage. Leave placeholders for real client results rather than filling them.

## 5. Way of working

- **Show options side by side.** For any style choice (fonts, underline styles, label treatments, layouts), show three to five options visually before building one. Mark the current state for comparison and recommend one.
- **Preview before rollout.** For a site-wide change, build it on a throwaway preview copy of one page first, let Sam review it, and only roll out once approved. Preview files are never linked from the site and are deleted after rollout.
- **List copy changes by page.** After any copy edit, report exactly what changed on which page. Separate rewritten wording from formatting-only changes, and flag any figure that needs its source checked.
- **Verify in the browser before saying done.** Load every affected page, check for script errors, confirm nothing stays hidden, and scan the rendered text for leftovers of whatever pattern was just removed. Say plainly what could not be checked (for example, animations that could not be watched live).

## Quick review checklist

Run this before calling any page finished:

1. No font from the avoid lists, anywhere, including buttons and labels.
2. Motion is subtle; no two neighbouring sections share a background or reveal.
3. Accent words in headings have the brush underline; it doesn't cover the letters.
4. Autoplay pauses on hover, focus, off screen and for reduced motion.
5. No stock step cards, generic icon cards, breadcrumbs or unearned hero eyebrows.
6. Light page, no stacked dark bands; section text spans the content width.
7. Copy is plain English, results-led, and every number has a source.
8. Every page checked in the browser; changes reported page by page.
