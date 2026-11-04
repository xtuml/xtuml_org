# xtuml.org

Jekyll site for [xtuml.org](https://xtuml.org), published with GitHub Pages.

## Add an article

Create a Markdown file in `articles/`. The file name is the URL.

```markdown
---
title: How bridges work
date: 2026-11-04
tags:
  - Announcements
---

The note goes here.
```

A push to `main` rebuilds the site. Locally:

```bash
bundle install
bundle exec jekyll serve
```

The preview is served with the project base path `/xtuml_org`, matching `https://xtuml.github.io/xtuml_org/`.

## Layout

- `articles/` — news and notes. Older WordPress posts live here and keep their original URLs.
- `learn/`, `about/`, `download.md`, `faqs.md` — durable pages.
- `forums/topic/` — read-only archive of the bbPress forums.
- `assets/uploads/` — documents and images migrated off WordPress.

`tools/import_site.py` rebuilt those pages from the WordPress REST API and the `xtumlorg` scrape. It is not part of the published site.
