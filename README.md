# Blog animations — Voice mode STT correction

Interactive React demos for the article *Adding Voice Mode to a chatbot (without generative models)*.

## Demos (high impact)

| Section | Blog concept |
|--------|----------------|
| **Pipeline** | Web STT vs Whisper latency tradeoff |
| **Phonetic vs edit** | Why Metaphone beats Levenshtein for `carfentanyl` / `car-fend-nile` |
| **Metaphone** | Consonant skeleton step-by-step |
| **Scoring** | Weighted Metaphone + Jaro-Winkler + token sort ratio |
| **Sliding window** | Greedy multi-word grouping and replacement |
| **Acronyms** | HashMap for enunciated acronyms (`ay bee see` → ABC) |
| **Optimizations** | Stopwords, length filter, precomputed index, STT failure map |

## Run locally

```bash
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173`).

## Embed in a blog

1. Build: `npm run build`
2. Host `dist/` (Vercel, Netlify, S3, etc.)
3. Link to section anchors, e.g. `https://your-host.com/#sliding-window`
4. Or iframe a single section: `https://your-host.com/#metaphone`

To embed only one demo, import the component from `src/components/` into your site or split into separate Vite entries later.

## Note on Metaphone

The in-repo Metaphone is a **simplified, educational** implementation for visualization. Production systems should use a well-tested library; the animations focus on *why* phonetic matching helps, not on spec-complete encoding.
