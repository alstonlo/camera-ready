# Revise cuts when stop rules apply

Revise a cut if it leaves a paragraph without needed explanation or support, or breaks the paragraph's [topic string](../prose/topic-string.md). Merge the paragraph with an adjacent one that makes the same point, or restore the missing material and connections. Before cutting a confusing passage, check for a missing step or [referent](../prose/referents.md). Restore it only from elsewhere in the draft, or flag it if the draft lacks it. If a reader outside the subfield cannot follow the shortened passage, restore the needed context and steps instead of cutting further. These stop rules override the length target. Never meet a target by adding negative `\vspace`, reducing font sizes, or narrowing figures. Report the remaining excess instead.

## Details

Confusion in a passage usually means that a step is missing, not that the passage is too long. When no further cut that the author has authorized would keep the text clear, report how far the text exceeds the limit and name the content that keeps it over the limit, so that the author can decide what to cut. Spacing commands already in the draft are not defects in themselves. This rule forbids only layout changes that an editor adds to force the paper to fit.

## Examples

**Edit 1.** An earlier cut removed the draft's seedling count. The edit restores "We have eighteen seedlings" so that readers can see why six seedlings per tray requires three trays.

> **Before.** Each tray holds six seedlings. We therefore need three trays.
>
> **After.** Each tray holds six seedlings. We have eighteen seedlings and therefore need three trays.

**Edit 2.** An earlier cut left these adjacent paragraphs; a slash marks the paragraph break. The edit removes the paragraph break and keeps both sentences together because they make the same point about reduced water loss.

> **Before.** The lid reduces evaporation. / Less water is lost overnight.
>
> **After.** The lid reduces evaporation. Less water is lost overnight.

**Edit 3.** The draft already contains \smallskip, and an editor adds negative \vspace to meet the length limit. The edit removes "\vspace{-4mm}" but keeps "\smallskip", because the rule forbids adding layout changes to force the paper to fit. If no authorized cut keeps the text clear, the editor reports the remaining excess instead.

> **Before.** \smallskip The sample remains dry. \vspace{-4mm}
>
> **After.** \smallskip The sample remains dry.
