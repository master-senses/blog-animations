# Diagrams

## STT options rejected

`stt-options-rejected.excalidraw` — fan-out of three STT approaches, each with a rejection reason, converging to **all rejected**.

Matches the blog architecture section (Self-host, whisper-wasm, Whisper API).

### Open / edit

1. Go to [excalidraw.com](https://excalidraw.com)
2. **Menu → Open** → select `stt-options-rejected.excalidraw`

### Export PNG locally

```bash
cd ~/.cursor/skills/excalidraw-diagram/references
uv run python ../../blog-animations/scripts/render-excalidraw.py \
  ../../blog-animations/diagrams/stt-options-rejected.excalidraw
```

Outputs `stt-options-rejected.png` next to the `.excalidraw` file.

Or in Excalidraw: **Menu → Export image → PNG** (enable background).

Dark canvas (`#0d0d0d`), orange rejection labels, monospace text.
