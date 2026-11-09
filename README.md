# michelletrame.github.io
## Password-protected case studies

AT&T, REI and the Canvas grading case study are encrypted with [StaticCrypt](https://github.com/robinmoisson/staticrypt).
Their sources live in a gitignored `private/` folder (backed up separately), not in this repo.

To rebuild them after editing:

    bundle exec jekyll build --config _config.yml,_config.private.yml -d _site-private
    LOCK_PASSWORD='your password' python3 tools/lock-pages.py

Then commit the updated `work-att.html`, `work-rei.html`, `work-canvas.html` and `.staticrypt.json`.
