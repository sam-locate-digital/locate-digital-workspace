/*
  3-step enquiry form, ported from canvas/EnquiryForm.dc.html.
  Mounts into every [data-enquiry-form] element. The drawer's form is reset with a new prefill
  each time it opens (HarlowForm.reset). Nothing is sent anywhere unless CONFIG.formEndpoint is set.
*/
(function () {
  const C = window.CONFIG;
  const TEAM = C.team.filter((t) => t.books);
  const SITS = [
    { id: 'first-home', label: 'First home', sub: 'Buying my first place' },
    { id: 'next-home', label: 'Next home', sub: 'Upsizing or moving on' },
    { id: 'refinance', label: 'Refinance', sub: 'Review my current loan' },
    { id: 'invest', label: 'Invest', sub: 'An investment property' },
    { id: 'self-employed', label: 'Self-employed', sub: 'Business or contract income' },
    { id: 'other', label: 'Something else', sub: 'Building, bridging, other' },
  ];
  const CONTACTS = [
    { id: 'call', label: 'Phone call', verb: 'call you' },
    { id: 'video', label: 'Video call', verb: 'video call you' },
    { id: 'sms', label: 'Text first', verb: 'text you' },
    { id: 'email', label: 'Email', verb: 'email you' },
  ];
  const SLOTS = [
    { id: 'morning', label: 'Morning', sub: '9–11am', h: 9, m: 30, word: 'in the morning' },
    { id: 'lunch', label: 'Lunchtime', sub: '12–2pm', h: 12, m: 30, word: 'at lunchtime' },
    { id: 'evening', label: 'Evening', sub: '5:30–7:30pm', h: 18, m: 0, word: 'in the evening' },
  ];
  const LANGS = ['English', 'Mandarin', 'Hindi', 'Gujarati', 'Vietnamese'];
  const READY = ['Your last two payslips (or two years of tax returns if self-employed)', 'Photo ID, like a driver licence or passport', 'Three months of bank statements', 'Your current home loan statement, if you have one'];
  const DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const DOWL = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const MONL = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const FIELDS = ['name', 'mobile', 'email', 'consent'];

  const esc = (s) => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  const pad = (n) => String(n).padStart(2, '0');
  function fmtMoney(v) { const d = String(v == null ? '' : v).replace(/\D/g, '').slice(0, 9); return d ? Number(d).toLocaleString('en-AU') : ''; }
  function fmtMobile(v) {
    let d = String(v || '').replace(/\D/g, '');
    if (d.startsWith('61')) d = '0' + d.slice(2);
    d = d.slice(0, 10);
    if (d.length <= 4) return d;
    if (d.length <= 7) return d.slice(0, 4) + ' ' + d.slice(4);
    return d.slice(0, 4) + ' ' + d.slice(4, 7) + ' ' + d.slice(7);
  }
  function nextDays() {
    const out = []; const t = new Date(); t.setHours(12, 0, 0, 0);
    let weekdays = 0; let sat = null;
    for (let i = 1; i < 14 && (weekdays < 5 || !sat); i++) {
      const d = new Date(t); d.setDate(t.getDate() + i);
      const w = d.getDay();
      const item = { id: d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()), dow: DOW[w], dm: d.getDate() + ' ' + MON[d.getMonth()], long: DOWL[w] + ' ' + d.getDate() + ' ' + MONL[d.getMonth()], sat: w === 6, y: d.getFullYear(), mo: d.getMonth(), da: d.getDate() };
      if (w >= 1 && w <= 5 && weekdays < 5) { out.push(item); weekdays++; }
      else if (w === 6 && !sat) { sat = item; }
    }
    if (sat) out.push(sat);
    return out.sort((a, b) => (a.id < b.id ? -1 : 1));
  }
  // Melbourne offset: AEDT (+11) from first Sunday in October to first Sunday in April, else AEST (+10)
  function melOffset(y, mo, da) {
    const firstSun = (yy, m) => { const d = new Date(Date.UTC(yy, m, 1)); return 1 + ((7 - d.getUTCDay()) % 7); };
    const startDst = Date.UTC(y, 9, firstSun(y, 9)); const endDst = Date.UTC(y, 3, firstSun(y, 3));
    const t = Date.UTC(y, mo, da);
    return (t >= startDst || t < endDst) ? 11 : 10;
  }
  function blank(prefill) {
    const p = prefill || {};
    let sit = p.situation || '';
    let note = p.note || '';
    if (sit === 'building') { sit = 'other'; note = note || 'Interested in a construction loan.'; }
    return {
      situation: sit, price: fmtMoney(p.price), deposit: fmtMoney(p.deposit), income: fmtMoney(p.income), suburb: p.suburb || '',
      name: '', mobile: '', email: '', contact: 'call', day: '', slot: '', broker: p.broker || 'any', language: p.language || 'English', consent: false,
      note, source: p.source || 'Website',
    };
  }
  function validate(d) {
    const e = {};
    if (!d.situation) e.situation = 'Choose the option that fits best, or "Something else".';
    if (!d.name || d.name.trim().length < 2) e.name = 'Please tell us your name.';
    const m = String(d.mobile || '').replace(/\D/g, '');
    if (!m) e.mobile = 'We need a mobile number to call you back.';
    else if (!/^04\d{8}$/.test(m)) e.mobile = "That doesn't look like an Australian mobile. It should be 10 digits starting with 04.";
    if (!d.email) e.email = 'Please add your email so we can send a summary.';
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(d.email.trim())) e.email = 'Check your email address. It should look like name@example.com.';
    if (!d.consent) e.consent = "Please tick the box so we're allowed to contact you.";
    return e;
  }

  const ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>';
  const BACK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>';
  const TICK = (s, w) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg>`;
  const CAL = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"></rect><path d="M3 9.5h18M8 2.5v4M16 2.5v4"></path></svg>';
  const pressed = (on) => `aria-pressed="${on ? 'true' : 'false'}"`;

  class EnquiryForm {
    constructor(el, prefill) {
      this.el = el;
      this.uid = el.dataset.uid || 'enq';
      this.days = nextDays();
      el.innerHTML = '<div class="enq-root"><p class="sr" aria-live="polite" role="status" data-live></p><div data-body></div></div>';
      this.body = el.querySelector('[data-body]');
      this.reset(prefill, false);
      el.addEventListener('click', (e) => this.onClick(e));
      el.addEventListener('input', (e) => this.onInput(e));
      el.addEventListener('change', (e) => this.onChange(e));
      el.addEventListener('focusout', (e) => this.onBlur(e));
      el.addEventListener('submit', (e) => this.submit(e));
    }

    reset(prefill, announce) {
      this.prefill = prefill || {};
      this.s = { step: 1, d: blank(this.prefill), touched: {}, tried: {}, sending: false, done: false, ref: '' };
      this.render();
      if (announce) this.live('New enquiry, step 1 of 3');
    }

    id(k) { return this.uid + '-' + k; }
    live(msg) { const p = this.el.querySelector('[data-live]'); if (p) p.textContent = msg; }
    show(k) {
      const errs = validate(this.s.d);
      if (k === 'situation') return !!errs.situation && !!this.s.tried[1];
      return !!errs[k] && (!!this.s.touched[k] || !!this.s.tried[3]);
    }

    // Re-render the whole form, keeping focus on the same control if it still exists.
    render(focusSel) {
      const key = document.activeElement && this.el.contains(document.activeElement) ? document.activeElement.getAttribute('data-key') : null;
      this.body.innerHTML = this.html();
      const target = focusSel ? this.el.querySelector(focusSel) : key ? this.el.querySelector(`[data-key="${key}"]`) : null;
      if (target) target.focus();
    }

    goStep(n) { this.s.step = n; this.render(); this.live('Step ' + n + ' of 3'); const h = this.el.querySelector('[data-head]'); if (h) h.focus(); }

    // Update error messages and aria state in place, so typing never loses focus.
    syncErrors() {
      const errs = validate(this.s.d);
      FIELDS.forEach((k) => {
        const input = this.el.querySelector(`[data-field="${k}"]`);
        const err = this.el.querySelector(`[data-err="${k}"]`);
        if (!input || !err) return;
        const on = this.show(k);
        err.hidden = !on; err.textContent = on ? errs[k] : '';
        input.setAttribute('aria-invalid', on ? 'true' : 'false');
        if (on) input.setAttribute('aria-describedby', this.id(k + '-err')); else input.removeAttribute('aria-describedby');
      });
    }

    onClick(e) {
      const b = e.target.closest('button'); if (!b || !this.el.contains(b)) return;
      const s = this.s; const d = s.d; const ds = b.dataset;
      if (ds.sit) { d.situation = ds.sit; s.tried[1] = false; this.render(); return; }
      if (ds.contact) { d.contact = ds.contact; this.render(); return; }
      if (ds.broker) { d.broker = ds.broker; this.render(); return; }
      if (ds.slot) { if (!b.disabled) { d.slot = ds.slot; this.render(); } return; }
      if (ds.day) {
        const x = this.days.find((y) => y.id === ds.day);
        d.day = d.day === x.id ? '' : x.id;
        if (x.sat && d.slot && d.slot !== 'morning') d.slot = 'morning';
        if (d.day && !d.slot) d.slot = x.sat ? 'morning' : '';
        this.render(); return;
      }
      const act = ds.act;
      if (act === 'next') {
        if (s.step === 1 && !d.situation) { s.tried[1] = true; this.render(); this.live('Please choose your situation to continue.'); return; }
        this.goStep(Math.min(3, s.step + 1));
      } else if (act === 'back') {
        this.goStep(Math.max(1, s.step - 1));
      } else if (act === 'ics') {
        this.downloadIcs();
      } else if (act === 'restart') {
        this.reset(this.prefill, true);
      }
    }

    onInput(e) {
      const f = e.target.dataset.field; if (!f) return;
      const d = this.s.d; const v = e.target.value;
      if (f === 'price' || f === 'deposit' || f === 'income') { d[f] = fmtMoney(v); e.target.value = d[f]; }
      else if (f === 'mobile') { d.mobile = fmtMobile(v); e.target.value = d.mobile; }
      else if (f === 'name' || f === 'email' || f === 'suburb') d[f] = v;
      this.syncErrors();
    }

    onChange(e) {
      const f = e.target.dataset.field;
      if (f === 'language') this.s.d.language = e.target.value;
      if (f === 'consent') { this.s.d.consent = e.target.checked; this.s.touched.consent = true; this.syncErrors(); }
    }

    onBlur(e) {
      const f = e.target.dataset.field;
      if (FIELDS.includes(f)) { this.s.touched[f] = true; this.syncErrors(); }
    }

    submit(e) {
      e.preventDefault();
      const s = this.s;
      if (s.sending || s.step !== 3) return;
      const errs = validate(s.d); delete errs.situation;
      const list = Object.values(errs);
      if (list.length) {
        s.tried[3] = true; this.syncErrors();
        this.live(list.length === 1 ? 'There is 1 thing to fix: ' + list[0] : 'There are ' + list.length + ' things to fix before we can book your chat.');
        setTimeout(() => { const el = this.el.querySelector('[aria-invalid="true"]'); if (el) el.focus(); }, 30);
        return;
      }
      s.sending = true; this.render('[data-submit]'); this.live('Sending your enquiry');
      const payload = Object.assign({}, s.d, { submittedAt: new Date().toISOString() });
      if (C.formEndpoint) {
        try { fetch(C.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) }).catch(() => {}); } catch (err) { /* demo */ }
      } else {
        console.log('[Harlow demo] Enquiry (not sent anywhere):', payload);
      }
      setTimeout(() => {
        s.sending = false; s.done = true; s.ref = 'HL-' + String(Math.floor(10000 + Math.random() * 90000));
        this.render('[data-done]');
        this.live('Thanks. Your chat is booked. Reference ' + s.ref);
      }, 900);
    }

    brokerName() { const b = TEAM.find((t) => t.id === this.s.d.broker); return b ? b.first : null; }

    downloadIcs() {
      const d = this.s.d; const day = this.days.find((x) => x.id === d.day); const slot = SLOTS.find((x) => x.id === d.slot);
      if (!day || !slot) return;
      const off = melOffset(day.y, day.mo, day.da);
      const start = new Date(Date.UTC(day.y, day.mo, day.da, slot.h - off, slot.m));
      const end = new Date(start.getTime() + 20 * 60000);
      const f = (dt) => dt.getUTCFullYear() + pad(dt.getUTCMonth() + 1) + pad(dt.getUTCDate()) + 'T' + pad(dt.getUTCHours()) + pad(dt.getUTCMinutes()) + '00Z';
      const who = this.brokerName() || 'a Harlow broker'; const ref = this.s.ref;
      const lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Harlow Home Loans//Demo//EN', 'CALSCALE:GREGORIAN', 'METHOD:PUBLISH', 'BEGIN:VEVENT',
        'UID:' + ref + '@harlowhomeloans.example', 'DTSTAMP:' + f(new Date()), 'DTSTART:' + f(start), 'DTEND:' + f(end),
        'SUMMARY:Free 20-minute chat with ' + who, 'DESCRIPTION:Reference ' + ref + '. ' + who + ' will contact you. Questions? Call ' + C.contact.phone + '.',
        'LOCATION:' + (d.contact === 'video' ? 'Video call (link to follow)' : 'Phone call'), 'END:VEVENT', 'END:VCALENDAR'];
      const blob = new Blob([lines.join('\r\n')], { type: 'text/calendar;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = 'harlow-chat-' + ref + '.ics';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 2000);
    }

    field(k, label, attrs, value) {
      const on = this.show(k); const errs = validate(this.s.d);
      return `<div class="f">
