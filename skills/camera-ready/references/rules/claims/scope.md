# Match scope and confidence to the evidence

Use the broadest scope and most direct confidence the evidence supports, from a guarantee to one observed case, without [underclaiming](underclaiming.md). Limit each claim, especially a headline claim, to the conditions, datasets, and settings its evidence covers. If support is uncertain, leave the claim and flag it. A bare generic plural such as "Solar cells degrade in humid air" can state a tendency, but it still makes a claim about the whole class; when the evidence covers only the tested cases, name them ("the four cell designs we test"). Check whether absolutes such as "always" or "unique" extend a claim to untested cases. One in-scope counterexample defeats a universal claim but need not defeat a tendency.

A micrograph, case report, generated sample, or other single example shows only that a case occurs, not how often. For a broader claim, the draft must explain how the example was selected, such as at random, as typical, or as the best case; flag missing information. Keep any explicit label marking an example as hypothetical or constructed, and never add such a label by inference. A broad claim drawn from sampled data needs a justified population and an account of how the sample was selected; check a claim of [independent confirmation](variability.md) under its own rule.

Flag a research question or conclusion that, without support, treats a score as the broader property it measures indirectly or treats a ratio of scores as a proportional change in that property. Do not rewrite the question or add a caveat to fix the mismatch. A claim of superiority needs a relevant baseline; flag missing comparisons. A claim such as "ready for clinical use" or "ready for production" needs evidence about costs and operating conditions beyond gains under test conditions; flag missing support, but keep applications that the draft explicitly marks as tentative.

For temporal trends, small-sample probabilities, baseline selection, score differences, and wording that assumes an unstated fact ("the solution", "restores accuracy"), see the page.

## Details

Increasing the sample size does not by itself make an unrepresentative sample representative, and labeling a single example random, typical, or best-case does not by itself establish a broader claim. A valid constructed example can establish mathematical possibility, but do not present it as an empirical observation.

Claiming a trend in prevalence or rate requires observations over time with comparable denominators, whereas a trend in raw counts needs counts over time but no denominators; a few recent cases establish neither. In small samples, keep the observed numerator and denominator visible, and do not treat a sample percentage as an estimate of a population probability without support.

Comparison against a baseline that the draft identifies as irrelevant or needlessly weak cannot establish general superiority, though age alone does not make a baseline obsolete.

Read the research question, the measurement, and the conclusion together. A scale that orders systems need not support claims about the size of differences in the underlying property. Do not infer a scale type or change reported values to repair an unsupported interpretation.

Check wording that presupposes an unstated fact: "the solution" may assume existence or uniqueness, and "restores accuracy" assumes higher prior accuracy. Keep a definite article when it refers to an introduced object or a chosen representative, and do not take an indefinite article ("a solution") to imply that several solutions exist.

When checking recommendations for practical adoption, check the requirements documented in the draft, such as startup costs or output guarantees, rather than imposing a generic deployment checklist. Keep conditional recommendations that the draft's evidence supports.

## Examples

The draft reports that the seal prevented leaks at the three pressures tested, with no evidence about other pressures.

> Bad: The seal prevents leaks at all pressures.
>
> Good: The seal prevents leaks at the three tested pressures.

The draft identifies the interaction as hypothetical.

> Bad: In the interaction, the user dismisses the permission prompt.
>
> Good: In the hypothetical interaction, the user dismisses the permission prompt.

The draft tests only four panel designs and reports cracking in all four.

> Bad: Solar panels crack in dry heat.
>
> Good: The four tested solar panel designs crack in dry heat.

The draft reports that 99 of 100 tested bulbs lit within a second and describes prompt lighting as typical.

> Bad: The tested bulbs always lit within a second.
>
> Good: The tested bulbs usually lit within a second.

The draft reports one photographed crack and no survey of other tiles.

> Bad: Cracks are common in these tiles.
>
> Good: A crack occurs in the photographed tile.

The draft states that the pictured crystal was selected as the largest in the batch; the revision is proposed to the author.

> Bad: The pictured crystal measures 8 mm.
>
> Good: The pictured crystal, selected as the largest in the batch, measures 8 mm.

The draft reports that surveyed volunteers at one library prefer evening hours and supports no citywide estimate.

> Bad: City residents prefer evening hours.
>
> Good: The surveyed library volunteers prefer evening hours.

The draft measures only a reduction in spelling errors and explicitly leaves overall writing quality untested; the revision of the conclusion is proposed to the author.

> Bad: The course improves writing quality.
>
> Good: The course reduces spelling errors.

The draft reports scores of 8 and 4 on a comfort scale and gives no proportional interpretation; the revision is proposed to the author.

> Bad: Chair A is twice as comfortable as chair B.
>
> Good: Chair A scores twice as high as chair B on the comfort scale.

The draft reports warmth ratings of 2, 3, and 4 for coats A, B, and C without establishing equal intervals of warmth; the revision is proposed to the author.

> Bad: The warmth gain from coat A to B equals that from coat B to C.
>
> Good: The warmth-rating gain from coat A to B equals that from coat B to C.

The draft compares absorption only with a 1990 pad design that it identifies as a relevant baseline.

> Bad: The pad absorbs more water than every alternative.
>
> Good: The pad absorbs more water than the 1990 pad design.

The draft establishes only that the sensor meets the accuracy target in laboratory tests and supplies no field evaluation; the revision is proposed to the author.

> Bad: The sensor is ready for field use.
>
> Good: The sensor meets the accuracy target in laboratory tests.

The draft tests the coating on aluminum only and explicitly proposes bridge use as an untested application.

> Bad: The coating resists corrosion on all metals and may be useful on bridges.
>
> Good: The coating resists corrosion on aluminum in the tests and may be useful on bridges.

The draft records more cracked tiles each month while inspecting more tiles and claims only an increase in the count; the revision is proposed to the author.

> Bad: The proportion of cracked tiles increased each month.
>
> Good: The number of cracked tiles increased each month.

The draft reports three failures this week and no earlier observations; the revision is proposed to the author.

> Bad: Pump failures are increasing.
>
> Good: Three pump failures occurred this week.

The draft reports one failure among five tested switches, with no population estimate.

> Bad: The probability of switch failure is 20%.
>
> Good: One of the five tested switches failed (20%).

The draft establishes one feasible solution but identifies no unique or previously introduced solution.

> Bad: We give the solution to the routing problem.
>
> Good: We give a solution to the routing problem.

The draft reports that calibration raises accuracy from 70% to 80%, with no earlier accuracy measurement.

> Bad: Calibration restores accuracy to 80%.
>
> Good: Calibration raises accuracy to 80%.

The draft constructs a mathematical example with two stable equilibria but reports no physical observation.

> Bad: We observe a system with two stable equilibria.
>
> Good: We construct an example of a system with two stable equilibria.

The draft supports classroom use below 30 °C and reports that the device fails above that temperature.

> Bad: We recommend the device for classroom use.
>
> Good: We recommend the device for classroom use below 30 °C.
