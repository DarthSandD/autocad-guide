# LinkedIn Carousel — AutoCAD Hotkey & Command Guide

7-slide carousel promoting the guide. 1080×1080 PNGs, brand-matched to the site.

| File | Purpose |
|---|---|
| `slide-1.png` … `slide-7.png` | Upload in this order as a LinkedIn document post |
| `carousel.html` | Source. Edit, then re-render |
| `post-copy.md` | Main + short post text, posting notes, per-slide alt text |
| `shots/` | Real screenshots of the live site, embedded in slides 1, 3, 4 |
| `_v1-old/` | Earlier all-text version, kept as a fallback |

## Slides

1. Hook — "I got tired of Googling AutoCAD commands" + real desktop screenshot
2. The problem — 30 seconds of intro to find 20 seconds you needed
3. The site — 126 commands / 8 categories / one page + desktop screenshot
4. Mobile — real phone-width screenshot
5. The 12 hotkeys that do most of the work
6. The honest bit — I checked every video by hand
7. CTA

## Why these are screenshots, not AI images

Every AI image provider on this machine is unavailable (Nous 402 insufficient
credits, Google free-tier image quota 0, Ideogram 402 no credits). Slides are
rendered from HTML with headless Chrome, and slides 1/3/4 embed **real
screenshots of the live site**, which is more credible than generated art
anyway.

## Re-render

```bash
CHROME="/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
for i in 1 2 3 4 5 6 7; do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --allow-file-access-from-files --force-device-scale-factor=1 \
    --window-size=1080,1080 --virtual-time-budget=9000 \
    --screenshot="slide-$i.png" "file://$(pwd)/_one$i.html"
done
```

`#sN` alone does NOT isolate a slide (all slides share one document). Inject
`body{margin:0}.slide{display:none!important}.slide#sN{display:flex!important}`
before `</head>` and screenshot that.

## Refreshing the site screenshots

```bash
# desktop crop (slides 1, 3) — 1180x640
# mobile (slide 4) — 390x844
```

On Windows, headless Chrome clamps its window to roughly 494px minimum, so
requesting `--window-size=390,844` renders at 494 and *crops the image* to 390,
which looks like broken mobile layout. It isn't. Render mobile inside a
390px-wide iframe in a wide window instead.
