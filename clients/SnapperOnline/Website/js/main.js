/* ===========================================================
   Snapper Online — main.js
   - Slide-out nav panel (Explore drawer)
   - Lightbox (used on portfolio page)
   - Contact form thank-you (front-end only)
   - Subtle staggered entrance reveals
   =========================================================== */

(function () {
  'use strict';

  /* ------- NAV PANEL ------- */
  const panel    = document.querySelector('.nav-panel');
  const backdrop = document.querySelector('.nav-backdrop');
  const toggle   = document.querySelector('.menu-toggle');
  const closeBtn = document.querySelector('.nav-close');

  const openNav = () => {
    if (!panel) return;
    panel.setAttribute('aria-hidden', 'false');
    backdrop.setAttribute('aria-hidden', 'false');
    document.body.classList.add('nav-open');
    setTimeout(() => {
      const firstLink = panel.querySelector('a');
      firstLink && firstLink.focus();
    }, 80);
  };
  const closeNav = () => {
    if (!panel) return;
    panel.setAttribute('aria-hidden', 'true');
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('nav-open');
    toggle && toggle.focus();
  };

  toggle   && toggle.addEventListener('click', openNav);
  closeBtn && closeBtn.addEventListener('click', closeNav);
  backdrop && backdrop.addEventListener('click', closeNav);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && panel && panel.getAttribute('aria-hidden') === 'false') closeNav();
  });

  /* ------- LIGHTBOX ------- */
  const lightbox = document.querySelector('.lightbox');
  if (lightbox) {
    const lbImg    = lightbox.querySelector('img');
    const lbClose  = lightbox.querySelector('.lb-close');
    const lbPrev   = lightbox.querySelector('.lb-prev');
    const lbNext   = lightbox.querySelector('.lb-next');
    const triggers = Array.from(document.querySelectorAll('[data-lightbox]'));
    let idx = 0;

    const show = (i) => {
      idx = (i + triggers.length) % triggers.length;
      const src = triggers[idx].getAttribute('data-lightbox');
      const alt = triggers[idx].getAttribute('data-alt') || '';
      lbImg.src = src;
      lbImg.alt = alt;
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    };
    const hide = () => {
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    };

    triggers.forEach((t, i) => t.addEventListener('click', () => show(i)));
    lbClose && lbClose.addEventListener('click', hide);
    lbPrev  && lbPrev.addEventListener('click', () => show(idx - 1));
    lbNext  && lbNext.addEventListener('click', () => show(idx + 1));
    lightbox.addEventListener('click', (e) => { if (e.target === lightbox) hide(); });

    document.addEventListener('keydown', (e) => {
      if (lightbox.getAttribute('aria-hidden') === 'true') return;
      if (e.key === 'Escape')     hide();
      if (e.key === 'ArrowLeft')  show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* ------- CONTACT FORM (FE-only) ------- */
  const form = document.querySelector('.form');
  const thanks = document.querySelector('.form__thanks');
  if (form && thanks) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      form.style.display = 'none';
      thanks.setAttribute('data-visible', 'true');
      thanks.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  /* ------- STAGGERED REVEAL ON LOAD/SCROLL ------- */
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    reveals.forEach((r) => io.observe(r));
  } else {
    reveals.forEach((r) => r.classList.add('in'));
  }

  /* ------- AUTO-MARK CURRENT PAGE IN NAV ------- */
  const here = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-links a').forEach((a) => {
    const target = (a.getAttribute('href') || '').toLowerCase();
    if (target === here || (here === '' && target === 'index.html')) {
      a.setAttribute('aria-current', 'page');
    }
  });
})();
