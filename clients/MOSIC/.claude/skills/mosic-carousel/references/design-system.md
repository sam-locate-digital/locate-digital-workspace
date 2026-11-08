# MOSIC carousel design system — "text-led, anatomy highlight"

Text carries the slide; anatomy renders explain it. Each slide reads in two seconds: eyebrow, big headline, short body, one visual.

## Canvas

- 4:5 portrait, final 1080x1350 PNG.
- Margins: 8% left/right, 7% top/bottom. Text column left-aligned.
- **Logo zone** (carousel cover and CTA only): top-left box, roughly the top 22% height x left 55% width. Keep it completely empty in the render; `compose.py` places the real logo there.
- **Progress bar** on every carousel slide (never on a single post): thin segmented bar along the bottom margin, one segment per slide, completed segments solid, the rest faint, with "N/T" small at the right end.
- Swipe cue: a small thin chevron ">" at the right edge, vertically centred, on every carousel slide except the last. None on a single post.

## Palette (exact hex)

| Role | Hex |
|---|---|
| Navy (brand primary) | `#1B2674` |
| Deep navy (dark backgrounds) | `#12184C` |
| Purple (accent, highlights) | `#7D59B4` |
| Lavender (accent on dark) | `#E4E0F7` |
| Light background | `#F4F3F9` fading to `#E2DEEC` |
| Muted body text on light | `#5B5762` |
| Gradient | `#12184C` → `#1B2674` → `#7D59B4` (top-left to bottom-right) |

Accent words: purple `#7D59B4` on light slides, lavender `#E4E0F7` on dark slides.

## Typography

- Headlines: **Poppins Bold**, tight leading, slight negative tracking, sentence case.
- Eyebrow: Poppins SemiBold, uppercase, wide letter-spacing, preceded by a short horizontal dash.
- Body and list sub-lines: **Inter Regular**.
- List numbers: Poppins Light, large, faint lavender-grey.

## Background rhythm (never two identical backgrounds in a row)

Default 7-slide order: light → deep navy → gradient → light → deep navy → light → gradient.

## The anatomy highlight

- A stylised, semi-translucent 3D render of the relevant body part, glassy blue-grey or soft silver tones with fine muscle-fibre detail, like a premium medical-education render.
- The injured or relevant structure glows in purple `#7D59B4` → lavender `#E4E0F7`, with a soft bloom.
- Placement: right side or lower right, cropped by the slide edge, sitting *behind* the text column at no more than about 40% of the slide area. Text never overlaps the glowing area.
- No skin, faces, blood, gore, surgical imagery or real clinical photos. No labels or callout text unless the copy asks for one.
- Anatomy belongs on `anatomy` slides and can appear faintly on `cover` and `cta`. Keep `list` slides clean, or use a small inset render.

## Slide types

| Type | Layout |
|---|---|
| `cover` | Light gradient background. Logo zone empty. Lower half: eyebrow, 2-line headline (accent word), one-line sub. Large faint anatomy render on the right. |
| `anatomy` | Deep navy background. Eyebrow + headline top-left, body below. Glowing anatomy render lower right. |
| `quote` | Gradient background. Eyebrow + headline, then a frosted rounded card containing "Our approach" plus the quote in italic. |
| `list` | Light background. Eyebrow + headline, then 3–5 rows: big faint number, bold title, sub-line, thin dividers. |
| `statement` | Deep navy background. Big headline centred vertically, body underneath, optional subtle anatomy or texture. |
| `cta` | Gradient background. Logo zone empty. Eyebrow, headline (accent), body, sitting in the lower half above the progress bar. No button, pill, website, phone number or handle on the slide; booking details go in the caption only. |
| `single` | "Spotlight" one-image post, deliberately unlike the carousel cover (see below). |

## Single posts: "Spotlight"

Single posts must never look like a carousel cover. They flip every cover choice:

| | Carousel cover | Single (Spotlight) |
|---|---|---|
| Background | Light lavender gradient | Deep navy `#12184C` with a large soft purple `#7D59B4` radial glow behind centre, darker at the edges |
| Layout | Left-aligned, text in lower half | Symmetrical and centred |
| Anatomy | Cropped off the right edge | Large and centred, seen straight from behind, glowing structure with a strong bloom |
| Text | Eyebrow with dash + headline + body bottom-left | Eyebrow (lavender, no dash) and 2-line white headline centred at the top; one centred body line under the anatomy |
| Logo | Large, top-left (400px) | Small white sign-off, bottom centre (280px), via `compose.py --pos bottom-center` |

- Keep the bottom 17% of the render empty dark background for the logo.
- Accent words in lavender `#E4E0F7`; body in lavender-grey.
- No footer, progress bar, counter, chevron or border. Contact details go in the caption.
- Body ≤ 15 words so it fits on two centred lines.
- For a body part that isn't symmetrical from behind (e.g. one ankle, one knee), centre it anyway: a single limb or joint, centred, glowing.

