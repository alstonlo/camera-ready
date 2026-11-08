# Preserve LaTeX boundaries when reflowing prose

When reflowing LaTeX source, compare it with the original: keep paragraph breaks (blank lines) where they were, and keep each % comment hiding exactly the text it hid before. Joining a prose line onto the end of a comment line hides that prose; breaking a comment line can expose the rest of the comment as text. Undo boundary changes introduced by reflow.

## Details

An unescaped percent sign comments out the rest of its source line. Moving a newline can therefore change which characters appear in the rendered text even if every character remains in the source. Keep the comment and the text it excludes on the same side of that boundary.

A blank source line starts a paragraph. Compare the edited source with the original to distinguish a paragraph break introduced by reflow from one already present in the draft. Do not infer that an original blank line is accidental. For paragraph boundaries around displayed mathematics, follow [math prose](math-prose.md).

## Examples

The original draft places both sentences in one paragraph; reflow inserted a blank line, and `\n` below denotes a source newline.

- Bad: `We rinse the jars.\n\nWe leave them to dry.`
- Good: `We rinse the jars.\nWe leave them to dry.`
