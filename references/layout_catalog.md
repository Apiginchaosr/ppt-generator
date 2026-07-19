# Layout Catalog — PPT Generator

Complete catalog of available slide layouts with descriptions, use cases, and config examples.

## Table of Contents
- [Cover](#cover)
- [TOC](#toc)
- [Content Layouts](#content-layouts)
  - [text_only](#text_only)
  - [text_left_image_right](#text_left_image_right)
  - [image_left_text_right](#image_left_text_right)
  - [text_top_image_bottom](#text_top_image_bottom)
  - [two_column](#two_column)
  - [three_column](#three_column)
- [Chart](#chart)
- [Table](#table)
- [Image](#image)
- [Diagram](#diagram)
- [Ending](#ending)

---

## Cover

Title slide — the first impression.

**Best for**: Opening of any presentation.

**Config**:
```json
{
  "type": "cover",
  "title": "2026年Q2 销售业绩汇报",
  "subtitle": "销售部 | 2026年7月"
}
```

**Visual**: Centered title + subtitle on clean background, with accent bars top and bottom.

---

## TOC

Table of contents — audience roadmap.

**Best for**: Presentations with 3+ sections, typically slide 2.

**Config**:
```json
{
  "type": "toc",
  "title": "目录",
  "items": ["业绩总览", "区域分析", "产品表现", "下季度规划"]
}
```

**Visual**: Numbered list with accent-colored indices, title + accent underline.

**Tip**: For presentations with ≤3 slides total, skip the TOC — it's not necessary.

---

## Content Layouts

### text_only

Pure text, no images. The workhorse layout.

**Best for**: Explaining concepts, listing points, text-heavy content.

```json
{
  "type": "content",
  "layout": "text_only",
  "title": "Q2关键发现",
  "body": [
    "华东区营收首次突破 ¥2,000万",
    "线上渠道占比从35%提升至48%",
    "客户满意度评分达到4.8/5.0",
    "新客户获客成本下降15%"
  ]
}
```

**Design notes**: Keep bullets to 5-7 items max. If you have more, split across two slides.

---

### text_left_image_right

Text on the left (60%), image on the right (40%).

**Best for**: Introducing a concept with a visual example, product showcase, team introduction.

```json
{
  "type": "content",
  "layout": "text_left_image_right",
  "title": "新产品发布",
  "body": [
    "AI驱动的智能分析引擎",
    "支持自然语言查询",
    "毫秒级响应速度",
    "企业级安全保障"
  ],
  "image": {"path": "assets/img/product.png", "alt": "产品界面截图"}
}
```

---

### image_left_text_right

Mirror of above — image left, text right.

**Best for**: Visual-first storytelling, case studies, before/after comparisons.

---

### text_top_image_bottom

Text on top, image fills lower portion.

**Best for**: Diagrams, screenshots, maps with explanatory text above.

---

### two_column

Side-by-side content blocks with a vertical divider.

**Best for**: Comparisons, pros/cons, before/after, Chinese + English bilingual slides.

```json
{
  "type": "content",
  "layout": "two_column",
  "title": "方案对比",
  "body": {
    "left": ["方案A：成本低", "部署周期短", "功能基础"],
    "right": ["方案B：功能全面", "可定制化强", "成本较高"]
  }
}
```

---

### three_column

Three equal columns.

**Best for**: Feature trios, three options, timeline overview (past/present/future).

```json
{
  "type": "content",
  "layout": "three_column",
  "title": "三阶段路线图",
  "body": {
    "col1": ["Phase 1: 基础搭建", "Q3完成"],
    "col2": ["Phase 2: 功能完善", "Q4完成"],
    "col3": ["Phase 3: 全面推广", "明年Q1"]
  }
}
```

---

## Chart

Data visualization with embedded chart.

**Best for**: Sales data, trends, survey results, any quantitative comparison.

**Supported chart types**: `bar`, `horizontal_bar`, `line`, `pie`

```json
{
  "type": "chart",
  "title": "区域销售对比",
  "chart_type": "bar",
  "data": {
    "categories": ["华东", "华南", "华北", "西部"],
    "series": {
      "Q1销售额": [1800, 1200, 900, 400],
      "Q2销售额": [2100, 1500, 1100, 500]
    }
  }
}
```

**Data best practices**:
- Bar charts: Up to 10 categories, 3 series max
- Line charts: Time-series data, up to 3 lines
- Pie charts: 2-6 slices (beyond 6, use a bar chart)
- Always label axes and include units

---

## Table

Formatted data table with header row.

**Best for**: Feature matrices, pricing, specifications, structured data.

```json
{
  "type": "table",
  "title": "产品线表现",
  "headers": ["产品", "销售额", "同比增长", "市场份额"],
  "rows": [
    ["产品A", "¥1,800万", "+22%", "35%"],
    ["产品B", "¥1,400万", "+15%", "27%"],
    ["产品C", "¥950万", "+8%", "18%"]
  ]
}
```

**Tips**:
- Keep columns to 5 or fewer for readability
- Use alternating row colors automatically
- Right-align numbers, left-align text

---

## Image

Full-slide image with optional overlay text.

**Best for**: Impact moments, chapter dividers, inspirational quotes, product hero shots.

```json
{
  "type": "image",
  "title": "我们的使命",
  "subtitle": "让每个人都能轻松创建专业演示",
  "image": {"path": "assets/img/hero.jpg", "alt": "团队协作场景"}
}
```

**Visual**: Image fills entire slide, semi-transparent dark overlay at bottom with text.

---

## Diagram

Flowchart, architecture diagram, or process illustration.

**Best for**: System architecture, workflows, organizational charts, mind maps.

```json
{
  "type": "diagram",
  "title": "系统架构",
  "image": {
    "path": "assets/img/architecture.png",
    "mermaid": "graph TD;\n  A[User]-->B[API Gateway];\n  B-->C[Service];\n  C-->D[Database];"
  }
}
```

**Workflow**: Generate Mermaid syntax → render to PNG (via mermaid.ink or CLI) → insert as diagram slide.

---

## Ending

Closing slide with thank you and Q&A prompt.

**Best for**: Final slide of every presentation.

```json
{
  "type": "ending",
  "title": "谢谢",
  "subtitle": "Q & A"
}
```

**Visual**: Full primary-color background, large centered text, accent bar divider.
