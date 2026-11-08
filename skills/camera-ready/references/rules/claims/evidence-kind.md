# Identify the kind of evidence supporting each claim

When a sentence reads like a theorem but cites no formal result and states no conditions, clarify its status: link it to the proved result and its assumptions, restate it as the empirical or intuitive claim the draft supports, or flag it. When the text uses a theorem to support an empirical claim, check that the theorem's assumptions hold in that setting and flag any invalid application; an unmet assumption makes the theorem inapplicable, not false. Never drop a condition from a theorem or other formal statement to simplify it; instead, flag any condition that seems unnecessary. Distinguish proofs, model calculations, simulations, and measurements of the real system. Flag any claim that extends a model result to the real system without supporting evidence, though a valid claim limited to the model needs no experiment or field study of the real system.

## Details

Universal claims about all cases, inputs, executions, or admissible parameters can signal a formal claim even without the word "theorem". Locate the supporting result and its conditions before judging whether it applies.

Propose a simpler mathematical condition only when the draft establishes that it is equivalent and the removed restriction adds no useful information. Flag a suspected error in a proof separately from an invalid application of a valid theorem.

## Examples

The draft reports the bridge's response only in a simulation, with no measurements of the actual bridge; the revision is proposed to the author.

> Bad: Under the tested load, the bridge bends by 2 cm.
>
> Good: In the simulation, under the tested load, the bridge bends by 2 cm.

The draft's Theorem 2 proves uniqueness for positive stiffness.

> Bad: The equilibrium is unique.
>
> Good: By Theorem 2, the equilibrium is unique when stiffness is positive.

The draft reports only that five tested mixtures settled within an hour.

> Bad: Every mixture settles within an hour.
>
> Good: Each of the five tested mixtures settles within an hour.

The draft states that Theorem 1 assumes independent errors and that these sensors have correlated errors; the revision is proposed to the author.

> Bad: The correlated errors in these sensors make Theorem 1 false.
>
> Good: The correlated errors in these sensors make Theorem 1 inapplicable here.

The draft proves the convergence result only for positive step sizes.

> Bad: Theorem 3 guarantees convergence for any step size.
>
> Good: Theorem 3 guarantees convergence for any positive step size.

The draft calculates the load from a static model and reports no simulation; the revision is proposed to the author.

> Bad: The simulation gives a load of 6 N.
>
> Good: The model calculation gives a load of 6 N.

The draft establishes that positivity makes the nonzero condition redundant for this bound; the revision is proposed to the author.

> Bad: For positive, nonzero x, the bound holds.
>
> Good: For positive x, the bound holds.
