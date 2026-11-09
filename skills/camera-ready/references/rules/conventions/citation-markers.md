# Keep citation markers out of subject and object positions

Do not use a bracketed or parenthetical citation marker as a subject or object. Replace "[8] introduces" with a textual citation such as `\citet{key}`, keeping the citation key. When asserting an established result, shorten "In a recent study, ... showed that X" to "X (citation)". Keep cited authors as the subject when reporting, characterizing, or contrasting a claim that the paper does not assert, following [prior work](../story/prior-work-comparisons.md). Place each citation beside its clause when the draft identifies that link; otherwise, flag a trailing cluster that obscures which source supports which claim. Flag any passage that leaves unclear where a source's material begins or ends. For package commands, author formatting, and multi-sentence attribution, see Details.

## Details

To test a citation marker in parentheses or brackets, remove it temporarily and read the sentence. The remaining words must form a grammatical sentence. When a marker splits a verb phrase, as in "has~\citep{key} dissolved", move it after the full verb phrase without changing which claim it supports.

Match the commands of the document's citation package. In natbib, `\citet` names the authors in running text and `\citep` encloses the citation in parentheses or brackets. Other packages use different commands, such as `\textcite` and `\parencite` in biblatex. Put a non-breaking space before a parenthetical citation, as in `result~\citep{key}`. Use "et al." only for three or more authors. Set it in upright type, with a period after "al" and no period after "et".

When a passage moves from reporting a cited source's claims to presenting the paper's own interpretation, state who makes each claim at the transition point. Follow [prior work](../story/prior-work-comparisons.md) to preserve the source's qualifications.

## Examples

**Edit 1.** The draft uses natbib and cites ortiz2025, a paper by one author. The edit replaces "\citep{ortiz2025}" with "\citet{ortiz2025}", keeping the key while making the author's name the subject because a parenthetical citation cannot serve as one.

> **Before.** \citep{ortiz2025} compares two methods for measuring rainfall.
>
> **After.** \citet{ortiz2025} compares two methods for measuring rainfall.

**Edit 2.** The draft uses natbib and treats the salt's solubility as established. The edit removes "In a recent study" and the report that Ortiz "showed" the result, states the result directly, and places "~\citep{ortiz2025}" after it, so that the sentence asserts the accepted fact with its source.

> **Before.** In a recent study, \citet{ortiz2025} showed that this salt dissolves in water.
>
> **After.** This salt dissolves in water~\citep{ortiz2025}.

**Edit 3.** The draft cites ortiz2025 for the shell's shrinkage and patel2024 for slower decay. The edit splits the trailing citation cluster and places each citation beside its clause, so that readers can tell which source supports each claim.

> **Before.** Drying shrinks the shell, and cooling slows decay~\citep{ortiz2025,patel2024}.
>
> **After.** Drying shrinks the shell~\citep{ortiz2025}, and cooling slows decay~\citep{patel2024}.

**Edit 4.** Elsewhere, the draft attributes the cooling hypothesis to its own authors. The edit, a proposal to the author after flagging the unclear attribution, adds "We hypothesize that" before the cooling claim, so that readers attribute the hypothesis to the paper's authors rather than Ortiz.

> **Before.** Ortiz reports that the shell shrinks. Cooling may reduce this effect.
>
> **After.** Ortiz reports that the shell shrinks. We hypothesize that cooling may reduce this effect.

**Edit 5.** The draft uses natbib, and the authors extend Ortiz's method. The edit replaces "\citep{ortiz2025}" with "the method of \citet{ortiz2025}", so that the object names what the authors extend; a parenthetical citation cannot be an object, and "\citet" alone would name a person.

> **Before.** We extend \citep{ortiz2025}.
>
> **After.** We extend the method of \citet{ortiz2025}.
