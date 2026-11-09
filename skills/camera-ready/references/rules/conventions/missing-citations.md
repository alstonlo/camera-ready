# Flag missing citations and citation keys absent from the references

Flag a technical claim presented as prior knowledge without an identifiable source, as in "It is well known that". Also flag any citation key missing from the supplied references. Common knowledge needs no citation. Do not delete an existing citation merely because it seems unnecessary. Preserve secondhand wording such as "as cited in". Follow [vague attribution](../deslopping/vague-attribution.md) for "Studies show" and [reference markers](figure-table-references.md) for "??".

## Details

When references are supplied, check that they include every citation key used in the draft. If the bibliography or source texts are not supplied, do not flag citations as unverified on that basis alone. If you suspect that a citation points to the wrong source or version, flag the discrepancy without substituting another reference. Do not audit every bibliographic field or flag uncited entries in a shared bibliography. Preserve secondhand phrasing such as "as cited in", because removing it would imply that the authors read the original source directly.

In every example below, the Good line is a correction proposed to the author, not an edit made directly.

## Examples

> **Context.** Elsewhere, the draft cites patel2025 for the seed-storage finding. This sentence omits the citation.
>
> **Bad.** Dry storage extends the shelf life of these seeds.
>
> **Good.** Dry storage extends the shelf life of these seeds~\citep{patel2025}.

> **Context.** The draft identifies ortiz2025 as the source, but the sentence cites ortiz2026, which is absent from the bibliography.
>
> **Bad.** Drying shrinks the shell~\citep{ortiz2026}.
>
> **Good.** Drying shrinks the shell~\citep{ortiz2025}.

> **Context.** The draft identifies chen2024 as the source of the cooling result, while Ortiz's result is cited secondhand through Patel.
>
> **Bad.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay.
>
> **Good.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay~\citep{chen2024}.

> **Context.** The draft identifies patel2025 as the source of the seed-storage finding. The first sentence states common knowledge.
>
> **Bad.** A year has twelve months. Dry storage extends these seeds' shelf life.
>
> **Good.** A year has twelve months. Dry storage extends these seeds' shelf life~\citep{patel2025}.

> **Context.** The draft supplies both references and identifies chen2024 as the source of the cooling result. The first sentence states common knowledge and already includes a citation.
>
> **Bad.** A year has twelve months~\citep{calendar2025}. Cooling slows decay.
>
> **Good.** A year has twelve months~\citep{calendar2025}. Cooling slows decay~\citep{chen2024}.
