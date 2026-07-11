# Lesson 1.2 — Installing Daz &amp; the Content Library — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_02_installing_and_content_library.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §1 "App vs Content: The Big Idea" | `l02_app_vs_content.png` (or SVG) | Diagram | Two labeled boxes — the Daz Studio **application** on one side, the **content library** folders on the other — joined by an arrow reading "the app reads content from the library." Reinforces that they're installed separately. | The Daz Studio application and the content library shown as two separate things connected by an arrow |
| 2 | §3 "Installing Daz Studio" | `l02_dim_ready_to_download.png` | Screenshot | Daz Install Manager on the **Ready to Download** tab, with Daz Studio and Genesis 8 Starter Essentials checked. Show the tab strip (Ready to Download / Ready to Install / Installed). | Daz Install Manager showing the Ready to Download tab with Daz Studio and Starter Essentials checked |
| 3 | §5 "Smart Content vs Content Library" | `l02_smart_vs_library.png` | Screenshot | Side-by-side: the **Smart Content** pane filtered to a selected Genesis 8 figure, next to the **Content Library** pane showing the folder tree (DAZ Studio Formats → My DAZ 3D Library → People → Genesis 8). | Smart Content pane filtered to a Genesis 8 figure beside the Content Library pane showing its folder tree |

## Notes
- The two Mermaid diagrams (§2 install-method map, §3 install arc) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Prefer 16:9 or 4:3 screenshots at ~1600px wide; PNG for UI, JPG only if photographic.
- For the DIM and pane screenshots, a **light UI theme** reads better in print. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).
- If producing the §1 diagram as SVG, use `currentColor`/CSS-variable-friendly strokes so it works in both light and dark themes (course convention: `svgDarkModeSupport`).

## Status
- [x] Figure 1 — app vs content diagram
- [x] Figure 2 — DIM Ready to Download
- [x] Figure 3 — Smart Content vs Content Library
