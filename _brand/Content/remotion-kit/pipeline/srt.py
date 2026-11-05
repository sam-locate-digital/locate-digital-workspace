"""Write captions.srt and timings.txt for the CapCut pack from the reel's caption data.

Usage: python -I srt.py <data.json> <out_dir>
"""
import json
import sys
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
OUT = Path(sys.argv[2])


def ts(s):
    ms = round(s * 1000)
    h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"


def mmss(s):
    return f"{int(s // 60)}:{s % 60:05.2f}"


lines, n = [], 0
for c in data["cues"]:
    if c.get("logo"):
        continue  # brand names show as logo overlays instead of captions
    n += 1
    text = f"{c['setup']} {c['em']}" if c.get("em") else c["text"]
    end = min(c["e"], data["endCard"])
    lines.append(f"{n}\n{ts(c['s'])} --> {ts(end)}\n{text}\n")
(OUT / "captions.srt").write_text("\n".join(lines), encoding="utf-8")

logos = [c for c in data["cues"] if c.get("logo")]
shots = [("automation-1.png", 4.76, 7.95, "$34,298.65 result, while you describe the 3-month automation"),
         ("automation-2.png", 7.95, 9.48, "$171,434.33 result, the 6-month automation"),
         ("automation-3.png", 9.48, 11.21, "$71,249.38 result, the 12-month automation")]
t = [
    "CapCut pack: $200,000 automation reel (v3)",
    f"Length {data['total']:.2f} s, 1080 x 1920, 30 fps. Times are m:ss.ss from the start.",
    "",
    "MAIN TRACK",
    f"  footage.mp4         0:00.00 - {mmss(data['total'])}   cut footage with the zooms, no captions or overlays",
    "                      (its own audio is the raw voice, for lining things up or CapCut Auto captions; mute it in the final)",
    "",
    "OVERLAYS (each PNG is a full 1080 x 1920 transparent frame, already in position: drop it on, don't move it)",
]
for f, a, b, note in shots:
    t.append(f"  {f:<20}{mmss(a)} - {mmss(b)}   {note}")
for c in logos:
    name = "logo-highlevel.png" if c["logo"] == "highlevel" else "logo-claude.png"
    t.append(f"  {name:<20}{mmss(c['s'])} - {mmss(c['s'] + 1.1)}   when you say \"{c['text']}\"")
t += [
    "",
    "AUDIO (all start at 0:00.00; together they make the finished -14 LUFS mix)",
    "  voice.wav           your voice, cleaned (80 Hz high-pass, noise reduction, presence, compression)",
    "  music.wav           original music bed, already ducked under your voice",
    "  sfx.wav             soft clicks as each screenshot and logo lands",
    "",
    "CAPTIONS",
    "  captions.srt        every caption with its timing. Text > Local captions > Import.",
    "                      Style: white fill, black stroke about 6-8, bold font (TikTok Sans if CapCut lists it).",
    "                      GoHighLevel and Claude have no caption on purpose: their logos show instead.",
    "",
    "EXPORT FROM CAPCUT",
    "  1080p, 30 fps. Keep text out of the top 220 px, bottom 420 px and right 120 px.",
]
(OUT / "timings.txt").write_text("\n".join(t) + "\n", encoding="utf-8")
print(f"{n} captions, {len(shots)} screenshots, {len(logos)} logos")
