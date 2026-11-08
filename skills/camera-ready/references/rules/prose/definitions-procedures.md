# Spell out definitions and procedures

Explain each metric, rule, and procedure the reader relies on, including how to interpret or reproduce its results. A definition must identify the kind of thing named and what distinguishes it; an acronym expansion is not enough. Accompany formal definitions that the reader needs with a plain-language explanation, and for related concepts, state both their shared category and how they differ. When definitions compete, state which meaning the paper adopts and its justification from the draft; neither invent competing definitions nor drop ones the draft mentions. Do not flag standard steps covered by a precise citation, but keep every modification to them and the explanation readers need at that point. When a procedure's description only lists its steps, state the purpose the draft gives, or flag that the purpose is missing. Check that worked examples match the stated method or definition, and flag mismatches rather than changing either. Use the diagnostics in Details when an explanation is hard to follow or an example lacks a stated purpose. Apply the domain checks in Details (for algorithms, numerical work, experiments, data and samples, or human participants) only during a story or claims check, or when a result depends on a missing setting. Delete or move reproducibility detail only where the [cutting rules](../cutting/sentence-dependencies.md) allow it.

## Details

Restating a term with a word derived from it does not define it. Mark a definition explicitly when a reader could mistake it for a one-way implication. Within a marked mathematical definition, "if" may stand for equivalence, but do not treat "if" as equivalence in ordinary statements or delete explicit equivalence wording.

Check whether the draft specifies the details needed for its kind of work only during a story or claims check, or when a result depends on an unstated setting. Flag any missing item, and never fill it with a plausible default, a standard condition, or a presumed safeguard:

- **Algorithms:** Check that the draft states the task, inputs, outputs, nontrivial variable types, data structures, preconditions, environment assumptions, and error behavior, and that claims of correctness or cost have matching support. Explain what the algorithm does conceptually rather than narrating routine loop mechanics. If a compact step in code or math hides a decisive choice, flag it without changing the code or formulas.
- **Numerical work:** Check that the draft states the working precision, sampling distributions, randomness settings, software versions, and any compiler or optimization settings that affect reported timings.
- **Experiments:** Check that the draft states the materials and their source or purity, sample preparation, instruments and calibration, controlled conditions, replicates, and the order of steps whenever that order affects the outcome.
- **Data or samples:** Check that the draft states the source, how the data or samples were collected or generated, the version, inclusion criteria, sampling method, transformations, cleaning, exclusions, uncertainty in measurements or labels, and how readers can access or reconstruct the data.
- **Human participants or assessors:** Check that the draft states how participants or assessors were recruited, their relevant characteristics, the instructions or interventions they received, the comparison design, whether blinding was used where it could affect the outcome, sources of bias, and how rater disagreement was measured or resolved. Distinguish illustrative qualitative cases from controlled comparisons.

A citation covers standard steps only if it identifies the specific method used; a method name alone is not enough. Procedures that are novel, disputed, or central to a contribution need enough explanation in the text for readers to judge them.

When an explanation cannot be followed, use an example already in the draft to locate the missing step, or flag the gap; do not add examples to prose that is already clear. State what each example illustrates. Start with a case from the draft that isolates the operation, and add supplied complications only to explain a boundary case. Running two or more methods on a shared input can clarify how they differ, but if that input hides the distinction, switch to another case from the draft, and never invent an outcome for any case. Check that each example matches the method's preconditions, transformations, and output, and follow [evidence scope](../claims/scope.md) for broader claims.

## Examples

The draft defines germination rate as the fraction of planted seeds that sprout within seven days.

> Bad: Germination rate measures how well seeds germinate.
>
> Good: Germination rate is the fraction of planted seeds that sprout within seven days.

The draft defines drying time as the time until mass stops falling.

> Bad: DT stands for drying time.
>
> Good: DT stands for drying time, the time until mass stops falling.

The draft defines m as total mass and n as the number of equal portions.

> Bad: Portion mass is m/n.
>
> Good: Portion mass is m/n, the total mass divided by the number of equal portions.

The draft defines both rates as fractions of seeds: germination counts sprouts, and emergence counts shoots above soil.

> Bad: Germination and emergence are two rates.
>
> Good: Germination and emergence are fractions of seeds: germination counts sprouts, and emergence counts shoots above soil.

The draft chooses visible cracks because imaging detects them.

> Bad: Damage can mean visible cracks or reduced strength. We measure damage.
>
> Good: Damage can mean visible cracks or reduced strength. We measure damage as visible cracks because imaging detects them.

The draft modifies Lee’s protocol by drying for 2 h instead of 1 h; Good is the proposed revision.

> Bad: We follow Lee’s protocol [4].
>
> Good: We follow Lee’s protocol [4], but dry for 2 h instead of 1 h.

The draft says decanting separates the water from settled sand.

> Bad: We let the sand settle, then pour off the water.
>
> Good: To separate the water from the sand, we let the sand settle, then pour off the water.

The draft defines mean mass as total mass divided by count and states the correct mean of 3 g elsewhere; Good is the correction proposed to the author.

> Bad: For masses of 2 g and 4 g, the mean mass is 6 g.
>
> Good: For masses of 2 g and 4 g, the mean mass is 3 g.

The draft intends this sentence as the full definition of a valid reading.

> Bad: A reading is valid if it lies between the two limits.
>
> Good: We define a reading as valid if it lies between the two limits.

During a claims check, you find elsewhere in the draft that the input list must be sorted; Good is the proposed revision.

> Bad: The search takes a list and returns the target’s position.
>
> Good: The search takes a sorted list and returns the target’s position.

The draft says the loop totals the masses.

> Bad: The loop visits each mass and updates the variable.
>
> Good: The loop totals the masses.

During a claims check, you find elsewhere in the draft that the error bound uses 64-bit arithmetic; Good is the proposed revision.

> Bad: The calculation’s error is below 0.001.
>
> Good: With 64-bit arithmetic, the calculation’s error is below 0.001.

During a story check, you find elsewhere in the draft that the leaves are dried at 60 °C; Good is the proposed revision.

> Bad: We dry the leaves for 2 h.
>
> Good: We dry the leaves for 2 h at 60 °C.

During a claims check, you find elsewhere in the draft that the apples were selected at random from the orchard; Good is the proposed revision.

> Bad: We measure 20 apples.
>
> Good: We measure 20 apples selected at random from the orchard.

During a story check, you find elsewhere in the draft that participants were instructed to rate legibility; Good is the proposed revision.

> Bad: Participants rate each label.
>
> Good: Participants rate each label’s legibility.

The draft supplies the operation and an example: an 8 g filled jar and a 3 g empty jar give 5 g of water.

> Bad: We obtain the water’s mass from the jar measurements.
>
> Good: We subtract the empty jar’s mass from the filled jar’s mass: 8 g minus 3 g gives 5 g of water.

The draft says this example demonstrates the method’s handling of ties.

> Bad: For scores of 4, 4, and 2, the method retains both scores of 4.
>
> Good: To illustrate tie handling, for scores of 4, 4, and 2, the method retains both scores of 4.

The draft supplies both cases, and the example is meant to distinguish a strict cutoff above 5 from an inclusive cutoff at 5.

> Bad: To compare the cutoffs, we test a score of 6, which both admit.
>
> Good: To compare the cutoffs, we test a score of 5, which only the inclusive cutoff admits.
