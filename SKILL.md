---
name: ppt-generator
description: >
  Automatically generate professional PowerPoint (.pptx) presentations through an interactive step-by-step guided conversation. Use this skill whenever the user mentions making a PPT, presentation, slides, 演示文稿, 幻灯片, slideshow, deck, quarterly report, project briefing, lecture slides, pitch deck, training material, or any request to create presentation files — even if they don't explicitly say "PPT" or "skill". Supports Chinese and English, all use cases (business/academic/tech/creative), and scales from 5-slide briefs to 30+ page comprehensive decks. Features: guided 10-dimension requirement gathering, dual-channel image sourcing (web search + AI), HTML-to-PPTX native generation via PptxGenJS (requires claude-office-skills installed alongside), python-pptx fallback for templates, typography quality check, and iterative refinement.
---

# PPT Generator (Fusion Edition)

Fuses the guided conversation and media sourcing of ppt-generator with the high-quality native PPTX rendering of claude-office-skills.

## Prerequisites

This skill works best when **claude-office-skills** is installed alongside it:
```
~/.claude/skills/
├── ppt-generator/           ← this skill (guided pipeline + media sourcing)
└── claude-office-skills/    ← rendering engine (html2pptx + PptxGenJS)
```

The html2pptx engine is at `../claude-office-skills/html2pptx-local.cjs`. If that path doesn't exist, fall back to python-pptx mode.

Node dependencies must be installed once in claude-office-skills:
```bash
cd ~/.claude/skills/claude-office-skills && npm install
```

## The Pipeline

```
Gather → Content → Media → Design → Generate → Check → Iterate
                                    ├─ Mode A: python-pptx (templates, quick)
                                    └─ Mode B: html2pptx (native shapes, visual quality) ← DEFAULT
```

---

## Step 1: Gather Requirements

Ask naturally, 1-2 questions at a time. Cover these dimensions:

| Dimension | What to ask |
|-----------|------------|
| **Topic** | What's this about? |
| **Scenario** | Who's the audience? (boss/client/students/conference) |
| **Scale** | How many slides? |
| **Language** | Chinese / English / Bilingual? |
| **Template** | Have a .pptx template, or design from scratch? |
| **Style** | Visual preference? (Business / Academic / Tech dark / Creative cute / "You choose") |
| **Content** | Have material ready, or should I draft? |
| **Image Style** | Realistic photos / Anime-cartoon / Minimalist / Mixed? |
| **Design Richness** | Clean minimal, or rich decorative? ("可爱搞怪" needs stars/cards/bubbles; "商务" needs clean lines) |
| **Process** | Review outlines first, or go straight to final? |

**Crucial for creative/cute styles**: Ask "你喜欢哪种感觉？粉嫩少女 / 游戏公告栏 / 漫画分镜 / 你帮我混搭？"

Stop when you have ~80% of answers. Better to start than exhaust the user.

---

## Step 2: Generate Content

### 2a: Outline
Show a structured outline. Ask for approval.

### 2b: Slide Content
Draft text per slide. Titles clear and concise. Body as bullet points (not paragraphs), 3-7 items max.

### 2c: Content Density Limits

| Slide Type | Max Content |
|------------|------------|
| Title slide | 1 heading + 1 subtitle |
| Content slide | 1 heading + 4-6 bullets |
| Card grid | 1 heading + 6 cards max |
| Stats slide | 3-4 big numbers |
| Quote | 1 quote (max 3 lines) + attribution |

**Content exceeds limits? Split into multiple slides.**

---

## Step 3: Source Media

**MANDATORY**: Actually search for and download images. Never leave placeholders.

### Dual-Channel Strategy

| Style | Primary Channel | How |
|-------|----------------|-----|
| Realistic/Business | Web search | Tavily → Unsplash/Pexels CDN download |
| Anime/Cartoon | Web search first | "wallpaper HD free" queries, Unsplash fallback |
| Minimalist/Abstract | AI generation | Describe, generate, label as AI |
| Game/IP-specific | Web search + copyright notice | Tell user: official art is copyrighted; educational use OK |

### How to Source (Do Not Skip)

1. Search with multiple queries, different angles
2. Actually download via `requests` — try multiple CDN sources
3. For copyrighted content (game characters etc.): be honest, suggest user downloads official media for classroom use
4. Track all image sources for attribution

### Image Dissatisfaction Flow

If user doesn't like the images:

