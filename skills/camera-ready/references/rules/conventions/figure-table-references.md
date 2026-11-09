# Cite each figure and table in the sentence that states its finding

Cite each figure or table where its claim is stated, replacing announcements like "In Figure 6 we show the results". Point to the specific panel or comparison that the draft identifies, using numbered references instead of relative pointers such as "below". When a claim requires an exact value readers can only estimate from a plot, state the draft's value or flag the missing number. Flag unresolved citation or reference markers like "??". For LaTeX commands, capitalization, and float placement, see Details.

## Details

Write `Figure~\ref{...}` with a non-breaking space between "Figure" and the reference command. Capitalize "Figure", "Table", "Section", and "Theorem" when referring to numbered items. Place an existing `\label` after its `\caption`, keeping the label's identifier unchanged. LaTeX can move figures and tables during typesetting, so do not judge float placement from the order in the source file.

## Examples

> **Context.** The draft identifies the lower plot as Figure 4(b).
>
> **Bad.** The water level falls during summer, as shown in the plot below.
>
> **Good.** The water level falls during summer, as shown in Figure 4(b).

> **Bad.** Figure 2 shows the results. Water loss increases with temperature.
>
> **Good.** Water loss increases with temperature (Figure 2).

> **Context.** The draft identifies the comparison as open jars versus sealed jars.
>
> **Bad.** Water loss is greater (Figure 3).
>
> **Good.** Water loss is greater in open jars than in sealed jars (Figure 3).

> **Context.** The draft reports a water level of 5.2 cm, which readers cannot determine from the plot alone.
>
> **Bad.** The water level exceeds the 5 cm limit (Figure 4).
>
> **Good.** The water level is 5.2 cm, which exceeds the 5 cm limit (Figure 4).

> **Context.** The draft identifies Figure 4 as the plot supporting the claim. The Good line proposes replacing the unresolved marker for the author.
>
> **Bad.** The water level falls during summer (Figure ??).
>
> **Good.** The water level falls during summer (Figure 4).

> **Bad.** The water level falls during summer (figure 4).
>
> **Good.** The water level falls during summer (Figure 4).

> **Bad.** The water level falls during summer (Figure \ref{fig:level}).
>
> **Good.** The water level falls during summer (Figure~\ref{fig:level}).

> **Bad.** \label{fig:level}\caption{Water level falls during summer.}
>
> **Good.** \caption{Water level falls during summer.}\label{fig:level}
