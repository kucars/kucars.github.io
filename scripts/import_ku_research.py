#!/usr/bin/env python3
"""Import KUCARS research content from ku.ac.ae into Jekyll data and _projects."""

from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "_projects"
THEMES_FILE = ROOT / "_data" / "research" / "themes.yml"
IMAGE_ROOT = ROOT / "assets" / "images" / "research"
SOURCE_URL = (
    "https://www.ku.ac.ae/research-centers/"
    "center-for-autonomous-robotic-systems-kucars/research"
)
USER_AGENT = "Mozilla/5.0 (compatible; KUCARS-site-importer/1.0)"

THEME_IMAGE_PREFIXES = {
    "autonomous-vehicles": ("AVLab-fig", "DX2_7444", "DX3_7490"),
    "aerial-robotics": ("ariel-fig",),
    "marine-robotics": ("marine-fig",),
    "industrial-robotics": ("the4-fig",),
}

THEMES = [
    {
        "slug": "autonomous-vehicles",
        "title": "Autonomous Vehicles Lab",
        "short_title": "AVLab",
        "order": 1,
        "theme_number": 1,
        "description": (
            "Autonomous vehicle research for safe operation, smart urban ecosystems, "
            "passenger-centered mobility, V2X-enabled perception, and rigorous decision "
            "making under uncertainty."
        ),
        "questions": [
            "What strategies guarantee safety within autonomous vehicle decision making?",
            "How can multi-agent autonomous vehicles share sensory data, decisions, and uncertainty through V2X?",
            "How can decision-making strategies provide robust safety assurance through theoretical validation?",
        ],
    },
    {
        "slug": "aerial-robotics",
        "title": "Aerial Robotics",
        "short_title": "UAV Systems",
        "order": 2,
        "theme_number": 2,
        "description": (
            "UAV research for surveillance, inspection, sense-and-avoid, GPS-denied navigation, "
            "and operations in critical infrastructure and extreme environments."
        ),
        "questions": [],
    },
    {
        "slug": "marine-robotics",
        "title": "Marine Robotics and Vision",
        "short_title": "VSAP Lab",
        "order": 3,
        "theme_number": 3,
        "description": (
            "Marine robotics research integrates underwater swarms, computer vision, multimodal AI, "
            "mapping, and monitoring for maritime safety and sustainability."
        ),
        "questions": [],
    },
    {
        "slug": "industrial-robotics",
        "title": "Industrial Robotics and Manipulators",
        "short_title": "Manipulation",
        "order": 4,
        "theme_number": 4,
        "description": (
            "Robotic manipulation research covers industrial robotics, compliant mechanisms, "
            "greenhouse automation, and embodied intelligence for physical interaction."
        ),
        "questions": [],
    },
]


def normalize_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/:%")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def fetch(url: str) -> str:
    req = urllib.request.Request(normalize_url(url), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def download_file(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        req = urllib.request.Request(normalize_url(url), headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            dest.write_bytes(resp.read())
        return True
    except (urllib.error.URLError, OSError) as exc:
        print(f"  warning: could not download {url}: {exc}", file=sys.stderr)
        return False


def slugify(text: str, max_len: int = 96) -> str:
    text = html.unescape(text).lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_len].rstrip("-")


def yaml_quote(value: str) -> str:
    value = value.replace("\n", " ").strip()
    if re.search(r'[:#\[\]{},&*!|>\'"%@`]', value) or value.startswith(("-", "?", "|")):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def extract_image_urls(page_html: str) -> list[str]:
    urls = re.findall(
        r'src="(https://www\.ku\.ac\.ae/wp-content/uploads/[^"]+\.(?:jpg|jpeg|png|webp))"',
        page_html,
        re.I,
    )
    seen: set[str] = set()
    ordered: list[str] = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    return ordered


def theme_for_image(filename: str) -> str | None:
    lower = filename.lower()
    for theme_slug, prefixes in THEME_IMAGE_PREFIXES.items():
        for prefix in prefixes:
            if prefix.lower() in lower:
                return theme_slug
    return None


def download_theme_images(page_html: str) -> dict[str, list[str]]:
    downloaded: dict[str, list[str]] = {slug: [] for slug in THEME_IMAGE_PREFIXES}
    for url in extract_image_urls(page_html):
        filename = Path(urllib.parse.urlparse(url).path).name
        theme_slug = theme_for_image(filename)
        if not theme_slug:
            continue
        local_name = filename.lower().replace("ariel-fig1-1", "ariel-fig1")
        dest = IMAGE_ROOT / theme_slug / local_name
        if download_file(url, dest):
            rel = f"/assets/images/research/{theme_slug}/{local_name}"
            downloaded[theme_slug].append(rel)
    for theme_slug in downloaded:
        downloaded[theme_slug].sort()
    return downloaded


def write_themes_yaml(images_by_theme: dict[str, list[str]], force: bool) -> None:
    THEMES_FILE.parent.mkdir(parents=True, exist_ok=True)
    if THEMES_FILE.exists() and not force:
        print(f"Skipping existing {THEMES_FILE.relative_to(ROOT)} (use --force to overwrite)")
        return

    lines: list[str] = []
    for theme in THEMES:
        slug = theme["slug"]
        hero_override = {
            "autonomous-vehicles": "/assets/images/research/autonomous-vehicles/avlab-msap-hero.png",
            "aerial-robotics": "/assets/images/research/aerial-robotics/aerial-robotics-hero.png",
            "industrial-robotics": "/assets/images/research/industrial-robotics/industrial-robotics-hero.png",
        }
        hero = hero_override.get(slug) or images_by_theme.get(slug, [None])[0]
        lines.append(f"- slug: {slug}")
        lines.append(f"  title: {yaml_quote(theme['title'])}")
        lines.append(f"  short_title: {yaml_quote(theme['short_title'])}")
        lines.append(f"  order: {theme['order']}")
        if theme.get("theme_number"):
            lines.append(f"  theme_number: {theme['theme_number']}")
        lines.append(f"  description: {yaml_quote(theme['description'])}")
        if theme["questions"]:
            lines.append("  questions:")
            for question in theme["questions"]:
                lines.append(f"    - {yaml_quote(question)}")
        else:
            lines.append("  questions: []")
        if hero:
            lines.append(f"  hero_image: {yaml_quote(hero)}")
        lines.append("")

    THEMES_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {THEMES_FILE.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite themes.yml even if it already exists",
    )
    parser.add_argument(
        "--images-only",
        action="store_true",
        help="Only download images and update themes.yml",
    )
    args = parser.parse_args()

    print(f"Fetching: {SOURCE_URL}")
    page_html = fetch(SOURCE_URL)

    print("Downloading research images...")
    images_by_theme = download_theme_images(page_html)
    for theme_slug, paths in images_by_theme.items():
        print(f"  {theme_slug}: {len(paths)} images")

    write_themes_yaml(images_by_theme, force=args.force)

    if args.images_only:
        return 0

    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    print(
        "Project markdown files are maintained as curated content in _projects/. "
        "Re-run with --images-only to refresh assets only."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
