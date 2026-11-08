Yep, it's simpler than it sounds. Vercel is basically saying: "I'm ready to host demo.locatedigital.io, but the internet doesn't know to send people to me yet. Go and tell it."

**What's actually going on**

Your domain (locatedigital.io) is registered somewhere, like GoDaddy, Cloudflare, Namecheap, VentraIP or Crazy Domains. Wherever that is, there's a settings page called "DNS" that works like a phone book for your domain. It tells the internet where each address should go.

Right now that phone book has no entry for "demo", so anyone who types in demo.locatedigital.io gets nowhere. You need to add one line that says "demo goes to Vercel".

**What to do (about 5 minutes)**

1. Log in to wherever you bought locatedigital.io.
2. Find the DNS settings. It might be called "DNS", "Manage DNS", "DNS Records" or "Zone Editor".
3. Have a quick look for any existing record where the name is `demo`. If there is one, delete it. (This is the "remove it first" bit. There probably isn't one.)
4. Add a new record and fill it in like this:
   - **Type:** CNAME
   - **Name** (sometimes called Host): `demo`
   - **Value** (sometimes called Points to or Target): `cname.vercel-dns.com`
   - **TTL:** leave it on whatever the default is
5. Save.

That's it. Don't touch any of the other records in there, because they run your main website and your email.

**What happens next**

- **The wait:** it usually starts working within about 10 to 30 minutes. Vercel says "up to 48 hours" to cover itself, but it's rarely that long.
- **You don't need to go back to Vercel:** it keeps checking on its own. Once it sees the new record, the red "Invalid Configuration" turns green.
- **The SSL bit:** that's just the padlock in the browser, the thing that makes it https instead of "Not secure". Vercel sets that up for free automatically. Nothing for you to do.

**Two things that commonly trip people up**

- **Typing the full domain in the Name box.** Just put `demo`, not `demo.locatedigital.io`. Most providers add the rest for you, and if you type the whole thing you can end up with demo.locatedigital.io.locatedigital.io.
- **If you're on Cloudflare,** you'll see a little orange cloud next to the record. Click it so it turns grey ("DNS only"). Vercel works better with it off.

If you tell me where the domain is registered, I can give you the exact clicks for that provider. Or send me a screenshot of the DNS page once you've added it and I'll check it's right.
