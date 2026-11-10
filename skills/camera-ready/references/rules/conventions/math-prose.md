# Write mathematics as grammatical prose

An equality can supply a sentence's verb; to check the grammar, mentally replace each formula with words that play the same role and reread. Begin sentences and clauses with words, not bare symbols ("A function f is semicontinuous if...", not "f is semicontinuous if..."), and spell out sentence-initial numbers regardless of the number-spelling cutoff. Separate adjacent formulas with words ("Consider S_q, where q < p"), even across sentence boundaries. Reword a sentence-final symbol that could be read as part of the next name or abbreviation. Except in work on logic, write quantifiers and implications in prose as words ("for all" for $\forall$). Never let a relation symbol stand for words in a verbal phrase ("is at most 0.1", not "is $\le 0.1$"). End a displayed formula with a period when the sentence ends or a comma when it continues. Put a colon before a display only after a complete clause ("we define the loss as follows:"), never after an incomplete one ("the loss is:"). A trailing "where" clause may define symbols, but put any definition needed to understand a claim before the claim: in "Every convex polynomial has even degree, where a function is convex if ...", move the definition of convexity first. In LaTeX source, put no blank lines around a displayed formula that continues its paragraph.

## Details

An expression without a relation, such as $a+b$, usually acts as a noun phrase.

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
