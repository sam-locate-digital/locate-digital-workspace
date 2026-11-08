---
name: client-report-call
description: Prepare Sam for a client's monthly report call, the meeting where Sam walks a Locate Digital client through last month's results. Reads the client's report and narrative, then writes a short brief with the headline result, a run sheet, how to handle a bad month honestly, next month's 2–3 priorities to agree, the decisions and approvals needed from the client, and whether a growth or upsell conversation has been earned. Use whenever Sam mentions a report call, monthly review, results call, strategy call or catch-up with an existing client ("prep my MOSIC report call", "I'm walking Brighten through October tomorrow", "how do I explain this month's drop to the client", "what should I cover on the monthly call"). Not for writing the report itself (use monthly-report-narrative), first calls with prospects (use discovery-call) or 30/60/90-day check-ins (use check-in-call).
---

# Client report call prep

Every Locate retainer includes a monthly report and a call (Starter: one call a month, Growth: a strategy call, Scale: fortnightly calls). The report says what happened. The call is where the client decides whether they trust Locate with next month.

A good report call isn't a read-through of the report, because the client can read. It does four jobs:

1. **Agree next month's plan:** 2–3 priorities the client signs off on.
2. **Get decisions and approvals:** budget changes, creative, access, anything waiting on the client.
3. **Handle a bad month well:** say it first, explain the cause plainly and show the fix.
4. **Spot growth:** when results justify more, plan how to raise it, and when they don't, leave it alone.

The output is a short brief Sam reads before the call, not slides.

## Workflow

### 1. Load the client and the month

Read, in this order:

- `clients/<client>/CLAUDE.md`: package and tier, goal, baseline metrics at onboarding, average job, appointment or loan value, active channels, key contact, anything out of scope.
- `clients/<client>/reports/YYYY-MM/`: `report.md` or `report.html` for the numbers, and `narrative.md` if it exists. If there's no narrative yet, tell Sam that running `monthly-report-narrative` first gives a better call, then work from the report's numbers anyway.
- The previous month's report, to see whether last month's priorities were delivered. Some clients' reports cover two months in one folder (`reports/2026-03-04/`), so look for last month's figures wherever they are. Anything in the client's `reports/` folders counts as the report (`report.md`, `report.html`, `data.json`, decks), as long as you name the file you took each number from.
- Past briefs and `-notes.md` files for this client in `_ops/meetings/` (search by client name). Look for what was agreed last call, what was promised, and any decisions still open. If there are none (early on, there won't be), use the "next steps" or "actioned" parts of the previous report or deck, or `memory/`, and say where the promises came from.
- `clients/<client>/memory/` for pending items such as access requests and open questions.

### 2. Short interview

Ask Sam only what the files can't tell you, using the AskUserQuestion tool with concrete options (or ask in chat if it isn't available). One round, at most four questions:

- **When, who and how long:** the date and time, who's attending (names if Sam knows them), and 30 or 60 minutes.
- **How the client is feeling:** happy, neutral, or uneasy (asking about results, slow to pay, mentioned budget pressure, an agency comparing).
- **Anything Sam needs from them:** approvals, access, budget, content, a case study.
- **Anything Sam doesn't want to raise yet.**

Skip what Sam already told you.

### 3. Read the month

Work out these before writing anything:

- **The headline:** one sentence on the result that matters to the client's goal, against the baseline and last month. Use the client's outcome metric (enquiries, booked appointments, new patients, funded loans), not clicks or impressions. Example: "38 new patients from Google Ads in April, up from 31 in March, at 52 dollars each."
- **Good, flat or bad month.** Judge it against the goal and the baseline, not one metric picked in isolation. If it's mixed, say which part matters more.
- **What drove it:** the 1–3 changes or outside factors behind the result (a campaign change, a landing page, seasonality, a rate change, tracking breaking). Separate what Locate did from what happened anyway, and say honestly when you can't tell.
- **What was promised last month** and whether it happened.
- **Whether the numbers agree.** Check figures across the report, the deck and `CLAUDE.md`. If they contradict each other (totals that don't add up, a "best month ever" claim the history doesn't support), put that under "handle carefully" so Sam doesn't repeat it.

**Early months and missing goals.** In the first month or two, the onboarding baseline may be the same month you're reporting, and no goal may be set yet. Then compare with the months before onboarding, if the report has them, and say so. Write "not set" in the goal column, and make "agree a goal" one of the decisions for this call, because every later report call depends on it.

### 4. Plan the call

**Run sheet.** Fit it to the call length. For 30 minutes:

1. *Open (2 min):* how they're going and what's on their mind. Let them raise any worry first.
2. *Headline (3 min):* the one sentence, then stop and let it land.
3. *What worked and what didn't (8 min):* 2–3 points, each with the reason.
4. *Next month (8 min):* the 2–3 priorities, with Sam's recommendation, then agreement.
5. *Decisions (5 min):* each item they need to decide or approve.
6. *Close (4 min):* recap what was agreed, confirm the next call date. Raise growth here only if it's been earned.

