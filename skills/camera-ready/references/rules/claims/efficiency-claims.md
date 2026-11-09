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

> **Context.** The draft states that the assay costs $4 per sample for reagents and excludes sample preparation.
>
> **Bad.** The assay costs $4 per sample.
>
> **Good.** The assay costs $4 per sample for reagents, excluding sample preparation.

> **Context.** The draft analyzes the worst-case time to scan a table. It defines table size as the number of cells (rows times columns).
>
> **Bad.** The worst-case time to scan the table is linear.
>
> **Good.** The worst-case time to scan the table is linear in the number of cells.

> **Context.** The draft reports that the washer uses 3 liters of water per washed tray.
>
> **Bad.** The washer uses 3 liters.
>
> **Good.** The washer uses 3 liters of water per washed tray.

> **Context.** The draft measures the heater's energy use at an ambient temperature of 20 °C.
>
> **Bad.** The heater uses 2 kWh per day.
>
> **Good.** At an ambient temperature of 20 °C, the heater uses 2 kWh per day.

> **Context.** The draft compares the kiln's fuel use with that of the uninsulated kiln.
>
> **Bad.** The kiln uses less fuel per batch.
>
> **Good.** The kiln uses less fuel per batch than the uninsulated kiln.

> **Context.** The draft calculates the heater's 80% efficiency by dividing the heat delivered to the water by the electrical energy supplied.
>
> **Bad.** The heater's efficiency is 80%.
>
> **Good.** The heater delivers 80% of the supplied electrical energy as heat to the water.

> **Context.** The draft calculates yield by dividing the amount of isolated product by the theoretical yield from ethanol, the limiting reagent.
>
> **Bad.** The product yield is 60%.
>
> **Good.** The isolated product yield is 60% of the theoretical yield from ethanol.

> **Context.** The draft reports that ten samples suffice to estimate the mean within 2 mg.
>
> **Bad.** The procedure needs ten samples.
>
> **Good.** The procedure needs ten samples to estimate the mean within 2 mg.

> **Context.** The draft gives an amortized bound for insertion time and defines n as the number of stored readings.
>
> **Bad.** The time per insertion is O(1).
>
> **Good.** The amortized time per insertion is O(1).

> **Context.** The draft excludes the time to build the index from its query bound. It defines n as the number of stored items.
>
> **Bad.** Each query takes O(log n) time.
>
> **Good.** After the index is built, each query takes O(log n) time.

> **Context.** The draft reports lower energy use per item but higher total energy use when more items are produced. Propose the revision to the author.
>
> **Bad.** The new process uses less energy.
>
> **Good.** The new process uses less energy per item.

> **Context.** The draft establishes that method A's time grows asymptotically more slowly than method B's, but reports no timing comparison. Propose the revision to the author.
>
> **Bad.** Method A has lower elapsed time than method B.
>
> **Good.** Method A's time grows asymptotically more slowly than method B's.

> **Context.** The draft's analysis counts the time to scan an n-cell row as O(n), but this sentence calls the scan constant-time. Propose the revision to the author.
>
> **Bad.** The algorithm performs a constant-time row scan.
>
> **Good.** The algorithm performs a row scan whose time is linear in n.

> **Context.** The draft proves an upper bound for one algorithm and defines n as the number of entries. Propose the revision to the author.
>
> **Bad.** Every algorithm for the problem requires quadratic time.
>
> **Good.** This algorithm requires at most quadratic time.
