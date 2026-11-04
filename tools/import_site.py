#!/usr/bin/env python3
"""Import xtuml.org pages, posts, media, and the forum archive.

Pages and posts come from the WordPress REST API. Forum topics come from the
local wget scrape of the bbPress forums. Re-running overwrites generated
content and leaves hand-written layouts alone.
"""

import html
import json
import re
import shutil
import subprocess
import urllib.parse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRAPE = Path("/Users/cort/git/xtumlorg")
UPLOADS = ROOT / "assets" / "uploads"
CACHE = Path(__file__).resolve().parent / "_cache"
API = "https://xtuml.org/wp-json/wp/v2"

SKIP_SLUGS = {
    "homepage",
    "account",
    "checkout",
    "login",
    "marketplace",
    "courses",
    "forum",
    "order-failed",
    "order-received",
}
SPAM = re.compile(r"办理|文凭|毕业证|学历|微\s*[:：]|wechat\d|qq-wechat", re.I)
SIZE_SUFFIX = re.compile(r"-\d+x\d+(?=\.[A-Za-z0-9]+$)")
FENCE = re.compile(r"(```.*?```)", re.S)

FORUM_ORDER = {
    "xtuml-forum": 1,
    "executable-uml-and-xtuml-methodology": 2,
    "bridgepoint-development-and-integrations": 3,
    "miscellaneous": 4,
}


def curl(url, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["curl", "-fsSL", "--retry", "3", "--retry-delay", "1", "-A", "xtuml-migration", "-o", str(dest), url],
        check=True,
    )


def fetch_collection(kind):
    dest_dir = CACHE / kind
    dest_dir.mkdir(parents=True, exist_ok=True)
    page = 1
    items = []
    while True:
        fields = ""
        embed = "&_embed=author" if kind == "posts" else ""
        url = f"{API}/{kind}?per_page=100&page={page}{embed}"
        path = dest_dir / f"page-{page}.json"
        print(f"fetch {url}")
        curl(url, path)
        batch = json.loads(path.read_text())
        if not isinstance(batch, list) or not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def fetch_categories():
    path = CACHE / "categories.json"
    curl(f"{API}/categories?per_page=100&_fields=id,name,slug", path)
    return {c["id"]: html.unescape(c["name"]) for c in json.loads(path.read_text())}


def copy_local_uploads():
    src = SCRAPE / "wp-content" / "uploads"
    if not src.is_dir():
        print("no local uploads at", src)
        return
    for year in src.iterdir():
        if year.is_dir() and year.name.isdigit():
            shutil.copytree(year, UPLOADS / year.name, dirs_exist_ok=True)
    print("copied local uploads")


def fetch_media():
    page = 1
    urls = []
    while True:
        path = CACHE / "media" / f"page-{page}.json"
        url = f"{API}/media?per_page=100&page={page}&_fields=source_url,media_details"
        print(f"fetch {url}")
        try:
            curl(url, path)
        except subprocess.CalledProcessError:
            break
        batch = json.loads(path.read_text())
        if not isinstance(batch, list) or not batch:
            break
        for item in batch:
            if item.get("source_url"):
                urls.append(item["source_url"])
            sizes = (item.get("media_details") or {}).get("sizes") or {}
            for info in sizes.values():
                if isinstance(info, dict) and info.get("source_url"):
                    urls.append(info["source_url"])
        if len(batch) < 100:
            break
        page += 1
    missing = []
    for url in urls:
        rel = upload_rel(url)
        if rel and not (UPLOADS / rel).exists():
            missing.append((url, UPLOADS / rel))
    print(f"media referenced by API: {len(urls)}; missing locally: {len(missing)}")
    for url, dest in missing:
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            curl(url, dest)
        except subprocess.CalledProcessError:
            print("  miss", url)


def upload_rel(url):
    m = re.search(r"/wp-content/uploads/(.+)$", url)
    if not m:
        return None
    rel = urllib.parse.unquote(m.group(1).split("?")[0].split("#")[0])
    return rel


