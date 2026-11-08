# Say what literally happens

Name the actual event, object, and quantity in the words you would use to explain them at a whiteboard.

- *Figurative verbs.* In descriptions such as a loader that "retires" malformed rows, results that "move", or a filter that "passes on" borderline examples, replace the figurative verb with the literal event: the rows are deleted, the accuracy drops, or the filter accepts (or rejects) the examples.
- *Nouns used as verbs.* When a noun is used as a verb for one occasion ("calendar it", "we footnote the caveat"), the reader must reanalyze the word as a verb and guess the action. Replace the word with a verb phrase that names the action ("add it to the calendar", "we state the caveat in a footnote"). Keep such a verb when the field uses it routinely ("we benchmark", "we cache the results"). Follow the [rule on parts of speech](../conventions/terminology.md) for technical terms.
- *Unusual word pairs.* When two words rarely appear together ("verified red", "a reader-patience budget"), the pair compresses an idea into a phrase the reader must decode. Replace the pair with the ordinary wording for the idea ("verified that the test fails on the original code"). Keep established technical collocations, however rare outside the field.
- *Phrasal verbs.* A verb with a particle ("carry out", "come up with", "figure out", and similar) has several meanings that its parts do not predict. Replace it with a single verb naming the operation ("run", "propose", "determine"), unless it is the standard term and no single verb has the same meaning.
- *Inflated words.* Write "use" for "utilize" or "leverage", and "try to determine" for "endeavor to ascertain".
- *Abstraction.* General nouns such as *approach, framework, strategy,* and *issue* describe an idea indirectly. For example, "we adopt a data-augmentation strategy to address the issue of overfitting" becomes "we augment the training data to reduce overfitting". Functional labels name an object by its role in the authors' setup ("the assessment word" for "the word *true* or *false*"). Name the object first, then its role if needed.

A technical term may still be the right word. Keep it and explain the literal operation at first use, as in "Losses above 10.0 are set to 10.0 before averaging (winsorization)."

## Examples

- Bad: "Losses above the threshold are winsorized."
- Good: "Losses above 10.0 are set to 10.0 before averaging (winsorization)."
