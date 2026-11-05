// Locate Reel Style kit — reusable pieces that follow _brand/Content/CLAUDE.md.
import React from 'react';
import {AbsoluteFill, Easing, Img, Loop, OffthreadVideo, interpolate, staticFile} from 'remotion';
import {loadFont as loadNewsreader} from '@remotion/google-fonts/Newsreader';
import {loadFont as loadPublicSans} from '@remotion/google-fonts/PublicSans';
import {loadFont as loadTikTokSans} from '@remotion/google-fonts/TikTokSans';

const serif = loadNewsreader('normal', {weights: ['400', '600'], subsets: ['latin']});
loadNewsreader('italic', {weights: ['600'], subsets: ['latin']});
const sans = loadPublicSans('normal', {weights: ['600', '700', '800'], subsets: ['latin']});
// Social captions use TikTok's own platform font (Sam, v3: standard social fonts, not the brand fonts)
const tiktok = loadTikTokSans('normal', {weights: ['400', '600', '700', '800'], subsets: ['latin']});
export const SOCIAL_FONT = `${tiktok.fontFamily}, 'Helvetica Neue', Arial, sans-serif`;

// Simple black outline around white text, built from a ring of hard text shadows
const outline = (r = 5, steps = 16, color = '#000') =>
  Array.from({length: steps}, (_, i) => {
    const a = (i / steps) * Math.PI * 2;
    return `${(Math.cos(a) * r).toFixed(2)}px ${(Math.sin(a) * r).toFixed(2)}px 0 ${color}`;
  }).join(', ');
const OUTLINE = outline(5) + ', ' + outline(2.5);

// v3 caption: white TikTok Sans with a plain black outline. Emphasis cues read as one plain line.
export const SocialCaption = ({cue, t, bottom = 1470}) => {
  const p = cue.s <= 0.001 ? 1 : enter(t, cue.s, 0.12);
  const text = cue.em ? `${cue.setup} ${cue.em}` : cue.text;
  return (
    <div
      style={{
        position: 'absolute', left: 90, right: 90, top: 0, height: bottom,
        display: 'flex', alignItems: 'flex-end', justifyContent: 'center', textAlign: 'center',
        opacity: p, transform: `scale(${0.94 + 0.06 * p})`, transformOrigin: `50% ${bottom - 40}px`,
      }}
    >
      <div style={{fontFamily: SOCIAL_FONT, fontWeight: 800, fontSize: 68, lineHeight: 1.12, color: '#fff', textShadow: OUTLINE, letterSpacing: '-0.005em'}}>
        {text}
      </div>
    </div>
  );
};

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
  shadow: '0 4px 18px rgba(0,0,0,.5)',
  cardShadow: '0 2px 6px rgba(13,13,13,.05), 0 26px 52px -18px rgba(0,60,120,.24)',
};

// Social reels: every graphic uses TikTok Sans instead of the brand fonts (Sam, 2026-11-04).
// Call once at the top of a reel file, before rendering.
export const useSocialFonts = () => {
  T.serif = SOCIAL_FONT;
  T.sans = SOCIAL_FONT;
};

export const BRUSH = 'M3 19 C 28 11, 96 5, 190 2 C 196 1, 200 4, 197 8 C 186 10, 120 13, 60 17 C 38 19, 18 21, 9 25 C 3 27, 0 22, 3 19 Z';

const easeOut = Easing.bezier(0.2, 0.7, 0.2, 1);
const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);

// 0..1 progress of an entrance that starts at `at` seconds and lasts `dur`
export const enter = (t, at, dur = 0.2, ease = easeOut) =>
  interpolate(t, [at, at + dur], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});

// Graphics enter: slide up 40 px and fade (sheet), plus a de-blur and a 97% -> 100% settle for a premium feel
export const riseStyle = (p) => ({
  opacity: p,
  transform: `translateY(${(1 - p) * 40}px) scale(${0.97 + 0.03 * p})`,
  filter: p < 1 ? `blur(${(1 - p) * 10}px)` : 'none',
});

// ---------- Premium layer (v2) ----------

