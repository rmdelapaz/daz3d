# -*- coding: utf-8 -*-
"""Generate every course figure as HTML into .figbuild/html/, then render.py
rasterizes to PNG. All figures carry a stand-in badge."""
import os
from figkit import *

HTML = os.path.join(os.path.dirname(__file__), "html")
os.makedirs(HTML, exist_ok=True)
FIGURES = {}
def fig(name, w, h, inner, bg="#ffffff"):
    FIGURES[name] = html_doc(inner, w, h, bg=bg)

# ------------------------------------------------------------------ helpers
def two_col(left, right, lw="42%"):
    return ("<div style='display:flex;height:100%%'>"
            "<div style='width:%s;border-right:1px solid #cdd0d6;overflow:hidden'>%s</div>"
            "<div style='flex:1;overflow:hidden'>%s</div></div>") % (lw, left, right)

def cbrow(label, checked=True, sub=None, ver=None, size=None):
    box = ("<span style='width:15px;height:15px;border:1px solid #8a8f98;border-radius:3px;"
           "background:%s;display:inline-flex;align-items:center;justify-content:center;"
           "color:#fff;font-size:11px;flex:none'>%s</span>") % (
           ("#2f6fb2" if checked else "#fff"), ("&#10003;" if checked else ""))
    right = ""
    if ver:  right += "<span style='color:#7b808a;font-size:11px;margin-left:auto'>%s</span>" % ver
    if size: right += "<span style='color:#7b808a;font-size:11px;width:64px;text-align:right'>%s</span>" % size
    subhtml = "<div style='font-size:10.5px;color:#8b909a;margin-left:23px'>%s</div>" % sub if sub else ""
    return ("<div style='display:flex;align-items:center;gap:8px;padding:6px 12px;"
            "border-bottom:1px solid #e6e8eb;font-size:12.5px;color:#2c3038'>%s<span>%s</span>%s</div>%s"
            ) % (box, label, right, subhtml)

def ifield(label, value, w="160px"):
    return ("<div class='prow' style='padding:7px 16px'><span class='pname'>%s</span><span style='flex:1'></span>"
            "<span class='field' style='flex:none;width:%s'>%s</span></div>") % (label, w, value)

def idrop(label, value, w="180px"):
    return ("<div class='prow' style='padding:7px 16px'><span class='pname'>%s</span><span style='flex:1'></span>"
            "<span class='field' style='flex:none;width:%s;display:flex;justify-content:space-between'>"
            "<span>%s</span><span style='color:#7b808a'>&#9662;</span></span></div>") % (label, w, value)

def icheck(label, checked=True):
    box = ("<span style='width:14px;height:14px;border:1px solid #8a8f98;border-radius:3px;"
           "background:%s;display:inline-flex;align-items:center;justify-content:center;"
           "color:#fff;font-size:10px'>%s</span>") % (("#2f6fb2" if checked else "#fff"),
           ("&#10003;" if checked else ""))
    return ("<div style='display:flex;align-items:center;gap:8px;padding:5px 10px;font-size:12.5px;color:#2c3038'>"
            "%s<span>%s</span></div>") % (box, label)

def dialog(title, body, w=400, sub=None):
    subhtml = "<div style='font-size:11.5px;color:#6b7079;padding:0 16px 8px'>%s</div>" % sub if sub else ""
    return ("<div style='position:absolute;inset:0;background:rgba(30,33,38,.34)'></div>"
            "<div style='position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);width:%dpx;"
            "background:#eceef1;border:1px solid #9297a1;border-radius:7px;box-shadow:0 14px 40px rgba(0,0,0,.4);overflow:hidden'>"
            "<div style='padding:11px 16px;font-size:14px;font-weight:600;color:#20232a;"
            "background:linear-gradient(#e0e3e7,#d0d3d9);border-bottom:1px solid #b3b7bf'>%s</div>%s"
            "<div style='padding:12px 6px'>%s</div></div>") % (w, title, subhtml, body)

def studio_cell(fig_svg, label=None, tag=None):
    return rcell(fig_svg, label=label, tag=tag)

# =================================================================== L01
def build_window(center_svg, overlay=""):
    scene = tree([
        dict(depth=0, toggle="open", icon="figure", label="Genesis 8 Female", sel=True, eye=True),
        dict(depth=1, toggle="close", icon="bone", label="hip"),
        dict(depth=1, icon="node", label="Genesis 8 Female Eyes"),
        dict(depth=0, icon="camera", label="Perspective View"),
    ])
    params = (group_header("Pose Controls") + prow_slider("Bend", 0.55, "12.0") +
              prow_slider("Twist", 0.5, "0.0") + group_header("General") + prow_slider("Scale", 0.6, "100%"))
    left = pane("Content Library", tree([
        dict(depth=0, toggle="open", icon="folder", label="DAZ Studio Formats"),
        dict(depth=1, toggle="open", icon="folder", label="My DAZ 3D Library"),
        dict(depth=2, toggle="open", icon="folder", label="People"),
        dict(depth=3, icon="figure", label="Genesis 8 Female", sel=True),
        dict(depth=3, icon="figure", label="Genesis 8 Male"),
    ]), style="height:100%")
    right = ("<div class='col' style='height:100%'>" + pane("Scene", scene, style="flex:1")
             + pane("Parameters", params, style="flex:1") + "</div>")
    win = ("<div class='win'>"
           "<div class='menubar'><b>Daz Studio</b><span>File</span><span>Edit</span><span>Create</span>"
           "<span>Tools</span><span>Render</span><span>Window</span><span>Help</span></div>"
           "<div class='toolbar'><span class='tbtn'>&#9776;</span><span class='tbtn'>&#128190;</span>"
           "<span class='tbtn'>&#8635;</span><span class='tbtn'>&#128260;</span>"
           "<span style='flex:1'></span><span class='tbtn'>&#127909;</span></div>"
           "<div class='workspace'>"
           "<div style='width:24%'>" + left + "</div>"
           "<div style='flex:1'>" + viewport(center_svg, style="height:100%") + "</div>"
           "<div style='width:26%'>" + right + "</div>"
           "</div></div>")
    return win + overlay

