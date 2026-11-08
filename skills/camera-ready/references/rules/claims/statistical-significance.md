# Draw only the conclusions a statistical test supports

Use *significant* only for the result of a named statistical test, reported with its p-value or significance level and any effect size the draft supplies; flag missing information. When *significant* means large or important, replace it with the reported magnitude. Keep available effect estimates and uncertainty even when the test is not significant. A p-value gives the probability, under the null hypothesis and test assumptions, of observing results at least as extreme as those measured, not the probability that a hypothesis is true. Preserve the tested hypothesis and the test's direction. Failing to reject the null hypothesis does not establish equality, and statistical significance does not establish practical importance. Whether two intervals overlap settles neither superiority nor its absence; flag any claim of superiority inferred from interval overlap alone, without a test. When the draft tests significance across several datasets, outcomes, or metrics, flag a missing explanation of how it corrects for multiple comparisons. For reporting only a significance threshold, and for statistical power, see the page.

## Details

When the draft supplies a numeric p-value, preserve that number rather than reducing it to a threshold label such as p < 0.05. When the draft gives only a bound or significance level, keep that statement without rounding or recomputing it.

Because statistical power depends on sample size, variability, and the effect of interest, a non-significant result alone does not establish inadequate power. Never select a replacement statistical test or invent a multiple-comparison adjustment that the draft does not state.

## Examples

> **Context.** The draft specifies a significance level of 0.05 and tests for a difference in mean drying times, not for equivalence; the revision is proposed to the author.
>
> **Bad.** Mean drying times are equal for paints A and B (Welch's t-test, p = 0.18).
>
> **Good.** Mean drying times do not differ significantly between paints A and B (Welch's t-test, p = 0.18).

> **Context.** The draft reports a 2 min reduction in drying time and uses "significant" to mean large, without a statistical test.
>
> **Bad.** Paint A reduces drying time significantly.
>
> **Good.** Paint A reduces drying time by 2 min.

> **Context.** The draft reports a two-sided Welch's t-test with p = 0.02 for the mean difference; the revision is proposed to the author.
>
> **Bad.** Mean drying times differ significantly.
>
> **Good.** Mean drying times differ significantly (two-sided Welch's t-test, p = 0.02).

> **Context.** The draft reports a 2 min estimated difference with a 95% confidence interval from −1 to 5 min; the revision is proposed to the author.
>
> **Bad.** The difference is not significant (Welch's t-test, p = 0.18).
>
> **Good.** The estimated difference is 2 min (95% confidence interval: −1 to 5 min) and is not significant (Welch's t-test, p = 0.18).

> **Context.** The draft defines the null as equal mean masses and reports p = 0.03; the revision is proposed to the author.
>
> **Bad.** The probability that the equal-means null is true is 0.03.
>
> **Good.** Under the equal-means null and the test assumptions, the probability of results at least as extreme as observed is 0.03.

> **Context.** The draft reports a one-sided test for lower, not higher, mean wear; the revision is proposed to the author.
>
> **Bad.** The test assesses whether mean wear differs.
>
> **Good.** The test assesses whether mean wear is lower.

> **Context.** The draft reports a 0.1 s difference and establishes statistical significance but no practical importance; the revision is proposed to the author.
>
> **Bad.** The 0.1 s difference is practically important (Welch's t-test, p = 0.01).
>
> **Good.** The 0.1 s difference is statistically significant (Welch's t-test, p = 0.01).

> **Context.** The draft reports overlapping intervals and explicitly states that no test of the difference was performed; the revision is proposed to the author.
>
> **Bad.** The overlapping intervals establish that paint A is not faster.
>
> **Good.** The overlapping intervals do not establish whether paint A is faster.

> **Context.** The draft reports that its outcome tests use the Holm correction; the revision is proposed to the author.
>
> **Bad.** We test differences across six outcomes at a significance level of 0.05.
>
> **Good.** We test differences across six outcomes at a significance level of 0.05 using the Holm correction.

> **Context.** The draft reports p = 0.032 for this test.
>
> **Bad.** The difference is significant (Welch's t-test, p < 0.05).
>
> **Good.** The difference is significant (Welch's t-test, p = 0.032).

> **Context.** The draft reports only the bound p < 0.001 for the drying-time test.
>
> **Bad.** Mean drying times differ significantly (Welch's t-test, p = 0.001).
>
> **Good.** Mean drying times differ significantly (Welch's t-test, p < 0.001).

> **Context.** The draft reports p = 0.18 at a significance level of 0.05 but supplies no power analysis; the revision is proposed to the author.
>
> **Bad.** The non-significant result establishes inadequate power.
>
> **Good.** The result is not significant.
