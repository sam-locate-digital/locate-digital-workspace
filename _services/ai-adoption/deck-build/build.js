// Claude 101 workshop deck, rebuilt as one story in the Locate Digital glass-bubble style.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const lu = require("react-icons/lu");
const { applyTheme } = require("C:/Users/samue/.claude/skills/synced/5fe1f769-63bc-44cb-8645-905729bfe078_2531e392-cefd-4022-a1be-9eb548f6f2f5/pptx/scripts/apply_theme.js");

const OUT = process.argv[2] || "claude-101.pptx";
const A = (f) => path.join(__dirname, "assets", f);

const HEX = {
  ink: "0D0D0D", white: "FFFFFF", deep: "0058C4", soft: "F4F8FD", blue: "007AE8",
  cyan: "75DFEE", orange: "FF5900", muted: "63666B", line: "E6E6E6", pale: "9CC9F5", tint: "E8F2FD",
};
const THEME = {
  name: "Locate Digital",
  headFontFace: "Newsreader SemiBold",
  bodyFontFace: "Public Sans",
  colors: {
    dk1: HEX.ink, lt1: HEX.white, dk2: HEX.deep, lt2: HEX.soft,
    accent1: HEX.blue, accent2: HEX.cyan, accent3: HEX.orange, accent4: HEX.muted,
    accent5: HEX.line, accent6: HEX.pale, hlink: HEX.deep, folHlink: HEX.muted,
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.author = "Sam Cheng, Locate Digital";
pres.company = "Locate Digital";
pres.title = "Claude 101: ahead of the pack";
const C = pres.SchemeColor;

const W = 13.333, L = 0.75, R = 12.583, CW = R - L;
const LABEL = "Newsreader"; // small labels: Newsreader 400, sentence case, never tracked capitals

// ---------- layouts ----------
pres.defineSlideMaster({
  title: "Light",
  background: { color: HEX.white },
  objects: [
    { image: { path: A("logo-white.png"), x: L, y: 6.92, w: 0.88, h: 0.3 } },
    { placeholder: { options: { name: "eyebrow", type: "body", x: L, y: 0.55, w: 10, h: 0.32, fontFace: LABEL, fontSize: 14, color: C.accent1, margin: 0, valign: "top" }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: L, y: 0.88, w: CW, h: 0.78, fontSize: 32, color: C.text1, margin: 0, valign: "top", align: "left" }, text: "" } },
  ],
  slideNumber: { x: 12.08, y: 6.95, w: 0.5, h: 0.25, fontSize: 10, color: HEX.muted, align: "right" },
});
pres.defineSlideMaster({
  title: "Dark",
  background: { color: HEX.blue },
  objects: [
    { image: { path: A("logo-blue-crop.png"), x: L, y: 6.92, w: 0.88, h: 0.3 } },
    { placeholder: { options: { name: "eyebrow", type: "body", x: L, y: 1.7, w: 10, h: 0.32, fontFace: LABEL, fontSize: 15, color: C.background1, margin: 0, valign: "top" }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: L, y: 2.1, w: CW, h: 2.2, fontSize: 44, color: C.background1, margin: 0, valign: "top", align: "left" }, text: "" } },
  ],
  slideNumber: { x: 12.08, y: 6.95, w: 0.5, h: 0.25, fontSize: 10, color: HEX.white, align: "right" },
});

