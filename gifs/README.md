# GIFs for Substack (free plan)

Generated from the HTML animations. Regenerate:

```bash
npm run generate-gifs
```

## Light mode

HTML animations follow your system theme (`prefers-color-scheme: light`). Open any `.html` URL in a light-mode browser to preview.

The GIFs in this folder were captured in **dark mode**. Run `npm run generate-gifs` after switching your Mac to Light Appearance if you want light GIFs.

## Upload in Substack

In the post editor: **+** → **Image** → upload the `.gif` file, or drag it in.

## Direct URLs (GitHub Pages)

After deploy, images are also at:

- https://master-senses.github.io/blog-animations/gifs/sliding-window.gif
- https://master-senses.github.io/blog-animations/gifs/metaphone.gif
- https://master-senses.github.io/blog-animations/gifs/phonetic-vs-edit.gif
- https://master-senses.github.io/blog-animations/gifs/pipeline-latency.gif
- https://master-senses.github.io/blog-animations/gifs/acronym-hashmap.gif

## Files

| GIF | Animation |
|-----|-----------|
| `sliding-window.gif` | Sliding window matcher |
| `metaphone.gif` | Metaphone steps |
| `phonetic-vs-edit.gif` | Edit distance vs Metaphone |
| `pipeline-latency.gif` | Whisper vs Web API latency |
| `acronym-hashmap.gif` | Acronym HashMap lookup |
