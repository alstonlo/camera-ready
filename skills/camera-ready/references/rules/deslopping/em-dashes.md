# Delete em dashes

Delete every em dash, including `---` in LaTeX, and every en dash used as a pause. Replace one with a colon or semicolon only if the [pause-punctuation test](pause-punctuation.md) permits it there. Use parentheses only if they do not make an essential qualification look optional, following [stress position](../prose/stress-position.md). Otherwise rewrite the sentence without the pause while preserving its emphasis. Keep compound hyphens and en dashes in numeric ranges or two-person names ("Sections 3–5", "Kullback–Leibler"). For `--` source forms, see the page.

## Details

In LaTeX source, two hyphens (`--`) produce an en dash; judge each pair by its function. Keep it when it encodes a numeric range or a name joining two people, and replace it when it encodes a pause. Keep the single hyphen in a compound.

Changing the punctuation must preserve how the clauses relate. A subordinate clause, reordered condition, or separate sentence may express the relation more clearly than substituting another pause mark. Follow the linked stress-position rule when deciding how much prominence the interrupted material needs.

## Examples

- Bad: The firewall rejects expired credentials—before checking access rules.
- Good: The firewall rejects expired credentials before checking access rules.
