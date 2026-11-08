import make_guide


def test_guide_is_up_to_date():
    assert make_guide.GUIDE.read_text() == make_guide.build(), (
        "references/guide.md is out of date; run python3 scripts/make_guide.py"
    )
