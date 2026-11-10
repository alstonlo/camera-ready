# Draw only the conclusions a statistical test supports

Use *significant* only for a named statistical test, reported with its p-value or significance level and any effect size in the draft; flag any that is missing. Where *significant* means large or important, replace it with the reported magnitude. Keep the draft's effect and uncertainty estimates even for a result that is not significant, and use the numeric p-value that the draft reports anywhere rather than a threshold such as p < 0.05. Preserve the tested hypothesis and the test's direction.

Check for these misreadings:

- A p-value is not the probability that a hypothesis is true.
- Failing to reject the null hypothesis does not establish equality: replace "the two methods perform the same (paired bootstrap, p = 0.21)" with "we find no significant difference between the two methods (paired bootstrap, p = 0.21)".
- Significance does not establish practical importance.
- A result that is not significant does not by itself show that the test had too little power.
- Flag a claim about whether one result is better that rests only on interval overlap, without a test.

When the draft tests significance across several datasets, outcomes, or measures, flag a missing account of how it handles multiple comparisons.

## Details

A statistical test starts from a null hypothesis, such as "the two groups have equal means", and a significance level, which is the p-value threshold below which a result counts as significant. The test's direction is whether it checks for lower values, higher values, or a difference in either direction. When the draft gives only a bound or significance level, keep that statement without rounding or recomputing it.

Statistical power is the probability that a test detects an effect of a given size when that effect exists. Power depends on the sample size, the variability of the data, and the size of the effect of interest. Never choose a replacement statistical test or invent a correction for multiple comparisons that the draft does not state.

## Examples

**Edit 1.** Suppose the draft sets the significance level at 0.05 and tests for a difference in mean drying times.

> **Before.** Mean drying times are equal for paints A and B (Welch's t-test, p = 0.18).

> **After.** Mean drying times do not differ significantly between paints A and B (Welch's t-test, p = 0.18).

**Edit 2.** Say the draft reports a 2 min reduction in drying time but gives no statistical test.

> **Before.** Paint A reduces drying time significantly.

> **After.** Paint A reduces drying time by 2 min.

**Edit 3.** Suppose the draft gives an estimated difference of 2 min with a 95% confidence interval from −1 to 5 min elsewhere.

> **Before.** The difference is not significant (Welch's t-test, p = 0.18).

> **After.** The estimated difference is 2 min, with a 95% confidence interval from −1 to 5 min. The difference is not significant (Welch's t-test, p = 0.18).

**Edit 4.** Imagine that the draft reports p = 0.03 for a test of equal mean masses.

> **Before.** The probability that the equal-means null is true is 0.03.

> **After.** If mean masses are equal and the test's assumptions hold, the probability of results at least as extreme as those observed is 0.03.

**Edit 5.** Here the draft establishes statistical significance but gives no evidence of practical importance.

> **Before.** The 0.1 s difference is practically important (Welch's t-test, p = 0.01).

> **After.** The 0.1 s difference is statistically significant (Welch's t-test, p = 0.01).