// Glass surface: frosted white over the animated plate, a bright top edge and a soft blue-tinted shadow
export const glass = {
  background: 'linear-gradient(180deg, rgba(255,255,255,.86), rgba(255,255,255,.70))',
  backdropFilter: 'blur(22px) saturate(140%)',
  WebkitBackdropFilter: 'blur(22px) saturate(140%)',
  border: '1.5px solid rgba(255,255,255,.95)',
  boxShadow: '0 0 0 1px rgba(13,13,13,.05), 0 2px 6px rgba(13,13,13,.04), 0 30px 60px -22px rgba(0,60,120,.30), inset 0 1px 0 rgba(255,255,255,1)',
};

// Premium entrance: rise 40 px, fade, de-blur and settle from 97% (0.28 s, ease-out)
export const premiumEnter = (t, at, dur = 0.28) => {
  const p = enter(t, at, dur);
  return {p, style: {opacity: p, transform: `translateY(${(1 - p) * 40}px) scale(${0.97 + 0.03 * p})`, filter: `blur(${(1 - p) * 10}px)`}};
};

// Animated Higgsfield plate under a faint brand grid. plateFrames = frames in the looping clip.
export const PremiumCanvas = ({plate = 'plate_loop.mp4', plateFrames = 300, style}) => (
  <AbsoluteFill style={{backgroundColor: T.soft, overflow: 'hidden', ...style}}>
    <Loop durationInFrames={plateFrames}>
      <OffthreadVideo src={staticFile(plate)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    </Loop>
    <AbsoluteFill style={{background: 'rgba(251,252,255,.42)'}} />
    <AbsoluteFill
      style={{
        backgroundImage: `linear-gradient(rgba(230,230,230,.55) 1px, transparent 1px), linear-gradient(90deg, rgba(230,230,230,.55) 1px, transparent 1px)`,
        backgroundSize: '54px 54px', backgroundPosition: '-1px -1px',
      }}
    />
    <AbsoluteFill style={{background: 'radial-gradient(60% 35% at 88% 6%, rgba(117,223,238,.26), transparent 70%)'}} />
  </AbsoluteFill>
);

// Floating 3D icon (Higgsfield render, background removed): pops in, then bobs gently
export const FloatIcon = ({src, t, at, x, y, size = 200, phase = 0}) => {
  const p = enter(t, at, 0.45, Easing.bezier(0.34, 1.56, 0.64, 1)); // slight overshoot
  if (t < at) return null;
  const bob = Math.sin((t + phase) * 1.7) * 10;
  const tilt = Math.sin((t + phase) * 1.1) * 3;
  return (
    <Img
      src={staticFile(src)}
      style={{
        position: 'absolute', left: x, top: y, width: size, height: size, objectFit: 'contain',
        opacity: Math.min(1, p * 1.4), transform: `translateY(${bob + (1 - p) * 30}px) rotate(${tilt}deg) scale(${0.6 + 0.4 * p})`,
        filter: 'drop-shadow(0 24px 30px rgba(0,80,160,.25))', zIndex: 3,
      }}
    />
  );
};

// iOS-style app tile with a brand mark. kind: 'highlevel' | 'claude'
const TILES = {
  highlevel: {bg: '#ffffff', mark: 'logos/highlevel-mark.svg', pad: 0.2},
  claude: {bg: '#D97757', mark: 'logos/claude-mark.svg', pad: 0.2},
};
export const AppTile = ({kind, size = 220, style}) => {
  const k = TILES[kind];
  return (
    <div
      style={{
        width: size, height: size, borderRadius: size * 0.225, background: k.bg,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        boxShadow: `0 0 0 ${Math.max(1, size / 110)}px rgba(13,13,13,.06), 0 ${size * 0.09}px ${size * 0.2}px -${size * 0.05}px rgba(0,40,90,.35), inset 0 1px 0 rgba(255,255,255,.6)`,
        ...style,
      }}
    >
      <Img src={staticFile(k.mark)} style={{width: size * (1 - 2 * k.pad), height: size * (1 - 2 * k.pad), objectFit: 'contain'}} />
    </div>
  );
};

// A big logo tile that pops in when the brand is spoken and holds for at least `hold` seconds
export const LogoPop = ({kind, t, at, hold = 1.1, cx = 540, cy = 960, size = 240}) => {
  if (t < at || t > at + hold) return null;
  const p = enter(t, at, 0.4, Easing.bezier(0.34, 1.7, 0.64, 1));
  const out = interpolate(t, [at + hold - 0.12, at + hold], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', left: cx - size / 2, top: cy - size / 2, zIndex: 6, opacity: Math.min(1, p * 1.5) * out,
      transform: `scale(${0.55 + 0.45 * p}) rotate(${(1 - p) * -10}deg)`}}>
      <AppTile kind={kind} size={size} />
    </div>
  );
};

