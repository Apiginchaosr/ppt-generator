# PPT Generator (Fusion Edition)

> 你的下一个 PPT，何必自己动手。

[English](#english) | [中文](#chinese)

---

## English

A Claude Code skill for generating professional PowerPoint (.pptx) presentations through interactive guided conversation.

### What It Does

1. **Guided Conversation** — Asks the right questions (audience, style, length, image preference…) instead of guessing
2. **Content Generation** — Drafts outlines and slide content; user reviews and tweaks
3. **Dual-Channel Image Sourcing** — Web search for real photos, AI generation for styled visuals. Image style selectable (realistic / anime / business / minimalist)
4. **Design Auto-Selection** — Picks colors, fonts, and layout density based on scenario (business / academic / tech / creative)
5. **Dual-Engine PPTX Generation**:
   - **Mode B (default)**: HTML-to-PPTX via PptxGenJS — produces native editable shapes and textboxes with rich visuals
   - **Mode A (fallback)**: python-pptx — for template-based or quick generation
6. **Typography Quality Check** — Auto-scans for text overflow, font inconsistencies, contrast issues, and overlaps
7. **Iterative Refinement** — Accepts feedback and re-generates until satisfied

### Fusion Credits

This skill integrates the **html2pptx** rendering engine from [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) by **@tfriedel**, combined with the original ppt-generator pipeline (guided conversation, image search, quality check). The two skills work side-by-side — ppt-generator handles the creative direction and media sourcing, while claude-office-skills provides the high-fidelity PPTX rendering via PptxGenJS.

### Installation

```bash
# 1. Clone this skill
git clone https://github.com/Apiginchaosr/ppt-generator ~/.claude/skills/ppt-generator

# 2. Install the rendering engine dependency
git clone https://github.com/tfriedel/claude-office-skills ~/.claude/skills/claude-office-skills
cd ~/.claude/skills/claude-office-skills && npm install

# 3. Restart Claude Code or run /reload-skills
```

### Quick Start

Just talk to Claude naturally:

- "帮我做一个Q2销售汇报PPT，给老板看的"
- "Make me a pitch deck about our AI startup"
- "准备一个课堂演讲，主题是原神出海"

The skill triggers automatically when you mention PPT, slides, presentation, 演示文稿, etc.

---

## 中文

一个通过交互式引导对话自动生成专业 PowerPoint (.pptx) 演示文稿的 Claude Code 技能。

### 功能

1. **渐进式引导对话** — 主动询问关键信息（受众、风格、页数、图片偏好等），不瞎猜
2. **内容生成** — AI 起草大纲和每页内容，用户确认修改
3. **双通道图片采源** — 搜索引擎找实拍图 + AI 生成风格化配图。图片风格可选（写实 / 二次元 / 商务 / 极简）
4. **场景自适应设计** — 根据场景（商业 / 教学 / 技术 / 创意）自动匹配配色、字体、装饰密度
5. **双引擎 PPTX 生成**：
   - **Mode B（默认）**：HTML → PptxGenJS 渲染 → 原生可编辑形状和文本框，视觉效果丰富
   - **Mode A（兜底）**：python-pptx —— 模板填充或快速模式
6. **排版质量检查** — 自动扫描文字溢出、字号不一致、对比度、元素重叠
7. **迭代优化** — 接受反馈，修改后重新生成

### 融合说明

本技能融合了 **@tfriedel** 开发的 [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills) 中的 **html2pptx** 渲染引擎，与原始 ppt-generator 管线（引导对话、图片搜索、质量检查）整合。两个技能协同工作——ppt-generator 负责创意方向和素材采源，claude-office-skills 通过 PptxGenJS 提供高保真 PPTX 渲染。

### 安装

```bash
# 1. 克隆本技能
git clone https://github.com/Apiginchaosr/ppt-generator ~/.claude/skills/ppt-generator

# 2. 安装渲染引擎依赖
git clone https://github.com/tfriedel/claude-office-skills ~/.claude/skills/claude-office-skills
cd ~/.claude/skills/claude-office-skills && npm install

# 3. 重启 Claude Code 或运行 /reload-skills
```

### 快速开始

直接用大白话说：

- "帮我做一个Q2销售汇报PPT，给老板看的"
- "准备一个课堂演讲，主题是原神出海"
- "Make me a tech talk about AI agents, dark theme"

提到 PPT、演示文稿、slides、presentation 等关键词时自动触发。

---

## Version History

| Version | Commit | Description |
|---------|--------|-------------|
| **v2** | `59a5f4d` | Fusion Edition — integrated tfriedel/claude-office-skills html2pptx engine |
| **v1** | `628df00` | Initial release — python-pptx based, 7-step pipeline |

[View all versions on GitHub](https://github.com/Apiginchaosr/ppt-generator/commits/master)