<label for="${this.id(k)}">${label}</label>
<input class="fld" id="${this.id(k)}" data-field="${k}" data-key="f-${k}" value="${esc(value)}" ${attrs} aria-required="true" aria-invalid="${on}"${on ? ` aria-describedby="${this.id(k + '-err')}"` : ''}>
<p class="err" id="${this.id(k + '-err')}" data-err="${k}"${on ? '' : ' hidden'}>${on ? esc(errs[k]) : ''}</p>
</div>`;
    }

    html() {
      const s = this.s; const d = s.d; const id = (k) => this.id(k);
      if (s.done) {
        const day = this.days.find((x) => x.id === d.day); const slot = SLOTS.find((x) => x.id === d.slot);
        const first = (d.name || '').trim().split(/\s+/)[0] || 'there';
        const contact = CONTACTS.find((c) => c.id === d.contact) || CONTACTS[0];
        const who = this.brokerName() || 'One of our brokers';
        const line = day && slot
          ? who + ' will ' + contact.verb + ' on ' + day.long + ' ' + slot.word + '. If that time stops suiting you, just reply to our confirmation or call ' + C.contact.phone + '.'
          : who + ' will ' + contact.verb + ' within ' + C.responseTime + ' [PLACEHOLDER] to find a time that suits.';
        return `<div class="enq">
