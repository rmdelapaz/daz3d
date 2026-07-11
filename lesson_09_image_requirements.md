# Lesson 3.3 — Rendering with Iray — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_09_rendering_with_iray.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §2 "The Render Settings Pane" | `l09_render_settings.png` | Screenshot | The Daz Studio **Render Settings** pane with the **Progressive Rendering** tab open, showing **Max Samples**, **Max Time**, and **Rendering Quality** fields. Ideally also show the **General** tab's engine dropdown set to **Iray** and the Pixel Size fields. | The Render Settings pane, Progressive Rendering tab, showing Max Samples, Max Time, and Rendering Quality with the Iray engine selected |
| 2 | §7 "Saving & Post-Processing" | `l09_denoise_comparison.png` | Rendered comparison (three-up) | The **same Iray portrait** at three stages, side by side: **(1)** a **noisy low-sample** pass — visibly grainy; **(2)** the **denoised** version — grain cleared, detail intact; **(3)** the **final saved image** after a light post-processing grade (gentle contrast/saturation, subtle vignette). Matched crop and exposure. | The same portrait at three stages — noisy low-sample render, denoised version, and final graded image |

## Notes
- Both Mermaid diagrams (§1 render pipeline map; §5 iterate-then-final-render flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 is best made from **one real render**: save an early low-sample frame for panel 1, the denoised full render for panel 2, and a lightly graded export for panel 3 — so the only differences are noise and the grade, not the pose or lighting.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot, PNG/high-quality JPG for the renders.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Render Settings pane (Progressive Rendering tab)
- [x] Figure 2 — noisy vs denoised vs final graded render comparison
