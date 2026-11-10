# Report variability and compare like with like

For each numerical comparison, check that the draft states the following beside it or in a general statement. Flag missing information:

- The number of runs, repetitions, or samples.
- How they were combined, such as by mean, median, or best run. A best run is not comparable with a mean.
- Whether ± is a standard deviation, standard error, or confidence interval.
- What varied, such as the random seed, data split, or resampled test examples.

Also check the following:

- Flag a comparison, including one with other papers' results, unless the draft establishes that both sides use equivalent tasks, outputs, quality requirements, aggregation, and procedures.
- When one measure improves and another worsens, state both changes, or flag the missing comparison.
- Check what each percentage is of and whether a percentage change is relative or in percentage points. Clarify the wording from the draft, or flag the ambiguity.
- Name the measure behind each ranking, and flag selective reporting.
- Flag a claim of independent confirmation from data used to generate a hypothesis, select or tune the method, related datasets, or correlated measures unless the draft establishes a separate test.
- Flag a mean that a skewed distribution, missing outcomes, or unequal groups make unrepresentative of a typical case.
- Flag a stated test condition that could push every measurement in the same direction, such as calibration or a warm cache.
- Flag a convergence claim supported only by successive estimates rather than a measure of error.

## Details

- Percentages: A relative change is a percentage of the starting value. A change in percentage points is the difference between the percentages. A rise from 50% to 55% is a 10% increase, or 5 percentage points.
- Typical behavior: Check whether the summary statistic supports the claim. A skewed distribution, missing outcomes, unequal group sizes, or subgroup weights can make a mean unrepresentative. Flag unsupported claims without automatically replacing the mean with another statistic.
- Systematic bias: Check calibration, environment, run order, and measurement resolution for conditions that could push measurements in the same direction. For software timings, also check compiler options, cache state, hardware, and clock resolution. Small variation across repeats establishes agreement, not freedom from bias. Flag stated conditions that could bias the measurements or comparison without inventing a cause.
- Selective reporting: Check for unexplained changes of measure across datasets and favorable summaries that omit a conflicting measure reported elsewhere in the draft.
- Independent confirmation: Trace which data the draft uses to discover patterns, select or tune the method, and test it. A held-out subset reserved for testing can provide a separate test even when it shares a source with the other data. Preserve exploratory findings and conclusions that do not depend on independent confirmation. Do not require preregistration.
- Convergence: Check that the draft reports a measure of error rather than only successive estimates. If errors or residuals depend on problem size or scale, check that the draft defines how it normalizes them. Flag a missing definition without choosing a norm, computing replacement values, or rewriting a table.

## Examples

**Edit 1.** Suppose the draft compares both modes on the same photographs and reports that mode A loses more image detail than mode B.

> **Before.** Mode A produces smaller files than mode B.

> **After.** Mode A produces smaller files than mode B but loses more image detail.

**Edit 2.** Say the draft gives the mean yield for six independently prepared batches and defines ± as standard deviation.

> **Before.** The yield is 72 ± 3%.

> **After.** Across six independently prepared batches, the mean yield is 72 ± 3% (standard deviation).

**Edit 3.** Imagine the draft says the authors tested their tiles wet, while Lee's tiles were tested dry.

> **Before.** Our tiles are stronger than Lee's tiles.

Flag the comparison for the author: the tiles were tested under different conditions, so these tests do not establish which tiles are stronger.

**Edit 4.** Suppose the draft uses the same photographs to select the filter and measure its accuracy.

> **Before.** The photographs independently confirm the selected filter's accuracy.

Flag the claim for the author: photographs used to select the filter cannot independently confirm its accuracy.

**Edit 5.** Say the draft describes separate, independently sampled plots for selection and held-out testing.

> **Before.** The test reuses the selection plots from the farm.

> **After.** The test uses separate held-out plots from the farm.

Plots from the same farm can still provide a separate test; a shared source does not make them the same data.

**Edit 6.** Suppose the draft reports a known calibration error that went uncorrected.

> **Before.** The small spread rules out measurement error.

> **After.** The small spread shows little variation across repeats.

**Edit 7.** Here the draft defines the increase as four percentage points.

> **Before.** The attendance rate increases by 4%.

> **After.** The attendance rate increases by 4 percentage points.
