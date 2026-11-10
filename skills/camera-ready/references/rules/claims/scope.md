# Match scope and confidence to the evidence

Scope ranges from every case ("X always holds") through a tendency across contexts ("X generally happens") and named settings ("X is best for settings V and W") to one observed case ("we find one case where X"). Choose the broadest scope and the most direct confidence the evidence supports, avoiding [underclaiming](underclaiming.md), but keep every claim within the conditions, datasets, and settings its evidence covers. An unqualified plural noun ("Solar cells degrade in humid air") may state a tendency; if the evidence covers only the tested cases, name them ("the four cell designs we test"). Check whether words such as "always" or "unique" extend a claim to untested cases.

A single example, such as a generated sample or saliency map, can establish that a case occurs. Flag a universal claim contradicted by an in-scope example; an exception need not refute a tendency. Flag a broader claim from one example or from sampled data unless the draft explains how it was selected (such as at random, as typical, or as the best case) and, for sampled data, justifies the target population. Keep an explicit label marking an example as hypothetical or constructed, but never add one by inference. Check [independent confirmation](variability.md) under its own rule.

Also check these kinds of claim:

- Unless the draft supports the interpretation, flag a research question or conclusion that treats a score as the broader property it measures indirectly, or a ratio of scores as a proportional change in that property, without rewriting the question or adding a caveat.
- A result without a comparison supports "X works", not "X is better" or "X is practical"; flag any stronger claim that lacks a relevant baseline.
- A claim such as "ready for clinical use" or "ready for production" also needs evidence on costs and operating conditions beyond test gains, and must address the adverse consequences and relevant alternatives that the draft identifies; flag missing support or unsupported assurances unless the draft explicitly marks the claim as tentative.
- A claimed trend over time needs observations over time, and a small sample needs both its count of cases and its total visible in the text.
- Flag words that assume an unstated fact, such as "the solution" (which may assume that a solution exists or is unique).

## Details

Even when the draft explains how an example was selected, calling a single example random, typical, or the best case does not by itself establish a broader claim, and increasing the sample size does not by itself make an unrepresentative sample representative. A valid constructed example can establish that something is mathematically possible, but do not present it as an empirical observation.

To claim that a proportion or rate changes over time, the draft needs observations over time with comparable denominators. To claim that a raw count changes over time, it needs counts over time but no denominators. A few recent cases establish neither trend. Do not treat the sample percentage as an estimate of a probability in the population without support.

A baseline is a method or result used for comparison. If the draft identifies a baseline as irrelevant or needlessly weak, outperforming it cannot establish that a method is generally superior. Check the draft's account of whether baselines reflect current methods, are competently implemented, and cover credible simple alternatives it identifies; flag gaps that undermine the claimed comparison. A baseline is not obsolete merely because it is old.

Read the research question, the measurement, and the conclusion together. A scale may rank systems without measuring how much they differ in the underlying property. Do not infer the type of scale or change reported values to repair an unsupported interpretation.

Keep "the" when it refers to an object already introduced or a chosen representative. Do not read "a solution" as implying that several solutions exist.

When the draft recommends practical use, check the requirements it documents, such as startup costs or guarantees about outputs. Do not impose a generic checklist for deployment. Keep conditional recommendations that the draft's evidence supports.

## Examples

**Edit 1.** Suppose the draft records that 99 of the 100 tested bulbs lit within a second and calls that timing typical.

> **Before.** The tested bulbs always lit within a second.

> **After.** The tested bulbs usually lit within a second.

**Edit 2.** If the draft documents a crack in one photographed tile but gives no survey of other tiles, propose the revision in After to the author.

> **Before.** Cracks are common in these tiles.

> **After.** The photographed tile has a crack.

**Edit 3.** Say the draft gives chair A a comfort score of 8 and chair B a score of 4, without establishing that the scores are proportional to comfort. Treat After as a proposal to the author.

> **Before.** Chair A is twice as comfortable as chair B.

> **After.** Chair A scores twice as high as chair B on the comfort scale.

**Edit 4.** Imagine the draft reports tests only on aluminum and explicitly describes possible use on bridges as untested.

> **Before.** The coating resists corrosion on all metals and may be useful on bridges.

> **After.** The coating resists corrosion on aluminum in the tests and may be useful on bridges.

The draft already marks the bridge application as untested, so the tentative suggestion can stay.
