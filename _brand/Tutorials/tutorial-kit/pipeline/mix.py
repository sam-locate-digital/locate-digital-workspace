"""Mix the tutorial's sound: cleaned voice, music bed, soft sound effects on graphics, loudness to target.

Usage: python -I mix.py <work_dir> [--lufs -14]
Inputs: base.wav (voice), remotion/src/timeline.json. Makes music.wav with music.py if it's missing or too short.
Output: mix.wav (48 kHz stereo), plus voice_clean.wav, music_env.wav and sfx.wav for checking.

Music modes (plan.json "music"):
  bookends  (default) the bed plays under the opening up to the lesson title, swells briefly under each chapter
            card, and comes back for the last section and the end card. Screen demos stay clean.
  under     a quiet bed the whole way through, ducked under the voice
  off       no music
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

WORK = Path(sys.argv[1])
LUFS = float(sys.argv[sys.argv.index("--lufs") + 1]) if "--lufs" in sys.argv else -14.0
SR = 48000
tl = json.loads((WORK / "remotion" / "src" / "timeline.json").read_text(encoding="utf-8"))
LENGTH, TOTAL = tl["length"], tl["total"]
N = int(round(LENGTH * SR))
rng = np.random.default_rng(3)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)
    return r.stderr


def write(path, x):
    x = np.atleast_2d(x)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(x.shape[0]); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x.T, -1, 1) * 32767).astype("<i2").tobytes())


def read(path):
    with wave.open(str(path), "rb") as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768
        return x.reshape(-1, w.getnchannels()).T


# ---- music bed with its envelope ----
music_path = WORK / "music.wav"
if not music_path.exists() or read(music_path).shape[1] < N:
    run([sys.executable, "-I", str(Path(__file__).with_name("music.py")), f"{LENGTH + 1:.2f}", str(music_path)])
music = read(music_path)[:, :N]
env = np.zeros(N)
mode = tl.get("music", "bookends")


def trap(a, b, fade_in, fade_out, level):
    """Add a trapezoid to the envelope: up over fade_in from a, level until b, down over fade_out after b."""
    t = np.arange(N) / SR
    up = np.clip((t - a) / max(fade_in, 1e-3), 0, 1) if a > 0 else np.ones(N)
    down = np.clip(1 - (t - b) / max(fade_out, 1e-3), 0, 1)
    np.maximum(env, level * np.minimum(up, down), out=env)


if mode == "under":
    env[:] = 0.5
elif mode == "bookends":
    open_end = tl["intro"]["e"] if tl.get("intro") else (tl["chapters"][0]["s"] if tl["chapters"] else min(20, TOTAL))
    trap(0, open_end + 1.0, 0, 3.0, 1.0)
    last = tl["sections"][-1]["s"] if len(tl["sections"]) > 1 else max(0, TOTAL - 20)
    trap(last, LENGTH + 5, 3.0, 1.0, 1.0)
    for c in tl["chapters"]:
        trap(c["s"] - 0.3, c["e"] - 0.4, 0.5, 1.6, 0.7)
write(WORK / "music_env.wav", music * env)

# ---- sound effects on graphic landings ----


def lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR); y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y


def whoosh(length=0.5):
    n = int(SR * length); t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    e = np.sin(np.pi * np.clip(t / length, 0, 1)) ** 2
    return (lp(noise, 600) * (1 - t / length) + lp(noise, 2600) * (t / length) * 0.6) * e * 2.2


def tick():
    t = np.arange(int(SR * 0.06)) / SR
    return np.sin(2 * np.pi * 2300 * t) * np.exp(-t / 0.015) * 0.6


W, K = whoosh(), tick()
events = [(c["s"] - 0.15, W, 0.10) for c in tl["chapters"]] + [(c["s"] - 0.15, W, 0.08) for c in tl["cards"]]
events += [(s["s"] - 0.1, W, 0.06) for s in tl["splits"]] + [(l["s"] + 0.1, K, 0.07) for l in tl["labels"]]
if tl.get("intro"):
    events.append((tl["intro"]["s"] - 0.15, W, 0.10))
if tl.get("end"):
    events.append((tl["end"]["s"] - 0.15, W, 0.10))
sfx = np.zeros(N)
for at, sig, g in events:
    i = max(0, int(at * SR)); j = min(N, i + len(sig)); sfx[i:j] += sig[:j - i] * g
write(WORK / "sfx.wav", np.stack([sfx, sfx]))


# ---- voice chain, ducking, mix, two-pass loudness ----
def lufs(path, extra=None):
    out = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", (extra + "," if extra else "") + "ebur128=peak=true",
               "-f", "null", "-"])
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])


VOICE = ("highpass=f=80,afftdn=nr=10:nf=-42,equalizer=f=4000:t=q:w=1.2:g=2.5,"
         "acompressor=threshold=-18dB:ratio=3:attack=5:release=90:makeup=2")
v_l = lufs(WORK / "base.wav", VOICE)
gain = 0.0
if mode != "off" and env.max() > 0:
    m_l = lufs(WORK / "music.wav")
    gain = (v_l - (18 if mode == "bookends" else 24)) - m_l
graph = (f"[0:a]{VOICE},aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={LENGTH}[vc];"
         f"[vc]asplit=2[v][vsc];[1:a]volume={gain:.2f}dB[m];"
         f"[m][vsc]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=350:makeup=1[md];"
         f"[2:a]aformat=channel_layouts=stereo[s];"
         f"[v][md][s]amix=inputs=3:normalize=0:duration=longest,atrim=0:{LENGTH}[mix]")
pre = WORK / "mix_pre.wav"
run(["ffmpeg", "-hide_banner", "-y", "-i", str(WORK / "base.wav"), "-i", str(WORK / "music_env.wav"), "-i", str(WORK / "sfx.wav"),
     "-filter_complex", graph, "-map", "[mix]", "-ar", "48000", "-c:a", "pcm_s24le", str(pre)])
m = run(["ffmpeg", "-hide_banner", "-i", str(pre), "-af", f"loudnorm=I={LUFS}:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
js = json.loads(m[m.rindex("{"): m.rindex("}") + 1])
ln = (f"loudnorm=I={LUFS}:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
      f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
run(["ffmpeg", "-hide_banner", "-y", "-i", str(pre), "-af", ln + ",aresample=48000", "-c:a", "pcm_s16le", str(WORK / "mix.wav")])
summary = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(WORK / "mix.wav"), "-af", "ebur128=peak=true", "-f", "null", "-"])
i_l = re.findall(r"I:\s+(-?[\d.]+) LUFS", summary)[-1]
tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", summary)[-1]
print(f"mix.wav {LENGTH:.2f}s | music {mode} ({gain:+.1f} dB) | {len(events)} sound effects | {i_l} LUFS, true peak {tp} dBTP")
