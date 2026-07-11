# Lesson 5.1 — The Daz to Blender Bridge — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_12_daz_to_blender_bridge.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §3 "Exporting a Figure" | `l12_bridge_export_dialog.png` | Screenshot | The Daz Studio **Daz to Blender Bridge** export dialog, launched from **File → Send To → Daz to Blender**, showing the **asset name** field, checkboxes/options for **morphs** and **animation**, and the **Send/Accept** button. | The Daz to Blender Bridge export dialog showing the asset name field, morph and animation options, and the send button |
| 2 | §7 "A Bridge Workflow" | `l12_daz_vs_blender.png` | Comparison (two-up) | The **same Genesis figure** side by side: **left** — rendered in **Daz Studio** with Iray; **right** — the same figure imported into **Blender**, shown in the viewport with its **armature** visible and materials applied (ideally a Cycles preview). Matched pose and framing to show a faithful transfer. | The same Genesis figure in Daz Studio with Iray on the left and imported into Blender with its armature and materials on the right |

## Notes
- Both Mermaid diagrams (§1 what-the-bridge-transfers map; §7 prepare→send→fix→render flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 reads best when the Blender side clearly shows the **armature** (enter pose mode or enable "In Front") so viewers see the rig came across, not just the mesh.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the comparison.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Daz to Blender export dialog
- [x] Figure 2 — same figure in Daz vs Blender after bridging
