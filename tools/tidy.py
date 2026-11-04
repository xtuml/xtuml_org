#!/usr/bin/env python3
"""Clean imported Markdown: relative scrape links, leftover HTML, hard breaks."""

import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "tools" / "_cache"
SKIP = {
    "download.md",
    "getting-started.md",
    "learn/on-line-courses.md",
    "about/testimonial.md",
    "index.md",
    "README.md",
}

FENCE = re.compile(r"(```.*?```)", re.S)
BROKEN = re.compile(
    r"\[?\{\{\s*'([^\]']+)\]\(([^)']*)'\s*\|\s*relative_url\s*\}\}(\)?)"
)


def load_id_map():
    found = {}
    for kind in ("posts", "pages"):
        folder = CACHE / kind
        if not folder.is_dir():
            continue
        for path in folder.glob("*.json"):
            data = json.loads(path.read_text())
            if not isinstance(data, list):
                continue
            for item in data:
                link = urllib.parse.urlparse(item.get("link") or "").path or "/"
                if not link.endswith("/"):
                    link += "/"
                found[str(item["id"])] = link
    return found


IDS = load_id_map()


def liquid(path):
    if not path.startswith("/"):
        path = "/" + path
    if "/assets/uploads/" in path:
        return "{{ '" + path.rstrip("/") + "' | relative_url }}"
    if path != "/" and not path.endswith("/"):
        path += "/"
    return "{{ '" + path + "' | relative_url }}"


def site_href(raw):
    original = raw.strip()
    if original.startswith(("mailto:", "https://", "http://")) and "xtuml.org" not in original and "hustlefish" not in original and "zipfish" not in original and "wp-content/uploads" not in original:
        return original
    text = urllib.parse.unquote(original)
    match = re.search(r"(?:\?|&|%3F)p=(\d+)", text)
    if match and match.group(1) in IDS:
        return liquid(IDS[match.group(1)])
    path = text.split("#")[0].split("?")[0]
    parts = []
    for part in path.split("/"):
        if part in ("", ".", ".."):
            continue
        if part.endswith(".html"):
            part = part[:-5]
        if part == "index":
            continue
        parts.append(part)
    if not parts:
        return liquid("/")
    if "uploads" in parts:
        rel = "/".join(parts[parts.index("uploads") + 1 :])
        return liquid("/assets/uploads/" + rel)
    if "topic" in parts:
        index = parts.index("topic")
        if index + 1 < len(parts):
            return liquid("/forums/topic/" + parts[index + 1] + "/")
    if len(parts) >= 3 and parts[0] == "community" and parts[1] == "forum":
        return liquid("/forums/" + parts[2] + "/")
    if len(parts) >= 3 and parts[0] == "forums" and parts[1] == "community":
        return liquid("/forums/" + parts[2] + "/")
    if parts[0] in ("wp-json", "wp-includes", "feed", "xmlrpc"):
        return original
    return liquid("/" + "/".join(parts) + "/")


def fix_broken(text):
    def repl(match):
        path = match.group(1)
        if not path.startswith("/"):
            path = "/" + path
        label = path.strip("/").split("/")[-1].replace("-", " ") or "page"
        return f"[{label}]({liquid(path)})"
    return BROKEN.sub(repl, text)


def fix_liquid(text):
    def repl(match):
        path = match.group(1)
        path = path.replace("/community/forum/", "/forums/")
        path = path.replace("/community/topic/", "/forums/topic/")
        path = re.sub(r"^//wp-content/uploads/", "/assets/uploads/", path)
        path = path.replace("/wp-content/uploads/", "/assets/uploads/")
        if "hustlefish" in path or "zipfish" in path:
            return match.group(0)
        return liquid(path)
    return re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", repl, text)


def html_to_md(text):
    def img(match):
        src = match.group(1)
        alt = match.group(2) or ""
        href = site_href(src) if not src.startswith("{{") else src
        if href.startswith("http") or href.startswith("{{"):
            return f"![{alt}]({href})"
        return ""

    text = re.sub(
        r'<img[^>]*?src="([^"]+)"[^>]*?(?:alt="([^"]*)")?[^>]*>',
        img,
        text,
        flags=re.I,
    )

    def anchor(match):
        href, body = match.group(1), re.sub(r"<[^>]+>", "", match.group(2)).strip()
        if not body:
            return ""
        dest = href if href.startswith("{{") else site_href(href)
        return f"[{body}]({dest})"

    text = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', anchor, text, flags=re.I | re.S)
    text = re.sub(r"</?(?:span|div|font|section|figure|figcaption)(?:\s[^>]*)?>", "", text, flags=re.I)
    return text


def relative_links(text):
    def repl(match):
        dest = match.group(1)
        if dest.startswith(("{{", "http://", "https://", "mailto:", "#")):
            return match.group(0)
        return "](" + site_href(dest) + ")"
    return re.sub(r"\]\(([^)\s]+)\)", repl, text)


def hard_breaks(text):
    parts = FENCE.split(text)
    out = []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
        else:
            out.append(part.replace("\\\n", "\n"))
    return "".join(out)


def add_topic_redirect(text, path: Path):
    if "forums/topic" not in path.as_posix():
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    slug = path.stem
    target = f"/community/topic/{slug}/"
    if target in parts[1]:
        return text
    line = f"  - \"{target}\"\n"
    if "redirect_from:" in parts[1]:
        parts[1] = parts[1].replace("redirect_from:\n", "redirect_from:\n" + line, 1)
    else:
        parts[1] = "\nredirect_from:\n" + line + parts[1]
    return "---".join(parts)


def tidy_file(path: Path):
    original = path.read_text(encoding="utf-8")
    text = original
    text = fix_broken(text)
    text = html_to_md(text)
    text = relative_links(text)
    text = fix_liquid(text)
    text = hard_breaks(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = add_topic_redirect(text, path)
    if text != original:
        path.write_text(text.strip() + "\n", encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(("tools/", ".git/")) or rel in SKIP:
            continue
        if tidy_file(path):
            changed += 1
    print("tidied", changed)


if __name__ == "__main__":
    main()
