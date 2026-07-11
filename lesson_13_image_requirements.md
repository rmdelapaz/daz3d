# Lesson 5.2 — The Daz to Unreal Bridge — Image Requirements

Art/screenshots needed to replace the `.image-placeholder` blocks in `lesson_13_daz_to_unreal_bridge.html`. Save finished files to `images/` and swap each placeholder `<div class="image-placeholder">…</div>` for an `<img src="images/FILENAME" alt="…">`.

| # | Placeholder location (section) | Suggested filename | Type | Description | Alt text |
|---|-------------------------------|--------------------|------|-------------|----------|
| 1 | §3 "Exporting to Unreal" | `l13_unreal_export_dialog.png` | Screenshot | The Daz Studio **Daz to Unreal** export dialog, launched from **File → Send To → Daz to Unreal**, showing the **asset name** field, the **Asset Type** dropdown set to **Skeletal Mesh**, morph/subdivision options, and the **port** setting. | The Daz to Unreal export dialog showing the asset name, Asset Type set to Skeletal Mesh, morph options, and the port setting |
| 2 | §7 "An Unreal Workflow" | `l13_figure_in_unreal_level.png` | Screenshot / real-time render | The bridged **Daz Genesis character standing in an Unreal Engine level**, lit in real time, with the **editor viewport** and ideally the **Content Browser** showing the imported **Skeletal Mesh**, skeleton, and **Material Instances**. Show the character clearly staged in a scene. | A bridged Daz character standing in an Unreal Engine level, lit in real time, with the Skeletal Mesh and materials visible in the Content Browser |

## Notes
- Both Mermaid diagrams (§1 what-transfers-to-UE map; §6 install→send→retarget→material→animate flow) are **live Mermaid** already in the page — no image needed. They re-theme automatically in dark mode.
- Figure 2 sells the "real-time" payoff — capture it in the **Unreal editor** with a lit level, not an isolated mesh preview, so the game-engine context is obvious.
- Prefer 16:9 or 4:3 at ~1600px wide; PNG for the UI screenshot. Figure 2 can be a wide editor capture.
- A **light UI theme** reads better in print for Figure 1. Blur or crop out any account email/username.
- Keep alt text descriptive for accessibility (WCAG AA — matches course standard).

## Status
- [x] Figure 1 — Daz to Unreal export dialog (Asset Type: Skeletal Mesh)
- [x] Figure 2 — bridged figure staged in an Unreal level
