// Buying your next home (canvas/NextHome.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Buying your next home | Harlow Home Loans",
  description: "Upsizing or moving in Melbourne? Bridging finance, buying before you sell and using your equity, explained by a Melbourne mortgage broker.",
  active: "buying",
  drawerDefaults: {"situation":"next-home","source":"Next home page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
${photo({"src":"icons/next-home.webp","alt":"","width":240,"height":240,"cls":"ph-ic ill hero-in","loading":"eager"})}
<h1 class="h1 hero-in" id="ph-h">Your next home, with less juggling</h1>
<p class="lead hero-in" style="--d: 80ms">Buying before you sell, bridging finance and using the equity you've built. We'll plan the timing so you're not paying for two homes for longer than you need to.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
<p class="trust hero-in" style="--d: 240ms"><span>Free 20-minute chat</span><span>No credit check</span><span>Evening and Saturday times</span></p>
</div>
<div class="phero-photo">${photo({"src":"images/next-home.jpg","alt":"A family exploring the backyard of their next home","width":1168,"height":876,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="ex-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="ex-h">What we'll <em class="ul">sort</em> out</h2>
<p class="lead">Moving is busy enough. We take the finance side off your plate.</p>
</div>
<ul class="hl-list rv focus" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>How much equity you can use</b><p>We estimate what your current home could free up and what that means for your next purchase.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Buy first or sell first</b><p>We talk through both, including bridging finance, so you can choose with your eyes open.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Keeping the features you rely on</b><p>Offset accounts, redraw and split loans, carried over or set up fresh.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Settlement dates that line up</b><p>We work with your conveyancer and agent so the two settlements don't clash.</p></li>
</ul>
</div>
</section>

<section class="band" aria-labelledby="tl-h">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="tl-h">From first chat to <em class="ul">moving</em> day</h2>
<p class="lead">The usual path when you're selling one home and buying another. Timings depend on you, the lender and both properties.</p>
</div>
<ol class="tl">
<li class="rv rise" style="--d: 0ms"><span class="when">Now</span><b>Work out your equity</b><p>A rough value for your home, what you owe, and what that leaves to work with.</p></li>
<li class="rv rise" style="--d: 70ms"><span class="when">Week 1</span><b>Your free chat</b><p>We compare selling first, buying first and bridging, with the costs of each.</p></li>
<li class="rv rise" style="--d: 140ms"><span class="when">Often 1 to 2 weeks</span><b>Pre-approval</b><p>Approval for the next place, so you know your limit before you make an offer.</p></li>
<li class="rv rise" style="--d: 210ms"><span class="when">Sale and purchase</span><b>Two contracts, one plan</b><p>We check both settlement dates and line up the lender for each.</p></li>
<li class="rv rise" style="--d: 280ms"><span class="when">Settlement</span><b>Move in</b><p>Any bridging loan closes when your sale settles. Then we review your loan every year.</p></li>
</ol>
</div>
</section>

<section class="band band-w1" aria-labelledby="bs-h">
<div class="wrap">
<div class="intro rv from-l">
<h2 class="h2" id="bs-h">Sell first or buy <em class="ul">first</em>?</h2>
<p class="lead">There's no single right answer. Here's how the two paths compare, before we look at your numbers.</p>
</div>
<div class="grid-2">
<div class="rv from-l" style="--d: 60ms">
<p class="h3" style="margin-bottom: 8px">Selling first</p>
<ul class="hl-list">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg><b>You know your budget</b><p>The sale price is locked in before you buy, so there's no guessing.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path></svg><b>You may need somewhere to stay</b><p>If you haven't found the next place by settlement, you may rent for a while or negotiate a longer settlement.</p></li>
</ul>
</div>
<div class="rv from-l" style="--d: 140ms">
<p class="h3" style="margin-bottom: 8px">Buying first, with bridging finance</p>
<ul class="hl-list">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg><b>You don't miss the right place</b><p>You can buy when you find it, then sell without rushing.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path></svg><b>You carry two loans for a while</b><p>Interest builds up during the bridging period, and the lender sets a time limit to sell.</p></li>
</ul>
</div>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"Families who've ","hBrush":"moved","hTail":" up","filterKey":"situation","filterVal":"next-home"})}
</div>
</section>

<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">Next home <em class="ul">questions</em></h2>
<p class="lead">What people ask us most when they're moving on.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
<details name="faq" open><summary>What is bridging finance?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">A short-term loan that covers the gap when you buy your next home before your current one sells. It usually ends when your sale settles, and the lender sets a time limit to sell.</p></details>
<details name="faq"><summary>How much of my equity can I use?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">It depends on your home's value, what you still owe and each lender's limits. We'll get an estimate of value and show you what's realistic.</p></details>
<details name="faq"><summary>Should I sell first or buy first?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Selling first gives you certainty about your budget. Buying first means you don't miss the right place. We'll walk through the costs and risks of both for your situation.</p></details>
<details name="faq"><summary>Can I stay with my current lender?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Sometimes that's simplest. We'll compare it with other lenders so you can see whether staying put still makes sense.</p></details>
</div>
</div>
</section>

${ctaBand(C, {"hLead":"Let's plan your ","hBrush":"move","hTail":"","sub":"Tell us where you're at with selling and buying.","prefill":{"situation":"next-home","source":"Next home page"}})}`,
});
