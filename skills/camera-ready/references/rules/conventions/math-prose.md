# Write mathematics as grammatical prose

Read each formula as part of the sentence so that the prose and mathematics together are grammatical. Begin sentences and clauses with words, not bare symbols, and spell out sentence-initial numbers. Separate adjacent formulas with words, including across sentence boundaries. In prose, write quantifiers and relations as words ("for all", not ∀; "is at most 0.1", not "is ≤ 0.1"), except in work on logic. Punctuate a displayed formula with a period when it ends a sentence and a comma when the sentence continues; use a colon before a display only after a complete clause. A trailing "where" clause may define symbols, but any definition needed to understand a claim must precede the claim. For LaTeX paragraph breaks, see the page.

## Details

Test grammar by mentally replacing each formula with a phrase of the same grammatical role: an equality may supply a verb, whereas a bare expression usually supplies a noun phrase.

In LaTeX, omit blank lines around a display that continues its paragraph, even when the display ends a sentence.

## Examples

> **Bad.** The area of a circle of radius $r$ is: \[\pi r^2.\]
>
> **Good.** The area of a circle of radius $r$ is \[\pi r^2.\]

> **Context.** The draft defines $r$ as the circle's radius.
>
> **Bad.** The circumference $2\pi r$.
>
> **Good.** The circumference is $2\pi r$.

> **Bad.** $r$ denotes the radius.
>
> **Good.** The symbol $r$ denotes the radius.

> **Bad.** 12 jars remain sealed.
>
> **Good.** Twelve jars remain sealed.

> **Context.** The draft defines $a$ and $b$ as lengths.
>
> **Bad.** We compare $a$ $b$.
>
> **Good.** We compare $a$ with $b$.

> **Context.** The draft defines $a$ as the observed length.
>
> **Bad.** We measure $a$. $b$ denotes the predicted length.
>
> **Good.** We measure $a$. The symbol $b$ denotes the predicted length.

> **Context.** The passage states a bound on sample size and is not part of work on logic.
>
> **Bad.** The bound holds $\forall n$.
>
> **Good.** The bound holds for all $n$.

> **Bad.** The error is $\leq 0.2$.
>
> **Good.** The error is at most 0.2.

> **Context.** The passage explains universal quantification in a logic paper.
>
> **Bad.** $P$ is the predicate in $\forall x\,P(x)$.
>
> **Good.** The symbol $P$ is the predicate in $\forall x\,P(x)$.

> **Context.** The draft defines $a$ and $b$ as the two component masses.
>
> **Bad.** The total is \[s=a+b\]
>
> **Good.** The total is \[s=a+b.\]

> **Context.** The draft has already defined $a$ and $b$ as component masses and introduces $s$ here.
>
> **Bad.** The total is \[s=a+b\] where $s$ denotes total mass.
>
> **Good.** The total is \[s=a+b,\] where $s$ denotes total mass.

> **Bad.** The value of $q$ is positive, where $q$ denotes net inflow.
>
> **Good.** Let $q$ denote net inflow. The value of $q$ is positive.

> **Context.** The display stays in the same paragraph, $a$ and $b$ are already defined, and `\n` denotes a newline.
>
> **Bad.** `The total is\n\n\[s=a+b.\]\nWe compare it with the limit.`
>
> **Good.** `The total is\n\[s=a+b.\]\nWe compare it with the limit.`
