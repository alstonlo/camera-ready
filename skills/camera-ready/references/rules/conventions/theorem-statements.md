# Make theorem statements self-contained

Introduce a theorem, lemma, or algorithm with a complete sentence, and use a colon only after a complete clause. Make the formal statement self-contained: state each object's type and define every symbol before use. Keep motivation and informal comments outside the statement. If hypotheses run for several lines, flag the statement and suggest extracting them into named conditions defined before it (see Details).

## Details

State the type of each object, as in "the linear operator $A$". Keep every assumption in the theorem statement, because an assumption is part of the claim rather than commentary. When suggesting named conditions, such as "Assumption 1 (smoothness)", preserve every restriction. If an assumption seems unnecessary, follow [formal support](../claims/evidence-kind.md).

## Examples

**Edit 1.** The edit replaces "We prove that" with "We prove the following result", so that the colon follows a complete clause rather than a clause still missing what is proved.

> **Before.** We prove that: Theorem 1. Every square is a rectangle.
>
> **After.** We prove the following result: Theorem 1. Every square is a rectangle.

**Edit 2.** The draft defines the angles before the theorem. The edit defines $a$, $b$, and $c$ as the interior angles of a Euclidean triangle inside the theorem and refers to "Their sum", so that the symbols are defined before use and the statement can be understood on its own.

> **Before.** Theorem 2. The sum of $a$, $b$, and $c$ is 180°.
>
> **After.** Theorem 2. Let $a$, $b$, and $c$ be the interior angles of a Euclidean triangle. Their sum is 180°.

**Edit 3.** The draft defines $n$ as the number of items and $s$ as storage. The edit moves "The following bound gives an upper limit on storage" before "Theorem 3", so that the explanation of purpose sits outside the formal statement while the condition $n>0$ remains part of the claim.

> **Before.** Theorem 3. The following bound gives an upper limit on storage. If $n>0$, then $s(n)\leq 2n$.
>
> **After.** The following bound gives an upper limit on storage. Theorem 3. If $n>0$, then $s(n)\leq 2n$.

**Edit 4.** The theorem's assumptions take several lines in the draft. The edit, a proposal to the author, moves $a<b$ and the continuity and differentiability conditions into "Assumption 1 (regularity)" before the theorem and uses "Under Assumption 1" in the theorem, so that the statement is shorter while retaining every restriction.

> **Before.** Theorem 4. If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, where $a<b$, then $f$ satisfies the mean value theorem.
>
> **After.** Assumption 1 (regularity): Let $a<b$, and let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Theorem 4. Under Assumption 1, $f$ satisfies the mean value theorem.
