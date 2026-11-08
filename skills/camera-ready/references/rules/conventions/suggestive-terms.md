# Clarify suggestive, overloaded, and suitcase terms

Clarify suggestive coinages ("thought vector"), overloaded terms ("deconvolution" for transposed convolution), and suitcase words with several field meanings ("generalization"): state which meaning applies. Flag an undefined coinage and suggest a literal alternative. Keep established technical usage and explain its operation at first use; preserve "The network learns features". Replace "the model tries to reason" with the stated operation or author goal ("we train the model to"). Replace an ordinary word that collides with a nearby technical meaning, such as "a heap of requests" in a paper about binary heaps, keeping the technical term. Follow [definitions and procedures](../prose/definitions-procedures.md) for unfamiliar categories and competing definitions.

## Details

A familiar everyday word can suggest more than the stated computation performs. Explain the literal operation rather than assigning intentions or mental states to a model. An accepted field term can remain useful even when its everyday meaning is figurative; clarify its technical meaning instead of banning it.

Distinguish a term that changes a precise technical meaning from a broad word that names several different properties. For example, a claim about "generalization" must identify which transfer or evaluation setting it means. Do not replace a narrow measured property with the broader everyday reading.

When an ordinary expression conflicts with a nearby technical use of a direction, time, or shape word, replace the ordinary expression. Preserve the defined technical name.

## Examples

The draft states that the authors train the robot to sort bottles by color.

- Bad: The robot wants to sort bottles by color.
- Good: We train the robot to sort bottles by color.
