<h1 align="center">camera-ready</h1>

An editing skill for camera-ready academic writing.

I created this skill out of frustration with Opus 5's writing style when using agents for exploratory research. Prior humanizing skills generally improved the superficial style of writing but failed to fix the deeper issues that made Opus 5 incomprehensible. This skill was created by compiling writing tips across multiple deep research reports on academic writing and prior humanizer skills (see [Credits](#credits)). Afterwards, I personally tuned it by testing the skill on AI-generated reports and providing feedback.

> ⚠ **Disclaimer.** Writing is subjective, and this skill reflects just one of many styles and preferences. I welcome any feedback and contributions to improve this skill.

## Installation

### Claude Code

```text
/plugin marketplace add alstonlo/camera-ready
/plugin install camera-ready@camera-ready
```

Invoke the Claude Code plugin with `/camera-ready:camera-ready` or the shorter `/camera-ready` unless another command already uses that name. To install updates, run `/plugin marketplace update camera-ready`, or enable automatic updates for the marketplace under **Marketplaces** in `/plugin`.

### Codex

```bash
codex plugin marketplace add alstonlo/camera-ready
codex plugin add camera-ready@camera-ready
```

Codex runs the skill only when you name it. To install updates, run `codex plugin marketplace upgrade camera-ready`.

### Other agents

```bash
npx skills add alstonlo/camera-ready --global --agent '*'
```

This installs the skill for every agent the [Skills CLI](https://github.com/vercel-labs/skills) supports. Omit `--global` to install it only in the current project. If the Skills CLI does not support your agent, copy the whole `skills/camera-ready/` folder into its skills directory, because the skill reads `references/guide.md` on every run.

## Usage

In Claude Code, run `/camera-ready` followed by the request. In Codex, start the request with `$camera-ready:camera-ready` instead.

### Lite mode

By default, the skill edits in one pass in `lite` mode. It reads the whole text and identifies its story, claims, and terminology. It then edits the text chunk by chunk, rereads it, and reports what changed along with questions for the author.

```
/camera-ready polish this section
/camera-ready tighten my abstract
```

### Full mode

For an edit with saved notes and verification, start the request with `full`:

```
/camera-ready full polish this paper
/camera-ready full cut this to eight pages
```

The full workflow first writes notes on the text: the story, an outline, a claim ledger that lists claims and their evidence, and a style sheet of terms and abbreviations. It uses these notes to guide the edit, verifies the result against them, and keeps them for the next run.

Each file you name gets its own notes file in `.camera-ready/` at the project root, the directory where the session started. For example, notes for `paper/main.tex` go in `.camera-ready/paper/main.notes.md`, and they also cover the files that `main.tex` includes. To store the notes elsewhere, name a directory in the request, set the `CAMERA_READY_ROOT` environment variable, or name a directory in the project's `CLAUDE.md` or `AGENTS.md`. The skill checks these sources in that order, uses the first directory specified, and resolves a relative path against the project root.

## Credits

Writing guidance compiled from:

- Several deep research reports on academic writing
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- [blader/humanizer](https://github.com/blader/humanizer)
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer)
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)

See [REFERENCES.md](REFERENCES.md) for the sources cited by the deep research reports.

## License

MIT
