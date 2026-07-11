# -*- coding: utf-8 -*-
"""figkit — components for building illustrative stand-in figures for the
Daz Studio Essentials course. Emits self-contained HTML that render.py
rasterizes to PNG. Every figure carries a corner badge marking it a
stand-in, not a genuine software capture."""

FONT = "'Segoe UI','Noto Sans','DejaVu Sans','Liberation Sans',system-ui,sans-serif"

_CSS_RAW = """
* { box-sizing: border-box; margin: 0; padding: 0; }
html,body { background:#fff; }
#fig { position:relative; overflow:hidden; font-family:%(font)s;
       color:#23262b; background:#fff; -webkit-font-smoothing:antialiased; }
#fig, #fig * { line-height:1.25; }

/* ---- app / window chrome ---- */
.win { display:flex; flex-direction:column; width:100%%; height:100%%;
       background:#c7cad1; }
.menubar { display:flex; gap:2px; padding:5px 10px; font-size:12px;
       background:linear-gradient(#eef0f3,#d9dce1); border-bottom:1px solid #b0b4bc;
       color:#33373d; }
.menubar b { font-weight:600; margin-right:14px; }
.menubar span { padding:1px 7px; border-radius:3px; }
.toolbar { display:flex; align-items:center; gap:7px; padding:5px 9px;
       background:linear-gradient(#e4e6ea,#cfd2d8); border-bottom:1px solid #adb1b9; }
.tbtn { width:22px; height:20px; border-radius:3px; background:linear-gradient(#fbfbfc,#dfe2e7);
       border:1px solid #b3b7bf; display:flex; align-items:center; justify-content:center;
       font-size:12px; color:#4a4f57; }
.workspace { flex:1; display:flex; gap:5px; padding:5px; min-height:0; }
.col { display:flex; flex-direction:column; gap:5px; min-height:0; }

/* ---- panes ---- */
.pane { background:#dfe1e5; border:1px solid #b4b8c0; border-radius:4px;
        display:flex; flex-direction:column; min-height:0; overflow:hidden; }
.pane-tabs { display:flex; align-items:flex-end; gap:2px; padding:4px 6px 0 6px;
        background:linear-gradient(#d0d3d9,#c2c6cd); border-bottom:1px solid #a9adb5; }
.pane-tab { font-size:11.5px; padding:4px 11px; border:1px solid #a9adb5; border-bottom:none;
        border-radius:4px 4px 0 0; background:#cbced4; color:#4b5058; position:relative; top:1px; }
.pane-tab.active { background:#eef0f3; color:#20232a; font-weight:600; }
.pane-head { display:flex; align-items:center; justify-content:space-between;
        padding:5px 8px; font-size:12px; font-weight:600; color:#2b2f36;
        background:linear-gradient(#e9ebee,#d7dade); border-bottom:1px solid #b0b4bc; }
.pane-head .dots { color:#7b808a; letter-spacing:1px; font-weight:400; }
.pane-body { background:#f3f4f6; flex:1; min-height:0; overflow:hidden; }
.pane-body.scroll { overflow:auto; }
.filterbar { display:flex; align-items:center; gap:6px; padding:5px 7px;
        background:#e7e9ec; border-bottom:1px solid #cdd0d6; font-size:11px; color:#5b606a; }
.field { flex:1; background:#fff; border:1px solid #b9bdc5; border-radius:3px;
        padding:3px 7px; font-size:11px; color:#3a3f47; }

/* ---- trees ---- */
.tree { padding:4px 0; font-size:12px; color:#2c3038; }
.row { display:flex; align-items:center; height:22px; padding:0 8px; white-space:nowrap; }
.row.sel { background:#cfe0f4; box-shadow:inset 2px 0 0 #2f6fb2; }
.tri { width:12px; text-align:center; color:#6b7079; font-size:9px; flex:none; }
.eye { margin-left:auto; color:#8a8f98; font-size:11px; padding-left:10px; flex:none; }
.row.sel .eye { color:#3f6a97; }
.ni { width:15px; height:15px; flex:none; margin-right:6px; }
.lbl { overflow:hidden; text-overflow:ellipsis; }
.muted { color:#8b909a; }

/* ---- property rows / dials ---- */
.props { padding:6px 0; font-size:12px; }
.ghead { display:flex; align-items:center; gap:6px; padding:5px 9px; font-size:11.5px;
        font-weight:600; color:#3b4048; background:#e4e6ea; border-top:1px solid #d0d3d9;
        border-bottom:1px solid #d0d3d9; }
.prow { display:flex; align-items:center; gap:9px; padding:4px 10px; }
.pname { width:40%%; color:#40454d; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.slider { flex:1; height:6px; border-radius:4px; background:#c9cdd4;
        position:relative; box-shadow:inset 0 1px 2px rgba(0,0,0,.18); }
.slider>i { position:absolute; left:0; top:0; bottom:0; border-radius:4px;
        background:linear-gradient(#5a92cf,#2f6fb2); }
.slider>b { position:absolute; top:50%%; width:11px; height:11px; margin:-6px 0 0 -6px;
        border-radius:50%%; background:radial-gradient(circle at 40% 35%,#fff,#cdd2da);
        border:1px solid #8b909a; }
.pval { width:52px; text-align:center; font-size:11px; color:#33373e; background:#fff;
        border:1px solid #bcc0c8; border-radius:3px; padding:2px 0; }
.swatch { width:26px; height:16px; border-radius:3px; border:1px solid #9297a1; flex:none; }

/* ---- buttons / tabs ---- */
.btn { display:inline-flex; align-items:center; justify-content:center; gap:6px;
        font-size:12px; padding:6px 15px; border-radius:4px; border:1px solid #a2a7b0;
        background:linear-gradient(#fbfbfc,#e2e5ea); color:#33373e; }
.btn.pri { border-color:#255e97; color:#fff; background:linear-gradient(#4f8fd0,#2f6fb2); }
.strip { display:flex; gap:2px; padding:6px 8px 0 8px; background:#e0e2e6; }
.stab { font-size:11.5px; padding:5px 13px; border:1px solid #b0b4bc; border-bottom:none;
        border-radius:4px 4px 0 0; background:#d3d6dc; color:#4d525a; }
.stab.active { background:#f3f4f6; color:#20232a; font-weight:600; }

/* ---- viewport ---- */
.vp { position:relative; background:linear-gradient(#9aa0aa,#6f757f 55%,#585d66);
        display:flex; flex-direction:column; overflow:hidden; }
.vptop { display:flex; align-items:center; justify-content:space-between;
        padding:4px 7px; font-size:11px; color:#eef0f3;
        background:linear-gradient(rgba(40,43,48,.72),rgba(40,43,48,.30)); }
.vpsel { background:rgba(20,22,25,.55); border:1px solid rgba(255,255,255,.28);
        border-radius:3px; padding:2px 9px; color:#eef1f4; }
.vpnav { display:flex; gap:5px; }
.vpnav i { width:19px; height:18px; border-radius:3px; background:rgba(20,22,25,.42);
        border:1px solid rgba(255,255,255,.22); display:flex; align-items:center;
        justify-content:center; color:#e7eaee; font-style:normal; font-size:11px; }
.vpstage { flex:1; display:flex; align-items:flex-end; justify-content:center; min-height:0; }
.vpstage svg { height:100%%; width:auto; display:block; }

/* ---- menus (dropdown) ---- */
.menu { background:#f3f4f6; border:1px solid #9297a1; border-radius:4px;
        box-shadow:0 6px 18px rgba(0,0,0,.28); padding:4px 0; font-size:12px; min-width:210px; }
.mi { display:flex; align-items:center; justify-content:space-between; gap:20px;
        padding:5px 14px; color:#2f333b; }
.mi.hl { background:#2f6fb2; color:#fff; }
.mi.sep { border-top:1px solid #d3d6dc; margin:4px 0; padding:0; height:0; }
.mi .rk { color:#9297a1; font-size:11px; }
.mi.hl .rk { color:#dbe6f2; }

/* ---- render comparison scaffolding ---- */
.rrow { display:flex; width:100%%; height:100%%; }
.rcell { position:relative; flex:1; overflow:hidden; }
.rcell svg { display:block; width:100%%; height:100%%; }
.rlabel { position:absolute; left:10px; bottom:9px; font-size:12px; color:#fff;
        background:rgba(20,22,26,.62); padding:3px 9px; border-radius:3px; letter-spacing:.2px; }
.rtag { position:absolute; left:0; top:0; font-size:11px; font-weight:600; color:#fff;
        background:rgba(20,22,26,.55); padding:3px 9px; border-bottom-right-radius:5px; }
.rdiv { width:2px; background:rgba(255,255,255,.55); flex:none; }

/* ---- diagram ---- */
.diagram { width:100%%; height:100%%; background:#fbfcfd; }

/* ---- captions / annotations ---- */
.figtitle { position:absolute; left:0; top:0; right:0; padding:10px 16px; font-size:14px;
        font-weight:600; color:#20232a; background:rgba(255,255,255,.0); z-index:5; }
.callout { position:absolute; font-size:12px; font-weight:600; color:#12314f;
        background:#eaf2fb; border:1.5px solid #2f6fb2; border-radius:5px; padding:4px 9px;
        z-index:6; box-shadow:0 2px 6px rgba(0,0,0,.15); }
.olay { position:absolute; inset:0; z-index:4; pointer-events:none; }

/* ---- stand-in badge ---- */
.badge { position:absolute; right:0; bottom:0; z-index:20; font-size:10px; letter-spacing:.2px;
        color:#f4f5f7; background:rgba(28,31,36,.72); padding:4px 9px;
        border-top-left-radius:6px; font-family:__FONT__; }
"""
CSS = _CSS_RAW.replace("%%", "%").replace("%(font)s", FONT).replace("__FONT__", FONT)


