# Delete em dashes

Delete every em dash, including `---` in LaTeX, and every en dash used as a pause. Replace the dash with a colon or semicolon only when the [pause punctuation](pause-punctuation.md) rule allows it. Use parentheses only when they do not make an essential qualification look optional under [stress position](../prose/stress-position.md). Otherwise, rewrite the sentence without the pause and keep its emphasis. Keep hyphens in compound words and en dashes in numeric ranges or two-person names (see Details).

## Details

In LaTeX, `--` produces an en dash. Keep an en dash in numeric ranges and in names formed from two people's names, such as "Sections 3–5" and "Kullback–Leibler". In LaTeX source, keep `--` for those same ranges and names, but replace `--` when it marks a pause.

## Examples

**Example 1.**

> **Bad.** The firewall rejects expired credentials—before checking access rules.
>
> **Good.** The firewall rejects expired credentials before checking access rules.

**Example 2.**

> **Bad.** The valve closes – before the tank empties.
>
> **Good.** The valve closes before the tank empties.

**Example 3.**

> **Bad.** The valve closes---before the tank empties.
>
> **Good.** The valve closes before the tank empties.

**Example 4.**

> **Bad.** We test settings 2--5--with the lid closed.
>
> **Good.** We test settings 2--5 with the lid closed.

**Example 5.**

> **Bad.** The two-stage test uses the Kullback–Leibler divergence—over steps 3–5.
>
> **Good.** The two-stage test uses the Kullback–Leibler divergence over steps 3–5.

**Example 6.**

> **Bad.** The tray holds two tools—a ruler and a brush.
>
> **Good.** The tray holds two tools: a ruler and a brush.

**Example 7.**

> **Bad.** The tray holds six vials—the rack holds twelve.
>
> **Good.** The tray holds six vials; the rack holds twelve.

**Example 8.**

> **Bad.** The seal holds—only below 30 °C.
>
> **Good.** The seal holds, but only below 30 °C.

**Example 9.** In this draft, the purchase date is an optional detail.

> **Bad.** The tray—purchased in May—holds six vials.
>
> **Good.** The tray (purchased in May) holds six vials.

**Example 10.**

> **Bad.** The new tap is effective—it reduces water use by 18%.
>
> **Good.** The new tap reduces water use by 18%.
