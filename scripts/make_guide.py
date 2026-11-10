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
LINK = re.compile(r"\]\(([^)]+)\)")
FENCE = re.compile(r"^(?:> ?)?```.*?^(?:> ?)?```", flags=re.M | re.S)
HEAD = re.compile(FENCE.pattern + r"|^(#+ [^\n]*)$", flags=re.M | re.S)
HEADS = ["## Details", "## Examples"]
LABEL = re.compile(r"\*\*Edit (\d+)\.\*\*(?: \S.*)?")
QUOTE = re.compile(r"> \*\*(Before|After)\.\*\*((?: \S.*)?(?:\n>.*)*)")
NOTE = re.compile(r"[^>*\s].*")


def fail(msg: str):
    sys.exit(f"make_guide: {msg}")


def check_examples(name: str, examples: str):
    for i, edit in enumerate(re.split(r"\n\n(?=\*\*Edit )", examples), 1):
        parts = edit.split("\n\n")
        label = LABEL.fullmatch(parts[0])
        quotes = [QUOTE.fullmatch(part) for part in parts[1:3]]
        if not (
            len(parts) in (3, 4)
            and label
            and all(quotes)
            and [m[1] for m in quotes] == ["Before", "After"]
            and all(re.sub(r"^>", "", m[2], flags=re.M).strip() for m in quotes)
            and all(NOTE.fullmatch(part) for part in parts[3:])
        ):
            fail(
                f"{name}.md: each edit must be an '**Edit N.**' line with optional context, "
                "a quote starting '> **Before.**', a quote starting '> **After.**', "
                "and an optional one-paragraph explanation"
            )

        if label[1] != str(i):
            fail(f"{name}.md: edits must be numbered 1, 2, ... in order")
        if quotes[0][2].strip() == quotes[1][2].strip():
            fail(f"{name}.md: an edit's After passage repeats its Before passage")


def read_rule(name: str, text: str) -> tuple[str, str]:
    title, _, body = text.partition("\n")
    if not title.startswith("# ") or not title[2:].strip():
        fail(f"{name}.md: the first line must be '# <rule name>'")

    heads = [m for m in HEAD.finditer(body) if m[1]]
    if [m[1] for m in heads] != HEADS:
        fail(f"{name}.md: the headings must be {HEADS}, in that order")

    bounds = [0, *(i for m in heads for i in m.span()), len(body)]
    summary, *parts = (body[a:b].strip() for a, b in zip(bounds[::2], bounds[1::2]))
    if not summary:
        fail(f"{name}.md: the rule text after the title is empty")
    if re.search(r"\bDetails\b", summary):
        fail(f"{name}.md: the summary must state its rule without pointing to Details")
    if not all(parts):
        fail(f"{name}.md: a section under {HEADS} is empty")

    check_examples(name, parts[-1])
    return title[2:].strip(), summary


def relink(target: str, name: str, names: set[str]) -> str:
    if target.startswith(("http://", "https://")):
        return target

    path = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
    if not path.endswith(".md") or path.removesuffix(".md") not in names:
        fail(f"{name}.md: link to {target} is neither a URL nor a rule page")
    return f"rules/{path}"


def render(name: str, title: str, summary: str, names: set[str]) -> str:
    summary = LINK.sub(lambda m: f"]({relink(m[1], name, names)})", summary)
    lead = f"**[{title}](rules/{name}.md).**"
    if re.match(r"[-*+>] |\d+\. |\||```", summary):
        return f"{lead}\n\n{summary}"
    return f"{lead} {summary}"


def slug(heading: str) -> str:
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def anchors(text: str) -> set[str]:
    text = FENCE.sub("", text)
    heads = {slug(h) for h in re.findall(r"^#+ (.*)$", text, flags=re.M)}
    return heads | set(re.findall(r'<a id="([\w-]+)"></a>', text))


def build() -> str:
    stray = set(RULES.rglob("*.md")) - set(RULES.glob("*/*.md"))
    if stray:
        fail(f"rule pages must sit at rules/<section>/<name>.md: {sorted(map(str, stray))}")
    pages = {
        p.relative_to(RULES).with_suffix("").as_posix(): p.read_text()
        for p in sorted(RULES.glob("*/*.md"))
    }
    rules = {name: read_rule(name, text) for name, text in pages.items()}
    names = set(rules)
    for name, text in pages.items():
        if re.search(r"^\[[^\]]+\]:", text, flags=re.M):
            fail(f"{name}.md: use inline links, not reference-style links")
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

    texts = {SKILL / "SKILL.md": (SKILL / "SKILL.md").read_text(), GUIDE: guide}
    for page, text in texts.items():
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://")):
                continue

            path, _, anchor = target.partition("#")
            dest = (page.parent / path).resolve() if path else page
            if dest not in texts and not dest.is_file():
                fail(f"{page.name}: link to missing file {target}")
            if anchor and anchor not in anchors(texts.get(dest) or dest.read_text()):
                fail(f"{page.name}: link to missing heading {target}")
    return guide


if __name__ == "__main__":
    GUIDE.write_text(build())
