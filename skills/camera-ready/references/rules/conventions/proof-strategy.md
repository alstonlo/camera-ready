# Open each proof with its strategy and mark its progress

Open each proof with its strategy and mark subgoals as they are completed. Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Add a strategy or progress statement only when the draft makes it identifiable. For "clearly" and "it is easy to see", follow [intensifiers](../prose/intensifiers.md). For matching case order and separating a construction from its use, see the page.

## Details

Treat cases in the announced order and under the announced names unless a stated dependency requires another order.

Separate the construction of an object from its use; at the transition, state the property of the constructed object that supports the next step. Flag a missing strategy or progress statement rather than inventing one.

## Examples

> **Context.** The draft's proof assumes a largest integer and derives a contradiction by adding one.
>
> **Bad.** Let $n$ be the largest integer.
>
> **Good.** We argue by contradiction. Let $n$ be the largest integer.

> **Context.** The proof announces existence and uniqueness as its two subgoals, and the preceding paragraph proves existence.
>
> **Bad.** We next prove uniqueness.
>
> **Good.** Existence is established. We next prove uniqueness.

> **Context.** The draft introduces evenness as this case's assumption, not as a proved property.
>
> **Bad.** The integer $n$ is even. Write $n=2k$.
>
> **Good.** Assume that the integer $n$ is even. Write $n=2k$.

> **Context.** The draft has already defined the lengths $a$ and $b$ and introduces $s$ here as shorthand for their sum.
>
> **Bad.** We have $s=a+b$.
>
> **Good.** Define $s=a+b$.

> **Context.** The draft defers the convergence proof to Lemma 3.
>
> **Bad.** The sequence converges.
>
> **Good.** The sequence converges, as we prove in Lemma 3.

> **Context.** The draft proves the two cases independently.
>
> **Bad.** We treat the dry case, then the wet case. In the wet case, the mass doubles. In the dry case, the mass stays fixed.
>
> **Good.** We treat the dry case, then the wet case. In the dry case, the mass stays fixed. In the wet case, the mass doubles.

> **Context.** The draft identifies the first regime as the dry case.
>
> **Bad.** We treat the dry and wet cases. In the first regime, the mass stays fixed.
>
> **Good.** We treat the dry and wet cases. In the dry case, the mass stays fixed.

> **Context.** The draft announces the dry case first, but the dry-case argument uses the bound from the wet case.
>
> **Bad.** We treat the dry case, then the wet case. We begin with the wet case.
>
> **Good.** We treat the dry case, then the wet case. We begin with the wet case, because the dry-case argument uses the bound from the wet case.

> **Context.** The preceding construction shows that $S$ is finite, and Lemma 2 applies to finite sets.
>
> **Bad.** We now apply Lemma 2 to $S$.
>
> **Good.** The construction makes $S$ finite. We now apply Lemma 2 to $S$.
