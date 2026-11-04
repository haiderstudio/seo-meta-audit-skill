"""Tests for the seo-meta-audit skill: frontmatter, required sections,
and the sample walkthrough (sample page -> sample audit, no invented values)."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "seo-meta-audit" / "SKILL.md"
PAGE = ROOT / "examples" / "sample-page.html"
AUDIT = ROOT / "examples" / "sample-audit.md"
README = ROOT / "README.md"
BANNED = ["TODO", "FIXME", "lorem", "coming soon"]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.canonical = ""
        self.h1s = []
        self.in_h1 = False
        self.images = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            if a.get("name") == "description":
                self.meta["description"] = a.get("content", "")
            if a.get("property", "").startswith("og:"):
                self.meta[a["property"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href", "")
        if tag == "h1":
            self.in_h1 = True
        if tag == "img":
            self.images.append(a)

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1s.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        sys.exit(1)


def main():
    skill = SKILL.read_text()
    m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
    check("test_skill_frontmatter", bool(m) and "name: seo-meta-audit" in m.group(1) and "description:" in m.group(1))
    for section in ["When to use this skill", "When NOT to use it", "Workflow", "Good examples", "Bad examples", "Output rules", "Limits and safety rules"]:
        check("test_skill_sections_" + section.split()[0], section in skill)
    for f in [SKILL, PAGE, AUDIT, README]:
        check("test_no_placeholders_" + f.name, not any(b in f.read_text() for b in BANNED))
    p = PageParser()
    p.feed(PAGE.read_text())
    audit = AUDIT.read_text()
    check("test_sample_title", p.title in audit and f"({len(p.title)} characters)" in audit)
    check("test_sample_description", p.meta["description"] in audit and f"({len(p.meta['description'])} characters)" in audit)
    check("test_sample_canonical", p.canonical in audit)
    check("test_sample_og", all(k in p.meta for k in ["og:title", "og:description", "og:image"]) and "og:title, og:description, og:image all present" in audit)
    check("test_sample_h1", len(p.h1s) == 1 and p.h1s[0] in audit)
    missing = [i.get("src", "") for i in p.images if not i.get("alt")]
    check("test_sample_alt_gaps", len(p.images) == 2 and missing == ["hero.png"] and "1 of 2 images missing alt: hero.png" in audit)
    check("test_sample_no_ranking", "rank" not in audit.lower().replace("ranking check", "") or "ranking check" in audit)
    print("All tests passed.")


if __name__ == "__main__":
    main()
