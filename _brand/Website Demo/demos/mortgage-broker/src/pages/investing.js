// Investment loans (canvas/Investing.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Investment loans | Harlow Home Loans",
  description: "Investment property loans set up properly from the start. A Melbourne mortgage broker for property investors.",
  active: "investing",
  drawerDefaults: {"situation":"invest","source":"Investing page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
${photo({"src":"icons/invest.webp","alt":"","width":240,"height":240,"cls":"ph-ic ill hero-in","loading":"eager"})}
<h1 class="h1 hero-in" id="ph-h">Investment loans, set up properly from the start</h1>
<p class="lead hero-in" style="--d: 80ms">Whether it's your first investment property or your next, how the loan is structured can matter as much as the property. We'll set it up with your accountant in the loop.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
<p class="trust hero-in" style="--d: 240ms"><span>Free 20-minute chat</span><span>No credit check</span><span>Happy to work with your accountant</span></p>
</div>
<div class="phero-photo">${photo({"src":"images/invest.jpg","alt":"A woman looking at new townhouses as an investment","width":1168,"height":876,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="ex-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="ex-h">What we'll <em class="ul">look</em> at</h2>
<p class="lead">The loan should suit this purchase and leave room for the next one.</p>
</div>
<ul class="hl-list rv focus" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>What you can borrow for an investment</b><p>Lenders count rental income differently. We know which ones suit your plans.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Interest only or principal and interest</b><p>We explain how each works with different lenders, so you can talk it through with your accountant.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Using equity from your home</b><p>Split loans keep your home debt and investment debt separate and easy to track.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Your next purchase, not just this one</b><p>We set up today's loan so it doesn't get in the way of your next step.</p></li>
</ul>
</div>
</section>

<section class="band" aria-labelledby="tl-h">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="tl-h">From idea to <em class="ul">tenants</em></h2>
<p class="lead">The usual path for an investment purchase. Timings depend on you, the lender and the property.</p>
</div>
<ol class="tl">
<li class="rv rise" style="--d: 0ms"><span class="when">Now</span><b>Set your goals</b><p>Growth, income or both. Your accountant or adviser can help with the strategy.</p></li>
<li class="rv rise" style="--d: 70ms"><span class="when">Week 1</span><b>Your free chat</b><p>We work out your borrowing range, equity and the right loan structure.</p></li>
<li class="rv rise" style="--d: 140ms"><span class="when">Often 1 to 2 weeks</span><b>Pre-approval</b><p>So you can make offers knowing the finance is lined up.</p></li>
<li class="rv rise" style="--d: 210ms"><span class="when">When you find it</span><b>Contract and valuation</b><p>The lender values the property; we keep things moving with your conveyancer.</p></li>
<li class="rv rise" style="--d: 280ms"><span class="when">Settlement</span><b>Ready for tenants</b><p>Your loan is live and set up as planned. We review it with you every year.</p></li>
</ol>
</div>
</section>

<section class="band band-w1" aria-labelledby="ad-h">
<div class="wrap schemes">
<div class="rv from-l">
<h2 class="h2" id="ad-h">Finance, not tax <em class="ul">advice</em></h2>
<p class="lead">We arrange the loan. Your accountant or financial adviser should advise on tax and whether a property suits your goals. We're happy to work alongside them.</p>
</div>
<ul class="hl-list rv from-l" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3"></circle><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"></path><path d="M16 4.5a3 3 0 0 1 0 6M21 20c0-2.8-1.6-5-4-5.8"></path></svg><b>Bring your accountant in</b><p>Invite them to your chat, or we'll send them the loan structure to check.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"></rect><path d="M8 8h8M8 12h8M8 16h5"></path></svg><b>Everything in writing</b><p>You get a summary of the recommended loan, why we chose it and the trade-offs.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 4l9 6.5"></path><path d="M5 9.5V20h14V9.5"></path></svg><b>Trusts and SMSFs</b><p>Some lenders allow these, with extra paperwork. We'll tell you who does.</p></li>
</ul>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What investors ","hBrush":"say","hTail":"","filterKey":"situation","filterVal":"invest"})}
</div>
</section>

<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">Investor <em class="ul">questions</em></h2>
<p class="lead">General information to get you started. Your accountant can advise on tax.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
<details name="faq" open><summary>Can I use the equity in my home?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Often, yes. Many investors use equity instead of a cash deposit. We'll show you how much is realistic and how to keep the debts separate.</p></details>
<details name="faq"><summary>Interest only or principal and interest?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Interest only keeps repayments lower for a set time, but you don't pay the loan down and repayments rise later. Your accountant can advise on what suits your tax position; we'll explain how each lender treats it.</p></details>
<details name="faq"><summary>How do lenders count rental income?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Most count only part of the expected rent, to allow for vacancies and costs. Each lender does it differently, which is one reason we compare them.</p></details>
<details name="faq"><summary>Can I buy in a trust or an SMSF?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Some lenders allow it, with extra documents. Get advice on the structure first; we'll then find lenders who accept it.</p></details>
</div>
</div>
</section>

${ctaBand(C, {"hLead":"Talk through your next ","hBrush":"investment","hTail":"","sub":"Bring your questions, and your accountant if you like.","prefill":{"situation":"invest","source":"Investing page"}})}`,
});
