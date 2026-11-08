// Render the tutorial in one-minute chunks and join them. Chunks are cached by what's in them, so after a change
// request only the minutes that changed are rendered again.
//
// Usage (from the kit folder):  node render.mjs [--scale 0.5] [--concurrency 4] [--chunk 60] [--force]
// Output: out/video.mp4 (no audio; finish.py adds the mix). Preview renders (--scale 0.5) go to out/preview.mp4.
import {bundle} from '@remotion/bundler';
import {renderMedia, selectComposition} from '@remotion/renderer';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const arg = (name, dflt) => {
  const i = process.argv.indexOf(`--${name}`);
  return i > 0 ? process.argv[i + 1] : dflt;
};
const SCALE = Number(arg('scale', 1));
const CONC = Number(arg('concurrency', 4)); // 4 was ~70% faster than 2 on Sam's PC; 6 gained nothing
const CHUNK_S = Number(arg('chunk', 60));
const FORCE = process.argv.includes('--force');
const root = path.resolve('.');
const tl = JSON.parse(fs.readFileSync(path.join(root, 'src/timeline.json'), 'utf8'));
const fps = tl.fps;

const sha = (s) => createHash('sha1').update(s).digest('hex').slice(0, 12);
// code + assets fingerprint (any change to the components re-renders everything)
const files = (dir) => fs.readdirSync(dir, {withFileTypes: true}).flatMap((d) =>
  d.isDirectory() ? files(path.join(dir, d.name)) : [path.join(dir, d.name)]);
const codeKey = sha(files(path.join(root, 'src')).filter((f) => !f.endsWith('timeline.json'))
  .map((f) => fs.readFileSync(f, 'utf8')).join('|') + files(path.join(root, 'public'))
  .map((f) => `${path.relative(root, f)}:${fs.statSync(f).size}:${fs.statSync(f).mtimeMs}`).join('|'));
const globalKey = JSON.stringify({face: tl.face, screen: tl.screen, title: tl.title, kicker: tl.kicker,
  chapters: tl.chapters.length, scale: SCALE});

// everything in the timeline that has times, so a chunk's key only covers what can show in it
const timed = [];
const walk = (o) => {
  if (Array.isArray(o)) return o.forEach(walk);
  if (o && typeof o === 'object') {
    if (typeof o.s === 'number' || typeof o.t === 'number') timed.push(o);
    Object.values(o).forEach((v) => (typeof v === 'object' ? walk(v) : null));
  }
};
walk({segments: tl.segments, shots: tl.shots, cam: tl.cam, labels: tl.labels, chapters: tl.chapters, intro: tl.intro,
  cards: tl.cards, splits: tl.splits, end: tl.end});

console.log('bundling...');
const serveUrl = await bundle({entryPoint: path.join(root, 'src/index.jsx'), publicDir: path.join(root, 'public')});
const composition = await selectComposition({serveUrl, id: 'Tutorial'});
const total = composition.durationInFrames;
const per = Math.round(CHUNK_S * fps);
const dir = path.join(root, 'out', SCALE === 1 ? 'chunks' : `chunks_${SCALE}`);
fs.mkdirSync(dir, {recursive: true});
const list = [];
const started = Date.now();
for (let a = 0, i = 0; a < total; a += per, i++) {
  const b = Math.min(total - 1, a + per - 1);
  const w0 = a / fps - 2, w1 = (b + 1) / fps + 2;
  const inside = timed.filter((o) => {
    const s = typeof o.s === 'number' ? o.s : o.t;
    const e = typeof o.e === 'number' ? o.e : s;
    return s <= w1 && e >= w0;
  });
  const key = sha(codeKey + globalKey + JSON.stringify(inside) + `${a}-${b}`);
  const file = path.join(dir, `c${String(i).padStart(3, '0')}_${key}.mp4`);
  list.push(file);
  if (fs.existsSync(file) && !FORCE) {
    console.log(`chunk ${i} (${(a / fps).toFixed(0)}-${((b + 1) / fps).toFixed(0)}s) unchanged, skipped`);
    continue;
  }
  for (const old of fs.readdirSync(dir).filter((f) => f.startsWith(`c${String(i).padStart(3, '0')}_`))) fs.rmSync(path.join(dir, old));
  const t0 = Date.now();
  let last = -1;
  await renderMedia({
    composition, serveUrl, codec: 'h264', crf: 18, colorSpace: 'bt709', muted: true, concurrency: CONC, scale: SCALE,
    frameRange: [a, b], outputLocation: file + '.tmp.mp4',
    onProgress: ({progress}) => {
      const pct = Math.floor(progress * 10) * 10;
      if (pct !== last) { last = pct; process.stdout.write(`\rchunk ${i}: ${pct}%   `); }
    },
  });
  fs.renameSync(file + '.tmp.mp4', file);
  const secs = (Date.now() - t0) / 1000;
  console.log(`\rchunk ${i} (${(a / fps).toFixed(0)}-${((b + 1) / fps).toFixed(0)}s) rendered in ${secs.toFixed(0)}s ` +
    `(${((b - a + 1) / secs).toFixed(1)} fps)`);
}
const txt = path.join(dir, 'list.txt');
fs.writeFileSync(txt, list.map((f) => `file '${f.replace(/\\/g, '/')}'`).join('\n'));
const out = path.join(root, 'out', SCALE === 1 ? 'video.mp4' : 'preview.mp4');
execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', txt, '-c', 'copy',
  '-movflags', '+faststart', out]);
console.log(`${out}: ${total} frames, ${(total / fps).toFixed(2)}s, done in ${((Date.now() - started) / 60000).toFixed(1)} min`);
