**The short version**
Meta is counting every lead twice. So the ads look about twice as good as they really are, and Meta is learning from those inflated numbers.

**In plain English**
When someone fills in the form, Meta gets told about it in two ways:

- **From the person's browser.** This is the Pixel, a small piece of code on the website.
- **From the website's server.** This is the Conversions API (CAPI), a direct back-end connection to Meta. It's a backup, because browsers and ad blockers often stop the first message getting through.

Sending both is normal and good. To stop Meta counting one lead twice, each message is meant to carry the same reference number (the "event_id"). Meta sees two messages with the same number and counts one lead.

On this setup the two messages aren't getting the same reference number. Meta can only match about 3 in every 100 pairs. It treats the rest as two separate leads.

That has two knock-on effects:

- **The reports are wrong.** If Meta shows 40 leads at $25 each, the real figure is closer to 20 leads at $50 each.
- **The ads are learning from bad numbers.** Meta decides who to show the ads to based on what it thinks is working. Right now it's working from a picture where everything looks twice as successful.

The "Event Match Quality is 7.8" part is fine and isn't the problem. That score is about how well Meta can work out who the person was. The problem is only the double counting.

**Think of it like this**
Picture a shop where every sale gets written down twice: once at the till, and once by the warehouse when the stock goes out. That's fine if both notes have the same order number, because the bookkeeper can see they're the same sale and count it once. Here the order numbers don't match, so the bookkeeper counts every sale twice. The owner thinks the shop is doing double the trade, and starts making decisions on that.

**What you need to do**
1. **Get the fix done.** When someone submits the form, the website should create one reference number and attach it to both messages. Whoever manages the tracking (Tag Manager or the site developer) can do this. It's a small job.
2. **Don't judge the campaign on current numbers.** Mentally halve the leads and double the cost per lead until the fix is in.
3. **Expect the numbers to "drop" once it's fixed.** Leads will roughly halve and cost per lead will roughly double overnight. Nothing got worse. It's the true figure showing up. If the client watches these reports, tell them before it happens.
4. **Give it a week or two after the fix** before changing budgets or targeting, so Meta can relearn from correct numbers.
