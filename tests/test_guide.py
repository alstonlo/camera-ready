import build_guide


def test_guide_is_up_to_date():
    assert build_guide.GUIDE.read_text() == build_guide.build(), (
        "references/guide.md is out of date; run python3 scripts/build_guide.py"
    )
