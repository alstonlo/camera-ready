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

**Edit 1.** The draft compares both modes on the same photographs and reports both outcomes. The edit adds "but loses more image detail", so that the comparison states the loss in image quality alongside the reduction in file size.

> **Before.** Mode A produces smaller files than mode B.
>
> **After.** Mode A produces smaller files than mode B but loses more image detail.

**Edit 2.** The draft describes independently prepared batches and supplies the batch count, averaging procedure, and meaning of ±. The edit identifies six independently prepared batches, labels the yield as a mean, and defines ± as standard deviation, so that readers know what was repeated and how the results were summarized.

> **Before.** The yield is 72 ± 3%.
>
> **After.** Across six independently prepared batches, the mean yield is 72 ± 3% (standard deviation).

**Edit 3.** The draft gives the test conditions for both sets of tiles. The edit names the wet and dry conditions and replaces the strength ranking with "These tests do not establish whether", because the different conditions do not establish a fair comparison.

> **Before.** Our tiles are stronger than Lee's tiles.
>
> **After.** These tests do not establish whether our tiles, tested wet, are stronger than Lee's tiles, tested dry.

**Edit 4.** The draft identifies the photographs used at each stage. The edit replaces "independently confirm" with a statement that accuracy is measured on the same photographs used for selection, because data that influenced the choice cannot independently confirm it.

> **Before.** The photographs independently confirm the selected filter's accuracy.
>
> **After.** The selected filter's accuracy is measured on the same photographs used to select it.

**Edit 5.** The draft describes separate, independently sampled plots for selection and testing. The edit replaces "reuses the selection plots" with "uses separate held-out plots", because coming from one farm does not make the plots the same data.

> **Before.** The test reuses the selection plots from the farm.
>
> **After.** The test uses separate held-out plots from the farm.

**Edit 6.** The draft leaves a known calibration error uncorrected. The edit replaces "rules out measurement error" with "shows little variation across repeats", because closely agreeing measurements can share the same error.

> **Before.** The small spread rules out measurement error.
>
> **After.** The small spread shows little variation across repeats.

**Edit 7.** The draft defines the increase as four percentage points. The edit replaces "4%" with "4 percentage points", so that the increase is stated as the difference between rates rather than a percentage of the starting rate.

> **Before.** The attendance rate increases by 4%.
>
> **After.** The attendance rate increases by 4 percentage points.
