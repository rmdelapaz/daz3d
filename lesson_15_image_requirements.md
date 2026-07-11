# Lesson 5.3 — The Daz to Photoshop Bridge — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_15_daz_to_photoshop_bridge.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §4 "Into Photoshop: The Layer Stack" | `l15_photoshop_layers.png` | Screenshot | The Daz Iray render open in **Photoshop**, with the **Layers** panel showing a non-destructive stack: the **Beauty (render)** layer near the base, the **Depth** and **Specular** passes below it, and finishing/adjustment layers above (Skin Retouch, Dodge &amp; Burn, Depth Haze, Bloom, Colour Grade · Curves, Vignette). Dark Photoshop UI, blend-mode/opacity header visible. | A Photoshop window with the Daz render open, its Layers panel showing the Beauty render at the base beneath render passes and non-destructive adjustment layers for grading, retouch, depth haze, and a vignette |
| 2 | §6 "A Photoshop Workflow" | `l15_before_after_post.png` | Rendered comparison (side-by-side) | The **same render** before and after Photoshop finishing. **Left:** the raw Iray render — flat and slightly cool. **Right:** the finished version — colour-graded warmer, dodged/burned, with a depth-driven glow, atmosphere, and a vignette. Matched crop. | Before and after Photoshop finishing — the raw Iray render on the left looks flat and cool, the finished version on the right is colour-graded warmer with a soft glow, depth atmosphere, and a vignette |

## Notes
- The two Mermaid diagrams (§2 what-crosses-the-bridge map; §6 finishing pipeline) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 1 is a **Photoshop** UI capture (dark theme is standard for Photoshop). Blur or crop out any account name/filename bar.
- Figure 2 reads best when the **only** differences are the grade/retouch/atmosphere — same pose, same render — so the post-processing is unmistakable.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the comparison.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Photoshop layer stack (render + passes + adjustment layers)
- [x] Figure 2 — before &amp; after Photoshop finishing
