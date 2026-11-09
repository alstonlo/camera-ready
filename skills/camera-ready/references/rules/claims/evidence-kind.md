# Identify the kind of evidence supporting each claim

If a sentence reads like a theorem but gives no formal result or conditions, link it to the proved result and its assumptions, restate it as the observed or intuitive claim the draft supports, or flag it. If the draft applies a theorem to observations or experiments, flag the claim when the theorem's assumptions do not hold. An unmet assumption makes a theorem inapplicable, not false. Never drop a condition to simplify a formal statement. Instead, flag any condition that seems unnecessary (see Details). Distinguish proofs, calculations from a model, simulations, and measurements of the real system. Flag any claim that a model result holds in the real system without evidence. A valid claim limited to the model needs no experiment or field study.

## Details

A statement about all cases, inputs, runs, or allowed parameter values may claim a mathematical guarantee even without the word "theorem". Find the supporting result and its conditions before judging whether the result applies.

Propose a simpler mathematical condition only when the draft shows that the two conditions are equivalent and that the condition you would remove adds no useful information. Flag a suspected error in a proof separately from a claim that applies a valid theorem where its assumptions do not hold.

## Examples

**Edit 1.** A simulation is reported in the draft, but measurements of the actual bridge are absent.

> **Before.** Under the tested load, the bridge bends by 2 cm.
>
> **After.** Under the tested load, the simulated bridge bends by 2 cm.

**Edit 2.** In Theorem 2, the draft proves uniqueness when stiffness is positive.

> **Before.** The equilibrium is unique.
>
> **After.** When stiffness is positive, Theorem 2 guarantees that the equilibrium is unique.

**Edit 3.** Theorem 1 requires independent errors.

> **Before.** The correlated errors in these sensors make Theorem 1 false.
>
> **After.** Theorem 1 does not apply to these sensors because their errors are correlated.

**Edit 4.** As the draft shows, positivity already requires x to be nonzero, and stating both conditions adds no useful information.

> **Before.** For positive, nonzero x, the bound holds.
>
> **After.** For positive x, the bound holds.

**Edit 5.** The reported observations cover only five tested mixtures.

> **Before.** Every mixture settles within an hour.
>
> **After.** Each of the five tested mixtures settles within an hour.
