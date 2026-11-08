# Match scope and confidence to the evidence

Use the broadest scope and most direct confidence the evidence supports, from a guarantee to one observed case, without [underclaiming](underclaiming.md). Limit each claim, especially a headline claim, to the conditions, datasets, and settings its evidence covers. If support is uncertain, leave the claim and flag it. A bare generic plural such as "Transformers fail to retrieve early tokens" can state a tendency, but it still makes a claim about the whole class; when the evidence covers only the tested models, name them ("the four Transformers we test"). Check whether absolutes such as "always" or "unique" extend a claim to untested cases. One in-scope counterexample defeats a universal claim, but need not defeat a tendency.

A generated sample, saliency map, or case study shows that a case occurs, not how often. For a broader claim, the draft must explain how the example was selected, such as at random, as typical, or as the best; flag missing information. Keep the draft's explicit label of an example as hypothetical or constructed; never add such a label by inference. A broad claim from sampled data needs a justified population and an account of how the sample was selected; check a claim of [independent confirmation](uncertainty.md) under its own rule.

Flag a research question or conclusion that, without support, treats a score as the broader property it measures indirectly, or treats a ratio of scores as a proportional change in that property. Do not rewrite the question or add a caveat to fix the mismatch. A claim of superiority needs a relevant baseline; flag missing comparisons. A claim such as "ready for production" needs evidence about costs and operating conditions beyond benchmark gains; flag missing support, but keep applications that the draft explicitly marks as tentative.

For temporal trends, small-sample probabilities, baseline selection, score differences, and wording that assumes an unstated fact ("the solution", "restores accuracy"), see the page.

## Details

A guarantee covers every case within its conditions. A systematic claim describes a supported pattern across cases. A narrower comparison names the tested settings. An existence claim establishes that a case occurs. Choose the widest justified level; narrowing a supported claim merely to avoid criticism is underclaiming.

For a claim about a population, check the intended population, the selection procedure, and the relevant variation in the sample. More observations do not automatically make a sample representative. A random, typical, or best-case label explains how an example was selected; the label alone does not establish a broader claim.

One observed example establishes that its outcome occurs under those conditions. It does not establish how often the outcome occurs. A counterexample can disprove a universal statement when it satisfies that statement's conditions. A constructed example can establish mathematical possibility when its construction meets the required conditions, but cannot become an observed empirical case through relabeling. Keep the draft's explicit hypothetical or constructed label wherever omitting it would make an illustration look like an observation.

A trend in prevalence needs comparable denominators and observations over time. A claim explicitly about an absolute count can use counts. A few recent cases do not establish either trend. For small samples, keep the observed numerator and denominator visible, and distinguish the fraction of tested cases from a general probability. A percentage may describe the observed sample without estimating a population probability.

A baseline must support the breadth of the superiority claim. A comparator that the draft identifies as irrelevant or needlessly weak cannot establish general leadership. Judge alternatives and implementation choices from the draft; age alone does not make a baseline obsolete.

Read the research question, measurement, and conclusion together. A task-completion score may measure one aspect of usability without establishing usability as a whole. A scale that orders systems need not support claims about the size or ratio of differences in the underlying property. Flag an unsupported interpretation without choosing a different research question, inferring a scale type, or changing values.

Wording can assume a fact without asserting it directly. Check whether "the solution" presupposes an established solution or uniqueness, and whether "restores accuracy" presupposes a higher prior accuracy. A definite article can also identify an object already introduced or a representative already selected; keep that use. An indefinite article does not establish that several solutions exist.

An adoption recommendation needs an argument about the proposed operating conditions. Check requirements that bear on the recommendation and appear in the draft, such as startup costs or output guarantees; do not add a generic deployment checklist. Keep a supported conditional recommendation or an explicitly tentative application at its stated strength.

## Examples

The draft reports that the seal prevented leaks at the three pressures tested, with no evidence about other pressures.

- Bad: The seal prevents leaks at all pressures.
- Good: The seal prevents leaks at the three tested pressures.

The draft identifies the interaction as hypothetical.

- Bad: In the interaction, the user dismisses the permission prompt.
- Good: In the hypothetical interaction, the user dismisses the permission prompt.
