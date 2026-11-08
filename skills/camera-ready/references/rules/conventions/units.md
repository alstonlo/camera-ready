# Give units, separated from numbers by a non-breaking space

Give units for measurements and axes, with a non-breaking space between number and unit. If "Mb" could mean bits or bytes, expand the unit from the draft or flag the ambiguity. For ambiguous binary or decimal prefixes and time representations, see the page; never normalize them by changing a value.

## Details

In LaTeX, use a non-breaking space, as in `40~ms`. A measurement and its unit should stay together across a line break.

Keep bit and byte quantities distinct. When a capacity prefix could denote either a decimal or binary scale, use the scale the draft states or flag the missing definition. Do not silently change the number to fit a preferred prefix.

A decimal duration and a clock-style duration can denote different lengths of time. Use the draft's stated convention to resolve notation that admits both readings; otherwise flag it. This check does not call for converting every time measurement to a single representation.

## Examples

- Bad: We stir the solution for 30s.
- Good: We stir the solution for 30~s.
