# Use the correct type for operators, subscripts, and signs

Use upright type for multi-letter operators (`\log`, `\operatorname{softmax}`) and word subscripts (`\mathcal{L}_{\text{train}}`), but italic for variable subscripts (`x_i`). Use × (`\times`) for multiplication and multiplicative factors rather than x or `*`, except in code. Write negative values in math mode (`$-0.3$`) to give them minus signs rather than hyphens. Fix LaTeX typography only when mathematical meaning stays unchanged, and flag any change to symbols, grouping, delimiters, or operator meaning. Propose a clearer form for ambiguous notation, such as a slash fraction whose denominator has no clear end, only when the draft establishes the intended meaning. Flag stacked inline fractions that disrupt line spacing, exponent fractions too small to read, and oversized delimiters; suggest slash fractions or smaller delimiters only with grouping preserved.

## Details

This rule has no further details.

## Examples

**Edit 1.** Suppose the draft describes this operation as taking a logarithm.

> **Before.** We evaluate $log(x)$.

> **After.** We evaluate $\log(x)$.

**Edit 2.** Say the draft indexes samples by $i$ and defines "cool" as a word label for cooling time.

> **Before.** We compare $t_i$ with $t_{cool}$.

> **After.** We compare $t_i$ with $t_{\text{cool}}$.

The variable index $i$ stays italic; the word label "cool" is upright.

**Edit 3.**

> **Before.** The code `a*b` computes $a * b$.

> **After.** The code `a*b` computes $a \times b$.

The asterisk stays in the code.

**Edit 4.** Suppose the draft specifies $b+c$ as the denominator. After proposes a correction to the author.

> **Before.** The ratio is $a/b+c$.

> **After.** The ratio is $\frac{a}{b+c}$.

Changing the grouping requires author review.
