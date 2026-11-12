<div align="center">

# camera-ready

**An editing skill for camera-ready academic writing.**

[![skills.sh installs](https://skills.sh/b/alstonlo/camera-ready)](https://skills.sh/alstonlo/camera-ready)

</div>

I created this skill out of frustration with Opus 5's writing style when using agents for exploratory research. Prior humanizing skills generally improved the superficial style of writing but failed to fix the deeper issues that made Opus 5 incomprehensible. This skill aims to holistically improve the quality of AI-generated academic writing. It was created by compiling guidance from multiple resources on academic writing and humanizer skills (see [Credits](#credits)). The result is a unified writing guide covering a variety of topics including story, claims, cuts, prose, conventions, and AI slop patterns. Afterwards, I refined it by testing the skill on AI-generated papers and making manual edits.

> [!NOTE]
> Writing is subjective, and this skill reflects just one of many styles and preferences. I welcome any feedback and contributions to improve this skill.

## Installation

### Claude Code

```
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

In Claude Code, run `/camera-ready` followed by the request. In Codex, start the request with `$camera-ready:camera-ready` instead. Note that model invocation has been disabled for this skill.

```
/camera-ready polish this section
/camera-ready tighten my abstract
/camera-ready cut this to eight pages
```

The skill will read the source text and writing guide, audit and edit the source text according to your instructions, check its work, and return a report back to you. If you only want feedback without any edits, use the word "review" explicitly:

```
/camera-ready review my introduction
/camera-ready review the story of my paper
```

To aid in its execution, the skill will save a notes file that serves as a working memory of the text's story, outline, claims, and more, and, in edit mode, a backup of the original source texts. By default, these will be saved in a `.camera-ready/` directory at the project root. For example, if you were editing `paper/main.tex`, the skill would create the files:

```
.camera-ready/paper/
    main.orig.tex
    main.notes.md
```

To store these files elsewhere, name a directory in the prompt, `CLAUDE.md` or `AGENTS.md`, or set the `CAMERA_READY_ROOT` environment variable.

## Credits

Writing guidance was compiled from:

- A variety of resources on writing in [REFERENCES.md](REFERENCES.md)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- [blader/humanizer](https://github.com/blader/humanizer)
- [brandonwise/humanizer](https://github.com/brandonwise/humanizer)
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)

## License

MIT