def html_doc(inner, w, h, bg="#ffffff", badge_text="Illustrative stand-in · not an actual capture"):
    b = '<div class="badge">%s</div>' % badge_text if badge_text else ""
    return ("<!doctype html><html><head><meta charset='utf-8'><style>%s</style></head>"
            "<body><div id='fig' style='width:%dpx;height:%dpx;background:%s'>%s%s</div>"
            "</body></html>") % (CSS, w, h, bg, inner, b)


# -------------------------------------------------- small SVG node icons
def icon(kind):
    c = {
        "figure": "#c98a5a", "bone": "#b0b6c0", "prop": "#7b9e6f", "camera": "#5f6b7a",
        "light": "#e0b64c", "surface": "#6f93c4", "hair": "#8a6f57", "cloth": "#b06f9e",
        "folder": "#d8b366", "morph": "#6f93c4", "group": "#8b909a", "node": "#9aa0ab",
    }.get(kind, "#9aa0ab")
    if kind == "camera":
        body = "<rect x='2' y='4' width='8' height='7' rx='1.5' fill='%s'/><path d='M10 6.5 L13 4.5 L13 10.5 L10 8.5 Z' fill='%s'/>" % (c, c)
    elif kind == "light":
        body = "<circle cx='7.5' cy='6.5' r='4' fill='%s'/><rect x='6' y='10' width='3' height='3' fill='%s'/>" % (c, c)
    elif kind == "bone":
        body = "<circle cx='4' cy='4' r='2.3' fill='%s'/><circle cx='11' cy='11' r='2.3' fill='%s'/><rect x='4.4' y='6.4' width='2' height='4' transform='rotate(-45 5.4 8.4)' fill='%s'/>" % (c, c, c)
    elif kind == "folder":
        body = "<path d='M1 4 H6 L7.5 5.5 H14 V12 H1 Z' fill='%s'/>" % c
    elif kind == "figure":
        body = "<circle cx='7.5' cy='4' r='2.6' fill='%s'/><path d='M3.5 13 Q7.5 7 11.5 13 Z' fill='%s'/>" % (c, c)
    else:
        body = "<rect x='2' y='2.5' width='11' height='10' rx='2' fill='%s'/>" % c
    return "<svg class='ni' viewBox='0 0 15 15'>%s</svg>" % body


