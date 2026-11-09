# Open each proof with its strategy and state when each goal is met

Open each proof with its strategy and mark subgoals as they are completed. Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Add strategy or progress statements only when identifiable in the draft; otherwise, flag the omission. Follow [intensifiers](../prose/intensifiers.md) for "clearly" and "it is easy to see". See Details for cases and constructions.

## Details

Treat cases in the order announced and under the names given in the proof. Change the order only when the draft states that one case's argument depends on the result of another.

Separate the construction of an object from its use. At the transition, state the property of the constructed object that justifies the next step. If the draft neither explains the proof's strategy nor marks which goals are met, flag the omission rather than inventing an explanation.

## Examples

**Edit 1.** Suppose the proof later derives a contradiction by adding one to $n$. Before:

> Let $n$ be the largest integer.

After:

> We argue by contradiction. Let $n$ be the largest integer.

**Edit 2.** Say the draft assumes evenness for this case. Before:

> The integer $n$ is even. Write $n=2k$.

After:

> Assume that the integer $n$ is even. Write $n=2k$.

**Edit 3.** Suppose the draft establishes that the dry case uses the bound proved in the wet case. Before:

> We treat the dry case, then the wet case. We begin with the wet case.

After:

> We treat the dry case, then the wet case. We begin with the wet case because the proof of the dry case uses the bound from the wet case.

The announced order can stay because the proof gives a reason for handling the cases in a different order.

**Edit 4.** Imagine the draft has just constructed $S$ and proved it finite, and Lemma 2 applies to finite sets. Before:

> We now apply Lemma 2 to $S$.

After:

> We have constructed a finite set $S$. We now apply Lemma 2 to $S$.
