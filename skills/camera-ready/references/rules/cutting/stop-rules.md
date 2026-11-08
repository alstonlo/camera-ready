# Revise cuts when stop rules apply

Revise a cut if it leaves a paragraph underdeveloped or breaks its [topic string](../prose/topic-string.md): either merge the paragraph with an adjacent one that makes the same point, or restore the missing development and connections. Before cutting a confusing passage, check whether a step is missing, because confusion usually signals an omission rather than excess. Supply a missing step or [referent](../prose/referents.md) only from elsewhere in the draft, and flag it if the draft does not contain it. If a reader outside the subfield cannot follow the shortened passage, restore the needed framing and steps instead of cutting further. These stop rules override the length target. Never meet a length target by adding negative `\vspace`, reducing font sizes, or narrowing figures; report the remaining excess instead.

## Details

When no further authorized cut can preserve clarity, report the remaining excess length and the content decision that keeps the text from meeting the target. Spacing commands already in the draft are not defects in themselves; this rule forbids only layout changes added to force the paper to fit.

## Examples

> **Context.** A proposed cut removes the draft's statement that there are eighteen seedlings.
>
> **Bad.** Each tray holds six seedlings. We therefore need three trays.
>
> **Good.** Each tray holds six seedlings. We have eighteen seedlings and therefore need three trays.

> **Context.** A cut leaves two adjacent paragraphs that make the same point (with "/" marking the paragraph break).
>
> **Bad.** The lid reduces evaporation. / Less water is lost overnight.
>
> **Good.** The lid reduces evaporation. Less water is lost overnight.

> **Context.** A cut removes the draft's definition of the meniscus as the curved liquid surface, which readers outside the subfield need.
>
> **Bad.** We record the meniscus height.
>
> **Good.** The meniscus is the curved liquid surface. We record the meniscus height.

> **Context.** The draft already contains \smallskip, and a proposed length edit adds negative \vspace to meet the length limit. No further authorized cut preserves clarity, so keep the original spacing and report the remaining excess.
>
> **Bad.** \smallskip The sample remains dry. \vspace{-4mm}
>
> **Good.** \smallskip The sample remains dry.
