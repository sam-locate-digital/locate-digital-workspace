// Construction loans (canvas/Building.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Construction loans | Harlow Home Loans",
  description: "Building a home in Melbourne? Construction loans, progress payments and building contracts explained by a Melbourne mortgage broker.",
  active: "buying",
  drawerDefaults: {"situation":"building","source":"Building page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
${photo({"src":"icons/settle.webp","alt":"","width":240,"height":240,"cls":"ph-ic ill hero-in","loading":"eager"})}
<h1 class="h1 hero-in" id="ph-h">Building a home, financed in stages</h1>
<p class="lead hero-in" style="--d: 80ms">A construction loan pays your builder in stages as the work gets done. We'll help you set it up, check the contract timing and keep the payments moving.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
<p class="trust hero-in" style="--d: 240ms"><span>Free 20-minute chat</span><span>No credit check</span><span>Land, packages and knockdown rebuilds</span></p>
</div>
<div class="phero-photo">${photo({"src":"images/next-home.jpg","alt":"A family exploring the backyard of their next home","width":1168,"height":876,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="ex-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="ex-h">What we'll <em class="ul">handle</em></h2>
<p class="lead">Building has more moving parts than buying. We keep the finance side simple.</p>
</div>
<ul class="hl-list rv focus" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Land and build, together or apart</b><p>Buying land first, a house and land package, or a knockdown rebuild, we structure it to match.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Progress payments</b><p>The lender pays your builder at each stage. We explain what happens and when.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Contract and plans the lender will accept</b><p>Lenders usually want a fixed-price contract and approved plans. We check the paperwork early.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Any first home help</b><p>Building a new home can open up grants or concessions. We'll check what you're eligible for.</p></li>
</ul>
</div>
</section>

<section class="band" aria-labelledby="tl-h">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="tl-h">How progress payments <em class="ul">work</em></h2>
<p class="lead">A typical build is paid out in stages like these. Your builder's contract sets the exact stages and amounts.</p>
</div>
<ol class="tl">
<li class="rv rise" style="--d: 0ms"><span class="when">Stage 1</span><b>Base</b><p>The slab or footings are down. The lender inspects or checks the builder's invoice, then pays.</p></li>
<li class="rv rise" style="--d: 70ms"><span class="when">Stage 2</span><b>Frame</b><p>The frame is up. You start paying interest on what's been drawn so far.</p></li>
<li class="rv rise" style="--d: 140ms"><span class="when">Stage 3</span><b>Lock-up</b><p>Roof, windows and external doors are in.</p></li>
<li class="rv rise" style="--d: 210ms"><span class="when">Stage 4</span><b>Fixing</b><p>Kitchen, bathrooms and internal fit-out.</p></li>
<li class="rv rise" style="--d: 280ms"><span class="when">Stage 5</span><b>Completion</b><p>Final inspection and handover. Your loan switches to normal repayments.</p></li>
</ol>
</div>
</section>

<section class="band band-w1" aria-labelledby="kn-h">
<div class="wrap schemes">
<div class="rv from-l">
<h2 class="h2" id="kn-h">Good to know before you <em class="ul">sign</em></h2>
<p class="lead">A few things that catch people out, so they don't catch you.</p>
</div>
<ul class="hl-list rv from-l" style="--d: 100ms">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v5M12 16h.01"></path></svg><b>Variations need the lender's okay</b><p>Changes to the plans can change the loan. Tell us before you sign a variation.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v5M12 16h.01"></path></svg><b>Plan for rent and a loan at once</b><p>If you're renting while you build, you may be paying both for a while. We'll factor that in.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v5M12 16h.01"></path></svg><b>Keep a buffer</b><p>Lenders usually ask you to cover cost overruns yourself before they pay more out.</p></li>
</ul>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What our clients ","hBrush":"say","hTail":""})}
</div>
</section>

<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">Building <em class="ul">questions</em></h2>
<p class="lead">What people ask us before they start a build.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
<details name="faq" open><summary>Do I pay interest on the full loan while building?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Usually not. Interest is charged on the amount paid out so far, and many lenders let you pay interest only during the build.</p></details>
<details name="faq"><summary>What if the build runs over budget?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Lenders usually need you to cover extra costs yourself before more is paid out. We'll talk about a buffer early so it isn't a surprise.</p></details>
<details name="faq"><summary>Can I build as an owner-builder?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">It's harder and fewer lenders allow it. We'll tell you honestly whether it's an option for your project.</p></details>
<details name="faq"><summary>Do you help with knockdown rebuilds?<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span></summary><p class="ans">Yes. These are common in Melbourne. We'll plan for demolition, the build and where you'll live in the meantime.</p></details>
</div>
</div>
</section>

${ctaBand(C, {"hLead":"Plan your ","hBrush":"build","hTail":" with us","sub":"Bring your builder's quote or plans if you have them.","prefill":{"situation":"building","source":"Building page"}})}`,
});
