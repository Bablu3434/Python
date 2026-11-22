"""Blue Lotus - entry point.

python main.py --export reel.mp4 \
--seconds 15 --size 1080x1920 --fps 30
"""

import argparse

from lotusfx.config import Config
from lotusfx.palette import THEMES


def parse():
    app = argparse.ArgumentParser(
        description="Blue Lotus - pointillism flower"
    )

    app.add_argument(
        "--size",
        default="540x960",
        help="WIDTHxHEIGHT, even numbers (default 540x960)"
    )

    app.add_argument("--fps", type=int, default=None)

    app.add_argument(
        "--seed",
        type=int,
        default=5,
        help="different seed = different lotus"
    )
