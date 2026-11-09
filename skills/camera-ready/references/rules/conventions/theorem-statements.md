# Make theorem statements self-contained

Introduce a theorem, lemma, or algorithm with a complete sentence, and use a colon only after a complete clause. Make the formal statement self-contained: state each object's type and define every symbol before use. Keep motivation and informal comments outside the statement. If hypotheses run for several lines, flag the statement and suggest extracting them into named conditions defined before it (see Details).

## Details

State the type of each object, as in "the linear operator $A$". Keep every assumption in the theorem statement, because an assumption is part of the claim rather than commentary. When suggesting named conditions, such as "Assumption 1 (smoothness)", preserve every restriction. If an assumption seems unnecessary, follow [formal support](../claims/evidence-kind.md).

## Examples

**Example 1.** Good completes the clause before the colon; "We prove that" still needs the statement of what is proved.

> **Bad.** We prove that: Theorem 1. Every square is a rectangle.
>
> **Good.** We prove the following result: Theorem 1. Every square is a rectangle.

**Example 2.** The draft defines the angles before the theorem. Good repeats the definition inside the theorem so that readers can understand the statement on its own.

> **Bad.** Theorem 2. The sum of $a$, $b$, and $c$ is 180°.
>
> **Good.** Theorem 2. Let $a$, $b$, and $c$ be the interior angles of a Euclidean triangle. Their sum is 180°.

**Example 3.** The draft defines $n$ as the number of items and $s$ as storage. Good moves the explanation of the bound's purpose outside the theorem but keeps $n>0$, which restricts when the bound holds.

> **Bad.** Theorem 3. The following bound gives an upper limit on storage. If $n>0$, then $s(n)\leq 2n$.
>
> **Good.** The following bound gives an upper limit on storage. Theorem 3. If $n>0$, then $s(n)\leq 2n$.

**Example 4.** The theorem's assumptions take several lines in the draft. Good proposes a named assumption to shorten the statement while retaining every restriction.

> **Bad.** Theorem 4. If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, where $a<b$, then $f$ satisfies the mean value theorem.
>
> **Good.** Assumption 1 (regularity): Let $a<b$, and let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Theorem 4. Under Assumption 1, $f$ satisfies the mean value theorem.
