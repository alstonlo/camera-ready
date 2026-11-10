# Open each proof with its strategy and state when each goal is met

Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Treat cases in the order and under the names the proof announces, and at the transition from constructing an object to using it, state the property that justifies the next step. Add strategy or progress statements only from the draft; otherwise, flag the omission. Follow [intensifiers](../prose/intensifiers.md) for "clearly" and "it is easy to see".

Flag deferred proofs whose stated dependencies form a cycle; a forward reference alone is no defect. Flag missing equality links between successive bounds when the draft establishes that their right-hand sides are equal.

## Details

Flag a proof that orders cases differently from their definition without a stated dependency. Change the order of cases only when the draft states that one case's argument depends on the result of another. If the draft neither explains the proof's strategy nor marks which goals are met, flag the omission rather than inventing an explanation.

## Examples

**Edit 1.** Suppose the proof later derives a contradiction by adding one to $n$.

> **Before.** Let $n$ be the largest integer.

> **After.** We argue by contradiction. Let $n$ be the largest integer.

**Edit 2.** Say the draft assumes evenness for this case.

> **Before.** The integer $n$ is even. Write $n=2k$.

> **After.** Assume that the integer $n$ is even. Write $n=2k$.

**Edit 3.** Suppose the draft establishes that the dry case uses the bound proved in the wet case.

> **Before.** We treat the dry case, then the wet case. We begin with the wet case.

> **After.** We treat the dry case, then the wet case. We begin with the wet case because the proof of the dry case uses the bound from the wet case.

The announced order can stay because the proof gives a reason for handling the cases in a different order.

**Edit 4.** Imagine the draft has just constructed $S$ and proved it finite, and Lemma 2 applies to finite sets.

> **Before.** We now apply Lemma 2 to $S$.

> **After.** We have constructed a finite set $S$. We now apply Lemma 2 to $S$.
