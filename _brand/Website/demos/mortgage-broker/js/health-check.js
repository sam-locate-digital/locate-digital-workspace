/*
  Refinance health check quiz, ported from canvas/HealthCheck.dc.html.
  Five questions, then a general verdict. "Book a free rate review" opens the drawer with a summary note.
  No rates or savings are shown: the result only says whether a review looks worthwhile.
*/
(function () {
  const root = document.querySelector('[data-healthcheck]');
  if (!root) return;
  const body = root.querySelector('[data-hc-body]');
  const liveEl = root.querySelector('[data-live]');

  const LENDERS = [{ id: 'big4', label: 'One of the big four banks' }, { id: 'bank', label: 'Another bank or credit union' }, { id: 'nonbank', label: 'A non-bank lender' }, { id: 'unsure', label: "I'm not sure" }];
  const TYPES = [{ id: 'fixed', label: 'Fixed' }, { id: 'variable', label: 'Variable' }, { id: 'split', label: 'Split' }];
  const FIXED_WHEN = [{ id: 'f3', label: 'In the next 3 months', soon: true }, { id: 'f6', label: 'In 3 to 6 months', soon: true }, { id: 'f12', label: 'In 6 to 12 months' }, { id: 'f99', label: 'More than a year away' }];
  const VAR_WHEN = [{ id: 'v1', label: 'In the last 12 months' }, { id: 'v2', label: 'More than a year ago', stale: true }, { id: 'v3', label: "Never, or I'm not sure", stale: true }];
  const AUD = (n) => '$' + Math.round(n).toLocaleString('en-AU');
  const num = (v) => { const n = Number(String(v).replace(/[^\d.]/g, '')); return isFinite(n) ? n : 0; };
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  const fresh = () => ({ lender: '', bal: 500000, rate: '', unsure: false, type: '', when: '' });

  const s = { q: 1, a: fresh(), err: false, done: false };
  const live = (m) => { liveEl.textContent = m; };
  const isFixed = () => s.a.type === 'fixed' || s.a.type === 'split';
  const whenList = () => (isFixed() ? FIXED_WHEN : VAR_WHEN);

  function answered() {
    const { q, a } = s;
    if (q === 1) return !!a.lender; if (q === 2) return a.bal > 0; if (q === 3) return a.unsure || num(a.rate) > 0;
    if (q === 4) return !!a.type; if (q === 5) return !!a.when; return true;
  }
  function result() {
    const a = s.a; const reasons = []; let worth = false;
    const fw = FIXED_WHEN.find((x) => x.id === a.when); const vw = VAR_WHEN.find((x) => x.id === a.when);
    if (fw && fw.soon) { worth = true; reasons.push("Your fixed rate ends soon. When it does, your loan usually moves to the lender's standard variable rate."); }
    if (fw && !fw.soon) reasons.push("Your fixed rate has a while to run. Breaking it early can cost money, so it's often better to plan ahead.");
    if (vw && vw.stale) { worth = true; reasons.push("Your rate hasn't been reviewed in over a year. Lenders often offer new customers sharper deals than existing ones."); }
    if (vw && !vw.stale) reasons.push('Your rate was reviewed in the last year, which is a good sign.');
    if (a.unsure) { worth = true; reasons.push("You weren't sure of your rate. A quick look at your statement will tell us where you stand."); }
    if (a.lender === 'unsure') reasons.push('We can find your lender details from your loan statement.');
    if (a.bal >= 300000) reasons.push('With a balance around ' + AUD(a.bal) + ', small changes to your loan can add up over the years.');
    return { worth, reasons };
  }
  function summary() {
    const a = s.a; const res = result();
    const l = LENDERS.find((x) => x.id === a.lender); const t = TYPES.find((x) => x.id === a.type); const w = whenList().find((x) => x.id === a.when);
    return 'Health check: ' + (l ? l.label.toLowerCase() : 'lender not given') + ', balance about ' + AUD(a.bal) + ', rate ' + (a.unsure ? 'not sure' : num(a.rate).toFixed(2) + '%') + ', ' + (t ? t.label.toLowerCase() : '') + (w ? ' (' + w.label.toLowerCase() + ')' : '') + '. Result: ' + (res.worth ? 'worth a review' : 'looks OK for now') + '.';
  }

  const chips = (list, sel, cls, extra = '') => list.map((o) => `<button type="button" class="${cls}" aria-pressed="${sel === o.id}" data-pick="${o.id}" data-key="p-${o.id}"${extra}>${esc(o.label)}</button>`).join('');

  function html() {
    const a = s.a;
    if (s.done) {
      const res = result();
      return `<div class="done">
<span class="verdict${res.worth ? ' good' : ''}"><i aria-hidden="true"></i>${res.worth ? 'Worth a review' : 'Looks OK for now'}</span>
<h2 class="h3" tabindex="-1" data-res>${res.worth ? 'A free rate review is worth your time.' : "Your loan looks OK for now. We're happy to check in later."}</h2>
<ul class="ready">${res.reasons.map((r) => `<li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="color: #5B6684"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>${esc(r)}</li>`).join('')}</ul>
<p class="disc">This is a general guide based on your answers. It isn't credit advice, and it doesn't compare your loan against any lender's current rates.</p>
<div class="row">
<button type="button" class="btn btn-primary" data-act="book">Book a free rate review</button>
<button type="button" class="textlink" data-act="restart">Start again</button>
</div>
</div>`;
    }
    const head = (t) => `<h2 class="h3" tabindex="-1" data-q>${esc(t)}</h2>`;
    let q = '';
    if (s.q === 1) q = `${head('Who is your loan with?')}
<p class="cap" style="margin-top: 6px">No need to name them.</p>
<div class="sit-chips" role="group" aria-label="Your lender" style="margin-top: 18px">${chips(LENDERS, a.lender, 'chip chip-lg')}</div>`;
    if (s.q === 2) {
      const raw = Math.min(3000000, Math.max(50000, a.bal));
      q = `${head('Roughly how much do you owe?')}
<div class="slide-f" style="margin-top: 20px">
<label for="hc-bal">Loan balance</label>
<input class="range" type="range" min="50000" max="3000000" step="10000" value="${raw}" data-f="range" aria-label="Loan balance" style="--fill: ${Math.round(((raw - 50000) / 2950000) * 100)}%" tabindex="-1">
<div class="money"><input class="fld" id="hc-bal" inputmode="numeric" value="${a.bal.toLocaleString('en-AU')}" data-f="bal" data-key="bal"></div>
</div>`;
    }
    if (s.q === 3) q = `${head("What's your current interest rate?")}
<p class="cap" style="margin-top: 6px">It's on your latest loan statement or in your banking app.</p>
<div class="enq-grid two">
<div class="f">
<label for="hc-rate">Current rate</label>
<div class="suffix"><input class="fld" id="hc-rate" inputmode="decimal" placeholder="e.g. 6.25" value="${esc(a.rate)}" data-f="rate" data-key="rate"${a.unsure ? ' disabled' : ''}><i>% p.a.</i></div>
</div>
<div class="f" style="justify-content: flex-end">
<button type="button" class="chip" aria-pressed="${a.unsure}" data-act="unsure" data-key="unsure" style="min-height: 52px">I'm not sure</button>
</div>
</div>`;
    if (s.q === 4) q = `${head('Is it fixed or variable?')}
<div class="chips" role="group" aria-label="Rate type" style="margin-top: 18px">${chips(TYPES, a.type, 'chip chip-lg', ' style="width: auto; min-width: 140px"')}</div>`;
    if (s.q === 5) {
      const t = isFixed() ? 'When does your fixed rate end?' : 'When was your rate last reviewed?';
      q = `${head(t)}
<div class="sit-chips" role="group" aria-label="${t}" style="margin-top: 18px">${chips(whenList(), a.when, 'chip chip-lg')}</div>`;
    }
    return `<div class="enq-prog"><span>Question ${s.q} of 5</span><span class="bar" aria-hidden="true"><i style="width: ${s.q * 20}%"></i></span></div>
${q}
${s.err ? '<p class="err" style="margin-top: 12px">Choose an option to continue.</p>' : ''}
<div class="enq-nav">
${s.q > 1 ? '<button type="button" class="btn btn-secondary" data-act="back" data-key="back">Back</button>' : ''}
<button type="button" class="btn btn-primary" data-act="next" data-key="next">${s.q < 5 ? 'Next' : 'See my result'}</button>
</div>`;
  }

  function render(focus) {
    const key = document.activeElement && body.contains(document.activeElement) ? document.activeElement.getAttribute('data-key') : null;
    body.innerHTML = html();
    const el = focus ? body.querySelector(focus) : key ? body.querySelector(`[data-key="${key}"]`) : null;
    if (el) el.focus();
  }
  const setA = (o) => { Object.assign(s.a, o); s.err = false; };

  body.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    const a = s.a;
    if (b.dataset.pick) {
      const id = b.dataset.pick;
      if (s.q === 1) setA({ lender: id });
      if (s.q === 4) setA({ type: id, when: (id === 'variable') === (a.type === 'variable') ? a.when : '' });
      if (s.q === 5) setA({ when: id });
      render(); return;
    }
    const act = b.dataset.act;
    if (act === 'unsure') { setA({ unsure: !a.unsure }); render(); }
    if (act === 'back') { s.q = Math.max(1, s.q - 1); s.err = false; render('[data-q]'); }
    if (act === 'next') {
      if (!answered()) { s.err = true; render(); live('Choose an option to continue.'); return; }
      if (s.q < 5) { s.q += 1; s.err = false; render('[data-q]'); live('Question ' + s.q + ' of 5'); }
      else { s.done = true; render('[data-res]'); live(result().worth ? 'Result: worth a review' : 'Result: looks OK for now'); }
    }
    if (act === 'restart') { s.q = 1; s.a = fresh(); s.done = false; s.err = false; render('[data-q]'); live('Question 1 of 5'); }
    if (act === 'book') window.HarlowOpen({ situation: 'refinance', price: a.bal, source: 'Health check', note: summary() });
  });

  body.addEventListener('input', (e) => {
    const f = e.target.dataset.f;
    if (f === 'range') {
      setA({ bal: Number(e.target.value) });
      const box = body.querySelector('#hc-bal'); if (box) box.value = s.a.bal.toLocaleString('en-AU');
      e.target.style.setProperty('--fill', Math.round(((s.a.bal - 50000) / 2950000) * 100) + '%');
    }
    if (f === 'bal') {
      setA({ bal: Math.min(num(e.target.value), 99999999) });
      e.target.value = s.a.bal ? s.a.bal.toLocaleString('en-AU') : '';
      const r = body.querySelector('[data-f="range"]');
      if (r) { const raw = Math.min(3000000, Math.max(50000, s.a.bal)); r.value = raw; r.style.setProperty('--fill', Math.round(((raw - 50000) / 2950000) * 100) + '%'); }
    }
    if (f === 'rate') { setA({ rate: e.target.value.replace(/[^\d.]/g, '').slice(0, 5) }); e.target.value = s.a.rate; }
  });

  render();
})();
