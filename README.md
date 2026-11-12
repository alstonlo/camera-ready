<h1 align="center">camera-ready</h1>

An editing skill for camera-ready academic writing.

I created this skill out of frustration with Opus 5's writing style when using agents for exploratory research. Prior humanizing skills generally improved the superficial style of writing but failed to fix the deeper issues that made Opus 5 incomprehensible. This skill aims to holistically improve the quality of AI-generated academic writing. It was created by compiling guidance from multiple resources on academic writing and humanizer skills (see [Credits](#credits)). The result is a unified writing guide covering a variety of topics including story crafting, claim calibration, concision, clarity, prose, and AI slop patterns.  Afterwards, I personally tuned it by testing the skill on AI-generated reports and providing feedback.

> [!NOTE]
> Writing is subjective, and this skill reflects just one of many styles and preferences. I welcome any feedback and contributions to improve this skill.

## Installation

### Claude Code

```text
/plugin marketplace add alstonlo/camera-ready
/plugin install camera-ready@camera-ready
```

To install updates, run `/plugin marketplace update camera-ready`, or enable automatic updates for the marketplace under **Marketplaces** in `/plugin`.

### Codex

```bash
codex plugin marketplace add alstonlo/camera-ready
codex plugin add camera-ready@camera-ready
```

To install updates, run `codex plugin marketplace upgrade camera-ready`.

### Other agents

```bash
npx skills add alstonlo/camera-ready --global --agent '*'
```

This installs the skill for every agent the [Skills CLI](https://github.com/vercel-labs/skills) supports. Omit `--global` to install it only in the current project. If the Skills CLI does not support your agent, copy the whole `skills/camera-ready/` folder into its skills directory.

## Usage

In Claude Code, run `/camera-ready` followed by the request. In Codex, start the request with `$camera-ready:camera-ready` instead.

### Lite mode

By default, the skill edits in lite mode. It reads the text and writing guide, edits the text chunk by chunk, rereads the result, and returns a report to the user.

```
/camera-ready polish this section
/camera-ready tighten my abstract
```

### Full mode

For a more comprehensive edit, run the skill in full mode:

```
/camera-ready full polish this paper
/camera-ready full cut this to eight pages
```

Instead of managing everything in-context, full mode first reads the paper and writes a set of audit notes on it, which records high-level information like the paper's central argument, outline, claims and their evidence, and convention choices. The notes are [TODO]

skill uses these notes to edit for factual consistency, readability, and clear academic style while tracking changes and unresolved questions. Compared with lite mode, full mode should produce higher-quality revisions with greater consistency and attention to detail, but require more tokens in return.

By default, the audit notes are saved in `.camera-ready/` at the project root. For example, notes for `paper/main.tex` would go in `.camera-ready/paper/main.notes.md`. To store the notes elsewhere, name a directory in the prompt, `CLAUDE.md` or `AGENTS.md` or set the `CAMERA_READY_ROOT` environment variable.

## Credits

Writing guidance was compiled from:

-  A variety of resources on writing in [REFERENCES.md](REFERENCES.md)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- [blader/humanizer](https://github.com/blader/humanizer)
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer)
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)

## License

MIT
