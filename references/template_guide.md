# Template Guide — PPT Generator

How to work with user-provided .pptx templates.

---

## When Template Mode Activates

Template mode activates when:
1. The user says "用我的模板" / "use my template" / "我有现成的模板"
2. The user provides a .pptx file path in Step 1
3. The user asks to follow corporate branding / 企业VI

---

## Template Analysis (do this first)

Before filling a template, read its structure:

```bash
python -c "
from pptx import Presentation
prs = Presentation('path/to/template.pptx')
print(f'Slide width: {prs.slide_width}')
print(f'Slide height: {prs.slide_height}')
print(f'Slide layouts: {len(prs.slide_layouts)}')
for i, layout in enumerate(prs.slide_layouts):
    print(f'  Layout {i}: {layout.name}')
    for ph in layout.placeholders:
        print(f'    Placeholder {ph.placeholder_format.idx}: {ph.name} ({ph.placeholder_format.type})')
print(f'Slides: {len(prs.slides)}')
"
```

This tells you:
- What slide layouts are available (e.g., "Title Slide", "Title and Content", "Section Header")
- What placeholders each layout has (title, body, image, etc.)
- The exact dimensions of the template

---

## Filling Strategy

### 1. Match your slide types to template layouts

| Your Slide Type | Look for Template Layout Named |
|----------------|-------------------------------|
| cover | "Title Slide", "Cover", "封面" |
| toc | "Section Header", "Agenda" |
| content | "Title and Content", "内容页", "Blank" |
| chart | "Title and Content" (add chart manually) |
| ending | "Section Header", "Closing", "结尾" |

If no matching layout is found, use the first available layout.

### 2. Fill placeholders, don't add new text boxes

When working with a template, the script (`generate_pptx.py`) will:
- Look for placeholder shapes in the chosen layout
- Fill `title` placeholders with slide titles
- Fill `body` placeholders with slide body content
- Add images, charts, and tables as new shapes positioned near existing content

### 3. Respect existing styling

The template's fonts, colors, and formatting are preserved. Don't override them unless the user explicitly asks for style changes. The design preset from the scenario is IGNORED in template mode — the template IS the design.

---

## Common Template Issues & Solutions

| Issue | Solution |
|-------|----------|
| Template has only 1 layout | Use it for all slides; manually adjust positioning per slide |
| Placeholder names are in Chinese | The script matches by index order as fallback |
| Template has no blank layout | Use the most minimal layout available |
| Fonts in template don't support Chinese | Warn the user; recommend font replacement in PowerPoint |
| Template uses custom slide sizes | The script reads dimensions from the template automatically |

---

## Best Practices

1. **Analyze before filling**: Always run the analysis command first to understand what you're working with.
2. **Preserve branding**: Don't change colors, fonts, or logo positions unless asked.
3. **Test with one slide first**: Generate a single slide, verify it looks right, then generate the rest.
4. **Warn about limitations**: If the template doesn't have enough layouts for your slide types, tell the user before generating.
5. **Keep a copy**: Never modify the original template file. Work on a copy.
