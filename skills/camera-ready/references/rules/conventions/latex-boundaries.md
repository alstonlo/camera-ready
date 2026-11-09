# Preserve LaTeX paragraphs and comments when changing line breaks

When changing line breaks in LaTeX source, compare the result with the original. Keep paragraph breaks (blank lines) where they were, and keep each `%` comment covering the same text as before (see Details). Undo any paragraph or comment boundary changes caused by reflowing.

## Details

Joining a prose line onto a comment line hides that prose inside the comment. Splitting a comment line prints the rest of the comment as ordinary text. A percent sign (`%`) starts a comment only when unescaped; use `\%` to print a literal percent sign.

For blank lines around equations displayed on their own lines, follow the rule on [math prose](math-prose.md).

## Examples

**Example 1.** The original source puts both sentences in one paragraph. Here, `\n` represents a line break.

> **Bad.** `We rinse the jars.\n\nWe leave them to dry.`
>
> **Good.** `We rinse the jars.\nWe leave them to dry.`

**Example 2.** The original source starts a new paragraph before the second sentence. Here, `\n` represents a line break.

> **Bad.** `We rinse the jars.\nWe store them in a cool room.`
>
> **Good.** `We rinse the jars.\n\nWe store them in a cool room.`

**Example 3.** The original source puts the sentence on the line after the comment. Here, `\n` represents a line break.

> **Bad.** `% check label We weigh the jar.`
>
> **Good.** `% check label\nWe weigh the jar.`

**Example 4.** The original source keeps `% check label` on one line. Here, `\n` represents a line break.

> **Bad.** `% check\nlabel\nWe weigh the jar.`
>
> **Good.** `% check label\nWe weigh the jar.`
