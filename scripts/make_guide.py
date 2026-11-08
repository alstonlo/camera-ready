import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "camera-ready"
RULES = SKILL / "references" / "rules"
GUIDE = SKILL / "references" / "guide.md"
TEMPLATE = ROOT / "scripts" / "guide.template.md"

SLOT = re.compile(r"^\{\{([a-z0-9-]+/[a-z0-9-]+)\}\}$", flags=re.M)
LINK = re.compile(r"\]\(([^)\s]+)\)")
ANCHOR_LINK = re.compile(r"guide\.md#([\w-]+)")
RULE_LINK = re.compile(r"\brules/([a-z0-9-]+/[a-z0-9-]+)\.md\)")
PARTS = ["## Details", "## Examples"]


def fail(msg: str):
    sys.exit(f"make_guide: {msg}")


def read_rule(name: str, text: str) -> tuple[str, str]:
    title, _, body = text.partition("\n")
    if not title.startswith("# "):
        fail(f"{name}.md: the first line must be '# <rule name>'")

    heads = re.findall(r"^#+ .*$", body, flags=re.M)
    if heads != [h for h in PARTS if h in heads]:
        fail(f"{name}.md: the only headings allowed are {PARTS}, in that order")

    summary = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0].strip()
    if not summary:
        fail(f"{name}.md: the rule text after the title is empty")
    return title[2:].strip(), summary


def relink(target: str, name: str, names: set[str]) -> str:
    if target.startswith(("http://", "https://")):
        return target

    path = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
    if path.removesuffix(".md") not in names:
        fail(f"{name}.md: link to {target} is neither a URL nor a rule page")
    return f"rules/{path}"


def render(name: str, title: str, summary: str, names: set[str]) -> str:
    summary = LINK.sub(lambda m: f"]({relink(m[1], name, names)})", summary)
    lead = f"**[{title}](rules/{name}.md).**"
    if re.match(r"[-*] |\d+\. |\|", summary):
        return f"{lead}\n\n{summary}"
    return f"{lead} {summary}"


def slug(heading: str) -> str:
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def build() -> str:
    pages = {
        p.relative_to(RULES).with_suffix("").as_posix(): p.read_text()
        for p in sorted(RULES.glob("*/*.md"))
    }
    rules = {name: read_rule(name, text) for name, text in pages.items()}
    names = set(rules)
    for name, text in pages.items():
        for target in LINK.findall(text):
            relink(target, name, names)

    template = TEMPLATE.read_text()
    slots = SLOT.findall(template)

    unknown = sorted(set(slots) - names)
    unused = sorted(names - set(slots))
    repeated = sorted({s for s in slots if slots.count(s) > 1})
    if unknown or unused or repeated:
        fail(f"template slots: unknown {unknown}, missing {unused}, repeated {repeated}")

    guide = SLOT.sub(lambda m: render(m[1], *rules[m[1]], names), template)

    anchors = {slug(h) for h in re.findall(r"^#+ (.*)$", guide, flags=re.M)}
    anchors |= set(re.findall(r'<a id="([\w-]+)"></a>', guide))
    sources = {
        "SKILL.md": (SKILL / "SKILL.md").read_text(),
        "guide.md": re.sub(r"\]\(#", "](guide.md#", guide),
    }
    for page, text in sources.items():
        broken = sorted(set(ANCHOR_LINK.findall(text)) - anchors)
        if broken:
            fail(f"{page}: links to missing guide headings {broken}")
        missing = sorted(set(RULE_LINK.findall(text)) - names)
        if missing:
            fail(f"{page}: links to missing rule pages {missing}")
    return guide


if __name__ == "__main__":
    GUIDE.write_text(build())
