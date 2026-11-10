# Cite each figure and table in the sentence that states its finding

Replace announcements like "In Figure 6 we show the results" with the finding and its reference ("Accuracy falls as the noise rate rises (Figure 6)" or "Figure 6 shows that accuracy falls ..."; in the abstract, follow the [abstract rule](../story/section-functions.md)). Point to the specific panel or comparison the draft identifies, with numbered references rather than relative pointers such as "below". When a claim needs an exact value readers can only estimate from a plot, state the draft's value in the sentence or caption, or flag its absence. Flag unresolved citation or reference markers ("??"). Write `Figure~\ref{...}` with a non-breaking space, and capitalize "Figure", "Table", "Section", and "Theorem" for numbered items. Place an existing `\label` after its `\caption`.

## Details

LaTeX can move figures and tables during typesetting, so do not judge float placement from the order in the source file.

## Examples

**Edit 1.** If the draft identifies this plot as Figure 4(b), use that reference.

> **Before.** The water level falls during summer, as shown in the plot below.

> **After.** The water level falls during summer, as shown in Figure 4(b).

**Edit 2.**

> **Before.** Figure 2 shows the results. Water loss increases with temperature.

> **After.** Water loss increases with temperature (Figure 2).

**Edit 3.** Suppose the draft gives the water level as 5.2 cm, but the plot is too coarse to show how far it exceeds the limit.

> **Before.** The water level exceeds the 5 cm limit (Figure 4).

> **After.** The water level is 5.2 cm, which exceeds the 5 cm limit (Figure 4).
