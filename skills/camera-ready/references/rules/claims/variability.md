# Report variability and compare like with like

For each numerical comparison, check that the draft states the number of runs, repetitions, or samples, how they were combined, what ± means, and what varied across runs. These details may appear beside the comparison or in a general statement; flag any that is missing. A best run is not comparable with a mean. Flag a comparison, including one with results from other papers, unless the draft establishes that both sides use equivalent tasks, outputs, quality requirements, aggregation, and procedures. When one measure improves and another worsens, state both changes. If the draft does not establish how the other measure compares, flag the missing comparison.

Check that the draft states what each percentage is of and whether a percentage change is relative or in percentage points. Edit the wording when the draft makes the meaning clear; otherwise, flag the ambiguity without guessing. Name the measure behind each ranking, and flag selective reporting.

Data used to select or tune a method cannot independently test it. Flag a claim of independent confirmation from reused data, related datasets, or correlated measures unless the draft establishes a separate test. For misleading averages, systematic measurement errors (including biased timings), and convergence error, see Details.

## Details

In a numerical comparison, the draft may state how runs or samples were combined (for example, by taking the mean) and what varied from one run to the next (such as the random seed or the sample batch) either beside the comparison or in a general statement about how it reports results. For percentages, a relative change is a percentage of the starting value (a rise from 50% to 55% is a 10% increase), whereas a change in percentage points is the arithmetic difference between the two percentages (5 percentage points).

Check whether a summary statistic, such as a mean, supports a claim about typical behavior. A skewed distribution (one with a long tail of extreme values on one side), missing outcomes, groups of different sizes, or subgroup weights can make a mean unrepresentative of a typical case. Flag a claim that the statistic does not support, and do not automatically replace a mean with another statistic.

Check the stated test conditions for systematic bias, meaning errors that push every measurement in the same direction rather than scattering them at random. Look at calibration, environment, the order of runs, and measurement resolution. For software timings, also look at compiler options, the state of the cache, hardware, and clock resolution. Small variation across repeats shows only that the runs agree with one another, not that they are free of systematic bias. Flag any stated condition that could bias the measurements or the comparison, and do not invent a cause for it.

Selective reporting includes switching to a different measure for some datasets without explaining why, and giving a favorable summary that leaves out a conflicting measure reported elsewhere in the draft.

Trace which data the draft uses to discover patterns, to select or tune the method, and to test it. Data that suggested a hypothesis cannot independently test it. A held-out subset reserved for testing can provide a separate test even when it comes from the same source as the other data; a shared source alone does not mean that the data were reused. Preserve exploratory findings and conclusions that do not depend on independent confirmation, and do not require preregistration (registering the study plan in advance).

For a claim that an iterative method converges, meaning that its successive estimates approach a solution, check that the draft reports a measure of error rather than only listing the successive estimates. When errors or residuals (the amounts by which an estimate fails to satisfy the equations) depend on the size or scale of the problem, check that the draft defines how it normalizes them to remove that scale. Flag a missing definition rather than choosing a norm (a measure of size), computing replacement values, or rewriting a table.

## Examples

**Example 1.** The draft compares two modes on the same photographs and reports that mode A produces smaller files but loses more image detail.

> **Bad.** Mode A produces smaller files than mode B.
>
> **Good.** Mode A produces smaller files than mode B but loses more image detail.

**Example 2.** The draft defines the increase as four percentage points.

> **Bad.** The attendance rate increases by 4%.
>
> **Good.** The attendance rate increases by 4 percentage points.

**Example 3.** The draft reports a mean across six independently prepared batches and defines ± as the standard deviation. The edit is a proposal for the author.

> **Bad.** The yield is 72 ± 3%.
>
> **Good.** Across six independently prepared batches, the mean yield is 72 ± 3% (standard deviation).

**Example 4.** The draft reports mean drying times of 8 min for paint A and 9 min for paint B, and a best time of 6 min for paint A. The edit is a proposal for the author.

> **Bad.** Paint A's best drying time is 6 min, compared with paint B's mean of 9 min.
>
> **Good.** Paint A's mean drying time is 8 min, compared with paint B's mean of 9 min.

**Example 5.** The draft states that Lee's tiles were tested dry and the authors' tiles were tested wet, so the tests do not establish which tiles are stronger. The edit is a proposal for the author.

> **Bad.** Our tiles are stronger than Lee's tiles.
>
> **Good.** These tests do not establish whether our tiles, tested wet, are stronger than Lee's tiles, tested dry.

**Example 6.** The draft states that 40% refers to the seeds planted.

> **Bad.** Forty percent germinate.
>
> **Good.** Forty percent of the seeds planted germinate.

**Example 7.** The draft ranks the jars by sealed storage life only.

> **Bad.** Jar A ranks first.
>
> **Good.** Jar A ranks first for sealed storage life.

**Example 8.** The draft reports that filter A removes more dust but filter B removes more pollen. The edit is a proposal for the author.

> **Bad.** Filter A outperforms filter B on particle removal.
>
> **Good.** Filter A removes more dust than filter B, but filter B removes more pollen.

**Example 9.** The draft describes using the same photographs to select and evaluate the filter. The edit is a proposal for the author.

> **Bad.** The photographs independently confirm the selected filter's accuracy.
>
> **Good.** The selected filter's accuracy is measured on the same photographs used to select it.

**Example 10.** The draft states that total mass and mass per item come from the same measurements, so they are not independent tests. The edit is a proposal for the author.

> **Bad.** Total mass and mass per item independently confirm the reduction.
>
> **Good.** Total mass and mass per item show the reduction, but both come from the same measurements.

**Example 11.** The draft describes reserving separate, independently sampled plots from one farm for selection and testing. The edit is a proposal for the author.

> **Bad.** The test reuses the selection plots from the farm.
>
> **Good.** The test uses separate held-out plots from the farm.

**Example 12.** The draft describes an exploratory association found in the same data used to propose it. The edit is a proposal for the author.

> **Bad.** The data independently confirm the exploratory association.
>
> **Good.** The data suggest the exploratory association.

**Example 13.** The draft reports a mean wait of 12 min but says that a few long waits make the mean unrepresentative of a typical wait. The edit is a proposal for the author.

> **Bad.** A typical wait is 12 min.
>
> **Good.** The mean wait is 12 min.

**Example 14.** The draft reports little variation across repeats but leaves a known error in instrument calibration uncorrected. The edit is a proposal for the author.

> **Bad.** The small spread rules out measurement error.
>
> **Good.** The small spread shows little variation across repeats.

**Example 15.** The draft times method A with its data already in the cache and method B with an empty cache. It gives no timings of the two methods under matching conditions. The edit is a proposal for the author.

> **Bad.** Method A runs faster than method B.
>
> **Good.** Method A runs faster with data already in the cache than method B with an empty cache.

**Example 16.** The draft says that its convergence plot shows the magnitude of the difference from the exact solution. The edit is a proposal for the author.

> **Bad.** The convergence plot shows successive solution values.
>
> **Good.** The convergence plot shows the magnitude of the difference from the exact solution.

**Example 17.** The draft defines normalized error as absolute error divided by the exact solution's magnitude. The edit is a proposal for the author.

> **Bad.** The normalized error falls below 0.01.
>
> **Good.** The normalized error is absolute error divided by the exact solution's magnitude. It falls below 0.01.
