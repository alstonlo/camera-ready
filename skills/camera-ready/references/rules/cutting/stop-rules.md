# Revise cuts when stop rules apply

Revise a cut if it leaves a paragraph without needed explanation or support, or breaks the paragraph's [topic string](../prose/topic-string.md). Merge the paragraph with an adjacent one that makes the same point, or restore the missing material and connections. Before cutting a confusing passage, check for a missing step or [referent](../prose/referents.md). Restore it only from elsewhere in the draft, or flag it if the draft lacks it. If a reader outside the subfield cannot follow the shortened passage, restore the needed context and steps instead of cutting further. These stop rules override the length target. Never meet a target by adding negative `\vspace`, reducing font sizes, or narrowing figures. Report the remaining excess instead.

## Details

Confusion in a passage usually means that a step is missing, not that the passage is too long. When no further cut that the author has authorized would keep the text clear, report how far the text exceeds the limit and name the content that keeps it over the limit, so that the author can decide what to cut. Spacing commands already in the draft are not defects in themselves. This rule forbids only layout changes that an editor adds to force the paper to fit.

## Examples

**Example 1.** An earlier cut removed the draft's seedling count.

> **Bad.** Each tray holds six seedlings. We therefore need three trays.
>
> **Good.** Each tray holds six seedlings. We have eighteen seedlings and therefore need three trays.

**Example 2.** An earlier cut left these adjacent paragraphs; a slash marks the paragraph break. Good merges them because they make the same point.

> **Bad.** The lid reduces evaporation. / Less water is lost overnight.
>
> **Good.** The lid reduces evaporation. Less water is lost overnight.

**Example 3.** The draft already contains \smallskip, and an editor adds negative \vspace to meet the length limit. Good removes the added command but keeps the draft's own spacing; if no authorized cut keeps the text clear, the editor reports the remaining excess instead.

> **Bad.** \smallskip The sample remains dry. \vspace{-4mm}
>
> **Good.** \smallskip The sample remains dry.
