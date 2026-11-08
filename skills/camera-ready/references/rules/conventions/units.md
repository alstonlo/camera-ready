# Give units, separated from numbers by a non-breaking space

Give units for all measurements and axes, separated from the number by a non-breaking space. When a unit or its basis is ambiguous ("ppm" by mass or by volume; "Mb" as megabits or megabytes), state the intended unit and basis from the draft, or flag the ambiguity. For ambiguous binary or decimal prefixes and time formats, see the page; never change a value to normalize units.

## Details

In LaTeX, tie the number to its unit with a non-breaking space (`40~ms`).

When a capacity prefix could be binary or decimal, clarify the scale from the draft or flag that it is unstated. Likewise, use the draft's convention to distinguish decimal durations from clock-style durations ("1.30" as 1 min 30 s), or flag the ambiguity. Neither check authorizes converting numerical values.

## Examples

> **Bad.** We stir the solution for 30s.
>
> **Good.** We stir the solution for 30~s.

The draft states that this length is measured in centimeters.

> **Bad.** The rod is 15 long.
>
> **Good.** The rod is 15~cm long.

The draft states that the plotted time axis is in seconds.

> **Bad.** Time
>
> **Good.** Time (s)

The draft defines this concentration on a mass basis.

> **Bad.** The concentration is 6 ppm.
>
> **Good.** The concentration is 6 ppm by mass.

The draft states that these sizes are measured in megabytes.

> **Bad.** Each file is 8 Mb.
>
> **Good.** Each file is 8 megabytes.

The draft defines one capacity unit as 1,048,576 bytes, so the unit is a mebibyte and the value remains 2.

> **Bad.** The capacity is 2 MB.
>
> **Good.** The capacity is 2 MiB.

The draft states that the period separates minutes from seconds rather than marking a decimal point.

> **Bad.** The duration is 1.30.
>
> **Good.** The duration is 1 min 30 s.
