---
name: check-in-call
description: Prepare Sam for a 30, 60 or 90-day check-in call after Locate Digital has delivered a workshop or service, such as an AI training workshop and policy, a new retainer's first months, or a one-off project like tracking or a landing page. Works out what this checkpoint should focus on, then writes a short brief that checks whether the work is actually being used, finds what's stuck, captures results and testimonial-ready quotes, and makes a well-timed referral ask. Use whenever Sam mentions a 30/60/90-day check-in, follow-up call, post-workshop call, "how's it going" call, or checking on a client after delivery ("prep my 30-day check-in with the Geelong brokerage", "60-day call with MaxiFinancial on Friday", "it's been 90 days since the workshop", "I want to get a testimonial from…"). Not for monthly report calls (use client-report-call) or first calls with prospects (use discovery-call).
---

# 30/60/90-day check-in prep

The check-ins are part of what Locate sells. The AI training offer includes reviews at 30, 60 and 90 days, and every new retainer has a first 90 days where the client decides whether this was a good call. The check-ins matter because:

- **Training that isn't used is wasted money,** and clients quietly blame the trainer. A check-in that finds what's stuck and fixes it is what makes the workshop pay off.
- **Proof comes from these calls.** Locate is early and short on case studies. Results and quotes captured at day 60 and 90, in the client's own words, are the proof the next ten sales depend on.
- **Referrals come from these calls.** A client who has just told you what changed is in the best mood they'll ever be in to name someone else.

Each checkpoint has a different main job:

| Checkpoint | Main job | Also |
|---|---|---|
| **30 days** | Adoption: is it being used, and what's stuck? Fix blockers fast. | Note early wins to come back to. |
| **60 days** | Results: what has changed, in numbers and in their words. | Ask permission to quote. A light referral ask if the energy is right. |
| **90 days** | Outcome against the original goal. A testimonial or case study ask. The referral ask. | Agree what happens next (stays on retainer, moves to monthly reporting, or the engagement closes). |

Don't pitch more work on these calls. If the client raises more work, note it, say Sam will come back with a proposal, and move on. These calls exist to make the client successful, and pitching on them undermines that.

## Workflow

### 1. Load what was delivered

Read:

- `clients/<client>/CLAUDE.md`: what was sold, the goal, the baseline and the key contact. If there's no client folder (a workshop-only client may not have one), use whatever Sam provides and the meetings folder.
- For AI training: the offer details in `_services/ai-adoption/` (workshop content, policy, the 30/60/90 promise), plus anything delivered to this firm, such as their AI use policy, workflow templates or workshop notes.
- For a marketing service: the onboarding baseline, tracking setup notes, and any reports so far in `clients/<client>/reports/`.
- Past briefs and `-notes.md` files for this client in `_ops/meetings/`, especially the workshop or kickoff notes and the previous check-in. What was promised last time, and did Sam do it?

Client folders are often thin early on: access still marked pending, no reports yet. Don't fill the gaps with guesses. Put anything Sam should confirm in a short "check before the call" list at the top of the brief. If what Sam tells you conflicts with the files (Sam says a campaign launched but nothing in the folder shows it), go with Sam and note that the files need updating.

### 2. Short interview

