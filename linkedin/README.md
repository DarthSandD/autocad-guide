# LinkedIn Carousel — AutoCAD Hotkey & Command Guide

7-slide carousel promoting the guide. 1080×1080 PNGs, brand-matched to the site.

| File | Purpose |
|---|---|
| `slide-1.png` … `slide-7.png` | Upload in this order as a LinkedIn document post |
| `carousel.html` | Source. Edit, then re-render (see below) |
| `post-copy.md` | 3 post options, posting notes, per-slide alt text |

## Slides

1. Cover — 126 commands / 8 categories / 125 clips
2. The Problem — you lose hours to the ribbon, not AutoCAD
3. The 12 Essential Hotkeys
4. Eight Categories (counts sum to 126)
5. How It Works — search, copy, watch
6. Built Different — one HTML file, zero dependencies
7. CTA — link

## Re-render

Slides are rendered with headless Chrome (no AI image gen available — all
providers returned 402/429). To rebuild after editing `carousel.html`:

```bash
CHROME="/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
for i in 1 2 3 4 5 6 7; do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1080 \
    --virtual-time-budget=7000 --screenshot="slide-$i.png" \
    "file:///$(pwd)/carousel.html#s$i"
done
```

Note: `#sN` alone does not isolate a slide (all slides share one document).
To render a single slide, inject `body{margin:0}.slide{display:none!important}.slide#sN{display:flex!important}` before `</head>`.
