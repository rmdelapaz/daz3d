# Lesson 1.1 — Welcome to Daz Studio — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_01_welcome_to_daz_studio.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §1 "What Is Daz Studio?" | `l01_daz_interface_overview.png` | Screenshot | Clean Daz Studio window with a single Genesis 8/9 figure in the viewport, default layout, Content Library + Scene + Parameters panes visible. Light UI theme preferred for print. | Daz Studio interface with a Genesis figure in the viewport and the main panes visible |
| 2 | §3 "Genesis: The Heart of Daz" | `l01_genesis_anatomy.png` (or SVG) | Diagram | Labeled diagram of a Genesis figure calling out its four built-in parts: rig/skeleton, morphs, surfaces & UVs, auto-fit compatibility. Could be an annotated screenshot or a clean vector diagram. | Diagram of a Genesis figure showing its rig, morphs, surfaces, and auto-fit compatibility |

## Notes
- The pipeline diagram in §4 (Daz → Render / Blender / Unreal) is a **live Mermaid diagram** already in the page — no image needed. It re-themes automatically in dark mode.
- Prefer 16:9 or 4:3 screenshots at ~1600px wide; PNG for UI, JPG only if photographic.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).
- If producing the §3 diagram as SVG, use `currentColor`/CSS-variable-friendly strokes so it works in both light and dark themes (course convention: `svgDarkModeSupport`).

## Status
- [x] Figure 1 — interface overview
- [x] Figure 2 — Genesis anatomy diagram
