# Citation markers are not nouns

A bracketed or parenthetical citation marker cannot be the subject or object of a sentence because it is not a noun. An author name is a noun and may be either.

In LaTeX, use `\citet` for textual citations and `\citep` for parenthetical ones, with a non-breaking space before the citation (`widgets~\citep{smith2001}`). Use "et al." only for three or more authors. Put the period on "al." only, and do not italicize the phrase.

Move a citation out of a lead-in when the sentence states an established result the text relies on ("In a recent study, Smith et al. (2015) showed that X" becomes "X (Smith et al., 2015)"). Keep the authors as the subject when the sentence characterizes, contrasts, or reports a claim of theirs that the text does not itself assert.

## Examples

- Bad: "[10] was the first..." / "(Smith, 2001) shows that..."
- Good: "Smith et al. [10] were the first..." / "Widgets reduce latency (Smith, 2001)." / "Smith (2001) shows that..."
