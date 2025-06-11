#!/usr/bin/env python3
"""Fetch the most recent image from the Carmanah lighthouse camera.

The script scrapes the camera web page to determine the latest JPG and
downloads it to ``Pictures/carmanah_latest.jpg`` by default.
"""

import argparse
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen
import re

BASE_URL = "https://ccgsitecams.ca/sites/carmanah/camera_1/"

PATTERN = re.compile(r"Carmanah_1_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.jpg")


def fetch_latest_image_url(base_url: str = BASE_URL) -> str:
    """Return the full URL of the most recent camera image."""
    with urlopen(base_url) as resp:
        html = resp.read().decode("utf-8", errors="ignore")

    matches = PATTERN.findall(html)
    if not matches:
        raise RuntimeError("No image links found on the page")

    # Sort the filenames chronologically using the timestamp in the name.
    def parse_timestamp(name: str) -> datetime:
        ts = name[len("Carmanah_1_"):-len(".jpg")]
        return datetime.strptime(ts, "%Y-%m-%d_%H-%M-%S")

    latest = max(matches, key=parse_timestamp)
    return base_url.rstrip('/') + '/' + latest


def download_latest_image(dest: Path, base_url: str = BASE_URL) -> Path:
    """Download the latest camera image to the given destination."""
    url = fetch_latest_image_url(base_url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as resp, open(dest, "wb") as fh:
        fh.write(resp.read())
    return dest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch the latest Carmanah camera image"
    )
    parser.add_argument(
        "dest",
        nargs="?",
        default="Pictures/carmanah_latest.jpg",
        help="where to save the downloaded image",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL,
        help="camera page URL to scrape for the image",
    )
    args = parser.parse_args()
    path = Path(args.dest)
    saved_path = download_latest_image(path, base_url=args.base_url)
    print(f"Saved latest image to {saved_path}")
