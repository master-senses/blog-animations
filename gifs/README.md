# GIFs for Substack (free plan)

Generated from the HTML animations. Regenerate:

```bash
npm run generate-gifs
```

## Light mode

HTML animations follow your system theme (`prefers-color-scheme: light`). Open any `.html` URL in a light-mode browser to preview.

GIFs are captured in **dark mode** by default. For light GIFs: `npm run generate-gifs -- --light`

## Upload in Substack

In the post editor: **+** → **Image** → upload the `.gif` file, or drag it in.

## Direct URLs (GitHub Pages)

After deploy, images are also at:

- https://master-senses.github.io/blog-animations/gifs/sliding-window.gif
- https://master-senses.github.io/blog-animations/gifs/metaphone.gif
- https://master-senses.github.io/blog-animations/gifs/phonetic-vs-edit.gif
- https://master-senses.github.io/blog-animations/gifs/pipeline-latency.gif
- https://master-senses.github.io/blog-animations/gifs/acronym-hashmap.gif
- https://master-senses.github.io/blog-animations/gifs/context-window.gif
- https://master-senses.github.io/blog-animations/gifs/lazy-load-progression.gif
- https://master-senses.github.io/blog-animations/gifs/sandbox-chaining.gif
- https://master-senses.github.io/blog-animations/gifs/cli-mcp-stack.png

## Files

| GIF | Animation |
|-----|-----------|
| `sliding-window.gif` | Sliding window matcher |
| `metaphone.gif` | Metaphone steps |
| `phonetic-vs-edit.gif` | Edit distance vs Metaphone |
| `pipeline-latency.gif` | Whisper vs Web API latency |
| `acronym-hashmap.gif` | Acronym HashMap lookup |
| `context-window.gif` | MCP context window bloat (tools + output) |
| `lazy-load-progression.gif` | Lazy load → filesystem → search_tool |
| `sandbox-chaining.gif` | execute_tool sandbox chaining |

## Static PNGs

| File | Diagram |
|------|---------|
| `cli-mcp-stack.png` | CLI vs MCP — same API stack |
