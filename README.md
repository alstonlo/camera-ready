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

Codex runs the skill only when you name it, as in `$camera-ready:camera-ready polish this section`. To install updates, run `codex plugin marketplace upgrade camera-ready`.

### Other agents

```bash
npx skills add alstonlo/camera-ready --global --agent '*'
```

This installs the skill for every agent the [Skills CLI](https://github.com/vercel-labs/skills) supports. Omit `--global` to install it only in the current project. If the Skills CLI does not support your agent, copy the whole `skills/camera-ready/` folder into its skills directory, because the skill reads `references/guide.md` on every run.

## Usage

Run `/camera-ready` followed by the request:

```
/camera-ready polish this section
/camera-ready tighten my abstract
/camera-ready cut this to eight pages
```

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
