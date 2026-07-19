# Design Guide — PPT Generator

Reference for making informed design decisions when generating presentations.

## Table of Contents
1. [Color Palettes by Scenario](#color-palettes)
2. [Font Pairings](#font-pairings)
3. [Spacing Rules](#spacing-rules)
4. [Slide Composition Patterns](#slide-composition)
5. [Accessibility Guidelines](#accessibility)

---

## Color Palettes by Scenario

### Business (商业汇报)
```
Primary:   #1a3a5c (Deep Navy Blue)  — titles, headers, emphasis
Secondary: #f0f4f8 (Light Gray-Blue) — backgrounds, alternating rows
Accent:    #e8a817 (Warm Gold)       — highlights, calls-to-action, icons
Text:      #333333 (Charcoal)        — body text
Bg:        #ffffff (White)           — slide background
```
Use for: quarterly reports, project updates, pitch decks, corporate presentations.

### Academic (教学课件)
```
Primary:   #2c3e50 (Dark Slate)     — titles, section headers
Secondary: #ecf0f1 (Off-White Gray) — backgrounds
Accent:    #8e44ad (Purple)         — emphasis, hyperlinks, diagrams
Text:      #2c3e50 (Dark Slate)     — body text
Bg:        #ffffff (White)          — slide background
```
Use for: lectures, training materials, research presentations, courseware.

### Tech (技术分享)
```
Primary:   #00d4aa (Neon Teal)      — titles, code highlights
Secondary: #1e1e2e (Dark Navy)      — backgrounds, code blocks
Accent:    #f38ba8 (Pink)           — warnings, important notes
Text:      #cdd6f4 (Light Lavender) — body text on dark
Bg:        #1e1e2e (Dark Navy)      — slide background
```
Use for: tech talks, architecture presentations, developer conferences, hackathons.

### Creative (创意演讲)
```
Primary:   #ff6b6b (Coral Red)      — titles, key messages
Secondary: #feca57 (Sunny Yellow)   — accents, highlights
Accent:    #48dbfb (Sky Blue)       — secondary elements
Text:      #2d3436 (Dark Gray)      — body text
Bg:        #ffffff (White)          — slide background
```
Use for: product launches, creative pitches, marketing decks, keynote speeches.

### General (通用)
```
Primary:   #4a4a4a (Neutral Dark)    — titles
Secondary: #f5f5f5 (Light Gray)     — backgrounds
Accent:    #0078d4 (Microsoft Blue) — hyperlinks, emphasis
Text:      #333333 (Charcoal)       — body
Bg:        #ffffff (White)          — slide background
```
Fallback when no specific scenario is identified.

---

## Font Pairings

### Chinese + English (bilingual presentations)

| Role | Chinese Font | English Equivalent | Size |
|------|-------------|-------------------|------|
| Title | Microsoft YaHei (微软雅黑) | Segoe UI | 28-36pt |
| Subtitle | Microsoft YaHei | Segoe UI | 20-24pt |
| Body | Microsoft YaHei | Calibri | 18-22pt |
| Caption | Microsoft YaHei | Calibri | 14-16pt |
| Code | Consolas / Source Code Pro | — | 14-16pt |

### Why these fonts?
- **Microsoft YaHei**: Pre-installed on Windows, excellent CJK rendering, clean sans-serif
- **SimHei (黑体)**: Alternative for titles, bolder weight
- **Consolas**: Monospace for code, universally available

### Font size rules (non-negotiable for readability)
- **Titles**: ≥ 28pt. Below this, the back row can't read.
- **Body**: ≥ 18pt. Any smaller and slides become handouts, not presentations.
- **Captions/Footnotes**: ≥ 12pt. Anything smaller is invisible on a projector.

---

## Spacing Rules

### Margins
- Standard content margin: **0.8 inches** from slide edges
- For text-heavy slides (academic): **1.0 inches** — more breathing room
- For visual slides (creative): **0.5 inches** — maximize visual real estate

### Line Spacing
- Body text: **1.5× font size** (e.g., 18pt text = 27pt line spacing)
- Titles: **1.2× font size**
- Dense slides (technical): **1.3×** is acceptable

### Element Gaps
- Between title and body: **0.3 inches** minimum
- Between bullet items: **0.15 inches** minimum
- Between image and adjacent text: **0.3 inches** minimum

---

## Slide Composition Patterns

### Cover Slide
```
┌─────────────────────────────────────┐
│ █████████████████████████ (accent bar, 0.15in)
│
│        Presentation Title
│        (1.5in from left, 2.2in from top)
│
│        Subtitle / Author / Date
│        (below title, 0.5in gap)
│
│                              ██████ (bottom accent, 0.15in)
└─────────────────────────────────────┘
```

### Content Slide (text_left_image_right)
```
┌─────────────────────────────────────┐
│ █████████████████████████ (title bar, primary color, 0.9in)
│   Slide Title (white text, 28pt)
├─────────────────────────────────────┤
│  • Bullet 1                 ┌──────┐│
│  • Bullet 2                 │      ││
│  • Bullet 3                 │ IMG ││
│  • Bullet 4                 │      ││
│   (6.5in wide)              └──────┘│
│                             (4.8in) │
└─────────────────────────────────────┘
```

### Table of Contents
```
┌─────────────────────────────────────┐
│ 目录                                │
│ ──── (accent underline)             │
│                                     │
│  01  业绩总览                        │
│  02  区域分析                        │
│  03  产品表现                        │
│  04  下季度规划                      │
│                                     │
│  (Numbers in accent color, 24pt)     │
│  (Items in body color, 20pt)        │
└─────────────────────────────────────┘
```

### Data Slide (chart + insight)
```
┌─────────────────────────────────────┐
│ █████████████████████████ (title bar)
│   Chart Title
├─────────────────────────────────────┤
│  ┌─────────────────────┐  • Key     │
│  │                     │  • Take-   │
│  │     CHART           │  • Aways   │
│  │                     │  • Here    │
│  └─────────────────────┘            │
│   (chart 8in)          (insights 4in)
└─────────────────────────────────────┘
```

### Ending Slide
```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│              谢  谢                 │
│           (48pt, white, centered)    │
│         ─────────────               │
│           (accent bar)              │
│              Q & A                  │
│           (24pt, light)             │
│                                     │
│   (full primary-color background)    │
└─────────────────────────────────────┘
```

---

## Accessibility Guidelines

### Color Contrast (WCAG AA)
- Normal text (<18pt): contrast ratio ≥ **4.5:1**
- Large text (≥18pt or bold ≥14pt): contrast ratio ≥ **3.0:1**

The typography checker (`check_typography.py`) tests these automatically.

### Color Blindness
- Don't rely on color alone to convey meaning. Add patterns, labels, or icons.
- For charts: use distinct shapes/textures in addition to color.
- Avoid red-green as the only distinguishing pair in charts.

### Readability Checklist
- [ ] All body text ≥ 18pt
- [ ] All titles ≥ 28pt
- [ ] Maximum 7 bullet points per slide
- [ ] Maximum 2 fonts per slide
- [ ] Images have alt text in the config
- [ ] Charts have labeled axes
