#!/usr/bin/env python3
"""Turn the built Jekyll site (_site) into a self-contained preview folder.

Usage: python3 tools/make-preview.py OUT_DIR [SITE_DIR]
Build first: `bundle exec jekyll build` (public) or, to include the
confidential AT&T page, the private build described in _config.private.yml
with SITE_DIR=_site-private. Copies the migrated pages plus only
the assets they reference, rewrites root-relative links (/assets/x) to
relative ones (assets/x), and points pages that aren't in the preview
(REI and AT&T, which are password protected) at the live site.
The home page loses its <html>/<head>/<body> wrapper because the preview
host adds its own; the other pages keep theirs.
"""
import re, shutil, sys
from pathlib import Path

OUT = Path(sys.argv[1])
SITE = Path(sys.argv[2] if len(sys.argv) > 2 else '_site')
PAGES = ['index.html', 'about.html', 'work-canvas.html', 'work-apf.html']
if 'staticrypt' not in (SITE / 'work-att.html').read_text()[:2000]:
    PAGES.append('work-att.html')  # private build: the new AT&T page
LIVE = 'https://michelletrame.github.io/'

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

def rewrite(html):
    def fix(m):
        attr, url = m[1], m[2]
        if url.startswith('//') or not url.startswith('/'):
            return m[0]
        path = url[1:]
        target = path.split('#')[0]
        if target == '':
            path = 'index.html' + path  # "/" or "/#work"
        elif target.endswith('.html') and target not in PAGES:
            return f'{attr}="{LIVE}{path}"'
        return f'{attr}="{path}"'
    html = re.sub(r'(href|src)="([^"]*)"', fix, html)
    html = re.sub(r'srcset="([^"]*)"', lambda m: 'srcset="' + re.sub(r'(^|, )/', r'\1', m[1]) + '"', html)
    return html

refs = set()
for page in PAGES:
    html = rewrite((SITE / page).read_text())
    refs |= set(re.findall(r'(?:href|src)="((?:assets|[\w-]+\.(?:pdf|svg))[^"#]*)"', html))
    for srcset in re.findall(r'srcset="([^"]*)"', html):
        refs |= {part.split()[0] for part in srcset.split(', ')}
    if page == 'index.html':
        html = re.sub(r'<title>[^<]*</title>', '<title>Portfolio Redesign Preview</title>', html)
        html = re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>|</head>\s*<body[^>]*>|</body>\s*</html>\s*$', '', html, flags=re.I)
    (OUT / page).write_text(html)

css = (SITE / 'assets/css/main.css').read_text().replace('url(/assets/fonts/', 'url(../fonts/')
refs |= {'assets/fonts/' + f for f in re.findall(r'url\(\.\./fonts/([^)]+)\)', css)}
refs.discard('assets/css/main.css')
(OUT / 'assets/css').mkdir(parents=True)
(OUT / 'assets/css/main.css').write_text(css)

for ref in sorted(refs):
    src = SITE / ref
    if not src.exists():
        print('missing:', ref)
        continue
    (OUT / ref).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, OUT / ref)

files = sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file())
size = sum((OUT / f).stat().st_size for f in files)
print(f'{len(files)} files, {size / 1e6:.1f} MB')