# -------------------------------------------------- panes & trees
def pane(title, body, tabs=None, active=0, dots=True, style=""):
    head = ""
    if tabs:
        head += "<div class='pane-tabs'>" + "".join(
            "<div class='pane-tab%s'>%s</div>" % (" active" if i == active else "", t)
            for i, t in enumerate(tabs)) + "</div>"
    if title is not None:
        head += "<div class='pane-head'><span>%s</span>%s</div>" % (
            title, "<span class='dots'>&#9776;</span>" if dots else "")
    return "<div class='pane' style='%s'>%s<div class='pane-body'>%s</div></div>" % (style, head, body)


def tree(rows):
    out = ["<div class='tree'>"]
    for r in rows:
        depth = r.get("depth", 0)
        cls = "row sel" if r.get("sel") else "row"
        tri = {"open": "&#9660;", "close": "&#9654;"}.get(r.get("toggle"), "")
        ic = icon(r["icon"]) if r.get("icon") else "<span class='ni'></span>"
        eye = "<span class='eye'>&#128065;</span>" if r.get("eye") else (
              "<span class='eye' style='opacity:.35'>&#128065;</span>" if r.get("eye_off") else "")
        lblcls = "lbl muted" if r.get("muted") else "lbl"
        out.append(
            "<div class='%s' style='padding-left:%dpx'><span class='tri'>%s</span>%s<span class='%s'>%s</span>%s</div>"
            % (cls, 8 + depth * 15, tri, ic, lblcls, r["label"], eye))
    out.append("</div>")
    return "".join(out)


