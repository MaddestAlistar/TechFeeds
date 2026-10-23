#!/usr/bin/env python3
"""Regenerate OPML files from feeds.json, standard library only."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
feed_data = json.loads((ROOT / "feeds.json").read_text(encoding="utf-8"))


def generate(categories):
    root = ET.Element("opml", {"version": "2.0"})
    head = ET.SubElement(root, "head")
    ET.SubElement(head, "title").text = "良友科技资讯订阅库"
    ET.SubElement(head, "ownerName").text = "良哥看未来"
    body = ET.SubElement(root, "body")
    for key in categories:
        section = ET.SubElement(body, "outline", {"text": feed_data["groups"][key], "title": feed_data["groups"][key]})
        for f in feed_data["feeds"]:
            if f["category"] == key:
                ET.SubElement(section, "outline", {"type": "rss", "text": f["title"], "title": f["title"], "xmlUrl": f["xmlUrl"], "htmlUrl": f["htmlUrl"]})
    ET.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"


out = ROOT / "opml"
out.mkdir(exist_ok=True)
for key in feed_data["groups"]:
    (out / f"{key}.opml").write_text(generate([key]), encoding="utf-8")
(out / "all.opml").write_text(generate(list(feed_data["groups"])), encoding="utf-8")
for name in ["all", *feed_data["groups"]]:
    ET.parse(out / f"{name}.opml")
print(f"Generated 5 valid OPML files from {len(feed_data['feeds'])} feeds")
