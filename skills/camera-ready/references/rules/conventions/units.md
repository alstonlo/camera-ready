# Give units and separate them from numbers with a non-breaking space

Give units for every measurement and axis, separated from numbers by a non-breaking space. If a unit or its basis is ambiguous ("ppm" by mass or volume; "Mb" as megabits or megabytes), state the intended meaning from the draft or flag the ambiguity. For binary prefixes and durations, see Details. Never change a value to normalize units.

## Details

In LaTeX, use a tilde to insert a non-breaking space between the number and its unit, as in `40~ms`.

For storage capacity, a prefix may be binary (powers of two) or decimal (powers of ten). If the draft leaves the scale unclear, state the scale from elsewhere in the draft or flag that it is unstated.

For durations, use the draft's convention to distinguish a decimal number from a clock reading, such as "1.30" for 1 min 30 s. If the draft leaves the format ambiguous, flag it. Neither check permits converting a numerical value.

## Examples

**Edit 1.**

> **Before.** We stir the solution for 30s.
>
> **After.** We stir the solution for 30~s.

**Edit 2.** The ratio specified in the draft is by mass.

> **Before.** The concentration is 6 ppm.
>
> **After.** The concentration is 6 ppm by mass.

**Edit 3.** In the draft, one capacity unit is defined as 1,048,576 bytes.

> **Before.** The capacity is 2 MB.
>
> **After.** The capacity is 2 MiB.

**Edit 4.** A period separates minutes from seconds in the draft.

> **Before.** The duration is 1.30.
>
> **After.** The duration is 1 min 30 s.
