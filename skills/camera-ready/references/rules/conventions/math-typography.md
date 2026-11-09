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

**Example 1.** The draft defines $x$ as a positive concentration ratio and $\log$ as the logarithm.

> **Bad.** We evaluate $log(x)$.
>
> **Good.** We evaluate $\log(x)$.

**Example 2.** The draft defines $i$ as a sample index and "cool" as the label for cooling time.

> **Bad.** We compare $t_i$ with $t_{cool}$.
>
> **Good.** We compare $t_i$ with $t_{\text{cool}}$.

**Example 3.**

> **Bad.** The code `a*b` computes $a * b$.
>
> **Good.** The code `a*b` computes $a \times b$.

**Example 4.** The draft states that the denominator is $b+c$. The Good line suggests a clearer fraction to the author.

> **Bad.** The ratio is $a/b+c$.
>
> **Good.** The ratio is $\frac{a}{b+c}$.
