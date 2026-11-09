# Number referenced and central displays

Number every display that the text refers to and every central display; leave intermediate steps unnumbered. See Details.

## Details

A display is mathematics set apart from running text. Central displays include governing equations, the objective, and the main bound.

Keep existing `\label` commands unchanged. Flag any numbering change that requires editing a protected display environment.

## Examples

**Edit 1.** The draft identifies this equation as its central model. The edit, a proposal to the author, changes the "equation*" environment to "equation" so that the central model receives a number. The change must be flagged because the display environment is protected.

> **Before.** \begin{equation*} h(t)=h(0)+rt. \end{equation*}
>
> **After.** \begin{equation} h(t)=h(0)+rt. \end{equation}

**Edit 2.** The draft later refers to this display by its label. The edit, a proposal to the author, changes the "equation*" environment to "equation" while keeping the existing label, so that the referenced display receives a number. The change must be flagged because the display environment is protected.

> **Before.** \begin{equation*}\label{eq:sum} s=a+b. \end{equation*}
>
> **After.** \begin{equation}\label{eq:sum} s=a+b. \end{equation}

**Edit 3.** The draft uses this equation only as an intermediate step and never refers to it. The edit, a proposal to the author, changes the "equation" environment to "equation*" so that this unreferenced intermediate step has no number. The change must be flagged because the display environment is protected.

> **Before.** \begin{equation} 2+3=5. \end{equation}
>
> **After.** \begin{equation*} 2+3=5. \end{equation*}
