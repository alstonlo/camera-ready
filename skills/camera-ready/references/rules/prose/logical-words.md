# Use logical words unambiguously

Replace ambiguous "any" with "every" or "at least one", whichever the draft means; "some" requires only one case and leaves open whether every case qualifies. If "all" with a plural noun could suggest that objects share one value, use "each" with a singular noun instead ("each sample is held at its own temperature"). Rewrite a negative statement as a positive one only when both statements hold in exactly the same cases, including values equal to a threshold. Keep a deliberate denial as a denial. Do not replace a negated property, including monotonicity, with its apparent opposite ("not connected" does not mean "every vertex is isolated"). When "can" or "should" could mean capability, possibility, or obligation, use the meaning the draft establishes, or flag the ambiguity; also follow [hedges](../claims/hedges.md) and [performed actions](../conventions/performed-actions.md). Replace an ambiguous slash in prose with the words it stands for, such as "or" or "and", while keeping standard abbreviations and notation. Preserve whether a list is complete; "includes" alone does not imply omitted members. Keep "then" after an "if" clause whose conclusion is a formula or technical claim. When "contains" could mean membership or subset inclusion, state which. Use the checks in Details for nested conditions, negation scope, or an "if" that frames a comparison.

## Details

If the draft does not establish what an ambiguous quantity word such as "any" or "all" means, flag the ambiguity. To rewrite a statement with several negatives, first list the cases that it allows and the cases that it excludes, including a value exactly equal to a threshold. Distinguish "not all" from "none". Also distinguish a denial that an outcome occurred from a denial that a proposed cause produced it.

In a conditional statement, preserve the distinction between a necessary condition (one that must hold for the conclusion to be true) and a sufficient condition (one that guarantees the conclusion). Make clear where the conclusion begins. Combine nested conditions into one condition only when both govern the same conclusion. When "if" introduces a comparison rather than a condition, rewrite the sentence so that the comparison is stated separately from the theorem's claim and from any additional assumption. For a definition that states that two descriptions are equivalent, follow the [rule on definitions](definitions-procedures.md).

When you edit "can", "should", and similar verbs, distinguish an observation, a capability, a prediction, a recommendation, and a requirement. Saying that a step is not required does not prohibit it. Failing to observe an outcome does not make it impossible.

When you replace a slash, check whether it separates alternatives, joint requirements, or names for the same thing. State whether both alternatives may occur together when that matters. Keep conventional forms such as w/v, S/N, and I/O.

## Examples

**Example 1.** The draft states that two of the five jars leaked and the other three did not.

> **Bad.** All five jars did not leak.
>
> **Good.** Not all five jars leaked.

**Example 2.** The draft requires every jar to pass.

> **Bad.** The batch passes if any jar passes.
>
> **Good.** The batch passes if every jar passes.

**Example 3.** The draft requires one or more working lamps.

> **Bad.** The display works if any lamp works.
>
> **Good.** The display works if at least one lamp works.

**Example 4.** The draft reports that all ten samples passed.

> **Bad.** Some of the ten samples passed.
>
> **Good.** All ten samples passed.

**Example 5.** The draft assigns a separate temperature to every sample.

> **Bad.** All samples are held at a set temperature.
>
> **Good.** Each sample is held at its own set temperature.

**Example 6.**

> **Bad.** The score is not less than 60.
>
> **Good.** The score is at least 60.

**Example 7.** The draft explicitly denies that heating caused the crack and requires every seal to pass.

> **Bad.** Heating did not cause the crack. The batch passes if any seal passes.
>
> **Good.** Heating did not cause the crack. The batch passes if every seal passes.

**Example 8.** The draft states that a rate is not increasing monotonically and requires at least one valid reading.

> **Bad.** The rate is not increasing monotonically. Retain the run if any reading is valid.
>
> **Good.** The rate is not increasing monotonically. Retain the run if at least one reading is valid.

**Example 9.** The draft describes the pump's capability, not the operator's permission to use it.

> **Bad.** The pump can move hot water.
>
> **Good.** The pump is capable of moving hot water.

**Example 10.** The draft recommends replacing the seal.

> **Bad.** The seal should be replaced.
>
> **Good.** We recommend replacing the seal.

**Example 11.** The draft says gloves are optional.

> **Bad.** You should not wear gloves.
>
> **Good.** You need not wear gloves.

**Example 12.** The draft permits either or both cleaning agents.

> **Bad.** Use soap/alcohol.
>
> **Good.** Use soap, alcohol, or both.

**Example 13.** The draft requires both measurements.

> **Bad.** Record mass/volume.
>
> **Good.** Record mass and volume.

**Example 14.** The draft requires both mass and volume and uses S/N for signal-to-noise ratio.

> **Bad.** Record S/N, then mass/volume.
>
> **Good.** Record S/N, then mass and volume.

**Example 15.** The original draft states that steel and glass are the kit's only materials. The Bad line is an earlier edit that no longer says that the list is complete.

> **Bad.** The kit includes steel and glass.
>
> **Good.** The kit consists of steel and glass.

**Example 16.** The draft states that the kit includes steel and glass but does not say whether it includes anything else.

> **Bad.** The kit includes steel and glass, so it must contain another material.
>
> **Good.** The kit includes steel and glass.

**Example 17.**

> **Bad.** If the force is zero, acceleration is zero.
>
> **Good.** If the force is zero, then acceleration is zero.

**Example 18.** The draft states that every element of B belongs to A, not that B is itself an element of A.

> **Bad.** The set A contains B.
>
> **Good.** The set A contains every element of B.

**Example 19.**

> **Bad.** If the lid is closed, then if the seal is intact, the jar holds water.
>
> **Good.** If the lid is closed and the seal is intact, then the jar holds water.

**Example 20.** The draft says the lid closed, but the spring did not cause it to close.

> **Bad.** The lid did not close because of the spring.
>
> **Good.** The lid closed, but not because of the spring.

**Example 21.** The draft proves the bound without conditions and uses it to compare two designs.

> **Bad.** If we compare the two designs, the theorem gives a 5 W bound.
>
> **Good.** The theorem gives a 5 W bound, which we use to compare the two designs.
