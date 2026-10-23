#!/usr/bin/env python3
"""Optional network health check. Upstream sites may block automated requests."""
import json
from pathlib import Path
from urllib.request import Request, urlopen

feeds = json.loads((Path(__file__).resolve().parents[1] / "feeds.json").read_text(encoding="utf-8"))["feeds"]
for f in feeds:
    try:
        request = Request(f["xmlUrl"], headers={"User-Agent": "LiangYou-TechFeeds/1.0 (+https://github.com/MaddestAlistar/TechFeeds)"})
        with urlopen(request, timeout=10) as response:
            data = response.read(300).lstrip()
            print("OK  ", response.status, f["title"], f["xmlUrl"], "XML" if data.startswith((b"<?xml", b"<rss", b"<feed")) else "(review response)")
    except Exception as e:
        print("WARN", f["title"], type(e).__name__, str(e)[:100])
