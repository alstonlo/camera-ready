# Preserve LaTeX boundaries when reflowing prose

When reflowing LaTeX source, compare it with the original: keep paragraph breaks (blank lines) where they were, and keep each `%` comment hiding the same text as before. Joining a prose line onto the end of a comment line hides that prose; breaking a comment line can expose the rest of the comment as text. Undo any boundary changes introduced by reflow.

## Details

Only an unescaped `%` starts a comment; `\%` prints a literal percent sign.

For blank lines around displayed equations, follow [math prose](math-prose.md).

## Examples

> **Context.** The original source keeps both sentences in one paragraph, and `\n` denotes a newline.
>
> **Bad.** `We rinse the jars.\n\nWe leave them to dry.`
>
> **Good.** `We rinse the jars.\nWe leave them to dry.`

> **Context.** The original source starts a new paragraph before the second sentence, and `\n` denotes a newline.
>
> **Bad.** `We rinse the jars.\nWe store them in a cool room.`
>
> **Good.** `We rinse the jars.\n\nWe store them in a cool room.`

> **Context.** The original source puts the sentence on the line after the comment, and `\n` denotes a newline.
>
> **Bad.** `% check label We weigh the jar.`
>
> **Good.** `% check label\nWe weigh the jar.`

> **Context.** The original source keeps the comment `% check label` on one line, and `\n` denotes a newline.
>
> **Bad.** `% check\nlabel\nWe weigh the jar.`
>
> **Good.** `% check label\nWe weigh the jar.`
