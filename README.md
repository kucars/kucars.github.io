# KUCARS Jekyll Site

This is a Jekyll site for an academic research center. The project keeps content separate from the theme:

- Content pages live in `index.md` and `pages/*.md`.
- Editorial content lives in Markdown files, including news posts in `_news/*.md`.
- Structured content that is easier to maintain as tables or lists lives in `_data/*.yml`.
- Theme templates live in `_layouts` and `_includes`.
- Styling lives in `assets/css/site.css`.

## Run Locally

```bash
jekyll serve --livereload
```

Then open `http://127.0.0.1:4000`.
