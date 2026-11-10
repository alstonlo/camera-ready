import make_guide
import pytest

PAIR = "> **Before.** We perform an evaluation of the model.\n\n> **After.** We evaluate the model."
LABEL = "**Edit 1.**\n\n"
EX1 = LABEL + PAIR


def page(*sections: str) -> str:
    return "\n\n".join(["# Use verbs for actions", "Write actions as verbs.", *sections]) + "\n"


def test_guide_is_up_to_date():
    assert make_guide.GUIDE.read_text() == make_guide.build(), (
        "references/guide.md is out of date; run python3 scripts/make_guide.py"
    )


@pytest.mark.parametrize(
    "text",
    [
        page("## Details", "More cases.", "## Examples", EX1),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "**Edit 1.** Suppose this is a Methods section.\n\n" + PAIR,
            "A verb names the action directly.",
            "**Edit 2.**\n\n> **Before.** We list:\n> 1. A.\n>\n> Then B.",
            "> **After.** We list:\n> - A.\n\nWhy.",
        ),
        page("## Details", "```python\n# A comment, not a heading.\n```", "## Examples", EX1),
        page(
            "## Details", "More.", "## Examples", LABEL + "> **Before.** We evaluate.\n\nFlag it."
        ),
    ],
)
def test_valid_pages_render_only_title_and_summary(text: str):
    assert make_guide.read_rule("prose/verbs", text) == (
        "Use verbs for actions",
        "Write actions as verbs.",
    )


@pytest.mark.parametrize(
    "text",
    [
        page(),
        page("## Examples", EX1),
        "# Use verbs for actions\n\nWrite actions as verbs (see Details).\n\n## Details\n\nMore.\n\n"
        "## Examples\n\n" + EX1,
        page("## Details", "More cases."),
        page("## Examples", "## Details", "More cases."),
        page("## Details", "", "## Examples", EX1),
        page("## Details", "More cases.", "## Examples", LABEL + "> **Before.** We evaluate."),
        page("## Details", "More cases.", "## Examples", PAIR),
        page(
            "## Details", "More cases.", "## Examples", LABEL + "> **Before.**\n\n> **After.** B."
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "**Edit 1.** Before:\n\n" + PAIR.replace("**Before.** ", ""),
        ),
        page("## Details", "More cases.", "## Examples", "**Edit 2.**\n\n" + PAIR),
        page("## Details", "More cases.", "## Examples", "**Example 1.**\n\n" + PAIR),
        page("## Details", "More cases.", "## Examples", EX1, "**Edit 2.** Trailing."),
        page("## Details", "More cases.", "## Examples", EX1, "Why.", "More why."),
        page("## Details", "More cases.", "## Examples", EX1, "> A stray quote."),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            LABEL + "> **After.** A.\n\n> **Before.** B.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            LABEL + "> **Before.** A.\n\n> **Before.** B.\n\n> **After.** C.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            LABEL + "> **Before.** Same.\n\n> **After.** Same.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            LABEL + "> **Before.** A.\n>\n> **After.** B.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            LABEL + "> **Before.**\n>\n\n> **After.** B.",
        ),
        "# \n\nWrite actions as verbs.\n\n## Details\n\nMore.\n\n## Examples\n\n" + EX1,
    ],
)
def test_invalid_pages_fail(text: str):
    with pytest.raises(SystemExit):
        make_guide.read_rule("prose/verbs", text)


def test_fenced_headings_stay_in_their_section():
    summary = "Keep this code:\n\n```markdown\n## A sample heading\nKeep this line.\n```"
    text = f"# Use verbs for actions\n\n{summary}\n\n## Details\n\nMore.\n\n## Examples\n\n{EX1}\n"
    assert make_guide.read_rule("prose/verbs", text) == ("Use verbs for actions", summary)


def test_relink_resolves_relative_rule_links():
    assert make_guide.relink("../prose/verbs.md", "story/titles", {"prose/verbs"}) == (
        "rules/prose/verbs.md"
    )


@pytest.mark.parametrize("target", ["verbs", "nope.md", 'verbs.md "Title"', "verbs.md#x"])
def test_relink_rejects_targets_that_are_not_rule_pages(target: str):
    with pytest.raises(SystemExit):
        make_guide.relink(target, "prose/titles", {"prose/verbs"})


@pytest.mark.parametrize(
    ("summary", "sep"),
    [("Write verbs.", " "), ("- Write verbs.", "\n\n"), ("> Write verbs.", "\n\n")],
)
def test_render_puts_block_summaries_on_their_own_line(summary: str, sep: str):
    lead = "**[Use verbs](rules/prose/verbs.md).**"
    assert make_guide.render("prose/verbs", "Use verbs", summary, set()) == lead + sep + summary


TEMPLATE = "# Guide\n\n```markdown\n## Details\n```\n\n## Prose\n\n{{prose/verbs}}\n"


@pytest.fixture
def repo(tmp_path, monkeypatch):
    skill = tmp_path / "skill"
    rules = skill / "references" / "rules"
    (rules / "prose").mkdir(parents=True)
    (rules / "prose" / "verbs.md").write_text(page("## Details", "More cases.", "## Examples", EX1))
    monkeypatch.setattr(make_guide, "SKILL", skill)
    monkeypatch.setattr(make_guide, "RULES", rules)
    monkeypatch.setattr(make_guide, "GUIDE", skill / "references" / "guide.md")
    monkeypatch.setattr(make_guide, "TEMPLATE", tmp_path / "guide.template.md")
    return skill


def test_build_accepts_valid_links(repo):
    (repo / "SKILL.md").write_text(
        "Read the [guide](references/guide.md), [prose](references/guide.md#prose), "
        '[verbs](references/rules/prose/verbs.md), and [edit](#edit).\n\n<a id="edit"></a>\n'
    )
    make_guide.TEMPLATE.write_text(TEMPLATE + "\nSee [prose](#prose).\n")
    assert "**[Use verbs for actions](rules/prose/verbs.md).** Write" in make_guide.build()


@pytest.mark.parametrize(
    ("skill", "extra"),
    [
        ("[x](references/guide.md#nope)", ""),
        ("[x](references/rule/prose/verbs.md)", ""),
        ("[x](references/rules/prose/verbs)", ""),
        ("[x](#nope)", ""),
        ("", "See [details](#details).\n"),
        ("", "See [nouns](rules/prose/nouns.md).\n"),
    ],
)
def test_build_rejects_broken_links(repo, skill: str, extra: str):
    (repo / "SKILL.md").write_text(skill + "\n")
    make_guide.TEMPLATE.write_text(TEMPLATE + "\n" + extra)
    with pytest.raises(SystemExit):
        make_guide.build()


def test_build_rejects_pages_outside_section_folders(repo):
    (repo / "SKILL.md").write_text("\n")
    make_guide.TEMPLATE.write_text(TEMPLATE)
    (make_guide.RULES / "stray.md").write_text("# Stray\n")
    with pytest.raises(SystemExit):
        make_guide.build()
