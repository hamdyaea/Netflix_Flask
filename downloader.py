#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Explicit snapshot updater; no import-time requests or hosting reload."""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import tempfile
import requests

API_URL = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"


def fetch_items(key):
    if not key:
        raise ValueError("Set UNOGS_RAPIDAPI_KEY before updating.")
    response = requests.get(API_URL, params={"q": "get:new7:CH", "p": "1", "t": "ns", "st": "adv"},
                            headers={"x-rapidapi-host": "unogs-unogs-v1.p.rapidapi.com", "x-rapidapi-key": key},
                            timeout=15)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or not isinstance(data.get("ITEMS"), list):
        raise ValueError("Unexpected API response")
    if not all(isinstance(item, dict) for item in data["ITEMS"]):
        raise ValueError("Unexpected catalogue entry")
    return data["ITEMS"]


def write_snapshot(path, items):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            json.dump({"updated": date.today().isoformat(), "items": items}, stream, ensure_ascii=False)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "instance/movies.json")
    args = parser.parse_args()
    items = fetch_items(os.environ.get("UNOGS_RAPIDAPI_KEY"))
    write_snapshot(args.output, items)


if __name__ == "__main__":
    main()
