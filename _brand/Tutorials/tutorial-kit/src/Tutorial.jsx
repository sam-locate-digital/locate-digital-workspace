// The tutorial composition. Everything comes from src/timeline.json (pipeline/timeline.py), so a new video needs no
// code changes: base.mp4 is the cut (face and screen pieces, 2560x1440), and this file decides, frame by frame,
// what layout shows it and which graphics sit on top.
import React from 'react';
import {AbsoluteFill, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from 'remotion';
import tl from './timeline.json';
import {
  Canvas, ChapterCard, EndCard, LowerThird, Panel, T, TitleCard, easeInOut, enter, leave, lerp,
} from './tkit';

const FPS = tl.fps;
const W = 1920, H = 1080, BW = 2560, BH = 1440;
const clamp01 = (v) => Math.max(0, Math.min(1, v));
const at = (arr, t) => (arr || []).find((x) => x.s <= t && t < x.e);

const BaseVideo = ({style}) => (
  <OffthreadVideo src={staticFile('base.mp4')} muted style={{position: 'absolute', maxWidth: 'none', ...style}} />
);

// Face: full frame, wide or punched in (alternates at natural breaks, from timeline.shots)
const FaceView = ({t}) => {
  const shot = at(tl.shots, t);
  const z = shot && shot.mode === 'punch' ? tl.face.punch : 1;
  return (
    <AbsoluteFill style={{overflow: 'hidden', background: '#000'}}>
      <BaseVideo style={{left: 0, top: 0, width: W, height: H, transform: `scale(${z})`,
        transformOrigin: `${tl.face.fx * 100}% ${tl.face.fy * 100}%`}} />
    </AbsoluteFill>
  );
};

// Camera state on a screen segment, eased between keyframes
const camAt = (keys, t) => {
  if (!keys || !keys.length) return {z: 1, x: 0.5, y: 0.5};
  let i = 0;
  while (i < keys.length - 1 && keys[i + 1].t <= t) i++;
  const a = keys[i], b = keys[Math.min(i + 1, keys.length - 1)];
  if (b === a || b.t <= a.t) return a;
  const p = easeInOut(clamp01((t - a.t) / (b.t - a.t)));
  return {z: lerp(a.z, b.z, p), x: lerp(a.x, b.x, p), y: lerp(a.y, b.y, p)};
};

// Screen: the recording sits as a window on the brand canvas, and grows to fill the frame as it zooms in
const ScreenView = ({t, seg, si}) => {
  const cam = camAt((tl.cam.find((c) => c.seg === si) || {}).keys, t);
  const [bx, by, bw, bh] = seg.box;
  const ins = tl.screen.inset;
  const fit = Math.min(W / bw, H / bh);
  const p = clamp01((cam.z - 1) / 0.25);
  const fw = lerp(bw * fit * ins, W, p), fh = lerp(bh * fit * ins, H, p);
  const cs = fit * lerp(ins, 1, p) * cam.z;
  const cw = bw * cs, ch = bh * cs;
  const place = (win, content, focus) => {
    const want = win / 2 - focus * content;
    return content >= win ? Math.min(0, Math.max(win - content, want)) : (win - content) / 2;
  };
  const left = place(fw, cw, cam.x), top = place(fh, ch, cam.y);
  const settle = seg.s > 0 ? interpolate(t, [seg.s, seg.s + 0.35], [0.975, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeInOut}) : 1;
  return (
    <AbsoluteFill>
      {p < 1 || fw < W || fh < H ? <Canvas /> : null}
      <div style={{position: 'absolute', left: (W - fw) / 2, top: (H - fh) / 2, width: fw, height: fh, overflow: 'hidden',
        background: '#fff', borderRadius: lerp(18, 0, p), transform: `scale(${settle})`,
        boxShadow: p < 1 ? `0 0 0 1px rgba(13,13,13,${0.08 * (1 - p)}), 0 30px 70px -24px rgba(0,60,120,${0.35 * (1 - p)})` : 'none'}}>
        <BaseVideo style={{left: left - bx * cs, top: top - by * cs, width: BW * cs, height: BH * cs}} />
      </div>
    </AbsoluteFill>
  );
};

// Split: the full-frame face shrinks into a rounded card on one side, a panel rises on the other, then it reverses
const SplitView = ({t, sp}) => {
  const m = Math.min(enter(t, sp.s, 0.5, easeInOut), leave(t, sp.e, 0.45));
  const left = sp.side === 'left';
  const card = {x: left ? W - 64 - 820 : 64, y: 64, w: 820, h: H - 128};
  const r = {x: lerp(0, card.x, m), y: lerp(0, card.y, m), w: lerp(W, card.w, m), h: lerp(H, card.h, m)};
  const vh = lerp(H, card.h * 1.12, m), vw = (vh * 16) / 9;
  const fit = (win, content, focus) => Math.min(0, Math.max(win - content, win / 2 - focus * content));
  const vl = lerp(0, fit(r.w, vw, tl.face.fx), m), vt = lerp(0, fit(r.h, vh, tl.face.fy), m);
  // the panel is gone before the face card starts growing back to full frame
  const pp = Math.min(enter(t, sp.s + 0.25, 0.4), leave(t, sp.e - 0.4, 0.25));
  return (
    <AbsoluteFill>
      <Canvas />
      <div style={{position: 'absolute', left: r.x, top: r.y, width: r.w, height: r.h, overflow: 'hidden', background: '#000',
        borderRadius: 28 * m, boxShadow: m > 0 ? `0 30px 70px -24px rgba(0,60,120,${0.35 * m})` : 'none'}}>
        <BaseVideo style={{left: vl, top: vt, width: vw, height: vh}} />
      </div>
      <div style={{position: 'absolute', top: 0, bottom: 0, left: left ? 64 : 884 + 40, right: left ? 884 + 40 : 64,
        display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <Panel panel={sp.panel} t={t} at={sp.s + 0.25} p={pp} />
      </div>
    </AbsoluteFill>
  );
};

const FullCard = ({t, cd}) => (
  <AbsoluteFill>
    <Canvas />
    <AbsoluteFill style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
      <Panel panel={cd} t={t} at={cd.s + 0.15} p={enter(t, cd.s + 0.15, 0.4)} big />
    </AbsoluteFill>
  </AbsoluteFill>
);

export const Tutorial = () => {
  const t = useCurrentFrame() / FPS;
  if (tl.end && t >= tl.end.s) return <EndCard t={t} end={tl.end} />;
  let si = tl.segments.findIndex((s) => s.s <= t && t < s.e);
  if (si < 0) si = tl.segments.length - 1;
  const seg = tl.segments[si];
  const ch = at(tl.chapters, t), cd = at(tl.cards, t);
  const it = tl.intro && t >= tl.intro.s && t < tl.intro.e ? tl.intro : null;
  const active = ch || it || cd;
  // back-to-back cards (lesson title straight into part 1) cut card to card instead of dipping to the video
  const fulls = [tl.intro, ...tl.chapters, ...tl.cards].filter(Boolean);
  const before = active && fulls.some((x) => x !== active && Math.abs(x.e - active.s) < 0.4);
  const after = active && fulls.some((x) => x !== active && Math.abs(x.s - active.e) < 0.4);
  const fp = active ? Math.min(before ? 1 : enter(t, active.s, 0.3, easeInOut), after ? 1 : leave(t, active.e, 0.3)) : 0;
  const sp = at(tl.splits, t);
  const label = active ? null : at(tl.labels, t);
  let base = null;
  if (fp < 1) {
    if (sp && seg.kind === 'face') base = <SplitView t={t} sp={sp} />;
    else if (seg.kind === 'face') base = <FaceView t={t} />;
    else base = <ScreenView t={t} seg={seg} si={si} />;
  }
  return (
    <AbsoluteFill style={{background: T.soft}}>
      {base}
      {active ? (
        <AbsoluteFill style={{opacity: fp, transform: `scale(${1.03 - 0.03 * enter(t, active.s, 0.45)})`}}>
          {ch ? <ChapterCard t={t} c={ch} /> : it ? <TitleCard t={t} it={it} /> : <FullCard t={t} cd={cd} />}
        </AbsoluteFill>
      ) : null}
      {label ? <LowerThird t={t} l={label} /> : null}
    </AbsoluteFill>
  );
};
