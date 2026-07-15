# MCP blog visuals — Taming Bloated MCPs

## Header / hero image

**Placement:** top of the post, before the Introduction.

| File | Role |
|------|------|
| `mcp-header.excalidraw` | **Source of truth** — edit in Excalidraw, then re-export |
| `mcp-header.png` | **Canonical PNG** — hero banner (`../gifs/mcp-header.png` is a copy for Pages URLs) |

Visual concept: many scattered tool-call boxes and a raw/verbose JSON blob (left) converge into a `Sandbox` / `execute_tool()` box (center), which outputs only a small `filtered result` into a clean, slim `Context window` (right) before it reaches the `Agent`. The size contrast between the cluttered left side and the small clean box on the right is the argument — bloat gets filtered out before it ever reaches the model.

Regenerate the PNG from Excalidraw:

```bash
.venv/bin/python scripts/render-excalidraw.py diagrams/mcp-header.excalidraw -o diagrams/mcp-header.png
cp diagrams/mcp-header.png gifs/mcp-header.png
```

## GIFs (animated)

| File | Blog section | Preview HTML |
|------|----------------|--------------|
| `context-window.gif` | Introduction / problem | [context-window.html](../animations/context-window.html) |
| `lazy-load-progression.gif` | Problem with MCP (tool discovery) | [lazy-load-progression.html](../animations/lazy-load-progression.html) |
| `sandbox-chaining.gif` | Code Mode (execute_tool) | [sandbox-chaining.html](../animations/sandbox-chaining.html) |

Regenerate all GIFs:

```bash
npm run generate-gifs
```

## Static diagram (CLI vs MCP)

**Canonical embed:** `cli-mcp-stack.png` (exported from Excalidraw). Use this PNG in Substack and GitHub Pages.

| File | Role |
|------|------|
| `cli-mcp-stack.excalidraw` | **Source of truth** — edit in Excalidraw, then re-export |
| `cli-mcp-stack.png` | **Canonical PNG** — blog embed (`../gifs/cli-mcp-stack.png` is a copy for Pages URLs) |
| `cli-mcp-stack.html` | Optional dark-theme HTML preview only (not the published asset) |

Regenerate the PNG from Excalidraw:

```bash
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
.venv/bin/python scripts/render-excalidraw.py diagrams/cli-mcp-stack.excalidraw -o diagrams/cli-mcp-stack.png
cp diagrams/cli-mcp-stack.png gifs/cli-mcp-stack.png
```

## Substack placement

1. **Header** — `mcp-header.png` (top of post, before Introduction)
2. **Intro** — `context-window.gif`
3. **CLI vs MCP** — `cli-mcp-stack.png`
4. **Problem with MCP** — `lazy-load-progression.gif`
5. **Code Mode** — `sandbox-chaining.gif`

## GitHub Pages URLs (after deploy)

- `https://master-senses.github.io/blog-animations/gifs/mcp-header.png`
- `https://master-senses.github.io/blog-animations/gifs/context-window.gif`
- `https://master-senses.github.io/blog-animations/gifs/lazy-load-progression.gif`
- `https://master-senses.github.io/blog-animations/gifs/sandbox-chaining.gif`
- `https://master-senses.github.io/blog-animations/gifs/cli-mcp-stack.png`
