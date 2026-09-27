# AutoCAD Hotkey & Command Guide

Live site: https://darthsandd.github.io/autocad-guide/ (GitHub Pages, serves `index.html`).

Single-file reference for AutoCAD: 90+ commands across 8 categories (Draw, Modify,
Annotation, Layers, View, Dimension, Block, Misc) with hotkey, alias, description,
and a curated YouTube clip per command — press play on any card to open the clip at
its exact start/end timestamp in a modal player.

## Features

- Search + category filter across all commands
- Copy-to-clipboard per command (hotkey / alias)
- Sidebar navigation + scroll progress bar
- Modal YouTube player (single iframe, loads at exact start second, stops at end time)
- Responsive, keyboard-navigable, toast notifications

## Notes

- Fully self-contained: one `index.html`, no build step, no backend, no dependencies.
- Video is embedded from YouTube (per-command start/end timestamps). No local video files.

## Deploy

Local `main` pushes to remote `main`. Pages rebuilds in ~1–2 min.

```
git add -A && git commit -m "..." && git push origin main
```
