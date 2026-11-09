# Delete em dashes

The LaTeX form `---` also counts as an em dash. Delete every en dash used as a pause. Replace the dash with a colon or semicolon only when the [pause punctuation](pause-punctuation.md) rule allows it. Use parentheses only when they do not make an essential qualification look optional under [stress position](../prose/stress-position.md). Otherwise, rewrite the sentence without the pause and keep its emphasis. Keep hyphens in compound words and en dashes in numeric ranges or two-person names (see Details).

## Details

In LaTeX, `--` produces an en dash. Keep an en dash in numeric ranges and in names formed from two people's names, such as "Sections 3–5" and "Kullback–Leibler". In LaTeX source, keep `--` for those same ranges and names, but replace `--` when it marks a pause.

## Examples

**Edit 1.**

> **Before.** The two-stage test uses the Kullback–Leibler divergence—over steps 3–5.

> **After.** The two-stage test uses the Kullback–Leibler divergence over steps 3–5.

The dashes in "Kullback–Leibler" and "3–5" identify the name and range; they do not mark pauses.

**Edit 2.**

> **Before.** The tray holds two tools—a ruler and a brush.

> **After.** The tray holds two tools: a ruler and a brush.

**Edit 3.**

> **Before.** The seal holds—only below 30 °C.

> **After.** The seal holds, but only below 30 °C.

**Edit 4.** Suppose the purchase date serves as optional background.

> **Before.** The tray—purchased in May—holds six vials.

> **After.** The tray (purchased in May) holds six vials.
