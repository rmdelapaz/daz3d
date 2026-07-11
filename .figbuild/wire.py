# -*- coding: utf-8 -*-
"""Wire rendered figures into the lesson HTML: replace each .image-placeholder
div (in document order) with an <img>, and strip the '(… see <code>…</code>)'
note from figcaptions. Asserts the placeholder count per file first."""
import os, re, sys

ROOT = "/home/practicalace/projects/daz3d"

# lesson html -> ordered [(image file, alt text), ...] from the requirements files
M = {
 "lesson_01_welcome_to_daz_studio.html": [
  ("l01_daz_interface_overview.png", "Daz Studio interface with a Genesis figure in the viewport and the main panes visible"),
  ("l01_genesis_anatomy.png", "Diagram of a Genesis figure showing its rig, morphs, surfaces, and auto-fit compatibility"),
 ],
 "lesson_02_installing_and_content_library.html": [
  ("l02_app_vs_content.png", "The Daz Studio application and the content library shown as two separate things connected by an arrow"),
  ("l02_dim_ready_to_download.png", "Daz Install Manager showing the Ready to Download tab with Daz Studio and Starter Essentials checked"),
  ("l02_smart_vs_library.png", "Smart Content pane filtered to a Genesis 8 figure beside the Content Library pane showing its folder tree"),
 ],
 "lesson_03_the_daz_studio_interface.html": [
  ("l03_workspace_regions.png", "Annotated Daz Studio interface with the viewport, content panes, Scene pane, and Parameters pane each labeled"),
  ("l03_viewport_controls.png", "Close-up of the viewport corners showing the view selector, DrawStyle control, and navigation icons"),
  ("l03_scene_pane.png", "The Scene pane tree with a Genesis figure expanded to show its bone hierarchy"),
  ("l03_workspace_menu.png", "The Window to Workspace menu open, showing Select Layout and Save Layout As with the built-in layout list"),
 ],
 "lesson_04_loading_and_posing_figures.html": [
  ("l04_default_apose.png", "A freshly loaded Genesis 8 figure standing in its default neutral A-pose"),
  ("l04_activepose_powerpose.png", "ActivePose dragging a figure's hand beside the PowerPose puppet control map"),
 ],
 "lesson_05_shaping_characters_with_morphs.html": [
  ("l05_shaping_pane.png", "The Shaping pane with a Genesis figure selected, showing Actor, Head, and Body groups and their morph dials"),
  ("l05_face_before_after.png", "Before-and-after of a Genesis figure's face - default base head on the left, custom head morphs applied on the right"),
 ],
 "lesson_06_materials_and_iray_surfaces.html": [
  ("l06_surfaces_pane.png", "The Surfaces pane Editor tab with a Genesis figure selected, showing the named surface list and property dials"),
  ("l06_eyes_hair_before_after.png", "Eyes and hair before and after correct Iray surfaces - flat eyes and blocky hair on the left, glossy catchlit eyes and transparent strand hair on the right"),
 ],
 "lesson_07_building_a_scene.html": [
  ("l07_scene_pane_hierarchy.png", "The Scene pane hierarchy with fitted hair and clothing nested under the figure and a prop parented to the hand bone"),
  ("l07_headlamp_vs_light.png", "Headlamp lighting versus a directional scene light - flat and shadowless on the left, showing form and depth on the right"),
 ],
 "lesson_08_lighting_for_iray.html": [
  ("l08_emissive_surface.png", "The Surfaces Editor showing a plane's Emission Color and Luminance set to turn it into a mesh light"),
  ("l08_lighting_comparison.png", "The same portrait under flat light, an HDRI dome, and a three-point setup, showing how lighting changes mood and depth"),
 ],
 "lesson_09_rendering_with_iray.html": [
  ("l09_render_settings.png", "The Render Settings pane, Progressive Rendering tab, showing Max Samples, Max Time, and Rendering Quality with the Iray engine selected"),
  ("l09_denoise_comparison.png", "The same portrait at three stages - noisy low-sample render, denoised version, and final graded image"),
 ],
 "lesson_10_dforce_cloth_and_hair.html": [
  ("l10_simulation_settings.png", "The Simulation Settings pane showing the Simulate button, frames-to-simulate, and quality options with a garment's dForce surface properties"),
  ("l10_drape_before_after.png", "The same dress before and after a dForce drape - stiff and intersecting versus naturally draped with clean collision"),
 ],
 "lesson_11_animation_basics_timeline.html": [
  ("l11_timeline_pane.png", "The Timeline pane showing the frame ruler, playhead, keyframe markers on a figure, current-frame and total-frames fields, and playback controls"),
  ("l11_turntable_filmstrip.png", "A filmstrip of turntable frames showing a character rotating from front to side to back as a rendered image sequence"),
 ],
 "lesson_12_daz_to_blender_bridge.html": [
  ("l12_bridge_export_dialog.png", "The Daz to Blender Bridge export dialog showing the asset name field, morph and animation options, and the send button"),
  ("l12_daz_vs_blender.png", "The same Genesis figure in Daz Studio with Iray on the left and imported into Blender with its armature and materials on the right"),
 ],
 "lesson_13_daz_to_unreal_bridge.html": [
  ("l13_unreal_export_dialog.png", "The Daz to Unreal export dialog showing the asset name, Asset Type set to Skeletal Mesh, morph options, and the port setting"),
  ("l13_figure_in_unreal_level.png", "A bridged Daz character standing in an Unreal Engine level, lit in real time, with the Skeletal Mesh and materials visible in the Content Browser"),
 ],
 "lesson_14_capstone_full_pipeline.html": [
  ("l14_daz_hero_render.png", "A finished Iray hero render of the capstone character in Daz - posed, lit, denoised, and framed as a portfolio portrait"),
  ("l14_pipeline_triptych.png", "A triptych of the same capstone character in Daz, Blender, and Unreal, each panel labeled, showing one asset across three tools"),
 ],
}

ph_re = re.compile(r'<div class="image-placeholder[^"]*"[^>]*>.*?</div>', re.DOTALL)
# strip "(… see <code>…</code> …)" note from figcaptions (robust to wording)
note_re = re.compile(r'\s*\([^)]*see\s*<code>[^)]*</code>[^)]*\)')

def esc(s):  # minimal attribute escaping for alt text
    return s.replace("&", "&amp;").replace('"', "&quot;")

total = 0
for fname, imgs in M.items():
    path = os.path.join(ROOT, fname)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    found = ph_re.findall(html)
    if len(found) != len(imgs):
        print("!! %s: found %d placeholders, expected %d - SKIPPED" % (fname, len(found), len(imgs)))
        continue
    it = iter(imgs)
    def repl(m):
        img, alt = next(it)
        return '<img src="images/%s" alt="%s">' % (img, esc(alt))
    html2 = ph_re.sub(repl, html)
    notes = len(note_re.findall(html2))
    html2 = note_re.sub("", html2)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html2)
    total += len(imgs)
    print("ok %-46s %d imgs, %d caption notes stripped" % (fname, len(imgs), notes))
print("TOTAL images wired:", total)
