# Report variability and compare like with like

For each numerical comparison, check that the text states the number of runs, how they are aggregated, what ± means, and the source of variation, either beside the comparison or in a reporting convention; flag missing information. A best run is not comparable with a mean. Flag a comparison, including one with results borrowed from other papers, unless the text establishes that both sides use equivalent tasks, outputs, accuracy requirements, aggregation, and protocols. When the draft reports a speed gain with lower accuracy, state the trade-off. If it does not establish comparable accuracy, flag the missing comparison.

A percentage needs its base, and a reported change must say whether it is a relative percentage change or a difference in percentage points. Edit the wording when the draft settles which; otherwise flag it, and never relabel by guessing. Keep each ranking tied to its metric, and flag selective reporting.

Data used to select or tune a method do not independently test that choice. Flag a claim of independent confirmation that rests on reused data, related datasets, or correlated metrics, unless the draft establishes a separate test. For misleading averages, systematic timing errors, and how convergence error is measured and normalized, see the page.

## Details

A reporting convention may define aggregation and variation once for the paper. Distinguish means, medians, and best runs; standard deviations, standard errors, and confidence intervals; and variation across seeds, splits, or resampled test cases.

Check that compared methods meet equivalent output guarantees and accuracy requirements. Lower latency at a lower recall target or a looser numerical tolerance is a trade-off. Results taken from another paper need compatible evaluation protocols.

A percentage describes a quantity relative to a whole or reference value. A difference between percentage-valued measurements can be expressed in percentage points; a relative percentage change uses a baseline as its denominator. If the intended quantity is unclear, flag it without changing the number's meaning.

Compare an aggregate with the claim about typical behavior. Skew, missing outcomes, mixed task sizes, or benchmark weights can change that interpretation. A mean may answer a valid question; do not automatically replace it with another statistic.

For timing comparisons, inspect the stated compiler options, cache state, hardware, run order, and clock resolution. Small run-to-run variation does not eliminate systematic bias. Flag a visible confound without inventing a causal explanation.

Keep each ranking attached to the metric that produces it. Flag an unexplained change of metric across datasets or a favorable summary that omits a conflicting metric reported in the draft. Preserve measures that expose a real trade-off.

Trace the stated roles of data in discovery, tuning, and testing. A result that suggests a hypothesis is not an independent test of that hypothesis. A held-out split from one source can provide a legitimate separate test; shared origin alone does not establish reuse. Reused cases, jointly tuned subsets, and correlated metrics do not automatically provide independent confirmations. If the sampling or data roles are unclear, flag the unclear basis for claiming independence. Preserve exploratory findings and conclusions that do not depend on independence; do not require preregistration.

For a convergence claim, check whether the reported quantity measures error rather than merely listing successive values. When errors or residuals depend on the scale of the problem, look for a defined normalization that makes the comparison meaningful. Flag an unclear measure or missing normalization; do not choose a norm, compute replacement values, or rewrite a table.

## Examples

The draft compares two modes on the same photographs and reports that mode A produces smaller files but loses more image detail.

- Bad: Mode A produces smaller files than mode B.
- Good: Mode A produces smaller files than mode B but loses more image detail.

The draft explicitly defines the reported increase as a difference of four percentage points.

- Bad: The attendance rate increases by 4%.
- Good: The attendance rate increases by 4 percentage points.
