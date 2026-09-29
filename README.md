# AutoCAD Hotkey & Command Guide

Live site: https://darthsandd.github.io/autocad-guide/ (GitHub Pages, serves `index.html`).

Single-file reference for AutoCAD: 126 commands across 8 categories (Drawing, Modify,
Annotation, Layers, View, Dimension, Block, Misc) with hotkey, alias, description,
and a curated YouTube clip per command — press play on any card to open the clip at
its exact start/end timestamp in a modal player.

## Features

- Search + category filter across all commands
- Copy-to-clipboard per command (hotkey / alias)
- Sidebar navigation + scroll progress bar
- Modal YouTube player (single iframe, loads at exact start second, stops at end time)
- Honest "No clip" state: commands without a curated clip show a placeholder that
  opens a YouTube search for that exact command, instead of playing a mismatched video
- Responsive, keyboard-navigable, toast notifications

## Coverage

- 126 commands, 125 with a verified curated clip, 1 with no clip (DSVIEWER, an obsolete command).
- Video lookup is **exact-match only**. A clip is never borrowed from a
  similarly-named command (e.g. DIMBASELINE inheriting DIM), because playing the
  wrong tutorial is worse than showing none.
- Every video ID is verified live against YouTube (title + duration) before it
  ships; a dead or unavailable video is never left in place.

## Notes

- Fully self-contained: one `index.html`, no build step, no backend, no dependencies.
- Video is embedded from YouTube (per-command start/end timestamps). No local video files.

## Deploy

Local `main` pushes to remote `main`. Pages rebuilds in ~1–2 min.

```
git add -A && git commit -m "..." && git push origin main
```