def group_header(label, open=True):
    return "<div class='ghead'><span class='tri'>%s</span>%s</div>" % (
        "&#9660;" if open else "&#9654;", label)


def prow_slider(name, frac, value, unit=""):
    frac = max(0.0, min(1.0, frac))
    return ("<div class='prow'><span class='pname'>%s</span>"
            "<span class='slider'><i style='width:%d%%'></i><b style='left:%d%%'></b></span>"
            "<span class='pval'>%s%s</span></div>") % (name, int(frac*100), int(frac*100), value, unit)


def prow_value(name, value):
    return ("<div class='prow'><span class='pname'>%s</span>"
            "<span style='flex:1'></span><span class='pval' style='width:110px'>%s</span></div>") % (name, value)


def prow_color(name, hexc, value=None):
    v = value or hexc.upper()
    return ("<div class='prow'><span class='pname'>%s</span>"
            "<span class='swatch' style='background:%s'></span>"
            "<span style='flex:1'></span><span class='pval' style='width:74px'>%s</span></div>") % (name, hexc, v)


def strip(tabs, active=0):
    return "<div class='strip'>" + "".join(
        "<div class='stab%s'>%s</div>" % (" active" if i == active else "", t)
        for i, t in enumerate(tabs)) + "</div>"


def btn(label, pri=False):
    return "<span class='btn%s'>%s</span>" % (" pri" if pri else "", label)


def viewport(stage_svg, view="Perspective View", nav=True, style=""):
    navhtml = ""
    if nav:
        navhtml = ("<div class='vpnav'><i>&#8635;</i><i>&#10021;</i><i>&#128269;</i></div>")
    top = ("<div class='vptop'><span class='vpsel'>%s &#9662;</span>%s</div>") % (view, navhtml)
    return "<div class='vp' style='%s'>%s<div class='vpstage'>%s</div></div>" % (style, top, stage_svg)


