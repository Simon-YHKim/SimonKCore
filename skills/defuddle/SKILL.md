---
name: defuddle
description: >
  Use when the user provides a URL to read, fetch, or analyze — online documentation, articles, blog posts, or any standard web page. Triggers on "이 링크 정리해줘", "이 페이지 읽어줘", "본문만 추출해줘", "read this URL", "extract article", "fetch this page", "clean markdown from URL". Produces clean markdown extracted via the Defuddle CLI, removing navigation and clutter to save tokens. Use instead of WebFetch for HTML pages; do NOT use for URLs ending in .md, which are already markdown.
version: 1.0.0
---

# Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: `npm install -g defuddle`

## Usage

Always use `--md` for markdown output:

```bash
defuddle parse <url> --md
```

Save to file:

```bash
defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
