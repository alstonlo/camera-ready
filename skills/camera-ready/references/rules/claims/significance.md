# Draw only the conclusions a statistical test supports

Use *significant* only for the result of a named statistical test, reported with its p-value or significance level and, if the draft reports it, its effect size; flag missing information. If it means large or important, replace it with the reported magnitude. Keep available effect estimates and uncertainty even when the test is not significant. A p-value is the probability, under the null hypothesis and test assumptions, of results at least as extreme as observed, not the probability a hypothesis is true. Preserve the tested hypothesis and the test's direction. Non-rejection does not establish equality; significance does not establish practical importance. Whether two intervals overlap settles neither superiority nor its absence; flag superiority inferred from interval overlap alone, without a test. When the draft tests significance on several datasets or metrics, flag a missing explanation of how it corrects for multiple comparisons. For reporting only a significance threshold, and for statistical power, see the page.

## Details

A failure to reject a no-difference hypothesis does not show that two methods are equal. Overlap between separate intervals does not settle a test of their difference.

When the draft supplies a numeric p-value, preserve it rather than reducing it to a threshold label. Keep a reported bound or significance-level statement when no numeric p-value is supplied; do not round or recompute it.

Detection depends on sample size, variability, and the effect of interest. A non-significant estimate may remain compatible with meaningful effects. Non-significance alone does not establish inadequate power.

Keep the effect estimate and its uncertainty available on either side of a significance threshold. Statistical evidence, estimated magnitude, and practical importance answer different questions. A p-value is not the probability of a proposed causal explanation or the probability that the conclusion is wrong.

Preserve the stated null, alternative, and test direction. Flag inconsistencies or missing treatment of multiple comparisons without selecting a replacement test or inventing an adjustment.

## Examples

The draft specifies a significance level of 0.05 and tests for a difference in mean drying times, not for equivalence; the revision is proposed to the author.

- Bad: Mean drying times are equal for paints A and B (Welch's t-test, p = 0.18).
- Good: Mean drying times do not differ significantly between paints A and B (Welch's t-test, p = 0.18).
