# Delete em dashes

Delete every em dash, including `---` in LaTeX, and every en dash used as a pause. Replace the dash with a colon or semicolon only when the [pause-punctuation test](pause-punctuation.md) allows it, and use parentheses only when they do not make an essential qualification look optional under [stress position](../prose/stress-position.md); otherwise, rewrite the sentence without the pause while preserving its emphasis. Keep hyphens in compound words and en dashes in numeric ranges or two-person names ("Sections 3–5", "Kullback–Leibler"). For `--` in LaTeX source, see Details.

## Details

In LaTeX, `--` produces an en dash. Keep it for numeric ranges and two-person names; replace it when it marks a pause.

## Examples

> **Bad.** The firewall rejects expired credentials—before checking access rules.
>
> **Good.** The firewall rejects expired credentials before checking access rules.

> **Bad.** The valve closes – before the tank empties.
>
> **Good.** The valve closes before the tank empties.

> **Bad.** The valve closes---before the tank empties.
>
> **Good.** The valve closes before the tank empties.

> **Bad.** We test settings 2--5--with the lid closed.
>
> **Good.** We test settings 2--5 with the lid closed.

> **Bad.** The two-stage test uses the Kullback–Leibler divergence—over steps 3–5.
>
> **Good.** The two-stage test uses the Kullback–Leibler divergence over steps 3–5.

> **Bad.** The tray holds two tools—a ruler and a brush.
>
> **Good.** The tray holds two tools: a ruler and a brush.

> **Bad.** The tray holds six vials—the rack holds twelve.
>
> **Good.** The tray holds six vials; the rack holds twelve.

> **Bad.** The seal holds—only below 30 °C.
>
> **Good.** The seal holds, but only below 30 °C.

> **Context.** The purchase date is a subsidiary detail.
>
> **Bad.** The tray—purchased in May—holds six vials.
>
> **Good.** The tray (purchased in May) holds six vials.

> **Bad.** The new tap is effective—it reduces water use by 18%.
>
> **Good.** The new tap reduces water use by 18%.