<div class="done">
<span class="tick" aria-hidden="true">${TICK(24, 2)}</span>
<h3 class="h3" tabindex="-1" data-done>Thanks, ${esc(first)}.</h3>
<p>${esc(line)}</p>
<span class="ref">Reference ${s.ref}</span>
<div class="row">
${day && slot ? `<button type="button" class="btn btn-primary" data-act="ics" data-key="ics">${CAL}Add to calendar</button>` : ''}
<button type="button" class="btn btn-secondary" data-act="restart" data-key="restart">Start a new enquiry</button>
</div>
<div style="padding-top: 8px; border-top: 1px solid #DCE4F5">
<p class="ink" style="font-weight: 600; margin: 14px 0 10px">What to have ready</p>
<ul class="ready">${READY.map((r) => `<li>${TICK(18, 1.8)}${r}</li>`).join('')}</ul>
</div>
<p class="cap">Demo site: nothing has been sent to a real broker.</p>
</div>
</div>`;
      }

      const head = (t) => `<h3 class="h3" id="${id('head')}" tabindex="-1" data-head>${t}</h3>`;
      const note = d.note ? `<p class="note" style="margin-top: 16px">${esc(d.note)}</p>` : '';
      let body = '';
      if (s.step === 1) {
        body = `${head('What are you planning?')}
