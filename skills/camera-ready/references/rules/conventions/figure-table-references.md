# Cite each figure and table where its claim is stated

Cite each figure or table in the sentence stating its claim, rather than writing "In Figure 6 we show the results". Point to the specific panel or comparison that the draft identifies, and use numbered references instead of relative pointers such as "below". If the claim requires an exact value that a reader could only estimate from a plot, state the value from the draft or flag that it is missing. Flag unresolved citation or reference markers such as "??". For LaTeX float commands and capitalization, see the page.

## Details

Write `Figure~\ref{...}` with a non-breaking space. Capitalize numbered references to figures, tables, sections, and theorems. Place an existing `\label` after its `\caption` without changing the label key. Do not judge float placement from the LaTeX source order, because LaTeX moves floats during typesetting.

## Examples

The draft identifies the lower plot as Figure 4(b).

> Bad: The water level falls during summer, as shown in the plot below.
>
> Good: The water level falls during summer, as shown in Figure 4(b).

> Bad: Figure 2 shows the results. Water loss increases with temperature.
>
> Good: Water loss increases with temperature (Figure 2).

The draft identifies the comparison as open jars versus sealed jars.

> Bad: Water loss is greater (Figure 3).
>
> Good: Water loss is greater in open jars than in sealed jars (Figure 3).

The draft gives the water level as 5.2 cm, which the reader cannot read from the plot alone.

> Bad: The water level exceeds the 5 cm limit (Figure 4).
>
> Good: The water level is 5.2 cm, exceeding the 5 cm limit (Figure 4).

The draft identifies Figure 4 as the supporting plot; the Good line proposes replacing the unresolved marker for the author.

> Bad: The water level falls during summer (Figure ??).
>
> Good: The water level falls during summer (Figure 4).

> Bad: The water level falls during summer (figure 4).
>
> Good: The water level falls during summer (Figure 4).

> Bad: The water level falls during summer (Figure \ref{fig:level}).
>
> Good: The water level falls during summer (Figure~\ref{fig:level}).

> Bad: \label{fig:level}\caption{Water level falls during summer.}
>
> Good: \caption{Water level falls during summer.}\label{fig:level}
