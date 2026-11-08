# Specify what an efficiency claim counts

For a claim about efficiency, speed, yield, cost, sample efficiency, or scaling, check that the text states what is counted and per what unit, the conditions and assumptions, the comparator if a comparison is claimed, and which costs are included or excluded. Define both the numerator and the denominator of a ratio. For an analytical bound, also check that the text defines the size variables and specifies which case is analyzed (see Details). Add any missing detail that the draft states elsewhere; otherwise flag it. A better ratio or asymptotic bound alone does not establish lower total cost under the claimed conditions. Flag suspected analytical errors without changing the mathematics.

## Details

For yield, identify the limiting reagent and whether the product is crude or isolated. For sample efficiency, identify the target the samples must achieve. Check whether the claim omits costs such as setup, startup energy, discarded material, failed runs, preparation, purification, or calibration. Apply [comparability checks](variability.md) to claimed gains.

For analytical bounds, distinguish worst-case, average-case, expected, and amortized costs. Check whether the cost includes preparing an index and producing the output. If the analysis treats an operation as constant-cost when it depends on an object whose size is unbounded in the stated model, flag that mismatch.

Distinguish an upper bound for one algorithm from a lower bound on solving the problem; neither bound alone establishes optimality. Constants and resource bottlenecks can affect elapsed time at tested sizes; do not infer their values or recompute the analysis.

## Examples

> **Context.** The draft states that the assay costs $4 per sample for reagents and excludes sample preparation.
>
> **Bad.** The assay costs $4 per sample.
>
> **Good.** The assay costs $4 per sample for reagents, excluding sample preparation.

> **Context.** The draft's analysis counts the worst-case time to scan a table and defines its size variable as the number of cells (rows times columns).
>
> **Bad.** The worst-case time to scan the table is linear.
>
> **Good.** The worst-case time to scan the table is linear in the number of cells.

> **Context.** The draft defines the reported use as 3 liters of water per washed tray.
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

> **Context.** The draft defines the 80% efficiency as heat delivered to the water divided by electrical energy supplied.
>
> **Bad.** The heater's efficiency is 80%.
>
> **Good.** The heater delivers 80% of the supplied electrical energy as heat to the water.

> **Context.** The draft defines the yield as isolated product relative to the theoretical yield from the limiting reagent, ethanol.
>
> **Bad.** The product yield is 60%.
>
> **Good.** The isolated product yield is 60% of the theoretical yield from ethanol.

> **Context.** The draft reports that ten samples suffice to estimate the mean within 2 mg.
>
> **Bad.** The procedure needs ten samples.
>
> **Good.** The procedure needs ten samples to estimate the mean within 2 mg.

> **Context.** The draft's analysis gives an amortized bound, with n defined as the number of stored readings.
>
> **Bad.** The time per insertion is O(1).
>
> **Good.** The amortized time per insertion is O(1).

> **Context.** The draft's query bound excludes the time to build the index, with n defined as the number of stored items.
>
> **Bad.** Each query takes O(log n) time.
>
> **Good.** After the index is built, each query takes O(log n) time.

> **Context.** The draft reports lower energy use per item but higher total energy use at the larger production volume; the revision is proposed to the author.
>
> **Bad.** The new process uses less energy.
>
> **Good.** The new process uses less energy per item.

> **Context.** The draft establishes lower asymptotic time growth for method A but reports no timing comparison; the revision is proposed to the author.
>
> **Bad.** Method A has lower elapsed time than method B.
>
> **Good.** Method A has lower asymptotic time growth than method B.

> **Context.** The draft counts scanning an n-cell row as O(n) time but calls it constant time in this sentence; the revision is proposed to the author.
>
> **Bad.** The algorithm performs a constant-time row scan.
>
> **Good.** The algorithm performs a row scan whose time is linear in n.

> **Context.** The draft proves an upper bound for one algorithm, with n defined as the number of entries; the revision is proposed to the author.
>
> **Bad.** Every algorithm for the problem requires quadratic time.
>
> **Good.** This algorithm requires at most quadratic time.