<p class="small" style="color: #46506A">Pick the one that fits best. You can change it later.</p>
<div class="sit-chips" role="group" aria-label="Your situation" style="margin-top: 18px">
${SITS.map((it) => `<button type="button" class="chip chip-lg" ${pressed(d.situation === it.id)} data-sit="${it.id}" data-key="sit-${it.id}"><span><span style="display: block">${it.label}</span><small>${it.sub}</small></span></button>`).join('')}
</div>
${this.show('situation') ? `<p class="err" style="margin-top: 10px">${validate(d).situation}</p>` : ''}
${note}`;
      } else if (s.step === 2) {
        const isRefi = d.situation === 'refinance'; const isMove = d.situation === 'next-home';
        const money = (k, label) => `<div class="f">
<label for="${id(k)}">${label}</label>
<div class="money"><input class="fld" id="${id(k)}" data-field="${k}" data-key="f-${k}" inputmode="numeric" autocomplete="off" placeholder="0" value="${esc(d[k])}"></div>
</div>`;
        body = `${head('The numbers')}
<p class="small" style="color: #46506A">All optional. Rough is fine, we'll go through it properly on the call.</p>
<div class="enq-grid two">
${money('price', isRefi ? 'Current loan balance' : 'Property price')}
${money('deposit', isRefi || isMove ? 'Equity, roughly' : 'Deposit saved')}
${money('income', 'Household income (before tax, yearly)')}
<div class="f">
<label for="${id('suburb')}">Suburb</label>
<input class="fld" id="${id('suburb')}" data-field="suburb" data-key="f-suburb" list="${id('sublist')}" autocomplete="address-level2" placeholder="e.g. Doncaster" value="${esc(d.suburb)}">
<datalist id="${id('sublist')}">${C.suburbs.map((sb) => `<option value="${esc(sb)}"></option>`).join('')}</datalist>
</div>
</div>
${note}`;
      } else {
        const day = this.days.find((x) => x.id === d.day);
        body = `${head('Your details')}
