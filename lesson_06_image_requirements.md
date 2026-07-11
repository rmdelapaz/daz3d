# Lesson 2.3 — Materials &amp; Iray Surfaces — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_06_materials_and_iray_surfaces.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §2 "The Surfaces Pane" | `l06_surfaces_pane.png` | Screenshot | The Daz Studio **Surfaces** pane on the **Editor** tab with a Genesis 8 figure selected: the named surface list (Face, Lips, Torso, Eyes, etc.) on the left and the selected surface's property dials (Base Color, Glossy Roughness, Bump, Translucency) on the right. | The Surfaces pane Editor tab with a Genesis figure selected, showing the named surface list and property dials |
| 2 | §6 "Eyes & Hair Surfaces" | `l06_eyes_hair_before_after.png` | Rendered comparison (side-by-side) | Close-up of a character's eye and hair. **Left:** dull, flat eyes and blocky card hair with broken/opaque transparency. **Right:** the same eye rendered glossy and wet with a catchlight, and hair with a correctly applied cutout-opacity map reading as strands. Iray renders, matched crop and lighting. | Eyes and hair before and after correct Iray surfaces — flat eyes and blocky hair on the left, glossy catchlit eyes and transparent strand hair on the right |

## Notes
- Both Mermaid diagrams (§1 figure-surfaces map; §4 surfacing workflow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 is best as an **Iray render** (not a viewport grab) so SSS, catchlights, and cutout transparency show correctly.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the render.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Surfaces pane (Editor tab)
- [x] Figure 2 — eyes &amp; hair before &amp; after Iray surfacing
