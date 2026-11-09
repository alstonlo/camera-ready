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

**Example 2.** The draft defines drying time as the time until mass stops falling.

> **Bad.** DT stands for drying time.
>
> **Good.** DT stands for drying time, the time until mass stops falling.

**Example 3.** The draft defines m as total mass and n as the number of equal portions.

> **Bad.** Portion mass is m/n.
>
> **Good.** Portion mass is m/n, the total mass divided by the number of equal portions.

**Example 4.** The draft defines both rates as fractions of seeds, with germination counting sprouted seeds and emergence counting shoots above soil.

> **Bad.** Germination and emergence are two rates.
>
> **Good.** Germination and emergence are both fractions of seeds. Germination counts seeds that sprout. Emergence counts seeds that produce shoots above soil.

**Example 5.** The draft chooses to measure damage as visible cracks because imaging detects them.

> **Bad.** Damage can mean visible cracks or reduced strength. We measure damage.
>
> **Good.** Damage can mean visible cracks or reduced strength. We measure damage as visible cracks because imaging detects them.

**Example 6.** The draft follows Lee’s protocol but dries for 2 h, where Lee dries for 1 h. The Good line is a proposed revision for the author.

> **Bad.** We follow Lee’s protocol [4].
>
> **Good.** We follow Lee’s protocol [4], but dry for 2 h instead of 1 h.

**Example 7.** The draft says decanting separates the water from settled sand.

> **Bad.** We let the sand settle, then pour off the water.
>
> **Good.** To separate the water from the sand, we let the sand settle, then pour off the water.

**Example 8.** The draft defines mean mass as total mass divided by count and gives the correct mean of 3 g elsewhere. The editor flags the mismatch, and the Good line is the correction proposed to the author.

> **Bad.** For masses of 2 g and 4 g, the mean mass is 6 g.
>
> **Good.** For masses of 2 g and 4 g, the mean mass is 3 g.

**Example 9.** In the draft, this sentence is meant as the complete definition of a valid reading.

> **Bad.** A reading is valid if it lies between the two limits.
>
> **Good.** We define a reading as valid if it lies between the two limits.

**Example 10.** During an overclaiming check, the editor finds elsewhere in the draft that the input list must be sorted. The Good line is a proposed revision for the author.

> **Bad.** The search takes a list and returns the target’s position.
>
> **Good.** The search takes a sorted list and returns the target’s position.

**Example 11.** The draft says the loop totals the masses.

> **Bad.** The loop visits each mass and updates the variable.
>
> **Good.** The loop totals the masses.

**Example 12.** During an overclaiming check, the editor finds elsewhere in the draft that the error bound assumes 64-bit arithmetic. The Good line is a proposed revision for the author.

> **Bad.** The calculation’s error is below 0.001.
>
> **Good.** With 64-bit arithmetic, the calculation’s error is below 0.001.

**Example 13.** During a story check, the editor finds elsewhere in the draft that the leaves are dried at 60 °C. The Good line is a proposed revision for the author.

> **Bad.** We dry the leaves for 2 h.
>
> **Good.** We dry the leaves for 2 h at 60 °C.

**Example 14.** During an overclaiming check, the editor finds elsewhere in the draft that the apples were selected at random from the orchard. The Good line is a proposed revision for the author.

> **Bad.** We measure 20 apples.
>
> **Good.** We measure 20 apples selected at random from the orchard.

**Example 15.** During a story check, the editor finds elsewhere in the draft that participants were told to rate legibility. The Good line is a proposed revision for the author.

> **Bad.** Participants rate each label.
>
> **Good.** Participants rate each label’s legibility.

**Example 16.** The draft states the operation and gives an example of it: subtracting the mass of a 3 g empty jar from that of an 8 g filled jar gives 5 g of water.

> **Bad.** We obtain the water’s mass from the jar measurements.
>
> **Good.** We subtract the empty jar’s mass from the filled jar’s mass: 8 g minus 3 g gives 5 g of water.

**Example 17.** The draft uses the example to show what the method does when scores are tied.

> **Bad.** For scores of 4, 4, and 2, the method retains both scores of 4.
>
> **Good.** The scores 4, 4, and 2 illustrate how the method handles a tie: it retains both scores of 4.

**Example 18.** The draft supplies both test scores. The example is meant to distinguish a strict cutoff, which admits only scores above 5, from an inclusive cutoff, which also admits 5.

> **Bad.** To compare the cutoffs, we test a score of 6, which both admit.
>
> **Good.** To compare the cutoffs, we test a score of 5, which only the inclusive cutoff admits.
