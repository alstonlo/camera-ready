# Delete em dashes

Delete every em dash, including `---` in LaTeX, and every en dash used as a pause. Replace the dash with a colon or semicolon only when the [pause punctuation](pause-punctuation.md) rule allows it. Use parentheses only when they do not make an essential qualification look optional under [stress position](../prose/stress-position.md). Otherwise, rewrite the sentence without the pause and keep its emphasis. Keep hyphens in compound words and en dashes in numeric ranges or two-person names (see Details).

## Details

In LaTeX, `--` produces an en dash. Keep an en dash in numeric ranges and in names formed from two people's names, such as "Sections 3–5" and "Kullback–Leibler". In LaTeX source, keep `--` for those same ranges and names, but replace `--` when it marks a pause.

## Examples

**Example 1.** Good removes the pause while keeping the hyphen in the compound word and the en dashes in the name and range.

> **Bad.** The two-stage test uses the Kullback–Leibler divergence—over steps 3–5.
>
> **Good.** The two-stage test uses the Kullback–Leibler divergence over steps 3–5.

**Example 2.**

> **Bad.** The tray holds two tools—a ruler and a brush.
>
> **Good.** The tray holds two tools: a ruler and a brush.

**Example 3.** Good keeps the temperature limit in the main clause because it determines when the claim holds.

> **Bad.** The seal holds—only below 30 °C.
>
> **Good.** The seal holds, but only below 30 °C.

**Example 4.** The purchase date is optional background, so Good puts it in parentheses.

> **Bad.** The tray—purchased in May—holds six vials.
>
> **Good.** The tray (purchased in May) holds six vials.
