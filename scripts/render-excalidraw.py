#!/usr/bin/env python3
"""Render .excalidraw to PNG via local HTTP server (file:// blocks esm.sh imports)."""

from __future__ import annotations

import argparse
import json
import socket
import sys
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _start_server(directory: Path, port: int) -> HTTPServer:
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

        def log_message(self, *_args):
            pass

    httpd = HTTPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def compute_bounding_box(elements: list[dict]) -> tuple[float, float, float, float]:
    min_x = min_y = float("inf")
    max_x = max_y = float("-inf")

    for el in elements:
        if el.get("isDeleted"):
            continue
        x, y = el.get("x", 0), el.get("y", 0)
        w, h = el.get("width", 0), el.get("height", 0)

        if el.get("type") in ("arrow", "line") and "points" in el:
            for px, py in el["points"]:
                min_x = min(min_x, x + px)
                min_y = min(min_y, y + py)
                max_x = max(max_x, x + px)
                max_y = max(max_y, y + py)
        else:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x + abs(w))
            max_y = max(max_y, y + abs(h))

    if min_x == float("inf"):
        return (0, 0, 800, 600)
    return (min_x, min_y, max_x, max_y)


def render(path: Path, output: Path | None, scale: int, max_width: int) -> Path:
    from playwright.sync_api import sync_playwright

    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("type") != "excalidraw":
        raise SystemExit("Not an excalidraw file")

    elements = [e for e in data["elements"] if not e.get("isDeleted")]
    min_x, min_y, max_x, max_y = compute_bounding_box(elements)
    padding = 80
    vp_width = min(int(max_x - min_x + padding * 2), max_width)
    vp_height = max(int(max_y - min_y + padding * 2), 600)
    output = output or path.with_suffix(".png")

    port = _free_port()
    httpd = _start_server(_SCRIPT_DIR, port)
    template_url = f"http://127.0.0.1:{port}/render_template.html"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                viewport={"width": vp_width, "height": vp_height},
                device_scale_factor=scale,
            )
            page.on("console", lambda msg: print(f"  [browser] {msg.type}: {msg.text}", file=sys.stderr))
            page.on("pageerror", lambda err: print(f"  [pageerror] {err}", file=sys.stderr))

            page.goto(template_url, wait_until="load", timeout=60000)
            page.wait_for_function("window.__moduleReady === true", timeout=90000)

            module_error = page.evaluate("window.__moduleError")
            if module_error:
                raise SystemExit(f"Module load failed: {module_error}")

            result = page.evaluate(f"window.renderDiagram({json.dumps(data)})")
            if not result or not result.get("success"):
                err = result.get("error", "unknown") if result else "null"
                raise SystemExit(f"Render failed: {err}")

            page.wait_for_function("window.__renderComplete === true", timeout=30000)
            svg = page.query_selector("#root svg")
            if not svg:
                raise SystemExit("No SVG after render")
            svg.screenshot(path=str(output))
            browser.close()
    finally:
        httpd.shutdown()

    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    parser.add_argument("-s", "--scale", type=int, default=2)
    parser.add_argument("-w", "--width", type=int, default=1920)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Not found: {args.input}")

    out = render(args.input, args.output, args.scale, args.width)
    print(out)


if __name__ == "__main__":
    main()
