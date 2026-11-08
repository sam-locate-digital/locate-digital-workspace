// Locate tutorial kit: brand pieces for 16:9 long-form (1920x1080). Brand fonts (Newsreader + Public Sans), not the
// social fonts the reels use. Built light: no backdrop blur on large layers, so long renders stay quick.
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, staticFile} from 'remotion';
import {loadFont as loadNewsreader} from '@remotion/google-fonts/Newsreader';
import {loadFont as loadPublicSans} from '@remotion/google-fonts/PublicSans';

const serif = loadNewsreader('normal', {weights: ['400', '600'], subsets: ['latin']});
loadNewsreader('italic', {weights: ['600'], subsets: ['latin']});
const sans = loadPublicSans('normal', {weights: ['500', '600', '700', '800'], subsets: ['latin']});

export const T = {
  blue: '#007AE8',
  cyan: '#75DFEE',
  orange: '#FF5900',
  ink: '#0D0D0D',
  muted: '#63666B',
  line: '#E6E6E6',
  soft: '#FBFCFF',
  serif: `${serif.fontFamily}, Georgia, serif`,
  sans: `${sans.fontFamily}, system-ui, sans-serif`,
  cardShadow: '0 1px 3px rgba(13,13,13,.06), 0 24px 48px -18px rgba(0,60,120,.28)',
};

export const BRUSH = 'M3 19 C 28 11, 96 5, 190 2 C 196 1, 200 4, 197 8 C 186 10, 120 13, 60 17 C 38 19, 18 21, 9 25 C 3 27, 0 22, 3 19 Z';
export const easeOut = Easing.bezier(0.2, 0.7, 0.2, 1);
export const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};

// 0..1 progress of an entrance starting at `at` seconds lasting `dur`
export const enter = (t, at, dur = 0.3, ease = easeOut) => interpolate(t, [at, at + dur], [0, 1], {...clamp, easing: ease});
// 1 while on, falling to 0 over `dur` before `end`
export const leave = (t, end, dur = 0.25) => interpolate(t, [end - dur, end], [1, 0], {...clamp, easing: easeInOut});
export const lerp = (a, b, p) => a + (b - a) * p;

// rise 30 px, fade and settle; a light de-blur only on small elements
export const rise = (p, blur = true) => ({
  opacity: p,
  transform: `translateY(${(1 - p) * 30}px) scale(${0.97 + 0.03 * p})`,
  filter: blur && p < 1 ? `blur(${(1 - p) * 8}px)` : 'none',
});

export const Canvas = ({style}) => (
  <AbsoluteFill
    style={{
      backgroundColor: T.soft,
      backgroundImage: `linear-gradient(${T.line} 1px, transparent 1px), linear-gradient(90deg, ${T.line} 1px, transparent 1px)`,
      backgroundSize: '60px 60px', backgroundPosition: '-1px -1px', ...style,
    }}
  >
    <AbsoluteFill style={{background: 'radial-gradient(45% 40% at 92% 4%, rgba(117,223,238,.32), transparent 70%)'}} />
    <AbsoluteFill style={{background: 'radial-gradient(40% 40% at 4% 100%, rgba(0,122,232,.07), transparent 70%)'}} />
  </AbsoluteFill>
);

export const Brush = ({progress, height = 40}) => (
  <div style={{position: 'absolute', left: '-4%', width: '108%', bottom: -height * 0.3, height,
    clipPath: `inset(-50% ${100 - progress * 100}% -50% 0)`, zIndex: -1}}>
    <svg viewBox="0 0 200 28" preserveAspectRatio="none" style={{width: '100%', height: '100%', overflow: 'visible'}}>
      <path d={BRUSH} fill={T.blue} />
    </svg>
  </div>
);

// Text with one word (em) underlined by the blue brush, which sweeps in at `brushAt`
export const EmText = ({text, em, t, brushAt, brushH = 40}) => {
  if (!em || !text.includes(em)) return <>{text}</>;
  const i = text.indexOf(em);
  return (
    <>
      {text.slice(0, i)}
      <span style={{position: 'relative', isolation: 'isolate', display: 'inline-block'}}>
        {em}<Brush progress={enter(t, brushAt, 0.4, easeInOut)} height={brushH} />
      </span>
      {text.slice(i + em.length)}
    </>
  );
};

