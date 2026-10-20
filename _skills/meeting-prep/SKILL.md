---
name: meeting-prep
description: Prepare Sam for an industry insight meeting, the kind where Sam is picking a contact's brain about a market, its pain points and how to break into it, and wants to leave with a clear next step or a second meeting. Interviews Sam first, researches the person and company, then writes a short brief with a run sheet, prioritised questions, a planned closing ask and a second-meeting agenda. Use whenever Sam mentions an upcoming coffee, lunch, catch-up or call with an industry contact, former colleague, BDM, lender, aggregator or association person ("prep me for my lunch with…", "what should I ask X", "I'm catching up with X on Thursday", "help me plan a meeting with…", "I want to pick X's brain"), even if Sam doesn't say "prep". Not for writing proposals, sales decks or outreach emails.
---

# Meeting prep: industry insight meetings

Sam runs Locate Digital (marketing and practical AI training for Australian financial service firms). A big part of building it is sitting down with people who know a market from the inside (former colleagues, lender distribution heads, BDMs, aggregator and association people) and learning what's really going on.

These meetings are easy to waste. They drift into a pleasant catch-up, Sam does most of the talking, and the hour ends with "we should do this again" and nothing booked. This skill exists so Sam walks in with a plan: a few questions that actually matter, a light way to test the offer without pitching, one specific ask, and a reason to meet again.

The output is a short brief Sam can read on a phone in the car park five minutes before walking in.

## Workflow

1. Interview Sam (always, before any research)
2. Research the person, the company and Sam's own workspace
3. Plan the meeting: goal, arc, questions, test, ask, meeting two
4. Write the brief (HTML, saved to the workspace) and summarise it in chat

### 1. Interview first

Research without knowing Sam's real goal produces generic questions. So ask before you look anything up. Use the AskUserQuestion tool with concrete options wherever you can (or ask in chat if it isn't available), since it is much faster for Sam than typing. Skip anything Sam already told you, and don't ask more than two rounds.

What you need:

- **Who:** name, role, company. Usually given.
- **Relationship:** how they know each other, how close, and whether the contact knows what Locate does now. This changes the opening. A close former colleague needs a catch-up and a quick "here's what I'm doing now". A loose contact needs Sam to be clear about why they asked for the meeting.
- **Format:** coffee, lunch or call, how long, date and place. Time sets how many questions fit. Lunch loses 10–15 minutes to ordering and catching up.
- **What Sam wants to learn:** the one to three themes. Push for specifics: "broker pain points" is a theme, "which admin task brokers would hand to AI first, and what stops them" is a question.
- **The win beyond learning:** intros, feedback on the offer, a channel or partnership, or genuinely nothing. This sets the closing ask. If Sam says "just learning", still plan a small ask (a single intro, or permission to follow up), because a relationship with no next step goes cold.
- **What to avoid:** topics not to raise (client work, competitors, anything confidential), and anything awkward in the history.
- **What Sam will show:** a deck, pricing, a one-pager or nothing.

### 2. Research

Start with Sam's workspace, because it holds context the web won't have:

- `clients/` and `memory/`: is the contact's company, or its parent or a sister company, a Locate client? If so, read the engagement so you know what to avoid, then **keep it out of the meeting unless Sam says otherwise.** Information from client work is confidential and stays out of conversations with other people, even people who work at the same company in a different team. If workspace files disagree about the relationship, follow what Sam said in the interview and mention the mismatch in chat.
- `_services/<service>/` for the offer being discussed (scope, pricing, pitch deck, market research). Use the deck as the source of truth for what the offer is. Never describe a service the deck doesn't include.
- Any personas or targeting notes in `_brand/launch/` or the service folder that cover this market. Skip them if they describe a different audience.
- Past briefs and `-notes.md` files for this person in `_ops/meetings/` (search by their name), so a second meeting builds on the first.

Then do a short web pass:

