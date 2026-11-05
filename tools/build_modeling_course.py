#!/usr/bin/env python3
"""Write the Modeling with xtUML lessons from a logged-in capture.

Reads tools/_cache/modeling-units.json, which is the array captured from the
WordPress course outline. Survey units and quiz-only conclusions are omitted.
Each remaining lesson becomes a Markdown page with its YouTube link.
"""

import json
import re
import subprocess
from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]


def plain(html):
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = unescape(text).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def is_survey(unit):
    title = unit["title"].lower()
    slug = urlparse(unit["url"]).path.rstrip("/").split("/")[-1]
    return "survey" in title or slug.endswith("-survey")


def is_quiz_gate(unit):
    if unit.get("youtube"):
        return False
    text = plain(unit.get("html")).lower()
    if not text:
        return True
    quizish = any(
        phrase in text
        for phrase in (
            "quiz",
            "check your knowledge",
            "check what you",
            "let's check",
            "let’s check",
            "time for a quiz",
            "time to check",
        )
    )
    return quizish and len(text) < 180


def youtube_urls(src):
    if src.startswith("//"):
        src = "https:" + src
    src = src.replace(";", "&")
    match = re.search(r"embed/([A-Za-z0-9_-]+)", src)
    if not match:
        return None
    video_id = match.group(1)
    query = parse_qs(urlparse(src).query)
    start = (query.get("start") or [None])[0]
    end = (query.get("end") or [None])[0]
    embed = f"https://www.youtube.com/embed/{video_id}?rel=0"
    watch = f"https://www.youtube.com/watch?v={video_id}"
    if start and start != "0":
        embed += f"&start={start}"
        watch += f"&t={start}s"
    if end:
        embed += f"&end={end}"
    return watch, embed


def to_markdown(html):
    cleaned = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", html or "", flags=re.I | re.S)
    cleaned = re.sub(r"<iframe\b[^>]*/>", "", cleaned, flags=re.I)
    cleaned = re.sub(
        r'<span[^>]*font-weight:\s*bold[^>]*>(.*?)</span>',
        r"<strong>\1</strong>",
        cleaned,
        flags=re.I | re.S,
    )
    cleaned = re.sub(r"</?span[^>]*>", "", cleaned, flags=re.I)
    cleaned = cleaned.replace("//www.youtube.com", "https://www.youtube.com")
    cleaned = cleaned.replace("&nbsp;", " ")

    def star_list(match):
        inner = match.group(1)
        parts = [part.strip() for part in re.split(r"<br\s*/?>", inner, flags=re.I) if part.strip()]
        if sum(part.startswith("*") for part in parts) < 2:
            return match.group(0)
        items = []
        for part in parts:
            text = re.sub(r"^\*\s+", "", part)
            items.append("<li>" + text + "</li>")
        items = "".join(items)
        return "<ul>" + items + "</ul>"

    cleaned = re.sub(r"<p(?:\s[^>]*)?>(.*?)</p>", star_list, cleaned, flags=re.I | re.S)
    cleaned = re.sub(r"<br\s*/?>", " ", cleaned, flags=re.I)
    if not plain(cleaned):
        return ""
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=cleaned,
        text=True,
        capture_output=True,
        check=True,
    )
    body = result.stdout.strip().replace("\\\n", "\n")
    lines = []
    for line in body.splitlines():
        if line.startswith("\\* "):
            if lines and lines[-1] != "" and not lines[-1].startswith("- "):
                lines.append("")
            lines.append("- " + line[3:])
        else:
            lines.append(line)
    body = "\n".join(lines).strip()
    body = body.replace("{{", "&#123;&#123;").replace("{%", "&#123;%")
    return body + "\n"


