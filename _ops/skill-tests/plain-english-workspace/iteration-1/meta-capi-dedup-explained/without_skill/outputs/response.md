Short version: **Meta is counting every lead twice, so the ads look about twice as good as they really are.**

Here's what's going on.

**Two ways of reporting a lead**

When someone fills in the form, the website tells Meta about it in two ways:

1. **The Pixel**: a bit of code in the person's browser that says "hey Meta, someone just became a lead."
2. **The Conversions API (CAPI)**: the website's server sends Meta the same message directly.

Sending both is normal and a good idea. If one gets blocked (ad blockers, iPhone privacy settings and so on), the other still gets through.

**The catch**

Meta needs some way to know those two messages are about the **same person**. Otherwise it reads them as two different leads.

That's the job of the `event_id`. Think of it as a receipt number. If both messages carry receipt #12345, Meta knows it's one lead and throws the duplicate away.

At the moment the two messages don't carry the same receipt number. So Meta can't match them, and it counts both.

**What the numbers mean**

- **Dedup rate 3%**: Meta only managed to match and remove duplicates 3% of the time. Nearly everything is being double counted.
- **Event Match Quality 7.8**: this one is fine. It measures how well Meta can tell *who* the lead is (email, phone and so on). Nothing to fix there.

**Why it matters**

- **Cost per lead looks half what it really is.** If the dashboard says $30 a lead, the real number is closer to $60. The client's results look better on paper than they are.
- **Meta is learning from bad data.** The campaign thinks it's getting twice as many leads as it is, so it makes its decisions (who to show ads to, where to spend) based on numbers that are wrong.

**The fix**

When someone submits the form, create one ID for that submission and send that same ID with both messages: the Pixel one (the `fbq()` code in the browser) and the server one (CAPI). Then Meta can match them and count each lead once.

This is a job for whoever looks after the website or tracking setup. It's usually a small change.

**One heads up:** once it's fixed, the lead count in Meta will drop by about half and the cost per lead will roughly double, practically overnight. Nothing has actually got worse. You're just seeing the real numbers for the first time. It's worth telling the client before it happens so it doesn't look like the campaign suddenly fell over.
