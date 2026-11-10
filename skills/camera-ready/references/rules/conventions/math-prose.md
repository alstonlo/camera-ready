# Write mathematics as grammatical prose

An equality can supply a sentence's verb. Check the grammar by mentally replacing each formula with words that play the same role.

- Begin sentences and clauses with words, not bare symbols. Spell out sentence-initial numbers regardless of the number-spelling cutoff.
- Separate adjacent formulas with words ("Consider S_q, where q < p"), even across sentence boundaries.
- Reword a sentence-final symbol that could be read as part of the next name or abbreviation.
- Except in work on logic, write quantifiers and implications in prose as words ("for all" for $\forall$).
- Never let a relation symbol stand for words in a verbal phrase ("is at most 0.1", not "is $\le 0.1$").
- A trailing "where" clause may define symbols, but put definitions needed to understand a claim before it.
- End a displayed formula with a period if the sentence ends or a comma if it continues.
- Put a colon before a display only after a complete clause ("we define the loss as follows:"), never after an incomplete one ("the loss is:").
- In LaTeX source, put no blank lines around a displayed formula that continues its paragraph.

## Details

An expression without a relation, such as $a+b$, usually acts as a noun phrase.

## Examples

**Edit 1.**

> **Before.** The area of a circle of radius $r$ is: \[\pi r^2.\]

> **After.** The area of a circle of radius $r$ is \[\pi r^2.\]

**Edit 2.** Suppose this passage in a paper on logic explains the universal quantifier.

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
