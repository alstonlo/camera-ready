# Spell out definitions and procedures

Describe every metric, rule, or procedure readers rely on well enough to interpret and recompute its results, usually in one or two full sentences.

- **Definitions.** A definition must name the kind of thing and its distinguishing traits; expanding an acronym is not enough. Pair formal definitions readers need with plain explanations, and for related concepts, state their shared category and their differences. When definitions compete, state which one the paper adopts and the draft's reason, without inventing competing definitions.
- **Procedures.** Do not flag standard steps covered by a precise citation, but keep every modification and the explanation readers need at that point. For a procedure that only lists steps, state its purpose from the draft, or flag it.
- **Settings.** During a story or overclaiming check, or when a result depends on an unstated setting, check that the draft states the settings its kind of work needs, such as an algorithm's preconditions, the seeds and software versions of numerical work, an experiment's calibration, data exclusions, or how participants were recruited and blinded; flag each missing item without filling in a plausible default. Delete or move details needed for reproduction only where the [cutting rules](../cutting/sentence-dependencies.md) allow it.
- **Hard explanations.** When you cannot follow an explanation, find the missing step with an example already in the draft, or flag the gap. Build difficult explanations from a simple case through necessary complications, using cases from the draft.
- **Examples.** Flag a worked example that does not match the stated method or definition, without changing either. Reuse an illustrative input across methods unless it hides their differences. Prefer an available real input that explains the operation; retain toy cases when they explain it better. State what each example illustrates without inventing an outcome for any case.

## Details

Repeating a term, or restating it with a word derived from it ("germination rate measures how well seeds germinate"), does not define it. Mark a definition explicitly ("we define") when readers could mistake it for a one-way implication, that is, a statement that the condition implies the property but not the reverse. Within an explicitly marked mathematical definition, "if" may mean "if and only if". Do not read "if" that way in ordinary statements, and do not delete wording that explicitly states that both directions hold.

The settings to check for each kind of work are listed below. Never fill a gap with a plausible default, a standard condition, or a safeguard that you assume the authors used.

- **Algorithms:** Check that the draft states the task, the inputs and outputs, the types of variables whose type is not obvious, the data structures, the preconditions (what must be true of the input before the algorithm runs), the assumptions about the computing environment, and what happens when an error occurs. Check that each claim about correctness or cost has matching support, such as a proof or a measurement. Explain what the algorithm does at the level of ideas rather than narrating routine loop steps. If a brief step in code or mathematics hides a choice that decides the result, flag it without changing the code or formulas.
- **Numerical work:** Check that the draft states the floating-point precision, the distributions that inputs are sampled from, the random seeds or other settings that control randomness, the software versions, and any compiler or optimization settings that affect reported timings.
- **Experiments:** Check that the draft states the materials and their source or purity, how samples were prepared, which instruments were used and how they were calibrated, which conditions were held constant, the number of replicates, and the order of steps whenever that order affects the outcome.
- **Data or samples:** Check that the draft states the source, how the data or samples were collected or generated, the version, the inclusion criteria, the sampling method, the transformations and cleaning applied, the exclusions, the uncertainty in measurements or labels, and how readers can access or reconstruct the data.
- **Human participants or assessors:** Check that the draft states how participants or assessors were recruited, their relevant characteristics, the instructions or interventions they received, how the conditions being compared were assigned, and whether people were blinded (kept unaware of which condition they were in or rating) where knowing could affect the outcome. Also check that the draft states the sources of bias and how disagreement between raters was measured or resolved. Distinguish qualitative cases that only illustrate a point from controlled comparisons.

A citation can replace the description of standard steps only if it identifies the specific method used. A method name alone is not enough. A procedure that is new, disputed, or central to a contribution needs enough explanation in the paper itself for readers to judge it.

Do not add examples to prose that is already clear. Check that each example meets the method's preconditions, applies its operations correctly, and gives the output that the method specifies. For broader claims, follow the rule on [evidence scope](../claims/scope.md).

## Examples

**Edit 1.** Suppose the draft defines germination rate elsewhere as the fraction of planted seeds that sprout within seven days.

> **Before.** Germination rate measures how well seeds germinate.

> **After.** Germination rate is the fraction of planted seeds that sprout within seven days.

**Edit 2.** Say the draft specifies 2 h for drying and gives 1 h as the time in Lee’s protocol.

> **Before.** We follow Lee’s protocol [4].

> **After.** We follow Lee’s protocol [4], but dry for 2 h instead of 1 h.

**Edit 3.** Imagine another passage in the draft states that the procedure separates water from sand.

> **Before.** We let the sand settle, then pour off the water.

> **After.** To separate the water from the sand, we let the sand settle, then pour off the water.

**Edit 4.** Suppose the draft gives 3 g as the correct mean elsewhere; the editor flags the mismatch and proposes After to the author.

> **Before.** For masses of 2 g and 4 g, the mean mass is 6 g.

> **After.** For masses of 2 g and 4 g, the mean mass is 3 g.

The proposed correction needs the author's review because it changes a worked result.

**Edit 5.** Suppose the author intends a complete definition.

> **Before.** A reading is valid if it lies between the two limits.

> **After.** We define a reading as valid if it lies between the two limits.
