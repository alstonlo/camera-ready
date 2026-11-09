# Write mathematics as grammatical prose

Read each formula as part of its sentence so that words and mathematics form a grammatical sentence. Begin sentences and clauses with words rather than bare symbols, and spell out sentence-initial numbers. Separate adjacent formulas with words, including across sentence boundaries. Except in work on logic, write quantifiers and relations in prose as words. End a displayed formula with a period when the sentence ends, or a comma when it continues. Put a colon before a display only after a complete clause. A trailing "where" clause may define symbols, but put any definition needed to understand a claim before that claim. See Details for examples and LaTeX paragraph breaks.

## Details

To check the grammar, mentally replace each formula with words that play the same role in the sentence. An equality can supply the verb, because "$a=b$" reads as "$a$ equals $b$". An expression without a relation, such as $a+b$, usually acts as a noun phrase.

In prose, write "for all" rather than $\forall$, and write "is at most 0.1" rather than "is $\le 0.1$". Work on logic may use symbolic notation.

In LaTeX source, a blank line starts a new paragraph. Do not put blank lines around a displayed formula that continues its paragraph, even when the formula ends a sentence.

## Examples

**Example 1.**

> **Bad.** The area of a circle of radius $r$ is: \[\pi r^2.\]
>
> **Good.** The area of a circle of radius $r$ is \[\pi r^2.\]

**Example 2.** The draft defines $r$ as the radius of a circle.

> **Bad.** The circumference $2\pi r$.
>
> **Good.** The circumference is $2\pi r$.

**Example 3.**

> **Bad.** $r$ denotes the radius.
>
> **Good.** The symbol $r$ denotes the radius.

**Example 4.**

> **Bad.** 12 jars remain sealed.
>
> **Good.** Twelve jars remain sealed.

**Example 5.** The draft defines $a$ and $b$ as lengths.

> **Bad.** We compare $a$ $b$.
>
> **Good.** We compare $a$ with $b$.

**Example 6.** The draft defines $a$ as the observed length.

> **Bad.** We measure $a$. $b$ denotes the predicted length.
>
> **Good.** We measure $a$. The symbol $b$ denotes the predicted length.

**Example 7.** The passage states a bound on sample size in a paper outside mathematical logic.

> **Bad.** The bound holds $\forall n$.
>
> **Good.** The bound holds for all $n$.

**Example 8.**

> **Bad.** The error is $\leq 0.2$.
>
> **Good.** The error is at most 0.2.

**Example 9.** In a paper on logic, the passage explains the universal quantifier.

> **Bad.** $P$ is the predicate in $\forall x\,P(x)$.
>
> **Good.** The symbol $P$ is the predicate in $\forall x\,P(x)$.

**Example 10.** The draft defines $a$ and $b$ as two component masses.

> **Bad.** The total is \[s=a+b\]
>
> **Good.** The total is \[s=a+b.\]

**Example 11.** The draft defines $a$ and $b$ earlier as component masses and introduces $s$ here.

> **Bad.** The total is \[s=a+b\] where $s$ denotes total mass.
>
> **Good.** The total is \[s=a+b,\] where $s$ denotes total mass.

**Example 12.**

> **Bad.** The value of $q$ is positive, where $q$ denotes net inflow.
>
> **Good.** Let $q$ denote net inflow. The value of $q$ is positive.

**Example 13.** The draft defines $a$ and $b$ earlier, and the displayed formula belongs to the surrounding paragraph. Here, `\n` denotes a newline.

> **Bad.** `The total is\n\n\[s=a+b.\]\nWe compare it with the limit.`
>
> **Good.** `The total is\n\[s=a+b.\]\nWe compare it with the limit.`
