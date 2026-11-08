# Use logical words unambiguously

Replace ambiguous "any" with "every" or "at least one" according to the intended meaning; "some" requires only one case and leaves open whether every case qualifies. Use "each" with a singular noun instead of "all" with a plural when the plural could suggest that the objects share one value ("each run uses its own learning rate"). Rewrite a negative statement as a positive one only when the two statements hold in exactly the same cases, including values equal to a threshold. Keep a deliberate denial as a denial. Do not replace a negated property, including a monotonicity property, with its apparent opposite: "not connected" does not mean "every vertex is isolated". When "can" or "should" could mean capability, possibility, or obligation, use the meaning the draft establishes; otherwise flag it. For "can" and "should", also follow [hedges](../claims/hedges.md) and [performed actions](../conventions/actions.md). Replace an ambiguous slash in prose with the words it stands for, such as "or" or "and", keeping standard notation and abbreviations. Preserve whether a list is complete; "includes" alone does not imply omitted members. Keep "then" after an "if" clause whose conclusion is a formula or technical claim. When "contains" could mean membership or subset inclusion, say which. For nested conditions, negation scope, or a rhetorical "if" mistaken for a condition, use the page's diagnostics.

## Details

Determine what an ambiguous quantifier requires before replacing it. A statement about at least one case leaves open whether all cases qualify. A separate value for each object differs from one value shared by every object. Flag the ambiguity if the draft does not settle the intended claim.

Combine nested conditions only when both hypotheses govern the same conclusion. Preserve the distinction between necessary and sufficient conditions, and make clear where the conditions end and the conclusion begins. A plainly marked definition may use its own convention for equivalence; that convention does not strengthen an ordinary conditional.

For compounded negatives, list which cases the statement admits and excludes, including exact equality at a threshold. Preserve a deliberate denial or a weaker technical relation when a positive form would say more. Denying that all cases qualify ("not all") differs from denying that any case qualifies ("none"), and denying an outcome differs from denying a proposed cause. Place the negation on the intended target when the draft settles it.

For modals, distinguish an observed event, a capability, a prediction, a recommendation, and a requirement. An expectation is not an observation. The absence of a requirement is not a prohibition, and failure to observe an event does not prove that it cannot occur.

For a slash, determine whether its terms are alternatives, jointly required, or two labels for the same thing. State whether both alternatives can occur when that distinction matters. Keep conventional forms such as I/O and mathematical division.

Distinguish a full specification from a list of examples. Do not replace "consists of" with a weaker introduction when completeness matters, and do not infer that "includes" proves other members exist.

A sentence may use "if" to frame the author's wish to make a comparison rather than impose a mathematical condition. Separate that framing from what the theorem states and from any additional assumption needed for a conclusion.

## Examples

The draft states that two of the five jars leaked and the other three did not.

- Bad: All five jars did not leak.
- Good: Not all five jars leaked.
