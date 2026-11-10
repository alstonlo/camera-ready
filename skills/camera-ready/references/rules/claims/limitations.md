# State limitations precisely and explain their effects

State each limitation in full and without apology where it first affects a method or inference. Beside each limitation, keep the draft's explanation of how it affects the results ("results may not transfer to larger models, since every run uses the same 100M-parameter backbone") and which conclusions still hold, or flag the missing explanation. Flag unexplained unexpected results, unjustified data exclusions, and decoy limitations: a minor weakness named while a larger one documented elsewhere in the draft goes unmentioned. A limitation phrased as future work must still state what the current results do not cover. Keep brief reminders that limit later claims; move a limitation, or delete a repeated full statement of it, only as the [relocation rules](../cutting/idea-cuts.md) and the [triage order](../cutting/triage-order.md) allow.

## Details

When a later claim depends on a limitation, keep the brief reminder of the limitation next to that claim. If the draft does not explain how a limitation affects the results, flag the missing explanation instead of working out for yourself which conclusions still hold.

## Examples

**Edit 1.** Say the battery tests in the draft cover only room temperature.

> **Before.** Future work will test the battery in freezing conditions.

> **After.** The battery tests cover only room temperature. Future work will test the battery in freezing conditions.

**Edit 2.** Say the draft specifies that the observations cover only weekdays.

> **Before.** Unfortunately, the observations have limited coverage.

> **After.** The observations cover only weekdays.

**Edit 3.** Suppose the draft explains elsewhere that missing night readings prevent estimates of daily totals but leave the weekday daytime comparison valid.

> **Before.** Night readings are missing.

> **After.** Night readings are missing, so daily totals cannot be estimated. The weekday daytime comparison remains valid.

**Edit 4.** Imagine the draft says elsewhere that absolute masses cannot be interpreted because the scale was not calibrated. The revision below is a proposal to the author.

> **Before.** The only limitation is the slow display.

> **After.** One limitation is the slow display. Another limitation is that the scale was not calibrated, so absolute masses cannot be interpreted.

**Edit 5.** Suppose the author asks for cuts, and triage has reached repeated full statements of limitations. The full limitation already appears earlier in this section.

> **Before.** Demand peaks at noon. The tests exclude nights, so daily totals cannot be estimated.

> **After.** During the monitored daytime hours, demand peaks at noon.
