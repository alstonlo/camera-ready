# Spell out definitions and procedures

Describe every metric, rule, or procedure readers rely on well enough to interpret and recompute its results, usually in one or two full sentences.

- Definitions: Name the kind of thing and its distinguishing traits; expanding an acronym is not enough. Pair formal definitions readers need with plain explanations. For related concepts, state their shared category and differences. When definitions compete, state which the paper adopts and the draft's reason, without inventing alternatives.
- Procedures: Do not flag standard steps covered by a precise citation. Keep every modification and the explanation readers need at that point. If a procedure only lists steps, state its purpose from the draft, or flag its absence.
- Settings: During a story or overclaiming check, or when a result depends on an unstated setting, check that the draft gives the settings its kind of work needs, such as algorithm preconditions, random seeds, software versions, calibration, data exclusions, or participant recruitment and blinding. Flag each missing item without supplying a plausible default. Delete or move details needed for reproduction only as the [cutting rules](../cutting/sentence-dependencies.md) allow.
- Hard explanations: When you cannot follow an explanation, use an example already in the draft to find the missing step, or flag the gap. Build difficult explanations from a simple case through necessary complications, using the draft's cases.
- Examples: Flag a worked example that does not match the stated method or definition, without changing either. Reuse an illustrative input across methods unless it hides their differences. Prefer an available real input that explains the operation; keep toy cases when they explain it better. State what each example illustrates without inventing outcomes.

## Details

- Definitions: Repeating a term or using a word derived from it does not define it. Mark a definition explicitly ("we define") when readers could mistake it for a one-way implication. In an explicitly marked mathematical definition, "if" may mean "if and only if". Do not read "if" that way in ordinary statements or delete wording that explicitly states both directions.
- Citations: A citation can replace a description of standard steps only if it identifies the specific method used; a method name alone is not enough. A new or disputed procedure, or one central to a contribution, needs enough explanation in the paper for readers to judge it.
- Examples: Do not add examples to clear prose. Check that each example meets the method's preconditions, applies its operations correctly, and gives the specified output. For broader claims, follow [evidence scope](../claims/scope.md).

Check that the draft states the settings below for each kind of work. Never supply a plausible default, standard condition, or assumed safeguard.

- Algorithms: Check the task, inputs and outputs, variable types that are not obvious, data structures, preconditions, assumptions about the computing environment, and error handling. Check that each correctness or cost claim has matching support, such as a proof or measurement. Explain the ideas rather than narrating routine loop steps. Flag any brief step in code or mathematics that hides a choice that decides the result, without changing the code or formulas.
- Numerical work: Check floating-point precision, input distributions, random seeds or other settings that control randomness, software versions, and compiler or optimization settings that affect reported timings.
- Experiments: Check materials and their source or purity, sample preparation, instruments and calibration, conditions held constant, the number of replicates, and step order whenever it affects the outcome.
- Data or samples: Check the source, collection or generation, version, inclusion criteria, sampling method, transformations and cleaning, exclusions, uncertainty in measurements or labels, and how readers can access or reconstruct the data.
- Human participants or assessors: Check recruitment, relevant characteristics, instructions or interventions, assignment to conditions, and whether participants or assessors were blinded where knowing the condition could affect the outcome. Check sources of bias and how disagreement between raters was measured or resolved. Distinguish qualitative illustrations from controlled comparisons.

## Examples

**Edit 1.** Suppose the draft defines germination rate elsewhere as the fraction of planted seeds that sprout within seven days.

> **Before.** Germination rate measures how well seeds germinate.

> **After.** Germination rate is the fraction of planted seeds that sprout within seven days.

**Edit 2.** Suppose the draft specifies 2 h for drying and gives 1 h as the time in Lee’s protocol.

> **Before.** We follow Lee’s protocol [4].

> **After.** We follow Lee’s protocol [4], but dry for 2 h instead of 1 h.

**Edit 3.** Suppose the draft states elsewhere that the procedure separates water from sand.

> **Before.** We let the sand settle, then pour off the water.

> **After.** To separate the water from the sand, we let the sand settle, then pour off the water.

**Edit 4.** Suppose the draft gives 3 g as the correct mean elsewhere. The editor flags the mismatch and proposes the edited text to the author.

> **Before.** For masses of 2 g and 4 g, the mean mass is 6 g.

> **After.** For masses of 2 g and 4 g, the mean mass is 3 g.

The proposed correction needs the author's review because it changes a worked result.

**Edit 5.** Suppose the author intends a complete definition.

> **Before.** A reading is valid if it lies between the two limits.

> **After.** We define a reading as valid if it lies between the two limits.
