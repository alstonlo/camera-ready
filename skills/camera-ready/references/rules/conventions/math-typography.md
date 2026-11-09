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

> **Context.** The draft defines $x$ as a positive concentration ratio and $\log$ as the logarithm.
>
> **Bad.** We evaluate $log(x)$.
>
> **Good.** We evaluate $\log(x)$.

> **Context.** The draft defines $i$ as a sample index and "cool" as the label for cooling time.
>
> **Bad.** We compare $t_i$ with $t_{cool}$.
>
> **Good.** We compare $t_i$ with $t_{\text{cool}}$.

> **Bad.** The area is $3 * 4=12$.
>
> **Good.** The area is $3 \times 4=12$.

> **Bad.** The yield is 3x the baseline yield.
>
> **Good.** The yield is 3× the baseline yield.

> **Bad.** The reading is -5.
>
> **Good.** The reading is −5.

> **Bad.** The code `a*b` computes $a * b$.
>
> **Good.** The code `a*b` computes $a \times b$.

> **Context.** The draft states that the denominator is $b+c$. The Good line suggests a clearer fraction to the author.
>
> **Bad.** The ratio is $a/b+c$.
>
> **Good.** The ratio is $\frac{a}{b+c}$.

> **Context.** The draft specifies an exponent of one half. The Good line suggests a form that is easier to read.
>
> **Bad.** The factor is $e^{\frac{1}{2}}$.
>
> **Good.** The factor is $e^{1/2}$.

> **Context.** The draft encloses the entire sum in parentheses. The Good line suggests smaller delimiters to the author.
>
> **Bad.** The total is $\left(\frac{a}{b}+c\right)$.
>
> **Good.** The total is $(\frac{a}{b}+c)$.
