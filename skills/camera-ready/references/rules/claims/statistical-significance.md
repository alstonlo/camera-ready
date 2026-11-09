# Draw only the conclusions a statistical test supports

Use *significant* only for a named statistical test, reported with its p-value or significance level and any effect size in the draft; flag any that is missing. When *significant* means large or important, replace it with the reported magnitude. Keep available effect and uncertainty estimates even when the result is not significant. A p-value is the probability of observing results at least as extreme as those measured if the null hypothesis and test assumptions hold, not the probability that a hypothesis is true. Preserve the tested hypothesis and the test's direction. Failing to reject the null hypothesis does not establish equality, and statistical significance does not establish practical importance. Interval overlap alone does not show whether one result is better; flag any such claim made without a test. When the draft tests significance across several datasets, outcomes, or measures, flag a missing multiple-comparison correction. For p-value thresholds and statistical power, see Details.

## Details

A statistical test starts from a null hypothesis, such as "the two groups have equal means", and a significance level, which is the p-value threshold below which a result counts as significant. The test's direction is whether it checks for lower values, higher values, or a difference in either direction. Keep a numeric p-value when the draft supplies one rather than replacing it with a threshold such as p < 0.05. When the draft gives only a bound or significance level, keep that statement without rounding or recomputing it.

Statistical power is the probability that a test detects an effect of a given size when that effect exists. Because power depends on the sample size, the variability of the data, and the size of the effect of interest, a result that is not significant does not by itself show that the test had too little power. Never choose a replacement statistical test or invent a correction for multiple comparisons that the draft does not state.

## Examples

> **Context.** The draft sets the significance level at 0.05 and tests whether mean drying times differ, not whether they are equivalent. The edit is a proposal for the author.
>
> **Bad.** Mean drying times are equal for paints A and B (Welch's t-test, p = 0.18).
>
> **Good.** Mean drying times do not differ significantly between paints A and B (Welch's t-test, p = 0.18).

> **Context.** The draft reports a 2 min reduction in drying time and uses "significant" to mean large, without a statistical test.
>
> **Bad.** Paint A reduces drying time significantly.
>
> **Good.** Paint A reduces drying time by 2 min.

> **Context.** The draft reports p = 0.02 from Welch's t-test for a difference in means in either direction. The edit is a proposal for the author.
>
> **Bad.** Mean drying times differ significantly.
>
> **Good.** Mean drying times differ significantly (two-sided Welch's t-test, p = 0.02).

> **Context.** The draft estimates the difference at 2 min, with a 95% confidence interval from −1 to 5 min. The edit is a proposal for the author.
>
> **Bad.** The difference is not significant (Welch's t-test, p = 0.18).
>
> **Good.** The estimated difference is 2 min, with a 95% confidence interval from −1 to 5 min. The difference is not significant (Welch's t-test, p = 0.18).

> **Context.** The draft tests the null hypothesis that mean masses are equal and reports p = 0.03. The edit is a proposal for the author.
>
> **Bad.** The probability that the equal-means null is true is 0.03.
>
> **Good.** If mean masses are equal and the test's assumptions hold, the probability of results at least as extreme as those observed is 0.03.

> **Context.** The draft tests for lower mean wear only. The edit is a proposal for the author.
>
> **Bad.** The test assesses whether mean wear differs.
>
> **Good.** The test assesses whether mean wear is lower.

> **Context.** The draft reports a statistically significant difference of 0.1 s but does not establish that it matters in practice. The edit is a proposal for the author.
>
> **Bad.** The 0.1 s difference is practically important (Welch's t-test, p = 0.01).
>
> **Good.** The 0.1 s difference is statistically significant (Welch's t-test, p = 0.01).

> **Context.** The draft reports overlapping intervals and states that the authors did not test the difference. The edit is a proposal for the author.
>
> **Bad.** The overlapping intervals establish that paint A is not faster.
>
> **Good.** The overlapping intervals do not establish whether paint A is faster.

> **Context.** The draft states that the outcome tests use the Holm correction for multiple comparisons. The edit is a proposal for the author.
>
> **Bad.** We test differences across six outcomes at a significance level of 0.05.
>
> **Good.** We test differences across six outcomes at a significance level of 0.05 with the Holm correction for multiple comparisons.

> **Context.** The draft reports p = 0.032 for this test.
>
> **Bad.** The difference is significant (Welch's t-test, p < 0.05).
>
> **Good.** The difference is significant (Welch's t-test, p = 0.032).

> **Context.** For the drying-time test, the draft reports only p < 0.001.
>
> **Bad.** Mean drying times differ significantly (Welch's t-test, p = 0.001).
>
> **Good.** Mean drying times differ significantly (Welch's t-test, p < 0.001).

> **Context.** The draft reports p = 0.18 at a significance level of 0.05 but does not assess statistical power. The edit is a proposal for the author.
>
> **Bad.** The non-significant result establishes inadequate power.
>
> **Good.** The result is not significant.
