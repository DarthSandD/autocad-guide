#!/usr/bin/env python3
"""Render the Instagram 4:5 carousel (1080x1350) from carousel-ig.html.

Isolates each .slide by injecting a display:none rule before </head>,
then screenshots with headless Chrome. Mirrors the LinkedIn render recipe.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "carousel-ig.html"
SHOTS_SRC = HERE.parent / "linkedin" / "shots"
SHOTS_DST = HERE / "shots"

CHROME = Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
W, H = 1080, 1350
N = 7


def main() -> int:
    if not CHROME.exists():
        print(f"error: chrome not found at {CHROME}", file=sys.stderr)
        return 1
    if not SRC.exists():
        print(f"error: {SRC} missing", file=sys.stderr)
        return 1

    # shots/ must sit next to the HTML for relative <img src="shots/...">
    SHOTS_DST.mkdir(exist_ok=True)
    for png in SHOTS_SRC.glob("*.png"):
        dst = SHOTS_DST / png.name
        if not dst.exists() or dst.stat().st_mtime < png.stat().st_mtime:
            shutil.copy2(png, dst)
    print(f"shots ready: {[p.name for p in sorted(SHOTS_DST.glob('*.png'))]}")

    html = SRC.read_text(encoding="utf-8")
    for i in range(1, N + 1):
        isolate = (
            f"<style>body{{margin:0}}"
            f".slide{{display:none!important}}"
            f".slide#s{i}{{display:flex!important}}</style>"
        )
        one = html.replace("</head>", isolate + "</head>", 1)
        one_path = HERE / f"_one{i}.html"
        one_path.write_text(one, encoding="utf-8")

        out = HERE / f"slide-{i}.png"
        cmd = [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--allow-file-access-from-files",
            "--force-device-scale-factor=1",
            f"--window-size={W},{H}",
            "--virtual-time-budget=9000",
            f"--screenshot={out}",
            one_path.as_uri(),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not out.exists():
            print(f"error: slide {i} not rendered\n{r.stderr[-800:]}", file=sys.stderr)
            return 1
        print(f"  slide-{i}.png  {out.stat().st_size // 1024} KB")

    # verify real dimensions
    import struct
    for i in range(1, N + 1):
        p = HERE / f"slide-{i}.png"
        with open(p, "rb") as f:
            w, h = struct.unpack(">II", f.read(24)[16:24])
        flag = "OK" if (w, h) == (W, H) else "!! WRONG"
        print(f"slide-{i}.png  {w}x{h}  {flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
