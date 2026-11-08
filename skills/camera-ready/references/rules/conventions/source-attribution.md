# Flag missing or unresolvable citations

Flag a technical claim presented as prior knowledge ("It is well known that") without an identifiable source, or a citation key missing from supplied references. Common knowledge needs no added citation; do not delete an existing citation because it seems unnecessary. Preserve explicit secondhand wording such as "as cited in" rather than implying direct consultation. Follow [vague attribution](../deslopping/vague-attribution.md) for "Studies show" and [reference markers](float-refs.md) for "??".

## Details

Name the particular claim or citation key that needs support. The number of citations in a passage does not establish whether a particular claim has a source. Check a key against a supplied bibliography, but do not flag source verification as failed merely because the source text or bibliography was not supplied.

Keep an explicitly stated chain of attribution: reporting what one work says about another is not the same as reporting direct consultation of the original. A shorter sentence must not erase that distinction. Flag a suspected mismatch rather than substituting a different reference or publication version.

Do not audit every bibliographic field or flag unused entries in a shared bibliography database. A missing entry for a used key is a concrete defect; an entry unused by this paper may serve another document.

## Examples

The draft credits the finding about seed storage to the study with bibliography key patel2025, but this passage omits its citation; the Good line is the revision proposed to the author.

- Bad: Dry storage extends the shelf life of these seeds.
- Good: Dry storage extends the shelf life of these seeds~\citep{patel2025}.
