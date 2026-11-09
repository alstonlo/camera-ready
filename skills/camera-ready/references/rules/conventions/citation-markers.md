# Keep citation markers out of subject and object positions

Do not use a bracketed or parenthetical citation marker as a subject or object. Replace "[8] introduces" with a textual citation such as `\citet{key}`, keeping the citation key. When asserting an established result, shorten "In a recent study, ... showed that X" to "X (citation)". Keep cited authors as the subject when reporting, characterizing, or contrasting a claim that the paper does not assert, following [prior work](../story/prior-work-comparisons.md). Place each citation beside its clause when the draft identifies that link; otherwise, flag a trailing cluster that obscures which source supports which claim. Flag any passage that leaves unclear where a source's material begins or ends. For package commands, author formatting, and multi-sentence attribution, see Details.

## Details

To test a citation marker in parentheses or brackets, remove it temporarily and read the sentence. The remaining words must form a grammatical sentence. When a marker splits a verb phrase, as in "has~\citep{key} dissolved", move it after the full verb phrase without changing which claim it supports.

Match the commands of the document's citation package. In natbib, `\citet` names the authors in running text and `\citep` encloses the citation in parentheses or brackets. Other packages use different commands, such as `\textcite` and `\parencite` in biblatex. Put a non-breaking space before a parenthetical citation, as in `result~\citep{key}`. Use "et al." only for three or more authors. Set it in upright type, with a period after "al" and no period after "et".

When a passage moves from reporting a cited source's claims to presenting the paper's own interpretation, state who makes each claim at the transition point. Follow [prior work](../story/prior-work-comparisons.md) to preserve the source's qualifications.

## Examples

> **Context.** The draft uses natbib and cites ortiz2025, a paper by one author.
>
> **Bad.** \citep{ortiz2025} compares two methods for measuring rainfall.
>
> **Good.** \citet{ortiz2025} compares two methods for measuring rainfall.

> **Context.** The draft uses natbib and states that the authors extend Ortiz's method.
>
> **Bad.** We extend \citep{ortiz2025}.
>
> **Good.** We extend the method of \citet{ortiz2025}.

> **Context.** The draft uses natbib and treats the salt's solubility as an established result.
>
> **Bad.** In a recent study, \citet{ortiz2025} showed that this salt dissolves in water.
>
> **Good.** This salt dissolves in water~\citep{ortiz2025}.

> **Context.** The draft cites ortiz2025 for the shell's shrinkage and patel2024 for slower decay.
>
> **Bad.** Drying shrinks the shell, and cooling slows decay~\citep{ortiz2025,patel2024}.
>
> **Good.** Drying shrinks the shell~\citep{ortiz2025}, and cooling slows decay~\citep{patel2024}.

> **Context.** Elsewhere, the draft attributes the cooling hypothesis to its own authors, not to Ortiz. The Good line proposes clarifying the attribution for the author.
>
> **Bad.** Ortiz reports that the shell shrinks. Cooling may reduce this effect.
>
> **Good.** Ortiz reports that the shell shrinks. We hypothesize that cooling may reduce this effect.

> **Bad.** The salt has~\citep{ortiz2025} dissolved in water.
>
> **Good.** The salt has dissolved in water~\citep{ortiz2025}.

> **Bad.** The shell shrinks \citep{ortiz2025}.
>
> **Good.** The shell shrinks~\citep{ortiz2025}.

> **Context.** The draft uses biblatex, which provides `\textcite` for textual citations and `\parencite` for parenthetical ones.
>
> **Bad.** \parencite{ortiz2025} describes the apparatus.
>
> **Good.** \textcite{ortiz2025} describes the apparatus.

> **Context.** The draft cites a paper by two authors, Ortiz and Patel.
>
> **Bad.** Ortiz et al. describe the apparatus.
>
> **Good.** Ortiz and Patel describe the apparatus.

> **Context.** The draft cites a paper by three authors.
>
> **Bad.** Ortiz et. al describe the apparatus.
>
> **Good.** Ortiz et al. describe the apparatus.

> **Context.** The draft cites a paper by three authors.
>
> **Bad.** Ortiz *et al.* describe the apparatus.
>
> **Good.** Ortiz et al. describe the apparatus.
