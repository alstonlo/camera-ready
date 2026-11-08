import argparse
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "camera-ready"
RULES = SKILL / "references" / "rules"
GUIDE = SKILL / "references" / "guide.md"
TEMPLATE = ROOT / "scripts" / "guide.template.md"

NOTICE = (
    "<!-- Built by scripts/build_guide.py from scripts/guide.template.md and the rule pages in "
    "rules/. Edit those files, not this one. -->\n\n"
)
SLOT = re.compile(r"^\{\{([a-z0-9-]+/[a-z0-9-]+)\}\}$", flags=re.M)
LINK = re.compile(r"\]\(([^)\s]+)\)")
ANCHOR_LINK = re.compile(r"guide\.md#([\w-]+)")
PARTS = ["## Details", "## Examples"]


def fail(msg: str):
    sys.exit(f"build_guide: {msg}")


def read_rule(path: Path) -> tuple[str, str]:
    title, _, body = path.read_text().partition("\n")
    if not title.startswith("# "):
        fail(f"{path.relative_to(RULES)}: the first line must be '# <rule name>'")

    heads = re.findall(r"^#+ .*$", body, flags=re.M)
    if heads != [h for h in PARTS if h in heads]:
        fail(f"{path.relative_to(RULES)}: the only headings allowed are {PARTS}, in that order")

    summary = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0].strip()
    if not summary:
        fail(f"{path.relative_to(RULES)}: the rule text after the title is empty")
    return title[2:].strip(), summary


def relink(target: str, name: str, names: set[str]) -> str:
    if target.startswith(("http://", "https://")):
        return target

    path, _, anchor = target.partition("#")
    path = posixpath.normpath(posixpath.join("rules", posixpath.dirname(name), path))
    if path == "guide.md" and anchor:
        return f"#{anchor}"
    if path.startswith("rules/") and path.removeprefix("rules/").removesuffix(".md") in names:
        return path
    fail(f"{name}.md: link to {target} is neither a URL, a guide heading, nor a rule page")


def render(name: str, title: str, summary: str, names: set[str]) -> str:
    summary = LINK.sub(lambda m: f"]({relink(m[1], name, names)})", summary)
    lead = f"**[{title}](rules/{name}.md).**"
    if re.match(r"[-*] |\d+\. |\|", summary):
        return f"{lead}\n\n{summary}"
    return f"{lead} {summary}"


def slug(heading: str) -> str:
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def build() -> str:
    paths = sorted(RULES.glob("*/*.md"))
    rules = {p.relative_to(RULES).with_suffix("").as_posix(): read_rule(p) for p in paths}
    names = set(rules)
    template = TEMPLATE.read_text()
    slots = SLOT.findall(template)

    unknown = sorted(set(slots) - names)
    unused = sorted(names - set(slots))
    repeated = sorted({s for s in slots if slots.count(s) > 1})
    if unknown or unused or repeated:
        fail(f"template slots: unknown {unknown}, missing {unused}, repeated {repeated}")

    guide = NOTICE + SLOT.sub(lambda m: render(m[1], *rules[m[1]], names), template)

    anchors = {slug(h) for h in re.findall(r"^#+ (.*)$", guide, flags=re.M)}
    anchors |= set(re.findall(r'<a id="([\w-]+)"></a>', guide))
    sources = {p.relative_to(RULES).as_posix(): p.read_text() for p in paths}
    sources["SKILL.md"] = (SKILL / "SKILL.md").read_text()
    sources["guide.md"] = re.sub(r"\]\(#", "](guide.md#", guide)
    for page, text in sources.items():
        broken = sorted(set(ANCHOR_LINK.findall(text)) - anchors)
        if broken:
            fail(f"{page}: links to missing guide headings {broken}")
    return guide


def main():
    parser = argparse.ArgumentParser(description="Build references/guide.md from the rule pages.")
    parser.add_argument("--check", action="store_true", help="fail if guide.md is out of date")
    args = parser.parse_args()

    guide = build()
    if args.check and GUIDE.read_text() != guide:
        fail("references/guide.md is out of date; run python3 scripts/build_guide.py")
    if not args.check:
        GUIDE.write_text(guide)


if __name__ == "__main__":
    main()
