# Flag missing citations and citation keys absent from the references

Flag a technical claim presented as prior knowledge without an identifiable source, as in "It is well known that". Also flag any citation key missing from the supplied references. Common knowledge needs no citation. Do not delete an existing citation merely because it seems unnecessary. Preserve secondhand wording such as "as cited in". Follow [vague attribution](../deslopping/vague-attribution.md) for "Studies show" and [reference markers](figure-table-references.md) for "??".

## Details

When references are supplied, check that they include every citation key used in the draft. If the bibliography or source texts are not supplied, do not flag citations as unverified on that basis alone. If you suspect that a citation points to the wrong source or version, flag the discrepancy without substituting another reference. Do not audit every bibliographic field or flag uncited entries in a shared bibliography. Preserve secondhand phrasing such as "as cited in", because removing it would imply that the authors read the original source directly.

In every example below, the After line is a correction proposed to the author, not an edit made directly.

## Examples

**Edit 1.** The draft identifies ortiz2025 as the source; ortiz2026 is absent from the bibliography. The edit, a proposal to the author, replaces the missing key "ortiz2026" with the draft-supported key "ortiz2025", so that the citation identifies the stated source.

> **Before.** Drying shrinks the shell~\citep{ortiz2026}.
>
> **After.** Drying shrinks the shell~\citep{ortiz2025}.

**Edit 2.** The draft identifies chen2024 as the source of the cooling result. The edit, a proposal to the author, adds "~\citep{chen2024}" to that result to identify its source and keeps "as cited in" in the preceding sentence because removing it would imply that the authors read Ortiz directly.

> **Before.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay.
>
> **After.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay~\citep{chen2024}.

**Edit 3.** The draft supplies both references and identifies chen2024 as the source of the cooling result. The edit, a proposal to the author, adds "~\citep{chen2024}" to identify that source and keeps the calendar citation because common knowledge is not a reason to delete an existing citation.

> **Before.** A year has twelve months~\citep{calendar2025}. Cooling slows decay.
>
> **After.** A year has twelve months~\citep{calendar2025}. Cooling slows decay~\citep{chen2024}.
