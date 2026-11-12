# Changelog

This project follows [Semantic Versioning](https://semver.org/). The version is set in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json); bump it with every release so that installed plugins pick up the update.

## 0.4.0 (2026-11-11)

- Merged the lite and full modes into a single workflow. The skill now saves a copy of each file and its audit notes in `.camera-ready/`, checks its edits against the saved copy, and proposes claim changes in its report instead of making them, unless asked.
- Renamed the guide sections Cutting to Cuts and Deslopping to AI patterns.
- Improved the writing of the README and the skill instructions.

## 0.3.0 (2026-11-08)

- Split the writing guide into one page per rule.
- Incorporated guidance from writing textbooks.
- Added examples to every rule page.

## 0.2.0 (2026-11-04)

- Incorporated guidance from [Clark et al. (2026)](https://arxiv.org/abs/2610.29162).

## 0.1.0 (2026-10-20)

- Initial release.