<p class="small" style="color: #46506A">So we can call you at a time that suits. No credit check.</p>
<div class="enq-grid">
${this.field('name', 'Your name', 'autocomplete="name"', d.name)}
<div class="enq-grid two" style="margin-top: 0">
${this.field('mobile', 'Mobile', 'type="tel" inputmode="tel" autocomplete="tel" placeholder="04XX XXX XXX"', d.mobile)}
${this.field('email', 'Email', 'inputmode="email" autocomplete="email" placeholder="you@example.com"', d.email)}
</div>
<div class="f">
<span class="lbl" id="${id('how')}">Best way to reach you</span>
<div class="chips" role="group" aria-labelledby="${id('how')}">
${CONTACTS.map((c) => `<button type="button" class="chip" ${pressed(d.contact === c.id)} data-contact="${c.id}" data-key="c-${c.id}">${c.label}</button>`).join('')}
</div>
</div>
<div class="f">
<span class="lbl" id="${id('day')}">Preferred time <span style="font-weight: 500; color: #5B6684">(optional)</span></span>
<div class="days" role="group" aria-labelledby="${id('day')}">
${this.days.map((dy) => `<button type="button" class="day" ${pressed(d.day === dy.id)} data-day="${dy.id}" data-key="d-${dy.id}" aria-label="${dy.long}">${dy.dow}<small>${dy.dm}</small></button>`).join('')}
</div>
${day ? `<div class="chips" role="group" aria-label="Time of day" style="margin-top: 6px">
${SLOTS.map((sl) => { const off = !!(day.sat && sl.id !== 'morning'); return `<button type="button" class="chip" ${pressed(d.slot === sl.id)} data-slot="${sl.id}" data-key="s-${sl.id}"${off ? ' disabled' : ''} style="opacity: ${off ? 0.45 : 1}"><span><span style="display: block">${sl.label}</span><small>${sl.sub}</small></span></button>`; }).join('')}
</div>` : ''}
</div>
<div class="enq-grid two" style="margin-top: 0">
<div class="f">
<span class="lbl" id="${id('broker')}">Broker</span>
<div class="chips" role="group" aria-labelledby="${id('broker')}">
${[{ id: 'any', label: 'Any broker' }].concat(TEAM.map((t) => ({ id: t.id, label: t.first }))).map((b) => `<button type="button" class="chip" ${pressed(d.broker === b.id)} data-broker="${b.id}" data-key="b-${b.id}">${b.label}</button>`).join('')}
</div>
</div>
<div class="f">
<label for="${id('lang')}">Language</label>
<select class="fld" id="${id('lang')}" data-field="language" data-key="f-lang">
${LANGS.map((lg) => `<option value="${lg}"${d.language === lg ? ' selected' : ''}>${lg}</option>`).join('')}
</select>
</div>
</div>
<div class="f">
<label class="check"><input type="checkbox" data-field="consent" data-key="f-consent"${d.consent ? ' checked' : ''} aria-invalid="${this.show('consent')}"${this.show('consent') ? ` aria-describedby="${id('consent-err')}"` : ''}><span>I'm happy for Harlow Home Loans to contact me about my enquiry. I've read the <a href="privacy.html">Privacy Policy</a>.</span></label>
<p class="err" id="${id('consent-err')}" data-err="consent"${this.show('consent') ? '' : ' hidden'}>${this.show('consent') ? validate(d).consent : ''}</p>
</div>
</div>`;
      }

      return `<div class="enq">