fig("l01_daz_interface_overview", 900, 560, build_window(bust("hdri", w=400, h=520)))

def card(x, y, title, sub, w=200):
    return ("<g><rect x='%d' y='%d' width='%d' height='58' rx='8' fill='#eef4fb' stroke='#2f6fb2' stroke-width='1.6'/>"
            "<text x='%d' y='%d' font-size='16' font-weight='700' fill='#12314f'>%s</text>"
            "<text x='%d' y='%d' font-size='12.5' fill='#3d5670'>%s</text></g>") % (
        x, y, w, x+14, y+25, title, x+14, y+44, sub)
anatomy = ("<svg class='diagram' viewBox='0 0 900 560'><rect width='900' height='560' fill='#fbfcfd'/>"
    "<text x='34' y='42' font-size='19' font-weight='700' fill='#20232a'>Genesis: one figure, four built-in systems</text>"
    "<g transform='translate(390,150)'><ellipse cx='60' cy='300' rx='70' ry='16' fill='#000' opacity='.10'/>"
    "<circle cx='60' cy='40' r='30' fill='#c9b7a3'/>"
    "<path d='M32 74 Q60 64 88 74 L92 190 Q92 235 78 250 L42 250 Q28 235 28 190 Z' fill='#c9b7a3'/>"
    "<path d='M34 96 L4 190 M86 96 L116 190' stroke='#c9b7a3' stroke-width='22' fill='none' stroke-linecap='round'/>"
    "<path d='M50 248 L44 330 M70 248 L76 330' stroke='#c9b7a3' stroke-width='24' fill='none' stroke-linecap='round'/></g>"
    "<g stroke='#2f6fb2' stroke-width='1.4' stroke-dasharray='4 4' opacity='.8'>"
    "<line x1='300' y1='150' x2='430' y2='210'/><line x1='600' y1='150' x2='470' y2='210'/>"
    "<line x1='300' y1='430' x2='430' y2='340'/><line x1='600' y1='430' x2='470' y2='340'/></g>"
    + card(70, 120, "Rig / Skeleton", "shared bones &amp; joints") + card(630, 120, "Morphs", "reshape the same mesh")
    + card(70, 415, "Surfaces &amp; UVs", "materials map identically") + card(630, 415, "Auto-Fit", "clothing &amp; hair conform")
    + "</svg>")
fig("l01_genesis_anatomy", 900, 560, anatomy)

# =================================================================== L02
avc = ("<svg class='diagram' viewBox='0 0 900 520'><rect width='900' height='520' fill='#fbfcfd'/>"
    "<text x='40' y='52' font-size='20' font-weight='700' fill='#20232a'>Two separate installs, one relationship</text>"
    # app box
    "<rect x='70' y='150' width='300' height='240' rx='12' fill='#eef4fb' stroke='#2f6fb2' stroke-width='2'/>"
    "<text x='220' y='190' font-size='17' font-weight='700' fill='#12314f' text-anchor='middle'>Daz Studio</text>"
    "<text x='220' y='214' font-size='13' fill='#3d5670' text-anchor='middle'>the application (the program)</text>"
    "<rect x='120' y='236' width='200' height='120' rx='6' fill='#fff' stroke='#9db6d4'/>"
    "<rect x='120' y='236' width='200' height='24' rx='6' fill='#2f6fb2'/>"
    "<rect x='134' y='276' width='80' height='9' rx='4' fill='#c3d3e8'/><rect x='134' y='296' width='150' height='9' rx='4' fill='#d9e2ee'/>"
    "<rect x='134' y='316' width='120' height='9' rx='4' fill='#d9e2ee'/>"
    # content box
    "<rect x='530' y='150' width='300' height='240' rx='12' fill='#f3f0e6' stroke='#caa64e' stroke-width='2'/>"
    "<text x='680' y='190' font-size='17' font-weight='700' fill='#5a4a1e' text-anchor='middle'>Content Library</text>"
    "<text x='680' y='214' font-size='13' fill='#7a6836' text-anchor='middle'>figures, clothes, poses (the files)</text>"
    "<g transform='translate(560,238)'>"
    "<path d='M4 8 H34 L42 16 H120 V96 H4 Z' fill='#e0be6a' stroke='#b9973f'/>"
    "<path d='M14 26 H150 V104 H14 Z' fill='#eccd7e' stroke='#b9973f'/>"
    "<text x='150' y='60' font-size='12' fill='#7a6836'>/People/Genesis 8/</text></g>"
    # arrow
    "<g><line x1='378' y1='270' x2='520' y2='270' stroke='#39424c' stroke-width='3'/>"
    "<path d='M520 270 l-16 -8 l0 16 Z' fill='#39424c'/></g>"
    "<text x='449' y='256' font-size='12.5' fill='#39424c' text-anchor='middle' font-weight='600'>reads content from</text>"
    "<text x='450' y='430' font-size='13.5' fill='#5b616b' text-anchor='middle'>Install (or update) each one independently &#8212; the app on its own has almost nothing to show.</text>"
    "</svg>")
