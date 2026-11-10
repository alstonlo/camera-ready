# Use the correct type for operators, subscripts, and signs

Use upright type for multi-letter operators (`\log`, `\operatorname{softmax}`) and word subscripts (`\mathcal{L}_{\text{train}}`), but italic for variable subscripts (`x_i`). Use × (`\times`), not x or `*` (except in code), for multiplication and multiplicative factors, and write negative values in math mode for minus signs (`$-0.3$`), not hyphens. Fix LaTeX typography only where mathematical meaning stays unchanged, and flag any change to symbols, grouping, delimiters, or operator meaning. Propose a clearer form for ambiguous notation, such as a slash fraction whose denominator has no clear end, only when the draft establishes the intended meaning.

Flag stacked inline fractions that disrupt line spacing, exponent fractions too small to read, and oversized delimiters; suggest slash fractions or smaller delimiters only with grouping preserved.

## Details

A slash fraction can leave readers unsure where the denominator ends.

## Examples

**Edit 1.** Suppose the draft describes this operation as taking a logarithm.

> **Before.** We evaluate $log(x)$.

> **After.** We evaluate $\log(x)$.

**Edit 2.** Say the draft indexes samples by $i$ and defines "cool" as a word label for cooling time.

> **Before.** We compare $t_i$ with $t_{cool}$.

> **After.** We compare $t_i$ with $t_{\text{cool}}$.

The index $i$ stays italic because it is a variable, whereas "cool" is a word label.

**Edit 3.**

> **Before.** The code `a*b` computes $a * b$.

> **After.** The code `a*b` computes $a \times b$.

The asterisk in `a*b` belongs to the code, so it stays as written.

**Edit 4.** Suppose the draft specifies $b+c$ as the denominator. After proposes a correction to the author.

> **Before.** The ratio is $a/b+c$.

> **After.** The ratio is $\frac{a}{b+c}$.

Putting both terms in the denominator changes the grouping, so the author needs to review it.
