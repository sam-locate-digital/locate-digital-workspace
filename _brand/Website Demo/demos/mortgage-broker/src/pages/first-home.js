// First home buyers (canvas/FirstHome.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "First home buyers | Harlow Home Loans",
  description: "Buying your first home in Melbourne, step by step. Deposits, schemes, pre-approval and auction day, with a Melbourne mortgage broker.",
  active: "buying",
  drawerDefaults: {"situation":"first-home","source":"First home page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
${photo({"src":"icons/first-home.webp","alt":"","width":240,"height":240,"cls":"ph-ic ill hero-in","loading":"eager"})}
<h1 class="h1 hero-in" id="ph-h">Buying your first home, step by step</h1>
<p class="lead hero-in" style="--d: 80ms">From working out your deposit to auction day, we'll walk you through every form and find a lender that fits. Usually at no cost to you.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
<p class="trust hero-in" style="--d: 240ms"><span>Free 20-minute chat</span><span>No credit check</span><span>Evening and Saturday times</span></p>
</div>
<div class="phero-photo">${photo({"src":"images/first-home.jpg","alt":"First home buyers holding their new keys","width":1168,"height":876,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="ex-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="ex-h">What to <em class="ul">expect</em></h2>
<p class="lead">No jargon and no pressure. Here's what working with us looks like.</p>
</div>
<ul class="hl-list rv focus" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>A clear answer on what you could borrow</b><p>In your first chat we work out a realistic price range, so you only look at homes you can actually buy.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Help with your deposit</b><p>We look at your savings, any family help and which lower-deposit options you may qualify for.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Pre-approval before you bid</b><p>We handle the application and the paperwork, so you can make offers or bid at auction with confidence.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>One person from start to finish</b><p>Your broker stays with you through approval and settlement, then checks your loan every year.</p></li>
</ul>
</div>
</section>

<section class="band" aria-labelledby="tl-h">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="tl-h">From savings to <em class="ul">settlement</em></h2>
<p class="lead">The usual path for a first home in Melbourne. Timings depend on you, the lender and the property.</p>
</div>
<ol class="tl">
<li class="rv rise" style="--d: 0ms"><span class="when">Now</span><b>Get ready</b><p>Check your savings, tidy up credit cards and gather your payslips. We'll tell you what lenders look for.</p></li>
<li class="rv rise" style="--d: 70ms"><span class="when">Week 1</span><b>Your free chat</b><p>We work out your borrowing range, your deposit and which schemes may apply.</p></li>
<li class="rv rise" style="--d: 140ms"><span class="when">Often 1 to 2 weeks</span><b>Pre-approval</b><p>We compare lenders, lodge the application and keep you posted along the way.</p></li>
<li class="rv rise" style="--d: 210ms"><span class="when">When you find it</span><b>Offer or auction day</b><p>We check the contract dates with you and confirm the lender is ready to go.</p></li>
<li class="rv rise" style="--d: 280ms"><span class="when">Settlement day</span><b>Keys in hand</b><p>We line up settlement with your conveyancer, then review your loan every year.</p></li>
</ol>
</div>
</section>

<section class="band band-w1" aria-labelledby="sc-h">
<div class="wrap schemes">
<div class="rv from-l">
<h2 class="h2" id="sc-h">We'll check which <em class="ul">schemes</em> fit</h2>
<p class="lead">Help for first home buyers changes often, and the rules depend on the property, the price and your situation. We'll check what you're eligible for and what it means for your deposit.</p>
<p class="note" style="margin-top: 20px">[PLACEHOLDER] Confirm current scheme names and rules before this page goes live.</p>
</div>
<ul class="hl-list rv from-l" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 4l9 6.5"></path><path d="M5 9.5V20h14V9.5"></path></svg><b>Home Guarantee Scheme</b><p>An Australian Government scheme that can let eligible buyers purchase with a smaller deposit and no lenders mortgage insurance.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h16"></path><path d="M6 20V10l6-5 6 5v10"></path><path d="M10 20v-5h4v5"></path></svg><b>First Home Owner Grant</b><p>A Victorian grant for eligible buyers of a new home, or for building one.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M8 8h8M8 12h8M8 16h5"></path></svg><b>Stamp duty exemptions and concessions</b><p>Victoria offers relief for some first home buyers, depending on the price and how you'll use the home.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3"></circle><circle cx="17" cy="9" r="2.5"></circle><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"></path><path d="M15 14.5c2.8 0 5 2.2 5 5"></path></svg><b>Family guarantee</b><p>Some lenders let a parent's home equity stand in for part of your deposit. We explain the risks to everyone first.</p></li>
</ul>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What first home buyers ","hBrush":"say","hTail":"","filterKey":"situation","filterVal":"first-home"})}
</div>
</section>

<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">First home <em class="ul">questions</em></h2>
<p class="lead">The things people ask us most before their first purchase.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
<details name="faq" open><summary>How much deposit do I need?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Often 5 to 20% of the price. With a smaller deposit you may pay lenders mortgage insurance, unless a scheme or a family guarantee applies. We'll check your options.</p></details>
<details name="faq"><summary>Can I get pre-approval before I find a place?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Yes, and we recommend it. Pre-approval shows what you can spend and helps you move quickly. It isn't a final approval, so the lender still checks the property later.</p></details>
<details name="faq"><summary>What other costs should I plan for?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Stamp duty (unless you're exempt), conveyancing, building and pest inspections, lender fees and moving costs. We'll give you a list for your situation.</p></details>
<details name="faq"><summary>Can my parents help?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Yes. A family guarantee uses some of their home's equity as extra security. It's a big decision for them, so we explain the risks to everyone before anyone signs.</p></details>
<details name="faq"><summary>What happens on auction day?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">We make sure your pre-approval is current and you know your limit. If you win, you'll usually pay the deposit on the day, so we plan for that early.</p></details>
</div>
</div>
</section>

${ctaBand(C, {"hLead":"Start with a free ","hBrush":"chat","hTail":"","sub":"Tell us a little about your plans and we'll take it from there.","prefill":{"situation":"first-home","source":"First home page"}})}`,
});