fig("l02_app_vs_content", 900, 520, avc)

dim_rows = (cbrow("Daz Studio", True, "Application &#183; 64-bit", "4.21", "1.3 GB")
    + cbrow("Genesis 8 Starter Essentials", True, "Base figures, materials, poses", "1.0", "2.1 GB")
    + cbrow("Genesis 8.1 Female", True, "Base female figure", "1.0", "480 MB")
    + cbrow("Default Camera &amp; Light Presets", False, None, "1.0", "24 MB")
    + cbrow("Daz Studio Documentation", False, None, "4.21", "88 MB"))
dim = ("<div class='win' style='background:#d5d8dd'>"
    "<div class='pane-head' style='font-size:13px'>DAZ Install Manager<span class='dots'>&#8212; &#9744; &#10005;</span></div>"
    + strip(["Ready to Download", "Ready to Install", "Installed"], 0)
    + "<div style='background:#f3f4f6;flex:1;overflow:hidden'>"
    "<div class='filterbar'><span>Filter:</span><span class='field'>All products</span>"
    "<span style='margin-left:auto;color:#5b606a'>5 packages &#183; 2 selected</span></div>"
    + dim_rows + "</div>"
    "<div style='display:flex;align-items:center;gap:10px;padding:9px 12px;background:#e4e6ea;border-top:1px solid #b3b7bf'>"
    + btn("Start Queue", True) + btn("Account Settings")
    + "<span style='margin-left:auto;color:#5b606a;font-size:12px'>3.4 GB queued</span></div></div>")
fig("l02_dim_ready_to_download", 880, 520, dim)

def thumbgrid(title, items):
    tiles = ""
    for name, ic in items:
        tiles += ("<div style='width:96px'><div style='height:74px;border-radius:6px;border:1px solid #c3c7cf;"
                  "background:linear-gradient(#f7f8fa,#e3e6ea);display:flex;align-items:center;justify-content:center'>"
                  "<div style='width:34px;height:34px'>%s</div></div>"
                  "<div style='font-size:10.5px;color:#40454d;text-align:center;margin-top:4px'>%s</div></div>"
                  ) % (ic, name)
    return "<div style='display:flex;flex-wrap:wrap;gap:12px;padding:12px'>" + tiles + "</div>"

BIG = lambda k: icon(k).replace("class='ni'", "style='width:34px;height:34px'").replace("viewBox='0 0 15 15'", "viewBox='0 0 15 15' width='34' height='34'")
smart_body = ("<div class='filterbar'><span style='background:#2f6fb2;color:#fff;padding:2px 8px;border-radius:10px'>"
    "Filtered &#8594; Genesis 8 Female</span></div>"
    + thumbgrid("", [("Wear", "cloth"), ("Hair", "hair"), ("Poses", "figure"),
                     ("Materials", "surface"), ("Shaping", "morph"), ("Anatomy", "figure")]))
lib_body = tree([
    dict(depth=0, toggle="open", icon="folder", label="DAZ Studio Formats"),
    dict(depth=1, toggle="open", icon="folder", label="My DAZ 3D Library"),
    dict(depth=2, toggle="open", icon="folder", label="People"),
    dict(depth=3, toggle="open", icon="folder", label="Genesis 8", sel=True),
    dict(depth=4, icon="figure", label="Genesis 8 Female"),
    dict(depth=4, icon="figure", label="Genesis 8 Male"),
    dict(depth=4, icon="folder", label="Characters"),
    dict(depth=2, icon="folder", label="Props"),
])
smart_vs = ("<div style='display:flex;height:100%;gap:5px;padding:5px;background:#c7cad1'>"
    "<div style='flex:1'>" + pane("Smart Content", smart_body, style="height:100%") + "</div>"
    "<div style='flex:1'>" + pane("Content Library", lib_body, style="height:100%") + "</div></div>")
fig("l02_smart_vs_library", 900, 520, smart_vs)

# =================================================================== L03
# 3.1 annotated workspace
def callouts(items, w, h):
    lines = ""
    labels = ""
    for text, lx, ly, px, py in items:
        lines += "<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='#2f6fb2' stroke-width='2'/><circle cx='%d' cy='%d' r='4' fill='#2f6fb2'/>" % (lx, ly, px, py, px, py)
        labels += "<div class='callout' style='left:%dpx;top:%dpx;transform:translate(-50%%,-50%%)'>%s</div>" % (lx, ly, text)
    return ("<div class='olay'><svg width='%d' height='%d' style='position:absolute;inset:0'>%s</svg></div>%s"
            ) % (w, h, lines, labels)
l03_over = callouts([
    ("Viewport", 450, 150, 450, 300),
    ("Content panes", 120, 470, 120, 380),
    ("Scene pane", 790, 150, 790, 230),
    ("Parameters pane", 790, 470, 790, 430),
], 900, 560)
fig("l03_workspace_regions", 900, 560, build_window(bust("hdri", w=400, h=520), overlay=l03_over))

# 3.2 viewport controls close-up
vc = ("<div class='vp' style='width:100%;height:100%'>"
    "<div class='vptop' style='font-size:13px;padding:8px 12px'>"
    "<span class='vpsel' style='padding:5px 14px'>Perspective View &#9662;</span>"
    "<div class='vpnav' style='gap:8px'>"
    "<i style='width:30px;height:26px'>&#8635;</i><i style='width:30px;height:26px'>&#10021;</i>"
    "<i style='width:30px;height:26px'>&#128269;</i><i style='width:30px;height:26px'>&#9673;</i></div></div>"
    "<div style='flex:1;position:relative'>"
    "<div class='callout' style='left:150px;top:80px'>View / camera selector</div>"
    "<svg style='position:absolute;inset:0' width='900' height='320'>"
    "<line x1='150' y1='96' x2='120' y2='6' stroke='#2f6fb2' stroke-width='2'/>"
    "<line x1='760' y1='70' x2='820' y2='16' stroke='#2f6fb2' stroke-width='2'/></svg>"
    "<div class='callout' style='right:120px;top:70px'>DrawStyle &amp; orbit / pan / zoom</div>"
    "</div></div>")
