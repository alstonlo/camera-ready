# Flag missing citations and citation keys absent from the references

Flag a technical claim presented as prior knowledge without an identifiable source ("It is well known that"), and any citation key missing from the supplied references. Common knowledge needs no citation, but never delete an existing citation as unnecessary. Preserve secondhand wording such as "as cited in". Follow [vague attribution](../deslopping/vague-attribution.md) for "Studies show". For a specific passage or result cited from a book or long survey, flag a missing page, section, or theorem locator.

## Details

When references are supplied, check that they include every citation key used in the draft. If the bibliography or source texts are not supplied, do not flag citations as unverified on that basis alone. If you suspect that a citation points to the wrong source or version, flag the discrepancy without substituting another reference. Do not audit every bibliographic field or flag uncited entries in a shared bibliography. Preserve secondhand phrasing such as "as cited in", because removing it would imply that the authors read the original source directly.

In every example below, the After line is a correction proposed to the author, not an edit made directly.

## Examples

**Edit 1.** Suppose the draft names ortiz2025 as the source, but the bibliography lacks ortiz2026.

> **Before.** Drying shrinks the shell~\citep{ortiz2026}.

> **After.** Drying shrinks the shell~\citep{ortiz2025}.

**Edit 2.** Say the draft credits the cooling result to chen2024.

> **Before.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay.

> **After.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay~\citep{chen2024}.

The words "as cited in" still matter: they tell readers that the authors learned of Ortiz's result through Patel.

**Edit 3.** If the draft supplies both references and credits the cooling result to chen2024, propose this correction.

> **Before.** A year has twelve months~\citep{calendar2025}. Cooling slows decay.

> **After.** A year has twelve months~\citep{calendar2025}. Cooling slows decay~\citep{chen2024}.

Readers need no source for the number of months in a year, but that alone does not justify removing a citation the author included.
