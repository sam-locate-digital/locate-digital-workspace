"""Export voice / music / sfx stems that add up to the final mix (for editing in CapCut).

Usage: python -I stems.py <work_dir> <out_dir>
Run after audio.py: reuses aroll.mov, music.wav, sfx.wav, mix_pre.wav and mix.wav.
Music keeps its ducking under the voice. All three get the same gain the final loudness pass applied.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

WORK = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
total = json.loads((WORK / "remotion" / "src" / "data.json").read_text(encoding="utf-8"))["total"]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)
    return r.stderr


def lufs(path, af=None):
    chain = (af + "," if af else "") + "ebur128=peak=true"
    out = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", chain, "-f", "null", "-"])
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])


VOICE = ("highpass=f=80,afftdn=nr=10:nf=-42,equalizer=f=4000:t=q:w=1.2:g=2.5,"
         "acompressor=threshold=-18dB:ratio=3:attack=5:release=90:makeup=2")
v_l = lufs(WORK / "aroll.mov", VOICE)
m_l = lufs(WORK / "music.wav")
music_gain = (v_l - 20) - m_l
final_gain = lufs(WORK / "mix.wav") - lufs(WORK / "mix_pre.wav")  # the loudness pass was linear
print(f"music gain {music_gain:+.2f} dB, final gain {final_gain:+.2f} dB")

g = f"volume={final_gain:.3f}dB"
graph = (
    f"[0:a]{VOICE},aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={total},atrim=0:{total}[vc];"
    f"[vc]asplit=3[v][vsc][vout];"
    f"[1:a]volume={music_gain:.2f}dB,atrim=0:{total}[m];"
    f"[m][vsc]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=350:makeup=1,{g}[mout];"
    f"[v]anullsink;"
    f"[vout]{g}[vfinal];"
    f"[2:a]aformat=channel_layouts=stereo,atrim=0:{total},{g}[sout]"
)
run(["ffmpeg", "-hide_banner", "-y", "-i", str(WORK / "aroll.mov"), "-i", str(WORK / "music.wav"), "-i", str(WORK / "sfx.wav"),
     "-filter_complex", graph,
     "-map", "[vfinal]", "-c:a", "pcm_s24le", "-ar", "48000", str(OUT / "voice.wav"),
     "-map", "[mout]", "-c:a", "pcm_s24le", "-ar", "48000", str(OUT / "music.wav"),
     "-map", "[sout]", "-c:a", "pcm_s24le", "-ar", "48000", str(OUT / "sfx.wav")])

# Check: the three stems summed should match the final mix
check = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(OUT / "voice.wav"), "-i", str(OUT / "music.wav"), "-i", str(OUT / "sfx.wav"),
             "-filter_complex", "[0][1][2]amix=inputs=3:normalize=0,ebur128=peak=true", "-f", "null", "-"])
print("stems summed:", re.findall(r"I:\s+(-?[\d.]+) LUFS", check)[-1], "LUFS (final mix is -14.0)")
