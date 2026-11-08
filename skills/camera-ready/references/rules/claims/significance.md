# Draw only the conclusions a statistical test supports

Reserve "significant(ly)" for results of a named statistical test. Pair the test with its p-value or significance level and, if the draft reports it, its effect size. If the word means large or important, replace it with the magnitude. If it claims statistical significance without naming a test, flag it. When the draft tests significance on several datasets or metrics, flag any missing explanation of how it corrects for multiple comparisons.

Failure to reject a hypothesis of no difference does not establish equality. Replace "the two methods perform the same (paired bootstrap, p = 0.21)" with "we find no significant difference between the two methods (paired bootstrap, p = 0.21)". When intervals overlap and the text names no test, flag any claim of superiority. Overlap alone establishes neither superiority nor its absence.

## Examples

- Bad: "Our method significantly outperforms the baseline (71.2 ± 0.4 vs 68.4 ± 0.6)."
- Good: "Our method outperforms the baseline by 2.8 points (71.2 ± 0.4 vs 68.4 ± 0.6; mean ± standard deviation over five seeds)."
