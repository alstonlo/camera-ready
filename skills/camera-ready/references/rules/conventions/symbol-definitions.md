# Define each symbol by its first use and give it one meaning

Define every symbol, at least informally, at or before its first use, and [refresh the definition after a gap](shorthand-reminders.md). Give each symbol one meaning and each object one symbol. Flag conflicting meanings, unused definitions, easily confused symbols, dense notation, and functions equated with values; do not rename symbols yourself. Keep local definitions near the passages that use them. When definitions of symbols used throughout the paper are scattered, move them into an existing notation section only if the request [allows relocation](../cutting/idea-cuts.md); otherwise, flag them. Never create a new notation section. See Details for notation improvements and distinguishing functions from values.

## Details

Check later equations, captions, figures, and appendices before flagging a symbol definition as unused.

Distinguish a function from its value. For example, if $V$ is a potential function, flag "$V = 0.31$" when the draft means "$V(x_0) = 0.31$".

Suggest notation changes to the author rather than rewriting equations yourself:

- Suggest words in place of an indexed symbol when the index does not distinguish one quantity from another.
- Suggest a short name for a complex expression that appears repeatedly.
- Suggest grouping quantities in a vector, set, or other collection when grouping clarifies their structure.

## Examples

> **Bad.** We compare $h$ across plants. The symbol $h$ denotes plant height.
>
> **Good.** The symbol $h$ denotes plant height. We compare $h$ across plants.

> **Context.** The draft defines $V$ as a potential function and gives its value at $x_0$ as 0.4. The Good line shows the correction suggested to the author.
>
> **Bad.** The potential is $V=0.4$.
>
> **Good.** The potential is $V(x_0)=0.4$.

> **Context.** The draft defines both quantities, using $m$ twice here but using $w$ for moisture content in its tables. The Good line shows the correction suggested to the author.
>
> **Bad.** Let $m$ denote mass and $m$ denote moisture content.
>
> **Good.** Let $m$ denote mass and $w$ denote moisture content.

> **Context.** The draft uses two different symbols, $h$ and $z$, for the same height. The Good line suggests that the author use $h$ consistently.
>
> **Bad.** Let $h$ denote height. We report the height $z$.
>
> **Good.** Let $h$ denote height. We report the height $h$.

> **Context.** In the draft's font, lowercase $l$ looks identical to uppercase $I$, while a table already uses $L$ for length. The Good line suggests that the author replace $l$ with $L$.
>
> **Bad.** Let $l$ denote length and $I$ denote current.
>
> **Good.** Let $L$ denote length and $I$ denote current.

> **Context.** The draft defines $w$ as width but never uses $w$ in the text, captions, figures, or appendices. The Good line suggests that the author remove the unused definition.
>
> **Bad.** Let $h$ denote height and $w$ denote width. We report $h$.
>
> **Good.** Let $h$ denote height. We report $h$.

> **Context.** The draft introduces $h$ two sentences before using it.
>
> **Bad.** Let $h$ denote height. We prepare the soil and label the pots. We measure $h$.
>
> **Good.** We prepare the soil and label the pots. Let $h$ denote height. We measure $h$.

> **Context.** The draft uses both symbols throughout the paper and has an existing Notation section, but the request does not authorize moving content between sections. The Good line suggests moving the scattered definition for the author.
>
> **Bad.** Notation: Let $h$ denote height. Methods: Let $w$ denote width.
>
> **Good.** Notation: Let $h$ denote height. Let $w$ denote width. Methods:

> **Context.** The draft defines only one temperature, $T_1$, and never uses the subscript to distinguish different readings. The Good line suggests that the author replace the indexed symbol with the word "temperature".
>
> **Bad.** We record $T_1$.
>
> **Good.** We record the temperature.

> **Context.** The draft defines $a$, $b$, $c$, and $d$, and then repeats their ratio. The Good line suggests that the author name the ratio $R$.
>
> **Bad.** We compare $(a+b)/(c+d)$ across sites and plot $(a+b)/(c+d)$ over time.
>
> **Good.** Let $R=(a+b)/(c+d)$. We compare $R$ across sites and plot $R$ over time.

> **Context.** The draft treats three coordinates as a single position vector. The Good line suggests that the author define a vector symbol.
>
> **Bad.** We report $(x_1,x_2,x_3)$ and compare $(x_1,x_2,x_3)$ across trials.
>
> **Good.** Let $\mathbf{x}=(x_1,x_2,x_3)$. We report $\mathbf{x}$ and compare $\mathbf{x}$ across trials.
