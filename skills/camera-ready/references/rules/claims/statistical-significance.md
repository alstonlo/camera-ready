# Draw only the conclusions a statistical test supports

Use *significant* only for a named statistical test, reported with its p-value or significance level and any effect size in the draft; flag any that is missing. When *significant* means large or important, replace it with the reported magnitude. Keep available effect and uncertainty estimates even when the result is not significant. A p-value is the probability of observing results at least as extreme as those measured if the null hypothesis and test assumptions hold, not the probability that a hypothesis is true. Preserve the tested hypothesis and the test's direction. Failing to reject the null hypothesis does not establish equality, and statistical significance does not establish practical importance. Interval overlap alone does not show whether one result is better; flag any such claim made without a test. When the draft tests significance across several datasets, outcomes, or measures, flag a missing multiple-comparison correction. For p-value thresholds and statistical power, see Details.

## Details

A statistical test starts from a null hypothesis, such as "the two groups have equal means", and a significance level, which is the p-value threshold below which a result counts as significant. The test's direction is whether it checks for lower values, higher values, or a difference in either direction. Keep a numeric p-value when the draft supplies one rather than replacing it with a threshold such as p < 0.05. When the draft gives only a bound or significance level, keep that statement without rounding or recomputing it.

Statistical power is the probability that a test detects an effect of a given size when that effect exists. Because power depends on the sample size, the variability of the data, and the size of the effect of interest, a result that is not significant does not by itself show that the test had too little power. Never choose a replacement statistical test or invent a correction for multiple comparisons that the draft does not state.

## Examples

**Edit 1.** The draft sets the significance level at 0.05 and tests for a difference in mean drying times. The edit replaces "are equal for" with "do not differ significantly between" while keeping the test and p-value, because a nonsignificant result does not establish equality.

> **Before.** Mean drying times are equal for paints A and B (Welch's t-test, p = 0.18).
>
> **After.** Mean drying times do not differ significantly between paints A and B (Welch's t-test, p = 0.18).

**Edit 2.** The draft reports the reduction but no statistical test. The edit replaces "significantly" with "by 2 min" so that the sentence gives the measured reduction without implying a statistical test.

> **Before.** Paint A reduces drying time significantly.
>
> **After.** Paint A reduces drying time by 2 min.

**Edit 3.** The draft reports the estimate and confidence interval elsewhere. The edit adds the estimated difference of 2 min and its 95% confidence interval from −1 to 5 min before the unchanged test result, so that readers can see the effect's size and uncertainty even though it is not significant.

> **Before.** The difference is not significant (Welch's t-test, p = 0.18).
>
> **After.** The estimated difference is 2 min, with a 95% confidence interval from −1 to 5 min. The difference is not significant (Welch's t-test, p = 0.18).

**Edit 4.** The draft reports p = 0.03 for a test of equal mean masses. The edit replaces the probability that the null hypothesis is true with the probability of results at least as extreme as those observed, conditional on equal mean masses and the test's assumptions, so that 0.03 has its correct meaning as a p-value.

> **Before.** The probability that the equal-means null is true is 0.03.
>
> **After.** If mean masses are equal and the test's assumptions hold, the probability of results at least as extreme as those observed is 0.03.

**Edit 5.** The draft establishes statistical significance but gives no evidence of practical importance. The edit replaces "practically important" with "statistically significant" while keeping the difference, test, and p-value, so that the claim stays within the evidence.

> **Before.** The 0.1 s difference is practically important (Welch's t-test, p = 0.01).
>
> **After.** The 0.1 s difference is statistically significant (Welch's t-test, p = 0.01).
