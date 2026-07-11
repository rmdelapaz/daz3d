# Lesson 3.1 — Building a Scene — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_07_building_a_scene.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §4 "Hair &amp; Clothing" | `l07_scene_pane_hierarchy.png` | Screenshot | The Daz Studio **Scene** pane showing a dressed Genesis figure: the figure node expanded with **fitted hair** and an **outfit** nested as child (conforming) nodes beneath it, and a separate **held prop** parented to a hand bone. Make the parent/child indentation clearly visible. | The Scene pane hierarchy with fitted hair and clothing nested under the figure and a prop parented to the hand bone |
| 2 | §7 "Headlamp vs Scene Lights" | `l07_headlamp_vs_light.png` | Rendered comparison (side-by-side) | The **same character** rendered twice. **Left:** lit only by the flat frontal **headlamp** — no shadows, no form, characterless. **Right:** lit by a single **directional scene light** showing shadows, form, and depth. Iray renders, matched crop and pose. | Headlamp lighting versus a directional scene light — flat and shadowless on the left, showing form and depth on the right |

## Notes
- Both Mermaid diagrams (§1 scene-contents map; §6 camera/composition flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 is best as an **Iray render** (not a viewport grab) so the difference between flat headlamp light and directional shadows shows correctly.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the render.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Scene pane hierarchy with fitted hair/clothing and a parented prop
- [x] Figure 2 — headlamp vs directional scene light comparison