- The company: what it does, size, recent news (product launches, leadership changes, funding, partnerships), and its position in the market.
- The person: their current role and public professional background. Look specifically for **media features**: trade-press articles, appointment announcements, interviews, podcasts, conference talks, and quotes in industry news. These show what the person has said publicly and give Sam natural openers ("I saw your interview in…"). Stick to public, work-related information. Don't collect personal details.
- **LinkedIn:** find the person's profile (search "<name> <company> LinkedIn") and their company page. From the profile, use the career history (it often fills gaps the press leaves, such as earlier roles and how long they've been in the current one) and recent posts, articles, comments and reshares. Recent activity shows what's on their mind right now, so it's often the best source for an opener or a question ("I saw your post about…"). Note any shared employers or obvious mutual ground with Sam. LinkedIn often blocks reading without a login. If you can't open the profile, include the link anyway, say what you couldn't see, and suggest Sam skim the profile and the last month of activity before the meeting. If search doesn't turn up the profile at all, link a LinkedIn people search instead (`https://www.linkedin.com/search/results/people/?keywords=<First>%20<Last>%20<Company>`), which opens straight to them once Sam is logged in. Don't guess a profile URL.
- The market topic: anything recent and public that would make a good question ("I saw X announced Y. Is that changing how brokers…").

**Keep the link for everything you find.** Every media feature and every fact that comes from the web goes into the brief with its URL, so Sam can open and read the original before the meeting. If you only saw something in a search result summary and didn't open the page, still include the link, but label it *(search summary only, not read)*. If a claim has no link, Sam can't check it, so mark it *unconfirmed*. A wrong "fact" said out loud over lunch costs more than leaving it out.

### 3. Plan the meeting

**One-line goal and win condition.** Example: "Leave knowing which admin task advisers most want off their plate, with an honest reaction to the offer and one intro to a practice principal." The win condition is the concrete version: what Sam must walk out with for the meeting to have worked.

**The arc.** Insight meetings go best in this order, because trust comes before questions and questions come before the ask:

1. *Reconnect:* genuine catch-up, about them first.
2. *Frame:* one or two sentences on what Sam is doing and why they wanted this person's view. Keep it to the length of a sentence said across a table, not a pitch.
3. *Learn:* the main block, around half the time. The contact talks; Sam listens and probes.
4. *Test:* briefly show or describe the offer and ask for an honest reaction.
5. *Ask:* the closing ask.
6. *Bridge:* float meeting two and agree how to follow up.

Give each block a time budget that fits the format.

**Questions.** This is the part that makes or breaks the meeting. Good insight questions:

- **Ask about what has happened, not what might happen.** "When did a broker last complain to you about admin, and what was it about?" gets real information. "Would brokers pay for AI training?" gets politeness. People are bad at predicting what they'd buy and good at describing what's already happened.
- **Use their vantage point.** A head of distribution sees hundreds of brokers. Ask what they see across many ("What separates the brokers who grew this year from the ones who didn't?"), not what they personally want.
- **One question at a time, open-ended, in plain words.** Write them the way Sam would actually say them at a lunch table.
- **Each must-ask question gets one or two follow-up probes.** The first answer is usually the polite version. "What does that look like day to day?" or "Who handles that at a typical brokerage?"
- **Note what a good answer would change.** For each must-ask question, add a short "listen for" note so Sam knows which answers matter (for example, a named task, a person who owns the budget, a trigger event).

Split them into **must-ask** (4–6, in priority order, so if the meeting runs short the important ones are already covered) and **if there's time** (3–4).

