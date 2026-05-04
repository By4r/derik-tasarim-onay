#!/usr/bin/env node
// Usage: node screenshot.mjs <orig-url> <local-html-path> <out-dir>
// Requires: npx playwright install chromium
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const [origUrl, localHtml, outDir] = process.argv.slice(2);
if (!origUrl || !localHtml || !outDir) {
  console.error('usage: node screenshot.mjs <orig-url> <local-html-path> <out-dir>');
  process.exit(2);
}
mkdirSync(outDir, { recursive: true });
const localUrl = 'file://' + resolve(localHtml);

const viewports = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'mobile',  width: 375,  height: 800 },
];

const browser = await chromium.launch();
for (const vp of viewports) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
  for (const [label, url] of [['original', origUrl], ['template', localUrl]]) {
    const page = await ctx.newPage();
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    } catch { /* keep going on timeout */ }
    const out = `${outDir}/${label}-${vp.name}.png`;
    await page.screenshot({ path: out, fullPage: false });
    console.log('[shot]', out);
    await page.close();
  }
  await ctx.close();
}
await browser.close();
