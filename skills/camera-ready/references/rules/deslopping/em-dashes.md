# Delete em dashes

Delete every em dash, including `---` in LaTeX, and every en dash used as a pause. Replace the dash with a colon or semicolon only when the [pause punctuation](pause-punctuation.md) rule allows it. Use parentheses only when they do not make an essential qualification look optional under [stress position](../prose/stress-position.md). Otherwise, rewrite the sentence without the pause and keep its emphasis. Keep hyphens in compound words and en dashes in numeric ranges or two-person names (see Details).

## Details

In LaTeX, `--` produces an en dash. Keep an en dash in numeric ranges and in names formed from two people's names, such as "Sections 3–5" and "Kullback–Leibler". In LaTeX source, keep `--` for those same ranges and names, but replace `--` when it marks a pause.

## Examples

**Edit 1.** The edit replaces the em dash before "over steps 3–5" with a space so that the sentence reads without a pause, while keeping the hyphen in "two-stage" and the en dashes in "Kullback–Leibler" and "3–5" for their distinct uses.

> **Before.** The two-stage test uses the Kullback–Leibler divergence—over steps 3–5.
>
> **After.** The two-stage test uses the Kullback–Leibler divergence over steps 3–5.

**Edit 2.** The edit replaces the em dash with a colon so that the complete clause "The tray holds two tools" introduces the list of those tools.

> **Before.** The tray holds two tools—a ruler and a brush.
>
> **After.** The tray holds two tools: a ruler and a brush.

**Edit 3.** The edit replaces the em dash with ", but" so that the temperature limit stays in the main clause as an essential condition on the claim.

> **Before.** The seal holds—only below 30 °C.
>
> **After.** The seal holds, but only below 30 °C.

**Edit 4.** The purchase date is optional background. The edit replaces the em dashes around "purchased in May" with parentheses so that the date remains an aside without interrupting the main claim with dashes.

> **Before.** The tray—purchased in May—holds six vials.
>
> **After.** The tray (purchased in May) holds six vials.
