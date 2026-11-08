**The short version**
Vercel has the demo site ready, but the internet doesn't yet know that demo.locatedigital.io should go to Vercel. You need to add one line in your domain settings at IONOS. Vercel will do the rest by itself.

**In plain English**
- Your domain, locatedigital.io, is managed at IONOS. IONOS holds the list that tells the internet where each address goes. That list is called DNS (the internet's address book).
- "demo" is a subdomain: an extra address that sits in front of your main domain. Right now the address book has no proper entry for it, so Vercel says it's "not configured".
- Vercel is asking you to add an entry of a type called CNAME. A CNAME means "this address lives wherever that other address lives". Here it says: demo → cname.vercel-dns.com, which is Vercel's own address.
- If there's already an entry for "demo" at IONOS, delete it first. Two entries for the same name clash, and the new one won't work.
- Once it's saved, the change spreads out across the internet. Vercel says it can take up to 48 hours, but that's the worst case. It's usually minutes to an hour or two.
- When Vercel sees the change, it sets up SSL by itself. SSL is the padlock in the browser that makes the address start with https. Let's Encrypt is just the free service that issues it. You don't have to do anything for this part.

**Think of it like this**
It's like the directory at the front of an office building. locatedigital.io is the building. "demo" is a new tenant name you're adding to the board. The CNAME is the line next to it saying "go to Vercel's floor". Until that line is on the board, visitors arrive and can't find the office. Unlike a real board, the change takes a little while to show up for everyone.

**What you need to do**
1. Log in to IONOS and open the DNS settings for locatedigital.io.
2. Look for any existing record with the name "demo". If there is one, delete it.
3. Add a new record:
   - Type: **CNAME**
   - Name (IONOS may call it "Host name"): **demo**
   - Value (IONOS may call it "Points to"): **cname.vercel-dns.com**
   - Leave the TTL (how long other computers remember the old entry) at its default.
4. Save, then go back to the domain page in Vercel. It checks by itself. Once the warning turns into a green tick, the site is live at demo.locatedigital.io with the padlock.

If it's still showing the error after a few hours, take a screenshot of the IONOS DNS page and send it through, and I'll check the entry.
