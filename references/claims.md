# Claims

Every claim must match its evidence; overclaiming and underclaiming are both failures. An aspirational goal may motivate the text if the text marks it as not attained.

## The verb ladder

Pick the reporting verb from the evidence, never from enthusiasm.

| Verb | Evidence required |
|---|---|
| we **prove** | a theorem with stated assumptions, and nothing else |
| we **show / demonstrate / establish** | direct evidence that rules out the plausible alternatives |
| we **find / observe / report** | a directly measured empirical result |
| results **suggest / indicate**; we **hypothesize / conjecture** | an inference or interpretation that could reasonably be wrong |

A benchmark result never proves a mechanism, and a figure or table "shows" only what it displays; the claim read from it takes its own rung.

A claim hedged in the results must not reappear unhedged in the abstract, introduction, conclusion, or any other summary of the results. For each claim in the abstract, introduction, or another summary, find the result that supports it. Where the draft holds the support and the claim lacks a pointer, add one ("(Section 5)", "(Table 2)"). Where no support exists, flag the claim.

## Scope

Evidence sets both a claim's scope and its confidence (plain or hedged). From broadest to narrowest, scope ranges from a guarantee ("X always holds"), through a systematic claim ("X generally happens across contexts") and a narrow claim ("X is best for settings V and W"), to an existence claim ("we find one case where X"). Pick the broadest scope and the plainest confidence the evidence supports. When support is uncertain, leave the claim in place and flag it; that caution is no reason to hedge or drop a claim the evidence does support ([underclaiming](#failure-modes)).

Scope every headline claim to its conditions, datasets, and settings; absolutes ("always", "unique") claim the case you did not test. A bare generic plural claims the whole class, so "Transformers fail to retrieve early tokens" asserts it of every Transformer. When the evidence covers only the models tested, write "the four Transformers we test fail to retrieve early tokens".

A result reported without a comparison supports "X works", not "X is better" or "X is practical", so flag the missing baseline when the draft claims more. A qualitative example (a generated sample, a saliency map, a case study) supports only an existence claim. Offered as evidence for anything broader, it needs the text to say how it was chosen (at random, as typical, or as the best case), so flag it when the draft does not say.

## Causal language

Use "causes", "leads to", "improves because", and any other wording that credits a design choice only where the evidence supports causation, as an ablation that isolates the component does. Correlational results take "is associated with", "correlates with", or "coincides with". When the text introduces several changes together and isolates none, the text may credit the combination but no single change, and must not imply that every change is necessary.

## Formal and informal claims

Keep every claim visibly formal or visibly informal. A sentence that reads like a theorem ("all local minima have error close to that of the global minimum") but points to no result and states no conditions is neither; tie it to a stated result with its assumptions, rewrite it as the empirical or intuitive claim it is, or flag it when the draft supports neither. When the text invokes a theorem to support an empirical claim, check that the theorem's conclusion bears on that claim under the text's conditions; a convergence result for convex objectives does not support a claim about non-convex training, so flag the link.

## Uncertainty and significance

A comparison between two numbers is a claim, and its evidence includes how much the numbers vary. For every reported comparison, the reader must be able to find three things in the sentence, the caption, or a convention the text states once: how many runs each number covers and how it summarizes them (mean, median, or best run); whether the ± is a standard deviation, a standard error, or a confidence interval; and what varies (seed, data split, or the test examples a bootstrap resamples). Flag the gap when the draft omits one.

- Bad: "Our method significantly outperforms the baseline (71.2 ± 0.4 vs 68.4 ± 0.6)."
- Good: "Our method outperforms the baseline by 2.8 points (71.2 ± 0.4 vs 68.4 ± 0.6; mean ± standard deviation over five seeds)."

The two sides of a comparison must be computed the same way, so a best-run number is not comparable with a mean of final results, and a number copied from another publication is comparable only under the same evaluation protocol. Flag every comparison where the text does not show that its two sides were computed alike.

