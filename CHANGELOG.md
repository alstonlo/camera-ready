# Changelog

This project follows [Semantic Versioning](https://semver.org/). The version is set in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json); bump it with every release so that installed plugins pick up the update.

## Unreleased

- Split the writing guide into one page per rule in `skills/camera-ready/references/rules/`, one subfolder per section. The script `scripts/make_guide.py` builds `references/guide.md` from these pages, and the rule pages link to one another instead of to headings in the guide. The Bad/Good examples moved from the guide to the rule pages.
- Reorganized the rules so that each page states one rule. Each page's title now states its rule as an instruction. Split pages that covered a whole topic (typography, notation, terminology, figures and tables, paragraphs, uncertainty, voice, and prior work) into one page per rule, and merged pages that repeated each other. Every subsection of the guide contains at least two rules, and prior work moved from Prose to Story. The substance of the rules is unchanged.

## 0.2.0 (2026-11-04)

- Incorporated guidance from [Clark et al. (2026)](https://arxiv.org/abs/2610.29162).

## 0.1.0 (2026-10-20)

- Initial release.