# -------------------------------------------------- studio mannequin (SVG)
def _defs(mode):
    """Gradient defs for the clay bust under a given lighting mode."""
    # key light direction & fill by mode
    presets = {
        "flat":        dict(hl="#cfcbc4", mid="#b3afa8", sh="#a49f98", hlx="50%", hly="35%", rim=0,   cast=0.05, bg=("#8f9298", "#6d7075")),
        "headlamp":    dict(hl="#d3cfc8", mid="#bdb8b1", sh="#b0aba4", hlx="50%", hly="42%", rim=0,   cast=0.03, bg=("#8f9298", "#6d7075")),
        "directional": dict(hl="#e7ddcd", mid="#b39f8a", sh="#5f5346", hlx="26%", hly="30%", rim=0,   cast=0.5,  bg=("#5a5d64", "#34363b")),
        "three":       dict(hl="#efe6d6", mid="#c3ac93", sh="#6b5b49", hlx="32%", hly="30%", rim=1,   cast=0.42, bg=("#3f434b", "#212327")),
        "hdri":        dict(hl="#e6ddcf", mid="#cbb69f", sh="#8a7867", hlx="42%", hly="26%", rim=0.4, cast=0.28, bg=("#b9c2cc", "#7f8894")),
        "skin":        dict(hl="#f0d9c2", mid="#d9b093", sh="#8f6a52", hlx="36%", hly="30%", rim=0.5, cast=0.4,  bg=("#43474e", "#26282d")),
        "clay":        dict(hl="#dcd7cf", mid="#bdb6ac", sh="#8f8880", hlx="38%", hly="32%", rim=0.3, cast=0.3,  bg=("#7d828b", "#4f535b")),
    }
    p = presets.get(mode, presets["clay"])
    rim = ("<linearGradient id='rim' x1='1' y1='0' x2='0' y2='0'>"
           "<stop offset='0' stop-color='#fff' stop-opacity='%.2f'/>"
           "<stop offset='0.14' stop-color='#fff' stop-opacity='0'/></linearGradient>") % (0.85*p["rim"])
    return p, ("<defs>"
        "<radialGradient id='face' cx='%s' cy='%s' r='72%%'>"
        "<stop offset='0' stop-color='%s'/><stop offset='0.55' stop-color='%s'/>"
        "<stop offset='1' stop-color='%s'/></radialGradient>"
        "<linearGradient id='bg' x1='0' y1='0' x2='0' y2='1'>"
        "<stop offset='0' stop-color='%s'/><stop offset='1' stop-color='%s'/></linearGradient>"
        "%s"
        "<radialGradient id='vig' cx='50%%' cy='42%%' r='75%%'>"
        "<stop offset='0.55' stop-color='#000' stop-opacity='0'/>"
        "<stop offset='1' stop-color='#000' stop-opacity='0.42'/></radialGradient>"
        "</defs>") % (p["hlx"], p["hly"], p["hl"], p["mid"], p["sh"], p["bg"][0], p["bg"][1], rim)


