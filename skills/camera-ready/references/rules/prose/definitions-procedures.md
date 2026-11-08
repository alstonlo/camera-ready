# Spell out definitions and procedures

Explain each metric, rule, and procedure the reader relies on, including how to interpret or reproduce its results. A definition must identify the kind of thing named and what distinguishes it; an acronym expansion is not enough. Explain needed formal definitions in plain language. For related concepts, state their shared category and difference. When definitions compete, identify the adopted meaning and its stated justification; neither invent alternatives nor drop those stated. Do not flag standard steps covered by a precise citation, but keep every modification to them and the explanation readers need at that point. When an algorithm's description only restates its steps, state the purpose the draft gives, or flag that the purpose is missing. Check that worked examples match the stated method or definition; flag mismatches rather than changing either. For unclear explanations or examples with no stated purpose, use the page's diagnostics. Use the page's algorithm, numerical, dataset, or human-evaluation checks only during a story or claims check, or when a result depends on a missing setting. Delete or move reproducibility detail only where the [cutting rules](../cutting/sentence-by-sentence.md) allow it.

## Details

Identify the category a term belongs to and the property that separates it from related objects. Repeating an understood category can help; repeating an unclear word derived from the term does not define it. For contrasting definitions, state the shared category and the dimension of difference only when the definitions or surrounding draft establish them.

Mark a definition explicitly when readers could mistake it for a one-way implication. In a clearly marked mathematical definition, "if" can express definitional equivalence. This convention neither strengthens an ordinary implication nor licenses deleting explicit equivalence wording for brevity.

For a disputed operational definition, state the definition the draft selects and its reason. Distinguish technical and ordinary senses when the distinction matters. Flag an unexplained choice that changes evaluation or classification, while preserving stated alternatives without supplying a dispute absent from the draft.

The following checks apply only within a story or claims check, or to a setting needed to interpret a stated result. Do not demand these details from every paragraph during a polish.

- For an algorithm, check its task, inputs, outputs, nontrivial variable types, data structures, preconditions, relevant environment assumptions, and error behavior. Locate the correctness and cost support appropriate to the claim; do not demand the same kind of proof for every systems procedure.
- Explain conceptual operations instead of paraphrasing routine loop mechanics. When a compact step hides a choice that changes correctness, behavior, or cost, retain or recover that choice in the prose. Flag a missing decisive operation; leave protected code and formulas unchanged.
- For numerical work, check working precision, sampling distributions, relevant randomness settings, software versions, and compiler or optimization settings when timings depend on them. Do not fill gaps with plausible defaults.
- For a dataset, check its source or generation, version, selection, sampling, transformations, cleaning, exclusions, label uncertainty, and access or reconstruction. Explain stated limitations that affect interpretation without inventing bias or demanding irrelevant disclosures.
- For human evaluation, check participant or assessor selection, relevant characteristics, instructions, comparison design, blinding when it affects interpretation, and treatment of bias or annotation disagreement. Distinguish qualitative cases from controlled comparisons; do not presume that a safeguard was used.

A citation covers routine standard steps only when it identifies the method actually used and the paper states its modifications and relevant settings. A method name alone is insufficient. Novel, disputed, or contribution-defining procedures need enough local explanation to judge them. Do not delete existing reproducibility content merely because a citation also describes it.

When an explanation cannot be followed, use an example already in the draft to expose the missing step or flag that specific gap. State what the example illustrates. Start with an available case that isolates the operation, adding complications or contrasting cases from the draft only when they explain a boundary. Do not add examples merely to embellish clear prose.

A shared input can reveal differences between related algorithms, but use another supplied case when the first hides the relevant distinction. Do not fabricate outcomes for a reused input. Check preconditions, transformations, and output against the definition or method; a mismatch may be substantive, so flag it instead of adjusting either side. Whether an example supports a broader claim is governed by [evidence scope](../claims/scope.md).

## Examples

The draft defines germination rate as the fraction of planted seeds that sprout within seven days.

- Bad: Germination rate measures how well seeds germinate.
- Good: Germination rate is the fraction of planted seeds that sprout within seven days.
