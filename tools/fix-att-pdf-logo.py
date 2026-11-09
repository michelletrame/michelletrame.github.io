#!/usr/bin/env python3
"""Fix the AT&T logo inside att-billing-case-study.pdf.

The deck embeds the logo once (image object 75, drawn 11 times on slides
7, 8, 10, 11, 13 and 14) as a 34x33 colour image with a 958x948 soft mask.
The mask holds the globe in its top-left corner plus a sliver of the 'A'
from the full wordmark, so every logo shows up small, off-centre and with
a stray letter fragment.

This rewrites that one object: the mask becomes the globe alone, 1.3x
larger around the same centre (nudged only if it would leave the frame),
and the colour layer becomes solid AT&T blue so the stripes stay crisp.

Usage: python3 tools/fix-att-pdf-logo.py IN.pdf OUT.pdf
"""
import sys, zlib
import numpy as np
import pikepdf
from PIL import Image

SCALE = 1.3
BLUE = (0, 159, 219)  # AT&T brand blue, #009FDB

src, dst = sys.argv[1], sys.argv[2]
pdf = pikepdf.open(src)
img = pdf.get_object(75, 0)
smask = img.SMask
W, H = int(smask.Width), int(smask.Height)
mask = np.frombuffer(smask.read_bytes(), dtype=np.uint8).reshape(H, W)

# Globe = everything left of the first empty column after the globe starts.
cols = (mask > 128).any(axis=0)
x = int(np.argmax(cols))
while x < W and cols[x]:
    x += 1
globe = mask[:, :x]
ys, xs = np.nonzero(globe > 16)
y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
g = Image.fromarray(np.ascontiguousarray(globe[y0:y1, x0:x1]))
cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
nw, nh = round(g.width * SCALE), round(g.height * SCALE)
# Keep it inside the frame, with a margin: the slides clip the image a
# little inside its edges.
M = 50
cx = min(max(cx, nw / 2 + M), W - nw / 2 - M)
cy = min(max(cy, nh / 2 + M), H - nh / 2 - M)
out = Image.new('L', (W, H), 0)
out.paste(g.resize((nw, nh), Image.LANCZOS), (round(cx - nw / 2), round(cy - nh / 2)))
print(f'globe {x1 - x0}x{y1 - y0} at ({cx:.0f},{cy:.0f}) -> {nw}x{nh} in {W}x{H} mask')

smask.write(zlib.compress(out.tobytes(), 9), filter=pikepdf.Name.FlateDecode)
cw, ch = int(img.Width), int(img.Height)
img.write(zlib.compress(bytes(BLUE) * (cw * ch), 9), filter=pikepdf.Name.FlateDecode)
img.ColorSpace = pikepdf.Name.DeviceRGB
img.BitsPerComponent = 8
for k in ('/DecodeParms', '/Decode'):
    for o in (img, smask):
        if k in o:
            del o[k]
pdf.save(dst, linearize=True)
