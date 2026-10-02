"""Re-render every README animation in one command.

Usage: python docs/src/render_gifs.py
Needs: pip install playwright pillow && python -m playwright install chromium; ffmpeg on PATH.

  hero_anim.html     -> docs/hero.gif          (illustration)
  before-after.html  -> docs/before-after.gif  (illustration)
  how-it-works.html  -> docs/how-it-works.gif  (illustration)
  walkthrough.html   -> docs/walkthrough.gif   (real app screens from docs/screens.png, animated taps)

docs/hero.png (the static still and social preview) comes from render.py.
"""
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
DOCS = SRC.parent
JOBS = [
    ("hero_anim.html", "hero.gif", 1600, 800, 9),
    ("before-after.html", "before-after.gif", 1200, 660, 10),
    ("how-it-works.html", "how-it-works.gif", 1200, 620, 10),
    ("walkthrough.html", "walkthrough.gif", 1200, 680, 10),
]

subprocess.run([sys.executable, str(SRC / "crop_screens.py")], check=True)
for html, gif, w, h, dur in JOBS:
    subprocess.run([sys.executable, str(SRC / "record_html.py"), str(SRC / html), str(DOCS / gif),
                    "--w", str(w), "--h", str(h), "--dur", str(dur), "--fps", "15", "--colors", "128"], check=True)
