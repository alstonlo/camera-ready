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

**Edit 1.** The operation is described in the draft as taking a logarithm.

> **Before.** We evaluate $log(x)$.
>
> **After.** We evaluate $\log(x)$.

**Edit 2.** Samples are indexed by $i$ in the draft, and "cool" is defined as a word label for cooling time.

> **Before.** We compare $t_i$ with $t_{cool}$.
>
> **After.** We compare $t_i$ with $t_{\text{cool}}$.

**Edit 3.**

> **Before.** The code `a*b` computes $a * b$.
>
> **After.** The code `a*b` computes $a \times b$.

**Edit 4.** The denominator is $b+c$, as specified in the draft. After is a proposal to the author.

> **Before.** The ratio is $a/b+c$.
>
> **After.** The ratio is $\frac{a}{b+c}$.
