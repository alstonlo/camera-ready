import make_guide
import pytest

PAIR = "> **Bad.** We perform an evaluation of the model.\n>\n> **Good.** We evaluate the model."


def page(*sections: str) -> str:
    return "\n\n".join(["# Use verbs for actions", "Write actions as verbs.", *sections]) + "\n"


def test_guide_is_up_to_date():
    assert make_guide.GUIDE.read_text() == make_guide.build(), (
        "references/guide.md is out of date; run python3 scripts/make_guide.py"
    )


@pytest.mark.parametrize(
    "text",
    [
        page("## Details", "More cases.", "## Examples", PAIR),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "> **Context.** In a Methods section.\n>\n" + PAIR,
            PAIR,
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
        page("## Examples", PAIR),
        page("## Details", "More cases."),
        page("## Examples", "## Details", "More cases."),
        page("## Details", "", "## Examples", PAIR),
        page("## Details", "More cases.", "## Examples", "> **Bad.** We perform an evaluation."),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "> **Good.** We evaluate.\n>\n> **Bad.** We perform an evaluation.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "> **Bad.** A.\n>\n> **Bad.** B.\n>\n> **Good.** C.",
        ),
        page(
            "## Details",
            "More cases.",
            "## Examples",
            "> **Bad.** A.\n\nContext.\n\n> **Good.** B.",
        ),
        page("## Details", "More cases.", "## Examples", "In a Methods section.", PAIR),
        page("## Details", "More cases.", "## Examples", PAIR, "> **Context.** Trailing."),
        page(
            "## Details", "More cases.", "## Examples", "> Bad caption: A.\n>\n> Good caption: B."
        ),
        page("## Details", "More cases.", "## Examples", "> **Bad.** Same.\n>\n> **Good.** Same."),
        page("## Details", "More cases.", "## Examples", "- **Bad.** A.\n- **Good.** B."),
        page("## Details", "More cases.", "## Examples", "> **Bad.** A.\n> **Good.** B."),
    ],
)
def test_invalid_pages_fail(text: str):
    with pytest.raises(SystemExit):
        make_guide.read_rule("prose/verbs", text)
