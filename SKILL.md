---
name: ppt-generator
description: >
  Automatically generate professional PowerPoint (.pptx) presentations through an interactive step-by-step guided conversation. Use this skill whenever the user mentions making a PPT, presentation, slides, 演示文稿, 幻灯片, slideshow, deck, quarterly report, project briefing, lecture slides, pitch deck, training material, or any request to create presentation files — even if they don't explicitly say "PPT" or "skill". This skill handles the full pipeline: requirement gathering, content generation, image sourcing (web search + AI), design/layout selection, .pptx generation, typography quality check, and iterative refinement. Supports Chinese and English, all use cases (business/academic/tech/creative), and scales from 5-slide briefs to 30+ page comprehensive decks.
---

# PPT Generator

Generate professional PowerPoint (.pptx) files through guided interactive conversation.

## Why This Skill Exists

Creating a polished presentation takes time and design sense — most people spend hours tweaking layouts and formatting instead of focusing on content. This skill automates the mechanical parts while keeping the user in creative control. It handles the full pipeline: understand what the user needs → generate content → source media → design slides → build the file → check quality → iterate. The result is a .pptx the user can download and further edit in PowerPoint.

## The Pipeline (7 Steps)

```
Gather → Content → Media → Design → Generate → Check → Iterate
```

Don't skip steps. Each step is essential for quality. But be smart — if the user says "just make it fast" or "直接生成", collapse steps 1-4 into a single efficient pass.

---

## Step 1: Gather Requirements (Guided Conversation)

The goal is to collect enough information to make informed design and content decisions. Don't ask all questions at once — ask them naturally, one or two at a time, adapting to what the user has already volunteered.

### The 10 Dimensions to Cover

| Dimension | Key Question | Why It Matters |
|-----------|-------------|----------------|
| **Topic** | What's the presentation about? | Drives content generation direction |
| **Scenario** | Who's the audience? (boss/client/students/conference) | Determines formality, tone, design style |
| **Scale** | Roughly how many slides? | Affects structure depth and generation strategy |
| **Language** | Chinese, English, or both? | Font selection, text positioning |
| **Template** | Have a .pptx template? Or should I design from scratch? | Build mode: template-fill vs. code-generate |
| **Style** | Preferred visual style? (Business professional / Academic clean / Tech dark / Creative bold / "You choose") | Color palette, font pairing, layout density |
| **Content** | Have specific content ready, or should I draft it for you? | AI generation vs. user-provided text |
| **Image Style** | For any visuals: realistic photos, anime/cartoon, minimalist abstract, or mixed? | Image sourcing strategy (search vs. AI) |
| **Charts/Data** | Need charts, tables, flowcharts, or diagrams? | Triggers charting tools and Mermaid rendering |
| **Process** | Want to review outlines before generation, or go straight to final output? | Determines checkpoint frequency |

### How to Ask

