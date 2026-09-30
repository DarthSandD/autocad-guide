# Caption Brief — AutoCAD Hotkey & Command Guide

Hand this file to any AI (or writer) and it has everything needed to write a
LinkedIn caption for this project. Every fact below was verified against the
live site on 2026-09-30. Nothing here is a guess.

---

## 1. What the product actually is

A single-page web reference for AutoCAD commands.

- **126 commands**, across **8 categories** (Drawing 20, Modifying 24,
  Annotation 15, Layers 18, Blocks 10, Navigation 9, Settings 13,
  Management 17 — sums to exactly 126).
- Each command shows: the **hotkey/alias**, a **one-line description**, and a
  **short video clip that opens at the exact second the command is explained**
  and stops at the end timestamp.
- **125 of 126 commands have a verified clip.** 1 does not (`DSVIEWER`, an
  obsolete command) — that card honestly reads "No clip" and links to a
  YouTube search instead of playing a mismatched video.
- **Search** matches on command name, hotkey, or plain-English intent
  (e.g. "offset", "O", "space between walls" all find OFFSET).
- **Category filter**, **copy-to-clipboard** for the hotkey/alias.
- **Responsive** — works at phone width (verified 0px horizontal overflow at
  360/390/414/430px).
- **Free, no signup, no app, no email.** Just a web page.

### The technical facts, if the caption goes technical

- **One `index.html`, 50 KB.** No framework, no build step, no backend, no
  dependencies, no CDN scripts.
- Video is embedded from YouTube via a single iframe in a modal, loaded at the
  start second.
- **Video lookup is exact-match only** — a clip is never borrowed from a
  similarly-named command. Playing the wrong tutorial is treated as worse than
  showing none.
- Every video ID was **verified live against YouTube** (title + duration)
  before shipping.
- Hosted on GitHub Pages; repo is `DarthSandD/autocad-guide`.

### The one genuinely interesting engineering detail

While auditing the clip list, a **deleted video was found still linked to 4
commands** (CIRCLE, POLYLINE, RECTANGLE, EXTEND) — anyone
clicking those got a broken player. A **separate clip pointed at a completely
unrelated topic** (OFFSET linked to a video about nesting). Both were replaced.

That's the most credible fact in the whole story: it's specific, it's
unflattering, and it's the kind of thing only someone who actually checked
would know. **Recommend keeping it.**

---

## 2. Who is posting, and how to position them

**Darren Lieu** — experienced AutoCAD/drafting practitioner, near-professional
level. He is **not** a beginner and the caption must not imply he is.

**Positioning rule: he is the person who noticed the problem and fixed it, not
the person who suffers from it.**

| Do not write | Write instead |
|---|---|
| "I still Google basic commands" | "Drawings take longer than they should because commands get typed out in full" |
| "I built this to help myself" | What the tool does for the reader |
| "I'm learning AutoCAD" | Framing him as someone who knows the shortcuts cold |

**Hard constraints:**

- **No first-person narrative.** No "I built / I noticed / I still struggle".
  Third person, benefit-first. This is the single most important rule.
- No beginner framing anywhere.
- No em dashes. (Reads as machine-written; the audience notices.)
- No marketing vocabulary: *seamless, leverage, unlock, game-changer, dive into,
  effortless, supercharge*.
- No "Here's the thing" / "Let that sink in" openers.
- No "Agree?" / "Thoughts?" closers.
- No neat two-part contrasts ("Not a PDF. Not a blog post.").
- No bolded-label-then-paragraph repeated down the page.

---

## 3. Audience and platform

- **Platform:** LinkedIn. Limit 3,000 chars; aim 800–1,300 so it doesn't
  truncate awkwardly behind "see more".
- **Audience:** drafters, CAD technicians, MEP/architectural/electrical
  designers, engineers, CAD managers, and students.
- **What earns engagement with them:** recognising a specific daily annoyance,
  a concrete number, and a tip they can use immediately (the 12 hotkeys).
- **Tone:** plain, confident, short sentences, one idea per line.

---

## 4. The 12 hotkeys (real, from the site)

`L` Line · `C` Circle · `M` Move · `CO` Copy · `TR` Trim · `EX` Extend ·
`O` Offset · `MI` Mirror · `F` Fillet · `AR` Array · `RO` Rotate · `SC` Scale

Slide 5 of the carousel is built on these, so a caption that references them
lines up with the images.

---

## 5. The carousel the caption must match

7 slides, 1080×1080, uploaded in order as a LinkedIn document post.

| # | Slide |
|---|---|
| 1 | "I got tired of Googling AutoCAD commands" + real desktop screenshot |
| 2 | "You sit through 30 seconds of intro to find the 20 seconds you needed" |
| 3 | "126 commands. 8 categories. One page." + real desktop screenshot |
| 4 | "Because that's where you actually look things up" + real phone screenshot |
| 5 | The 12 hotkeys above |
| 6 | The checked-every-video story (dead video linked to 4 commands) |
| 7 | CTA + URL + closing question |

**Note for whoever writes this:** slide 1 still opens on the *"I got tired of
Googling"* first-person line, which conflicts with the no-first-person rule
above. Either keep the caption's opening aligned with the slide, or re-render
slide 1 to match a third-person caption. Flag the choice rather than silently
mismatching.

---

## 6. Link handling

**Put the URL in the first comment, not the post body.** LinkedIn suppresses
reach on posts containing external links in the body.

`darthsandd.github.io/autocad-guide`

---

## 7. Closing question — pick one

- What's the one command you still type the long way?
- Which hotkey took you embarrassingly long to start using?
- What's your most-used AutoCAD shortcut that isn't on this list?

Ask something a drafter would genuinely enjoy answering. Avoid "Agree?" and
"Thoughts?".

---

## 8. Hashtags

Three or four at the very bottom, never a wall:
`#AutoCAD #CAD #Drafting` (add `#MEP` only if the post claims that discipline)

---

## 9. Reference: current caption (for style, not to copy verbatim)

> Most AutoCAD drawings take longer than they should.
>
> Not because the drafter is slow. Because half the commands get typed out in
> full when a two-letter hotkey does the same thing.
>
> 126 commands on one page. Hotkey, a one-line description, and a clip that
> starts at the exact second it's explained. No intros. No 40-minute tutorials.
>
> 8 categories, and search that actually works. Type "offset", "O", or "space
> between walls" and it finds the same command.
>
> Works on your phone. No app, no signup, no email.
>
> Slide 5 has the 12 hotkeys that do most of the work. If you only ever learn
> 12, learn those.
>
> Every video link was checked by hand. One had been deleted and was still
> linked to 4 commands. Another was about something completely unrelated. Both
> fixed. For the one command with no decent clip available, the card says "no
> clip" rather than playing the wrong thing.
>
> Free. Bookmark it and save yourself the next search.
>
> What's the one command you still type the long way?
>
> `#AutoCAD #CAD #Drafting`

1,002 chars · 0 em dashes · 0 first-person references.

---

## 10. Fact sheet — copy these numbers, don't invent new ones

| Fact | Value |
|---|---|
| Commands | 126 |
| Categories | 8 |
| Commands with a verified clip | 125 |
| Commands without a clip | 1 (DSVIEWER, obsolete) |
| Size | one 50 KB `index.html` |
| Dependencies / build step | none |
| Cost / signup | free, none |
| URL | darthsandd.github.io/autocad-guide |
| Repo | github.com/DarthSandD/autocad-guide |
| Author | Darren Lieu |

**If a caption needs a number not on this list, do not invent it.** Check the
live site or ask.
