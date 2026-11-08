# Specify what an efficiency claim counts

For an efficiency claim such as "linear", "optimal", or "asymptotically faster", check that the text states the input-size variable, the resource counted (time, memory, or messages), the case analyzed (worst, average, or amortized), the assumptions, and whether preprocessing and output costs are included. Add a missing fact that the draft states elsewhere; otherwise flag it. A better asymptotic bound alone does not establish a lower running time. Flag suspected analytical errors without changing the mathematics.

## Details

Identify the input-size variables and other parameters on which the cost depends. State whether the analysis counts time, memory, messages, or another resource, and whether it gives a worst-case, average-case, expected, or amortized bound. These cases are not interchangeable.

Check whether the analysis includes preparing an index and producing the output, especially when the prose claims an end-to-end cost. An operation treated as constant cost may depend on an object whose size is unbounded in the stated model; flag that mismatch.

A better asymptotic growth rate does not establish lower elapsed time at the tested sizes. Constants and resource bottlenecks may matter, but do not infer their values or recompute the analysis.

Distinguish an upper bound for one algorithm from a lower bound on solving the problem. Neither bound alone establishes optimality. Flag an apparent mathematical error for the author, even when the correction seems straightforward.

## Examples

The draft's analysis counts the worst-case time to scan a table and defines its size variable as the number of cells (rows times columns).

- Bad: The worst-case time to scan the table is linear.
- Good: The worst-case time to scan the table is linear in the number of cells.