fig("l03_viewport_controls", 900, 380, vc)

# 3.3 scene pane
scene3 = pane("Scene", tree([
    dict(depth=0, toggle="open", icon="figure", label="Genesis 8 Female", sel=True, eye=True),
    dict(depth=1, toggle="open", icon="bone", label="hip", eye=True),
    dict(depth=2, toggle="open", icon="bone", label="spine", eye=True),
    dict(depth=3, toggle="open", icon="bone", label="chest", eye=True),
    dict(depth=4, toggle="open", icon="bone", label="neck", eye=True),
    dict(depth=5, toggle="open", icon="bone", label="head", eye=True),
    dict(depth=6, icon="prop", label="Cowboy Hat", eye=True),
    dict(depth=0, icon="camera", label="Perspective View", eye=True),
    dict(depth=0, icon="light", label="Distant Light 1", eye_off=True),
]), style="height:100%")
fig("l03_scene_pane", 720, 520, scene3)

# 3.4 workspace menu
wm = ("<div class='win' style='height:100%'>"
    "<div class='menubar'><b>Daz Studio</b><span>File</span><span>Edit</span><span>Create</span>"
    "<span>Tools</span><span>Render</span><span style='background:#2f6fb2;color:#fff'>Window</span><span>Help</span></div>"
    "<div style='position:relative;flex:1;background:#c7cad1'>"
    "<div style='position:absolute;left:250px;top:6px' class='menu'>"
    + "".join("<div class='mi%s'>%s%s</div>" % (c, t, ("<span class='rk'>&#9656;</span>" if r else ""))
              for t, c, r in [("Style", "", False), ("Workspace", " hl", True), ("Panes (Tabs)", "", True),
                              ("Layout", "", True), ("", " sep", False), ("Show Hidden Panes", "", False)])
    + "</div>"
    "<div style='position:absolute;left:462px;top:28px' class='menu'>"
    + "".join("<div class='mi%s'>%s%s</div>" % (c, t, k)
              for t, c, k in [("Select Layout&#8230;", "", ""), ("Save Layout As&#8230;", "", ""),
                              ("Update &amp; Merge Layout", "", ""), ("", " sep", ""),
                              ("City Limits (4 x 3)", "", "<span class='rk'>&#10003;</span>"),
                              ("Hollywood Blvd (Adv.)", "", ""), ("Studio (Basic)", "", "")])
    + "</div></div></div>")
fig("l03_workspace_menu", 820, 480, wm)

# =================================================================== L04
fig("l04_default_apose", 760, 560, viewport(body_fig("hdri", pose="apose", w=360, h=540), view="Perspective View", style="height:100%"))

def powerpose_map():
    return ("<svg viewBox='0 0 260 460' style='height:100%;width:auto'>"
        "<rect width='260' height='460' fill='#eef0f3'/>"
        "<g stroke='#9aa6b4' stroke-width='10' stroke-linecap='round' fill='none'>"
        "<line x1='130' y1='70' x2='130' y2='250'/><line x1='130' y1='110' x2='70' y2='190'/>"
        "<line x1='130' y1='110' x2='190' y2='190'/><line x1='130' y1='250' x2='95' y2='400'/>"
        "<line x1='130' y1='250' x2='165' y2='400'/></g><circle cx='130' cy='48' r='26' fill='#9aa6b4'/>"
        "<g fill='#2f6fb2'>"
        + "".join("<circle cx='%d' cy='%d' r='8'/>" % (x, y) for x, y in
                  [(130,48),(130,110),(70,190),(190,190),(130,180),(130,250),(95,400),(165,400),(70,150),(190,150)])
        + "</g><text x='130' y='440' font-size='13' fill='#5b616b' text-anchor='middle'>PowerPose</text></svg>")
ap_left = viewport(body_fig("directional", pose="apose", w=320, h=430,
    extra="<circle cx='256' cy='320' r='16' fill='none' stroke='#e0b64c' stroke-width='3'/>"
          "<circle cx='256' cy='320' r='5' fill='#e0b64c'/>"
          "<path d='M256 320 L300 300' stroke='#e0b64c' stroke-width='2.5'/>"),
    view="ActivePose &#8212; drag", style="height:100%")
ap = ("<div style='display:flex;height:100%;gap:5px;padding:5px;background:#c7cad1'>"
    "<div style='flex:1.2'>" + ap_left + "</div>"
    "<div style='flex:1'>" + pane("PowerPose", "<div style='height:100%;display:flex;justify-content:center;padding:8px'>"
    + powerpose_map() + "</div>", style="height:100%") + "</div></div>")
fig("l04_activepose_powerpose", 900, 520, ap)

