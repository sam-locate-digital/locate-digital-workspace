---
name: locate-content
description: Plans and writes Sam's weekly Instagram content for @locatingsam to grow to 10,000 followers. Produces a 7-day plan (a reel every day, plus carousels and single-image posts across teaching, journey and story content), writes every caption and slide, hands each reel to reels-script, and adds Trial Reels hook variants. Also runs the weekly review and the one-off profile setup. Use when Sam asks to "plan my week", "plan content", "what should I post", "write this week's posts", a carousel or single post for Sam's Instagram, or a content review. Reel scripts on their own go to reels-script; Facebook posts go to locate-voice.
---

# Locate content: @locatingsam weekly plan

Plans and writes a week of Instagram content for Sam's personal account, **@locatingsam**, with one goal: **10,000 followers through consistent daily posting.** Leads come later. Every post is judged on whether it earns a follow.

This skill is the planning layer. It decides what goes out each day and writes the captions, carousels and single posts. **Every reel script is written by the `reels-script` skill.** Follow that skill's hook formulas, formats and output for anything spoken on camera.

## Before planning (read every time)

1. `_brand/social-media/insights-log.md`: what has earned follows so far, winning Trial Reels hooks, what flopped. Lean the week toward winners.
2. `_brand/social-media/profile.md`: the current bio and pinned posts. If it doesn't exist, run **Profile setup** (below) before the first week.
3. `$HOME/.claude/skills/locate-content/references/formats.md`: the spec for every format in the weekly mix.
4. `$HOME/.claude/skills/locate-content/references/reference-accounts.md`: what the five reference accounts do and why it works.
5. `$HOME/.claude/skills/locate-voice/references/voice-bank.md`: what Locate actually offers, so content never promises a service that doesn't exist.

## Who it's for

Owners, principals and team leads of **advice and finance-style firms**: brokers, advisers, accountants, insurance and other businesses that run on client files, compliance and trust. Use their world for examples (file notes, enquiry forms, client follow-ups, document chasing, EOFY, ASIC, AFSL, aggregators).

**But never spell out "financial service providers" as the audience.** The content is operational: how a firm runs its marketing, admin and AI. Write it so any Australian business owner can take the lesson and apply it. Say "your firm", "your business", "your team", not "brokers and advisers, listen up".

They're busy, careful and sceptical of agencies and AI hype. They follow people who are clearly doing the work.

## Voice: convincing with credibility, strong hooks

- **Hooks are strong.** Use the seven formulas in `reels-script` for reels, carousel covers and the first line of every caption. The opening has to stop the scroll.
- **Everything after the hook is calm and specific**, in `locate-voice`'s register: short sentences, concrete detail (the exact task, field, prompt, step), no hype, no exclamation marks, no emojis, no em dashes, Australian spelling.
- **Credibility comes from showing the work, not from results.** Sam has no client results to share yet. Use: screens of real builds, the prompt or setup itself, what Sam tested and what failed, how long something took, what Sam uses every day. Never invent a number, client, result or count. If a real figure would help, leave a `[Sam: real number]` gap.
- First person. Sam is building Locate in public and teaching what Sam builds.

## Topic areas

| Area | Share of the week | What it covers |
|---|---|---|
| **Practical AI for firms** | ~35% | One small AI job done properly: file notes, enquiry summaries, follow-up drafts, document chasing, an AI use policy. A person always checks anything that reaches a client. |
| **Marketing that brings enquiries** | ~25% | One fixable thing between marketing and a booked meeting: forms, Google profile, landing pages, ads, follow-up, reporting on enquiries not clicks. |
| **Journey** | ~25% | Building Locate in public: what today holds, what Sam's building this week, the routine around the work. Present tense. |
| **Story** | ~15% | A decision and why, a client-type story (unnamed), a moment that changed how Sam works. |

## Weekly mix (starting point)

At least one reel every day. Adjust after each weekly review.

| Format | Per week | Area | Who writes it |
|---|---|---|---|
| Teaching reel (talking head) | 3 | AI, marketing | `reels-script` |
| Series episode | 1 | AI or marketing, one fix | `reels-script`, with the series title card |
| Short journey reel (5–15s, text over footage) | 2 | Journey | This skill (see formats.md) |
| Story reel | 1 | Story | `reels-script`, story structure |
| Carousel | 3 | 2 teaching (save-worthy), 1 story or journey | This skill |
| Single image | 2 | 1 claim card, 1 real photo with a journey caption | This skill |

That's 7 reels and 5 feed posts: one reel every day, plus a second post on five days.