def bust(mode="clay", eyes=None, hair=None, w=400, h=500, noise=0, extra=""):
    """A neutral clay portrait bust on a studio backdrop, lit per `mode`.
    eyes: None|'flat'|'glossy'; hair: None|'block'|'strand'."""
    p, defs = _defs(mode)
    # hair (frames the face; face oval left exposed below hairline y~154)
    hair_svg = ""
    if hair == "block":  # dull blocky card hair
        hair_svg = ("<path d='M114 196 Q106 104 200 98 Q294 104 286 196 Q250 156 200 156 Q150 156 114 196 Z' fill='#3c342c'/>"
                    "<path d='M120 178 Q112 232 130 260 Q146 244 148 202 Q138 186 120 178 Z' fill='#3c342c'/>"
                    "<path d='M280 178 Q288 232 270 260 Q254 244 252 202 Q262 186 280 178 Z' fill='#3c342c'/>")
    elif hair == "strand":  # softer bob with strand detail
        hair_svg = ("<path d='M114 196 Q104 100 200 96 Q296 100 286 196 Q250 152 200 152 Q150 152 114 196 Z' fill='#4a3d31'/>"
                    "<path d='M116 168 Q94 284 128 360 Q150 322 150 214 Q140 186 116 168 Z' fill='#4a3d31'/>"
                    "<path d='M284 168 Q306 284 272 360 Q250 322 250 214 Q260 186 284 168 Z' fill='#4a3d31'/>"
                    "<g stroke='#6a5642' stroke-width='1.2' opacity='.5' fill='none'>"
                    "<path d='M160 118 Q150 150 140 192'/><path d='M200 108 Q200 130 200 150'/>"
                    "<path d='M240 118 Q250 150 260 192'/><path d='M126 206 Q120 284 133 350'/>"
                    "<path d='M274 206 Q280 284 267 350'/></g>")
    # eyes (head center 200,204)
    eye_svg = ""
    if eyes == "flat":
        eye_svg = ("<ellipse cx='174' cy='198' rx='10' ry='6.5' fill='#cfc9bf'/>"
                   "<ellipse cx='226' cy='198' rx='10' ry='6.5' fill='#cfc9bf'/>"
                   "<circle cx='174' cy='198' r='3.6' fill='#5b5148'/><circle cx='226' cy='198' r='3.6' fill='#5b5148'/>")
    elif eyes == "glossy":
        eye_svg = ("<ellipse cx='174' cy='198' rx='11' ry='7' fill='#f5f2ec'/>"
                   "<ellipse cx='226' cy='198' rx='11' ry='7' fill='#f5f2ec'/>"
                   "<circle cx='175' cy='198' r='4.7' fill='#5a83a6'/><circle cx='227' cy='198' r='4.7' fill='#5a83a6'/>"
                   "<circle cx='175' cy='198' r='2.2' fill='#182430'/><circle cx='227' cy='198' r='2.2' fill='#182430'/>"
                   "<circle cx='172.6' cy='195.6' r='1.5' fill='#fff'/><circle cx='224.6' cy='195.6' r='1.5' fill='#fff'/>")
    noise_svg = ""
    if noise:
        # deterministic scattered speckles to imply render grain
        pts, seed = [], 1234
        for i in range(360):
            seed = (1103515245*seed + 12345) & 0x7fffffff
            x = 108 + (seed % 200); seed = (1103515245*seed + 12345) & 0x7fffffff
            y = 120 + (seed % 300); seed = (1103515245*seed + 12345) & 0x7fffffff
            o = (seed % 100)/100.0*0.55*noise
            pts.append("<circle cx='%d' cy='%d' r='1' fill='%s' opacity='%.2f'/>" % (x, y, "#fff" if (x+y) % 2 else "#000", o))
        noise_svg = "<g>" + "".join(pts) + "</g>"
    rim_svg = ""
    if p["rim"]:
        rim_svg = "<path d='M258 150 Q300 236 262 320 L250 318 Q286 236 248 158 Z' fill='url(#rim)'/>"
    cast = ("<path d='M232 300 Q270 360 258 470 L300 470 Q312 380 300 320 Z' fill='#000' opacity='%.2f'/>"
            % (p["cast"]*0.28)) if p["cast"] else ""
    tx = (w - 400) // 2  # centre the fixed 400-wide figure in a wider canvas
    return ("<svg viewBox='0 0 %d %d' preserveAspectRatio='xMidYMax meet'>%s"
            "<rect x='0' y='0' width='%d' height='%d' fill='url(#bg)'/>"
            "<g transform='translate(%d,0)'>"
            "<path d='M78 500 Q78 388 142 356 Q176 342 200 342 Q224 342 258 356 Q322 388 322 500 Z' fill='url(#face)'/>"  # shoulders
            "%s"                                                                                    # cast on shoulder
            "<path d='M182 288 L182 352 Q200 361 218 352 L218 288 Z' fill='url(#face)'/>"           # neck
            "<ellipse cx='200' cy='296' rx='34' ry='11' fill='#000' opacity='0.13'/>"               # under-chin shadow
            "<ellipse cx='200' cy='204' rx='80' ry='98' fill='url(#face)'/>"                        # head
            "<path d='M200 190 Q206 220 200 230 Q196 230 193 226' fill='#000' opacity='0.07'/>"     # nose shadow (soft)
            "<path d='M160 170 Q200 160 240 170' stroke='#fff' stroke-opacity='0.07' stroke-width='7' fill='none'/>"  # brow highlight
            "%s%s%s%s%s</g>"
            "<rect x='0' y='0' width='%d' height='%d' fill='url(#vig)'/></svg>") % (
        w, h, defs, w, h, tx, cast, hair_svg, eye_svg, rim_svg, noise_svg, extra, w, h)