# =================================================================== L05
shaping = pane(None, strip(["Shaping"], 0) + two_col(
    tree([
        dict(depth=0, toggle="open", icon="figure", label="Genesis 8 Female"),
        dict(depth=1, toggle="open", icon="group", label="Actor", sel=True),
        dict(depth=2, icon="morph", label="Head"),
        dict(depth=2, icon="morph", label="Body"),
        dict(depth=1, icon="group", label="Head"),
        dict(depth=1, icon="group", label="Body"),
        dict(depth=1, icon="group", label="Expressions"),
    ], ),
    "<div class='props'>" + group_header("Actor / Head") +
    prow_slider("Head Size", 0.5, "0.0") + prow_slider("Face Round&#8594;Long", 0.62, "0.24") +
    prow_slider("Eyes Size", 0.44, "-0.12") + group_header("Actor / Body") +
    prow_slider("Height", 0.55, "0.30") + prow_slider("Body Tone", 0.4, "0.0") + "</div>", lw="40%"),
    tabs=["Shaping"], active=0, style="height:100%;border:none")
fig("l05_shaping_pane", 860, 520, shaping)

morph_over = ("<path d='M150 210 Q140 250 158 286' stroke='#000' stroke-opacity='0.08' stroke-width='8' fill='none'/>"
    "<path d='M250 210 Q260 250 242 286' stroke='#000' stroke-opacity='0.08' stroke-width='8' fill='none'/>"
    "<path d='M200 214 Q212 244 200 258' fill='#000' opacity='0.06'/>")
face_ba = rrow([
    rcell(bust("skin", eyes="flat", w=400, h=460), label="Base head", tag="Before"),
    rcell(bust("skin", eyes="flat", w=400, h=460, extra=morph_over), label="Custom head morphs", tag="After"),
])
fig("l05_face_before_after", 900, 500, face_ba, bg="#26282d")

# =================================================================== L06
surf_list = tree([
    dict(depth=0, toggle="open", icon="figure", label="Genesis 8 Female"),
    dict(depth=1, icon="surface", label="Face", sel=True), dict(depth=1, icon="surface", label="Lips"),
    dict(depth=1, icon="surface", label="Torso"), dict(depth=1, icon="surface", label="Arms"),
    dict(depth=1, icon="surface", label="Legs"), dict(depth=1, icon="surface", label="EyeMoisture"),
    dict(depth=1, icon="surface", label="Cornea"),
])
surf_props = (group_header("Base") + prow_color("Base Color", "#c98e73", "Skin") +
    prow_slider("Metallic Weight", 0.0, "0.0") + prow_slider("Glossy Roughness", 0.35, "0.35") +
    group_header("Bump &amp; Normal") + prow_slider("Bump Strength", 0.42, "0.42") +
    prow_value("Normal Map", "skin_face_nm.png") + group_header("Translucency") +
    prow_slider("Translucency Weight", 0.28, "0.28") + prow_color("SSS Reflectance", "#c46a5a"))
fig("l06_surfaces_pane", 860, 540, pane(None, strip(["Editor", "Shader Baker", "Presets"], 0)
    + two_col(surf_list, "<div class='props'>" + surf_props + "</div>", lw="38%"),
    tabs=["Surfaces"], active=0, style="height:100%;border:none"))

eyes_ba = rrow([
    rcell(bust("skin", eyes="flat", hair="block", w=400, h=460), label="Flat eyes &#183; blocky hair", tag="Before"),
    rcell(bust("skin", eyes="glossy", hair="strand", w=400, h=460), label="Glossy eyes &#183; strand hair", tag="After"),
])
fig("l06_eyes_hair_before_after", 900, 500, eyes_ba, bg="#26282d")

# =================================================================== L07
scene7 = pane("Scene", tree([
    dict(depth=0, toggle="open", icon="figure", label="Genesis 8 Female", sel=True, eye=True),
    dict(depth=1, toggle="open", icon="bone", label="hip", eye=True),
    dict(depth=1, icon="hair", label="Bob Hair", eye=True),
    dict(depth=1, icon="cloth", label="Summer Dress", eye=True),
    dict(depth=1, icon="cloth", label="Ankle Boots", eye=True),
    dict(depth=1, toggle="open", icon="bone", label="rHand", eye=True),
    dict(depth=2, icon="prop", label="Coffee Cup (parented)", eye=True),
    dict(depth=0, icon="camera", label="Perspective View", eye=True),
]), style="height:100%")
fig("l07_scene_pane_hierarchy", 720, 520, scene7)

cmp7 = rrow([
    rcell(bust("headlamp", w=400, h=450), label="Headlamp only &#8212; flat, shadowless", tag="Before"),
    rcell(bust("directional", w=400, h=450), label="Directional scene light &#8212; form &amp; depth", tag="After"),
])
fig("l07_headlamp_vs_light", 900, 500, cmp7, bg="#2b2e33")

# =================================================================== L08
emis_vp = ("<div class='vp' style='height:150px'>"
    "<div class='vpstage' style='align-items:center'>"
    "<svg viewBox='0 0 400 150' style='height:100%'>"
    "<rect width='400' height='150' fill='#2b2e33'/>"
    "<rect x='150' y='30' width='100' height='90' rx='4' fill='#fff6df'/>"
    "<rect x='150' y='30' width='100' height='90' rx='4' fill='#ffe9a8' opacity='.6'/>"
    "<ellipse cx='200' cy='75' rx='150' ry='70' fill='#ffdf9a' opacity='.20'/></svg></div></div>")
emis_props = strip(["Editor", "Shader Baker", "Presets"], 0) + two_col(
    tree([dict(depth=0, toggle="open", icon="prop", label="Plane"),
          dict(depth=1, icon="surface", label="Default", sel=True)]),
    "<div class='props'>" + group_header("Base") + prow_color("Base Color", "#3a3a3a", "Dark") +
    group_header("Emission") + prow_color("Emission Color", "#fff3d6", "Warm white") +
    prow_value("Emission Temperature", "6500 K") + prow_slider("Luminance", 0.7, "1500") +
    prow_value("Luminance Units", "cd/m&#178;") + "</div>", lw="34%")
