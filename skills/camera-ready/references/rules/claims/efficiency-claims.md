# Specify what an efficiency claim counts

A claim about efficiency, speed, yield, cost, samples needed, or scaling must state what it counts and per what unit, its conditions and assumptions, and which costs it includes or excludes. A comparison must name what it compares against, and a ratio must define its numerator and denominator. An analytical bound must define each size variable and the case analyzed (see Details). Add any missing detail the draft states elsewhere; otherwise, flag it. A better ratio or asymptotic bound alone does not show lower total cost under the claimed conditions. Flag suspected errors in the analysis without changing the mathematics.

## Details

For yield, name the limiting reagent, which is the reactant that runs out first and so sets how much product can form. State whether the product is crude, meaning unpurified, or isolated, meaning separated from the reaction mixture. For a claim about how many samples a method needs, state the target that the method must reach with those samples. Check whether the claim omits costs such as setup, startup energy, discarded material, failed runs, preparation, purification, or calibration. Apply [comparability checks](variability.md) to claimed gains.

For analytical bounds, which are limits on cost derived mathematically rather than measured, distinguish the following costs:

- Worst-case cost is the greatest cost for any input of a given size.
- Average-case cost averages over a distribution of inputs.
- Expected cost averages over the randomness specified in the analysis.
- Amortized cost averages the cost per operation over a sequence of operations.

Check whether the cost includes building an index for later lookup and producing the output. If an operation's cost depends on an object's size and the stated model places no limit on that size, flag any claim that the operation has constant cost.

Distinguish an upper bound on one algorithm's cost from a lower bound that every algorithm must meet to solve the problem. Neither bound alone proves that an algorithm is optimal, meaning as efficient as possible. An asymptotic bound describes how fast cost grows as problem size grows, so constants in the bound and resource limits can still affect elapsed time at the sizes tested. Do not infer their values or redo the analysis.

## Examples

**Edit 1.** Suppose the draft specifies elsewhere that the assay cost covers reagents and excludes sample preparation.

> **Before.** The assay costs $4 per sample.

> **After.** The assay costs $4 per sample for reagents, excluding sample preparation.

**Edit 2.** Say the draft defines heater efficiency as the fraction of supplied electrical energy delivered as heat to the water.

> **Before.** The heater's efficiency is 80%.

> **After.** The heater delivers 80% of the supplied electrical energy as heat to the water.

**Edit 3.** Suppose the draft establishes that method A has slower asymptotic time growth than method B but reports no measured times.

> **Before.** Method A has lower elapsed time than method B.

> **After.** Method A's time grows asymptotically more slowly than method B's.

**Edit 4.** If the draft proves a quadratic upper bound for the algorithm under discussion, the claim can be narrowed as follows.

> **Before.** Every algorithm for the problem requires quadratic time.

> **After.** This algorithm requires at most quadratic time.

**Edit 5.** Imagine the draft reports higher total energy use when production increases, despite lower energy use per item.

> **Before.** The new process uses less energy.

> **After.** The new process uses less energy per item.
