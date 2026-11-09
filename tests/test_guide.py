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
    ],
)
def test_invalid_pages_fail(text: str):
    with pytest.raises(SystemExit):
        make_guide.read_rule("prose/verbs", text)
