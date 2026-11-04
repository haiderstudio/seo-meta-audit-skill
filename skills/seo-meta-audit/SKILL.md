---
name: seo-meta-audit
description: Audit one HTML page's SEO basics — title, meta description, canonical, Open Graph, and H1 structure. Use when a user asks to check a single page's SEO meta tags, or to find what a page's head actually shows versus what it is missing. Reports only what the page itself shows, never a ranking or a guess about search results.
---

# seo-meta-audit

Audit one page, fast, honestly: what its head tags actually say,
what is missing, and what to fix first — with the page's own values
as evidence for every line.

## When to use this skill

Use it when the user asks to:
- Audit a single HTML page's SEO basics.
- Check a page's title, meta description, canonical URL, Open
  Graph tags, or H1 structure.
- Find image alt gaps on one page.
- Compare what a page claims in its head against what it shows.

## When NOT to use it

- Do not use it as a full-site SEO suite, a crawler, or a keyword
  rank checker. Those are separate jobs; this skill covers one
  page only.
- Do not use it to predict a search ranking, a click rate, or
  traffic. It reports tags, not results.
- Do not use it from a summary, a screenshot, or a memory of a
  page. Read the page's actual HTML first.
- Do not use it as a sitemap or robots.txt auditor. That is a
  separate job with its own rules.

## Workflow

### 1. Read the one page's actual HTML

1. Confirm the exact page with the user: one file or one URL.
   A vague target ("the site", "our pages") is not a target —
   ask for the one page, do not guess.
2. Read its `<head>` and its body headings and images in full.
   A rendered preview is not the HTML; check the source.
3. Record every value exactly as written, including empty ones.
   An empty description is a finding, not a blank to fill in.

### 2. Run only these checks, in this order

- `Title` — present, and not empty. Length is reported as a
  number; a title over 60 characters is flagged as likely to be
  cut off in results, not as a proven ranking loss.
- `Meta description` — present, and not empty. Length is
  reported as a number; a description over 160 characters is
  flagged as likely to be cut off, not as a proven ranking loss.
- `Canonical` — present, and an absolute URL. A relative
  canonical, or a canonical pointing at a different page, is
  flagged with the exact value found.
- `Open Graph` — `og:title`, `og:description`, and `og:image`
  each present or missing, reported one by one. A missing tag is
  a finding; a present tag is quoted, never rewritten.
- `H1 structure` — exactly one `<h1>` is the pass. Zero H1s, or
  two or more, is flagged with the exact count and the H1 texts
  found.
- `Image alt gaps` — every `<img>` counted, and every image
  without an `alt` attribute (or with an empty `alt`) listed by
  its `src`. Decorative images still get listed; the user decides
  which ones are decorative, the skill does not guess.

### 3. Report in this fixed format

1. The page audited, by its exact file or URL.
2. One line per check, in the order above, marked PASS or FAIL,
   with the actual value found as evidence.
3. The fix list, in the same order, naming only the failed
   checks — nothing else, no extra SEO advice.
4. Anything deliberately left out: checks not run (a live fetch,
   a ranking check, a full-site crawl), listed by name, with why
   they were left out.

## Good examples

A single page with one H1, a canonical, and one alt gap (from
the sample page in `examples/sample-page.html`):

```markdown
Page: examples/sample-page.html

- Title: PASS — "Example Tool — Fast CSV to Markdown" (35 characters)
- Meta description: PASS — "Convert CSV to Markdown tables in seconds, free, no sign-up." (60 characters)
- Canonical: PASS — https://example.com/tool
- Open Graph: PASS — og:title, og:description, og:image all present
- H1 structure: PASS — 1 H1: "Convert CSV to Markdown tables"
- Image alt gaps: FAIL — 1 of 2 images missing alt: hero.png

Fix first: add alt text to hero.png.
```

A missing description is reported as missing, not invented:

```markdown
- Meta description: FAIL — missing (no meta description tag found)
```

## Bad examples (do not write like this)

> `Title: good, description: good, SEO: 95/100`

No values, no evidence, and a score nobody can check.

> `Meta description: "The best tool on the internet for everything"`

A description the page does not contain. If the page does not
show it, the audit does not say it.

> `Ranking: this page will rank #1 for its keyword`

A prediction this skill cannot make. It audits tags, not
rankings, and never promises a position.

## Output rules

- Output one audit per page, in its own code block.
- Every line in the audit must trace to the page's HTML. If it
  cannot be traced, leave it out and list it as deliberately
  omitted.
- Never invent a title, a description, a canonical, an Open
  Graph tag, an H1, or an alt value the page does not show.
- Never claim a ranking, traffic, or click result unless the
  user actually shows it from a separate source.
- Never edit the page, commit, or deploy by itself. Auditing is
  the whole job; the user fixes and publishes, after reading it.

## Limits and safety rules

- This skill reads one page's HTML only. It sends nothing
  anywhere, edits no file, and changes no ranking.
- It does not crawl a site, fetch live search results, or check
  competitors. A single-page audit is the whole scope.
- Local fixture pages (see `examples/sample-page.html`) cannot
  prove a live ranking, a live URL, or a live result. A
  walkthrough run on fixtures marks live checks as deliberately
  omitted, exactly as the sample audit does.
