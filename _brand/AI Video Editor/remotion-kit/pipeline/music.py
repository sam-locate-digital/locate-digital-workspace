"""Generate an original, royalty-free instrumental bed: warm keys, soft pad, sub bass, light percussion.

Usage: python -I music.py <seconds> <out.wav> [bpm]
Everything is synthesised here, so Locate owns the result outright.
"""
import sys
import wave

import numpy as np

SR = 48000
DUR = float(sys.argv[1])
OUT = sys.argv[2]
BPM = float(sys.argv[3]) if len(sys.argv) > 3 else 92.0
BEAT = 60.0 / BPM
BAR = BEAT * 4
rng = np.random.default_rng(7)

n = int(SR * (DUR + 2))
L = np.zeros(n)
R = np.zeros(n)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def onepole_lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def add(buf, start, sig, gain=1.0):
    i = int(start * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def key_note(f, length, vel):
    """Soft electric-piano-ish tone: sine + gentle harmonics, fast attack, long decay, slight tremolo."""
    t = np.arange(int(SR * length)) / SR
    env = (1 - np.exp(-t / 0.006)) * np.exp(-t / 1.4)
    trem = 1 + 0.06 * np.sin(2 * np.pi * 4.5 * t)
    sig = (np.sin(2 * np.pi * f * t) + 0.32 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.4)
           + 0.08 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t / 0.2))
    return sig * env * trem * vel


def pad_chord(freqs, length):
    t = np.arange(int(SR * length)) / SR
    env = np.minimum(1, t / 0.9) * np.minimum(1, np.maximum(0, (length - t) / 0.9))
    sig = np.zeros_like(t)
    for f in freqs:
        for det in (-0.12, 0.0, 0.12):
            ff = f * 2 ** (det / 12)
            sig += np.sin(2 * np.pi * ff * t + rng.uniform(0, 6.28)) + 0.25 * np.sin(2 * np.pi * 2 * ff * t)
    return sig * env / (len(freqs) * 3)


def kick():
    t = np.arange(int(SR * 0.35)) / SR
    f = 48 + 70 * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t / 0.12)


def shaker():
    t = np.arange(int(SR * 0.08)) / SR
    x = rng.standard_normal(len(t))
    x = x - onepole_lp(x, 5000)  # crude high-pass
    return x * np.exp(-t / 0.025)


# Fmaj7 - Am7 - Cmaj7 - G6 (voiced around middle C)
prog = [
    (41, [53, 57, 60, 64]),
    (45, [57, 60, 64, 67]),
    (48, [55, 60, 64, 71]),
    (43, [55, 59, 62, 64]),
]
# Small keys motif per bar (beat offset, scale degree in the chord voicing index)
motif = [(0.0, 3, 0.55), (1.5, 2, 0.4), (2.0, 1, 0.45), (3.0, 2, 0.35)]

bars = int(np.ceil((DUR + 2) / BAR))
k = kick()
sh = shaker()
for b in range(bars):
    root, chord = prog[b % 4]
    t0 = b * BAR
    pad = pad_chord([hz(m) for m in chord], BAR + 0.6)
    add(L, t0, pad, 0.16); add(R, t0, pad, 0.16)
    # keys: chord stab on 1, motif above
    for m in chord:
        s = key_note(hz(m), BAR, 0.11)
        add(L, t0 + 0.004 * (m % 3), s, 0.9); add(R, t0, s, 0.8)
    for off, idx, vel in motif:
        s = key_note(hz(chord[idx] + 12), BEAT * 2.5, vel * 0.22)
        pan = 0.35 + 0.3 * (idx / 3)
        add(L, t0 + off * BEAT, s, 1 - pan); add(R, t0 + off * BEAT, s, pan)
    # sub bass
    t = np.arange(int(SR * BAR)) / SR
    bass = np.sin(2 * np.pi * hz(root - 12) * t) * np.minimum(1, t / 0.02) * np.exp(-t / 2.2) * 0.32
    add(L, t0, bass); add(R, t0, bass)
    # percussion enters from bar 2
    if b >= 1:
        for beat in (0, 2):
            add(L, t0 + beat * BEAT, k, 0.28); add(R, t0 + beat * BEAT, k, 0.28)
        for e in range(8):
            g = 0.05 if e % 2 else 0.03
            add(L, t0 + e * BEAT / 2 + 0.008, sh, g * 0.8); add(R, t0 + e * BEAT / 2, sh, g)

mix = np.stack([L, R])
mix = np.stack([onepole_lp(ch, 7000) for ch in mix])
mix = mix[:, : int(SR * DUR)]
# 1.5 s fade in, 1.2 s fade out
fi = int(SR * 1.5); fo = int(SR * 1.2)
mix[:, :fi] *= np.linspace(0, 1, fi)
mix[:, -fo:] *= np.linspace(1, 0, fo)
mix /= np.max(np.abs(mix)) + 1e-9
mix *= 0.7
pcm = (mix.T * 32767).astype("<i2")
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wrote", OUT, f"{DUR:.1f}s @ {BPM} bpm")
