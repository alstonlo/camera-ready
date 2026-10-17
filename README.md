# Camera Ready

This is an editing skill for camera-ready academic writing. It was created by compiling writing tips across multiple deep research reports on academic prose and some existing humanizer skills (see [Credits](#credits)). Afterwards, I personally tuned it by testing the skill on AI-generated reports and providing feedback.

I created `camera-ready` out of frustration with Opus 5's writing style when using agents for exploratory research. Prior humanizing skills generally improved the superficial style of writing but failed to fix the deeper issues with content and narrative flow that made Opus 5 incomprehensible.

## Installation

Clone this repository into your personal skills directory:

```
git clone https://github.com/alstonlo/camera-ready.git ~/.claude/skills/camera-ready
```

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
