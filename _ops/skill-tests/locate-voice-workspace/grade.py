"""Programmatic checks for locate-voice outputs. Usage: python grade.py iteration-N"""
import json, re, sys
from pathlib import Path

BANNED = ["leverage", "unlock", "game-changer", "game changer", "supercharge", "seamless", "robust",
          "delve", "elevate", "empower", "landscape", "fast-paced", "let that sink in", "here's why", "the truth is"]
US = ["optimize", "organization", "color", "analyze", "behavior", "favor"]
FAMILY = ["wife", "husband", "partner and", "kids", "son", "daughter", "baby", "family"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
ALLOWED_NUMS = {"ai-file-notes-instagram": set(), "journey-day-post": {"6"}, "client-win-story": {"4", "11"}}

def caption(text):
    """Best-effort: the caption is the text before the first Visual/Carousel/Note line, minus headings and hashtags."""
    body = re.split(r"\n\s*(?:\*\*)?(?:Visual|Carousel|Note|Slides?)\b", text, maxsplit=1, flags=re.I)[0]
    lines = [l for l in body.splitlines() if l.strip() and not l.startswith("#") and not l.strip().startswith("**")
             and not re.match(r"^\s*(#\w+\s*)+$", l)]
    return "\n".join(lines)

def check(eval_name, text):
    cap = caption(text)
    words = len(cap.split())
    tags = re.findall(r"(?<!\w)#[A-Za-z]\w+", text)
    nums = set(re.findall(r"\b\d+\b", cap))
    low = text.lower()
    out = [
        ("No em dashes", "—" not in text, f"em dashes found: {text.count(chr(0x2014))}"),
        ("No exclamation marks", "!" not in cap, f"count: {cap.count('!')}"),
        ("No emojis", not EMOJI.search(text), f"emojis: {EMOJI.findall(text)}"),
        ("Caption body 40-120 words", 40 <= words <= 140, f"~{words} words (parser allows 20 slack for labels)"),
        ("Instagram hashtags 3-5 (per caption)", 3 <= len(set(tags)) <= 7, f"{len(set(tags))} unique hashtags: {sorted(set(tags))}"),
        ("No banned words", not [b for b in BANNED if b in low], f"found: {[b for b in BANNED if b in low]}"),
        ("Australian spelling", not [u for u in US if re.search(rf'\b{u}', low)], f"US spellings: {[u for u in US if re.search(rf'\b{u}', low)]}"),
        ("No invented numbers in caption", nums <= ALLOWED_NUMS[re.sub(r"^eval-\d+-","",eval_name)], f"numbers in caption: {sorted(nums)}; allowed: {sorted(ALLOWED_NUMS[re.sub(r"^eval-\d+-","",eval_name)])}"),
        ("No family references", not [f for f in FAMILY if re.search(rf'\b{f}\b', low)], f"found: {[f for f in FAMILY if re.search(rf'\b{f}\b', low)]}"),
    ]
    return [{"text": t, "passed": bool(p), "evidence": e} for t, p, e in out]

it = Path(sys.argv[1])
for ev in sorted(p for p in it.iterdir() if p.is_dir()):
    for run in ev.iterdir():
        f = run / "run-1" / "outputs" / "post.md"
        if not f.exists():
            continue
        exp = check(ev.name, f.read_text(encoding="utf-8"))
        n = sum(e["passed"] for e in exp)
        (run / "run-1" / "grading.json").write_text(json.dumps({"expectations": exp, "summary": {
            "passed": n, "failed": len(exp) - n, "total": len(exp), "pass_rate": round(n / len(exp), 2)}}, indent=2))
        print(f"{ev.name}/{run.name}: {n}/{len(exp)}", [e["text"] for e in exp if not e["passed"]])
