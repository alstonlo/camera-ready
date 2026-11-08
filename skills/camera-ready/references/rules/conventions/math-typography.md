# Set operators, subscripts, and signs in the correct type

Set multi-letter operators and word subscripts upright, while keeping variable subscripts italic. Use × for multiplication and multiplicative factors ("3× the yield"), not x or *, and use a minus sign for negative values. Fix LaTeX typography when the mathematical meaning stays unchanged. Flag, rather than make, changes to symbols, grouping, delimiters, or operator meaning, and preserve code syntax. For ambiguous slash fractions, tiny exponent fractions, oversized delimiters, and LaTeX commands, see the page.

## Details

In LaTeX, use `\log` or `\operatorname{...}` for multi-letter operators, `\text{...}` for word subscripts, `\times` for multiplication, and math mode for minus signs.

Check whether a slash fraction leaves the extent of the denominator unclear, a stacked fraction in an exponent typesets too small to read, or automatic delimiters obscure grouping. Propose a clearer form only when the draft establishes the intended meaning.

## Examples

The draft defines $x$ as a positive concentration ratio and $\log$ as the logarithm.

> **Bad.** We evaluate $log(x)$.
>
> **Good.** We evaluate $\log(x)$.

The draft defines $i$ as a sample index and "cool" as the label for cooling time.

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

The draft states that the denominator is $b+c$; the Good line proposes a clearer fraction to the author.

> **Bad.** The ratio is $a/b+c$.
>
> **Good.** The ratio is $\frac{a}{b+c}$.

The draft specifies an exponent of one half; the Good line proposes a more legible form to the author.

> **Bad.** The factor is $e^{\frac{1}{2}}$.
>
> **Good.** The factor is $e^{1/2}$.

The draft encloses the whole sum in parentheses; the Good line proposes smaller delimiters to the author.

> **Bad.** The total is $\left(\frac{a}{b}+c\right)$.
>
> **Good.** The total is $(\frac{a}{b}+c)$.
