#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Render a local JSON snapshot with Jinja's normal escaping enabled."""
import json
import os
from pathlib import Path
from flask import Flask, render_template


def create_app(snapshot=None):
    app = Flask(__name__)
    app.config["SNAPSHOT"] = Path(snapshot or os.environ.get("NETFLIX_SNAPSHOT", Path(app.instance_path) / "movies.json"))

    @app.get("/")
    def index():
        try:
            path = app.config["SNAPSHOT"]
            if path.stat().st_size > 5_000_000:
                raise ValueError("Snapshot too large")
            data = json.loads(path.read_text(encoding="utf-8"))
            items = data["items"]
            if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
                raise ValueError("Invalid items")
            updated = data["updated"]
            if not isinstance(updated, str):
                raise ValueError("Invalid date")
        except (OSError, ValueError, KeyError, TypeError):
            return "Catalogue snapshot unavailable. Run the configured updater.", 503
        return render_template("index.html", movielist=items, totalcount=len(items), dateup=updated)

    return app


app = create_app()
