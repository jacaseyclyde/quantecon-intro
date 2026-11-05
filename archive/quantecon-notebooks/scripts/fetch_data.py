#!/usr/bin/env python3
"""Download a dataset file into data/external."""

from __future__ import annotations

import argparse
import urllib.request
from pathlib import Path

from qe_custom.paths import data_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="HTTP(S) URL to download")
    parser.add_argument(
        "--output-name",
        help="Optional output file name. Defaults to basename from URL.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_dir = data_dir("external")
    target_dir.mkdir(parents=True, exist_ok=True)

    default_name = Path(args.url).name
    output_name = args.output_name or default_name
    if not output_name:
        raise ValueError("Could not infer file name from URL; pass --output-name.")

    destination = target_dir / output_name
    urllib.request.urlretrieve(args.url, destination)
    print(f"Saved: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
