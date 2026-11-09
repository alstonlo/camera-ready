# Identify the kind of evidence supporting each claim

If a sentence reads like a theorem but gives no formal result or conditions, link it to the proved result and its assumptions, restate it as the observed or intuitive claim the draft supports, or flag it. If the draft applies a theorem to observations or experiments, flag the claim when the theorem's assumptions do not hold. An unmet assumption makes a theorem inapplicable, not false. Never drop a condition to simplify a formal statement. Instead, flag any condition that seems unnecessary (see Details). Distinguish proofs, calculations from a model, simulations, and measurements of the real system. Flag any claim that a model result holds in the real system without evidence. A valid claim limited to the model needs no experiment or field study.

## Details

A statement about all cases, inputs, runs, or allowed parameter values may claim a mathematical guarantee even without the word "theorem". Find the supporting result and its conditions before judging whether the result applies.

Propose a simpler mathematical condition only when the draft shows that the two conditions are equivalent and that the condition you would remove adds no useful information. Flag a suspected error in a proof separately from a claim that applies a valid theorem where its assumptions do not hold.

## Examples

**Edit 1.** The draft reports only a simulation, with no measurements of the actual bridge. The edit adds "simulated" before "bridge", so that the reported bending describes the model rather than the actual bridge.

> **Before.** Under the tested load, the bridge bends by 2 cm.
>
> **After.** Under the tested load, the simulated bridge bends by 2 cm.

**Edit 2.** The draft proves the stated result in Theorem 2. The edit adds "When stiffness is positive" and attributes the guarantee to Theorem 2, so that the uniqueness claim names both its supporting proof and its condition.

> **Before.** The equilibrium is unique.
>
> **After.** When stiffness is positive, Theorem 2 guarantees that the equilibrium is unique.

**Edit 3.** Theorem 1 assumes independent errors, which these sensors violate without disproving the theorem. The edit replaces "make Theorem 1 false" with a statement that the theorem does not apply because the errors are correlated, so that an unmet assumption is not mistaken for a false theorem.

> **Before.** The correlated errors in these sensors make Theorem 1 false.
>
> **After.** Theorem 1 does not apply to these sensors because their errors are correlated.

**Edit 4.** The draft establishes that positivity implies the nonzero condition and that the latter adds no useful information. The edit, a proposal to the author, removes "nonzero" while keeping "positive", so that the condition is simpler but covers exactly the same values of x.

> **Before.** For positive, nonzero x, the bound holds.
>
> **After.** For positive x, the bound holds.

**Edit 5.** The draft reports observations from only five tested mixtures. The edit replaces "Every mixture" with "Each of the five tested mixtures", so that the claim describes the observations without promising the same outcome for untested mixtures.

> **Before.** Every mixture settles within an hour.
>
> **After.** Each of the five tested mixtures settles within an hour.
