# Use logical words unambiguously

- Replace ambiguous "any" with "every" or "at least one", whichever the draft means ("the bound holds for every learning rate below 1/L").
- If "all" with a plural noun could suggest that objects share one value, use "each" with a singular noun ("each sample is held at its own temperature").
- Distinguish "not all" from "none". When it affects the claim, clarify whether "some" allows all cases or means fewer than all.
- Rewrite a negative statement as a positive one only when both hold in exactly the same cases ("not nonincreasing" does not mean "increasing"), including values equal to a threshold. Keep a deliberate denial as a denial. With "not" and "because", clarify whether the denial concerns the outcome or its proposed cause.
- When "can" or "should" could mean observation, capability, possibility, prediction, recommendation, or obligation, use the meaning the draft establishes, or flag the ambiguity; also follow [hedges](../claims/hedges.md) and [performed actions](../conventions/performed-actions.md). Keep impossibility, prohibition, and lack of obligation distinct when negating modals.
- Keep "then" after an "if" clause whose conclusion is a formula or technical claim. Combine nested conditions ("if A, then if B, then C") into one ("if A and B, then C") only when both govern the same conclusion, and keep necessary and sufficient conditions distinct. When "if" introduces a comparison rather than a condition, state the comparison separately from the claim.
- Replace an ambiguous slash in prose with the words it stands for, such as "or" or "and", keeping standard abbreviations and notation.
- Preserve whether a list is complete; "includes" alone does not imply omitted members.
- When "contains" could mean membership or subset inclusion, state which.

## Details

If the draft does not establish what an ambiguous quantity word such as "any" or "all" means, flag the ambiguity. To rewrite a statement with several negatives, first list the cases that it allows and the cases that it excludes, including a value exactly equal to a threshold.

In a conditional statement, preserve the distinction between a necessary condition (one that must hold for the conclusion to be true) and a sufficient condition (one that guarantees the conclusion). Make clear where the conclusion begins. When you separate a comparison introduced by "if", also keep it separate from any additional assumption. A conclusion that holds only under an added assumption is something the result implies under that assumption, not something it states: write "Lemma 2 implies that the solution is unique when the load is bounded", not "If the load is bounded, Lemma 2 states that the solution is unique". For a definition that states that two descriptions are equivalent, follow the [rule on definitions](definitions-procedures.md).

Failing to observe an outcome does not make it impossible.

When you replace a slash, check whether it separates alternatives, joint requirements, or names for the same thing. State whether both alternatives may occur together when that matters. Keep conventional forms such as w/v, S/N, and I/O.

## Examples

**Edit 1.**

> **Before.** The score is not less than 60.

> **After.** The score is at least 60.

**Edit 2.** Suppose one valid reading is enough to retain a run under the draft's requirements.

> **Before.** The rate is not increasing monotonically. Retain the run if any reading is valid.

> **After.** The rate is not increasing monotonically. Retain the run if at least one reading is valid.

The first sentence allows a rate that rises and falls; calling it decreasing would exclude that possibility.

**Edit 3.** Imagine the draft says gloves are optional.

> **Before.** You should not wear gloves.

> **After.** You need not wear gloves.

**Edit 4.** Say the draft requires both measurements.

> **Before.** Record S/N, then mass/volume.

> **After.** Record S/N, then mass and volume.

The slash in S/N belongs to the standard abbreviation for signal-to-noise ratio.

**Edit 5.** Suppose the draft does not say whether other materials are present.

> **Before.** The kit includes steel and glass, so it must contain another material.

> **After.** The kit includes steel and glass.

**Edit 6.** Imagine the draft proves the bound without conditions.

> **Before.** If we compare the two designs, the theorem gives a 5 W bound.

> **After.** The theorem gives a 5 W bound, which we use to compare the two designs.