<form aria-labelledby="${id('head')}" novalidate>
<div class="enq-prog"><span>Step ${s.step} of 3</span><span class="bar" aria-hidden="true"><i style="width: ${Math.round((s.step / 3) * 100)}%"></i></span></div>
${body}
<div class="enq-nav">
${s.step > 1 ? `<button type="button" class="btn btn-secondary" data-act="back" data-key="back">${BACK}Back</button>` : ''}
${s.step < 3 ? `<button type="button" class="btn btn-primary" data-act="next" data-key="next">Continue${ARROW}</button>` : ''}
${s.step === 3 ? `<button type="submit" class="btn btn-primary" data-submit data-key="submit" aria-disabled="${s.sending}">${s.sending ? '<span class="spin" aria-hidden="true"></span>Sending' : 'Book my free chat'}</button>` : ''}
</div>
<p class="cap" style="margin-top: 14px">No obligation and no credit check. Your details stay private.</p>
</form>
</div>`;
    }
  }

  const forms = new WeakMap();
  window.HarlowForm = {
    reset(el, prefill) { const f = forms.get(el); if (f) f.reset(prefill, false); },
  };
  document.querySelectorAll('[data-enquiry-form]').forEach((el) => {
    let prefill = {};
    try { prefill = JSON.parse(el.dataset.prefill || '{}'); } catch (e) { /* keep blank */ }
    forms.set(el, new EnquiryForm(el, prefill));
  });
})();
