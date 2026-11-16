# Flag missing citations and citation keys absent from the references

Flag technical claims presented as prior knowledge without an identifiable source, and citation keys missing from the supplied references. Common knowledge needs no citation, but never delete an existing citation as unnecessary. Preserve secondhand wording such as "as cited in". Follow [vague attribution](../slop/vague-attribution.md) for "Studies show". For a specific passage or result cited from a book or long survey, flag a missing page, section, or theorem locator.

## Details

- Reference checks: When references are supplied, check that they include every citation key used in the draft. Do not flag citations as unverified solely because the bibliography or source texts are absent. Do not audit every bibliographic field or flag uncited entries in a shared bibliography.
- Suspected mismatches: Flag a citation that appears to point to the wrong source or version without substituting another reference.
- Secondhand sources: Keep wording such as "as cited in"; removing it would imply that the authors read the original source directly.

Each example proposes a correction to the author.

## Examples

**Edit 1.** Suppose the draft names ortiz2025 as the source, but the bibliography lacks ortiz2026. The editor flags the citation and proposes the edited text to the author.

> **Before.** Drying shrinks the shell~\citep{ortiz2026}.

> **After.** Drying shrinks the shell~\citep{ortiz2025}.

**Edit 2.** Say the draft credits the cooling result to chen2024.

> **Before.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay.

> **After.** Ortiz, as cited in Patel, reports that dry storage extends shelf life. Cooling slows decay~\citep{chen2024}.

The words "as cited in" preserve the secondhand attribution.

**Edit 3.** Suppose the draft supplies both references and credits the cooling result to chen2024.

> **Before.** A year has twelve months~\citep{calendar2025}. Cooling slows decay.

> **After.** A year has twelve months~\citep{calendar2025}. Cooling slows decay~\citep{chen2024}.

Common knowledge alone does not justify removing an existing citation.
