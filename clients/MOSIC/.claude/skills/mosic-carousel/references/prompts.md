# Higgsfield prompt template (GPT Image 2.5)

Each slide prompt = **base block** + **slide-type block** + **copy block** (+ reference line for slides 2+). Paste the hex values and font names exactly; GPT Image follows explicit values far better than adjectives.

## Base block (every slide)

```
Instagram carousel slide, 4:5 portrait, slide {N} of {T}, for an osteopathy sports injury clinic in Melbourne. Premium, modern, clean editorial design: text-led, generous whitespace, crisp vector-sharp typography.
Typography: headlines in Poppins Bold, sentence case, tight line spacing; eyebrow label in Poppins SemiBold uppercase with wide letter-spacing and a short horizontal dash before it; body text in Inter Regular. All text left-aligned in a column starting 8% from the left edge.
Palette only: navy #1B2674, deep navy #12184C, purple #7D59B4, lavender #E4E0F7, light background #F4F3F9 to #E2DEEC, muted text #5B5762.
Bottom of slide: a thin segmented progress bar with {T} segments spanning the width inside the margins, the first {N} segments solid ({bar colour}), the rest faint, and the small text "{N}/{T}" at its right end.
{chevron line}
Render ONLY the text quoted below, spelled exactly, with no other words, letters, logos, watermarks, icons with text, or brand names anywhere.
```

- `{bar colour}`: navy `#1B2674` on light slides, white on dark/gradient slides.
- `{chevron line}`: "A small thin chevron '>' at the right edge, vertically centred." On the last slide: "No chevron."
- **Single post:** don't use this base block; the `single` block below is self-contained.

## Slide-type blocks

**cover**
```
Background: soft light gradient #F4F3F9 to #E2DEEC. Leave the top-left area (top 22% of height, left 55% of width) completely empty: no text, no shapes. On the right side, a large faint semi-translucent 3D anatomical render of {body part}, glassy silver-blue with fine muscle-fibre detail, the {structure} glowing purple #7D59B4 to lavender #E4E0F7 with a soft bloom, cropped by the right edge, behind the text, not overlapping it. Text sits in the lower half.
```

**anatomy**
```
Background: solid deep navy #12184C with a very subtle vignette. Lower right: a stylised semi-translucent 3D anatomical render of {body part}, glassy blue-grey with fine muscle-fibre detail, the {structure} glowing purple #7D59B4 to lavender #E4E0F7 with a soft bloom, cropped by the slide edge, taking no more than 40% of the slide, never behind the text, and kept above the progress bar (the bottom 10% of the slide stays clear background). No skin, no face, no gore. Text in white, accent words in lavender #E4E0F7, body text in lavender-grey at 80% opacity, in the upper-left text column.
```

**quote**
```
Background: smooth diagonal gradient from #12184C top-left through #1B2674 to #7D59B4 bottom-right. Text in white, accent words in lavender #E4E0F7. Below the headline, a frosted-glass rounded rectangle card (white at 10% opacity, thin white border at 20%) containing a small label and an italic quote in Poppins Italic.
```

**list**
```
Background: soft light gradient #F4F3F9 to #E2DEEC. Headline in deep navy #12184C, accent words in purple #7D59B4, eyebrow in navy #1B2674. Below, {k} rows separated by thin hairline dividers #DCD9E6: each row has a large thin number (Poppins Light, lavender-grey) on the left, a bold title in navy (Poppins SemiBold) and a sub-line in muted #5B5762 (Inter). {Optional: a small glowing anatomy inset of {body part} in the top-right corner.}
```

**statement**
```
Background: solid deep navy #12184C with a faint, out-of-focus purple #7D59B4 glow in one corner. Large headline vertically centred in the text column, white with accent words in lavender #E4E0F7, body text below in lavender-grey at 80% opacity.
```

**cta**
```
Background: smooth diagonal gradient from #12184C top-left through #1B2674 to #7D59B4 bottom-right. Leave the top-left area (top 22% of height, left 55% of width) completely empty. Text in white, accent words in lavender #E4E0F7, sitting in the lower half of the slide above the progress bar. Optional faint anatomy glow of {body part} at the far right edge, kept clear of the text and the progress bar. No button, no pill shape, no website address, no phone number, no social handle: only the eyebrow, headline and body.
```

**single** (Spotlight: use this block *instead of* the base block)
```
Standalone Instagram post, 4:5 portrait, for an osteopathy sports injury clinic in Melbourne. Style: 'Spotlight': cinematic, symmetrical, centred composition.
Background: deep navy #12184C, with a large soft radial glow of purple #7D59B4 behind the centre of the frame, fading to near-black navy at the edges.
Centre of the frame: a large, symmetrical, semi-translucent 3D anatomical render of {body part} seen straight from behind, glassy silver-blue with fine muscle-fibre detail, the {structure} glowing bright purple #7D59B4 to lavender #E4E0F7 with a strong bloom. It occupies the middle of the frame between the headline and the body text. No face, no skin, no gore.
Top of the frame, centred: a small uppercase eyebrow label in lavender #E4E0F7, Poppins SemiBold, wide letter-spacing, then a centred two-line headline in white Poppins Bold, sentence case, with the accent words in lavender #E4E0F7.
Below the anatomy, centred: one line of body text in Inter Regular, lavender-grey.
Leave the bottom 17% of the frame completely empty apart from the dark background: no text, no shapes.
No progress bar, no slide counter, no chevron, no frame or border.
Render ONLY the text quoted below, spelled exactly, with no other words, letters, logos, watermarks or brand names anywhere.
```
Copy block for a single: Eyebrow, Headline (two lines, centred, accent words in lavender #E4E0F7), Body (centred, may wrap to two lines).

## Copy block

```
Text to render, exactly:
Eyebrow: "{EYEBROW}"
Headline: "{HEADLINE}" — render the words "{ACCENT}" in {accent colour}.
Body: "{BODY}"
{List rows / quote lines as needed, each in quotes}
```

## Reference line (slides 2+)

```
Match the reference image's typography, colour palette, margins, text sizes and progress-bar style exactly; change only the background type, visual and text described here.
```

## Retry line (QA failure)

```
Previous attempt had this defect: {defect}. Fix it; spell "{word}" exactly as {letter-spaced}.
```
