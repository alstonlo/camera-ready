# Cite each figure and table where its claim is stated

Cite each figure or table in the sentence stating its claim, rather than writing "In Figure 6 we show the results". Point to the panel or comparison that the draft identifies, and use stable numbered references instead of "below". If the claim requires an exact value that a reader could only estimate from a plot, state the draft's value or flag its absence. Flag unresolved citation or reference markers such as "??". For LaTeX float commands and capitalization, see the page.

## Details

Write `Figure~\ref{...}` with a non-breaking space. Capitalize numbered references such as "Figure 6", "Table 2", "Section 4", and "Theorem 1". In LaTeX, put an existing `\label` after its `\caption`, preserving the label's identity. A rendered "?" or "??" where a reference belongs marks an undefined citation or cross-reference.

Use a panel or comparison that the draft actually identifies. A chain of figure numbers does not tell the reader which contrast supports the sentence; name that contrast when the draft supplies it. Do not infer a placement defect from source order alone, because the typesetter may move floats.

## Examples

The draft identifies the lower plot as Figure 4(b).

- Bad: The water level falls during summer, as shown in the plot below.
- Good: The water level falls during summer, as shown in Figure 4(b).
