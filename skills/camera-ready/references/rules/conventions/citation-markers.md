# Keep citation markers out of subject and object positions

- Replace a citation marker used as a subject or object ("[8] introduces") with a textual citation that names the authors.
- When asserting an established result, shorten "In a recent study, ... showed that X" to "X (citation)". Keep cited authors as the subject when reporting, characterizing, or contrasting a claim the paper does not assert, following [prior work](../story/prior-work-comparisons.md).
- Place each citation beside the clause it supports when the draft identifies the connection; otherwise, flag a trailing cluster that obscures which source supports which claim. Flag any passage that leaves unclear where a source's material begins or ends.
- Use the document's citation package commands, such as natbib's `\citet` (textual) and `\citep` (parenthetical), with a non-breaking space before a parenthetical citation (`result~\citep{key}`).
- Use upright "et al." only for three or more authors.

## Details

- Marker placement: Temporarily remove a parenthetical or bracketed marker and check that the remaining words form a grammatical sentence. If a marker splits a verb phrase ("has~\citep{key} dissolved"), move it after the full verb phrase without changing which claim it supports.
- Attribution: Follow [prior work](../story/prior-work-comparisons.md) to preserve the source's qualifications.

## Examples

**Edit 1.** Suppose the draft uses natbib, and ortiz2025 has one author.

> **Before.** \citep{ortiz2025} compares two methods for measuring rainfall.

> **After.** \citet{ortiz2025} compares two methods for measuring rainfall.

**Edit 2.** Say the draft uses natbib and treats the salt's solubility as established.

> **Before.** In a recent study, \citet{ortiz2025} showed that this salt dissolves in water.

> **After.** This salt dissolves in water~\citep{ortiz2025}.

**Edit 3.** Suppose the draft identifies ortiz2025 as the source for the shell's shrinkage and patel2024 as the source for slower decay.

> **Before.** Drying shrinks the shell, and cooling slows decay~\citep{ortiz2025,patel2024}.

> **After.** Drying shrinks the shell~\citep{ortiz2025}, and cooling slows decay~\citep{patel2024}.

**Edit 4.** Suppose the draft elsewhere attributes the cooling hypothesis to the paper's authors. After proposes a clarification to the author.

> **Before.** Ortiz reports that the shell shrinks. Cooling may reduce this effect.

> **After.** Ortiz reports that the shell shrinks. We hypothesize that cooling may reduce this effect.

