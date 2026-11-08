# Flag missing or unresolvable citations

Flag a technical claim presented as prior knowledge ("It is well known that") without an identifiable source, or a citation key missing from the supplied references. Common knowledge needs no citation, and you should not delete an existing citation merely because it seems unnecessary. Preserve explicit secondhand wording such as "as cited in" rather than implying that the authors consulted the original source directly. Follow [vague attribution](../deslopping/vague-attribution.md) for "Studies show" and [reference markers](figure-table-references.md) for "??".

## Details

When references are supplied, check that every cited key appears in them; if the bibliography or source texts are not supplied, do not flag citations as unverified on that basis alone. Flag a suspected mismatch in a citation's source or version without substituting another reference. Do not audit every bibliographic field or flag uncited entries in a shared bibliography.

## Examples

Elsewhere, the draft credits the seed-storage finding to patel2025, but this sentence omits the citation; the Good line proposes adding it for the author.

> Bad: Dry storage extends the shelf life of these seeds.
>
> Good: Dry storage extends the shelf life of these seeds~\citep{patel2025}.

The draft identifies ortiz2025 as the source, and its bibliography has no ortiz2026 entry; the Good line proposes correcting the key for the author.

> Bad: Drying shrinks the shell~\citep{ortiz2026}.
>
> Good: Drying shrinks the shell~\citep{ortiz2025}.

The draft credits the cooling result to chen2024 and cites Ortiz secondhand through Patel; the Good line proposes adding the missing citation for the author.

> Bad: Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay.
>
> Good: Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay~\citep{chen2024}.

The draft credits the seed-storage finding to patel2025; the Good line proposes adding that citation without citing common knowledge.

> Bad: A year has twelve months. Dry storage extends these seeds' shelf life.
>
> Good: A year has twelve months. Dry storage extends these seeds' shelf life~\citep{patel2025}.

The draft provides both references and credits the cooling result to chen2024; the Good line proposes adding chen2024 while keeping the existing citation.

> Bad: A year has twelve months~\citep{calendar2025}. Cooling slows decay.
>
> Good: A year has twelve months~\citep{calendar2025}. Cooling slows decay~\citep{chen2024}.
