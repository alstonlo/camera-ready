# Preserve LaTeX paragraphs and comments when changing line breaks

When changing line breaks in LaTeX source, compare the result with the original. Keep paragraph breaks (blank lines) where they were, and keep each `%` comment covering the same text as before (see Details). Undo any paragraph or comment boundary changes caused by reflowing.

## Details

Joining a prose line onto a comment line hides that prose inside the comment. Splitting a comment line prints the rest of the comment as ordinary text. A percent sign (`%`) starts a comment only when unescaped; use `\%` to print a literal percent sign.

For blank lines around equations displayed on their own lines, follow the rule on [math prose](math-prose.md).

## Examples

**Edit 1.** Suppose the original source consists of one paragraph; `\n` denotes a line break. Before:

> `We rinse the jars.\n\nWe leave them to dry.`

After:

> `We rinse the jars.\nWe leave them to dry.`

Before shows a paragraph break introduced during editing. After restores the author's single paragraph.

**Edit 2.** Say the original source puts the sentence on the line after the comment; `\n` denotes a line break. Before:

> `% check label We weigh the jar.`

After:

> `% check label\nWe weigh the jar.`

Before shows the lines joined during editing, which hides the sentence in the comment. After restores the original line break.