1. Provide direct search URLs:
```
📸 Find better images at:
- https://unsplash.com/s/photos/[keyword]
- https://www.pexels.com/search/[keyword]
- https://wall.alphacoders.com/ (anime/game wallpapers)
- https://www.freepik.com/ (illustrations)
```

2. Tell user: "把图片放到 `[workspace]/images/` 目录下，放好后告诉我，我立刻重新生成。"

3. Re-generate with user's images.

---

## Step 4: Design

### Scenario → Design Mapping

| Scenario | Palette | Decoration Level | Layout Style |
|----------|---------|-----------------|--------------|
| Business | Deep blue + white + gold | Low — clean, data cards | Structured, KPI-forward |
| Academic | White + navy + purple | Low-Med — numbered sections | Info-dense, clear hierarchy |
| Tech | Dark navy + neon teal + pink | Medium — code blocks, neon lines | Diagrams, code |
| **Creative/Cute** | **Pink + yellow + teal + green (Memphis pop) or user's choice** | **HIGH — go all out** | **Rounded cards, stars, bubbles, game-UI cards, bold borders, emoji-free decorative shapes** |
| General | Gray + one vibrant accent | Medium — balanced | Text + visuals |

### AI Slop Avoidance (for creative styles)

- DO: bold color combos, asymmetrical layouts, unique decorative shapes
- DO: CSS box-shadows, border-left accents, flexbox grids
- DON'T: gray-on-white everything, same-sized cards repeated, Inter/Roboto fonts
- DON'T: cyan-on-dark gradients, glassmorphism, emoji as design elements

---

## Step 5: Generate PPTX

### Mode Selection

| Condition | Mode |
|-----------|------|
| User has a .pptx template | **Mode A**: python-pptx template fill |
| No template, visual quality matters | **Mode B**: html2pptx (DEFAULT) |
| User says "快速" / "简单就行" | **Mode A**: python-pptx quick mode |

### Mode B: html2pptx (DEFAULT — Native Quality)

**This is the primary generation mode.** It produces PPTX where text is editable textboxes, colors are native shapes, and borders are native strokes — no screenshots.

#### Workflow

1. **Create one HTML file per slide** in `outputs/<project-name>/`

2. **HTML rules** (MANDATORY):
   - Body: `width:960pt;height:540pt;display:flex;...;margin:0;`
   - Fonts: web-safe only — Arial, Georgia, Verdana, Tahoma, Trebuchet MS, Impact
   - ALL text in `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>` — never bare text in `<div>` or `<span>`
   - NO `<br>` tags — use separate `<p>` elements
   - NO manual bullets (•, -, *) — use `<ul>` or `<ol>`
   - Backgrounds and borders only on `<div>` elements
   - Use `display:flex` for layout
   - Use hex colors with `#` prefix

3. **Write build script** `outputs/<project-name>/build.cjs`:
   ```javascript
   const pptxgen = require('pptxgenjs');
   const html2pptx = require('../claude-office-skills/html2pptx-local.cjs');
   const fs = require('fs'), path = require('path');

   async function main() {
       const pptx = new pptxgen();
       pptx.layout = 'LAYOUT_WIDE';
       const slides = ['slide_01.html', 'slide_02.html', ...];
       for (const f of slides) {
           await html2pptx(path.join(__dirname, f), pptx);
       }
       await pptx.writeFile({ fileName: 'output.pptx' });
   }
   main();
   ```

4. **Run**: `node outputs/<project-name>/build.cjs`

5. **For user images**: Reference them in HTML with `<img src="images/photo.jpg" style="max-width:100%;max-height:min(50vh,400px);object-fit:contain;">`

#### HTML Slide Templates

**Title Slide**:
```html
<body style="width:960pt;height:540pt;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#FF6B9D;font-family:Arial,sans-serif;margin:0;">
  <div style="text-align:center;">
    <h1 style="font-size:42pt;font-weight:900;color:#fff;margin:0;">Title</h1>
    <p style="font-size:18pt;color:rgba(255,255,255,0.85);margin:0;margin-top:8pt;">Subtitle</p>
  </div>
</body>
```

