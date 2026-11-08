# Report variability and compare like with like

For each numerical comparison, check that the text states the number of runs, replicates, or samples, how they are aggregated, what ± means, and the source of variation, either beside the comparison or in a reporting convention; flag missing information. A best run is not comparable with a mean. Flag a comparison, including one with results borrowed from other papers, unless the text establishes that both sides use equivalent tasks, outputs, quality requirements, aggregation, and protocols. When a gain in one measure comes with a loss in another, state the trade-off; if the draft does not establish comparable performance on the other measure, flag the missing comparison.

Every percentage needs its base, and a reported change must specify whether it is a relative percentage change or a difference in percentage points. Edit the wording when the draft settles which one is meant; otherwise flag the ambiguity, and never relabel by guessing. Keep each ranking tied to its metric, and flag selective reporting.

Data used to select or tune a method cannot independently test that choice. Flag any claim of independent confirmation that rests on reused data, related datasets, or correlated metrics, unless the draft establishes a separate test. For misleading averages, systematic measurement errors (including timing bias), and how convergence error is measured and normalized, see the page.

## Details

Check whether an aggregate statistic supports the claim about typical behavior, since skew, missing outcomes, mixed sample sizes, or subgroup weights can change how the aggregate should be interpreted. Flag such a mismatch, and do not automatically replace a mean with another statistic.

Check the stated test conditions for sources of systematic bias, including calibration, environment, run order, and resolution, as well as compiler options, cache state, hardware, and clock resolution in software timings. Small variation across repeats shows consistency across runs, not the absence of systematic bias; flag any visible confound without inventing its cause.

Selective reporting includes an unexplained change of metric across datasets and a favorable summary that omits a conflicting metric reported in the draft.

Trace which data are used for discovery, tuning, and testing. Data that suggested a hypothesis cannot independently test it, though a held-out split from the same source can provide a separate test; shared origin alone does not establish reuse. Preserve exploratory findings and conclusions that do not depend on independent confirmation, and do not require preregistration.

For convergence claims, check that the reported quantity measures error rather than merely listing successive values. When errors or residuals depend on problem scale, check that the text defines their normalization; flag missing definitions rather than choosing a norm, computing replacement values, or rewriting a table.

## Examples

The draft compares two modes on the same photographs and reports that mode A produces smaller files but loses more image detail.

> Bad: Mode A produces smaller files than mode B.
>
> Good: Mode A produces smaller files than mode B but loses more image detail.

The draft explicitly defines the reported increase as a difference of four percentage points.

> Bad: The attendance rate increases by 4%.
>
> Good: The attendance rate increases by 4 percentage points.

The draft reports a mean across six independently prepared batches, with ± giving the standard deviation; the revision is proposed to the author.

> Bad: The yield is 72 ± 3%.
>
> Good: Across six independently prepared batches, the mean yield is 72 ± 3% (standard deviation).

The draft reports mean drying times of 8 and 9 min for paints A and B and a best time of 6 min for A; the revision is proposed to the author.

> Bad: Paint A's best drying time is 6 min, compared with paint B's mean of 9 min.
>
> Good: Paint A's mean drying time is 8 min, compared with paint B's mean of 9 min.

The draft states that Lee's tiles were tested dry and the present tiles were tested wet, so the results do not establish superiority; the revision is proposed to the author.

> Bad: Our tiles are stronger than Lee's tiles.
>
> Good: Our wet-tested tiles cannot be ranked against Lee's dry-tested tiles from these tests.

The draft defines the reported fraction as 40% of the seeds planted.

> Bad: Forty percent germinate.
>
> Good: Forty percent of the seeds planted germinate.

The draft ranks the jars by sealed storage life only.

> Bad: Jar A ranks first.
>
> Good: Jar A ranks first for sealed storage life.

The draft reports that filter A removes more dust but filter B removes more pollen; the revision is proposed to the author.

> Bad: Filter A outperforms filter B on particle removal.
>
> Good: Filter A removes more dust than filter B, but filter B removes more pollen.

The draft uses the same photographs to select and evaluate the filter; the revision is proposed to the author.

> Bad: The photographs independently confirm the selected filter's accuracy.
>
> Good: The photographs used to select the filter also measure its accuracy.

The draft states that total mass and mass per item use the same measurements and do not provide independent tests; the revision is proposed to the author.

> Bad: Total mass and mass per item independently confirm the reduction.
>
> Good: Total mass and mass per item show the reduction in the same measurements.

The draft states that distinct, independently sampled plots from one farm are reserved for selection and testing; the revision is proposed to the author.

> Bad: The test reuses the selection plots from the farm.
>
> Good: The test uses separate held-out plots from the farm.

The draft describes the observed association as exploratory and states that it was found in the same data used to propose it; the revision is proposed to the author.

> Bad: The data independently confirm the exploratory association.
>
> Good: The data suggest the exploratory association.

The draft reports a mean wait of 12 min and states that a few long waits make that mean unrepresentative of a typical wait; the revision is proposed to the author.

> Bad: A typical wait is 12 min.
>
> Good: The mean wait is 12 min.

The draft reports a small spread across repeats but leaves a known calibration offset uncorrected; the revision is proposed to the author.

> Bad: The small spread rules out measurement error.
>
> Good: The small spread shows little variation across repeats.

The draft times method A with warm caches and method B with cold caches, providing no comparable speed result; the revision is proposed to the author.

> Bad: Method A runs faster than method B.
>
> Good: Method A runs faster with warm caches than method B with cold caches.

The draft states that its convergence plot shows absolute error relative to the exact solution; the revision is proposed to the author.

> Bad: The convergence plot shows successive solution values.
>
> Good: The convergence plot shows absolute error relative to the exact solution.

The draft defines normalized error as absolute error divided by the exact solution's magnitude; the revision is proposed to the author.

> Bad: The normalized error falls below 0.01.
>
> Good: The normalized error, absolute error divided by the exact solution's magnitude, falls below 0.01.
