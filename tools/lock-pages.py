#!/usr/bin/env python3
"""Password-protect the confidential case studies (AT&T, REI, Canvas grading).

Usage:
  bundle exec jekyll build --config _config.yml,_config.private.yml -d _site-private
  LOCK_PASSWORD='…' python3 tools/lock-pages.py

For each page in PAGES this:
  1. takes the rendered page from _site-private/,
  2. embeds its confidential images and audio (assets/*/*-private/) as data URIs, so no
     unencrypted copy of them is ever published,
  3. encrypts the whole page with StaticCrypt, writing the result to the repo
     root (work-att.html etc.), which the public build serves as-is.

The password comes only from the LOCK_PASSWORD environment variable and is never
written to disk. .staticrypt.json holds the salt (not secret); keeping it the
same means "Remember me" unlocks every protected page at once.
StaticCrypt: npx staticrypt (installed with `npm i staticrypt@3`).
"""
import base64, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

PAGES = ['work-att.html', 'work-rei.html', 'work-canvas.html']
SITE = Path('_site-private')
PRIVATE_IMG = re.compile(r'/assets/img/[a-z-]+-private/[^"\s,]+\.webp')
PRIVATE_AUDIO = re.compile(r'/assets/audio/[a-z-]+-private/[^"\s]+\.m4a')
ICONS = ('        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />\n'
         '        <link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32" />\n'
         '        <link rel="apple-touch-icon" href="/apple-touch-icon.png" />')
PUBLIC_OG = 'https://michelletrame.github.io/assets/img/home/color-1600.webp'
STATICRYPT = os.environ.get('STATICRYPT', 'npx staticrypt')

password = os.environ.get('LOCK_PASSWORD')
if not password:
    sys.exit('Set LOCK_PASSWORD in the environment (it is not stored anywhere).')

def data_uri(url):
    path = SITE / url.lstrip('/')
    big = path.with_name(path.name.replace('-800.webp', '-1600.webp'))
    if big.exists():
        path = big  # one sharp copy instead of both sizes
    return 'data:image/webp;base64,' + base64.b64encode(path.read_bytes()).decode()

def inline(html):
    # Link previews can't see inside an encrypted page, so point og:image at a public
    # image instead of letting a private cover get embedded a second time.
    html = re.sub(r'(<meta property="og:image" content=")[^"]*-private/[^"]*(")',
                  lambda m: m.group(1) + PUBLIC_OG + m.group(2), html)
    # Drop srcset on private images (we embed one size), then swap src for a data URI.
    html = re.sub(r'\s+srcset="[^"]*-private/[^"]*"', '', html)
    html = re.sub(r'\s+sizes="[^"]*"(?=[^>]*src="data:)', '', html)
    html = PRIVATE_AUDIO.sub(lambda m: 'data:audio/mp4;base64,' + base64.b64encode((SITE / m.group(0).lstrip('/')).read_bytes()).decode(), html)
    return PRIVATE_IMG.sub(lambda m: data_uri(m.group(0)), html)

with tempfile.TemporaryDirectory() as tmp:
    for page in PAGES:
        html = (SITE / page).read_text()
        if 'staticrypt' in html[:3000]:
            sys.exit(f'{SITE / page} is already encrypted: run the private build first.')
        html = inline(html)
        left = PRIVATE_IMG.findall(html) + PRIVATE_AUDIO.findall(html)
        if left:
            sys.exit(f'{page}: private images still linked: {left[:3]}')
        (Path(tmp) / page).write_text(html)
    cmd = STATICRYPT.split() + [*[str(Path(tmp) / p) for p in PAGES],
        '-d', tmp + '/out', '-c', '.staticrypt.json', '--short', '--remember', '30',
        '--template-title', 'Password protected · Michelle Trame',
        '--template-instructions', 'This case study includes confidential client work. Enter the password Michelle shared with you to view it.',
        '--template-button', 'View case study',
        '--template-placeholder', 'Password',
        '--template-remember', 'Remember me on this device',
        '--template-error', "That password didn't work. Check it and try again.",
        '--template-color-primary', '#2b1d2e', '--template-color-secondary', '#fbf6ea']
    env = dict(os.environ, STATICRYPT_PASSWORD=password)
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    for page in PAGES:
        out = Path(tmp) / 'out' / page
        locked = out.read_text()
        if password in locked:
            sys.exit(f'{page}: password found in output, refusing to write')
        # StaticCrypt's password screen has its own <head>: give it the site favicon.
        locked = locked.replace('<head>', '<head>\n' + ICONS, 1)
        Path(page).write_text(locked)
        print(f'{page}: {out.stat().st_size / 1e6:.1f} MB encrypted')
