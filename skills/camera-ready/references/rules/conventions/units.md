# Give units and separate them from numbers with a non-breaking space

Give units for every measurement and axis, separated from numbers by a non-breaking space. If a unit or its basis is ambiguous ("ppm" by mass or volume; "Mb" as megabits or megabytes), state the intended meaning from the draft or flag the ambiguity. For binary prefixes and durations, see Details. Never change a value to normalize units.

## Details

In LaTeX, use a tilde to insert a non-breaking space between the number and its unit, as in `40~ms`.

For storage capacity, a prefix may be binary (powers of two) or decimal (powers of ten). If the draft leaves the scale unclear, state the scale from elsewhere in the draft or flag that it is unstated.

For durations, use the draft's convention to distinguish a decimal number from a clock reading, such as "1.30" for 1 min 30 s. If the draft leaves the format ambiguous, flag it. Neither check permits converting a numerical value.

## Examples

> **Bad.** We stir the solution for 30s.
>
> **Good.** We stir the solution for 30~s.

> **Context.** The draft gives the rod's length in centimeters.
>
> **Bad.** The rod is 15 long.
>
> **Good.** The rod is 15~cm long.

> **Context.** The draft states that the plotted time axis is in seconds.
>
> **Bad.** Time
>
> **Good.** Time (s)

> **Context.** The draft defines the concentration as parts per million by mass.
>
> **Bad.** The concentration is 6 ppm.
>
> **Good.** The concentration is 6 ppm by mass.

> **Context.** The draft gives file sizes in megabytes.
>
> **Bad.** Each file is 8 Mb.
>
> **Good.** Each file is 8 megabytes.

> **Context.** The draft defines its capacity unit as 1,048,576 bytes, which is one mebibyte (MiB), so the value stays 2 and only the unit symbol changes.
>
> **Bad.** The capacity is 2 MB.
>
> **Good.** The capacity is 2 MiB.

> **Context.** The draft states that the period separates minutes from seconds rather than marking a decimal point.
>
> **Bad.** The duration is 1.30.
>
> **Good.** The duration is 1 min 30 s.
