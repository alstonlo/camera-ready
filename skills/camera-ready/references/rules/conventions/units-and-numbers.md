# State units clearly and never change a number's value or precision

Give every measurement and axis its unit, separated from the number by a non-breaking space (`0.3~s`). Preserve established number formats. Match forms within a comparison only when value and precision stay unchanged. Use the draft to resolve ambiguous unit meanings, measurement bases, binary or decimal prefixes, and duration formats, or flag the ambiguity. Flag, rather than perform, any unit conversion.

## Details

- Storage prefixes: A prefix may be binary (powers of two) or decimal (powers of ten). If its scale is unclear, state it from elsewhere in the draft or flag it as unstated.
- Durations: Use the draft's convention to distinguish a decimal number from a clock reading, such as "1.30" for 1 min 30 s. Flag any ambiguity the draft leaves unresolved. Neither check permits converting a numerical value.
- Percentages and percentage-point differences: Follow [variability](../claims/variability.md).

## Examples

**Edit 1.**

> **Before.** We stir the solution for 30s.

> **After.** We stir the solution for 30~s.

**Edit 2.** Suppose the draft specifies a ratio by mass.

> **Before.** The concentration is 6 ppm.

> **After.** The concentration is 6 ppm by mass.

**Edit 3.** Say the draft defines one capacity unit as 1,048,576 bytes.

> **Before.** The capacity is 2 MB.

> **After.** The capacity is 2 MiB.

The label correction preserves the capacity.

**Edit 4.** Imagine the draft uses a period to separate minutes from seconds.

> **Before.** The duration is 1.30.

> **After.** The duration is 1 min 30 s.

**Edit 5.** Suppose an editor removed the trailing zero from a measurement reported to two decimal places.

> **Before.** The probe reads 1.2 mV.

> **After.** The probe reads 1.20 mV.

After restores the draft's precision and established format.

**Edit 6.** Suppose an editor converted the draft's temperature to degrees Celsius while normalizing number forms.

> **Before.** The chamber remains at 20 °C.

> **After.** The chamber remains at 293.15 K.

After restores the original value and units; the proposed conversion requires author review.

**Edit 7.** Suppose the draft uses M for exact counts in millions in this comparison.

> **Before.** The sample counts are 3.2M and 400,000.

> **After.** The sample counts are 3.2M and 0.4M.

The matching forms preserve both exact counts without rounding.

**Edit 8.** Suppose an editor rounded the second count to match the first count's form.

> **Before.** The sample counts are 3.2M and 0.4M.

> **After.** The sample counts are 3.2M and 412,678.

After restores the exact count; the proposed rounding requires author review.