// ---------- icons ----------
const ICONS = {};
async function icon(name, color = HEX.blue) {
  const key = name + color;
  if (ICONS[key]) return ICONS[key];
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(lu[name], { color: "#" + color, size: 256, strokeWidth: 1.75 }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  ICONS[key] = "image/png;base64," + buf.toString("base64");
  return ICONS[key];
}

// ---------- helpers ----------
const FULL = ["bub-full-1.png", "bub-full-4.png", "bub-full-13.png", "bub-full-9.png", "bub-full-14.png", "bub-full-3.png", "bub-full-19.png", "bub-full-5.png", "bub-full-11.png"];
const CORNER = ["bub-corner-2.png", "bub-corner-6.png", "bub-corner-10.png", "bub-corner-15.png"];
let fullI = 0, cornerI = 0;
function bubbles(s, kind = "full") {
  // Neighbouring slides never share the same bubble art.
  if (kind === "none") return;
  if (kind === "full") s.addImage({ path: A(FULL[fullI++ % FULL.length]), x: 0, y: 0, w: W, h: 7.5, objectName: "Glass bubbles" });
  else s.addImage({ path: A(CORNER[cornerI++ % CORNER.length]), x: W - 2.7, y: -0.55, w: 3.2, h: 3.2, transparency: 25, objectName: "Glass bubbles" });
}
function T(s, text, o = {}) {
  s.addText(text, { isTextBox: true, margin: 0, fontSize: 14, color: C.text1, valign: "top", ...o });
}
const shadow = () => ({ type: "outer", color: "0058C4", opacity: 0.1, blur: 14, offset: 3, angle: 90 });
function card(s, x, y, w, h, o = {}) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, rectRadius: 0.12, fill: { color: o.fill || C.background1, transparency: o.transparency ?? 8 },
    line: { color: o.lineColor || C.accent5, width: o.lineWidth || 0.75 }, shadow: o.noShadow ? undefined : shadow(),
    objectName: o.name || "Card",
  });
}
async function iconDot(s, name, x, y, d = 0.52, o = {}) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: o.bg || HEX.tint }, line: { type: "none" }, objectName: "Icon circle" });
  const p = d * 0.27;
  s.addImage({ data: await icon(name, o.color || HEX.blue), x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p, objectName: name.replace(/^Lu/, "") + " icon" });
}
function light(section, eyebrow, title, bub = "full") {
  const s = pres.addSlide({ masterName: "Light", sectionTitle: section });
  bubbles(s, bub);
  s.addText(eyebrow, { placeholder: "eyebrow" });
  s.addText(title, { placeholder: "title" });
  return s;
}
function dark(section, eyebrow, title) {
  const s = pres.addSlide({ masterName: "Dark", sectionTitle: section });
  bubbles(s, "full");
  s.addText(eyebrow, { placeholder: "eyebrow" });
  s.addText(title, { placeholder: "title" });
  return s;
}
function source(s, text, y = 6.55) {
  T(s, text, { x: L, y, w: CW, h: 0.25, fontSize: 10, color: C.accent4 });
}
function handsOnBadge(s, text, x = L, y = 1.82) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 2.6, h: 0.38, rectRadius: 0.19, fill: { color: C.accent3 }, line: { type: "none" }, objectName: "Hands-on badge" });
  T(s, text, { x, y, w: 2.6, h: 0.38, fontSize: 12, bold: true, color: C.background1, align: "center", valign: "middle" });
}
function numberedList(s, items, x, y, w, o = {}) {
  // Single digits (1, 2, 3), per the brand rules; thin rules between rows.
  const rowH = o.rowH || 0.62;
  items.forEach((it, i) => {
    const yy = y + i * rowH;
    s.addShape(pres.shapes.LINE, { x, y: yy, w, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
    T(s, String(i + 1), { x, y: yy + 0.14, w: 0.4, h: 0.36, fontFace: LABEL, fontSize: 18, color: C.accent1 });
    const runs = Array.isArray(it)
      ? [{ text: it[0], options: { bold: true, breakLine: !!it[1] } }, ...(it[1] ? [{ text: it[1], options: { color: C.accent4 } }] : [])]
      : it;
    T(s, runs, { x: x + 0.5, y: yy + 0.14, w: w - 0.5, h: rowH - 0.18, fontSize: o.fontSize || 14 });
  });
  s.addShape(pres.shapes.LINE, { x, y: y + items.length * rowH, w, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
}

const S1 = "Welcome", S2 = "1 · The shift", S3 = "2 · The problem", S4 = "3 · Choose your tools",
  S5 = "4 · How to prompt", S6 = "5 · Go further", S7 = "6 · Lock in the lead";

async function build() {
  // =================== WELCOME ===================
  pres.addSection({ title: S1 });

  // 1. Title
  {
    const s = dark(S1, "Training 101 · An introduction to Claude", "Get ahead of the pack.");
    T(s, "A practical half-day on using Claude safely and well, for the brokerages that intend to lead the next five years, not catch up to them.", { x: L, y: 3.55, w: 7.6, h: 1.0, fontSize: 18, color: C.background1 });
    T(s, "Prepared for [Practice name] · [Date]", { x: L, y: 4.85, w: 7, h: 0.35, fontFace: LABEL, fontSize: 15, color: C.background1 });
    s.addNotes("Open with the promise, not the agenda. Most of the industry is still experimenting with AI on its own, without training or rules. By the end of today this team will be in the small group that uses it well and has it governed. Everything in the next three hours builds toward that.\n\nSwap in the practice name and date before the session.");
  }

  // 2. Agenda
  {
    const s = light(S1, "Today", "Six chapters, two hands-on blocks", "corner");
    const rows = [
      ["0:00", "Welcome", "Who's running today and why it matters"],
      ["0:05", "1  The shift", "Where the broking market and AI adoption actually stand"],
      ["0:17", "2  The problem", "The squeeze on brokerages, the real risk and what standing still costs"],
      ["0:35", "3  Choose your tools", "Claude vs Copilot vs ChatGPT, the Claude toolkit and who uses what"],
      ["0:55", "4  How to prompt", "The five-part brief, then hands-on: write your own prompts", true],
      ["1:25", "Break", "10 minutes"],
      ["1:35", "5  Go further", "Memory, skills, planning, models and a live demo"],
      ["2:15", "6  Lock in the lead", "Settings, client data, then hands-on: draft your AI use policy", true],
      ["2:50", "Questions", "What happens next. Finish at 3:00"],
    ];
    const y0 = 1.95, rh = 0.5;
    rows.forEach(([t, h, d, hands], i) => {
      const y = y0 + i * rh;
      if (i % 2 === 0) s.addShape(pres.shapes.RECTANGLE, { x: L, y, w: CW, h: rh, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Row band" });
      T(s, t, { x: L + 0.2, y, w: 0.9, h: rh, fontFace: LABEL, fontSize: 15, color: C.accent1, valign: "middle" });
      T(s, h, { x: L + 1.2, y, w: 3.0, h: rh, fontSize: 14, bold: true, valign: "middle" });
      T(s, d, { x: L + 4.3, y, w: 6.2, h: rh, fontSize: 13, color: C.accent4, valign: "middle" });
      if (hands) {
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: R - 1.45, y: y + 0.11, w: 1.3, h: 0.28, rectRadius: 0.14, fill: { color: C.accent3 }, line: { type: "none" }, objectName: "Hands-on tag" });
        T(s, "Hands-on", { x: R - 1.45, y: y + 0.11, w: 1.3, h: 0.28, fontSize: 11, bold: true, color: C.background1, align: "center", valign: "middle" });
      }
    });
    s.addNotes("About three hours. A guide, not a script: adjust live, but protect the two hands-on blocks above everything else. If you're running short, trim chapter 5 before you touch the policy exercise.\n\nThe story runs in three moves: the market has shifted (chapters 1–2), here's how to get ahead (3–5), and here's how to lock that lead in (6).");
  }

  // 3. Who's running this session
  {
    const s = light(S1, "Your facilitator", "Who's running this session", "none");
    s.addImage({ path: A("sam.jpg"), x: 7.35, y: 0, w: 5.983, h: 7.5, sizing: { type: "cover", w: 5.983, h: 7.5 }, objectName: "Sam Cheng photo" });
    T(s, "Sam Cheng", { x: L, y: 2.05, w: 6, h: 0.5, fontFace: "Newsreader SemiBold", fontSize: 24 });
    T(s, "Founder, Locate Digital", { x: L, y: 2.55, w: 6, h: 0.35, fontFace: LABEL, fontSize: 15, color: C.accent1 });
    numberedList(s, [
      ["Background in marketing technology", "Ads, tracking, reporting and the systems behind them"],
      ["Leads Locate Digital's own AI rollout", "Claude runs our reporting, content, research and admin"],
      ["Teaches what we use", "Everything today comes from real day-to-day work, not theory"],
    ], L, 3.2, 6.1, { rowH: 0.82 });
    card(s, L, 5.85, 6.1, 0.75, { fill: C.background2, noShadow: true, transparency: 0 });
    T(s, "\u201CWe use Claude to run our own agency every day. What we teach is what we use.\u201D", { x: L + 0.25, y: 5.85, w: 5.7, h: 0.75, fontFace: "Newsreader", italic: true, fontSize: 15, color: C.text2, valign: "middle" });
    s.addNotes("Why I built this session: Sam, this is your own story to tell. Suggested shape: what you saw AI do for your own business, and why you decided to teach it rather than just use it yourself. Keep it to two or three sentences told live.");
  }

  // =================== 1 · THE SHIFT ===================
  pres.addSection({ title: S2 });

  // 4. Landscape: the broker channel
  {
    const s = light(S2, "Chapter 1 · The shift", "The broker channel has never been bigger");
    T(s, "More borrowers are coming through brokers than ever before, and more brokers are competing for them.", { x: L, y: 1.75, w: 9, h: 0.4, fontSize: 15, color: C.accent4 });
    const stats = [
      ["81.6%", "of new home loans went through a broker in the June 2026 quarter, up from 53.9% in 2018"],
      ["24,116", "brokers in Australia, 9.1% more than a year earlier"],
      ["$495.6b", "in residential loans settled through brokers in 2025, up 23.5%"],
      ["38 sec", "between broker-written home loans, on average, across 2025"],
    ];
    const cw = (CW - 3 * 0.3) / 4;
    stats.forEach(([n, d], i) => {
      const x = L + i * (cw + 0.3);
      card(s, x, 2.55, cw, 3.4);
      T(s, n, { x: x + 0.3, y: 2.95, w: cw - 0.6, h: 0.9, fontFace: "Newsreader SemiBold", fontSize: 36, color: i === 0 ? C.accent1 : C.text1 });
      T(s, d, { x: x + 0.3, y: 4.0, w: cw - 0.6, h: 1.7, fontSize: 14, color: C.accent4 });
    });
    source(s, "Sources: MFAA Quarterly Market Share Report, June 2026 quarter; MFAA State of Mortgage & Finance Broking Report 2026 (Cotality), calendar 2025.");
    s.addNotes("The broking industry is in the best position it has ever been in. More than four in five home loans now go through a broker. But the number of brokers grew 9.1% in a single year, so the share of the pie is bigger and so is the queue for it.\n\nThe question for the rest of today: when demand and competition both go up, what separates the brokerages that pull ahead from the ones that just get busier?");
  }

  // 5. Landscape: AI use by business size
  {
    const s = light(S2, "Chapter 1 · The shift", "AI is already at work, but unevenly");
    s.addChart(pres.charts.BAR, [{ name: "Businesses using AI", labels: ["Micro (1–4 staff)", "Small (5–19)", "Mid-market (50–199)", "Large (200+)"], values: [33, 38, 60, 80] }], {
      x: L, y: 1.85, w: 6.9, h: 4.55, barDir: "bar", catAxisOrientation: "maxMin",
      chartColors: [HEX.blue, HEX.blue, HEX.pale, HEX.pale],
      showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: '0"%"', dataLabelFontSize: 13, dataLabelColor: HEX.ink, dataLabelFontFace: "+mn-lt",
      catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 13, catAxisLabelFontFace: "+mn-lt", catAxisLineShow: false,
      valAxisHidden: true, valAxisMaxVal: 100, valGridLine: { style: "none" }, catGridLine: { style: "none" },
      showLegend: false, showTitle: true, title: "Australian businesses using AI, by size", titleFontSize: 14, titleColor: HEX.ink, titleFontFace: "+mn-lt", barGapWidthPct: 55,
    });
    const x2 = 8.1, w2 = R - x2;
    card(s, x2, 1.95, w2, 2.05);
    T(s, "64%", { x: x2 + 0.3, y: 2.15, w: 2, h: 0.75, fontFace: "Newsreader SemiBold", fontSize: 36, color: C.accent1 });
    T(s, "of finance and insurance businesses use AI, second only to property services at around 70%.", { x: x2 + 0.3, y: 2.9, w: w2 - 0.6, h: 0.95, fontSize: 13, color: C.accent4 });
    card(s, x2, 4.25, w2, 2.05);
    T(s, "69% vs 22%", { x: x2 + 0.3, y: 4.45, w: w2 - 0.6, h: 0.75, fontFace: "Newsreader SemiBold", fontSize: 36, color: C.text1 });
    T(s, "of Australian employees use AI regularly at work, but only 22% have had any formal training.", { x: x2 + 0.3, y: 5.2, w: w2 - 0.6, h: 0.95, fontSize: 13, color: C.accent4 });
    source(s, "Sources: NAB/MYOB 2026 (sector, size); Plain English Foundation / National AI Centre, Jan 2026 (employees). Via Locate Digital market research, Sept 2026.");
    s.addNotes("Most brokerages sit in the two dark bars: micro and small businesses, where adoption is lowest. Large banks and aggregators are already past 80%.\n\nThat gap is the opportunity, not a reason to feel behind. A ten-person brokerage can move faster than a bank. And the second card is the real story: most people using AI at work have never been shown how.");
  }

  // 6. Stats and facts: brokers and AI
  {
    const s = light(S2, "Chapter 1 · The shift", "Brokers believe in AI. Very few have a plan for it");
    const stats = [
      ["86%", "say AI will be essential or helpful to running their business within two years"],
      ["37%", "use AI tools regularly and confidently today"],
      ["65%", "have no documented AI strategy"],
      ["3%", "have formal policies for safe, regulation-aligned AI use"],
    ];
    const cw = (CW - 0.3) / 2, ch = 1.6;
    stats.forEach(([n, d], i) => {
      const x = L + (i % 2) * (cw + 0.3), y = 1.95 + Math.floor(i / 2) * (ch + 0.3);
      card(s, x, y, cw, ch, i === 3 ? { lineColor: C.accent1, lineWidth: 1.5 } : {});
      T(s, n, { x: x + 0.35, y: y + 0.3, w: 1.9, h: 1.0, fontFace: "Newsreader SemiBold", fontSize: 44, color: i === 3 ? C.accent1 : C.text1, valign: "middle" });
      T(s, d, { x: x + 2.35, y: y + 0.3, w: cw - 2.65, h: 1.0, fontSize: 15, valign: "middle" });
    });
    T(s, [
      { text: "The age gap: ", options: { bold: true } },
      { text: "54% of brokers under 50 use AI at work, against 27% of those over 50." },
    ], { x: L, y: 5.85, w: CW, h: 0.4, fontSize: 14 });
    source(s, "Sources: Connective, AI Readiness in Australian Broking, March 2026 (300+ mortgage, commercial and asset finance brokers); FBAA member poll, March 2026.");
    s.addNotes("This is the slide to slow down on. Nearly nine in ten brokers think AI matters. Barely a third use it with confidence. Two thirds have no strategy. And only 3% have a formal policy for using it safely.\n\nThat 3% is the head of the pack, and it's where this team will be by the end of today. Come back to this number at the close.\n\nNote: an earlier version of this deck quoted '55% of mortgage brokers use AI daily'. That figure came from a US survey, so it has been replaced with Australian data.");
  }

  // =================== 2 · THE PROBLEM ===================
  pres.addSection({ title: S3 });

  // 7. The existing pain
  {
    const s = light(S3, "Chapter 2 · The problem", "What's squeezing brokerages right now", "corner");
    const pains = [
      ["LuHourglass", "Files take longer", "The average home loan now takes around 20 hours to write, up from 15 five years ago."],
      ["LuTrendingDown", "Clawbacks bite harder", "The median broker lost $11,442 to clawbacks in 2025, up 16.5% on the year before."],
      ["LuUsers", "More competition", "24,116 brokers, up 9.1% in a year, chasing the same borrowers and referral partners."],
      ["LuFileSearch", "Checking by eye", "Payslips, bank statements, ID and serviceability inputs, cross-checked by hand on every file."],
      ["LuMegaphone", "Marketing gets bumped", "Social posts, EDMs and follow-ups are the first thing dropped when the pipeline is busy."],
      ["LuScale", "More compliance", "Best Interest Duty, responsible lending and, from 10 December 2026, new Privacy Act rules on AI-assisted decisions."],
    ];
    const cw = (CW - 2 * 0.3) / 3, ch = 2.1;
    for (let i = 0; i < pains.length; i++) {
      const [ic, h, d] = pains[i];
      const x = L + (i % 3) * (cw + 0.3), y = 1.95 + Math.floor(i / 3) * (ch + 0.3);
      card(s, x, y, cw, ch);
      await iconDot(s, ic, x + 0.3, y + 0.3);
      T(s, h, { x: x + 1.0, y: y + 0.38, w: cw - 1.2, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x + 0.3, y: y + 1.0, w: cw - 0.6, h: 1.0, fontSize: 13, color: C.accent4 });
    }
    source(s, "Sources: BrokerEngine via The Adviser (time per loan); MFAA State of Mortgage & Finance Broking Report 2026; Privacy Act amendments on automated decisions.");
    s.addNotes("Ask the room before you click through: which of these is the biggest drain in your week? Then use their answer in every example for the rest of the day.\n\nThe common thread is that every one of these steals time from the work only a broker can do: advice, relationships and judgement. Swap in your own team's pain points if they differ.");
  }

  // 8. Problem statement
  {
    const s = dark(S3, "The problem", "Your team is already using AI. Nobody has shown them how, and nobody is checking.");
    T(s, "That's why it can feel slower than doing the job yourself, and why the risk sits with the licence holder, not the software vendor. It's a workflow problem, not an AI problem.", { x: L, y: 4.6, w: 8.2, h: 1.1, fontSize: 18, color: C.background1 });
    s.addNotes("Let this land. Pause after reading the headline.\n\nMost people in the room have tried AI. Many will say it wasn't worth it: the output was generic, or checking it took longer than writing it. That isn't the tool failing. It's what happens when nobody has been shown how to brief it, and there's no agreed way of working.");
  }

  // 9. The real risk
  {
    const s = light(S3, "Chapter 2 · The problem", "Under the NCCP, the risk stays with you");
    card(s, L, 1.95, 4.3, 4.3, { fill: C.background2, transparency: 0 });
    T(s, "74%", { x: L + 0.4, y: 2.3, w: 3.5, h: 1.1, fontFace: "Newsreader SemiBold", fontSize: 60, color: C.accent1 });
    T(s, [
      { text: "of Australian advice practices now use AI, up from 45% a year ago. Only ", options: {} },
      { text: "39%", options: { bold: true, color: C.accent1 } },
      { text: " have a policy governing how it's used.", options: {} },
    ], { x: L + 0.4, y: 3.55, w: 3.5, h: 1.6, fontSize: 15 });
    const x2 = 5.45, w2 = R - x2;
    const rows = [
      ["LuShieldCheck", "Best Interest Duty can't be outsourced", "Responsible lending and BID obligations stay with a person, whatever tool drafted the work."],
      ["LuAlertTriangle", "Ungoverned use is your exposure", "A staff member checking documents or drafting advice in an unapproved tool leaves the licence holder carrying the risk."],
      ["LuLock", "Free tools and client data don't mix", "The FBAA advises members never to upload client or company personal data into public AI tools."],
    ];
    for (let i = 0; i < rows.length; i++) {
      const [ic, h, d] = rows[i], y = 1.95 + i * 1.3;
      await iconDot(s, ic, x2, y + 0.05);
      T(s, h, { x: x2 + 0.75, y, w: w2 - 0.75, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x2 + 0.75, y: y + 0.42, w: w2 - 0.75, h: 0.75, fontSize: 13, color: C.accent4 });
    }
    T(s, "Governed properly, the same task becomes a time-saver instead of an exposure.", { x: x2, y: 5.85, w: w2, h: 0.4, fontSize: 15, bold: true, color: C.text2 });
    source(s, "Sources: Locate Digital market research, Sept 2026 (advice practices); FBAA guidance to members, March 2026.");
    s.addNotes("This is the part a principal cares about most. Adoption has outrun governance across the whole finance sector. Under the NCCP Act that gap sits with the licence holder, not the AI vendor.\n\nThe point isn't to scare anyone off AI. It's that the brokerages who get this right will be faster and safer at the same time.");
  }

  // 10. Total expenditure: what standing still costs
  {
    const s = light(S3, "Chapter 2 · The problem", "What standing still costs, per broker, per year", "corner");
    const steps = [
      ["~35", "loans settled per broker a year", "838,815 loans ÷ 24,116 brokers"],
      ["× 20 hrs", "of work per loan", "≈ 700 hours a year on files"],
      ["20%", "of that time handed to Claude", "≈ 140 hours, or 3.5 working weeks"],
      ["~$16,000", "of broker time back each year", "at ~$114 an hour of broker revenue"],
    ];
    const cw = 2.62, gap = 0.45;
    for (let i = 0; i < steps.length; i++) {
      const [n, h, d] = steps[i], x = L + i * (cw + gap);
      const last = i === steps.length - 1;
      card(s, x, 1.95, cw, 2.35, last ? { lineColor: C.accent1, lineWidth: 1.5 } : {});
      T(s, n, { x: x + 0.25, y: 2.2, w: cw - 0.5, h: 0.75, fontFace: "Newsreader SemiBold", fontSize: 32, color: last ? C.accent1 : C.text1 });
      T(s, h, { x: x + 0.25, y: 3.0, w: cw - 0.5, h: 0.6, fontSize: 14, bold: true });
      T(s, d, { x: x + 0.25, y: 3.6, w: cw - 0.5, h: 0.55, fontSize: 12, color: C.accent4 });
      if (!last) s.addImage({ data: await icon("LuArrowRight", HEX.pale), x: x + cw + 0.07, y: 2.95, w: 0.3, h: 0.3, objectName: "Arrow" });
    }
    // Total expenditure comparison
    card(s, L, 4.6, CW, 1.65, { fill: C.background2, transparency: 0, noShadow: true });
    T(s, [
      { text: "Total expenditure for a five-broker office", options: { bold: true, breakLine: true } },
      { text: "Time at stake: about 700 hours and $80,000 a year. Claude Team seats for five people: about US$1,200–1,500 a year.", options: { color: C.accent4 } },
    ], { x: L + 0.35, y: 4.78, w: 8.2, h: 1.3, fontSize: 15, valign: "middle" });
    T(s, "~50×", { x: 9.3, y: 4.75, w: 2.0, h: 0.85, fontFace: "Newsreader SemiBold", fontSize: 40, color: C.accent1, align: "right" });
    T(s, "return on the licence cost", { x: 9.3, y: 5.55, w: 2.0, h: 0.5, fontSize: 12, color: C.accent4, align: "right" });
    source(s, "Illustrative. MFAA 2026: median upfront $126,941 + trail $77,894 over 1,800 hours. BrokerEngine: hours per loan. 20% is an assumption. claude.com/pricing, Oct 2026.");
    s.addNotes("Walk through this left to right and invite them to argue with the assumptions. That's the point: the maths works even if you halve every number.\n\n35 loans a broker is a rough industry average (total loans divided by total brokers). 20 hours a file is contact to settlement. 20% is a conservative share of that work for AI to draft or pre-check, with the broker still reviewing everything. $114 an hour is median upfront plus trail revenue spread over a 1,800-hour working year.\n\nAgainst that, a Claude Team seat is US$20–25 a month. The real cost of AI isn't the licence. It's carrying on without it.");
  }

  // 11. The ultimatum
  {
    const s = dark(S3, "The choice", "Two brokerages, three years from now.");
    const colW = 5.65, y = 3.35, h = 2.95;
    const cols = [
      ["The one that waited", ["Still checking documents line by line", "Marketing goes out when there's a spare hour", "Staff on free tools nobody approved", "Competing on rate, because that's all that's left"]],
      ["The one that moved first", ["AI pre-checks every file, a broker signs off", "Posts and EDMs out every week, in the firm's voice", "One approved tool, a written policy", "More clients with the same team, without another hire"]],
    ];
    cols.forEach(([h1, items], i) => {
      const x = L + i * (colW + 0.5);
      card(s, x, y, colW, h, { fill: C.background1, transparency: i === 0 ? 82 : 0, lineColor: C.background1, noShadow: i === 0 });
      const ink = i === 0 ? C.background1 : C.text1;
      T(s, h1, { x: x + 0.35, y: y + 0.25, w: colW - 0.7, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 20, color: i === 0 ? C.background1 : C.accent1 });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 16 }, breakLine: j < items.length - 1 } })), { x: x + 0.35, y: y + 0.85, w: colW - 0.7, h: h - 1.05, fontSize: 15, color: ink, paraSpaceAfter: 8 });
    });
    s.addNotes("This is the ultimatum. Both brokerages have the same market, the same lenders and the same borrowers. The only difference is what they did in the next twelve months.\n\nAsk the room: which one are you building? Then move straight into 'what you'll get today', which is the first step toward the right-hand column.");
  }

  // 12. What you'll get out of today
  {
    const s = light(S3, "Your head start", "By 3pm, you'll be ahead of where most of the industry is");
    const items = [
      ["LuMessageSquare", "Brief Claude like a capable junior", "Not like a search engine. Clear context, a clear task and an example of good."],
      ["LuRepeat", "A habit that works first time", "A prompting routine that gets a usable answer on the first or second try, not the fifth."],
      ["LuCompass", "The right tool for every job", "Which Claude tool to open for which task, and for which person on your team."],
      ["LuClipboardCheck", "Your AI use policy, drafted", "What's allowed, what needs sign-off and what's off-limits, agreed as a team."],
    ];
    const cw = (CW - 3 * 0.3) / 4;
    for (let i = 0; i < items.length; i++) {
      const [ic, h, d] = items[i], x = L + i * (cw + 0.3);
      card(s, x, 1.95, cw, 3.55);
      await iconDot(s, ic, x + 0.3, 2.25, 0.6);
      T(s, h, { x: x + 0.3, y: 3.05, w: cw - 0.6, h: 0.75, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x + 0.3, y: 3.85, w: cw - 0.6, h: 1.5, fontSize: 13, color: C.accent4 });
    }
    T(s, [
      { text: "No technical skills needed. ", options: { bold: true } },
      { text: "If you can write an email, you can do everything in today's session." },
    ], { x: L, y: 5.85, w: CW, h: 0.4, fontSize: 15 });
    s.addNotes("The aim: everyone leaves as the person in their organisation who actually knows how to use this. The go-to, not just another user.\n\nAdjust the finish time on the title if your session doesn't end at 3pm.");
  }

  // =================== 3 · CHOOSE YOUR TOOLS ===================
  pres.addSection({ title: S4 });

  // 13. Claude vs Copilot vs ChatGPT
  {
    const s = light(S4, "Chapter 3 · Choose your tools", "Claude, Copilot or ChatGPT: all three beat a free account", "corner");
    const hd = (t, c) => ({ text: t, options: { bold: true, color: c || HEX.white, fill: { color: HEX.blue }, fontSize: 13, valign: "middle" } });
    const lab = (t) => ({ text: t, options: { bold: true, fill: { color: HEX.soft }, fontSize: 12, valign: "middle" } });
    const c = (t) => ({ text: t, options: { fontSize: 12, color: HEX.ink, valign: "middle" } });
    const rows = [
      [hd(""), hd("Claude"), hd("Microsoft 365 Copilot"), hd("ChatGPT")],
      [lab("Where it lives"), c("Web, desktop and mobile. Connects to Microsoft 365 and Google"), c("Inside Word, Excel, Outlook and Teams"), c("Web, desktop and mobile. Connects to common apps")],
      [lab("Strongest at"), c("Long documents, careful writing and following detailed instructions"), c("Working across your Microsoft email, files and meetings"), c("General drafting, research and image generation")],
      [lab("Business plan"), c("Team: US$20–25 per user a month"), c("Copilot Business: about US$21 per user a month, plus a Microsoft 365 licence"), c("Business: about US$25–30 per user a month")],
      [lab("Client data"), c("Business plans aren't used to train models by default"), c("Covered by Microsoft's enterprise data protection"), c("Business plans aren't used to train models by default")],
      [lab("Pick it if"), c("You want one capable assistant for drafting, documents and repeatable workflows"), c("Your firm lives in Outlook and Teams and wants AI inside them"), c("Your team already knows it and needs broad, general use")],
    ];
    s.addTable(rows, { x: L, y: 1.9, w: CW, colW: [1.75, 3.36, 3.36, 3.36], rowH: [0.42, 0.72, 0.72, 0.72, 0.72, 0.72], border: { type: "solid", color: HEX.line, pt: 0.75 }, fill: { color: HEX.white }, margin: [0.06, 0.12, 0.06, 0.12], objectName: "Tool comparison" });
    source(s, "Prices in US dollars as at October 2026, annual vs monthly billing. Check current pricing with each vendor before you buy.", 6.5);
    s.addNotes("Be even-handed here. The room will have people who already use ChatGPT or have Copilot through Microsoft 365, and that's fine. Any business plan is a step up from staff using free personal accounts, which is where the real risk sits.\n\nWhy we teach Claude: it's strong on long documents and careful writing, which is most of a broker's paperwork, and its Projects, Skills and Docs make good work repeatable. Most of today's prompting habits transfer to the other two.\n\nPricing changes often. Confirm current prices on each vendor's site within a week of the session. Claude Team pricing is from claude.com/pricing; Copilot and ChatGPT figures are from vendor-reported and third-party sources.");
  }

  // 14. The Claude toolkit
  {
    const s = light(S4, "Chapter 3 · Choose your tools", "One assistant, six ways to work with it");
    const tools = [
      ["LuMessageSquare", "Claude (chat)", "Quick questions and bigger multi-step jobs in one conversation. Web, desktop and mobile."],
      ["LuFileText", "Claude Docs", "Build documents together, section by section. Comment, share by link and edit on mobile."],
      ["LuPresentation", "Claude Slides", "Ask for a deck, refine it together, then export to PowerPoint or PDF."],
      ["LuFolderOpen", "Projects", "A workspace that remembers your templates, files and instructions for ongoing work."],
      ["LuCode", "Claude Code", "Works inside your files and systems. This is where repeatable automation lives."],
      ["LuPalette", "Claude Design", "Visual work checked against your brand's colours, type and spacing."],
    ];
    const cw = (CW - 2 * 0.3) / 3, ch = 1.95;
    for (let i = 0; i < tools.length; i++) {
      const [ic, h, d] = tools[i], x = L + (i % 3) * (cw + 0.3), y = 1.9 + Math.floor(i / 3) * (ch + 0.3);
      card(s, x, y, cw, ch);
      await iconDot(s, ic, x + 0.3, y + 0.3);
      T(s, h, { x: x + 1.0, y: y + 0.38, w: cw - 1.2, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x + 0.3, y: y + 0.98, w: cw - 0.6, h: 0.85, fontSize: 13, color: C.accent4 });
    }
    T(s, [
      { text: "Platform update: ", options: { bold: true } },
      { text: "Claude chat and the old Cowork tab are now one interface. Claude handles simple questions and multi-step work in the same conversation." },
    ], { x: L, y: 6.18, w: CW, h: 0.45, fontSize: 12, color: C.accent4 });
    s.addNotes("Quick reference: fast question, use chat. Recurring written content, Docs. Need a deck, Slides. Ongoing client or topic work, Projects. Work inside your own files, repeated, Claude Code. Anything visual and on-brand, Design.\n\nIf anyone remembers choosing between 'Chat' and 'Cowork', that choice no longer exists. Anthropic merged them in September 2026.");
  }

  // 15. Which team member uses what
  {
    const s = light(S4, "Chapter 3 · Choose your tools", "Every role gets a different head start", "corner");
    const hd = (t) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color: HEX.blue }, fontSize: 13, valign: "middle" } });
    const lab = (t, d) => ({ text: [{ text: t, options: { bold: true, breakLine: true } }, { text: d, options: { color: HEX.muted, fontSize: 11 } }], options: { fill: { color: HEX.soft }, fontSize: 13, valign: "middle" } });
    const c = (t, o = {}) => ({ text: t, options: { fontSize: 12, color: HEX.ink, valign: "middle", ...o } });
    const tool = (t) => c(t, { bold: true, color: HEX.deep });
    const rows = [
      [hd("Role"), hd("Start with"), hd("First jobs to hand over"), hd("Stays with the person")],
      [lab("Principal or director", "Runs the practice"), tool("Projects, Docs"), c("Monthly performance summaries, policy drafts, business planning notes"), c("Final calls on risk, pricing and people")],
      [lab("Broker or credit adviser", "Client-facing"), tool("Chat, Projects"), c("Pre-meeting client summaries, needs-analysis notes, plain-English loan comparisons"), c("The recommendation, and Best Interest Duty")],
      [lab("Loan processor", "Credit assistant"), tool("Chat, Projects"), c("Document checklists, flagging mismatches across payslips and statements, lender policy look-ups"), c("Verifying every flag before a file is submitted")],
      [lab("Client services and admin", "Inbox and follow-ups"), tool("Chat, Routines"), c("Status updates, follow-up emails, inbox sorting, settlement reminders"), c("Anything that goes to a client")],
      [lab("Marketing or BDM", "Referral partners"), tool("Docs, Slides, Design"), c("Weekly social posts and EDMs, referral partner updates, event and webinar decks"), c("Approving every piece before it's published")],
    ];
    s.addTable(rows, { x: L, y: 1.9, w: CW, colW: [2.65, 1.85, 4.33, 3.0], rowH: [0.42, 0.74, 0.74, 0.74, 0.74, 0.74], border: { type: "solid", color: HEX.line, pt: 0.75 }, fill: { color: HEX.white }, margin: [0.06, 0.12, 0.06, 0.12], objectName: "Roles table" });
    s.addNotes("This is the page people photograph. Ask each person to find their row and pick one job from the third column to try this week.\n\nThe right-hand column matters as much as the third. AI prepares the work; your people make the decisions that matter. That line comes straight from how we set up every client.");
  }

  // 16. Docs and Slides
  {
    const s = light(S4, "Chapter 3 · Choose your tools", "Docs and Slides: build the work with Claude");
    const cols = [
      ["LuFileText", "Claude Docs", "A living document you build with Claude, not a one-off export you paste into Word.", ["Ask for a section, Claude drafts it, you comment and it revises in place", "Shareable by link and editable on mobile, so a colleague can review without the original chat", "Good for your AI use policy, captions, copywriting and document analysis"], "Use Docs instead of drafting in chat and copy-pasting. You keep the history in one place."],
      ["LuPresentation", "Claude Slides", "Ask for a presentation, Claude builds it, and you refine it together.", ["Same collaborative model as Docs, section by section", "Export to PowerPoint or PDF when you're ready to present", "Parts of today's deck were built this way"], "Ask for a first draft, then refine. For exact brand matching, pair it with Claude Design or your own template."],
    ];
    const cw = (CW - 0.4) / 2;
    for (let i = 0; i < cols.length; i++) {
      const [ic, h, lead, items, tip] = cols[i], x = L + i * (cw + 0.4);
      card(s, x, 1.9, cw, 4.45);
      await iconDot(s, ic, x + 0.35, 2.2, 0.6);
      T(s, h, { x: x + 1.15, y: 2.3, w: cw - 1.5, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 20 });
      T(s, lead, { x: x + 0.35, y: 3.0, w: cw - 0.7, h: 0.65, fontSize: 14, bold: true });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: j < items.length - 1 } })), { x: x + 0.35, y: 3.72, w: cw - 0.7, h: 1.5, fontSize: 13, color: C.accent4, paraSpaceAfter: 5 });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.35, y: 5.35, w: cw - 0.7, h: 0.8, rectRadius: 0.08, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Tip panel" });
      T(s, [{ text: "Tip: ", options: { bold: true, color: C.text2 } }, { text: tip }], { x: x + 0.5, y: 5.35, w: cw - 1.0, h: 0.8, fontSize: 12, valign: "middle" });
    }
    s.addNotes("If time allows, show the AI use policy draft from this workshop as a live Doc. It's the clearest example of a document that gets revisited over more than one sitting.");
  }

  // 17. Schedules and routines
  {
    const s = light(S4, "Chapter 3 · Choose your tools", "Routines: work that runs while you're with clients", "corner");
    T(s, "A prompt or task that runs on a schedule (daily, weekly or on a trigger) without you opening a session. It runs in Anthropic's cloud, so it fires even with your laptop closed.", { x: L, y: 1.9, w: 5.2, h: 1.5, fontSize: 15 });
    numberedList(s, [
      ["Available on Pro, Max, Team and Enterprise", ""],
      ["Start low-stakes and human-reviewed", "Same governance rule as everything else today"],
      ["Let it prepare, never send", "A person approves anything that reaches a client"],
    ], L, 3.6, 5.2, { rowH: 0.78 });
    const x2 = 6.55, w2 = R - x2;
    card(s, x2, 1.9, w2, 4.45);
    T(s, "An example week", { x: x2 + 0.35, y: 2.15, w: w2 - 0.7, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 18 });
    const wk = [
      ["Mon 7:00", "Drafts this week's posts and EDM", "Your team approves"],
      ["Wed 8:00", "Summarises rate and lender news", "Your team reads"],
      ["Fri 3:00", "Drafts follow-ups for new enquiries", "Your team sends"],
    ];
    wk.forEach(([t, d, tag], i) => {
      const y = 2.8 + i * 1.12;
      s.addShape(pres.shapes.LINE, { x: x2 + 0.35, y, w: w2 - 0.7, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
      T(s, t, { x: x2 + 0.35, y: y + 0.18, w: 1.3, h: 0.35, fontFace: LABEL, fontSize: 15, color: C.accent1 });
      T(s, d, { x: x2 + 1.75, y: y + 0.18, w: w2 - 2.1, h: 0.4, fontSize: 14, bold: true });
      T(s, tag, { x: x2 + 1.75, y: y + 0.58, w: w2 - 2.1, h: 0.3, fontSize: 12, color: C.accent4 });
    });
    s.addNotes("Keep this grounded. Routines are powerful, but the governance principle from earlier still applies: AI prepares, a person decides. Start with something low-stakes like a weekly content draft before anything touches a client file.");
  }

  // =================== 4 · HOW TO PROMPT ===================
  pres.addSection({ title: S5 });

  // 18. Visionary vs executor
  {
    const s = light(S5, "Chapter 4 · How to prompt", "Visionary vs executor");
    const cols = [
      ["LuLightbulb", "The visionary", "Has the ideas", ["Sees what's possible and spots the opportunity in a changing market", "Ideas without execution don't move the business"]],
      ["LuZap", "The executor", "Does the work", ["Limited by time when volume is high", "Only so many hours to check documents or write follow-ups by hand"]],
    ];
    const cw = 5.2;
    for (let i = 0; i < cols.length; i++) {
      const [ic, h, sub, items] = cols[i], x = L + i * (cw + 0.35);
      card(s, x, 1.9, cw, 3.3);
      await iconDot(s, ic, x + 0.35, 2.2, 0.6);
      T(s, h, { x: x + 1.15, y: 2.22, w: cw - 1.5, h: 0.42, fontFace: "Newsreader SemiBold", fontSize: 20 });
      T(s, sub, { x: x + 1.15, y: 2.62, w: cw - 1.5, h: 0.3, fontSize: 13, color: C.accent1 });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: j < items.length - 1 } })), { x: x + 0.35, y: 3.2, w: cw - 0.7, h: 1.8, fontSize: 14, color: C.accent4, paraSpaceAfter: 6 });
    }
    T(s, "AI lets you be both at once: the visionary giving direction, with a tireless executor working under it.", { x: L, y: 5.55, w: 10.75, h: 0.8, fontFace: "Newsreader SemiBold", fontSize: 22, color: C.text2 });
    s.addNotes("Most brokers spend most of the day as the executor. The shift today is to spend more of it as the visionary: deciding what good looks like and directing the work, rather than typing all of it.");
  }

  // 19. How to prompt: the five-part brief
  {
    const s = light(S5, "Chapter 4 · How to prompt", "How to prompt: the five-part brief", "corner");
    const parts = [
      ["Context", "Who you are, who it's for and what they already know"],
      ["Task", "One clear job. What you want, in a sentence"],
      ["Example", "Show what good looks like. Paste a past email, note or post"],
      ["Format", "Length, tone and structure. Bullets or prose, formal or warm"],
      ["Review", "Ask it to check its work, or ask you questions first"],
    ];
    const cw = (CW - 4 * 0.25) / 5;
    parts.forEach(([h, d], i) => {
      const x = L + i * (cw + 0.25);
      card(s, x, 1.9, cw, 2.7);
      s.addShape(pres.shapes.OVAL, { x: x + 0.3, y: 2.15, w: 0.55, h: 0.55, fill: { color: C.accent1 }, line: { type: "none" }, objectName: "Step number" });
      T(s, String(i + 1), { x: x + 0.3, y: 2.15, w: 0.55, h: 0.55, fontFace: "Newsreader SemiBold", fontSize: 18, color: C.background1, align: "center", valign: "middle" });
      T(s, h, { x: x + 0.3, y: 2.9, w: cw - 0.5, h: 0.42, fontFace: "Newsreader SemiBold", fontSize: 19 });
      T(s, d, { x: x + 0.3, y: 3.38, w: cw - 0.5, h: 1.1, fontSize: 13, color: C.accent4 });
    });
    card(s, L, 4.9, CW, 1.4, { fill: C.background2, transparency: 0, noShadow: true });
    T(s, "Try it", { x: L + 0.35, y: 5.05, w: 2, h: 0.3, fontFace: LABEL, fontSize: 14, color: C.accent1 });
    T(s, "\u201CI'm a mortgage broker [context]. Write a follow-up email to a first-home buyer I met yesterday [task]. Match the tone of the email below [example]. Under 150 words, warm, no jargon, one clear next step [format]. Ask me anything you need before you start [review].\u201D", { x: L + 0.35, y: 5.35, w: CW - 0.7, h: 0.85, fontSize: 13, italic: true });
    s.addNotes("This is the core skill of the day. Most weak prompts are missing three or four of these five parts. You don't need all five every time, but context and an example make the biggest difference.\n\nThe review step is the one people forget. Asking Claude to ask you questions first nearly always gives a better first draft.");
  }

  // 20. Same task, two briefs
  {
    const s = light(S5, "Chapter 4 · How to prompt", "Same task, two briefs");
    const cw = (CW - 0.4) / 2;
    card(s, L, 1.9, cw, 4.4);
    card(s, L + cw + 0.4, 1.9, cw, 4.4, { lineColor: C.accent1, lineWidth: 1.5 });
    const heads = [["LuX", "Search-engine prompt", HEX.muted], ["LuCheck", "Five-part brief", HEX.blue]];
    for (let i = 0; i < 2; i++) {
      const x = L + i * (cw + 0.4);
      await iconDot(s, heads[i][0], x + 0.35, 2.15, 0.5, { color: heads[i][2] });
      T(s, heads[i][1], { x: x + 1.05, y: 2.2, w: cw - 1.4, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 19 });
    }
    T(s, "\u201CSummarise this bank statement.\u201D", { x: L + 0.35, y: 2.95, w: cw - 0.7, h: 0.5, fontSize: 15, italic: true });
    T(s, [
      { text: "What comes back: ", options: { bold: true, color: C.text1 } },
      { text: "a generic list of transactions. You still have to read the whole statement to find what matters for the file." },
    ], { x: L + 0.35, y: 4.6, w: cw - 0.7, h: 1.4, fontSize: 13, color: C.accent4 });
    const x2 = L + cw + 0.4;
    T(s, "\u201CI'm a broker preparing a home loan application. From this de-identified bank statement, list regular income credits, recurring expenses over $100, any dishonours or overdrawn days, and anything a credit assessor would query. Use a table. Flag anything you're unsure about rather than guessing.\u201D", { x: x2 + 0.35, y: 2.95, w: cw - 0.7, h: 1.6, fontSize: 13, italic: true });
    T(s, [
      { text: "What comes back: ", options: { bold: true, color: C.text1 } },
      { text: "the five things you'd actually look for, in a table you can check against the statement in minutes. You verify; you decide." },
    ], { x: x2 + 0.35, y: 4.6, w: cw - 0.7, h: 1.4, fontSize: 13, color: C.accent4 });
    s.addNotes("Read both out loud. The second one is longer, but it saves far more time than it costs, because the first answer is usable.\n\nPoint out 'de-identified' and 'flag anything you're unsure about'. Those two phrases are governance built into the prompt itself. We'll come back to both in chapter 6.");
  }

  // 21. The follow-up is where the value is
  {
    const s = light(S5, "Chapter 4 · How to prompt", "The first prompt starts it. The follow-ups finish it", "corner");
    const cw = (CW - 0.4) / 2;
    const cols = [
      ["The starting brief", "Visionary", ["\u201CHelp me prepare a presentation on [x]\u201D", "\u201CGive me five ideas for [x]\u201D", "\u201CDraft an email to [x] about [y]\u201D"]],
      ["The follow-up", "Executor, and where the value actually is", ["\u201CNot quite right. Try again, and give me three more directions\u201D", "\u201CMake it shorter\u201D", "\u201CMake it more casual\u201D"]],
    ];
    cols.forEach(([h, sub, items], i) => {
      const x = L + i * (cw + 0.4);
      card(s, x, 1.9, cw, 3.6, i === 1 ? { lineColor: C.accent1, lineWidth: 1.5 } : {});
      T(s, h, { x: x + 0.35, y: 2.15, w: cw - 0.7, h: 0.42, fontFace: "Newsreader SemiBold", fontSize: 20 });
      T(s, sub, { x: x + 0.35, y: 2.57, w: cw - 0.7, h: 0.3, fontSize: 13, color: C.accent1 });
      items.forEach((t, j) => {
        const y = 3.1 + j * 0.72;
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.35, y, w: cw - 0.7, h: 0.58, rectRadius: 0.08, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Prompt chip" });
        T(s, t, { x: x + 0.55, y, w: cw - 1.1, h: 0.58, fontSize: 13, italic: true, valign: "middle" });
      });
    });
    T(s, "Don't stop at the first draft. The second or third pass is usually where it gets good.", { x: L, y: 5.8, w: CW, h: 0.45, fontSize: 16, bold: true, color: C.text2 });
    s.addNotes("The follow-up is the skill most people skip, and it's where the real gain is. Treat the first answer as a draft from a junior: useful, but not finished.");
  }

  // 22. Hands-on: write your own prompts
  {
    const s = light(S5, "Chapter 4 · How to prompt", "Hands-on: write your own prompts", "corner");
    handsOnBadge(s, "Hands-on · 15 minutes");
    numberedList(s, [
      ["Pick one real task from this week", "One that took longer than it should have: a document check, a follow-up email, a social post"],
      ["Write a five-part brief for it", "Context, task, example, format, review. De-identify anything about a real client"],
      ["Push it with a follow-up", "'Shorter', 'more casual' or 'not quite right, try again'. At least one, ideally two"],
      ["Pair up and compare", "What worked, what didn't, and what you'd try differently next time"],
    ], L, 2.45, 7.4, { rowH: 1.0, fontSize: 13 });
    const x2 = 8.6, w2 = R - x2;
    card(s, x2, 2.5, w2, 3.7, { fill: C.background2, transparency: 0 });
    await iconDot(s, "LuTarget", x2 + 0.35, 2.8, 0.55);
    T(s, "What good looks like", { x: x2 + 0.35, y: 3.55, w: w2 - 0.7, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 17 });
    T(s, "A draft you'd be comfortable sending after a quick edit, in under 10 minutes, without retyping it yourself.", { x: x2 + 0.35, y: 4.0, w: w2 - 0.7, h: 1.9, fontSize: 14, color: C.accent4 });
    s.addNotes("Facilitator: circulate and help with the follow-up prompt specifically. That's the skill most people skip.\n\nWatch for anyone pasting real client details. Use it as a teaching moment, not a telling-off: show them how to strip names and account numbers first.");
  }

  // 23. Break
  {
    const s = dark(S5, "Break", "10 minutes.");
    T(s, "Grab a coffee, stretch, check your phone. Back at [time] for memory, skills and choosing the right model.", { x: L, y: 3.2, w: 7.5, h: 1.0, fontSize: 20, color: C.background1 });
    s.addNotes("Set the return time on the slide before the session.");
  }

  // =================== 5 · GO FURTHER ===================
  pres.addSection({ title: S6 });

  // 24. Memory
  {
    const s = light(S6, "Chapter 5 · Go further", "Memory: write it down once, stop repeating yourself", "corner");
    const tiers = [
      ["LuMessageSquare", "Within a conversation", "Claude remembers everything said earlier in the same chat, automatically."],
      ["LuBookOpen", "Project instructions", "Standing context Claude reads every time: who you are, your business, your voice and your rules."],
      ["LuBrain", "Account memory", "Facts and preferences carried between conversations. Viewable and editable in your settings."],
    ];
    const cw = 3.55, gap = 0.6;
    for (let i = 0; i < tiers.length; i++) {
      const [ic, h, d] = tiers[i], x = L + i * (cw + gap);
      card(s, x, 2.0, cw, 3.4);
      await iconDot(s, ic, x + 0.35, 2.3, 0.6);
      T(s, "Lasts: " + ["one chat", "every chat in the project", "across all your chats"][i], { x: x + 0.35, y: 3.1, w: cw - 0.7, h: 0.3, fontFace: LABEL, fontSize: 14, color: C.accent1 });
      T(s, h, { x: x + 0.35, y: 3.45, w: cw - 0.7, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 18 });
      T(s, d, { x: x + 0.35, y: 3.95, w: cw - 0.7, h: 1.3, fontSize: 13, color: C.accent4 });
      if (i < 2) s.addImage({ data: await icon("LuArrowRight", HEX.pale), x: x + cw + 0.15, y: 3.5, w: 0.3, h: 0.3, objectName: "Arrow" });
    }
    T(s, "The more you write down once, the less you repeat yourself. That's the real leverage.", { x: L, y: 5.8, w: CW, h: 0.45, fontSize: 16, bold: true, color: C.text2 });
    s.addNotes("The middle tier is the one to push. A good set of Project instructions (the firm's voice, the services, the rules) is what turns Claude from a generic assistant into one that writes like your practice.");
  }

  // 25. Skills
  {
    const s = light(S6, "Chapter 5 · Go further", "Skills: Claude's playbooks for your recurring work");
    const q = [
      ["LuBookOpen", "What they are", "A packaged set of instructions for one recurring task. Teach Claude how you want it done once, and it's done that way every time after."],
      ["LuRepeat", "Why they matter", "They turn a one-off good result into a repeatable process. The difference between explaining yourself every time and something that just works."],
      ["LuLayers", "Two kinds", "Official skills from Anthropic load automatically when relevant. Custom skills are built for your workflow: document checks, a report format, your brand voice."],
      ["LuWand2", "Making your own", "Describe the task, show Claude an example of good output and ask it to build the skill. Works the same in chat, Claude Code and the API."],
    ];
    const cw = (CW - 0.3) / 2, ch = 2.0;
    for (let i = 0; i < q.length; i++) {
      const [ic, h, d] = q[i], x = L + (i % 2) * (cw + 0.3), y = 1.9 + Math.floor(i / 2) * (ch + 0.3);
      card(s, x, y, cw, ch);
      await iconDot(s, ic, x + 0.35, y + 0.3);
      T(s, h, { x: x + 1.05, y: y + 0.37, w: cw - 1.4, h: 0.42, fontFace: "Newsreader SemiBold", fontSize: 18 });
      T(s, d, { x: x + 1.05, y: y + 0.85, w: cw - 1.4, h: 1.05, fontSize: 13, color: C.accent4 });
    }
    s.addNotes("Rule of thumb: if you do something the same way more than twice, it's a candidate for a skill. The live demo builds one together.");
  }

  // 26. Prompting vs planning
  {
    const s = light(S6, "Chapter 5 · Go further", "Prompt or plan? Match the effort to the stakes", "corner");
    const cw = (CW - 0.4) / 2;
    const cols = [
      ["LuZap", "Just prompt", "When you just need the answer", ["Fast, straightforward requests", "A good-enough first draft is fine", "Getting it wrong costs seconds"]],
      ["LuListChecks", "Plan first", "When the work is heavier", ["Use Plan Mode: Claude researches and proposes an approach before doing anything", "Ask Claude to write the prompt for you, or to ask you clarifying questions first", "Tell it to act as a specific expert, such as \u201Ca compliance-focused editor\u201D"]],
    ];
    for (let i = 0; i < cols.length; i++) {
      const [ic, h, sub, items] = cols[i], x = L + i * (cw + 0.4);
      card(s, x, 1.9, cw, 3.65);
      await iconDot(s, ic, x + 0.35, 2.2, 0.6);
      T(s, h, { x: x + 1.15, y: 2.22, w: cw - 1.5, h: 0.42, fontFace: "Newsreader SemiBold", fontSize: 20 });
      T(s, sub, { x: x + 1.15, y: 2.62, w: cw - 1.5, h: 0.3, fontSize: 13, color: C.accent1 });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: j < items.length - 1 } })), { x: x + 0.35, y: 3.2, w: cw - 0.7, h: 2.2, fontSize: 14, color: C.accent4, paraSpaceAfter: 6 });
    }
    T(s, "If getting it wrong costs real time to fix, plan first. If it costs ten seconds, just prompt.", { x: L, y: 5.85, w: CW, h: 0.45, fontSize: 16, bold: true, color: C.text2 });
    s.addNotes("A policy document, a client-facing template or anything touching compliance: plan first. A caption or a quick summary: just prompt.");
  }

  // 27. Which model
  {
    const s = light(S6, "Chapter 5 · Go further", "Which model to use, and when");
    const models = [
      ["Haiku", "Fastest and lightest", "Quick, simple tasks where speed matters more than depth.", 1],
      ["Sonnet", "The everyday default", "A strong balance of speed and quality for most day-to-day work.", 2],
      ["Opus", "Higher-stakes work", "Real analysis, complex documents, anything worth double-checking.", 3],
      ["Fable", "The most capable", "Long, complex tasks where quality matters more than speed.", 4],
    ];
    const cw = (CW - 3 * 0.3) / 4;
    models.forEach(([h, sub, d, lvl], i) => {
      const x = L + i * (cw + 0.3);
      card(s, x, 1.9, cw, 3.6, i === 1 ? { lineColor: C.accent1, lineWidth: 1.5 } : {});
      T(s, h, { x: x + 0.3, y: 2.15, w: cw - 0.6, h: 0.55, fontFace: "Newsreader SemiBold", fontSize: 26 });
      T(s, sub, { x: x + 0.3, y: 2.75, w: cw - 0.6, h: 0.35, fontSize: 13, bold: true, color: C.accent1 });
      T(s, d, { x: x + 0.3, y: 3.2, w: cw - 0.6, h: 1.2, fontSize: 13, color: C.accent4 });
      T(s, "Depth", { x: x + 0.3, y: 4.62, w: 0.8, h: 0.3, fontSize: 11, color: C.accent4 });
      for (let k = 0; k < 4; k++) s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 1.05 + k * 0.38, y: 4.68, w: 0.3, h: 0.16, rectRadius: 0.08, fill: { color: k < lvl ? C.accent1 : C.accent5 }, line: { type: "none" }, objectName: "Depth meter" });
    });
    T(s, "Start on the default. Step up only when the task is genuinely hard or a wrong answer is expensive.", { x: L, y: 5.85, w: CW, h: 0.45, fontSize: 16, bold: true, color: C.text2 });
    s.addNotes("Don't pay for more power than the task needs. Most broker admin and drafting runs well on Sonnet. Save Opus and Fable for complex document analysis, policy drafting and anything high-stakes.");
  }

  // 28. Live demo
  {
    const s = light(S6, "Chapter 5 · Go further", "Live demo: what good looks like", "corner");
    numberedList(s, [
      ["Tour a well-built Project", "Instructions, files and a few saved chats, so people see the target"],
      ["Set up a new Project, live", "Use the practice's own services and tone"],
      ["Build a simple custom skill together", "A social caption skill in the firm's voice"],
      ["Claude Code, briefly", "How it works inside your files, and how a recurring task becomes an agent"],
      ["Claude Design", "A landing page or social post built live from a prepared prompt, on brand"],
    ], L, 1.95, 7.6, { rowH: 0.84 });
    const x2 = 8.85, w2 = R - x2;
    card(s, x2, 1.95, w2, 4.2, { fill: C.background2, transparency: 0 });
    await iconDot(s, "LuMousePointerClick", x2 + 0.35, 2.25, 0.55);
    T(s, "20 minutes", { x: x2 + 0.35, y: 3.0, w: w2 - 0.7, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 20 });
    T(s, "Two or three things shown well beat rushing through all five. Save a full Claude Code walkthrough for a follow-on session.", { x: x2 + 0.35, y: 3.5, w: w2 - 0.7, h: 2.4, fontSize: 14, color: C.accent4 });
    s.addNotes("Have every demo prepared and tested before the session, with de-identified sample data only. Pick the order based on what the room reacted to in the pain-points slide.");
  }

  // 29. Top tips
  {
    const s = light(S6, "Chapter 5 · Go further", "Ten habits of the people who get the most from it", "corner");
    const tips = [
      "Ask Claude to ask you questions first",
      "Keep a written file for anything you repeat: voice, rules, context",
      "Tell it to act as a specific expert",
      "Build a skill for anything you do the same way more than twice",
      "Not sure how to ask? Ask Claude how to ask",
      "Use the tools together: draft in chat, build in Docs, polish in Design",
      "Talk instead of typing. Voice input works the same way",
      "Show it a real example of good, not just a description",
      "Don't accept the first draft",
      "Be specific when it's wrong: \u2018too long\u2019, \u2018too generic\u2019, \u2018wrong tone\u2019",
    ];
    const cw = (CW - 0.5) / 2, rh = 0.8;
    tips.forEach((t, i) => {
      const col = Math.floor(i / 5), row = i % 5, x = L + col * (cw + 0.5), y = 1.9 + row * rh;
      s.addShape(pres.shapes.LINE, { x, y, w: cw, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
      T(s, String(i + 1), { x, y: y + 0.18, w: 0.5, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 20, color: C.accent1 });
      T(s, t, { x: x + 0.6, y: y + 0.2, w: cw - 0.6, h: 0.5, fontSize: 14 });
    });
    s.addShape(pres.shapes.LINE, { x: L, y: 1.9 + 5 * rh, w: cw, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
    s.addShape(pres.shapes.LINE, { x: L + cw + 0.5, y: 1.9 + 5 * rh, w: cw, h: 0, line: { color: C.accent5, width: 0.75 }, objectName: "Row rule" });
    s.addNotes("Ask each person to circle the two habits they'll try this week. Vague feedback gets vague fixes; specific feedback gets specific fixes.");
  }

  // =================== 6 · LOCK IN THE LEAD ===================
  pres.addSection({ title: S7 });

  // 30. What changes
  {
    const s = light(S7, "Chapter 6 · Lock in the lead", "What changes when it sticks", "corner");
    const rows = [
      ["LuFileSearch", "Document checking", "Manual, line by line, on every file", "AI extracts and flags. You verify and sign off"],
      ["LuMegaphone", "Marketing", "Squeezed in after hours, when there's time", "Out every week in your voice, drafted in minutes"],
      ["LuMail", "Client questions", "Answers dug out of folders and inboxes", "Same-day replies, while the conversation is fresh"],
      ["LuTrendingUp", "Growth", "The next stage starts with another hire", "More clients with the same team"],
    ];
    T(s, "Before", { x: 4.3, y: 1.85, w: 3.5, h: 0.3, fontFace: LABEL, fontSize: 15, color: C.accent4 });
    T(s, "After", { x: 8.4, y: 1.85, w: 3.5, h: 0.3, fontFace: LABEL, fontSize: 15, color: C.accent1 });
    for (let i = 0; i < rows.length; i++) {
      const [ic, h, b, a] = rows[i], y = 2.3 + i * 1.0;
      card(s, L, y, CW, 0.82, { noShadow: true });
      await iconDot(s, ic, L + 0.2, y + 0.16, 0.5);
      T(s, h, { x: L + 0.9, y, w: 2.6, h: 0.82, fontFace: "Newsreader SemiBold", fontSize: 17, valign: "middle" });
      T(s, b, { x: 4.3, y, w: 3.7, h: 0.82, fontSize: 14, color: C.accent4, valign: "middle" });
      s.addImage({ data: await icon("LuArrowRight", HEX.pale), x: 7.95, y: y + 0.28, w: 0.26, h: 0.26, objectName: "Arrow" });
      T(s, a, { x: 8.4, y, w: 3.95, h: 0.82, fontSize: 14, bold: true, valign: "middle" });
    }
    T(s, "Your role moves from mostly executor to visionary first, with AI as the executor.", { x: L, y: 6.35, w: CW, h: 0.4, fontSize: 15, bold: true, color: C.text2 });
    s.addNotes("This is the right-hand brokerage from the ultimatum slide, made concrete. None of it requires new software or technical skills, just the habits from today and a clear policy.");
  }

  // 31. Settings
  {
    const s = light(S7, "Chapter 6 · Lock in the lead", "Settings worth checking before you start");
    const items = [
      ["LuShieldCheck", "Data and privacy", "Confirm you're on a business plan (Team or Enterprise), not a personal plan, before any client data goes near it."],
      ["LuBrain", "Memory", "Review what's being remembered about you and your practice. Correct or clear anything wrong."],
      ["LuPlug", "Connected apps", "Only connect the tools you actually use. Each connection is something Claude can act on."],
      ["LuBell", "Notifications", "Set them to match how you want to be interrupted, especially for longer tasks."],
      ["LuGauge", "Default model", "Pick a sensible default so you're not switching every time."],
      ["LuUserCog", "For admins", "Organisation settings hold the org-wide data and privacy controls, including use of feedback."],
    ];
    const cw = (CW - 2 * 0.3) / 3, ch = 1.95;
    for (let i = 0; i < items.length; i++) {
      const [ic, h, d] = items[i], x = L + (i % 3) * (cw + 0.3), y = 1.9 + Math.floor(i / 3) * (ch + 0.3);
      card(s, x, y, cw, ch);
      await iconDot(s, ic, x + 0.3, y + 0.3);
      T(s, h, { x: x + 1.0, y: y + 0.38, w: cw - 1.2, h: 0.4, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x + 0.3, y: y + 0.98, w: cw - 0.6, h: 0.9, fontSize: 13, color: C.accent4 });
    }
    s.addNotes("If people have laptops open, have them check the first two now. Five minutes here prevents most of the problems we see later.");
  }

  // 32. Client data
  {
    const s = light(S7, "Chapter 6 · Lock in the lead", "Client data: what's actually safe to upload", "corner");
    const tiers = [
      ["LuX", "Never", "Personal or free accounts", "Conversations can be used to improve models by default. Treat it like any consumer app: never a place for client documents.", HEX.orange],
      ["LuShieldCheck", "Minimum bar", "Business plans (Team, Enterprise)", "Commercial terms apply. By default your inputs and outputs aren't used to train models.", HEX.blue],
      ["LuEyeOff", "Good practice", "De-identify first", "Strip names, account numbers and other identifiers before uploading, even on a business plan.", HEX.blue],
      ["LuLock", "Higher sensitivity", "Enterprise options", "Zero data retention and formal data agreements exist on Enterprise. Ask Anthropic; don't assume they're included.", HEX.deep],
    ];
    const cw = (CW - 3 * 0.3) / 4;
    for (let i = 0; i < tiers.length; i++) {
      const [ic, lab, h, d, col] = tiers[i], x = L + i * (cw + 0.3);
      card(s, x, 1.9, cw, 3.85, i === 0 ? { lineColor: C.accent3, lineWidth: 1.25 } : {});
      await iconDot(s, ic, x + 0.3, 2.2, 0.55, { color: col, bg: i === 0 ? "FFEDE3" : HEX.tint });
      T(s, lab, { x: x + 0.3, y: 2.95, w: cw - 0.6, h: 0.3, fontFace: LABEL, fontSize: 14, color: i === 0 ? C.accent3 : C.accent1 });
      T(s, h, { x: x + 0.3, y: 3.28, w: cw - 0.6, h: 0.75, fontFace: "Newsreader SemiBold", fontSize: 17 });
      T(s, d, { x: x + 0.3, y: 4.05, w: cw - 0.6, h: 1.6, fontSize: 13, color: C.accent4 });
    }
    T(s, "This is exactly what your AI use policy covers: which documents, which tools, and what needs a person's sign-off before it goes near a client file.", { x: L, y: 6.0, w: CW, h: 0.55, fontSize: 14, bold: true, color: C.text2 });
    s.addNotes("Before you deliver this slide: verify current plan-tier data terms directly with Anthropic close to the session date. Privacy and data policy is the one area that can change between sessions.\n\nThis slide sets up the final exercise. Everything on it becomes a line in their policy.");
  }

  // 33. Hands-on: draft your AI use policy
  {
    const s = light(S7, "Chapter 6 · Lock in the lead", "Hands-on: draft your AI use policy");
    handsOnBadge(s, "Hands-on · 20 minutes");
    T(s, "As a group, fill in each cell for your practice. Best Interest Duty and responsible lending stay with a person, always.", { x: 3.6, y: 1.82, w: 9.0, h: 0.42, fontSize: 14, color: C.accent4, valign: "middle" });
    const hd = (t, col) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color: col }, fontSize: 14, valign: "middle", align: "left" } });
    const lab = (t) => ({ text: t, options: { bold: true, fill: { color: HEX.soft }, fontSize: 14, valign: "middle" } });
    const e = (t) => ({ text: t, options: { fontSize: 12, color: HEX.muted, italic: true, valign: "top" } });
    const rows = [
      [hd("", HEX.blue), hd("Allowed", HEX.blue), hd("Needs a person's sign-off", HEX.deep), hd("Off-limits", HEX.orange)],
      [lab("Document checking"), e("e.g. listing what's missing from a de-identified file"), e(""), e("")],
      [lab("Marketing"), e(""), e("e.g. every post before it's published"), e("")],
      [lab("Admin and follow-ups"), e(""), e(""), e("e.g. sending anything to a client automatically")],
      [lab("Tools and data"), e("e.g. our Claude Team plan only"), e(""), e("")],
    ];
    s.addTable(rows, { x: L, y: 2.5, w: CW, colW: [2.5, 3.11, 3.11, 3.11], rowH: [0.45, 0.8, 0.8, 0.8, 0.8], border: { type: "solid", color: HEX.line, pt: 0.75 }, fill: { color: HEX.white }, margin: [0.08, 0.12, 0.08, 0.12], objectName: "Policy canvas" });
    T(s, "This is the real takeaway. We'll turn today's draft into the finished written policy your practice keeps.", { x: L, y: 6.4, w: CW, h: 0.35, fontSize: 13, bold: true, color: C.text2 });
    s.addNotes("Start from what came up earlier: where is AI already being used, unsupervised, in this practice? Work through each row and agree what's allowed, what needs sign-off and what's off-limits.\n\nThis is what clients are paying for. If you're short on time, trim the earlier lecture sections. Don't cut this short.\n\nTip: capture the group's answers live in Claude Docs, so the draft already exists when the session ends.");
  }

  // 34. Close: you've left the pack
  {
    const s = dark(S7, "Where you stand now", "You've just left the pack.");
    T(s, [
      { text: "Only 3% of brokers have a formal policy for safe AI use. ", options: { bold: true, breakLine: true } },
      { text: "Once today's draft is finalised this week, your practice is one of them, with a team that knows how to use the tools behind it." },
    ], { x: L, y: 3.35, w: 8.4, h: 1.6, fontSize: 20, color: C.background1 });
    s.addNotes("Call back to the 3% from chapter 1. The team came in as part of the pack and leaves ahead of it. Then move to next steps.");
  }

  // 35. Questions and what's next
  {
    const s = light(S7, "Next steps", "Questions, and what happens next", "corner");
    const steps = [
      ["Today", "Your AI use policy, drafted together in this session"],
      ["Within a week", "The finished, written policy your practice keeps"],
      ["Two weeks", "Track hours on your three most repetitive tasks, so there's a baseline"],
      ["30, 60, 90 days", "Check-ins to confirm it's sticking, and hours saved against the baseline"],
    ];
    const cw = (CW - 3 * 0.3) / 4;
    steps.forEach(([h, d], i) => {
      const x = L + i * (cw + 0.3);
      s.addShape(pres.shapes.OVAL, { x, y: 2.0, w: 0.26, h: 0.26, fill: { color: C.accent1 }, line: { type: "none" }, objectName: "Timeline dot" });
      if (i < steps.length - 1) s.addShape(pres.shapes.LINE, { x: x + 0.34, y: 2.13, w: cw + 0.3 - 0.42, h: 0, line: { color: C.accent6, width: 1.5 }, objectName: "Timeline line" });
      T(s, h, { x, y: 2.45, w: cw - 0.1, h: 0.45, fontFace: "Newsreader SemiBold", fontSize: 19, color: C.accent1 });
      T(s, d, { x, y: 2.95, w: cw - 0.2, h: 1.1, fontSize: 14 });
    });
    card(s, L, 4.45, 7.2, 1.7, { fill: C.background2, transparency: 0, noShadow: true });
    T(s, "Open floor", { x: L + 0.35, y: 4.65, w: 6, h: 0.3, fontFace: LABEL, fontSize: 14, color: C.accent1 });
    T(s, "What's the one task you'd want AI doing for you by next week?", { x: L + 0.35, y: 5.0, w: 6.5, h: 0.9, fontFace: "Newsreader SemiBold", fontSize: 20 });
    T(s, [
      { text: "Sam Cheng", options: { bold: true, breakLine: true } },
      { text: "sam@locatedigital.io", options: { breakLine: true } },
      { text: "locatedigital.io" },
    ], { x: 8.45, y: 4.75, w: 4.1, h: 1.2, fontSize: 15 });
    s.addNotes("Close on the open-floor question and write the answers down. They're the first items for the 30-day check-in.\n\nThe two-week baseline is what lets us show a real number at 90 days rather than a feeling.");
  }

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
}

build().catch((e) => { console.error(e); process.exit(1); });