def body_fig(mode="clay", pose="apose", garment=None, w=360, h=560, extra=""):
    """Full-body clay mannequin for A-pose / dForce / turntable figures."""
    p, defs = _defs(mode)
    # simple articulated dummy silhouette
    limbs = {
        "apose": "<path d='M180 150 L150 250 L120 350 M180 150 L210 250 L240 350' />",
    }
    garment_svg = ""
    if garment == "stiff":  # unsimulated: rigid cone flaring off the legs
        garment_svg = ("<path d='M150 300 L92 496 L268 496 L210 300 Z' fill='url(#face)' opacity='.97'/>"
                       "<g stroke='#000' stroke-opacity='.10' fill='none' stroke-width='2.5'>"
                       "<path d='M150 360 L110 496'/><path d='M210 360 L250 496'/><path d='M180 320 L180 496'/></g>")
    elif garment == "drape":  # simulated: fabric falls with gravity folds
        garment_svg = ("<path d='M156 300 Q126 402 140 470 Q152 500 166 476 Q180 500 196 476 "
                       "Q210 500 224 470 Q238 402 204 300 Z' fill='url(#face)' opacity='.97'/>"
                       "<g stroke='#000' stroke-opacity='.14' fill='none' stroke-width='3'>"
                       "<path d='M172 322 Q164 404 158 468'/><path d='M188 324 Q188 404 186 474'/>"
                       "<path d='M208 322 Q216 404 220 468'/></g>")
    return ("<svg viewBox='0 0 %d %d' preserveAspectRatio='xMidYMax meet'>%s"
            "<rect width='%d' height='%d' fill='url(#bg)'/>"
            "<ellipse cx='180' cy='524' rx='84' ry='16' fill='#000' opacity='.24'/>"
            "<circle cx='180' cy='96' r='34' fill='url(#face)'/>"
            "<path d='M150 128 Q180 118 210 128 L214 250 Q214 300 200 320 L160 320 Q146 300 146 250 Z' fill='url(#face)'/>"
            "<path d='M150 150 L114 250 L108 322' stroke='url(#face)' stroke-width='26' fill='none' stroke-linecap='round'/>"
            "<path d='M210 150 L246 250 L252 322' stroke='url(#face)' stroke-width='26' fill='none' stroke-linecap='round'/>"
            "%s"
            "<path d='M166 318 L158 516' stroke='url(#face)' stroke-width='30' fill='none' stroke-linecap='round'/>"
            "<path d='M194 318 L202 516' stroke='url(#face)' stroke-width='30' fill='none' stroke-linecap='round'/>"
            "%s<rect width='%d' height='%d' fill='url(#vig)'/></svg>") % (
        w, h, defs, w, h, garment_svg, extra, w, h)


# -------------------------------------------------- render comparison rows
def rcell(svg, label=None, tag=None):
    inner = svg
    if tag:
        inner = "<span class='rtag'>%s</span>" % tag + inner
    if label:
        inner += "<span class='rlabel'>%s</span>" % label
    return "<div class='rcell'>%s</div>" % inner


def rrow(cells, divider=True):
    div = "<div class='rdiv'></div>" if divider else ""
    return "<div class='rrow'>" + div.join(cells) + "</div>"


def scene_svg(figure_svg, mode="clay", w=400, h=500):
    """Wrap a mannequin call output already includes its own backdrop; this is
    a thin alias so figures read clearly."""
    return figure_svg
