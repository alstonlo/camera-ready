# Open each proof with its strategy and state when each goal is met

Open each proof with its strategy and mark subgoals as they are completed. Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Add strategy or progress statements only when identifiable in the draft; otherwise, flag the omission. Follow [intensifiers](../prose/intensifiers.md) for "clearly" and "it is easy to see". See Details for cases and constructions.

## Details

Treat cases in the order announced and under the names given in the proof. Change the order only when the draft states that one case's argument depends on the result of another.

Separate the construction of an object from its use. At the transition, state the property of the constructed object that justifies the next step. If the draft neither explains the proof's strategy nor marks which goals are met, flag the omission rather than inventing an explanation.

## Examples

**Example 1.** The draft's proof assumes a largest integer and derives a contradiction by adding one.

> **Bad.** Let $n$ be the largest integer.
>
> **Good.** We argue by contradiction. Let $n$ be the largest integer.

**Example 2.** For this case, the draft introduces evenness as an assumption rather than a proved fact.

> **Bad.** The integer $n$ is even. Write $n=2k$.
>
> **Good.** Assume that the integer $n$ is even. Write $n=2k$.

**Example 3.** The draft lists the dry case first, but the proof of the dry case uses the bound established for the wet case.

> **Bad.** We treat the dry case, then the wet case. We begin with the wet case.
>
> **Good.** We treat the dry case, then the wet case. We begin with the wet case because the proof of the dry case uses the bound from the wet case.

**Example 4.** The draft has just constructed $S$ and proved that it is finite, and Lemma 2 applies to finite sets.

> **Bad.** We now apply Lemma 2 to $S$.
>
> **Good.** We have constructed a finite set $S$. We now apply Lemma 2 to $S$.
