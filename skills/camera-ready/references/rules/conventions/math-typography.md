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

**Edit 1.** The draft defines the operation as a logarithm. The edit replaces "log" with "\log" so that LaTeX typesets the logarithm as an upright operator rather than italic variables.

> **Before.** We evaluate $log(x)$.
>
> **After.** We evaluate $\log(x)$.

**Edit 2.** The draft defines $i$ as a sample index and "cool" as a label for cooling time. The edit puts "cool" inside "\text{...}" to make the word label upright while leaving the variable index $i$ italic.

> **Before.** We compare $t_i$ with $t_{cool}$.
>
> **After.** We compare $t_i$ with $t_{\text{cool}}$.

**Edit 3.** The edit replaces the asterisk in "$a * b$" with "\times" so that mathematical multiplication uses the multiplication sign, while preserving the code syntax "a*b".

> **Before.** The code `a*b` computes $a * b$.
>
> **After.** The code `a*b` computes $a \times b$.

**Edit 4.** The draft defines the denominator as $b+c$. The edit, a proposal to the author, replaces "$a/b+c$" with "$\frac{a}{b+c}$" to put both terms in the denominator. This requires the author's review because grouping the terms changes the mathematical meaning, not just the type.

> **Before.** The ratio is $a/b+c$.
>
> **After.** The ratio is $\frac{a}{b+c}$.
