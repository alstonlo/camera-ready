import make_guide
import pytest

PAIR = "- Bad: We perform an evaluation of the model.\n- Good: We evaluate the model."


def page(*sections: str) -> str:
    return "\n\n".join(["# Use verbs for actions", "Write actions as verbs.", *sections]) + "\n"


def test_guide_is_up_to_date():
    assert make_guide.GUIDE.read_text() == make_guide.build(), (
        "references/guide.md is out of date; run python3 scripts/make_guide.py"
    )


@pytest.mark.parametrize(
    "text",
    [
        page("## Examples", PAIR),
        page("## Details", "More cases.", "## Examples", PAIR),
        page("## Examples", "In a Methods section:", PAIR, PAIR),
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
        page("## Details", "More cases."),
        page("## Examples", "## Details", "More cases."),
        page("## Details", "", "## Examples", PAIR),
        page("## Examples", "- Bad: We perform an evaluation."),
        page("## Examples", "- Good: We evaluate.\n- Bad: We perform an evaluation."),
        page("## Examples", "- Bad: A.\n- Bad: B.\n- Good: C."),
        page("## Examples", "- Bad: A.\nContext.\n- Good: B."),
        page("## Examples", PAIR, "Trailing context."),
        page("## Examples", "- Bad caption: A.\n- Good caption: B."),
        page("## Examples", "- Bad: Same.\n- Good: Same."),
    ],
)
def test_invalid_pages_fail(text: str):
    with pytest.raises(SystemExit):
        make_guide.read_rule("prose/verbs", text)
