# Cite each figure and table in the sentence that states its finding

Cite each figure or table where its claim is stated, replacing announcements like "In Figure 6 we show the results". Point to the specific panel or comparison that the draft identifies, using numbered references instead of relative pointers such as "below". When a claim requires an exact value readers can only estimate from a plot, state the draft's value or flag the missing number. Flag unresolved citation or reference markers like "??". For LaTeX commands, capitalization, and float placement, see Details.

## Details

Write `Figure~\ref{...}` with a non-breaking space between "Figure" and the reference command. Capitalize "Figure", "Table", "Section", and "Theorem" when referring to numbered items. Place an existing `\label` after its `\caption`, keeping the label's identifier unchanged. LaTeX can move figures and tables during typesetting, so do not judge float placement from the order in the source file.

## Examples

**Edit 1.** The draft identifies the plot as Figure 4(b). The edit replaces "the plot below" with "Figure 4(b)" so that the reference names the specific panel and remains usable if the figure moves during typesetting.

> **Before.** The water level falls during summer, as shown in the plot below.
>
> **After.** The water level falls during summer, as shown in Figure 4(b).

**Edit 2.** The edit removes "Figure 2 shows the results" and adds "(Figure 2)" to the sentence about water loss, so that the figure is cited where its finding is stated.

> **Before.** Figure 2 shows the results. Water loss increases with temperature.
>
> **After.** Water loss increases with temperature (Figure 2).

**Edit 3.** The draft gives the exact level, but the plot is too coarse to show how far it exceeds the limit. The edit adds "is 5.2 cm, which" before "exceeds" so that readers can compare the exact water level with the 5 cm limit without estimating it from Figure 4.

> **Before.** The water level exceeds the 5 cm limit (Figure 4).
>
> **After.** The water level is 5.2 cm, which exceeds the 5 cm limit (Figure 4).
