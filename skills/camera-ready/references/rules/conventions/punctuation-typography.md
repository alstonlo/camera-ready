# Use punctuation and type only for their formal functions

Avoid contractions, exclamation marks, and emoji. Use title-case headings only when the venue requires them. Use italics for definitions, not for decorative emphasis. When italics mark what a negation denies ("we do not heat the *lid*"), express that contrast in words if the intended focus is clear; otherwise keep the italics and flag the ambiguity. Use quotation marks for quotations, mentioned words, and unendorsed terms. Keep quotation marks on unendorsed terms (the cell's "decision"), and flag the term if the draft never states what it refers to. Do not add scare quotes to ordinary words. Keep sentence punctuation outside exact literals, such as commands and outputs, unless it belongs to the literal, and preserve literal characters.

## Details

Replacing straight quotes with curly quotes can change a shell argument or exact output. Flag proposed corrections inside protected literals rather than changing their characters. When the draft states what an unendorsed term refers to, keep the quotation marks and state that referent beside the term.

## Examples

> Bad: The lid doesn't fit the jar.
>
> Good: The lid does not fit the jar.

> Bad: The lid fits!
>
> Good: The lid fits.

> Bad: The lid fits. ✅
>
> Good: The lid fits.

The venue does not require title-case headings.

> Bad: Seed Storage Conditions
>
> Good: Seed storage conditions

The venue requires title-case headings.

> Bad: Seed Storage Conditions!
>
> Good: Seed Storage Conditions

> Bad: The lid is *airtight*.
>
> Good: The lid is airtight.

> Bad: We call the gap between lid and jar the *clearance*. The clearance remains *constant*.
>
> Good: We call the gap between lid and jar the *clearance*. The clearance remains constant.

> Bad: We do not heat the *lid*; we heat the base.
>
> Good: We heat the base rather than the lid.

The draft does not settle the intended contrast, so keep the italics, flag the ambiguous focus, and expand the contraction.

> Bad: We don't heat the *lid*.
>
> Good: We do not heat the *lid*.

> Bad: The label reads "fragile". We weigh the "sample".
>
> Good: The label reads "fragile". We weigh the sample.

> Bad: The word "cold" appears on the label. We weigh the "sample".
>
> Good: The word "cold" appears on the label. We weigh the sample.

The draft defines the cell's "decision" as a change in swimming direction, without attributing conscious choice.

> Bad: We record the cell's "decision".
>
> Good: We record the cell's "decision", its change in swimming direction.

The draft identifies the command as `pwd`, without a period.

> Bad: The command is `pwd.`
>
> Good: The command is `pwd`.

The draft states that the program prints `Done.`, with the period as part of the output.

> Bad: The output is `Done`.
>
> Good: The output is `Done.`.

The script in the draft uses straight quotes in `echo "ready"`; the Good line proposes replacing the curly quotes for the author.

> Bad: The command is `echo “ready”`.
>
> Good: The command is `echo "ready"`.