def build(course):
    source = ROOT / course["source"]
    out = ROOT / course["out"]
    course_path = course["path"]
    units = json.loads(source.read_text())
    kept = []
    dropped = []
    for unit in units:
        if is_survey(unit) or is_quiz_gate(unit):
            dropped.append(unit)
            continue
        kept.append(unit)

    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()

    pages = []
    for unit in kept:
        slug = urlparse(unit["url"]).path.rstrip("/").split("/")[-1]
        permalink = f"{course_path}{slug}/"
        videos = [youtube_urls(src) for src in unit.get("youtube") or []]
        videos = [pair for pair in videos if pair]
        pages.append(
            {
                "unit": unit,
                "slug": slug,
                "permalink": permalink,
                "old": urlparse(unit["url"]).path,
                "videos": videos,
                "body": to_markdown(unit.get("html")),
            }
        )

    for index, page in enumerate(pages):
        prev_page = pages[index - 1] if index else None
        next_page = pages[index + 1] if index + 1 < len(pages) else None
        unit = page["unit"]
        front = {
            "layout": "unit",
            "title": unit["title"],
            "permalink": page["permalink"],
            "module": unit["module"],
            "module_title": unit["moduleTitle"],
            "unit": unit["unit"],
            "course_title": course["title"],
            "course_url": course_path,
            "redirect_from": [page["old"] if page["old"].endswith("/") else page["old"] + "/"],
        }
        if page["videos"]:
            front["youtube"] = page["videos"][0][0]
            front["youtube_embed"] = page["videos"][0][1]
        if prev_page:
            front["prev"] = prev_page["permalink"]
            front["prev_title"] = prev_page["unit"]["title"]
        if next_page:
            front["next"] = next_page["permalink"]
            front["next_title"] = next_page["unit"]["title"]
        text = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
        (out / f"{page['slug']}.md").write_text(f"---\n{text}---\n\n{page['body']}")

    lines = [
        "---",
        "layout: page",
        f"title: {course['title']}",
        f"permalink: {course_path}",
        "redirect_from:",
        f"  - {course['old']}",
    ]
    for unit in dropped:
        path = urlparse(unit["url"]).path
        if not path.endswith("/"):
            path += "/"
        lines.append(f"  - {path}")
    lines += [
        "---",
        "",
        course["blurb"],
        "",
        "The lesson material is shared under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).",
        "",
    ]
    current = None
    for page in pages:
        unit = page["unit"]
        key = (unit["module"], unit["moduleTitle"])
        if key != current:
            current = key
            if lines and lines[-1] != "":
                lines.append("")
            lines.append(f"## {unit['module']}. {unit['moduleTitle']}")
            lines.append("")
        label = f"{unit['unit']}. {unit['title']}".replace("[", "").replace("]", "")
        link = "{{ '" + page["permalink"] + "' | relative_url }}"
        lines.append(f"- [{label}]({link})")
    lines.append("")
    (out / "index.md").write_text("\n".join(lines))
    print(f"{course['title']}: kept {len(pages)} dropped {len(dropped)} videos {sum(1 for p in pages if p['videos'])}")
    for unit in dropped:
        print(f"  drop {unit['module']} {unit['unit']} {unit['title']}: {plain(unit.get('html'))[:80]}")


COURSES = {
    "modeling": {
        "source": "tools/_cache/modeling-units.json",
        "out": "learn/courses/modeling-with-xtuml",
        "path": "/learn/courses/modeling-with-xtuml/",
        "old": "/course/modeling-with-xtuml/",
        "title": "Modeling with xtUML",
        "blurb": "This course introduces xtUML modeling with the xtUML Editor and BridgePoint. The lessons stay in module order. Each video lesson links to its YouTube video. Opening a lesson does not require an account, and the site does not record progress.",
    },
    "developer": {
        "source": "tools/_cache/developer-units.json",
        "out": "learn/courses/xtuml-editor-developer-training",
        "path": "/learn/courses/xtuml-editor-developer-training/",
        "old": "/course/xtuml-editor-developer-training/",
        "title": "xtUML Editor Developer Training",
        "blurb": "This course teaches you how to become an xtUML Editor developer. It covers installing the required tools, downloading and building the open-source code, and practical exercises that add features to xtUML Editor. The lessons stay in module order. Each video lesson links to its YouTube video. Opening a lesson does not require an account, and the site does not record progress.",
    },
}


if __name__ == "__main__":
    import sys

    names = sys.argv[1:] or ["modeling"]
    for name in names:
        build(COURSES[name])