Use the AskUserQuestion tool with concrete options (or ask in chat if it isn't available). One round, at most four questions, skipping what Sam already told you:

- **Which checkpoint** (30, 60 or 90), and the date, length and format.
- **Who's on the call:** the principal only, or including the staff who actually use it. Users give truer answers about adoption than principals.
- **What Sam has already heard:** any feedback, complaints, wins or silence since delivery.
- **Has this client already given a testimonial or a referral?**

### 3. Plan the call

**Goal and win condition.** One line for this checkpoint. Example for 60 days: "Find out what's changed since the workshop, get one quotable result in their words, and permission to use it."

**Run sheet (30 minutes).** The blocks are the same at each checkpoint, but the time shifts from adoption to results:

| Block | 30 days | 60 days | 90 days |
|---|---|---|---|
| Open: how things are, what they want from the call | 3 | 3 | 3 |
| Usage: what's used, by whom, what's stopped | 10 | 8 | 5 |
| Blockers: what's stuck, and what Sam will do | 9 | 5 | 4 |
| Results: what has changed, in their words | 5 | 10 | 10 |
| Ask and close: proof or referral ask, next check-in | 3 | 4 | 8 |

**Usage questions.** Write 4–6, each with a probe and a short "listen for" note. Ask about specific recent events, because "Is it going well?" always gets "Yeah, good":

- "Walk me through the last time someone used it for a file note. What did they do, start to finish?"
- "Who on the team uses it most? Who hasn't touched it since the workshop?"
- "Has anyone used an AI tool that isn't on the approved list in the policy?" Ask this one openly and without judgement. The policy only protects the licence holder if people follow it, and finding out at day 30 is far better than at an audit.
- "What did you try, and drop?"

For a marketing service, the same idea applies to the client's side of the funnel, which is where results are usually won or lost:

- "Think about the last enquiry that came through from the ads. What happened to it, from the moment it landed?"
- "How quickly is someone calling new enquiries back at the moment? Who does it?"
- "Are the enquiries the kind of clients you want? What's the best one so far, and the worst?"
- "Is there anything we said we needed from you (access, photos, approvals) that's still sitting there?"

**Blockers.** Plan for the likely ones, and for each write what Sam can offer then and there.

- *AI training:* a tool access problem, a workflow step that doesn't fit how they work, one sceptical senior person, no time to practise, or a policy that's too strict to follow. Offer a 20-minute follow-up session, a revised template or a policy tweak.
- *Marketing service:* slow or no follow-up on enquiries, lead quality not matching what they want, missing access or approvals holding up campaigns, tracking gaps, or creative that needs their input. Offer a follow-up script, tighter targeting, a list of what's waiting on them with dates, or a quick tracking fix.

**Capturing results and proof.** Write the questions that draw out results in their own words: "What's different about your week compared with before the workshop?" "If you had to put a number on it, how much time does a file note take now?" Record numbers *as the client states them*. Don't round them up or turn them into percentages they didn't say.

Asking permission to use a quote is part of the call, not something to sort out later: "That's a great way to put it. Would you be comfortable with me using that as a quote, with your name and firm? I'll send it to you to approve first." At 90 days, ask about a short case study: what it involved for them (a 15-minute interview and approving the draft) and that they approve everything before it's used.

Most Locate clients are regulated (brokers, advisers, lenders), so keep quotes about how the firm works, not about client outcomes. "Our team gets file notes done the same day" is fine. "Our clients get approved faster" is not. A regulated client may also need their licensee or compliance team to approve a public testimonial, so mention that when asking.

**The referral ask.** Timed for the checkpoint: a light version at 60 days if they're clearly happy, and the full ask at 90. Write it word for word, specific and easy to act on: "Is there another principal you'd trust who's dealing with the same thing with AI? If you're happy to, I'll send you a two-line note you can forward." For a marketing client, adjust it to who they know: "Is there another business owner you refer with who's trying to get more clients online? …" Have a fallback ready: "No pressure. If someone comes to mind, I'd be grateful for the intro." If the call has gone badly (low adoption, unhappy client), skip the referral and testimonial asks entirely. Fix the problem first and ask next time.

**Expansion signals.** Don't pitch on the call. Do note anything that suggests further work (a second office, new staff to train, interest in marketing), so Sam can follow up separately.

**Handle carefully.** Anything sensitive: compliance issues they mention (don't give legal advice; suggest they check with their licensee or compliance adviser), staff performance (talk about the workflow, not the person), and no other client's results or names unless that client agreed.

### 4. Write the brief

Use `$HOME/.claude/skills/check-in-call/assets/brief-template.html`. Sections, in order:

1. **Header:** client, checkpoint (30, 60 or 90 days), what was delivered and when, call date, time, length, attendees.
2. **Goal:** the one line and the win condition.
3. **Where things stand:** 3–5 bullets: what was delivered, the original goal and baseline, what was promised last check-in and whether it was done, and anything heard since.
4. **Run sheet.**
5. **Usage questions:** numbered, each with a probe and a "listen for" note.
6. **Likely blockers:** each with what Sam can offer on the spot.
7. **Results and proof:** the questions, plus the exact permission-to-quote line. At 90 days, include the case study ask.
8. **The referral ask:** word for word with the fallback, or "skip this time" with the reason.
9. **Expansion signals to listen for:** don't pitch, just note.
10. **Handle carefully.**
11. **After the call:** the same day, send a recap with any fix Sam promised and the date it'll be done. Send any quote to the client to approve before using it. Send the referral blurb if they said yes. Write up the call in the `-notes.md` beside the brief (the full record), and copy any results and approved quotes into `clients/<client>/memory/` so case studies and report calls can find them. Book the next check-in: 30, 60 or 90 days from the delivery or onboarding date, moved to the nearest weekday.

**Writing style.** Sam's voice: plain, measured, Australian English, sentence case, no em dashes, no exclamation marks. Write questions as Sam would say them.

**Numbers.** Only use figures from the client's files, previous notes, or what Sam tells you. Never estimate a result for the client. The point of the call is to hear their numbers.

**Where to save.** `_ops/meetings/YYYY-MM-DD-<client>-day-<30|60|90>-checkin.html`, using the call date and the client folder name or firm name in lowercase. Example: `2026-11-20-maxifinancial-day-30-checkin.html`. Create the folder if needed. Post-call notes go beside it with the same name ending in `-notes.md`. These notes are where testimonial quotes live, so they matter.

Then in chat, give Sam the path, the goal, the top usage question and the ask for this checkpoint.

## Before delivering, check

- Does the brief focus on the right job for this checkpoint?
- Are the usage questions about specific recent events, not "how's it going"?
- Is there an exact permission-to-quote line, and is the referral ask timed right (or skipped if the call is likely to go badly)?
- Is there no pitch for more work in the brief?
- Are the client's numbers left for the client to say, not estimated?
