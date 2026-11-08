---
name: mosic-carousel
description: Creates a finished Instagram/Facebook post for MOSIC (Melbourne Osteopathy Sports Injury Centre), either a carousel or a single-image post. Writes the copy in MOSIC's voice, then has Higgsfield (GPT Image 2.5) render it in the text-led "anatomy highlight" style, composites the real logo, QA-checks the text and saves ready-to-post 1080x1350 PNGs plus caption and hashtags. Has a scheduled mode that takes the next topic from the MOSIC topic list and runs without stopping for approval. Use whenever Sam asks for a MOSIC carousel, slides, swipe post, single post, Instagram post or social post on any topic ("MOSIC carousel on runner's knee", "single post about desk back pain for melbosteo"), or when a scheduled task asks for this week's MOSIC social post. Not for blog posts (mosic-blog-post) or Google Business posts (mosic-gmb-post).
---

# MOSIC — Social post (carousel or single image)

Turn a topic into a finished post: copy in MOSIC's voice, slides rendered by Higgsfield, real logo composited on top, every slide checked before it reaches Sam.

Read these before starting:
- `references/brand-voice.md` — who we're talking to, how MOSIC sounds, AHPRA advertising limits
- `references/design-system.md` — palette, type, slide types, the anatomy-highlight style
- `references/prompts.md` — the Higgsfield prompt template and per-slide-type wording

Skill folder: `clients/MOSIC/.claude/skills/mosic-carousel/` (paths below are relative to the workspace root `G:\My Drive\Claude Code.Locate`).

## Modes