fig("l08_emissive_surface", 860, 560, emis_vp + pane(None, emis_props, tabs=["Surfaces"], active=0,
    style="height:calc(100% - 150px);border:none"))

light3 = rrow([
    rcell(bust("flat", w=340, h=440), label="Flat single light", tag="1"),
    rcell(bust("hdri", w=340, h=440), label="HDRI dome", tag="2"),
    rcell(bust("three", w=340, h=440), label="Three-point rig", tag="3"),
])
fig("l08_lighting_comparison", 1050, 470, light3, bg="#26282d")

# =================================================================== L09
rs = pane(None, strip(["General", "Progressive Rendering", "Advanced"], 1) + "<div class='props'>"
    + group_header("Engine") + prow_value("Render Engine", "NVIDIA Iray") + prow_value("Pixel Size", "1600 x 1200")
    + group_header("Progressive Rendering") + prow_slider("Max Samples", 0.6, "5000")
    + prow_slider("Max Time (s)", 0.4, "1800") + prow_slider("Rendering Quality", 0.75, "3.00")
    + prow_value("Rendering Converged Ratio", "95%") + "</div>",
    tabs=["Render Settings"], active=0, style="height:100%;border:none")
fig("l09_render_settings", 860, 540, rs)

denoise3 = rrow([
    rcell(bust("three", noise=1.0, w=340, h=440), label="Noisy low-sample", tag="1"),
    rcell(bust("three", w=340, h=440), label="Denoised", tag="2"),
    rcell(bust("three", w=340, h=440,
        extra="<rect width='400' height='500' fill='#d98c3a' opacity='0.06'/>"
              "<radialGradient id='grade'><stop offset='.6' stop-color='#000' stop-opacity='0'/>"
              "<stop offset='1' stop-color='#000' stop-opacity='.22'/></radialGradient>"
              "<rect width='400' height='500' fill='url(#grade)'/>"), label="Final graded", tag="3"),
])
fig("l09_denoise_comparison", 1050, 470, denoise3, bg="#26282d")

# =================================================================== L10
sim = pane("Simulation Settings",
    "<div style='padding:12px'>" + btn("Simulate", True).replace("padding:6px 15px", "padding:9px 26px;font-size:13px") + "</div>"
    + "<div class='props'>" + group_header("Frames") + prow_value("Frames to Simulate", "Animated (Use Timeline)")
    + prow_value("Current Frame", "30 / 30") + group_header("Quality")
    + prow_slider("Subframes", 0.4, "3") + prow_slider("Stabilization Time", 0.3, "0.30")
    + group_header("Garment &#183; dForce Surface") + prow_slider("Dynamics Strength", 0.85, "1.00")
    + prow_slider("Bend Stiffness", 0.4, "0.40") + prow_slider("Stretch Stiffness", 0.5, "0.50") + "</div>",
    style="height:100%")
fig("l10_simulation_settings", 760, 560, sim)

drape = rrow([
    rcell(body_fig("directional", pose="apose", garment="stiff", w=360, h=520), label="No simulation &#8212; stiff, intersecting", tag="Before"),
    rcell(body_fig("directional", pose="apose", garment="drape", w=360, h=520), label="After dForce drape &#8212; natural folds", tag="After"),
])
fig("l10_drape_before_after", 900, 560, drape, bg="#2b2e33")

# =================================================================== L11
def timeline_pane():
    # ruler ticks + keyframes + playhead over 0..30 frames across width 800
    ticks = ""
    for f in range(0, 31, 5):
        x = 30 + f * 24
        ticks += "<line x1='%d' y1='0' x2='%d' y2='12' stroke='#8a8f98'/><text x='%d' y='26' font-size='10' fill='#6b7079' text-anchor='middle'>%d</text>" % (x, x, x, f)
    keys = "".join("<path d='M%d 8 l6 6 l-6 6 l-6 -6 Z' fill='#2f6fb2'/>" % (30 + f*24) for f in [0, 6, 14, 22, 30])
    playhead = "<line x1='%d' y1='0' x2='%d' y2='60' stroke='#d0432f' stroke-width='2'/><path d='M%d 0 l6 0 l-6 8 l-6 -8 Z' fill='#d0432f'/>" % (30+14*24, 30+14*24, 30+14*24)
    body = ("<div style='display:flex;align-items:center;gap:10px;padding:8px 12px;background:#e7e9ec;border-bottom:1px solid #cdd0d6;font-size:12px'>"
        "<span class='tbtn'>&#9198;</span><span class='tbtn'>&#9664;</span>"
        "<span class='tbtn' style='background:#2f6fb2;color:#fff'>&#9654;</span>"
        "<span class='tbtn'>&#9654;&#9654;</span><span class='tbtn'>&#9199;</span>"
        "<span style='margin-left:14px;color:#40454d'>Current</span><span class='field' style='width:52px;flex:none;text-align:center'>14</span>"
        "<span style='color:#40454d'>Total</span><span class='field' style='width:52px;flex:none;text-align:center'>30</span>"
        "<span style='color:#40454d'>FPS</span><span class='field' style='width:44px;flex:none;text-align:center'>30</span></div>"
        "<div style='padding:6px 0 0 0'>"
        "<svg viewBox='0 0 800 40' style='width:100%;height:40px'>" + ticks + "</svg></div>"
        "<div style='display:flex'>"
        "<div style='width:180px;padding:8px 12px;font-size:12px;color:#2c3038;border-right:1px solid #d3d6dc;background:#eceef1'>"
        + icon("figure") + " Genesis 8 Female</div>"
        "<div style='flex:1;position:relative'>"
        "<svg viewBox='0 0 800 60' style='width:100%;height:60px'>"
        "<rect width='800' height='60' fill='#f7f8fa'/>" + keys + playhead + "</svg></div></div>")
    return pane("Timeline", body, style="height:100%")
