# Specify what an efficiency claim counts

For a claim about speed, yield, cost, samples needed, or scaling, state the following. Fill gaps from elsewhere in the draft or flag them:

- The unit counted, the conditions and assumptions, and the costs included or excluded.
- The baseline of each comparison.
- A ratio's numerator and denominator.
- An analytical bound's size variables and the case analyzed.

A better ratio or asymptotic bound alone does not show lower total cost under the claimed conditions. An upper bound on one algorithm's cost does not establish a lower bound for every algorithm solving the problem. Flag suspected errors in the analysis without changing the mathematics.

## Details

Apply these checks to claimed gains, along with the [comparability checks](variability.md):

- Yield: Name the limiting reagent, which sets how much product can form. State whether the product is crude (unpurified) or isolated (separated from the reaction mixture).
- Samples needed: State the target the method must reach with those samples.
- Included costs: Check for omitted setup, startup energy, discarded material, failed runs, preparation, purification, or calibration.

For analytical bounds, which are derived mathematically rather than measured, distinguish these costs:

- Worst-case cost is the greatest cost for any input of a given size.
- Average-case cost averages over a distribution of inputs.
- Expected cost averages over the randomness specified in the analysis.
- Amortized cost averages the cost per operation over a sequence of operations.

Check whether the cost includes building an index for later lookup and producing the output. If an operation's cost depends on an object's size and the stated model places no limit on that size, flag any claim that the operation has constant cost.

An upper bound on one algorithm's cost does not by itself prove that the algorithm is optimal. Neither does a lower bound that every algorithm must meet to solve the problem. An asymptotic bound describes how cost grows with problem size; constants and resource limits can still affect elapsed time at the sizes tested. Do not infer their values or redo the analysis.

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

**Edit 4.** Suppose the draft proves a quadratic upper bound for the algorithm under discussion but no lower bound for the problem. The editor flags the unsupported lower bound and proposes After to the author.

> **Before.** Every algorithm for the problem requires quadratic time.

> **After.** This algorithm requires at most quadratic time.

**Edit 5.** Imagine the draft reports higher total energy use when production increases, despite lower energy use per item.

> **Before.** The new process uses less energy.

> **After.** The new process uses less energy per item.
