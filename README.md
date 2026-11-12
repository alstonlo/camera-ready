<h1 align="center">camera-ready</h1>

<p align="center"><a href="https://skills.sh/alstonlo/camera-ready"><img src="https://skills.sh/b/alstonlo/camera-ready" alt="skills.sh installs"></a></p>

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

```
/camera-ready polish this section
/camera-ready tighten my abstract
/camera-ready cut this to eight pages
```

The skill reads the text and the writing guide, edits the text section by section with targeted changes, checks the result against a saved copy of the original, and returns a report. It does not change what the draft claims: it proposes claim changes in the report instead, unless you ask it to change claims.

Before editing, the skill saves a copy of each file and writes its audit of the text (the argument, each section's point, the strength of the main claims, and the terms) to a notes file, so that the audit survives compaction. Both go in `.camera-ready/` at the project root. For example, for `paper/main.tex`:

```
.camera-ready/paper/main.orig.tex
.camera-ready/paper/main.notes.md
```

To store the notes elsewhere, name a directory in the prompt, `CLAUDE.md` or `AGENTS.md`, or set the `CAMERA_READY_ROOT` environment variable.

## Credits

Writing guidance was compiled from:

-  A variety of resources on writing in [REFERENCES.md](REFERENCES.md)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- [blader/humanizer](https://github.com/blader/humanizer)
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer)
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)

## License

MIT