For 60 minutes, roughly double each block and add room for their questions.

**If it's a bad month,** plan it as follows, because how Sam handles a dip decides whether the client stays:

- **Say it first, in the headline.** Don't make them find it or wait for slide 6.
- **Give the cause in plain words.** If it's Locate's (a campaign change that underperformed, a tracking gap), own it in one sentence without grovelling. If it's outside (seasonality, rate rises, a competitor spending heavily), show the evidence. Don't blame the market when you're not sure.
- **Show the fix and when they'll see it.** "We've already rolled the ad group back. You should see it in the first two weeks of the next report."
- **Write a holding line** for the hardest question they might ask ("Should we be worried?" or "Is this working?"). Make it honest and specific, not reassuring for the sake of it.
- **No upsell in a bad month.**

**Next month's priorities.** 2–3, each one specific and tied to the goal: what Locate will do, why, and what the client should see from it. Example: "Rebuild the Essendon landing page so mobile visitors can book in two taps. Essendon clicks are converting at half the CBD rate." Put Sam's recommendation first so the client can agree to it rather than design it.

**Decisions and approvals.** List each one with the options and Sam's recommendation, worded as a question the client can answer on the call: "Can we move 500 dollars from Meta to Google search for November? Search is booking patients at half the cost." Include anything outstanding from earlier months.

**The growth check.** Decide whether a growth conversation is earned this month. It's earned when:

- results are at or above goal for two months or more, and there's clear room to scale (spend capped by budget, not by demand), or
- the client keeps asking for work outside their tier, or Sam's hours keep running past the tier's band (`_brand/launch/02-pricing.md`), or
- they've mentioned a new location, service or hire that marketing should support.

If it's earned, write the one or two lines Sam uses to raise it, framed around their goal, not Locate's revenue ("You're booking every patient the budget allows. If we added a grand a month, I'd expect around X more. Want me to model it properly before next call?"). Only use an estimate the numbers support, and label it as an estimate. If it isn't earned, say "not this month" and why, in one line, so Sam doesn't force it.

**Confidentiality.** Don't use another client's results or name as a comparison unless Sam has said that client agreed to it.

### 5. Write the brief

Use `$HOME/.claude/skills/client-report-call/assets/brief-template.html`. Sections, in order:

1. **Header:** client, month reported, call date, time, length, who's attending.
2. **Headline:** the one sentence, plus good, flat or bad.
3. **Key numbers:** a small table of 4–6 outcome metrics: this month, last month, baseline, goal. Only figures from the report.
4. **Last month's promises:** what was agreed and whether it was delivered.
5. **Run sheet.**
6. **What worked, what didn't:** 2–3 points each, with the reason in plain English.
7. **If it's a bad month:** cause, fix, timing and holding line. Delete the section for a good or flat month. If a flat or mixed month still invites a hard question ("Is Google Ads working?"), put that holding line under "Handle carefully".
8. **Next month:** the 2–3 priorities.
9. **Decisions needed:** each as a question with Sam's recommendation.
10. **Growth:** the lines to use, or "not this month" and why.
11. **Handle carefully:** anything not to raise yet, with holding lines.
12. **After the call:** send a recap of what was agreed the same day, log decisions in the client's `memory/`, and confirm the next call date.

**Writing style.** Sam's voice: plain, measured, Australian English, sentence case, no em dashes, no exclamation marks. Write anything Sam will say out loud as spoken sentences. Name metrics the way the client talks about them ("new patients", not "conversions").

**Numbers.** Every figure comes from the report or the client's `CLAUDE.md`. Don't round in a way that changes the story, and don't invent an estimate. If a number Sam needs is missing (cost per patient, say), list it under a "missing data" note rather than calculating something shaky.

**Where to save.** `_ops/meetings/YYYY-MM-DD-<client>-report-<YYYY-MM>.html`, using the call date and the month reported, with the client folder name in lowercase. Example: `2026-11-05-mosic-report-2026-10.html`. Create `_ops/meetings/` if needed. Post-call notes go beside it with the same name ending in `-notes.md`.

Then in chat, give Sam the path, the headline, the priorities and any decision that needs the client.

## Before delivering, check

- Is the headline about the client's outcome, compared with the baseline or goal, rather than a vanity metric?
- If the month is bad, does the brief say so first, with a cause and a fix?
- Is every number from the report, and are missing numbers flagged rather than invented?
- Can each decision be answered on the call (yes or no, a choice between options, or a number the client gives)?
- Is the growth conversation earned, and if not, does the brief say so?
- No other client named or compared without permission?
