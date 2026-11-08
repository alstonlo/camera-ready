# Number referenced and central displays

Number every display referred to in the text and every central display, such as a governing equation, the objective, or the main bound. Leave intermediate steps unnumbered.

## Details

Keep existing `\label` commands unchanged. Flag any numbering change that requires modifying a protected display environment.

## Examples

The draft identifies this equation as its central model of the water level, with height $h$, time $t$, and constant rate of rise $r$; the Good line proposes numbering the display for the author.

> **Bad.** \begin{equation*} h(t)=h(0)+rt. \end{equation*}
>
> **Good.** \begin{equation} h(t)=h(0)+rt. \end{equation}

The draft defines these symbols and later refers to this display by its label; the Good line proposes numbering the display for the author.

> **Bad.** \begin{equation*}\label{eq:sum} s=a+b. \end{equation*}
>
> **Good.** \begin{equation}\label{eq:sum} s=a+b. \end{equation}

The draft uses this equation only as an intermediate step and never refers to it; the Good line proposes removing the number for the author.

> **Bad.** \begin{equation} 2+3=5. \end{equation}
>
> **Good.** \begin{equation*} 2+3=5. \end{equation*}
