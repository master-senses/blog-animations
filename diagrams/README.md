# MCP blog visuals — Taming Bloated MCPs

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

1. **Intro** — `context-window.gif`
2. **CLI vs MCP** — `cli-mcp-stack.png`
3. **Problem with MCP** — `lazy-load-progression.gif`
4. **Code Mode** — `sandbox-chaining.gif`

## GitHub Pages URLs (after deploy)

- `https://master-senses.github.io/blog-animations/gifs/context-window.gif`
- `https://master-senses.github.io/blog-animations/gifs/lazy-load-progression.gif`
- `https://master-senses.github.io/blog-animations/gifs/sandbox-chaining.gif`
- `https://master-senses.github.io/blog-animations/gifs/cli-mcp-stack.png`
