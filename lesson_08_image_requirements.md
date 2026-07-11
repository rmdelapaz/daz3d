# Lesson 3.2 — Lighting for Iray — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_08_lighting_for_iray.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §4 "Emissive Surfaces" | `l08_emissive_surface.png` | Screenshot | The Daz Studio **Surfaces** pane (Editor tab) with a primitive **plane** selected, showing the Iray Uber **Emission** group: **Emission Color** set to a warm white (not black) and a **Luminance** value entered, turning the plane into a mesh light. Optionally show the glowing plane in the viewport behind. | The Surfaces Editor showing a plane's Emission Color and Luminance set to turn it into a mesh light |
| 2 | §7 "Choosing an Approach" | `l08_lighting_comparison.png` | Rendered comparison (three-up) | The **same character portrait** rendered three ways, side by side: **(1)** flat single light — dull and shadowless; **(2)** an **HDRI dome** — realistic directional ambient; **(3)** a full **three-point rig** — visible key, fill, and rim separating the subject. Iray renders, matched crop and pose. | The same portrait under flat light, an HDRI dome, and a three-point setup, showing how lighting changes mood and depth |

## Notes
- Both Mermaid diagrams (§1 four-ways-to-light map; §5 three-point build flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 is best as **Iray renders** (not viewport grabs) so shadow softness, rim separation, and dome realism read correctly. Keep all three panels at the same exposure baseline so the comparison is about lighting, not brightness.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the renders.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — emissive surface (Emission Color + Luminance) in the Surfaces Editor
- [x] Figure 2 — flat vs HDRI dome vs three-point lighting comparison
