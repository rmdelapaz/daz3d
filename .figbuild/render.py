#!/usr/bin/env python3
"""Rasterize every .html in html/ to a same-named .png in the output dir.
Clips to the #fig element and renders at 2x device scale for crisp text.
Usage: python3 render.py [html_dir] [out_dir] [only_substr]
"""
import sys, glob, os
from playwright.sync_api import sync_playwright

html_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "html")
out_dir  = sys.argv[2] if len(sys.argv) > 2 else html_dir
only     = sys.argv[3] if len(sys.argv) > 3 else ""
os.makedirs(out_dir, exist_ok=True)

htmls = sorted(glob.glob(os.path.join(html_dir, "*.html")))
if only:
    htmls = [h for h in htmls if only in os.path.basename(h)]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(device_scale_factor=2, viewport={"width": 1200, "height": 1000})
    for h in htmls:
        pg.goto("file://" + os.path.abspath(h))
        pg.wait_for_timeout(120)
        el = pg.query_selector("#fig")
        if el is None:
            print("SKIP (no #fig):", h); continue
        name = os.path.splitext(os.path.basename(h))[0]
        out = os.path.join(out_dir, name + ".png")
        el.screenshot(path=out)
        box = el.bounding_box()
        print("rendered %-40s %dx%d css -> %dx%d px" % (
            name + ".png", box["width"], box["height"], box["width"]*2, box["height"]*2))
    b.close()
print("DONE")
