---
name: discovery-call
description: Prepare Sam for a prospect or discovery call, the first proper conversation with a firm that might become a Locate Digital client. Interviews Sam, researches the firm, the person (LinkedIn and media) and their current marketing, works out whether a marketing retainer or AI training fits, then writes a short brief with a run sheet, discovery questions, the qualifying criteria and a polite-exit line, and the exact close to book a proposal meeting. Use whenever Sam mentions a prospect call, discovery call, sales call, intro call, first meeting with a potential client, or an enquiry to follow up ("I've got a call with a broker from Geelong tomorrow", "prep me for my discovery call with…", "an accounting firm booked in from the website", "what should I ask this prospect"). Not for existing clients (use client-report-call or check-in-call) or industry contacts who aren't buyers (use meeting-prep).
---

# Discovery call prep

A discovery call has two jobs, in this order:

1. **Qualify:** decide whether this firm can and should become a client. A firm that can't fund a result becomes a weak case study with Sam's name on it, so a polite, honest exit is a good outcome too.
2. **If they qualify, book the proposal meeting:** leave with a date in the calendar to present a proposal, not "send me something".

Sam doesn't quote a package or price on this call. The proposal does that. If the prospect asks about price, Sam gives an honest range and moves on (see below).

Locate sells two things, and the call may be about either:

- **Marketing retainers:** Starter, Growth and Scale (ads, tracking, SEO, landing pages, reporting). Pricing and rules: `_brand/launch/02-pricing.md` and `_brand/launch/rate-card-generic.html`.
- **AI training for finance firms:** a half-day workshop and a written NCCP-aware AI use policy, with check-ins on the larger tiers. It's priced by number of staff. Source of truth for prices and what each tier includes: `_services/ai-adoption/pitches/mortgage-brokers-finance-pitch.html` and `_services/ai-adoption/CLAUDE.md`.

Use these files for **prices, tiers and what's included**. Don't take the deck's market statistics on trust: some have no source, and some are about financial advisers, not brokers. Apply the numbers rule below to them like any other stat.

Older pricing and persona files were written for physio and osteo clinics. Use their numbers and rules, but not their clinic framing, when the prospect is a finance firm. For a marketing retainer, Starter is the floor and Growth suits most firms running two channels. The real decider is ad spend (the 15–20% rule), so make current or planned ad spend a qualifying question rather than guessing a tier.

## Workflow

### 1. Interview first

