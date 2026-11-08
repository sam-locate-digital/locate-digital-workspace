"""Generate an original, royalty-free music bed of any length: warm keys, soft pad, sub bass, light percussion.

Usage: python -I music.py <seconds> <out.wav> [bpm]
The reel kit's synth, built as one seamless 4-bar loop and tiled, so a 15-minute bed takes seconds.
Everything is synthesised here, so Locate owns the result outright.
"""
import sys
import wave

import numpy as np

SR = 48000
DUR = float(sys.argv[1])
OUT = sys.argv[2]
BPM = float(sys.argv[3]) if len(sys.argv) > 3 else 88.0
BEAT = 60.0 / BPM
BAR = BEAT * 4
LOOP = int(round(4 * BAR * SR))
rng = np.random.default_rng(7)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def onepole_lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y


def key_note(f, length, vel):
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
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12)


def shaker():
    t = np.arange(int(SR * 0.08)) / SR
    x = rng.standard_normal(len(t))
    return (x - onepole_lp(x, 5000)) * np.exp(-t / 0.025)


L = np.zeros(LOOP + SR * 4); R = np.zeros(LOOP + SR * 4)


def add(start, sig, gl, gr=None):
    i = int(start * SR); j = min(len(L), i + len(sig))
    L[i:j] += sig[: j - i] * gl; R[i:j] += sig[: j - i] * (gl if gr is None else gr)


prog = [(41, [53, 57, 60, 64]), (45, [57, 60, 64, 67]), (48, [55, 60, 64, 71]), (43, [55, 59, 62, 64])]
motif = [(0.0, 3, 0.55), (1.5, 2, 0.4), (2.0, 1, 0.45), (3.0, 2, 0.35)]
k, sh = kick(), shaker()
for b, (root, chord) in enumerate(prog):
    t0 = b * BAR
    pad = pad_chord([hz(m) for m in chord], BAR + 0.6)
    add(t0, pad, 0.16)
    for m in chord:
        add(t0, key_note(hz(m), BAR, 0.11), 0.9, 0.8)
    for off, idx, vel in motif:
        pan = 0.35 + 0.3 * (idx / 3)
        add(t0 + off * BEAT, key_note(hz(chord[idx] + 12), BEAT * 2.5, vel * 0.22), 1 - pan, pan)
    t = np.arange(int(SR * BAR)) / SR
    add(t0, np.sin(2 * np.pi * hz(root - 12) * t) * np.minimum(1, t / 0.02) * np.exp(-t / 2.2) * 0.32, 1)
    for beat in (0, 2):
        add(t0 + beat * BEAT, k, 0.22)
    for e in range(8):
        g = 0.05 if e % 2 else 0.03
        add(t0 + e * BEAT / 2 + 0.008, sh, g * 0.8, g)

# wrap the tails that ring past the loop end back to its start, so the loop is seamless
for ch in (L, R):
    ch[:len(ch) - LOOP] += ch[LOOP:]
loop = np.stack([onepole_lp(L[:LOOP], 7000), onepole_lp(R[:LOOP], 7000)])
n = int(SR * DUR)
mix = np.tile(loop, (1, n // LOOP + 1))[:, :n]
fi, fo = min(int(SR * 1.5), n // 3), min(int(SR * 1.5), n // 3)
mix[:, :fi] *= np.linspace(0, 1, fi); mix[:, n - fo:] *= np.linspace(1, 0, fo)
mix /= np.max(np.abs(mix)) + 1e-9
mix *= 0.7
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix.T * 32767).astype("<i2").tobytes())
print("wrote", OUT, f"{DUR:.1f}s @ {BPM} bpm")
