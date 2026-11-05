// "$200,000 from one simple automation" — v4 timeline.
// v4 = v2's graphics (glass canvas, split screens, step cards, proof card, 3D icons, logo tiles) with:
//   - Sam's three result screenshots on the canvas at 0:04–0:11 instead of numbered cards
//   - no "How to set it up" title
//   - every graphic in TikTok Sans (social font), captions white TikTok Sans with a black outline (v3 style)
import React from 'react';
import {AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import data from './data.json';
import {AppTile, FloatIcon, LogoPop, PremiumCanvas, ProofCard, SocialCaption, StepCard, T, enter, glass, riseStyle, useSocialFonts} from './kit';

useSocialFonts();

// Layout per stretch of time. mode: full | split | proof. zoom: [from, to] scale across the stretch.
const LAYOUT = [
  {s: 0, e: 4.14, mode: 'full', zoom: [1, 1.05]},
  {s: 4.14, e: 4.71, mode: 'full', zoom: [1.18, 1.18]},
  {s: 4.71, e: 11.21, mode: 'split', group: 'shots'},
  {s: 11.21, e: 14.5, mode: 'proof'},
  {s: 14.5, e: 16.41, mode: 'full', zoom: [1.18, 1.18]},
  {s: 16.41, e: 20.11, mode: 'split', group: 'steps'},
  {s: 20.11, e: 23.53, mode: 'full', zoom: [1, 1.05]},
  {s: 23.53, e: 27.72, mode: 'split', group: 'steps'},
  {s: 27.72, e: 28.77, mode: 'full', zoom: [1.18, 1.18]},
  {s: 28.77, e: 32.71, mode: 'split', group: 'steps'},
  {s: 32.71, e: 34.19, mode: 'full', zoom: [1.18, 1.18]},
  {s: 34.19, e: 35.12, mode: 'full', zoom: [1, 1.03]},
  {s: 35.12, e: 999, mode: 'split', group: 'steps'},
];

// Real booking results from the three automations, one at a time as each is described
const SHOTS = [
  {src: 'shots/automation-1.png', at: 4.76, until: 7.95},
  {src: 'shots/automation-2.png', at: 7.95, until: 9.48},
  {src: 'shots/automation-3.png', at: 9.48, until: 11.21},
];

const inlineTile = {display: 'inline-flex', verticalAlign: 'middle', margin: '0 10px 0 4px', position: 'relative', top: -3};

const STEPS = [
  {
    n: 1, text: 'A CRM that triggers on the last visit', at: 17.36, chipAt: 25.07,
    chip: (<>No CRM yet?<AppTile kind="highlevel" size={44} style={{...inlineTile, marginLeft: 10}} />HighLevel</>),
  },
  {n: 2, text: (<>Paste the prompt into<AppTile kind="claude" size={46} style={{...inlineTile, marginLeft: 12}} />Claude</>), at: 26.47},
  {n: 3, text: 'Add images and your brand voice', at: 30.3},
  {n: 4, text: 'Refresh every 3 to 6 months', at: 35.15},
];

// Spoken brands pop as big app tiles (instead of the word as a caption)
const LOGOS = data.cues.filter((c) => c.logo).map((c) => ({kind: c.logo, at: c.s}));

const SPLIT_TOP = 864; // canvas takes the top 45%
const FACE_OFFSET = -460; // shifts the 1920-tall frame so the face sits in the bottom 55%

const Footage = ({seg, t}) => {
  if (seg.mode === 'proof') return null;
  const video = <OffthreadVideo src={staticFile('aroll.mp4')} muted style={{width: 1080, height: 1920}} />;
  if (seg.mode === 'split') {
    return (
      <div style={{position: 'absolute', left: 0, right: 0, top: SPLIT_TOP, bottom: 0, overflow: 'hidden', background: '#111'}}>
        <div style={{position: 'absolute', left: 0, top: FACE_OFFSET, width: 1080, height: 1920}}>{video}</div>
      </div>
    );
  }
  const [a, b] = seg.zoom;
  const z = a + (b - a) * Math.min(1, Math.max(0, (t - seg.s) / (Math.min(seg.e, data.total) - seg.s)));
  return (
    <AbsoluteFill style={{overflow: 'hidden'}}>
      <div style={{width: 1080, height: 1920, transform: `scale(${z})`, transformOrigin: '50% 40%'}}>{video}</div>
    </AbsoluteFill>
  );
};

// Screenshot on a frosted glass card on the canvas; each one rises in and hard-cuts to the next
const Shot = ({src, at, until, t}) => {
  if (t < at || t >= until) return null;
  return (
    <div style={{...glass, ...riseStyle(enter(t, at, 0.28)), position: 'absolute', left: 48, right: 48, top: 320, borderRadius: 30, padding: '16px 18px', background: '#fff'}}>
      <Img src={staticFile(src)} style={{width: '100%', display: 'block'}} />
    </div>
  );
};

const SplitGraphic = ({seg, t}) => {
  if (seg.group === 'shots') {
    return (
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: SPLIT_TOP, overflow: 'hidden'}}>
        <PremiumCanvas />
        <FloatIcon src="icons/envelope.png" t={t} at={4.78} x={800} y={110} size={200} />
        <div style={{...riseStyle(enter(t, 4.74)), position: 'absolute', left: 64, top: 236, fontFamily: T.sans, fontWeight: 800, fontSize: 39, color: T.ink, whiteSpace: 'nowrap'}}>
          One client, three automated emails
        </div>
        {SHOTS.map((s) => <Shot key={s.src} {...s} t={t} />)}
        <div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: 2, background: 'rgba(13,13,13,.08)'}} />
      </div>
    );
  }
  // steps: no title, just the step cards building as they're said
  const shown = STEPS.filter((x) => t >= x.at);
  const latest = shown.length ? shown[shown.length - 1].n : 0;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: SPLIT_TOP, overflow: 'hidden'}}>
      <PremiumCanvas />
      {t < 35.15 ? <FloatIcon src="icons/checklist.png" t={t} at={16.5} x={820} y={110} size={200} phase={1.3} /> : null}
      {t >= 35.15 ? <FloatIcon src="icons/calendar.png" t={t} at={35.17} x={815} y={105} size={210} phase={2.1} /> : null}
      <div style={{position: 'absolute', left: 64, right: 64, top: 300, display: 'flex', flexDirection: 'column', gap: 18}}>
        {STEPS.map((x) =>
          t >= x.at ? (
            <StepCard
              key={x.n}
              n={x.n}
              text={x.text}
              chip={x.chip && t >= x.chipAt ? x.chip : null}
              chipP={x.chip ? enter(t, x.chipAt) : 0}
              p={enter(t, x.at, 0.28)}
              state={x.n === latest ? 'on' : 'dim'}
            />
          ) : null
        )}
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: 2, background: 'rgba(13,13,13,.08)'}} />
    </div>
  );
};