fig("l11_timeline_pane", 900, 340, timeline_pane())

def turn_body(i, angle):
    # simple clay full-body silhouette rotated; face on front, hair on back, nose on side
    face = ""
    if i == 0:   # front
        face = "<circle cx='90' cy='60' r='1.6' fill='#000' opacity='.2'/>"
    elif i in (1, 4):  # 3/4
        face = "<path d='M104 58 q6 6 0 12' stroke='#000' stroke-opacity='.15' fill='none'/>"
    elif i == 2:  # back
        face = "<path d='M62 40 Q90 30 118 40 Q120 70 90 74 Q60 70 62 40 Z' fill='#3c342c'/>"
    elif i == 3:  # side
        face = "<path d='M120 56 q10 6 0 12' fill='#c9b7a3'/>"
    return ("<svg viewBox='0 0 180 320' style='height:100%%'><rect width='180' height='320' fill='url(#tbg%d)'/>"
        "<defs><linearGradient id='tbg%d' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#7d828b'/><stop offset='1' stop-color='#4f535b'/></linearGradient></defs>"
        "<ellipse cx='90' cy='300' rx='46' ry='9' fill='#000' opacity='.2'/>"
        "<circle cx='90' cy='56' r='24' fill='#c9b7a3'/>%s"
        "<path d='M66 82 Q90 74 114 82 L118 180 Q118 210 106 220 L74 220 Q62 210 62 180 Z' fill='#c9b7a3'/>"
        "<path d='M68 96 L44 170 M112 96 L136 170' stroke='#c9b7a3' stroke-width='15' fill='none' stroke-linecap='round'/>"
        "<path d='M78 218 L72 292 M102 218 L108 292' stroke='#c9b7a3' stroke-width='17' fill='none' stroke-linecap='round'/>"
        "<rect x='62' y='8' width='56' height='22' rx='4' fill='rgba(20,22,26,.55)'/>"
        "<text x='90' y='24' font-size='14' fill='#fff' text-anchor='middle'>%s</text></svg>") % (i, i, face, angle)
film = "<div style='display:flex;height:100%'>" + "".join(
    "<div style='flex:1;border-right:%s'>%s</div>" % ("2px solid #d0d3d9" if i < 4 else "none", turn_body(i, a))
    for i, a in enumerate(["0&#176;", "72&#176;", "144&#176;", "216&#176;", "288&#176;"])) + "</div>"
fig("l11_turntable_filmstrip", 1000, 380, film, bg="#4f535b")

# =================================================================== L12
b12 = (ifield("Asset Name", "Genesis8Female_Hero") + icheck("Export Morphs", True)
    + icheck("Export Animation", False) + icheck("Merge Diffuse &amp; Translucency", True)
    + "<div style='display:flex;gap:8px;justify-content:flex-end;padding:10px 16px 4px'>"
    + btn("Cancel") + btn("Accept", True) + "</div>")
fig("l12_bridge_export_dialog", 820, 500,
    "<div class='win' style='background:#c7cad1'><div style='flex:1'></div></div>"
    + dialog("Daz to Blender Bridge &#8212; Export", b12, w=440,
             sub="File &#8594; Send To &#8594; Daz to Blender"))

