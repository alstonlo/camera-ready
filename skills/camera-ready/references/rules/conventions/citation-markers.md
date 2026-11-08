# Keep citation markers out of subject and object positions

A bracketed or parenthetical citation marker is not a noun. Replace "[8] introduces" with a textual citation (`\citet{key}` in LaTeX), keeping the key. For an established result that the paper asserts, shorten "In a recent study, ... showed that X" to "X (citation)"; keep the cited authors as the subject when the sentence reports, characterizes, or contrasts a claim that the paper does not itself assert, following [prior work](../story/prior-work-comparisons.md). When the draft shows which source supports which clause, place each citation beside its clause; otherwise flag a trailing citation cluster that leaves unclear which source supports which claim. Flag any passage where the draft leaves unclear how far a source's material extends. For citation commands, author-name formatting, and attribution across sentences, see the page.

## Details

If you remove a parenthetical citation marker temporarily, the rest of the sentence should remain grammatical. When a marker splits a verb phrase, move it without changing which claim it supports.

Match the commands of the document's citation package: natbib provides `\citet` and `\citep`, whereas other packages may use different commands. Put a non-breaking space before a parenthetical citation (`result~\citep{key}`). Write "et al." in upright type, with a period only after "al.", and use it only for three or more authors.

When a passage moves from a cited source's claims to the paper's own interpretation, mark the shift with explicit attribution; follow [prior work](../story/prior-work-comparisons.md) to preserve the source's qualifications.

## Examples

The draft uses natbib and cites the single-author paper ortiz2025.

> **Bad.** \citep{ortiz2025} compares two methods for measuring rainfall.
>
> **Good.** \citet{ortiz2025} compares two methods for measuring rainfall.

The draft uses natbib and states that the extension concerns Ortiz's method.

> **Bad.** We extend \citep{ortiz2025}.
>
> **Good.** We extend the method of \citet{ortiz2025}.

The draft asserts this established result and uses natbib.

> **Bad.** In a recent study, \citet{ortiz2025} showed that this salt dissolves in water.
>
> **Good.** This salt dissolves in water~\citep{ortiz2025}.

The draft assigns the shrinking result to ortiz2025 and the decay result to patel2024.

> **Bad.** Drying shrinks the shell, and cooling slows decay~\citep{ortiz2025,patel2024}.
>
> **Good.** Drying shrinks the shell~\citep{ortiz2025}, and cooling slows decay~\citep{patel2024}.

The draft indicates that the cooling hypothesis belongs to the present authors, not to Ortiz; the Good line proposes clarifying the attribution for the author.

> **Bad.** Ortiz reports that the shell shrinks. Cooling may reduce this effect.
>
> **Good.** Ortiz reports that the shell shrinks. We hypothesize that cooling may reduce this effect.

> **Bad.** The salt has~\citep{ortiz2025} dissolved in water.
>
> **Good.** The salt has dissolved in water~\citep{ortiz2025}.

> **Bad.** The shell shrinks \citep{ortiz2025}.
>
> **Good.** The shell shrinks~\citep{ortiz2025}.

The draft uses biblatex, which provides `\textcite` for textual citations and `\parencite` for parenthetical ones.

> **Bad.** \parencite{ortiz2025} describes the apparatus.
>
> **Good.** \textcite{ortiz2025} describes the apparatus.

The cited paper has two authors, Ortiz and Patel.

> **Bad.** Ortiz et al. describe the apparatus.
>
> **Good.** Ortiz and Patel describe the apparatus.

The cited paper has three authors.

> **Bad.** Ortiz et. al describe the apparatus.
>
> **Good.** Ortiz et al. describe the apparatus.

The cited paper has three authors.

> **Bad.** Ortiz *et al.* describe the apparatus.
>
> **Good.** Ortiz et al. describe the apparatus.