export const Tick = ({size = 30, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 16 16" aria-hidden="true">
    <path d="M3 8.5l3 3 7-7" fill="none" stroke={color} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

// App tiles: the brand's own mark from public/logos/<kind>-mark.svg on its tile colour (white unless listed)
const TILE_BG = {claude: '#D97757', highlevel: '#ffffff'};
export const AppTile = ({kind, size = 64}) => (
  <div style={{width: size, height: size, borderRadius: size * 0.225, background: TILE_BG[kind] || '#fff', flex: 'none',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    boxShadow: `0 0 0 1px rgba(13,13,13,.07), 0 ${size * 0.08}px ${size * 0.2}px -${size * 0.06}px rgba(0,40,90,.35)`}}>
    <Img src={staticFile(`logos/${kind}-mark.svg`)} style={{width: size * 0.6, height: size * 0.6, objectFit: 'contain'}} />
  </div>
);

const card = {background: '#fff', border: `1.5px solid ${T.line}`, borderRadius: 28, boxShadow: T.cardShadow};

// ---------- Panels: used on the right/left of a split frame, or large on a full-frame card ----------

export const PointsPanel = ({p, t, title, items = [], big = false}) => (
  <div style={{...card, ...rise(p, false), padding: big ? '64px 72px' : '48px 52px', width: big ? 1240 : 820}}>
    {title ? <div style={{fontFamily: T.serif, fontWeight: 600, fontSize: big ? 68 : 54, lineHeight: 1.1, color: T.ink, marginBottom: big ? 40 : 30}}>{title}</div> : null}
    <div style={{display: 'flex', flexDirection: 'column', gap: big ? 26 : 20}}>
      {items.map((it, i) => {
        const q = enter(t, it.at, 0.3);
        return (
          <div key={i} style={{...rise(q), display: 'flex', alignItems: 'center', gap: 22}}>
            <div style={{width: big ? 50 : 44, height: big ? 50 : 44, borderRadius: 999, background: T.blue, flex: 'none',
              display: 'flex', alignItems: 'center', justifyContent: 'center'}}><Tick size={big ? 28 : 24} /></div>
            <div style={{fontFamily: T.sans, fontWeight: 600, fontSize: big ? 44 : 36, lineHeight: 1.25, color: T.ink}}>{it.text}</div>
          </div>
        );
      })}
    </div>
  </div>
);

export const StatementPanel = ({p, t, at, text, em, sub, big = false}) => (
  <div style={{...rise(p, false), width: big ? 1500 : 800, textAlign: big ? 'center' : 'left'}}>
    <div style={{fontFamily: T.serif, fontWeight: 600, fontSize: big ? 104 : 72, lineHeight: 1.12, color: T.ink, letterSpacing: '-0.01em'}}>
      <EmText text={text} em={em} t={t} brushAt={at + 0.45} brushH={big ? 46 : 34} />
    </div>
    {sub ? <div style={{fontFamily: T.sans, fontWeight: 500, fontSize: big ? 40 : 32, color: T.muted, marginTop: 34}}>{sub}</div> : null}
  </div>
);

export const StatPanel = ({p, t, at, value, prefix = '', suffix = '', label, decimals = 0, big = false}) => {
  const num = typeof value === 'number';
  const v = num ? interpolate(t, [at + 0.2, at + 1.4], [0, value], {...clamp, easing: Easing.out(Easing.cubic)}) : value;
  return (
    <div style={{...card, ...rise(p, false), padding: big ? '70px 90px' : '52px 60px', textAlign: 'center'}}>
      <div style={{fontFamily: T.serif, fontWeight: 600, fontSize: big ? 200 : 150, lineHeight: 1, color: T.blue, fontVariantNumeric: 'tabular-nums'}}>
        {prefix}{num ? v.toLocaleString('en-AU', {minimumFractionDigits: decimals, maximumFractionDigits: decimals}) : v}{suffix}
      </div>
      <div style={{fontFamily: T.sans, fontWeight: 600, fontSize: big ? 44 : 36, color: T.muted, marginTop: 24}}>{label}</div>
    </div>
  );
};

export const ImagePanel = ({p, src, caption, big = false}) => (
  <div style={{...rise(p, false), display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22}}>
    <div style={{...card, padding: 12, borderRadius: 24}}>
      <Img src={staticFile(src)} style={{display: 'block', maxWidth: big ? 1500 : 860, maxHeight: big ? 800 : 720, borderRadius: 14}} />
    </div>
    {caption ? <div style={{fontFamily: T.sans, fontWeight: 600, fontSize: 30, color: T.muted}}>{caption}</div> : null}
  </div>
);

export const Panel = ({panel, t, at, p, big}) => {
  if (panel.kind === 'points') return <PointsPanel p={p} t={t} title={panel.title} items={panel.items} big={big} />;
  if (panel.kind === 'statement') return <StatementPanel p={p} t={t} at={at} text={panel.text} em={panel.em} sub={panel.sub} big={big} />;
  if (panel.kind === 'stat') return <StatPanel p={p} t={t} at={at} {...panel} big={big} />;
  if (panel.kind === 'image') return <ImagePanel p={p} src={panel.src} caption={panel.caption} big={big} />;
  return null;
};

// ---------- Full-frame cards ----------

// Section card: "Part 2 of 5", the title with its key word brushed, a progress row, a big faint numeral
export const ChapterCard = ({t, c}) => {
  const p1 = enter(t, c.s + 0.1, 0.35), p2 = enter(t, c.s + 0.22, 0.35), p3 = enter(t, c.s + 0.34, 0.35);
  return (
    <AbsoluteFill>
      <Canvas />
      <div style={{position: 'absolute', right: 70, top: 40, fontFamily: T.serif, fontWeight: 600, fontSize: 560, lineHeight: 1,
        color: 'rgba(0,122,232,.07)', ...rise(enter(t, c.s, 0.6), false)}}>{String(c.n).padStart(2, '0')}</div>
      <div style={{position: 'absolute', left: 160, top: 0, bottom: 0, width: 1500, display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
        <div style={{...rise(p1), fontFamily: T.sans, fontWeight: 700, fontSize: 28, letterSpacing: '0.14em', textTransform: 'uppercase', color: T.blue}}>
          Part {c.n} of {c.count}
        </div>
        <div style={{...rise(p2), fontFamily: T.serif, fontWeight: 600, fontSize: 124, lineHeight: 1.06, color: T.ink, marginTop: 26, letterSpacing: '-0.015em'}}>
          <EmText text={c.title} em={c.em} t={t} brushAt={c.s + 0.7} brushH={48} />
        </div>
        {c.count > 1 ? (
          <div style={{...rise(p3, false), display: 'flex', gap: 12, marginTop: 64}}>
            {Array.from({length: c.count}, (_, i) => (
              <div key={i} style={{width: 72, height: 8, borderRadius: 99,
                background: i + 1 < c.n ? 'rgba(0,122,232,.35)' : i + 1 === c.n ? T.blue : T.line}} />
            ))}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

// Lesson title card, shown once after the hook
export const TitleCard = ({t, it}) => {
  const p1 = enter(t, it.s + 0.1, 0.35), p2 = enter(t, it.s + 0.24, 0.4), p3 = enter(t, it.s + 0.45, 0.35);
  return (
    <AbsoluteFill>
      <Canvas />
      <AbsoluteFill style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', textAlign: 'center', padding: '0 180px'}}>
        {it.kicker ? (
          <div style={{...rise(p1), fontFamily: T.sans, fontWeight: 700, fontSize: 28, letterSpacing: '0.14em', textTransform: 'uppercase', color: T.blue}}>{it.kicker}</div>
        ) : null}
        <div style={{...rise(p2), fontFamily: T.serif, fontWeight: 600, fontSize: 118, lineHeight: 1.06, color: T.ink, marginTop: 30, letterSpacing: '-0.015em'}}>
          <EmText text={it.title} em={it.em} t={t} brushAt={it.s + 0.8} brushH={46} />
        </div>
        {it.sub ? <div style={{...rise(p3), fontFamily: T.sans, fontWeight: 500, fontSize: 40, color: T.muted, marginTop: 64}}>{it.sub}</div> : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const EndCard = ({t, end}) => {
  const p1 = enter(t, end.s + 0.1, 0.35), p2 = enter(t, end.s + 0.3, 0.35);
  return (
    <AbsoluteFill>
      <Canvas />
      <AbsoluteFill style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 54, textAlign: 'center', padding: '0 200px'}}>
        <div style={{...rise(p1), fontFamily: T.serif, fontWeight: 600, fontSize: 104, lineHeight: 1.08, color: T.ink}}>{end.title}</div>
        {end.button ? (
          <div style={{...rise(p2), background: T.orange, color: '#fff', fontFamily: T.sans, fontWeight: 700, fontSize: 44,
            padding: '28px 64px', borderRadius: 999, boxShadow: '0 22px 50px -18px rgba(255,89,0,.55)'}}>{end.button}</div>
        ) : null}
        {end.url ? <div style={{...rise(p2), fontFamily: T.sans, fontWeight: 500, fontSize: 34, color: T.muted}}>{end.url}</div> : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// Lower third: tool name, link or person, bottom left
export const LowerThird = ({t, l}) => {
  const p = enter(t, l.s, 0.35) * leave(t, l.e, 0.25);
  if (p <= 0) return null;
  return (
    <div style={{position: 'absolute', left: 56, bottom: 56, ...card, borderRadius: 22, padding: l.logo ? '14px 30px 14px 14px' : '18px 30px',
      display: 'flex', alignItems: 'center', gap: 18, opacity: p, transform: `translateX(${(1 - p) * -40}px)`}}>
      {l.logo ? <AppTile kind={l.logo} size={64} /> : <div style={{width: 14, height: 14, borderRadius: 4, background: T.blue, flex: 'none'}} />}
      <div>
        <div style={{fontFamily: T.sans, fontWeight: 700, fontSize: 34, lineHeight: 1.15, color: T.ink}}>{l.text}</div>
        {l.sub ? <div style={{fontFamily: T.sans, fontWeight: 500, fontSize: 24, lineHeight: 1.25, color: T.muted, marginTop: 2}}>{l.sub}</div> : null}
      </div>
    </div>
  );
};
