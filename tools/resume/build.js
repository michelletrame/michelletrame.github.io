// Render tools/resume/resume.html to resume-2026.pdf (one letter page, fonts embedded).
// Usage: node tools/resume/build.js [out.pdf]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2] || 'resume-2026.pdf';
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(__dirname, 'resume.html'));
  await p.evaluate(() => document.fonts.ready);
  const overflow = await p.evaluate(() => { const pg = document.querySelector('.page'); return pg.scrollHeight - pg.clientHeight; });
  if (overflow > 0) console.warn(`Warning: content overflows the page by ${overflow}px`);
  await p.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true });
  await b.close();
  console.log('wrote', out);
})();