**Testing the offer without pitching.** If Sam wants feedback, plan it as a question, not a presentation: one sentence describing the offer, then "What's your honest reaction?" and "What would make a broker say no?" Bring the details (price tiers, what's included) but only share them if asked. The aim is criticism Sam can use, so make it easy to give: "You won't offend me. I'd rather hear it from you than from 20 brokers who don't call back."

**The closing ask.** One specific, easy-to-say-yes-to ask, written out word for word, plus a smaller fallback if the first gets a soft no. Good asks are concrete: "Could you think of two brokers who'd give me 20 minutes? I'll send you a two-line blurb to forward." Bad asks are vague: "Let me know if you think of anyone." Time the ask after the contact has been helpful and is warm, usually after the test block.

**Setting up meeting two.** Sketch a short agenda for a second meeting that gives the contact a reason to come back: show them what Sam did with their advice, report back on the intros, or get their view on a revised offer. Write the line Sam uses to float it ("Once I've spoken to those brokers, can I come back and show you what I heard?"). It's easier to agree to a second meeting when it's about reporting back than when it's just "catch up again".

**Handle carefully.** List what not to raise, and a calm, honest holding line in case the contact brings it up anyway. Holding lines deflect without lying: "That's a separate piece of work, and I keep those separate. Today I'm really interested in the broker side."

### 4. Write the brief

Use `$HOME/.claude/skills/meeting-prep/assets/brief-template.html` as the structure and styling. Fill every section and delete any that don't apply. Aim for something Sam can read in five minutes: at most about two printed pages. If it runs long, cut background and the "if there's time" questions first, never the must-asks, the ask or the handle-carefully section.

Sections, in order:

1. **Header:** who, role and company, date, time, place, length, and a link to their LinkedIn profile.
2. **Goal:** the one-line goal and the win condition.
3. **Who they are:** 3–5 bullets: role, what they see from where they sit, relationship history (only what Sam told you; keep it general rather than guess), anything recent worth mentioning. Link each web fact inline to its source, for example (<a href="…">Australian Broker, 5 Mar 2026</a>).
4. **Run sheet:** the six blocks with time budgets.
5. **Opening:** a natural first line for the frame block (not a script for the whole meeting).
6. **Must-ask questions:** numbered, each with probes and a "listen for" note.
7. **If there's time:** the shorter list.
8. **Test the offer:** the one-sentence description, the reaction questions, and key facts to have ready.
9. **The ask:** primary ask word for word, plus the fallback.
10. **Meeting two:** the line to float it and a 3–4 point agenda.
11. **Handle carefully:** topics to avoid, with holding lines.
12. **After the meeting:** a short checklist: send the thank-you (with the intro blurb if the ask landed) the same day, note the three most useful things said, and lock in the meeting two date.
13. **In the media and sources:** every link you used. LinkedIn comes first (profile, plus any recent posts worth reading, each with a one-line note), then media features about the person, each with the publication, date and a one-line note on what it says, plus "worth reading before the meeting" on the one or two that matter most. Then company and market sources. Label anything you only saw in a search summary. If you found no media features for the person, say so in one line, so Sam knows you looked.

**Writing style.** Sam's voice: plain, measured, Australian English, sentence case, no em dashes, no exclamation marks, no sales jargon. Write questions as spoken sentences. The brief is for Sam's eyes only, so it can be direct ("Don't mention the Brighten marketing work").

**Numbers.** Only use figures from Sam's files (pitch deck, market research) or sources you checked, and keep the source in brackets so Sam can say where a number comes from if asked. Don't invent stats to make a question land. Sam's own decks count as a source but aren't automatically right: if a deck figure has no underlying source, describes a different audience (advisers rather than brokers, say), or may be out of date, say so in the brief and suggest softer wording. A press claim you only saw in search results stays marked *unconfirmed*, even inside a question.

**Where to save.** All briefs go in one folder, `_ops/meetings/`, so Sam has a single place to find every meeting. The file name carries the context:

`_ops/meetings/YYYY-MM-DD-<firstname-lastname>-<topic>.html`

- `YYYY-MM-DD` is the meeting date, not the day the brief was written, so the folder sorts by meeting date.
- `<topic>` is a short slug for the work the meeting serves: the service folder name (`ai-adoption`), the client folder name in lowercase (`mosic`), or a short topic (`partnerships`) if neither fits.
- If a client relationship has to stay out of the conversation, use the topic the meeting is actually about, not that client's name, so the file name doesn't link the two. Example: `2026-10-22-chris-meaker-ai-adoption.html`.

Create `_ops/meetings/` if it doesn't exist. Post-meeting notes go in the same folder with the same name ending in `-notes.md`.

Then in chat, give Sam the path plus a short summary: the goal, the top three questions and the ask. That lets Sam react before opening the file.

## Before delivering, check

- Could Sam ask the must-ask questions out loud, word for word, without sounding scripted or salesy?
- Is any question really a pitch dressed up as a question? Rewrite it.
- Does the time budget fit the format, including the catch-up?
- Is the ask specific enough that the contact knows exactly what to do next?
- Is anything from confidential client work (the contact's company, its parent or sister companies) in the brief as a talking point? Take it out.
- Are all figures sourced and all unconfirmed facts marked?
- Does every web fact link to its source, and does the sources section list every media feature you found about the person?
