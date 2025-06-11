import re
from datetime import datetime
from urllib.request import urlopen

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


if __name__ == "__main__":
    print(fetch_latest_image_url())