Reserve "significant(ly)" for the result of a statistical test that the text names, paired with the p-value or significance level and, where the draft reports it, the effect size. Where it means large or important, replace it with the magnitude; where it claims statistical significance but names no test, flag it. When the draft tests significance on several datasets or metrics, check that it says how it corrects for multiple comparisons, and flag it if it does not.

Failure to reject a hypothesis of no difference does not establish equality, so "the two methods perform the same (paired bootstrap, p = 0.21)" becomes "we find no significant difference between the two methods (paired bootstrap, p = 0.21)". When intervals overlap and the text names no test, flag the claimed superiority; overlap alone decides nothing in either direction. When the ranking of methods changes with the aggregate metric, scope each claim to the metric that produced it.

## Hedges

Place the hedge where data becomes interpretation, so that the measurement is unhedged and the mechanism is hedged, never the reverse.

- Bad: "Accuracy appears to drop by roughly 4.2 points when we remove the auxiliary loss, which shows the loss is a regularizer."
- Good: "Accuracy drops 4.2 points when we remove the auxiliary loss (Table 3), which suggests the loss acts as a regularizer."

Procedures are unhedged wherever the text describes them, in a Methods section or elsewhere; only the rationale for a choice may carry a hedge. Results, Discussion, and Conclusion sections, and any other passage that interprets a measurement, follow this boundary between measurement and interpretation. An abstract or other summary compresses each claim but keeps its rung on the [verb ladder](#the-verb-ladder) and its hedge.

Use at most one hedge per claim, in a standard academic form ("may", "likely", "suggests", "appears to"). Softeners ("somewhat", "relatively", "essentially", and similar; [Cut intensifiers](style.md#concision)) weaken a claim without saying where it fails, so where the draft holds the condition under which the claim fails, or the size of the effect, state that in place of the softener; otherwise keep it and flag it, since deleting a claim's only hedge upgrades it. A qualifier whose deletion changes what is claimed ("usually", "on average", "in most runs") is a scope condition, not a hedge, and stays ([Protect](cutting.md#protect)).

- Bad: "Our method is relatively robust to label noise."
- Good: "Our method loses 2 points of accuracy at 20% label noise, against 9 points for the baseline."

## Failure modes

**Overclaiming.** The following are banned for empirical results: *solves, proves, optimal, guarantees, first to* (unless the draft verifies the claim), unsupported superlatives, "human-level" or "state-of-the-art" without naming the task, benchmark, and metric, and "novel" as filler.

**Underclaiming.** State contributions plainly and completely, and do not weaken a real result with reflexive hedges. Each item in a "Contributions" list states a claim a reader could check and, where the draft has one, a pointer to its support. An item whose whole claim is *study, explore, investigate, describe*, or *discuss* claims nothing, so rewrite it from what the corresponding section reports, or flag it.

- Bad: "We study the theoretical properties of the estimator."
- Good: "We prove that the estimator is unbiased under assumption A1 (Section 4)."

## Speculation

Never state speculation in the grammatical form of established fact. Mark it with "We conjecture" or "One possible explanation is", or confine it to a Motivation or Discussion paragraph that the text marks, as a whole, as speculation.

An explanation built on an undefined term is speculation however it is phrased. "The gain comes from reduced internal covariate shift" cannot be checked until the text says how the shift is measured, so flag the term or mark the sentence as a hypothesis. A bare negative claim ("X does not imply Y") needs its status stated (a counterexample, a reference, or a statement that the question is open), so flag it when the draft gives none.

## Limitations

State each limitation once and precisely, without apology, and without a decoy limitation that hides the real weakness; flag a decoy, and cut a duplicate only under a length request ([Triage order](cutting.md#triage-order)). Frame each one by its impact on the findings ("results may not transfer to larger models, since every run uses the same 100M-parameter backbone"). A limitation phrased as future work must still say what the current results do not cover.