def blender_scene(w, h, label="Pose Mode"):
    return ("<svg viewBox='0 0 %d %d'><rect width='%d' height='%d' fill='#3b3b3b'/>"
        "<g stroke='#4a4a4a' stroke-width='1'>" + "".join(
            "<line x1='0' y1='%d' x2='%d' y2='%d'/>" % (y, w, y) for y in range(int(h*0.6), h, 26))
        + "".join("<line x1='%d' y1='%d' x2='%d' y2='%d'/>" % (x, int(h*0.6), x, h) for x in range(0, w, 40))
        + "</g>"
        # clay figure
        "<g transform='translate(%d,%d)'>"
        "<ellipse cx='0' cy='240' rx='42' ry='9' fill='#000' opacity='.3'/>"
        "<circle cx='0' cy='20' r='22' fill='#c3b4a2'/>"
        "<path d='M-22 44 Q0 36 22 44 L26 150 Q26 178 14 188 L-14 188 Q-26 178 -26 150 Z' fill='#c3b4a2'/>"
        "<path d='M-20 58 L-44 130 M20 58 L44 130' stroke='#c3b4a2' stroke-width='15' fill='none' stroke-linecap='round'/>"
        "<path d='M-12 186 L-18 250 M12 186 L18 250' stroke='#c3b4a2' stroke-width='17' fill='none' stroke-linecap='round'/>"
        # orange armature
        "<g stroke='#e08a2b' stroke-width='2' fill='#f2a94a' opacity='.92'>"
        "<path d='M0 6 l4 14 l-4 14 l-4 -14 Z'/><path d='M0 44 l5 50 l-5 50 l-5 -50 Z'/>"
        "<path d='M-4 60 l-18 34 M4 60 l18 34' /><path d='M-8 150 l-6 92 M8 150 l6 92'/>"
        "<circle cx='0' cy='6' r='3'/><circle cx='0' cy='150' r='3'/></g></g>"
        "<rect x='10' y='10' width='176' height='22' rx='3' fill='#252525'/>"
        "<text x='20' y='25' font-size='12' fill='#cfa46a'>&#9673; %s</text></svg>") % (
        w, h, w, h, w//2, int(h*0.16), label)
daz_vs = rrow([
    rcell(bust("skin", eyes="glossy", hair="strand", w=400, h=500), label="Daz Studio (Iray)", tag="Daz"),
    rcell(blender_scene(400, 500), label="Blender &#8212; armature &amp; materials", tag="Blender"),
])
fig("l12_daz_vs_blender", 980, 540, daz_vs, bg="#2b2e33")

# =================================================================== L13
b13 = (ifield("Asset Name", "Genesis8Female_Hero") + idrop("Asset Type", "Skeletal Mesh")
    + icheck("Bake Subdivision", True) + icheck("Export Morphs", True)
    + icheck("Enable Morph Auto JCM", True) + ifield("Port", "32345", w="90px")
    + "<div style='display:flex;gap:8px;justify-content:flex-end;padding:10px 16px 4px'>"
    + btn("Cancel") + btn("Accept", True) + "</div>")
fig("l13_unreal_export_dialog", 820, 520,
    "<div class='win' style='background:#c7cad1'><div style='flex:1'></div></div>"
    + dialog("Daz to Unreal &#8212; Export", b13, w=450, sub="File &#8594; Send To &#8594; Daz to Unreal"))

def unreal_scene(w, h):
    grid = "".join("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='#3a4048' stroke-width='1'/>" % (x, int(h*0.55), int(w/2 + (x-w/2)*2.4), h-70) for x in range(0, w, 46))
    grid += "".join("<line x1='0' y1='%d' x2='%d' y2='%d' stroke='#3a4048'/>" % (y, w, y) for y in range(int(h*0.55), h-70, 16))
    tiles = ""
    for i, (t, ic) in enumerate([("SK_Genesis8", "figure"), ("SKEL_Genesis8", "bone"), ("MI_Skin", "surface"), ("MI_Eyes", "surface")]):
        tiles += ("<g transform='translate(%d,%d)'><rect width='84' height='50' rx='4' fill='#2b2f36' stroke='#3f454e'/>"
            "<rect x='24' y='7' width='36' height='26' rx='3' fill='#3a4c66'/>"
            "<text x='42' y='45' font-size='9' fill='#c7ccd4' text-anchor='middle'>%s</text></g>") % (14 + i*100, h-54, t)
    return ("<svg viewBox='0 0 %d %d'><defs><linearGradient id='sky' x1='0' y1='0' x2='0' y2='1'>"
        "<stop offset='0' stop-color='#8fb4d6'/><stop offset='1' stop-color='#c9d6e0'/></linearGradient></defs>"
        "<rect width='%d' height='%d' fill='#20242a'/>"
        "<rect width='%d' height='%d' fill='url(#sky)'/>"
        "<rect y='%d' width='%d' height='%d' fill='#2a2f36'/>" + grid +
        # figure with shadow
        "<g transform='translate(%d,%d)'>"
        "<ellipse cx='0' cy='250' rx='52' ry='12' fill='#000' opacity='.4'/>"
        "<circle cx='0' cy='24' r='24' fill='#c9b7a3'/>"
        "<path d='M-24 50 Q0 42 24 50 L28 160 Q28 190 16 202 L-16 202 Q-28 190 -28 160 Z' fill='#c7b39d'/>"
        "<path d='M-22 64 L-48 140 M22 64 L48 140' stroke='#c7b39d' stroke-width='16' fill='none' stroke-linecap='round'/>"
        "<path d='M-13 200 L-20 264 M13 200 L20 264' stroke='#c7b39d' stroke-width='18' fill='none' stroke-linecap='round'/></g>"
        "<rect x='0' y='%d' width='%d' height='86' fill='#1b1e23'/>"
        "<text x='12' y='%d' font-size='11' fill='#9aa0aa'>Content Browser</text>" + tiles +
        "<text x='12' y='22' font-size='12' fill='#e6e6e6'>Unreal Editor &#8212; Level</text></svg>") % (
        w, h, w, h, w, int(h*0.6), int(h*0.55), w, int(h*0.45), w//2, int(h*0.2), h-86, w, h-68)
fig("l13_figure_in_unreal_level", 980, 560, unreal_scene(980, 560), bg="#20242a")

# =================================================================== L14
hero = rrow([rcell(bust("three", eyes="glossy", hair="strand", w=760, h=560,
        extra="<rect x='-180' width='760' height='560' fill='#e0a24a' opacity='0.05'/>"))])
fig("l14_daz_hero_render", 760, 560, hero, bg="#1e2024")

trip = rrow([
    rcell(bust("three", eyes="glossy", hair="strand", w=360, h=500), label="Daz &#8212; Iray render", tag="1 &#183; Daz"),
    rcell(blender_scene(360, 500, label="Cycles render"), label="Blender &#8212; Cycles", tag="2 &#183; Blender"),
    rcell(unreal_scene(360, 500), label="Unreal &#8212; in-engine", tag="3 &#183; Unreal"),
])
fig("l14_pipeline_triptych", 1100, 470, trip, bg="#1e2024")

# ------------------------------------------------------------------ write
for name, doc in FIGURES.items():
    with open(os.path.join(HTML, name + ".html"), "w", encoding="utf-8") as f:
        f.write(doc)
print("wrote", len(FIGURES), "figures:")
for n in sorted(FIGURES): print("  ", n)
