# Number referenced and central displays

Number every display that the text refers to and every central display; leave intermediate steps unnumbered. See Details.

## Details

A display is mathematics set apart from running text. Central displays include governing equations, the objective, and the main bound.

Keep existing `\label` commands unchanged. Flag any numbering change that requires editing a protected display environment.

## Examples

**Example 1.** The draft identifies this equation as its central model of water height $h$ at time $t$, with constant rate of rise $r$. The Good line suggests numbering the display for the author.

> **Bad.** \begin{equation*} h(t)=h(0)+rt. \end{equation*}
>
> **Good.** \begin{equation} h(t)=h(0)+rt. \end{equation}

**Example 2.** The draft defines the symbols and later refers to this display by its label. The Good line suggests numbering the display for the author.

> **Bad.** \begin{equation*}\label{eq:sum} s=a+b. \end{equation*}
>
> **Good.** \begin{equation}\label{eq:sum} s=a+b. \end{equation}

**Example 3.** The draft uses this equation only as an intermediate step and never refers to it. The Good line suggests removing the number for the author.

> **Bad.** \begin{equation} 2+3=5. \end{equation}
>
> **Good.** \begin{equation*} 2+3=5. \end{equation*}
