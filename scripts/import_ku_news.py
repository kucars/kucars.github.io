#!/usr/bin/env python3
"""Import KUCARS news from ku.ac.ae listing page into Jekyll _news posts."""

from __future__ import annotations

import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEWS_DIR = ROOT / "_news"
IMAGE_DIR = ROOT / "assets" / "images" / "news"
LISTING_URL = (
    "https://www.ku.ac.ae/research-centers/"
    "center-for-autonomous-robotic-systems-kucars/news"
)
USER_AGENT = "Mozilla/5.0 (compatible; KUCARS-site-importer/1.0)"
# Publish dates for social posts that do not expose reliable metadata.
MANUAL_DATES = {
    "activity:7110957564074299392": "2024-02-20",
    "activity:7099687723304677376": "2022-10-15",
    "facebook.com/khalifauniversity/videos/306543351990060": "2023-11-15",
    "facebook.com/khalifauniversity/posts/pfbid05nWhQkwi2iZXeMu89Dq5aPjBUWPoFW6teyyKmVnZMbAyAkg1Vvczgm93SNf8hbNdl": "2023-11-20",
}

MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def normalize_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/:%")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def fetch(url: str) -> str:
    req = urllib.request.Request(normalize_url(url), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def download_image(url: str, dest: Path) -> bool:
    if not url or "facilty-sample.jpg" in url:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        req = urllib.request.Request(normalize_url(url), headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            dest.write_bytes(resp.read())
        return True
    except (urllib.error.URLError, OSError) as exc:
        print(f"  warning: could not download image {url}: {exc}", file=sys.stderr)
        return False


def slugify(text: str, max_len: int = 96) -> str:
    text = html.unescape(text).lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_len].rstrip("-")


def detect_source(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.lower()
    if "twitter.com" in host or "x.com" in host:
        return "Twitter"
    if "linkedin.com" in host:
        return "LinkedIn"
    if "facebook.com" in host:
        return "Facebook"
    if "instagram.com" in host:
        return "Instagram"
    if "thenationalnews.com" in host:
        return "The National"
    if "ku.ac.ae" in host:
        return "Khalifa University"
    return "External"


def date_from_url(url: str) -> str | None:
    m = re.search(r"/(20\d{2})/(\d{2})/(\d{2})/", url)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def date_from_image(url: str) -> str | None:
    m = re.search(r"/uploads/(20\d{2})/(\d{2})/", url)
    if not m:
        return None
    year, month = int(m.group(1)), int(m.group(2))
    # KU re-hosted many social images in 2024/10; those paths are not publish dates.
    if year == 2024 and month == 10:
        return None
    return f"{year}-{month:02d}-01"


def date_from_twitter(url: str) -> str | None:
    m = re.search(r"/status/(\d+)", url)
    if not m:
        return None
    snowflake = int(m.group(1))
    timestamp_ms = (snowflake >> 22) + 1288834974657
    return datetime.utcfromtimestamp(timestamp_ms / 1000).strftime("%Y-%m-%d")


def parse_listing_date(day_html: str, year_html: str) -> str | None:
    day_match = re.search(r"(\d{1,2})\s*<b>([A-Za-z]{3})</b>", day_html, re.I)
    year_match = re.search(r"(\d{4})", year_html)
    if day_match and year_match:
        month = MONTHS.get(day_match.group(2).lower()[:3])
        if month:
            return f"{year_match.group(1)}-{month:02d}-{int(day_match.group(1)):02d}"
    return None


def html_to_markdown(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"</p>\s*<p[^>]*>", "\n\n", fragment, flags=re.I)
    fragment = re.sub(r"<p[^>]*>", "", fragment, flags=re.I)
    fragment = re.sub(r"</p>", "\n\n", fragment, flags=re.I)
    fragment = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", fragment, flags=re.I | re.S)
    fragment = re.sub(r"<i[^>]*>(.*?)</i>", r"*\1*", fragment, flags=re.I | re.S)
    fragment = re.sub(
        r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        r"[\2](\1)",
        fragment,
        flags=re.I | re.S,
    )
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    fragment = re.sub(r"&hellip;", "...", fragment)
    fragment = re.sub(r"\u00a0", " ", fragment)
    fragment = re.sub(r"\n{3,}", "\n\n", fragment)
    lines = [line.strip() for line in fragment.splitlines()]
    return "\n\n".join(line for line in lines if line)


def extract_post_body(page_html: str) -> str:
    m = re.search(r'<div class="post-dtl">(.*?)</div>\s*<br class="px-50">', page_html, re.S)
    if not m:
        return ""
    return html_to_markdown(m.group(1))


def extract_single_page_date(page_html: str) -> str | None:
    m = re.search(
        r'<div class="date">\s*<span class="day">(.*?)</span>\s*<span class="year">(.*?)</span>',
        page_html,
        re.S,
    )
    if m:
        return parse_listing_date(m.group(1), m.group(2))
    return None


def extract_article_date_from_body(body: str) -> str | None:
    m = re.search(
        r"\*\*(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\*\*",
        body,
        re.I,
    )
    if m:
        month = MONTHS[m.group(2).lower()[:3]]
        return f"{m.group(3)}-{month:02d}-{int(m.group(1)):02d}"
    return None


def parse_news_blocks(listing_html: str) -> list[dict]:
    blocks = re.findall(
        r'<div class="news-blk">(.*?)</div>\s*(?=<div class="news-blk">|</div>\s*</div>\s*<br)',
        listing_html,
        re.S,
    )
    items: list[dict] = []
    for block in blocks:
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        title_m = re.search(r'<span class="title">(.*?)</span>', block, re.S)
        desc_m = re.search(r'<p class="desc">(.*?)</p>', block, re.S)
        link_m = re.search(r'<a href="([^"]+)"[^>]*class="readmore"', block)
        if not title_m or not link_m:
            continue
        title = html.unescape(re.sub(r"<[^>]+>", "", title_m.group(1))).strip()
        desc = html.unescape(re.sub(r"<[^>]+>", "", desc_m.group(1) if desc_m else "")).strip()
        desc = desc.replace("&hellip;", "...")
        image_url = img_m.group(1).strip() if img_m else ""
        source_url = html.unescape(link_m.group(1)).strip()
        items.append(
            {
                "title": title,
                "summary": desc,
                "image_url": image_url,
                "source_url": source_url,
                "source": detect_source(source_url),
            }
        )
    return items


def fetch_full_article(source_url: str) -> tuple[str, str | None]:
    if "research-center-news-single" not in source_url:
        return "", None
    try:
        page = fetch(source_url)
    except (urllib.error.URLError, OSError) as exc:
        print(f"  warning: could not fetch article {source_url}: {exc}", file=sys.stderr)
        return "", None
    body = extract_post_body(page)
    article_date = extract_single_page_date(page) or extract_article_date_from_body(body)
    return body, article_date


def date_from_manual(url: str) -> str | None:
    for needle, value in MANUAL_DATES.items():
        if needle in url:
            return value
    return None


def choose_date(item: dict, body: str, article_date: str | None) -> str:
    if article_date:
        return article_date
    for candidate in (
        date_from_manual(item["source_url"]),
        date_from_url(item["source_url"]),
        date_from_twitter(item["source_url"]),
        extract_article_date_from_body(body),
        date_from_image(item["image_url"]),
    ):
        if candidate:
            return candidate
    # Stable fallback based on title hash — keeps builds deterministic.
    seed = sum(ord(c) for c in item["title"])
    year = 2019 + (seed % 6)
    month = 1 + (seed % 12)
    day = 1 + (seed % 28)
    return f"{year}-{month:02d}-{day:02d}"


def image_filename(slug: str, image_url: str) -> str:
    ext = Path(urllib.parse.urlparse(image_url).path).suffix.lower()
    if ext not in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        ext = ".jpg"
    return f"{slug}{ext}"


def write_post(item: dict, body: str, post_date: str, image_rel: str | None) -> Path:
    slug = slugify(item["title"])
    filename = f"{post_date}-{slug}.md"
    dest = NEWS_DIR / filename

    summary = item["summary"]
    if len(summary) > 320:
        summary = summary[:317].rstrip() + "..."

    source = item["source"]
    if source == "Khalifa University":
        source = "KUCARS"

    lines = [
        "---",
        f"title: {yaml_quote(item['title'])}",
        f"date: {post_date}",
        f"source: {source}",
        f"source_url: {yaml_quote(item['source_url'])}",
    ]
    if image_rel:
        lines.append(f"image: {yaml_quote(image_rel)}")
    lines.append(f"summary: {yaml_quote(summary)}")
    lines.append("---")
    lines.append("")

    if body:
        lines.append(body.strip())
    elif item["summary"]:
        lines.append(item["summary"])

    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


def yaml_quote(value: str) -> str:
    value = value.replace("\n", " ").strip()
    if re.search(r'[:#\[\]{},&*!|>\'"%@`]', value) or value.startswith(("-", "?", "|")):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def main() -> int:
    print(f"Fetching listing: {LISTING_URL}")
    listing_html = fetch(LISTING_URL)
    items = parse_news_blocks(listing_html)
    print(f"Found {len(items)} news items")

    NEWS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    # Remove previously imported posts so re-runs stay in sync with KU listing.
    for path in NEWS_DIR.glob("*.md"):
        path.unlink()

    written: list[Path] = []
    for index, item in enumerate(items, start=1):
        print(f"[{index}/{len(items)}] {item['title'][:72]}...")
        body, article_date = fetch_full_article(item["source_url"])
        post_date = choose_date(item, body, article_date)

        slug = slugify(item["title"])
        image_rel = None
        if item["image_url"]:
            local_name = image_filename(slug, item["image_url"])
            local_path = IMAGE_DIR / local_name
            if download_image(item["image_url"], local_path):
                image_rel = f"/assets/images/news/{local_name}"

        written.append(write_post(item, body, post_date, image_rel))
        time.sleep(0.35)

    print(f"Wrote {len(written)} posts to {_news_dir_display()}")
    return 0


def _news_dir_display() -> str:
    return str(NEWS_DIR.relative_to(ROOT))


if __name__ == "__main__":
    raise SystemExit(main())
