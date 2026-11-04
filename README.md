# seo-meta-audit-skill

Audit one page's SEO basics — title, meta description, canonical, Open Graph, and H1 structure — and report only what the page actually shows.

[![CI](https://github.com/haiderstudio/seo-meta-audit-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/haiderstudio/seo-meta-audit-skill/actions/workflows/ci.yml) [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](LICENSE)

## What it does

When an AI coding agent loads this skill, it audits a single HTML
page, in a fixed order:

- Title — present, with its exact length reported.
- Meta description — present, with its exact length reported.
- Canonical — present, and an absolute URL.
- Open Graph — `og:title`, `og:description`, and `og:image`,
  each reported present or missing, one by one.
- H1 structure — exactly one `<h1>` is the pass, with the exact
  count and texts found.
- Image alt gaps — every image counted, every image missing an
  `alt` listed by its `src`.

Every line carries the page's own value as evidence. Lengths
over 60 characters (title) or 160 characters (description) are
flagged as likely to be cut off in results, never as a proven
ranking loss.

## What it does NOT do

- It does not crawl a site, check rankings, or predict traffic
  or clicks. It audits tags on one page, nothing more.
- It does not work from a summary, a screenshot, or a memory of
  a page. No HTML, no audit.
- It does not invent a title, a description, a canonical, an
  Open Graph tag, an H1, or an alt value the page does not show.
- It does not edit the page, commit, or deploy by itself.
  Auditing is the whole job; the user fixes and publishes.

## Who it is for

Site owners and developers who want a fast, checkable answer
for one page — what its head tags actually say, what is missing,
and what to fix first — without a full-site suite or a made-up
SEO score.

## Install

This skill follows the open Agent Skills format: a folder with a
`SKILL.md` file.

**Claude Code / Codex / Gemini CLI (project level):**

```bash
mkdir -p .agents/skills
cp -r skills/seo-meta-audit .agents/skills/seo-meta-audit
```

## Usage

Ask the agent to audit one page, giving its exact file or URL.
The agent follows `skills/seo-meta-audit/SKILL.md` and returns
one line per check with its evidence, a fix list naming only
the failed checks, and anything deliberately left out.

## Example

From `examples/sample-page.html` (one H1, a canonical, two
images, one missing alt), the skill produces
`examples/sample-audit.md`:

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

## How it is tested

```bash
python3 tests/test_skill.py
```

The tests check that `SKILL.md` has valid `name` and `description`
frontmatter, the required workflow sections, and no unfinished
placeholder content; and that the sample audit matches the
sample page exactly — title and description values and lengths,
canonical, all three Open Graph tags, the single H1, and the
one alt gap — with no invented values.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and pull requests
are welcome; please keep examples real and checkable.

## Licence

MIT — see [LICENSE](LICENSE). This is original work.
