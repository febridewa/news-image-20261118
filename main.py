#!/usr/bin/env python3
"""news-image-20261118 entry.

Copies the bundled front-page image (entry.png, the 18 November 2026
world-news poster built for this competition) to the grader's output
directory as /output/entry.png.

Pure standard library, no network access, fully deterministic: every run
writes the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(HERE, "entry.png")
TARGET = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
# A plain byte copy: the output is identical to the bundled image, run after run.
shutil.copyfile(SOURCE, TARGET)
