# Use logical words unambiguously

Replace ambiguous "any" with "every" or "at least one" according to the intended meaning; "some" requires only one case and leaves open whether every case qualifies. Use "each" with a singular noun instead of "all" with a plural when the plural could suggest that the objects share one value ("each sample is held at its own temperature"). Rewrite a negative statement as a positive one only when the two statements hold in exactly the same cases, including values equal to a threshold. Keep a deliberate denial as a denial, and do not replace a negated property, including a monotonicity property, with its apparent opposite ("not connected" does not mean "every vertex is isolated"). When "can" or "should" could mean capability, possibility, or obligation, use the meaning the draft establishes, or flag the ambiguity if the draft establishes none; for these words, also follow [hedges](../claims/hedges.md) and [performed actions](../conventions/performed-actions.md). Replace an ambiguous slash in prose with the words it stands for, such as "or" or "and", while keeping standard notation and abbreviations. Preserve whether a list is complete; "includes" alone does not imply omitted members. Keep "then" after an "if" clause whose conclusion is a formula or technical claim, and when "contains" could mean membership or subset inclusion, state which. Use the diagnostics in Details for nested conditions, negation scope, or a rhetorical "if" mistaken for a condition.

## Details

If the draft does not settle what an ambiguous quantifier means, flag the ambiguity. When unpacking compounded negatives, list the cases admitted and excluded, including equality at thresholds. Distinguish "not all" from "none", and distinguish denying an outcome from denying its proposed cause.

In conditional statements, preserve the distinction between necessary and sufficient conditions and mark where the conclusion begins. Combine nested conditions only when both govern the same conclusion. When a rhetorical "if" frames a comparison rather than imposing a condition, rewrite it so that the framing is separated from the theorem’s claim and from any additional assumption. For definitional equivalence, follow [definitions](definitions-procedures.md).

When editing modal verbs, distinguish an observation, a capability, a prediction, a recommendation, and a requirement. Saying that a step is not required does not prohibit it, and failing to observe an outcome does not make it impossible.

When replacing a slash, check whether it expresses alternatives, joint requirements, or synonymous labels, and clarify whether both alternatives may occur when relevant. Keep conventional forms such as w/v, S/N, and I/O.

## Examples

The draft states that two of the five jars leaked and the other three did not.

> Bad: All five jars did not leak.
>
> Good: Not all five jars leaked.

The draft requires every jar to pass.

> Bad: The batch passes if any jar passes.
>
> Good: The batch passes if every jar passes.

The draft requires one or more working lamps.

> Bad: The display works if any lamp works.
>
> Good: The display works if at least one lamp works.

The draft reports that all ten samples passed.

> Bad: Some of the ten samples passed.
>
> Good: All ten samples passed.

The draft assigns a separate temperature to every sample.

> Bad: All samples are held at a set temperature.
>
> Good: Each sample is held at its own set temperature.

> Bad: The score is not less than 60.
>
> Good: The score is at least 60.

The draft explicitly denies that heating caused the crack and requires every seal to pass.

> Bad: Heating did not cause the crack. The batch passes if any seal passes.
>
> Good: Heating did not cause the crack. The batch passes if every seal passes.

The draft states that a rate is not increasing monotonically and requires at least one valid reading.

> Bad: The rate is not increasing monotonically. Retain the run if any reading is valid.
>
> Good: The rate is not increasing monotonically. Retain the run if at least one reading is valid.

The draft describes what the pump is capable of, not what the operator is permitted to do.

> Bad: The pump can move hot water.
>
> Good: The pump is capable of moving hot water.

The draft recommends replacing the seal.

> Bad: The seal should be replaced.
>
> Good: We recommend replacing the seal.

The draft says gloves are optional.

> Bad: You should not wear gloves.
>
> Good: You need not wear gloves.

The draft permits either or both cleaning agents.

> Bad: Use soap/alcohol.
>
> Good: Use soap, alcohol, or both.

The draft requires both measurements.

> Bad: Record mass/volume.
>
> Good: Record mass and volume.

The draft requires both mass and volume; S/N is its established signal-to-noise notation.

> Bad: Record S/N, then mass/volume.
>
> Good: Record S/N, then mass and volume.

The original draft specifies steel and glass as the kit’s complete material list; Bad weakens that specification.

> Bad: The kit includes steel and glass.
>
> Good: The kit consists of steel and glass.

The draft states that the kit includes steel and glass but does not say whether it includes anything else.

> Bad: The kit includes steel and glass, so it must contain another material.
>
> Good: The kit includes steel and glass.

> Bad: If the force is zero, acceleration is zero.
>
> Good: If the force is zero, then acceleration is zero.

The draft states that every element of B belongs to A, not that B is itself an element of A.

> Bad: The set A contains B.
>
> Good: The set A contains every element of B.

> Bad: If the lid is closed, then if the seal is intact, the jar holds water.
>
> Good: If the lid is closed and the seal is intact, then the jar holds water.

The draft says the lid closed, but the spring did not cause it to close.

> Bad: The lid did not close because of the spring.
>
> Good: The lid closed, but not because of the spring.

The draft proves the bound unconditionally and uses it to compare the two designs.

> Bad: If we compare the two designs, the theorem gives a 5 W bound.
>
> Good: The theorem gives a 5 W bound, which we use to compare the two designs.
