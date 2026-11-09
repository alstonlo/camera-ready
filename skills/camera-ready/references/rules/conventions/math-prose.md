# Write mathematics as grammatical prose

Read each formula as part of its sentence so that words and mathematics form a grammatical sentence. Begin sentences and clauses with words rather than bare symbols, and spell out sentence-initial numbers. Separate adjacent formulas with words, including across sentence boundaries. Except in work on logic, write quantifiers and relations in prose as words. End a displayed formula with a period when the sentence ends, or a comma when it continues. Put a colon before a display only after a complete clause. A trailing "where" clause may define symbols, but put any definition needed to understand a claim before that claim. See Details for examples and LaTeX paragraph breaks.

## Details

To check the grammar, mentally replace each formula with words that play the same role in the sentence. An equality can supply the verb, because "$a=b$" reads as "$a$ equals $b$". An expression without a relation, such as $a+b$, usually acts as a noun phrase.

In prose, write "for all" rather than $\forall$, and write "is at most 0.1" rather than "is $\le 0.1$". Work on logic may use symbolic notation.

In LaTeX source, a blank line starts a new paragraph. Do not put blank lines around a displayed formula that continues its paragraph, even when the formula ends a sentence.

## Examples

**Edit 1.**

> **Before.** The area of a circle of radius $r$ is: \[\pi r^2.\]

> **After.** The area of a circle of radius $r$ is \[\pi r^2.\]

**Edit 2.** Imagine a paper on logic in which this passage explains the universal quantifier.

> **Before.** $P$ is the predicate in $\forall x\,P(x)$.

> **After.** The symbol $P$ is the predicate in $\forall x\,P(x)$.

The quantifier stays in symbols because the passage discusses the notation itself.

**Edit 3.**

> **Before.** The value of $q$ is positive, where $q$ denotes net inflow.

> **After.** Let $q$ denote net inflow. The value of $q$ is positive.

**Edit 4.** Suppose the draft has already defined $a$ and $b$.

> **Before.**
>
> ```latex
> The total is
>
> \[s=a+b.\]
> We compare it with the limit.
> ```

> **After.**
>
> ```latex
> The total is
> \[s=a+b.\]
> We compare it with the limit.
> ```
