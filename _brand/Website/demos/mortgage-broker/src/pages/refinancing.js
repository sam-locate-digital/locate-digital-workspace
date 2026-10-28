// Refinancing (canvas/Refinancing.dc.html)
const { photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Refinancing | Harlow Home Loans",
  description: "Fixed rate ending or rate not reviewed in a while? A Melbourne mortgage broker checks whether refinancing is worth it, and tells you if it isn't.",
  active: "refinancing",
  drawerDefaults: {"situation":"refinance","source":"Refinancing page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
${photo({"src":"icons/refinance.webp","alt":"","width":240,"height":240,"cls":"ph-ic ill hero-in","loading":"eager"})}
<h1 class="h1 hero-in" id="ph-h">Is your home loan still working for you?</h1>
<p class="lead hero-in" style="--d: 80ms">If your fixed rate is ending, your rate hasn't been reviewed in a while, or you'd like to free up equity, we'll check whether switching is worth it. If it isn't, we'll say so.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free rate review</button>
<a class="btn btn-secondary btn-lg" href="health-check.html">Take the 2-minute health check</a>
</div>
<p class="trust hero-in" style="--d: 240ms"><span>Free review</span><span>No credit check to start</span><span>We'll tell you if it's not worth it</span></p>
</div>
<div class="phero-photo">${photo({"src":"images/refinance.jpg","alt":"A homeowner relaxed after reviewing his home loan","width":1168,"height":876,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="ex-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="ex-h">What a review <em class="ul">covers</em></h2>
<p class="lead">It's more than the rate. We look at the whole loan and what it's costing you.</p>
</div>
<ul class="hl-list rv focus" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Your loan against the market</b><p>We compare your loan with what <span class="ph">[PLACEHOLDER 30+]</span> lenders offer someone in your position.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Fees and features</b><p>Annual fees, offset accounts and redraw. Sometimes a better setup matters more than the rate.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Your current lender first</b><p>Sometimes your lender will sharpen up when asked, with no switch needed.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>The real cost of switching</b><p>Discharge fees, government fees and any break costs on a fixed loan, all counted before you decide.</p></li>
</ul>
</div>
</section>

<section class="band" aria-labelledby="tl-h">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="tl-h">How a <em class="ul">switch</em> works</h2>
<p class="lead">If refinancing makes sense, here's what happens. You keep living your life; we chase the paperwork.</p>
</div>
<ol class="tl">
<li class="rv rise" style="--d: 0ms"><span class="when">Today</span><b>Quick health check</b><p>Five questions to see whether a review is worth your time.</p></li>
<li class="rv rise" style="--d: 70ms"><span class="when">Week 1</span><b>Your review chat</b><p>We look at your loan statement and show you the options side by side.</p></li>
<li class="rv rise" style="--d: 140ms"><span class="when">Often 1 to 2 weeks</span><b>Application and approval</b><p>We lodge with the lender you choose and handle the back and forth.</p></li>
<li class="rv rise" style="--d: 210ms"><span class="when">Settlement</span><b>Lender to lender</b><p>Your old loan is paid out and the new one starts. Your home stays exactly as it is.</p></li>
<li class="rv rise" style="--d: 280ms"><span class="when">Every year</span><b>Free loan review</b><p>We check in each year so you're not left sitting on an old rate.</p></li>
</ol>
</div>
</section>

<section class="band band-w1" aria-labelledby="fx-h">
<div class="wrap schemes">
<div class="rv from-l">
<h2 class="h2" id="fx-h">When a fixed rate <em class="ul">ends</em></h2>
<p class="lead">When your fixed term finishes, your loan usually rolls onto the lender's standard variable rate. That can be higher than what they offer new customers.</p>
</div>
<div class="rv from-l" style="--d: 100ms">
<ul class="hl-list">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"></rect><path d="M3 9.5h18M8 2.5v4M16 2.5v4"></path></svg><b>Start early</b><p>Get in touch about <span class="ph">[PLACEHOLDER 90 days]</span> before your fixed rate ends, so there's time to compare and switch.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16M12 4v16"></path></svg><b>Fix again, go variable, or split</b><p>We'll explain the trade-offs of each so you can choose what lets you sleep at night.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg><b>Read the guide</b><p><a href="guides.html">What happens when your fixed rate ends</a>, in plain English.</p></li>
</ul>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"Clients who ","hBrush":"switched","hTail":"","filterKey":"situation","filterVal":"refinance"})}
</div>
</section>

<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">Refinancing <em class="ul">questions</em></h2>
<p class="lead">Short answers to what people ask before they switch.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
<details name="faq" open><summary>How often should I review my loan?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">At least once a year, and whenever a fixed rate is ending or your situation changes. Our clients get a free review every year.</p></details>
<details name="faq"><summary>Does refinancing cost anything?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">There can be discharge fees, government registration fees and, for fixed loans, break costs. We add them all up before you decide.</p></details>
<details name="faq"><summary>Can I refinance to renovate or pay off other debts?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Often, yes. We'll check your equity and whether rolling debts into your home loan makes sense, since spreading them over a longer term can mean paying more interest overall.</p></details>
<details name="faq"><summary>Will refinancing affect my credit score?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">A new application adds an enquiry to your credit file. That's why we only apply once we've found a loan that's worth switching to.</p></details>
</div>
</div>
</section>

${ctaBand(C, {"hLead":"Book your free rate ","hBrush":"review","hTail":"","sub":"Have your latest loan statement handy if you can.","prefill":{"situation":"refinance","source":"Refinancing page"}})}`,
});