// Light sheen sweeping across a card once (place inside a position:relative, overflow:hidden parent)
export const Sheen = ({t, at, dur = 0.7}) => {
  const p = interpolate(t, [at, at + dur], [-0.4, 1.4], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.quad)});
  if (t < at || t > at + dur) return null;
  return (
    <div style={{position: 'absolute', inset: 0, pointerEvents: 'none', borderRadius: 'inherit', overflow: 'hidden'}}>
      <div style={{position: 'absolute', top: '-20%', bottom: '-20%', width: '35%', left: `${p * 100}%`,
        background: 'linear-gradient(100deg, transparent, rgba(255,255,255,.75), transparent)', transform: 'skewX(-18deg)'}} />
    </div>
  );
};

export const Canvas = ({style}) => (
  <AbsoluteFill
    style={{
      backgroundColor: T.soft,
      backgroundImage: `linear-gradient(${T.line} 1px, transparent 1px), linear-gradient(90deg, ${T.line} 1px, transparent 1px)`,
      backgroundSize: '54px 54px',
      backgroundPosition: '-1px -1px',
      ...style,
    }}
  >
    <AbsoluteFill style={{background: 'radial-gradient(60% 35% at 88% 6%, rgba(117,223,238,.30), transparent 70%)'}} />
  </AbsoluteFill>
);

export const Brush = ({progress, height = 46}) => (
  <div
    style={{
      position: 'absolute', left: '-4%', width: '108%', bottom: -height * 0.45, height,
      clipPath: `inset(-50% ${100 - progress * 100}% -50% 0)`, zIndex: -1,
    }}
  >
    <svg viewBox="0 0 200 28" preserveAspectRatio="none" style={{width: '100%', height: '100%', overflow: 'visible'}}>
      <path d={BRUSH} fill={T.blue} />
    </svg>
  </div>
);

// One caption cue. `bottom` is the y (px) of the bottom of the text block.
export const Caption = ({cue, t, bottom, ink = false}) => {
  // the very first cue is fully on screen in frame one (it doubles as the cover image)
  const p = cue.s <= 0.001 ? 1 : enter(t, cue.s, 0.14);
  const color = ink ? T.ink : '#fff';
  const textShadow = ink ? 'none' : T.shadow;
  const brush = cue.em ? enter(t, cue.emAt, 0.35, easeInOut) : 0;
  return (
    <div
      style={{
        position: 'absolute', left: 64, right: 64, top: 0, height: bottom,
        display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', alignItems: 'center',
        textAlign: 'center', color, textShadow, opacity: p,
        transform: `scale(${0.92 + 0.08 * p})`, transformOrigin: `50% ${bottom - 60}px`,
      }}
    >
      {cue.em ? (
        <>
          <div style={{fontFamily: T.sans, fontWeight: 600, fontSize: 52, lineHeight: 1.05, marginBottom: 6}}>{cue.setup}</div>
          <div style={{position: 'relative', isolation: 'isolate', fontFamily: T.serif, fontStyle: 'italic', fontWeight: 600, fontSize: 112, lineHeight: 1}}>
            {cue.em}
            <Brush progress={brush} />
          </div>
        </>
      ) : (
        <div style={{fontFamily: T.sans, fontWeight: 800, fontSize: 64, lineHeight: 1.05, letterSpacing: '-0.01em'}}>{cue.text}</div>
      )}
    </div>
  );
};

