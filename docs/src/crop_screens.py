"""Crop the three real app screens out of docs/screens.png for the walkthrough GIF.

Usage: python docs/src/crop_screens.py
Writes docs/src/screen-unlock.png, screen-vault.png, screen-viewer.png (621x820 px each).
The pixels are the real screens, unchanged: only cropped above the bottom fade.
"""
from pathlib import Path

from PIL import Image

SRC = Path(__file__).resolve().parent
im = Image.open(SRC.parent / "screens.png").convert("RGB")
for name, x in (("unlock", 60), ("vault", 731), ("viewer", 1402)):
    im.crop((x, 60, x + 621, 880)).save(SRC / f"screen-{name}.png")
    print("wrote", SRC / f"screen-{name}.png")
