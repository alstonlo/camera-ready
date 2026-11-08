# Make theorem statements self-contained

Introduce a theorem, lemma, or algorithm with a complete sentence, using a colon only after a complete clause. Make the formal statement self-contained: state the type of each object ("the linear operator A") and define every symbol before use. Keep motivation and informal commentary outside the statement. When the hypotheses run for several lines, flag the statement and propose extracting them into named conditions defined before it ("Assumption 1 (smoothness)").

## Details

Keep every assumption inside the theorem statement, because an assumption is part of the claim rather than commentary; when proposing named conditions, retain every restriction. For assumptions that appear unnecessary, follow [formal support](../claims/evidence-kind.md).

## Examples

The paragraph before the theorem restricts the discussion to rectangles.

> Bad: Theorem 1. The diagonals of a quadrilateral have equal lengths.
>
> Good: Theorem 1. The diagonals of a rectangle have equal lengths.

> Bad: We prove that: Theorem 1. Every square is a rectangle.
>
> Good: We prove the following result: Theorem 1. Every square is a rectangle.

Before the theorem, the draft defines $a$, $b$, and $c$ as the interior angles of a Euclidean triangle.

> Bad: Theorem 2. The sum of $a$, $b$, and $c$ is 180°.
>
> Good: Theorem 2. Let $a$, $b$, and $c$ be the interior angles of a Euclidean triangle. Their sum is 180°.

The draft defines $n$ as the number of items and $s$ as storage; the condition $n > 0$ remains part of the theorem.

> Bad: Theorem 3. This bound controls storage. If $n>0$, then $s(n)\leq 2n$.
>
> Good: This bound controls storage. Theorem 3. If $n>0$, then $s(n)\leq 2n$.

The theorem's hypotheses run across several lines in the draft; the Good line proposes a named assumption for the author.

> Bad: Theorem 4. If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, where $a<b$, then $f$ satisfies the mean value theorem.
>
> Good: Assumption 1 (regularity): Let $a<b$, and let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Theorem 4. Under Assumption 1, $f$ satisfies the mean value theorem.
