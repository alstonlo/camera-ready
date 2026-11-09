# Number referenced and central displays

Number every display that the text refers to and every central display; leave intermediate steps unnumbered. See Details.

## Details

A display is mathematics set apart from running text. Central displays include governing equations, the objective, and the main bound.

Keep existing `\label` commands unchanged. Flag any numbering change that requires editing a protected display environment.

## Examples

**Edit 1.** This equation is presented as the draft's central model.

> **Before.** \begin{equation*} h(t)=h(0)+rt. \end{equation*}
>
> **After.** \begin{equation} h(t)=h(0)+rt. \end{equation}

**Edit 2.** A later passage in the draft refers to this display by its label.

> **Before.** \begin{equation*}\label{eq:sum} s=a+b. \end{equation*}
>
> **After.** \begin{equation}\label{eq:sum} s=a+b. \end{equation}

**Edit 3.** This equation serves only as an intermediate step, and the draft never refers to it.

> **Before.** \begin{equation} 2+3=5. \end{equation}
>
> **After.** \begin{equation*} 2+3=5. \end{equation*}