def visible_text(fragment):
    text = re.sub(r"<script[\s\S]*?</script>", " ", fragment, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def pandoc(fragment):
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=fragment,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        print(proc.stderr)
        return visible_text(fragment)
    return proc.stdout.strip()


def neutralize(markdown):
    parts = FENCE.split(markdown)
    out = []
    for part in parts:
        if part.startswith("```"):
            if "{{" in part or "{%" in part:
                out.append("{% raw %}\n" + part + "\n{% endraw %}")
            else:
                out.append(part)
        else:
            part = part.replace("{{", "&#123;&#123;").replace("{%", "&#123;%")
            out.append(part)
    text = "".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def resolve_upload(rel):
    rel = urllib.parse.unquote(rel.split("?")[0].split("#")[0]).lstrip("/")
    if (UPLOADS / rel).exists():
        return rel
    plain = SIZE_SUFFIX.sub("", rel)
    if plain != rel and (UPLOADS / plain).exists():
        return plain
    return rel


def rewrite(markdown, missing):
    def sub_upload(match):
        rel = resolve_upload(match.group(1))
        if not (UPLOADS / rel).exists():
            missing.add(rel)
        return "{{ '/assets/uploads/" + rel + "' | relative_url }}"

    def sub_site(match):
        raw = match.group(1) or "/"
        path = urllib.parse.unquote(raw.split("#")[0].split("?")[0])
        if not path.startswith("/"):
            path = "/" + path
        if path.startswith(("/wp-", "/feed", "/xmlrpc", "/comments")):
            return match.group(0)
        if path != "/" and not path.endswith("/"):
            path += "/"
        return "{{ '" + path + "' | relative_url }}"

    def rewrite_text(text):
        text = re.sub(
            r"https?://(?:www\.)?xtuml\.org/wp-content/uploads/([^\s)\[\]\"'<>]+)",
            sub_upload,
            text,
            flags=re.I,
        )
        text = re.sub(
            r"https?://(?:www\.)?xtuml\.org(/[^\s)\[\]\"'<>]*)?",
            sub_site,
            text,
            flags=re.I,
        )
        return text

    parts = re.split(r"(```.*?```|\{% raw %\}.*?\{% endraw %\})", markdown, flags=re.S)
    rewritten = []
    for part in parts:
        if part.startswith("```") or part.startswith("{% raw"):
            rewritten.append(part)
        else:
            rewritten.append(rewrite_text(part))
    return "".join(rewritten)


def front_matter(meta):
    lines = ["---"]
    for key, value in meta.items():
        if value is None or value == [] or value == "":
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def clean_title(raw):
    text = re.sub(r"<[^>]+>", "", html.unescape(raw or ""))
    return re.sub(r"\s+", " ", text).strip()


def permalink_of(link, slug):
    path = urllib.parse.urlparse(link).path or "/"
    if path in ("/", "") or "p=" in (link or ""):
        path = f"/{slug}/"
    if not path.endswith("/"):
        path += "/"
    return path


def file_for(permalink, all_paths):
    rel = permalink.strip("/")
    if any(other != rel and other.startswith(rel + "/") for other in all_paths):
        return ROOT / rel / "index.md"
    return ROOT / f"{rel}.md"


def download_missing(missing):
    for rel in sorted(missing):
        dest = UPLOADS / rel
        if dest.exists():
            continue
        url = "https://xtuml.org/wp-content/uploads/" + urllib.parse.quote(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            curl(url, dest)
            print("  got", rel)
        except subprocess.CalledProcessError:
            plain = SIZE_SUFFIX.sub("", rel)
            if plain != rel and (UPLOADS / plain).exists():
                continue
            print("  still missing", rel)


def import_pages(pages):
    published = [p for p in pages if p.get("status") == "publish"]
    kept = []
    redirects = {}
    for page in published:
        slug = page.get("slug") or ""
        if slug in SKIP_SLUGS or re.fullmatch(r"testimonial(?:-\d+)+", slug):
            link = permalink_of(page.get("link", ""), slug)
            if slug.startswith("testimonial"):
                redirects.setdefault("/about/testimonial/", []).append(link)
            continue
        body = (page.get("content") or {}).get("rendered") or ""
        if len(visible_text(body)) < 80:
            continue
        kept.append(page)

    paths = []
    prepared = []
    for page in kept:
        slug = page["slug"]
        link = permalink_of(page.get("link", ""), slug)
        paths.append(link.strip("/"))
        prepared.append((page, link))

    missing = set()
    written = []
    for page, link in prepared:
        slug = page["slug"]
        title = clean_title((page.get("title") or {}).get("rendered")) or slug
        markdown = rewrite(neutralize(pandoc(page["content"]["rendered"])), missing)
        meta = {
            "layout": "page",
            "title": title,
            "permalink": link,
        }
        if link == "/about/testimonial/":
            meta["redirect_from"] = redirects.get(link, [])
        dest = file_for(link, paths)
        # A parent index must not be replaced by a child file of the same path.
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(front_matter(meta) + markdown + "\n", encoding="utf-8")
        written.append(str(dest.relative_to(ROOT)))
    print(f"pages written: {len(written)}")
    return missing


def author_name(post):
    embedded = (post.get("_embedded") or {}).get("author") or []
    if embedded and isinstance(embedded[0], dict):
        return clean_title(embedded[0].get("name"))
    return ""


def import_posts(posts, categories):
    missing = set()
    count = 0
    for post in posts:
        if post.get("status") != "publish":
            continue
        slug = post.get("slug") or f"post-{post.get('id')}"
        title = clean_title((post.get("title") or {}).get("rendered")) or slug
        link = permalink_of(post.get("link", ""), slug)
        date = (post.get("date") or "")[:10]
        tags = [categories[c] for c in post.get("categories") or [] if c in categories]
        markdown = rewrite(neutralize(pandoc(post["content"]["rendered"])), missing)
        meta = {
            "layout": "article",
            "title": title,
            "date": date,
            "permalink": link,
            "tags": tags,
        }
        name = author_name(post)
        if name:
            meta["author"] = name
        dest = ROOT / "articles" / f"{slug}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(front_matter(meta) + markdown + "\n", encoding="utf-8")
        count += 1
    print(f"articles written: {count}")
    return missing


def parse_date(text):
    if not text:
        return None
    match = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", text)
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%B %d, %Y").date().isoformat()
    except ValueError:
        return None


def topic_replies(topic_dir: Path):
    replies = []
    seen = set()
    files = [p for p in topic_dir.rglob("index.html") if "feed" not in p.parts]
    files.sort(key=lambda p: str(p))
    for path in files:
        soup_text = path.read_text(encoding="utf-8", errors="replace")
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(soup_text, "html.parser")
        for body in soup.select("li.bbp-body"):
            nodes = [n for n in body.find_all(recursive=False) if getattr(n, "name", None)]
            index = 0
            while index < len(nodes):
                node = nodes[index]
                classes = node.get("class") or []
                if "bbp-reply-header" not in classes:
                    index += 1
                    continue
                date_node = node.select_one(".bbp-reply-post-date")
                date_text = date_node.get_text(" ", strip=True) if date_node else ""
                index += 1
                if index >= len(nodes):
                    break
                reply = nodes[index]
                index += 1
                post_id = node.get("id") or f"{path}:{index}:{date_text}"
                if post_id in seen:
                    continue
                seen.add(post_id)
                author_node = reply.select_one(".bbp-author-name")
                author = author_node.get_text(" ", strip=True) if author_node else "Participant"
                content = reply.select_one(".bbp-reply-content")
                if content is None:
                    continue
                fragment = content.decode_contents()
                if len(visible_text(fragment)) < 1:
                    continue
                replies.append((author, date_text, fragment))
    # Title and forum from the first page only.
    first = topic_dir / "index.html"
    meta = {"title": topic_dir.name, "forum": "Miscellaneous", "forum_slug": "miscellaneous"}
    if first.exists():
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(first.read_text(encoding="utf-8", errors="replace"), "html.parser")
        crumb = soup.select_one("a.bbp-breadcrumb-forum")
        if crumb:
            meta["forum"] = crumb.get_text(" ", strip=True)
            href = crumb.get("href") or ""
            found = re.search(r"community/([^/]+)", href)
            if found:
                meta["forum_slug"] = found.group(1)
        title = soup.find("title")
        if title:
            meta["title"] = re.sub(r"\s+-\s+xtUML\s*$", "", title.get_text(" ", strip=True)).strip()
    return meta, replies


def import_forum():
    from bs4 import BeautifulSoup  # noqa: F401  (import error surfaces early)
    topic_root = SCRAPE / "forums" / "topic"
    missing = set()
    forums = {}
    skipped = []
    count = 0
    for topic_dir in sorted(p for p in topic_root.iterdir() if p.is_dir()):
        meta, replies = topic_replies(topic_dir)
        title = clean_title(meta["title"])
        if SPAM.search(title) or SPAM.search(topic_dir.name):
            skipped.append(topic_dir.name)
            continue
        if not replies:
            skipped.append(topic_dir.name + " (empty)")
            continue
        blocks = []
        for author, date_text, fragment in replies:
            body = rewrite(neutralize(pandoc(fragment)), missing)
            when = f" · {date_text}" if date_text else ""
            blocks.append(f"**{author}**{when}\n\n{body}")
        markdown = "\n\n---\n\n".join(blocks)
        date = parse_date(replies[0][1]) or "1970-01-01"
        slug = meta["forum_slug"]
        forums[slug] = meta["forum"]
        front = {
            "layout": "topic",
            "title": title,
            "date": date,
            "permalink": f"/forums/topic/{topic_dir.name}/",
            "forum": meta["forum"],
            "forum_slug": slug,
            "forum_url": f"/forums/{slug}/",
        }
        dest = ROOT / "forums" / "topic" / f"{topic_dir.name}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(front_matter(front) + markdown + "\n", encoding="utf-8")
        count += 1
    print(f"topics written: {count}; skipped: {len(skipped)}")
    for name in skipped:
        print("  skip", name)

    order = 1
    for slug, title in sorted(forums.items(), key=lambda item: FORUM_ORDER.get(item[0], 50)):
        front = {
            "layout": "forum",
            "title": title,
            "permalink": f"/forums/{slug}/",
            "forum_slug": slug,
            "order": FORUM_ORDER.get(slug, 50),
        }
        dest = ROOT / "forums" / f"{slug}.md"
        intro = "Topics from the original forum, newest first."
        dest.write_text(front_matter(front) + intro + "\n", encoding="utf-8")
        order += 1

    index = {
        "layout": "forums",
        "title": "Forums",
        "permalink": "/forums/",
        "redirect_from": ["/forum/"],
    }
    text = "Discussions from the xtUML community forums, kept in the groups they originally used."
    (ROOT / "forums" / "index.md").write_text(front_matter(index) + text + "\n", encoding="utf-8")
    return missing


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    copy_local_uploads()
    categories = fetch_categories()
    pages = fetch_collection("pages")
    posts = fetch_collection("posts")
    fetch_media()
    missing = set()
    missing |= import_pages(pages)
    missing |= import_posts(posts, categories)
    missing |= import_forum()
    print(f"referenced uploads still absent: {len(missing)}")
    download_missing(missing)


if __name__ == "__main__":
    main()