// Numbered card for steps and lists. state: 'on' | 'dim' | 'plain'. Dim cards collapse to one compact line.
export const StepCard = ({n, text, sub, chip, chipP = 0, p, state = 'plain'}) =>
  state === 'dim' ? (
    <div
      style={{
        ...riseStyle(p), opacity: p * 0.5,
        display: 'grid', gridTemplateColumns: '60px 1fr', alignItems: 'center', columnGap: 20,
        background: '#fff', borderRadius: 26, padding: '12px 30px', border: `2px solid ${T.line}`,
      }}
    >
      <div style={{fontFamily: T.serif, fontWeight: 600, fontSize: 50, lineHeight: 1, color: T.blue, textAlign: 'center'}}>{n}</div>
      <div style={{fontFamily: T.sans, fontWeight: 700, fontSize: 32, lineHeight: 1.2, color: T.ink, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis'}}>{text}</div>
    </div>
  ) : (
  <div
    style={{
      ...glass,
      ...riseStyle(p),
      display: 'grid', gridTemplateColumns: '84px 1fr', alignItems: 'center', columnGap: 26,
      borderRadius: 32, padding: '22px 34px',
      border: state === 'on' ? `2px solid ${T.blue}` : glass.border,
      boxShadow: state === 'on' ? `0 0 0 6px rgba(0,122,232,.14), ${glass.boxShadow}` : glass.boxShadow,
    }}
  >
    <div style={{fontFamily: T.serif, fontWeight: 600, fontSize: 76, lineHeight: 1, color: T.blue, textAlign: 'center'}}>{n}</div>
    <div>
      <div style={{fontFamily: T.sans, fontWeight: 700, fontSize: 42, lineHeight: 1.18, color: T.ink}}>{text}</div>
      {sub ? <div style={{fontFamily: T.serif, fontSize: 32, color: T.muted, marginTop: 4}}>{sub}</div> : null}
      {chip ? (
        <div
          style={{
            ...riseStyle(chipP), display: 'inline-flex', alignItems: 'center', gap: 10, marginTop: 14,
            fontFamily: T.sans, fontWeight: 600, fontSize: 30, color: T.blue,
            background: 'rgba(0,122,232,.10)', borderRadius: 999, padding: '8px 22px',
          }}
        >
          {typeof chip === 'string' ? <Tick size={26} /> : null}{chip}
        </div>
      ) : null}
    </div>
  </div>
);

export const Tick = ({size = 30, color = T.blue}) => (
  <svg width={size} height={size} viewBox="0 0 16 16" aria-hidden="true">
    <path d="M3 8.5l3 3 7-7" fill="none" stroke={color} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

export const fmtMoney = (v) => '$' + Math.round(v).toLocaleString('en-AU');

export const ProofCard = ({t, at, countFrom, countTo, countStart, countEnd, label, sub, chip, suffix = ''}) => {
  const p = enter(t, at);
  const c = interpolate(t, [countStart, countEnd], [countFrom, countTo], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic),
  });
  const done = t >= countEnd;
  return (
    <div
      style={{
        ...glass, ...riseStyle(p), position: 'absolute', left: 76, right: 76, top: 430,
        borderRadius: 32, padding: '56px 56px 60px', overflow: 'hidden',
      }}
    >
      <Sheen t={t} at={countEnd - 0.05} />
      <div style={{fontFamily: T.serif, fontSize: 40, color: T.muted}}>{label}</div>
      <div style={{fontFamily: T.serif, fontWeight: 800, fontSize: 138, lineHeight: 1, color: T.blue, marginTop: 22, fontVariantNumeric: 'tabular-nums', letterSpacing: '-0.01em'}}>
        {fmtMoney(c)}{done ? suffix : ''}
      </div>
      <div style={{fontFamily: T.serif, fontSize: 40, color: T.muted, marginTop: 18}}>{sub}</div>
      <div
        style={{
          ...riseStyle(enter(t, countEnd, 0.2)), display: 'inline-flex', alignItems: 'center', gap: 12, marginTop: 30,
          fontFamily: T.sans, fontWeight: 600, fontSize: 34, color: T.blue, background: 'rgba(0,122,232,.10)',
          borderRadius: 999, padding: '10px 26px',
        }}
      >
        <Tick size={30} />{chip}
      </div>
    </div>
  );
};

export const EndCard = ({t, at, question, button, url}) => {
  const p = enter(t, at);
  const b = enter(t, at + 0.15);
  return (
    <AbsoluteFill>
      <Canvas />
      <div style={{position: 'absolute', left: 90, right: 90, top: 560, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', gap: 56}}>
        <div style={{...riseStyle(p), fontFamily: T.serif, fontWeight: 600, fontSize: 104, lineHeight: 1.05, color: T.ink}}>{question}</div>
        <div style={{...riseStyle(b), background: T.orange, color: '#fff', fontFamily: T.sans, fontWeight: 700, fontSize: 54, padding: '36px 76px', borderRadius: 999, boxShadow: '0 22px 54px -18px rgba(255,89,0,.55)'}}>{button}</div>
        <div style={{...riseStyle(b), fontFamily: T.sans, fontSize: 38, color: T.muted}}>{url}</div>
      </div>
    </AbsoluteFill>
  );
};