// CapCut pack helpers (clean footage + single overlays) kept from v3
export const OverlayStill = ({kind, index, logo}) => {
  if (kind === 'shot') {
    const s = SHOTS[index];
    return <AbsoluteFill><Shot {...s} t={s.at + 1} until={s.at + 2} /></AbsoluteFill>;
  }
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: 540 - 105, top: 380 - 105}}><AppTile kind={logo} size={210} /></div>
    </AbsoluteFill>
  );
};

// clean: footage only (zooms and split framing baked in). graphicsOnly: everything except footage and
// captions, on a transparent background — the two CapCut pack layers.
export const Reel = ({clean = false, graphicsOnly = false}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const seg = LAYOUT.find((x) => t >= x.s && t < x.e) || LAYOUT[LAYOUT.length - 1];
  const cue = data.cues.find((c) => t >= c.s && t < c.e && c.s < data.endCard);

  if (clean) {
    return <AbsoluteFill style={{background: '#000'}}><Footage seg={seg} t={t} /></AbsoluteFill>;
  }

  return (
    <AbsoluteFill style={{background: graphicsOnly ? 'transparent' : '#111'}}>
      {graphicsOnly ? null : <Footage seg={seg} t={t} />}
      {seg.mode === 'split' ? <SplitGraphic seg={seg} t={t} /> : null}
      {seg.mode === 'proof' ? (
        <AbsoluteFill>
          <PremiumCanvas />
          <ProofCard
            t={t}
            at={11.23}
            label="3 automated emails · this year"
            countFrom={0}
            countTo={200000}
            countStart={11.45}
            countEnd={13.25}
            suffix="+"
            sub="in additional revenue"
            chip="From existing customers"
          />
          <FloatIcon src="icons/chart.png" t={t} at={11.3} x={760} y={250} size={250} phase={0.6} />
        </AbsoluteFill>
      ) : null}
      {LOGOS.map((l) => (
        <LogoPop key={l.kind + l.at} kind={l.kind} t={t} at={l.at} hold={1.1}
          cx={540} cy={seg.mode === 'split' ? 960 : 1250} size={230} />
      ))}
      {cue && !cue.logo && t < data.endCard && !graphicsOnly ? (
        <SocialCaption cue={cue} t={t} bottom={seg.mode === 'split' ? 838 : 1470} />
      ) : null}
    </AbsoluteFill>
  );
};
