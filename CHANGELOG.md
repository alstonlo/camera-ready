# Changelog

This project follows [Semantic Versioning](https://semver.org/). The version is set in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json); bump it with every release so that installed plugins pick up the update.

## 0.2.0 (2026-11-04)

- Added rules for constructions that make AI-written prose hard to process, based on [Clark et al. (2026)](https://arxiv.org/abs/2610.29162).
- Added a rule against inanimate subjects with verbs that need a person or animal ("the docstring promises").
- Added rules against nouns used as verbs for one occasion ("calendar it") and unusual word pairs ("verified red").
- Lowered the noun-stack threshold to three nouns in a row.
- Added rules to keep optional words that mark where a clause begins ("that", "in order to") and to move lists or long phrases that separate a subject from its verb.
- Added a "compressed constructions" pattern to the deslopping section that links these rules.
- Updated concision rules to preserve the small words that mark a sentence's structure.

## 0.1.0 (2026-10-20)

- Distributed as a Claude Code and Codex plugin.
- Added lite mode as the default; full mode keeps audit notes.
