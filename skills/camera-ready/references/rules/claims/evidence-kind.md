# Identify the kind of evidence supporting each claim

If a sentence reads like a theorem but gives no formal result or conditions, link it to the proved result and its assumptions, restate it as the observed or intuitive claim the draft supports, or flag it. If the draft applies a theorem to observations or experiments, flag the claim when the theorem's assumptions do not hold. An unmet assumption makes a theorem inapplicable, not false. Never drop a condition to simplify a formal statement. Instead, flag any condition that seems unnecessary (see Details). Distinguish proofs, calculations from a model, simulations, and measurements of the real system. Flag any claim that a model result holds in the real system without evidence. A valid claim limited to the model needs no experiment or field study.

## Details

A statement about all cases, inputs, runs, or allowed parameter values may claim a mathematical guarantee even without the word "theorem". Find the supporting result and its conditions before judging whether the result applies.

Propose a simpler mathematical condition only when the draft shows that the two conditions are equivalent and that the condition you would remove adds no useful information. Flag a suspected error in a proof separately from a claim that applies a valid theorem where its assumptions do not hold.

## Examples

**Example 1.** The draft reports only a simulation of the bridge, with no measurements of the actual bridge. Propose the revision to the author.

> **Bad.** Under the tested load, the bridge bends by 2 cm.
>
> **Good.** Under the tested load, the simulated bridge bends by 2 cm.

**Example 2.** The draft's Theorem 2 proves that the equilibrium is unique when stiffness is positive.

> **Bad.** The equilibrium is unique.
>
> **Good.** When stiffness is positive, Theorem 2 guarantees that the equilibrium is unique.

**Example 3.** The draft reports only that five tested mixtures settled within an hour.

> **Bad.** Every mixture settles within an hour.
>
> **Good.** Each of the five tested mixtures settles within an hour.

**Example 4.** The draft states that Theorem 1 assumes independent errors and that these sensors have correlated errors. Propose the revision to the author.

> **Bad.** The correlated errors in these sensors make Theorem 1 false.
>
> **Good.** Theorem 1 does not apply to these sensors because their errors are correlated.

**Example 5.** The draft proves the convergence result only for positive step sizes.

> **Bad.** Theorem 3 guarantees convergence for any step size.
>
> **Good.** Theorem 3 guarantees convergence for any positive step size.

**Example 6.** The draft calculates the load from a static model and reports no simulation. Propose the revision to the author.

> **Bad.** The simulation gives a load of 6 N.
>
> **Good.** The load calculated from the model is 6 N.

**Example 7.** The draft establishes that requiring x to be positive makes the nonzero condition unnecessary for this bound. Propose the revision to the author.

> **Bad.** For positive, nonzero x, the bound holds.
>
> **Good.** For positive x, the bound holds.
