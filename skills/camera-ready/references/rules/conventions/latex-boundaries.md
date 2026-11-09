# Preserve LaTeX paragraphs and comments when changing line breaks

When changing line breaks in LaTeX source, compare the result with the original. Keep paragraph breaks (blank lines) where they were, and keep each `%` comment covering the same text as before (see Details). Undo any paragraph or comment boundary changes caused by reflowing.

## Details

Joining a prose line onto a comment line hides that prose inside the comment. Splitting a comment line prints the rest of the comment as ordinary text. A percent sign (`%`) starts a comment only when unescaped; use `\%` to print a literal percent sign.

For blank lines around equations displayed on their own lines, follow the rule on [math prose](math-prose.md).

## Examples

**Edit 1.** The original source has one paragraph, and `\n` denotes a line break. The edit replaces the two line breaks after "jars." with one, removing the blank line so that LaTeX keeps both sentences in the original paragraph.

> **Before.** `We rinse the jars.\n\nWe leave them to dry.`
>
> **After.** `We rinse the jars.\nWe leave them to dry.`

**Edit 2.** The original source places the sentence after the comment, and `\n` denotes a line break. The edit restores the line break after "% check label" so that "We weigh the jar." falls outside the comment and appears in the document.

> **Before.** `% check label We weigh the jar.`
>
> **After.** `% check label\nWe weigh the jar.`