**Content Slide with Cards**:
```html
<body style="width:960pt;height:540pt;display:flex;flex-direction:column;background:#FFFBFA;font-family:Arial,sans-serif;margin:0;padding:30pt;box-sizing:border-box;">
  <div style="background:#FF6B9D;height:5pt;width:100%;margin-bottom:16pt;"></div>
  <p style="font-size:24pt;font-weight:900;color:#FF6B9D;margin:0;margin-bottom:16pt;">Slide Title</p>
  <div style="display:flex;gap:16pt;flex:1;">
    <div style="flex:1;background:#fff;border:3pt solid #000;padding:16pt;">
      <p style="font-size:28pt;font-weight:900;color:#FF6B9D;margin:0;">Key Number</p>
      <p style="font-size:13pt;font-weight:900;margin:0;margin-top:4pt;">Label</p>
      <p style="font-size:10pt;color:#333;margin:0;margin-top:4pt;">Description text here.</p>
    </div>
    <!-- repeat cards -->
  </div>
</body>
```

**Stats Slide** (big numbers on colored bg):
```html
<body style="width:960pt;height:540pt;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#F5D547;font-family:Arial,sans-serif;margin:0;">
  <p style="font-size:32pt;font-weight:900;color:#000;margin:0;margin-bottom:30pt;">Section Title</p>
  <div style="display:flex;gap:30pt;">
    <div style="text-align:center;background:#fff;border:3pt solid #000;padding:24pt 36pt;">
      <p style="font-size:42pt;font-weight:900;color:#FF6B9D;margin:0;">$10B+</p>
      <p style="font-size:14pt;font-weight:700;margin:0;margin-top:6pt;">Global Revenue</p>
    </div>
    <!-- repeat stats -->
  </div>
</body>
```

**Market Bar Chart** (CSS bars — simple and effective):
```html
<body style="width:960pt;height:540pt;display:flex;flex-direction:column;justify-content:center;background:#4ECDC4;font-family:Arial,sans-serif;margin:0;padding:30pt;box-sizing:border-box;">
  <p style="font-size:28pt;font-weight:900;color:#fff;margin:0;margin-bottom:24pt;">Market Share</p>
  <div style="display:flex;flex-direction:column;gap:10pt;width:100%;">
    <div style="display:flex;align-items:center;gap:12pt;">
      <p style="width:100pt;font-size:14pt;font-weight:900;color:#fff;text-align:right;margin:0;">Japan</p>
      <div style="flex:1;background:#FF6B9D;height:28pt;display:flex;align-items:center;padding-left:8pt;">
        <p style="font-size:13pt;font-weight:900;color:#fff;margin:0;">35%</p>
      </div>
    </div>
    <!-- repeat bars at different widths -->
  </div>
</body>
```

**Closing Slide**:
```html
<body style="width:960pt;height:540pt;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#FF6B9D;font-family:Arial,sans-serif;margin:0;">
  <div style="background:#fff;border:4pt solid #000;padding:32pt 56pt;text-align:center;">
    <h1 style="font-size:48pt;font-weight:900;color:#FF6B9D;margin:0;">Thank You</h1>
    <p style="font-size:18pt;font-weight:900;color:#000;margin:0;margin-top:12pt;">Q & A</p>
  </div>
</body>
```

### Mode A: python-pptx (Template or Quick Mode)

Use the bundled `scripts/generate_pptx.py`:
```bash
python scripts/generate_pptx.py --config config.json --output output.pptx
```

Read `references/layout_catalog.md` for available slide types and layouts.

---

## Step 6: Quality Check

After generation, run the typography checker on the output:
```bash
python scripts/check_typography.py <output.pptx>
```

For html2pptx output, also visually verify:
- No text cut off at slide edges
- Colors render as expected
- Images are positioned correctly

---

## Step 7: Iterate

Each round of feedback = mini-cycle: understand change → modify HTML or config → re-generate → re-check.

---

## Quick Reference: Mode Selection

| User says | Use |
|-----------|-----|
| "用我的模板" | Mode A: python-pptx template fill |
| "快速/简单就行" | Mode A: python-pptx quick |
| Everything else | **Mode B: html2pptx** (default) |

---

## Important Reminders

- **Image attribution**: Track sources. Add credits slide or footnote.
- **Copyright**: For game/movie IP images, tell user official art is copyrighted; suggest official media for educational use.
- **The html2pptx engine** lives at `../claude-office-skills/html2pptx-local.cjs` relative to this skill. If missing, fall back to python-pptx.
- **Web-safe fonts only** in html2pptx mode: Arial, Georgia, Verdana, Tahoma, Trebuchet MS, Impact, Times New Roman, Courier New, Comic Sans MS.
- **Large presentations (>15 slides)**: Warn user. Split build into batches.
- **NO emoji** in slide content. Use styled text instead.
