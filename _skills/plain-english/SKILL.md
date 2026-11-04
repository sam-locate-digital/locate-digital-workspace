---
name: plain-english
description: Re-explain anything complicated in plain, everyday English that a layperson can follow, with a short real-world analogy by default. Covers technical material (code, tracking, DNS, errors), processes and procedures (how something works step by step, who does what, what happens next), and jargon from any field (legal, accounting and tax, lending and finance, insurance, government, medical, marketing, contracts, industry acronyms). Use whenever Sam asks to "dumb it down", "explain it simply", "in plain English", "ELI5", "explain like I'm five", "in layman's terms", "what does that actually mean", "what's the process", "walk me through how this works", "I don't get it", "say that again but simpler", "how would I explain this to a client", or asks for an analogy. Works on Claude's previous answer, pasted text, an email, a letter, a contract clause, an error message, a file, a report section or a topic. Also use when Sam wants a version of something complicated to send to a client or anyone without the background (a mortgage broker, a tradie, a business owner, a customer), even if Sam doesn't use the word "simple".
---

# Plain English

Sam runs a marketing agency and deals with a lot of things written for insiders: tracking tags, DNS and code, but also accountant emails about BAS, contract clauses, lender and compliance rules, ad-platform policies, government forms, and multi-step processes nobody explains properly. Sam's clients are mortgage brokers, tradies and small business owners who each have their own jargon and are outside everyone else's. This skill turns the insider version into one a smart person without that background can understand in one read, and act on.

It works the same whether the complication is technical, a process, or the vocabulary of a field. The reader isn't slow, they're just not in that world.

The goal is understanding, not shorter text for its own sake. A good result leaves the reader able to answer three questions: what is this, why does it matter to me, and do I need to do anything.

## What to simplify

Work out what the reader wants explained, in this order:

1. Text Sam names, pastes or points to (a file, an email, a clause, an error, a report section).
2. Otherwise, Claude's most recent complicated answer in this conversation.
3. Otherwise, the topic or process Sam names ("explain what a CNAME record is", "how does settlement actually work", "what's the process for getting a trade licence").

If it's genuinely unclear which of several things Sam means, pick the most recent and say which one you explained in a few words at the top. Don't stop to ask.

## Who it's for

- **Default: Sam.** Explain it to Sam directly ("you"). Sam is sharp and runs a business, so skip the hand-holding, just drop the jargon.
- **A client or someone else**, when Sam says so ("so I can send it to Dave", "for the client", "how do I explain this to a broker"). Write a paste-ready message Sam can send as is: first person from Sam, warm, no internal detail the client doesn't need (file names, which tool broke, whose fault it was), and no jargon at all. Australian English spelling. Pick the analogy from the client's world (see below).

## Format

Use this shape. Skip a section when it has nothing real to say, rather than padding it.

**The short version**
One or two sentences. What it is or what happened, and why it matters. If the reader stopped here they should still get the gist.

**In plain English**
The explanation itself, in short paragraphs or a few bullets. Walk through it in the order things actually happen, cause before effect. Keep only the details that change what the reader understands or does.

**Think of it like this**
One everyday analogy (see the next section).

**What you need to do**
Concrete next steps, in plain words. If there's nothing to do, say so in one line ("Nothing. This is just so you know what changed."). Leave this section out when the material is a pure "what is X" explanation with no action in it.

For a client-facing message, drop the headings and write it as a normal short message with the same flow: gist, explanation, analogy woven in, what happens next.

### When it's a process

Processes confuse people for different reasons than technical things: too many steps, unclear order, and nobody saying who does what or how long it takes. So for a process, "In plain English" becomes numbered steps in the order they actually happen. For each step, say in plain words:

- what happens, and who does it (you, the client, the bank, the council, "we");
- roughly how long it takes, if the material says or it's well known;
- what the reader has to do or provide, if anything.

