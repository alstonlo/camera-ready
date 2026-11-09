# Spell out definitions and procedures

Explain each metric, rule, and procedure readers rely on, including how to interpret or reproduce its results. A definition must name the kind of thing and its distinguishing traits; expanding an acronym is not enough. Accompany formal definitions readers need with plain explanations; for related concepts, state both their shared category and their differences. When definitions compete, state which one the paper adopts and the draft's reason; neither invent competing definitions nor drop ones the draft mentions. Do not flag standard steps covered by a precise citation, but keep every modification and the explanation readers need at that point. When a procedure only lists steps, state its purpose from the draft, or flag the missing purpose. Check that worked examples match the stated method or definition, and flag mismatches rather than changing either. Apply the domain checks in Details (for algorithms, numerical work, experiments, data and samples, or human participants) only during a story check or an overclaiming check, or when a result depends on an unstated setting. Delete or move details needed for reproduction only where the [cutting rules](../cutting/sentence-dependencies.md) allow it. For an unclear explanation or an example without a stated purpose, see Details.

## Details

Repeating a term, or restating it with a word derived from it ("germination rate measures how well seeds germinate"), does not define it. Mark a definition explicitly ("we define") when readers could mistake it for a one-way implication, that is, a statement that the condition implies the property but not the reverse. Within an explicitly marked mathematical definition, "if" may mean "if and only if". Do not read "if" that way in ordinary statements, and do not delete wording that explicitly states that both directions hold.

Check the following details only during a story check or an overclaiming check, or when a result depends on a setting that the draft does not state. Flag any missing item. Never fill the gap with a plausible default, a standard condition, or a safeguard that you assume the authors used:

- **Algorithms:** Check that the draft states the task, the inputs and outputs, the types of variables whose type is not obvious, the data structures, the preconditions (what must be true of the input before the algorithm runs), the assumptions about the computing environment, and what happens when an error occurs. Check that each claim about correctness or cost has matching support, such as a proof or a measurement. Explain what the algorithm does at the level of ideas rather than narrating routine loop steps. If a brief step in code or mathematics hides a choice that decides the result, flag it without changing the code or formulas.
- **Numerical work:** Check that the draft states the floating-point precision, the distributions that inputs are sampled from, the random seeds or other settings that control randomness, the software versions, and any compiler or optimization settings that affect reported timings.
- **Experiments:** Check that the draft states the materials and their source or purity, how samples were prepared, which instruments were used and how they were calibrated, which conditions were held constant, the number of replicates, and the order of steps whenever that order affects the outcome.
- **Data or samples:** Check that the draft states the source, how the data or samples were collected or generated, the version, the inclusion criteria, the sampling method, the transformations and cleaning applied, the exclusions, the uncertainty in measurements or labels, and how readers can access or reconstruct the data.
- **Human participants or assessors:** Check that the draft states how participants or assessors were recruited, their relevant characteristics, the instructions or interventions they received, how the conditions being compared were assigned, and whether people were blinded (kept unaware of which condition they were in or rating) where knowing could affect the outcome. Also check that the draft states the sources of bias and how disagreement between raters was measured or resolved. Distinguish qualitative cases that only illustrate a point from controlled comparisons.

A citation can replace the description of standard steps only if it identifies the specific method used. A method name alone is not enough. A procedure that is new, disputed, or central to a contribution needs enough explanation in the paper itself for readers to judge it.

When you cannot follow an explanation, use an example already in the draft to find the missing step, or flag the gap. Do not add examples to prose that is already clear. State what each example illustrates. Start with a case from the draft that shows the operation on its own, and add complications from the draft only to explain a boundary case, such as a value exactly equal to a cutoff. Running two or more methods on the same input can show how they differ. If that input hides the difference, switch to another case from the draft. Never invent an outcome for any case. Check that each example meets the method's preconditions, applies its operations correctly, and gives the output that the method specifies. For broader claims, follow the rule on [evidence scope](../claims/scope.md).

## Examples

**Example 1.** The draft defines germination rate as the fraction of planted seeds that sprout within seven days.

> **Bad.** Germination rate measures how well seeds germinate.
>
> **Good.** Germination rate is the fraction of planted seeds that sprout within seven days.

**Example 2.** The draft follows Lee’s protocol but dries for 2 h, where Lee dries for 1 h. The Good line is a proposed revision for the author.

> **Bad.** We follow Lee’s protocol [4].
>
> **Good.** We follow Lee’s protocol [4], but dry for 2 h instead of 1 h.

**Example 3.** The draft says decanting separates the water from settled sand.

> **Bad.** We let the sand settle, then pour off the water.
>
> **Good.** To separate the water from the sand, we let the sand settle, then pour off the water.

**Example 4.** The draft defines mean mass as total mass divided by count and gives the correct mean of 3 g elsewhere. The editor flags the mismatch, and the Good line is the correction proposed to the author.

> **Bad.** For masses of 2 g and 4 g, the mean mass is 6 g.
>
> **Good.** For masses of 2 g and 4 g, the mean mass is 3 g.

**Example 5.** In the draft, this sentence is meant as the complete definition of a valid reading.

> **Bad.** A reading is valid if it lies between the two limits.
>
> **Good.** We define a reading as valid if it lies between the two limits.
