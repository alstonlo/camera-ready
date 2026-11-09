# Number referenced and central displays

Leave intermediate steps unnumbered. See Details.

## Details

A display is mathematics set apart from running text. Central displays include governing equations, the objective, and the main bound.

Keep existing `\label` commands unchanged. Flag any numbering change that requires editing a protected display environment.

## Examples

**Edit 1.** Suppose the draft presents this equation as its central model.

> **Before.** \begin{equation*} h(t)=h(0)+rt. \end{equation*}

> **After.** \begin{equation} h(t)=h(0)+rt. \end{equation}

After is a proposal to the author because the display environment is protected.

**Edit 2.** Imagine that a later passage in the draft refers to this display by its label.

> **Before.** \begin{equation*}\label{eq:sum} s=a+b. \end{equation*}

> **After.** \begin{equation}\label{eq:sum} s=a+b. \end{equation}

Changing the protected display environment requires a proposal to the author.

**Edit 3.** Say this equation serves only as an intermediate step, and the draft never refers to it.

> **Before.** \begin{equation} 2+3=5. \end{equation}

> **After.** \begin{equation*} 2+3=5. \end{equation*}

After shows a proposed change for the author to review because the display environment is protected.
