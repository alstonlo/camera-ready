# Open each proof with its strategy and state when each goal is met

Open each proof with its strategy and mark subgoals as they are completed. Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Add strategy or progress statements only when identifiable in the draft; otherwise, flag the omission. Follow [intensifiers](../prose/intensifiers.md) for "clearly" and "it is easy to see". See Details for cases and constructions.

## Details

Treat cases in the order announced and under the names given in the proof. Change the order only when the draft states that one case's argument depends on the result of another.

Separate the construction of an object from its use. At the transition, state the property of the constructed object that justifies the next step. If the draft neither explains the proof's strategy nor marks which goals are met, flag the omission rather than inventing an explanation.

## Examples

**Edit 1.** The proof later derives a contradiction by adding one to $n$. The edit adds "We argue by contradiction" before the assumption so that readers know the proof's strategy from the start.

> **Before.** Let $n$ be the largest integer.
>
> **After.** We argue by contradiction. Let $n$ be the largest integer.

**Edit 2.** The draft treats evenness as an assumption for this case. The edit adds "Assume that" before "the integer $n$ is even" so that readers recognize an assumption rather than an established fact.

> **Before.** The integer $n$ is even. Write $n=2k$.
>
> **After.** Assume that the integer $n$ is even. Write $n=2k$.

**Edit 3.** The draft establishes that the dry case needs the bound proved in the wet case. The edit adds the reason for beginning with the wet case, explaining why the proof departs from the announced order.

> **Before.** We treat the dry case, then the wet case. We begin with the wet case.
>
> **After.** We treat the dry case, then the wet case. We begin with the wet case because the proof of the dry case uses the bound from the wet case.

**Edit 4.** The draft has just constructed $S$ and proved it finite, and Lemma 2 applies to finite sets. The edit adds "We have constructed a finite set $S$" to mark the completed construction and identify the property that permits applying the lemma.

> **Before.** We now apply Lemma 2 to $S$.
>
> **After.** We have constructed a finite set $S$. We now apply Lemma 2 to $S$.