Use the AskUserQuestion tool with concrete options (or ask in chat if it isn't available). Skip anything Sam has already said, and keep it to two rounds at most.

- **Who:** name, role, firm, website.
- **How they came in:** referral (from whom), website enquiry, the AI readiness assessment, an event, or cold outreach. This sets how warm the call is and what they already expect.
- **What they've said so far:** the enquiry message, emails, anything from the referrer. If they came in through the AI readiness assessment or a website form, ask Sam to paste their answers. Those arrive in Sam's enquiry inbox, not the workspace, and they're often the best information there is about the prospect.
- **Which offer Sam suspects:** marketing, AI training, both, or unsure.
- **Format:** call, video or in person, and how long. Most discovery calls are 30 minutes.
- **Anything to avoid or be careful of.**

### 2. Research

Do this before planning, because good discovery questions come from knowing what you'll find.

- **The firm:** what they do, size (staff, advisers or brokers, locations), how long they've been operating, any licences (AFSL, ACL) and aggregator or licensee, and recent news.
- **Their marketing now:** check the website (enquiry form, booking path, mobile), whether they're running ads (Meta Ad Library, Google Ads Transparency Center), their Google Business Profile and reviews, and social activity. Note 2–3 specific observations Sam can raise as questions. Don't present them as a teardown; the call is for listening.
- **Their AI use, if training is relevant:** any public sign of AI use, policies or job ads mentioning AI tools.
- **The person:** LinkedIn profile (career history, how long they've been in the role, recent posts) and any media features (trade press, interviews, podcasts). Search "<name> <firm> LinkedIn". If you can't open the profile, include the link and say so. If search doesn't find it, link a LinkedIn people search (`https://www.linkedin.com/search/results/people/?keywords=<First>%20<Last>%20<Firm>`) rather than guessing a profile URL. Stick to public, work-related information.
- **The workspace:** check `clients/` and `_ops/meetings/` in case Locate has spoken to this firm or person before.

Keep the link for every fact you use. Anything seen only in a search summary is labelled *(search summary only, not read)*, and anything without a source is marked *unconfirmed*.

Small firms often have almost no web presence. If research finds little, say so in one line per source (so Sam knows you looked), base "What I noticed" on the prospect's own words, and lean on market context that fits their kind of firm.

### 3. Plan the call

**Run sheet (30 minutes):**

1. *Open and set the agenda (3 min):* thank them, then set the agreement for the call: "I'd like to understand how things work at your firm, and by the end we'll both know whether it's worth me putting a proposal together. If it isn't a fit, I'll tell you." That last line builds trust and makes the qualifying feel natural.
2. *Their situation (7 min):* how the firm runs today, in their words.
3. *The problem (8 min):* where it hurts, what it costs and what they've tried.
4. *Fit and practicalities (6 min):* decision-making, budget, timing.
5. *Recap and next step (6 min):* play back what Sam heard, then book the proposal meeting or exit politely.

**Discovery questions.** Write 6–8, in the order of the run sheet, each with a follow-up probe and a short "listen for" note. Good discovery questions:

- **Ask about what has already happened, not what they'd hypothetically buy.** "Walk me through the last enquiry that came through the website. What happened next?" beats "Would faster follow-up help?"
- **Get them to put a cost on it themselves.** "Roughly how many enquiries a month don't turn into a meeting?" "How much of a broker's week goes on file work?" A cost the client names carries more weight than one Sam asserts.
- **Find out what they've tried.** Past agencies, tools or workshops show what they believe and what they'll be wary of.
- **Use Sam's research as questions, not accusations.** "I noticed your enquiry form asks for income and assets up front. Was that a deliberate choice?"

**Qualifying criteria.** List what Sam needs to learn, with green, amber and red signals.

*Marketing retainer:*
- Can they fund a result? The management fee plus ad spend they pay directly. Use the floor and the "higher of the flat fee or 15–20% of ad spend" rule from `02-pricing.md`, and the revenue proxies there (staff count, locations, already advertising).
- Is the decision-maker on the call or easy to reach?
- Will they accept the 3-month minimum and the $1,500 setup fee?
- Is there a clear outcome to measure (enquiries, booked meetings, funded loans)?

*AI training:*
- How many staff will be trained? This maps to a tier.
- Who signs off: the principal, the licence holder or an ops manager? Is the licence holder involved, since the policy is about their obligations?
- How are staff using AI now (free tools, aggregator tools, nothing), and is there a trigger such as an audit, a near-miss or an aggregator push?
- Timing: when could a half-day workshop realistically happen?

*Red flags for either* (two or more means a polite exit): asks for free work beyond a short audit, wants to "test with $200", is vague the moment budget comes up, wants lots of unrelated small jobs, or needs results Locate can't honestly promise.

**The polite exit.** Write the line Sam uses if they don't qualify. Make it honest, specific and useful, and leave the door open: "Honestly, at your current ad budget I don't think a retainer would pay for itself yet. The thing I'd do first is [one specific, free fix]. Come back to me when [condition], and I'll happily take another look."

**If they ask about price.** Give an honest range from the rate card and pricing files, not a quote: "Most firms your size land between X and Y a month, plus ad spend paid directly to Google or Meta. I'll confirm exactly in the proposal once I understand the scope." For AI training, name the tier range that fits their staff count. Then go back to discovery.

**The close.** If they qualify, write the recap and the booking line word for word: "Here's what I heard: [two or three of their problems in their words]. Does that sound right? … I'd like to come back with a proposal that tackles [the main one]. Can we lock in 30 minutes on [day] to walk through it?" Aim for within a week, avoiding public holidays where the prospect is. Offer a specific day and time plus one alternative, and book it on the call.

**Both offers.** If marketing and AI training could both fit, lead with the one they came in about. Give the other one question in the problem block and an optional line in the close, so Sam can raise it only if they put a cost on it. Two pitches in one first call dilutes both.

**Handle carefully.** Anything sensitive: they mention a current agency (no criticism of others), the prospect is a competitor of an existing client (raise it with Sam, don't hide it), or a Locate client's results would make a tempting example (only name a client or use their results if that client agreed). For AI training, the policy helps a firm meet its obligations but isn't legal or compliance sign-off, so never present it as that.

### 4. Write the brief

Use `$HOME/.claude/skills/discovery-call/assets/brief-template.html`. Sections, in order:

1. **Header:** name, role, firm, date, time, format, length, LinkedIn link.
2. **Goal:** qualify, and if they fit, book the proposal meeting. Name the offer Sam suspects fits best.
3. **The firm at a glance:** 4–6 bullets: size, licence or aggregator, how they came in, what they've said so far.
4. **What I noticed:** 2–3 observations from the research, each worded as the question Sam will ask about it.
5. **Run sheet.**
6. **Opening:** the agenda-setting line.
7. **Discovery questions:** numbered, each with a probe and a "listen for" note.
8. **Qualify:** the criteria for the likely offer, as a checklist with green, amber and red signals.
9. **If they ask about price:** the range line.
10. **The close:** recap and booking line, word for word.
11. **The polite exit:** the line, with the one free tip filled in.
12. **Handle carefully.**
13. **After the call:** the same day, send a recap email confirming the proposal meeting and what it will cover, or a short thank-you with the promised tip if it was an exit. Log the prospect in `_brand/launch/prospect-tracker.csv`. If they qualify, start the proposal from `_brand/launch/proposal-template.html`.
14. **In the media and sources:** LinkedIn first, then media features, then the firm's website, ad libraries and other sources, then any market context used, all linked.

**Writing style.** Sam's voice: plain, measured, Australian English, sentence case, no em dashes, no exclamation marks, no sales jargon. Write questions as Sam would say them.

**Numbers.** Prices and rules only from the pricing files and pitch deck. Market stats only with their source, and only if they're about this prospect's kind of firm (adviser stats aren't broker stats). No invented results or client counts.

**Where to save.** `_ops/meetings/YYYY-MM-DD-<firstname-lastname>-discovery.html`, using the call date. Example: `2026-10-28-jane-smith-discovery.html`. Create the folder if needed. Post-call notes go beside it with the same name ending in `-notes.md`.

Then in chat, give Sam the path, the offer that likely fits, the top three questions and the close.

## Before delivering, check

- Is anything in the brief really a pitch dressed up as a question? Rewrite it.
- Are the qualifying criteria specific enough to decide during the call?
- Is the polite exit honest and useful, not a brush-off?
- Does the close name a time, not "I'll send something through"?
- Are all prices from the pricing files, and all facts linked or marked unconfirmed?
