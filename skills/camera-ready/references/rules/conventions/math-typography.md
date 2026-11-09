# Use the correct type for operators, subscripts, and signs

Use upright type for multi-letter operators and word subscripts, but keep variable subscripts in italic type. Use × for multiplication and multiplicative factors ("3× the yield"), and use minus signs for negative values. Fix LaTeX typography when mathematical meaning stays unchanged. Flag, rather than make, any change to symbols, grouping, delimiters, or operator meaning, and preserve code syntax. See Details for LaTeX commands and ambiguous notation.

## Details

In LaTeX, use these commands and settings:

- Use `\log` or `\operatorname{...}` for operators with several letters.
- Use `\text{...}` for subscripts that are words.
- Use `\times`, not x or `*`, for multiplication.
- Write negative values in math mode to get minus signs.

Check for these problems, and propose a clearer form only when the draft establishes the intended meaning:

- A slash fraction leaves readers unsure where the denominator ends.
- A stacked fraction in an exponent is too small to read.
- Automatically sized delimiters obscure grouping.

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
