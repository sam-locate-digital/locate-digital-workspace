"""Build the reel's audio: SFX track, music bed level, voice chain, ducking, two-pass loudness to -14 LUFS.

Usage: python -I audio.py <work_dir>
Inputs: aroll.mov (voice), music.wav (from music.py), remotion/src/data.json (length)
Output: mix.wav (48 kHz stereo, -14 LUFS integrated, true peak <= -1.5 dBTP)
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

WORK = Path(sys.argv[1])
SR = 48000
total = json.loads((WORK / "remotion" / "src" / "data.json").read_text(encoding="utf-8"))["total"]
rng = np.random.default_rng(3)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)
    return r.stderr


def lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR); y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y


def click():
    t = np.arange(int(SR * 0.05)) / SR
    tone = np.sin(2 * np.pi * 1650 * t) * np.exp(-t / 0.012)
    noise = rng.standard_normal(len(t)); noise = (noise - lp(noise, 3000)) * np.exp(-t / 0.004)
    return 0.55 * tone + 0.25 * noise


def tick():
    t = np.arange(int(SR * 0.06)) / SR
    return np.sin(2 * np.pi * 2300 * t) * np.exp(-t / 0.015) * 0.6


def whoosh(length=0.5):
    n = int(SR * length); t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    env = np.sin(np.pi * np.clip(t / length, 0, 1)) ** 2
    # sweep: blend a dark and a brighter filtered copy across the envelope
    dark, bright = lp(noise, 600), lp(noise, 2600)
    mix = dark * (1 - t / length) + bright * (t / length) * 0.6
    return mix * env * 2.2


# At most about one every 4 s; each sits on a graphic landing, never on a caption word
EVENTS = [(4.62, "whoosh"), (7.95, "click"), (9.48, "click"), (11.13, "whoosh"), (13.25, "tick"),
          (17.36, "click"), (25.07, "click"), (26.47, "click"), (30.30, "click"), (35.15, "click")]
GAIN = {"click": 0.16, "tick": 0.14, "whoosh": 0.10}
SHAPE = {"click": click, "tick": tick, "whoosh": whoosh}

n = int(SR * total)
sfx = np.zeros(n)
for at, kind in EVENTS:
    s = SHAPE[kind]() * GAIN[kind]
    i = int(at * SR)
    j = min(n, i + len(s)); sfx[i:j] += s[: j - i]
st = np.stack([sfx, sfx]).T
with wave.open(str(WORK / "sfx.wav"), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(st, -1, 1) * 32767).astype("<i2").tobytes())


def lufs(path, extra=None):
    af = (extra + "," if extra else "") + "ebur128=peak=true"
    out = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", af, "-f", "null", "-"])
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])


VOICE = ("highpass=f=80,afftdn=nr=10:nf=-42,equalizer=f=4000:t=q:w=1.2:g=2.5,"
         "acompressor=threshold=-18dB:ratio=3:attack=5:release=90:makeup=2")
v_l = lufs(WORK / "aroll.mov", VOICE)
m_l = lufs(WORK / "music.wav")
music_gain = (v_l - 20) - m_l  # bed sits 20 dB under the voice before ducking
print(f"voice {v_l:.1f} LUFS, music {m_l:.1f} LUFS -> music gain {music_gain:+.1f} dB")

graph = (
    f"[0:a]{VOICE},aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={total}[vc];"
    f"[vc]asplit=2[v][vsc];"
    f"[1:a]volume={music_gain:.2f}dB,atrim=0:{total}[m];"
    f"[m][vsc]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=350:makeup=1[md];"
    f"[2:a]aformat=channel_layouts=stereo[s];"
    f"[v][md][s]amix=inputs=3:normalize=0:duration=first,atrim=0:{total}[mix]"
)
pre = WORK / "mix_pre.wav"
run(["ffmpeg", "-hide_banner", "-y", "-i", str(WORK / "aroll.mov"), "-i", str(WORK / "music.wav"), "-i", str(WORK / "sfx.wav"),
     "-filter_complex", graph, "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s24le", str(pre)])

# Two-pass loudness normalisation to -14 LUFS, true peak -1.5 dBTP (headroom for AAC)
m = run(["ffmpeg", "-hide_banner", "-i", str(pre), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
js = json.loads(m[m.rindex("{"): m.rindex("}") + 1])
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
      f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
run(["ffmpeg", "-hide_banner", "-y", "-i", str(pre), "-af", ln + ",aresample=48000", "-c:a", "pcm_s16le", str(WORK / "mix.wav")])
print("final:", run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(WORK / "mix.wav"), "-af", "ebur128=peak=true", "-f", "null", "-"])
      .split("Summary:")[-1].replace("\n", " ").strip())
