# Changelog

This project follows [Semantic Versioning](https://semver.org/). The version is set in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json); bump it with every release so that installed plugins pick up the update.

## Unreleased

- Split the writing guide into one page per rule in `skills/camera-ready/references/rules/`, one subfolder per section. The script `scripts/make_guide.py` builds `references/guide.md` from these pages. The rules are unchanged; the Bad/Good examples moved from the guide to the rule pages.

## 0.2.0 (2026-11-04)

- Incorporated guidance from [Clark et al. (2026)](https://arxiv.org/abs/2610.29162).

## 0.1.0 (2026-10-20)

- Initial release.
