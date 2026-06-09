# KUCARS Website

Jekyll site for the KU Center for Autonomous Robotic Systems.

**Live site:** [https://kucars.ae](https://kucars.ae)  
**Repository:** [github.com/kucars/kucars.github.io](https://github.com/kucars/kucars.github.io)

## How the site is organized

| What | Where |
|------|--------|
| Home page | `index.md` |
| Static pages (About, People, …) | `pages/*.md` |
| News posts | `_news/*.md` |
| Research projects | `_projects/*.md` |
| Lists & site config data | `_data/*.yml` |
| HTML templates | `_layouts/`, `_includes/` |
| CSS, JS, images | `assets/` |

Structured content (people, publications, facilities, sponsors, themes) lives in YAML so it is easy to edit without touching HTML.

## Run locally

```bash
bundle install
bundle exec jekyll serve --livereload
```

Open [http://127.0.0.1:4000](http://127.0.0.1:4000).

To preview with production URL settings:

```bash
JEKYLL_ENV=production bundle exec jekyll serve
```

## Publish changes

1. Edit the relevant file(s) below.
2. Commit and push to `main`.
3. GitHub Actions builds and deploys automatically (see `.github/workflows/jekyll.yml`).

Check deployment status under **Actions** in the repository.

---

## Update people

**File:** `_data/people.yml`

People are grouped by section. Each group has a `title` and a `people` list:

```yaml
faculty:
  title: Faculty
  people:
    - name: Dr. Example Name
      profile: https://www.ku.ac.ae/college-people/example-name
      role: Associate Professor
      unit: Computer Science
      photo: /assets/images/people/example.jpg   # optional
```

**Groups used on the People page:** `leadership`, `faculty`, `researchers`, `students`, `alumni`, `advisory_committee`

**To add someone:** append an entry under the right group in `_data/people.yml`.

**To add a new group:** create a new top-level key in `people.yml`, then add its key to `people_groups` in `pages/people.md` and to the `{% include people-list.html %}` call on that page.

Fields:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | Display name |
| `profile` | no | Link to KU profile (opens in new tab) |
| `role` | no | e.g. Postdoctoral Fellow |
| `unit` | no | Department or lab |
| `photo` | no | Path under `assets/images/` |

---

## Update research projects

**Folder:** `_projects/`

Each project is one Markdown file. The filename becomes the URL slug:  
`_projects/msap.md` → `/research/projects/msap/`

**Front matter example:**

```yaml
---
title: MSAP
theme: autonomous-vehicles
order: 1
subtitle: Short project tagline
summary: One-line description shown in project listings.
team:
  pi:
    name: Principal Investigator Name
    role: Full Professor
    dept: EECS
  co_investigators:
    - name: Co-PI Name
      email: name@ku.ac.ae
sponsors:
  - Sponsor Name
collaborators:
  - Partner Name
images:
  - src: /assets/images/research/autonomous-vehicles/example.png
    caption: Optional caption
video: "https://www.youtube.com/embed/VIDEO_ID"
---
```

Body text below the front matter is the full project description (Markdown).

**`theme` must match a theme slug** in `_data/research/themes.yml`:

- `autonomous-vehicles`
- `aerial-robotics`
- `marine-robotics`
- `industrial-robotics`

**`order`** controls sort order within a theme (lower numbers first).

Put images in `assets/images/research/<theme>/`.

---

## Update research themes (labs)

Theme metadata is in **`_data/research/themes.yml`** (title, description, focus areas, hero image, order).

Theme landing pages with extra content are in **`pages/research/<slug>.md`**, for example:

```yaml
---
title: Autonomous Vehicles Lab
layout: research-theme
theme_slug: autonomous-vehicles
permalink: /research/autonomous-vehicles/
---
```

The `theme_slug` must match the `slug` in `themes.yml`. Add Markdown below the front matter for theme-specific content.

---

## Update news

**Folder:** `_news/`

Create a new file named `YYYY-MM-DD-short-slug.md`:

```yaml
---
title: Article headline
date: 2026-01-20
source: Publication or outlet name
source_url: "https://example.com/original-article"
image: /assets/images/news/my-image.jpg
summary: Short excerpt for listings and SEO.
---

Full article body in Markdown.
```

Add the image to `assets/images/news/`. If no image is set, the site uses the default from `_data/center.yml` (`news_default_image`).

**Bulk import from KU:** optional script (requires network):

```bash
python3 scripts/import_ku_news.py
```

---

## Update publications

**File:** `_data/publications.yml`

Two sections: `patents` and `publications`.

**Patent entry:**

```yaml
- title: Patent title
  authors: Author One, Author Two
  status: Submitted for filing
  year: 2024
  reference: KU file no. 2024-001
```

**Publication entry:**

```yaml
- citation: >-
    Full bibliographic citation as a single string.
  doi: https://doi.org/10.xxxx/xxxxx
  year: 2024
```

Add new items at the top of the relevant list to show them first (or reorder as needed).

---

## Update facilities

**File:** `_data/facilities.yml`

```yaml
- name: Lab display name
  location: Room code or building
  theme: Theme 1 Lab
  research_theme: autonomous-vehicles
  description: Short lab description.
  image: /assets/images/facilities/example.png
```

`research_theme` links the card to `/research/<slug>/`. The facilities grid is rendered by `_includes/facilities.html` on `pages/facilities.md`.

---

## Update sponsors & partnerships

**File:** `_data/sponsors.yml`

- `approach` — bullet list for the partnership model section.
- `themes` — theme-level partners; each theme links to a research lab via `research_theme`.
- `external_sponsors` — simple name list (if used elsewhere).

```yaml
themes:
  - title: Theme 1
    research_theme: autonomous-vehicles
    partners:
      - name: Partner Organization
        summary: Short description of the collaboration.
```

---

## Update site-wide content (home, header, navigation)

| Content | File |
|---------|------|
| Center name, logos, home metrics, teasers | `_data/center.yml` |
| Main navigation | `_data/navigation.yml` |
| Home hero banner rotation | `_data/banners.yml` + images in `assets/images/banners/` |
| About page intro | `pages/about.md` |
| Collaborators list | `_data/research/collaborators.yml` |

**Logos** live in `assets/images/` (`ku-logo.png`, `ku-wordmark.png`, etc.). Paths are referenced from `center.yml`.

**Custom domain:** `CNAME` contains `kucars.ae`. Site URL is set in `_config.yml` (`url: "https://kucars.ae"`).

---

## Images

| Use | Location |
|-----|----------|
| Logos & branding | `assets/images/` |
| Home hero banners | `assets/images/banners/` |
| News | `assets/images/news/` |
| Facilities | `assets/images/facilities/` |
| Research / projects | `assets/images/research/<theme>/` |

Use site-root paths in YAML and Markdown, e.g. `/assets/images/news/example.jpg` (leading slash, no `assets` in the repo path when editing files).

Prefer `.jpg` or `.png`. Keep file sizes reasonable for web (hero images ~1200–2000 px wide).

---

## Optional import scripts

Scripts in `scripts/` can pull content from the legacy KU site. They are **not** run automatically on deploy.

```bash
# Import news posts from ku.ac.ae into _news/
python3 scripts/import_ku_news.py

# Import research themes/projects from ku.ac.ae
python3 scripts/import_ku_research.py

# Regenerate _projects/*.md from scripts/generate_projects.py data
python3 scripts/generate_projects.py
```

Review imported output before committing — manual edits in `_projects/` and `_news/` may be overwritten if you re-run importers.

---

## Project structure (for developers)

```
├── _config.yml          # Site settings, collections, defaults
├── _data/               # YAML content
├── _includes/           # Reusable HTML fragments
├── _layouts/            # Page layouts
├── _news/               # News collection
├── _projects/           # Research project collection
├── assets/css/site.css  # All styles
├── assets/js/           # JavaScript
├── assets/images/       # Media
├── pages/               # Top-level pages & research theme pages
├── index.md             # Home page
└── .github/workflows/   # GitHub Pages deployment
```

**Collections** (defined in `_config.yml`):

- `news` → `/news/:year/:month/:day/:title/`
- `projects` → `/research/projects/:name/`
- `pages` → `/:path/`

---

## Troubleshooting

| Problem | Check |
|---------|--------|
| Site not updating after push | GitHub **Actions** tab — workflow must succeed |
| Broken styles on live site | `_config.yml` `url` / `baseurl`; rebuild via push to `main` |
| New project not listed | `theme` slug matches `themes.yml`; `order` field set |
| Person not on People page | Entry is under correct group in `people.yml` and group is listed in `pages/people.md` |
| Image missing | Path starts with `/assets/...` and file exists in `assets/images/` |

For local build errors, run `bundle install` and `bundle exec jekyll build` to see the full error message.
