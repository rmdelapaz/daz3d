# Lesson 4.1 — dForce Cloth & Hair Simulation — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_10_dforce_cloth_and_hair.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §4 "Simulation Settings" | `l10_simulation_settings.png` | Screenshot | The Daz Studio **Simulation Settings** pane showing the **Simulate** button, **Frames to Simulate** (current frame vs animated), and quality options like **Subframes** and **Stabilization Time**. Optionally show a garment's **dForce surface properties** (Dynamic Strength, Bend/Stretch Stiffness) on the Surfaces pane beside it. | The Simulation Settings pane showing the Simulate button, frames-to-simulate, and quality options with a garment's dForce surface properties |
| 2 | §7 "A Reliable Workflow" | `l10_drape_before_after.png` | Rendered/viewport comparison (two-up) | The **same posed figure** in a dress or robe, **before vs after** a dForce drape: **left** — the skirt sticks out stiffly and intersects the legs (no simulation); **right** — the fabric falls naturally with gravity-driven folds, pooling, and clean collision. Matched camera and pose. | The same dress before and after a dForce drape — stiff and intersecting versus naturally draped with clean collision |

## Notes
- Both Mermaid diagrams (§1 dForce content map; §6 explosion-vs-pokethrough fix flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 reads best with an **obvious** difference — pick a flowing garment (long dress, robe, cape) where draping visibly changes the silhouette, so the before/after contrast is unmistakable.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the render comparison.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Simulation Settings pane (+ dForce surface properties)
- [x] Figure 2 — garment before vs after a dForce drape
