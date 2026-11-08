# Figures and tables

- **Captions.** Write captions that let readers interpret a figure correctly without reading the body text. State what is plotted or tabulated: the quantities, units where applicable, plot axes, and whether higher or lower is better when that is not obvious. Name the conditions (dataset, model, setting), explain each visual encoding (line styles, colors, shaded regions, and [error bars](../../references/guide.md#uncertainty-and-significance)), and state the figure's main point. A caption that only names the figure ("Results on ImageNet.") is incomplete. Complete it with the wording from the paragraph that references the figure; flag missing facts if they appear nowhere in the draft. Check that the caption and body text describe the figure consistently.
- **References in text.** Refer to every float in the sentence stating its claim ("Accuracy falls as the noise rate rises (Figure 6)" or "Figure 6 shows that accuracy falls as the noise rate rises", not "In Figure 6 we show the results"). If the claim depends on a value the reader can only estimate from the plot, give that number in the sentence or caption. Flag it if neither states the value. Write `Figure~\ref{...}` with a non-breaking space, and capitalize "Figure 6", "Table 2", "Section 4", and "Theorem 1". In LaTeX source, put `\label` after `\caption`. Flag every "?" or "??" in rendered text, which marks an undefined `\cite` or `\ref`.

## Examples

- Bad caption: "Figure 3: Ablation results."
- Good caption: "Figure 3: Top-1 accuracy (%) of ResNet-50 on ImageNet-1k when each component is removed, mean ± standard deviation over three seeds. Removing the auxiliary loss causes the largest drop."
