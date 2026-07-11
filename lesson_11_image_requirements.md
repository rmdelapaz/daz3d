# Lesson 4.2 — Animation Basics with the Timeline — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_11_animation_basics_timeline.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §3 "The Timeline Pane" | `l11_timeline_pane.png` | Screenshot | The Daz Studio **Timeline** pane showing the **frame ruler**, the **playhead/scrubber**, **keyframe markers** on a selected figure, the **current-frame** and **total-frames** fields, and the playback controls. A figure selected in the Scene so the keys are visible. | The Timeline pane showing the frame ruler, playhead, keyframe markers on a figure, current-frame and total-frames fields, and playback controls |
| 2 | §7 "An Animation Workflow" | `l11_turntable_filmstrip.png` | Rendered filmstrip (multi-frame) | A **filmstrip** of several frames from a character **turntable** in sequence — the figure rotating front → side → back → side — illustrating an image sequence rendered frame by frame before encoding to video. Evenly spaced angles, matched lighting and crop. | A filmstrip of turntable frames showing a character rotating from front to side to back as a rendered image sequence |

## Notes
- Both Mermaid diagrams (§1 ways-to-animate map; §6 plan→animate→render→encode pipeline) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 works best as **4–6 evenly spaced angles** (e.g. 0°, 72°, 144°, 216°, 288°) so the rotation reads clearly across the strip. Use the actual turntable render if available.
- Prefer 16:9 or 4:3 at ~1600px wide for Figure 1; a wide strip (e.g. 1600×400) suits Figure 2.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Timeline pane with keyframes on a selected figure
- [x] Figure 2 — turntable image-sequence filmstrip