- **Interactive** (default): Sam is in the chat. Show the copy and wait for approval before rendering.
- **Scheduled**: the run was started by a scheduled task, or the prompt says "scheduled mode". Nobody is watching, so never stop to ask a question. Follow the rules in [Scheduled mode](#scheduled-mode) on top of the steps below.

## Inputs

- **Topic** (required). A condition, injury, season or service: "hamstring strains in winter footy", "desk-job lower back pain", "first parkrun back after injury". In scheduled mode it comes from the topic list.
- **Format**: `carousel` (default 7 slides, allowed 5–10) or `single` (one image). If not given, choose: `single` for one sharp tip, myth or seasonal reminder; `carousel` when the topic needs a why + what to do. State which you picked.
- Optional: angle, practitioner quote to use, date to post.

If the topic is too broad ("back pain"), pick a specific angle that fits the target reader and say which one you picked. In interactive mode, only ask Sam when two angles would make genuinely different posts.

## Step 1 — Write the copy

Follow `references/brand-voice.md`.

**Carousel.** Default 7-slide arc (adapt, don't force it):

| # | Slide type | Job |
|---|---|---|
| 1 | `cover` | Scroll-stopping hook. Eyebrow + 2-line headline + one-line promise. Logo. |
| 2 | `anatomy` | Why it happens. Name the structure, show it lit up. |
| 3 | `anatomy` or `quote` | The real cause / MOSIC's root-cause view. |
| 4 | `list` | What the first appointment covers, or what to look out for. |
| 5 | `statement` | Melbourne / seasonal / lifestyle angle. |
| 6 | `list` | What you can do — 3 to 5 numbered actions. |
| 7 | `cta` | Soft closing line: eyebrow, headline, short body. Logo. No button, website, phone number or handle on the image; booking details go in the caption. |

**Single.** One `single` slide in the **Spotlight** style (dark, centred, small logo at the bottom; see design-system.md). It must never look like a carousel cover. Eyebrow, headline, one body line of 15 words or fewer, and the centred anatomy highlight. No website or phone on the image; contact details go in the caption. It has to work with no swipe: the headline is the hook *and* the point, the body gives the one takeaway, and the caption carries the detail and the call to action.

Hard limits per slide (GPT Image renders text reliably only when it's short):
- Eyebrow ≤ 4 words. Headline ≤ 8 words. Body ≤ 25 words.
- List slides: max 5 items, each a title ≤ 6 words + optional sub-line ≤ 10 words.
- Mark one or two headline words as the accent (rendered in purple/lavender).

Also write: caption (80–150 words; for a single post lean towards the longer end), 5–8 hashtags, and alt text per slide (one sentence).

Run the copy through the `humaniser` skill's rules (Australian English, no AI vocabulary, no em dashes). Then, in interactive mode, **show Sam the copy table and wait for approval** before spending credits. Edits at this stage are free; edits after rendering cost a re-render.

## Step 2 — Prepare Higgsfield

1. `models_explore` → `get` `gpt_image_2_5` once per session to confirm parameters still exist.
2. Get the user's folder preference: `get_preferences` before the first generation (per the Higgsfield server rules). Don't create a project unless that preference says to.

No logo upload is needed: slides are rendered **without** a logo and the real logo is composited locally in Step 4. Never ask GPT Image to draw the MOSIC logo; it redraws it wrong.

## Step 3 — Render the slides

Build each prompt from `references/prompts.md` (base block + slide-type block + exact copy). Settings for every slide:

```
model: gpt_image_2_5
aspect_ratio: "4:5"
resolution: "2k"
quality: "high"
```

Single post: one `generate_image` call, then `jobs_wait`.

Carousel — order matters for consistency:
1. Render **slide 1 alone** with `generate_image`. This is the style anchor.
2. Render all remaining slides in one `generate_image_batch`, each passing slide 1's job id in `medias` as `{"value": "<slide-1 job id>", "role": "image_references"}`, with the prompt line "Match the reference image's typography, colour palette, margins and progress-bar style exactly; change only the content."
3. `jobs_wait` until all are terminal, then show them once with `show_generation_by_ids`.

Cost is about 2.75 credits per slide (≈20 for a 7-slide carousel, ≈3 for a single). Say so in one line before rendering; no need to ask again once the copy is approved.

## Step 4 — Composite logo and export

Download every result URL into the output folder (Step 6) as `raw/NN.png`, then run:

```bash
python "clients/MOSIC/.claude/skills/mosic-carousel/scripts/compose.py" "<out>/raw/01.png" "<out>/01.png" --logo navy
python "clients/MOSIC/.claude/skills/mosic-carousel/scripts/compose.py" "<out>/raw/07.png" "<out>/07.png" --logo white
python "clients/MOSIC/.claude/skills/mosic-carousel/scripts/compose.py" "<out>/raw/02.png" "<out>/02.png"
```

- Carousels: `--logo navy` on light slides, `--logo white` on dark/gradient slides, omit on slides without a logo (only cover and CTA carry it).
- Single posts: always `--logo white --pos bottom-center` (small sign-off logo, bottom centre).
- The script resizes to 1080x1350 and places the logo in the reserved clear zone (top-left, or bottom centre with `--pos bottom-center`).

## Step 5 — QA every slide

Open each final PNG with the Read tool and check against the approved copy:
- Every word spelled exactly as approved; no extra or invented text, no fake logo, no garbled pseudo-text.
- Nothing inside the logo zone except the composited logo (top-left on cover/CTA, bottom 17% on a single).
- Highlighted anatomy matches the structure named on the slide (hamstring = back of thigh, adductors = inner thigh, etc.) and nothing looks gory or clinical-photo realistic.
- Carousels: progress bar shows the right slide number and nothing (anatomy included) runs behind it. Singles: Spotlight layout (centred, dark), and no progress bar, chevron or footer text. Text contrast is readable.

A failing slide gets **one** re-render with the same prompt plus a line naming the exact defect ("The word 'adductors' was misspelled; spell it a-d-d-u-c-t-o-r-s."). If it fails twice, keep the best version and tell Sam exactly what's wrong rather than calling it done.

## Step 6 — Save and deliver

Output folder: every post gets its **own new folder** inside `clients/MOSIC/Social Media Post/`, named `YYYY-MM-DD-<slug>` (date = the planned post date from the topic row if known, else today; slug = 2–5 lowercase hyphenated words from the topic, e.g. `2026-11-09-spring-gym-comeback`). Never save into the parent folder or reuse another post's folder; if the name already exists, add `-2`.
- `01.png` … `NN.png` — final 1080x1350 slides (a single post is just `01.png`)
- `raw/` — Higgsfield originals (keep for re-composites)
- `copy.md` — status line, format, slide copy table, caption, hashtags, alt text, Higgsfield job ids, QA notes

Send Sam the slides with SendUserFile (or show the folder), plus the caption ready to paste. Mention any QA issue that survived the retry.

## Scheduled mode

Topic list: `clients/MOSIC/content/social-topics.md`. Rows look like `- [ ] 2026-10-27 | topic | format`; format may be blank.

1. **Pick the topic.** Take the first unticked row in `## Queue` whose date is in the current week or earlier. If there is none, stop: render nothing and report "No MOSIC topic queued for this week — add one to content/social-topics.md."
2. **Check credits.** Call `balance`. If there are fewer than 30 credits, stop and report the balance instead of rendering.
3. **No questions.** Make every judgement call yourself (angle, format when blank, slide count) and record each one under "Decisions" in `copy.md`.
4. **Skip the copy approval** in Step 1. Everything else runs as normal, including the humaniser pass, QA and the one retry.
5. **Never publish.** Output is a draft. The first line of `copy.md` is `Status: DRAFT — awaiting Sam's review`, or `Status: NEEDS FIX — <what's wrong>` if a slide still fails QA after its retry.
6. **Update the topic list.** Tick the row and move it under `## Done`, appending ` → Social Media Post/<folder>/ (made YYYY-MM-DD)`. If the run failed before saving slides, leave the row in the queue and add a note under it.
7. **Report.** Finish with a short summary: topic, format, decisions made, any QA issue, credits used, the folder path and the caption ready to paste. Attach the slides with SendUserFile where available.
