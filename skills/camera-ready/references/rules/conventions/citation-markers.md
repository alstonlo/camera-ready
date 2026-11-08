# Keep citation markers out of subject and object positions

A bracketed or parenthetical citation marker is not a noun. Replace "[8] introduces" with a textual citation (`\citet{key}` in LaTeX), keeping the key. For an established result the paper asserts, shorten "In a recent study, ... showed that X" to "X (citation)"; keep the authors as the subject when the sentence reports, characterizes, or contrasts a claim the paper does not itself assert, following [prior work](../story/prior-work.md). When the draft shows which source supports which clause, place each citation beside that clause; otherwise flag a trailing cluster that leaves several claims' sources unclear. Flag a passage where the draft leaves unclear how far a source's material extends. For citation commands, author-name formatting, and attribution across sentences, see the page.

## Details

Temporarily remove a parenthetical marker and check whether the sentence is still grammatical. An author name in the sentence cannot be removed in that test. If a parenthetical marker needlessly splits a verb phrase, move it, keeping it attached to the same claim.

Use the textual and parenthetical citation commands supported by the document's citation system. With natbib, these are `\citet` and `\citep`; do not assume that another package provides them. Keep citation keys intact when changing a command. Use a non-breaking space before a parenthetical citation, as in `protocol~\citep{key}`. Use "et al." only for three or more authors, put the period on "al." only, and do not italicize it.

If a sentence reports claims from different sources, attach the relevant citation to each clause. Across a longer summary, use explicit attribution to show where a source's contribution ends and the paper's own interpretation begins. A final citation must not leave readers guessing whether it supports one sentence or the whole paragraph. Keep each source's qualifications when adjusting that wording.

## Examples

The draft uses natbib and supplies the key ortiz2025 for a single-author paper.

- Bad: \citep{ortiz2025} compares two methods for measuring rainfall.
- Good: \citet{ortiz2025} compares two methods for measuring rainfall.