**Series:** one episode a week under a fixed name, with the same title card every time. The name is "AI fix of the week" until Sam chooses another (it's a placeholder in the reel style too). Episodes end with "Follow for next week's fix".

## Workflow

1. **Ask Sam what's on this week** (only if Sam hasn't said): builds in progress, client sessions, events, wins, where Sam will be, anything Sam wants to talk about. Journey and story posts come from this. Never invent Sam's week.
2. **Read the insights log** and note what to repeat or drop.
3. **Draft the 7-day plan** as a table (below) and show it to Sam. Wait for Sam's OK or changes before writing everything.
4. **Write every post.** Reels go through `reels-script` (one script file per reel in `_brand/AI Video Editor/Scripts/`). Carousels, single images and journey reels are written here.
5. **Add Trial Reels hooks** to every reel (see below).
6. **Save the week** to `_brand/social-media/<D-M-YYYY>/plan.md`, using the Monday's date in the same style as the existing `2-11-2026` folder.
7. **Offer to build the visuals**: carousels and single images through the Canva connector (Sam's brand kit), or the `photo-story-carousel` skill for photo-story carousels.

### Plan table

| Day | Reel | Feed post | Area | Hook (first line) | CTA |
|---|---|---|---|---|---|

Post times: 7–9am, 12–1pm or 7–9pm AEDT (see `reels-script`). Spread the areas so two days in a row never share the same area and format.

## Trial Reels hooks

Instagram's Trial Reels show a reel to non-followers first. The reference accounts post the same reel with different hooks and keep the winner (the same reel did 183K plays with one hook and 10K with another). So every reel ships with:

- **Main hook:** title card, spoken line, frame-1 visual
- **2 trial hooks:** different formulas, same body. For short journey reels, vary the on-screen line.

Sam posts the main version to followers and the trial versions as Trial Reels. Log which hook won in the insights log.

## Calls to action (aimed at follows)

| Post type | CTA |
|---|---|
| Series episode | "Follow for next week's fix." |
| Journey reel or post | "Follow along if you want to see how this turns out." (or no CTA) |
| Story | Usually none, or a soft follow-along line |
| Teaching reel or carousel | Comment keyword about twice a week, for the full checklist, prompt or template. Otherwise a save prompt: "Save this for your next team meeting." |
| Single image | None, or one specific question |

- Comment keywords need DM automation (ManyChat or Instagram's auto-reply). Until Sam confirms it's set up, use "DM me [word] and I'll send it over". With automation, set the flow to ask people to follow before it sends the freebie.
- Never "follow for more" on its own. A follow CTA always says what they'll get next.
- Never pitch Locate's services in posts. The bio and pinned posts do that job.

## Hard limits

- No financial advice: nothing on rates, products, investments or what consumers should do with money.
- No family or home life.
- No client names, figures or documents unless Sam has written sign-off. Describe clients by type ("a Melbourne broking firm").
- **Story content may show real decisions and pressure in the present** ("I left my corporate job to build this. Here's why."), the way Tahlia's best reels do. It must not become a "what I got wrong" or "hard lessons" post, and never a struggle-and-comeback arc. Sam's business reads as steady and moving forward.
- No invented numbers, timeframes, client counts or results.
- Criticise habits, not people or other agencies.

## Profile setup (run once, then whenever the positioning changes)

Saved to `_brand/social-media/profile.md`:
1. **Bio** (150 characters max, no emojis, sentence case): who Sam is, what the account teaches, why follow. For example: "Sam, founder of Locate Digital. Practical AI and marketing for Australian firms. I show what I build, as I build it." Link: locatedigital.io.
2. **Three pinned posts**: an intro reel ("If you don't know me yet, I'm Sam…": who, what Sam's building, what this account will teach, follow to see it), the best-performing teaching reel, and the best story post. Until there's a winner, pin the intro, the newest series episode and the 2 November story carousel.
3. **Highlights**: up to 4, e.g. Start here, AI fixes, Behind the build, Free stuff.
4. **Intro reel**: write it with `reels-script` (story structure) and give 3 hook variants, the way Jun tests intro reels.

## Weekly review

When Sam shares the week's numbers (or ask for them each Monday before planning):
- Per post: plays/reach, follows, saves, shares, comments. If the vidiQ Instagram connection is set up, `vidiq_instagram_owner_insights` can pull these.
- Record in `_brand/social-media/insights-log.md`: the top 2 posts by follows, the winning trial hooks, one thing to repeat, one thing to drop.
- Adjust next week's mix: more of the format and area that earned follows, less of what didn't. Don't change more than two things a week.

## Output

1. The 7-day plan table (for approval)
2. Then, per day, under a `## Monday` style heading:
   - **Reel**: link to the script file from `reels-script`, plus the 2 trial hooks
   - **Feed post**: format, caption, hashtags, and slide-by-slide copy for carousels (or the image text for single images), plus the visual note
3. A short list of what Sam needs to film or photograph this week
4. Any freebie a CTA promises that doesn't exist yet

Captions follow `locate-voice`'s format rules (first line works above the fold, 40–120 words, 3–5 hashtags with 1–2 Australian business tags). Run the `humaniser` checks over captions before delivering.

## Maintenance

- Update `references/reference-accounts.md` when Sam adds a new account to model.
- Re-check the weekly mix monthly against the insights log.
- Never write a dollar sign followed directly by a digit in this file (Claude Code treats it as an argument placeholder).
- Last updated: 2026-11-04.
