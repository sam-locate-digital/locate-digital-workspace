Here's a version you can send Priya. It owns the mistake and keeps the tech out of it:

---

Hi Priya,

Thanks for flagging this, and sorry for the hassle.

Here's what happened. Your website has a security certificate. It's what puts the padlock next to your web address and tells browsers the site is safe to visit. It's meant to renew itself automatically. When we moved your site to its new hosting recently, one of the settings still pointed at the old host, so the renewal didn't go through and the certificate ran out at 9:14am yesterday.

When that happens, browsers play it safe. Anyone visiting saw a security warning instead of your site, and they couldn't click past it. Your site wasn't hacked and none of your or your clients' information was exposed. The browser was just refusing to load the page until the certificate was current again.

We fixed the setting and renewed the certificate by hand, and the site was back up at 11:20am. So it was down for about two hours.

That one's on us, since it came out of the move. To stop it happening again, we've set up monitoring that checks your site around the clock. It also warns us two weeks before the certificate is due to expire, so we'll catch any renewal problem well before it affects you.

If anyone mentions they had trouble reaching you yesterday morning, that's why. Happy to jump on a quick call if you'd like to talk it through.

Cheers,
Sam

---

A few things to check before you send it:

- **Lost enquiries.** Anyone who tried to book or fill in a form between 9:14 and 11:20 got blocked. If she was running ads in that window, the clicks were wasted. Check how much that was. Offering a credit for it, or at least mentioning it, will earn you a lot of trust.
- **"Nothing was exposed."** That's true for an expired certificate, because the warning stopped people loading the site at all. Only leave it in if nothing else went wrong during the migration.
- **Owning it.** I've written it as your mistake, because the migration caused it. If you'd rather keep it more neutral, change "That one's on us, since it came out of the move" to "It was a hiccup from the hosting move." I'd keep it as it is, though. Clients usually respect a straight answer more than a vague one.

If she'd rather get a text, here's a short version:

> Hi Priya, sorry about yesterday. When we moved your site to its new hosting, the security certificate (the padlock bit) didn't renew properly, so browsers showed a warning and blocked visitors from about 9:15 to 11:20am. Nothing was hacked or exposed. It's fixed, and we've added monitoring that warns us weeks ahead so it won't happen again. Happy to chat if you have any questions.