Keep it to the steps that matter to the reader. Merge the back-office steps they never see into one line ("the lender does its checks, which takes about a week"). Point out the step where things usually get stuck or go wrong, because that's what people most want to know. Use an analogy for the whole flow, not one per step.

### When it's jargon

Field jargon (legal, tax, lending, insurance, medical, government, industry acronyms) is often a normal idea dressed up. Say the normal idea. "Indemnify" becomes "you agree to cover their costs if…". "Lodge your BAS" becomes "send the tax office your quarterly GST form". If the reader will see the term again on forms or in emails, keep it once with the plain meaning beside it, so they recognise it next time. If a word has a legal or financial meaning that differs from its everyday one, say so, because that's where people get caught out.

## Writing it

- **Everyday words.** Swap jargon for what it does: "the code that tells Google someone filled in your form" instead of "the conversion tag", "the date the house officially becomes yours" instead of "settlement". If the reader will keep hearing a term (DNS, pixel, API), keep it once and define it in a few words the first time, so they recognise it next time. Don't leave an acronym unexplained, unless it's one the reader uses every day themselves (Sam knows ABN and SEO, a broker knows LVR, a tradie knows RCD).
- **Short sentences.** One idea per sentence. If a sentence needs a comma-heavy clause to work, split it.
- **Concrete over abstract.** Real numbers, real names, real examples from the material. "About 1 in 5 enquiries weren't being counted" beats "a significant tracking discrepancy".
- **Simplify, don't falsify.** Leaving out detail is fine; saying something untrue is not. If the simple version would mislead someone into a wrong decision, add the one caveat that matters, plainly.
- **Respect the reader.** Don't open with "Simply put", "Don't worry" or "Great question", don't apologise for complexity, and don't say "basically" every second line. Plain is not patronising.
- **Only as long as it needs to be.** A long technical explanation should come out shorter. A short, dense piece of jargon (a contract clause, an accountant's two-line email) may need more words than the original, because each packed phrase has to be unpacked. Either way, if it's running long, the analogy or the short version is probably doing too little work.

## The analogy

Include one by default. Leave it out only when Sam says "no analogy" or the thing is already everyday (there's no useful analogy for "the email bounced").

A good analogy:

- **Comes from the reader's world.** For Sam, anything ordinary: a shop, the post, a kitchen, a car, a house. For a mortgage broker: loan files, lenders, valuations, settlement. For a tradie: a job site, quotes, plumbing, wiring, council approvals. The closer to their day, the faster it lands.
- **Maps the parts that matter.** Don't just say "it's like a phone book". Say which part is which: "DNS is the phone book, your domain is your business name, and the server is the actual phone that rings." The mapping is where the understanding happens.
- **Is one analogy, kept short.** Two to four sentences. Stacking three analogies confuses more than it helps.
- **Admits where it breaks**, in one line, only if the gap could lead the reader astray ("Unlike a phone book, changes can take a few hours to reach everyone").

## Example

Technical original:
> The GA4 generate_lead event isn't firing because the GTM trigger listens for a form_submit dataLayer push, but the new Elementor form uses AJAX and never pushes that event, so conversions aren't recorded and Smart Bidding is optimising on incomplete data.

Plain English version:

**The short version**
Google isn't being told when people fill in your new website form, so your ads are learning from half the picture.

**In plain English**
When someone sends an enquiry through the website, a small piece of code is supposed to tell Google "that was a lead". The new form you put in sends enquiries in a slightly different way, and that piece of code doesn't notice. The enquiries still reach you fine. Google just never hears about them, so it thinks your ads are producing fewer leads than they are, and it adjusts who it shows them to based on that wrong picture.

**Think of it like this**
It's like a shop with a doorbell that counts customers. You moved the entrance, but the doorbell is still on the old door. Customers are still coming in, the counter just isn't clicking, so the owner thinks the shop is quiet and starts changing things that were working.

**What you need to do**
Nothing yet. The fix is to point the tracking at the new form, which takes about 20 minutes. After that, give Google a week or two of correct numbers before judging the ads.
