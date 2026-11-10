# Identify the kind of evidence supporting each claim

Link a sentence that reads like a theorem but gives no formal result or conditions to the proved result and its assumptions, restate it as the observed or intuitive claim the draft supports, or flag it. Flag a claim that applies a theorem to observations or experiments that violate its assumptions; the theorem is then inapplicable, not false. Never drop a condition to simplify a formal statement; flag one that seems unnecessary. Flag an unsupported claim that a result from a model or simulation holds in the real system. A valid claim limited to the model needs no experiment or field study.

## Details

- Mathematical guarantees: A statement about all cases, inputs, runs, or allowed parameter values may claim a guarantee without using the word "theorem". Find the supporting result and its conditions before judging whether it applies.
- Simpler conditions: Propose a simpler mathematical condition only when the draft shows that it still guarantees the conclusion and that the condition it replaces adds no useful information.
- Proof errors: Flag a suspected error in a proof separately from a claim that applies a valid theorem where its assumptions do not hold.

## Examples

**Edit 1.** Suppose the draft reports a simulation but gives no measurements of the actual bridge.

> **Before.** Under the tested load, the bridge bends by 2 cm.

> **After.** Under the tested load, the simulated bridge bends by 2 cm.

**Edit 2.** Say the draft proves uniqueness in Theorem 2 when stiffness is positive.

> **Before.** The equilibrium is unique.

> **After.** When stiffness is positive, Theorem 2 guarantees that the equilibrium is unique.

**Edit 3.** Suppose Theorem 1 requires independent errors.

> **Before.** The correlated errors in these sensors make Theorem 1 false.

> **After.** Theorem 1 does not apply to these sensors because their errors are correlated.

**Edit 4.** Say the draft shows that positivity already requires x to be nonzero and that stating both conditions adds no useful information. The editor flags the redundant condition and proposes After to the author.

> **Before.** For positive, nonzero x, the bound holds.

> **After.** For positive x, the bound holds.

**Edit 5.** Imagine the reported observations cover only five tested mixtures.

> **Before.** Every mixture settles within an hour.

> **After.** Each of the five tested mixtures settles within an hour.