Be conversational, not robotic. For example:
- "这个PPT是给谁看的？客户、领导还是大会听众？" (Who's the audience?)
- "大概需要多少页？5-10页的简报还是更完整的报告？" (How many slides?)

**Important**: If the user already mentioned something (e.g., "帮我做个Q2销售汇报PPT"), don't re-ask — infer what you can and only ask about the missing pieces. The user's first sentence often answers 3-4 dimensions at once.

Stop gathering when you have answers for most dimensions, or when the user signals impatience. It's better to start generating with 80% information than to exhaust the user with questions.

---

## Step 2: Generate Content

### 2a: Produce an Outline

Based on the topic and scale, generate a structured outline:

```
## PPT 大纲
1. 封面 — [标题]
2. 目录 — [章节概览]
3. [章节一标题]
   3.1 [小节]
   3.2 [小节]
4. [章节二标题]
   ...
N. 总结与致谢
```

Show the outline to the user. Ask: "这个大纲可以吗？有没有要增减的内容？"

### 2b: Generate Slide Content

Once the outline is approved, draft the text for each slide:
- **Titles**: Clear, concise, action-oriented
- **Body**: Bullet points (not paragraphs), 3-7 items per slide
- **Data placeholders**: Mark where charts/tables should go with `[图表: 描述]`
- **Image placeholders**: Mark with `[图片: 搜索关键词 | 风格偏好]`

For the iterative mode, show content slide-by-slide or in batches for large decks. For direct mode, generate all at once.

### 2c: Handle User-Provided Content

If the user pastes their own text/outline/data, don't overwrite it — use it as the source of truth. Clean up formatting, suggest improvements gently, but respect their material.

---

## Step 3: Source Media

### Image Strategy (Dual-Channel)

**Default priority**: Web search for real photos → AI generation for style-specific needs.

| User's Style Preference | Primary Channel | Fallback |
|------------------------|-----------------|----------|
| 写实/Realistic/Professional | Web search (Unsplash, Pexels, Bing Images) | AI generation |
| 二次元/卡通/Anime | AI generation | Web search |
| 极简/抽象/Minimalist | AI generation | Web search |
| 商务/Business | Web search | AI generation |
| "你帮我选" / Not specified | Smart auto-select based on PPT scenario | — |

### How to Source Images

1. **Web search**: Use the search tool (Tavily or built-in) to find suitable images. Search with descriptive keywords + style modifiers. E.g., "business meeting professional photo" or "mountain landscape minimalist"
2. **AI generation**: Describe the image need in detail, then use available image generation tools. Always note that AI-generated images should be labeled as such.
3. **Download**: Save images locally, then insert into the PPT via scripts. Track all image sources for attribution.

### Video Recommendations

If the presentation context suggests video would enhance it (product demos, event highlights, training), proactively suggest:
- **Free stock**: Pexels Video, Pixabay Video, Coverr
- **Professional**: Storyblocks, Artgrid
- **User's own**: Ask if they have local video files

Don't push video if the context doesn't call for it (e.g., a text-heavy academic report).

---

## Step 4: Design & Layout

### Scene-Adaptive Design Selection

Based on the scenario from Step 1, pick a design direction:

| Scenario | Palette | Font Feel | Layout Style |
|----------|---------|-----------|--------------|
| 商业汇报 (Business) | Deep blue + white + accent gold | Professional sans-serif | Structured, data-forward |
| 教学课件 (Academic) | Clean white + navy + muted accent | Readable serif headings | Information-dense, clear hierarchy |
| 技术分享 (Tech) | Dark bg + neon accent + white text | Modern monospace touches | Code blocks, diagrams |
| 创意演讲 (Creative) | Bold contrasting colors | Playful yet readable | Visual-first, minimal text |
| 通用 (General) | Neutral gray + one vibrant accent | Clean sans-serif | Balanced text + visuals |

Let the user override your choice. The design is a suggestion, not a command.

### Key Design Principles

- **Less is more**: Each slide should communicate ONE idea. If a slide has more than 7 bullet points, split it.
- **Consistency**: Same fonts, same color roles, same spacing throughout. This is non-negotiable.
- **Readability**: Minimum 18pt for body text, 28pt+ for titles. No exceptions.
- **White space**: Don't fill every corner. Empty space is a design element.

---

## Step 5: Generate the PPTX

Use the bundled `scripts/generate_pptx.py` script to build the .pptx file.

### Usage

```bash
python scripts/generate_pptx.py \
  --config <path-to-config.json> \
  --output <output-filename.pptx>
```

### Config JSON Structure

Before running the script, write a config.json that captures all decisions from Steps 1-4:

```json
{
  "meta": {
    "title": "Q2 销售业绩汇报",
    "language": "zh",
    "scenario": "business"
  },
  "design": {
    "mode": "from-scratch",
    "template_path": null,
    "slide_width_inches": 13.333,
    "slide_height_inches": 7.5,
    "palette": {
      "primary": "#1a3a5c",
      "secondary": "#f0f4f8",
      "accent": "#e8a817",
      "text": "#333333",
      "background": "#ffffff"
    },
    "fonts": {
      "title": "Microsoft YaHei",
      "body": "Microsoft YaHei",
      "title_size_pt": 32,
      "body_size_pt": 18
    }
  },
  "slides": [
    {
      "type": "cover",
      "title": "2026年Q2 销售业绩汇报",
      "subtitle": "销售部 | 2026年7月"
    },
    {
      "type": "toc",
      "title": "目录",
      "items": ["业绩总览", "区域分析", "产品表现", "下季度规划"]
    },
    {
      "type": "content",
      "layout": "text_left_image_right", 
      "title": "Q2整体业绩",
      "body": ["总营收：¥5,200万", "同比增长：+18%", "完成率：112%"],
      "image": {"path": "assets/img/chart_q2.png", "alt": "Q2业绩趋势图"}
    },
    {
      "type": "chart",
      "title": "区域销售对比",
      "chart_type": "bar",
      "data": {"categories": ["华东","华南","华北","西部"], "series": {"销售额": [2100, 1500, 1100, 500]}}
    },
    {
      "type": "table",
      "title": "产品线表现",
      "headers": ["产品", "销售额", "同比增长", "市场份额"],
      "rows": [["产品A", "¥1,800万", "+22%", "35%"], ["产品B", "¥1,400万", "+15%", "27%"]]
    },
    {
      "type": "ending",
      "title": "谢谢",
      "subtitle": "Q&A"
    }
  ]
}
```

### Supported Slide Types

- `cover` — Title slide with title + subtitle + optional background
- `toc` — Table of contents with numbered or bullet items
- `content` — General content slide. Supports layouts: `text_only`, `text_left_image_right`, `image_left_text_right`, `text_top_image_bottom`, `two_column`, `three_column`
- `chart` — Data chart. Supports `bar`, `line`, `pie`, `horizontal_bar`. Data in categories + series format.
- `table` — Formatted data table with header row styling
- `image` — Full-slide image with optional overlay text
- `diagram` — Flowchart/architecture diagram (pre-rendered as image)
- `ending` — Closing slide with thank you + Q&A

### Template Mode

If the user provides a .pptx template:
- Set `design.mode` to `"template"`
- Set `design.template_path` to the template file path
- The script reads slide layouts from the template and fills in content respecting the template's existing placeholders and styling
- Read `references/template_guide.md` for detailed template handling instructions

---

## Step 6: Typography & Layout Check

After generating the .pptx, **always** run the quality check script:

```bash
python scripts/check_typography.py <output.pptx>
```

This script inspects each slide and produces a report checking:

| Check | What It Catches |
|-------|----------------|
| **Text overflow** | Text boxes with content exceeding their boundaries |
| **Font consistency** | Mixed or unexpected fonts within the same slide |
| **Minimum font size** | Body text below 18pt, titles below 28pt |
| **Alignment** | Elements not aligned to grid/guides |
| **Contrast** | Text-background color contrast below readability thresholds |
| **Overlapping** | Elements that visually overlap or are too close |

### Presenting the Report

Show the user a clean summary:

```
🔍 排版检查报告 (5/20 页有问题)
├─ Slide 3: 文本框溢出 (正文第2段超出边界 ~12pt)
├─ Slide 7: 标题字号过小 (24pt → 建议 ≥28pt)  
├─ Slide 7: 颜色对比度偏低 (浅灰文字#999 on 白色)
├─ Slide 12: 两个文本框重叠 (左侧列表 vs 右侧图片)
└─ Slide 15: 字体不一致 (正文混入了宋体)

是否自动修复这些问题？(y/n/逐项确认)
```

If the user says yes, the script attempts fixes and reports what was changed. Some issues (like content that's genuinely too long) can't be auto-fixed — flag those for manual adjustment.

---

## Step 7: Iterate

After users review the output:
- They may want layout changes ("第3页换个左右布局")
- They may want style tweaks ("整体颜色太暗了")
- They may want content adjustments ("加一页关于竞品分析")

Treat each round of feedback as a mini-cycle: understand the change → modify the config → re-generate → re-check. Re-use existing slides that don't need changes.

When the user is satisfied, deliver the final .pptx file path.

---

## Bundled Resources

### Scripts
- `scripts/generate_pptx.py` — Core PPTX generation engine. Read this when you need to understand available slide types, layout options, or chart capabilities in detail.
- `scripts/check_typography.py` — Post-generation quality checker. Run after every generation.
- `scripts/search_images.py` — Image search and download helper.

### References
- `references/design_guide.md` — Detailed design guidelines: color palettes, font pairings, spacing rules, slide composition patterns. Read when making design decisions.
- `references/layout_catalog.md` — Visual catalog of all slide layouts with descriptions and use cases.
- `references/template_guide.md` — How to work with user-provided .pptx templates. Read when the user supplies a template.

### Assets
- `assets/templates/` — Built-in PPT templates for quick start (business, academic, tech, creative). Use when the user chooses "built-in template" mode but doesn't provide their own.

---

## Quick Reference: When to Skip Steps

If the user explicitly says "直接生成" / "just make it" / "快速模式" / "不要问太多":
- ✅ Skip Step 1: Infer from context, ask at most 3 critical questions
- ✅ Skip Step 2b confirmation: Generate content without user review
- ✅ Skip Step 4: Auto-select design, don't ask
- ❌ Never skip Step 5 (generation itself)
- ❌ Never skip Step 6 (quality check — it's automated anyway)
- ✅ Skip Step 7 unless user provides feedback

---

## Important Reminders

- **Image attribution**: Every image inserted should have its source tracked (URL or "AI-generated"). Add a small footnote or remarks slide with image credits at the end.
- **File paths**: Use absolute paths for all script invocations. The working directory may vary.
- **Chart data integrity**: Always validate user-provided data before charting — check for logic errors (e.g., percentages > 100%, negative values in wrong contexts).
- **Mermaid diagrams**: When the user needs flowcharts or architecture diagrams, generate Mermaid syntax, render it to an image via available tools, then insert as a diagram slide.
- **Large presentations (>20 slides)**: Warn the user that generation will take longer. Suggest splitting into sections for better manageability.
