# Set operators, subscripts, and signs in the correct type

Set multi-letter operators and word subscripts upright; variable subscripts stay italic. Use × for multiplication and speedup factors, not x or *, and use a minus sign for negative values. Fix LaTeX typography when the mathematical content stays unchanged. Flag, rather than make, changes to symbols, grouping, delimiters, or operator meaning; preserve code syntax. For ambiguous slash fractions, tiny exponent fractions, oversized delimiters, and LaTeX commands, see the page.

## Details

Use established operator commands such as `\log`, or `\operatorname{...}` for a named operator. Set a word subscript with `\text{...}` while keeping an index variable italic. These changes set the same operator or label in the correct type; they do not rename it or change a logarithm's base.

In LaTeX, use `\times` for multiplication and a math-mode minus for a negative value. Code may deliberately use `*` for multiplication or brackets for array access. Do not apply prose mathematics conventions to that syntax.

A slash fraction can leave its denominator's extent unclear. A stacked fraction in an exponent may be too small to read, and automatic delimiter sizing may obscure the surrounding structure. Flag a proposed regrouping or delimiter change when it could affect meaning. Give a clarified mathematical form only when the draft establishes that form's interpretation.

## Examples

- Bad: The cooling time is $t_{cool}$.
- Good: The cooling time is $t_{\text{cool}}$.
