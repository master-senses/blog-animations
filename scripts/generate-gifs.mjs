import { createServer } from 'node:http'
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { join, extname } from 'node:path'
import { fileURLToPath } from 'node:url'
import { chromium } from 'playwright'
import { PNG } from 'pngjs'
import gifenc from 'gifenc'
const { GIFEncoder, quantize, applyPalette } = gifenc

const ROOT = join(fileURLToPath(new URL('..', import.meta.url)))
const DOCS = join(ROOT, 'docs')
const OUT = join(ROOT, 'gifs')
const DOCS_GIFS = join(DOCS, 'gifs')
const PORT = 8765

const PAGES = [
  { file: 'sliding-window.html', out: 'sliding-window.gif', durationMs: 9000, intervalMs: 200 },
  { file: 'metaphone.html', out: 'metaphone.gif', durationMs: 8000, intervalMs: 200 },
  { file: 'phonetic-vs-edit.html', out: 'phonetic-vs-edit.gif', durationMs: 6000, intervalMs: 200 },
  { file: 'pipeline-latency.html', out: 'pipeline-latency.gif', durationMs: 7000, intervalMs: 200 },
  { file: 'acronym-hashmap.html', out: 'acronym-hashmap.gif', durationMs: 12000, intervalMs: 200 },
]

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css',
  '.js': 'text/javascript',
}

function startServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      const path = req.url?.split('?')[0] || '/'
      const file = join(DOCS, path === '/' ? 'index.html' : path.replace(/^\//, ''))
      if (!file.startsWith(DOCS) || !existsSync(file)) {
        res.writeHead(404)
        res.end('Not found')
        return
      }
      const ext = extname(file)
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' })
      res.end(readFileSync(file))
    })
    server.listen(PORT, '127.0.0.1', () => resolve(server))
  })
}

function pngToRgba(buffer) {
  const png = PNG.sync.read(buffer)
  return { data: new Uint8ClampedArray(png.data), width: png.width, height: png.height }
}

function framesToGif(frames, delayMs) {
  const gif = GIFEncoder()
  let first = true

  for (const frame of frames) {
    const palette = quantize(frame.data, 128, { format: 'rgb565' })
    const index = applyPalette(frame.data, palette, 'rgb565')
    gif.writeFrame(index, frame.width, frame.height, {
      palette,
      delay: delayMs,
      repeat: 0,
      transparent: true,
      transparentIndex: 0,
      ...(first ? { first: true } : {}),
    })
    first = false
  }

  gif.finish()
  return Buffer.from(gif.bytes())
}

async function capturePage(browser, spec) {
  const page = await browser.newPage({
    viewport: { width: 860, height: 700 },
    deviceScaleFactor: 1,
  })

  await page.goto(`http://127.0.0.1:${PORT}/${spec.file}`, { waitUntil: 'networkidle' })
  await page.waitForTimeout(800)

  const card = page.locator('.card')
  const frames = []
  const count = Math.ceil(spec.durationMs / spec.intervalMs)

  for (let i = 0; i < count; i++) {
    const shot = await card.screenshot({ type: 'png' })
    frames.push(pngToRgba(shot))
    await page.waitForTimeout(spec.intervalMs)
  }

  await page.close()
  return framesToGif(frames, spec.intervalMs)
}

async function main() {
  mkdirSync(OUT, { recursive: true })
  mkdirSync(DOCS_GIFS, { recursive: true })
  const server = await startServer()
  const browser = await chromium.launch()

  try {
    for (const spec of PAGES) {
      process.stdout.write(`Capturing ${spec.file}… `)
      const gif = await capturePage(browser, spec)
      const outPath = join(OUT, spec.out)
      writeFileSync(outPath, gif)
      writeFileSync(join(DOCS_GIFS, spec.out), gif)
      process.stdout.write(`→ ${spec.out} (${(gif.length / 1024).toFixed(0)} KB)\n`)
    }
  } finally {
    await browser.close()
    server.close()
  }

  console.log('\nDone. GIFs written to gifs/')
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})
