# Define each symbol by its first use and give it one meaning

Define symbols, at least informally, at or before first use and [refresh them after gaps](refresh-shorthand.md). Keep one meaning per symbol and one symbol per object. Flag conflicting meanings, unused definitions, confusable names, or dense notation; do not rename symbols. Distinguish a function from its value: if L is a loss function, flag "L = 0.31" where "L(θ_T) = 0.31" is intended. Keep local definitions near use. If global definitions are scattered, move them into an existing notation section only when the request [allows relocation](../cutting/idea-level.md); otherwise flag them. Never create that section. For unnecessary indices, repeated expressions, and verbal alternatives, see the page.

## Details

Define an object's meaning before relying on its symbol. Shared preliminaries can introduce global notation used in several sections, but centralizing every local definition makes readers look away from the passage where they need it. Check later equations, captions, figures, and appendices before flagging a definition as unused.

Flag notation whose distinctions depend on marks that are difficult to tell apart, or whose chosen letters conflict with established meanings elsewhere in the paper. A proposed repair should identify the collision without silently renaming mathematical objects.

Prose may be clearer where indices or named variables add no useful distinction. A repeated complex expression may benefit from a short name, and notation for a whole vector or collection may make its structure easier to see. Suggest these changes to the author; do not rewrite equations as part of a prose edit.

## Examples

- Bad: We compare $h$ across plants. The symbol $h$ denotes plant height.
- Good: The symbol $h$ denotes plant height. We compare $h$ across plants.
