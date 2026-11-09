# State limitations precisely and explain their effects

State each limitation fully, precisely, and without apology where it first affects a method or inference, and keep brief reminders that limit later claims. A limitation of an interpretation introduced in the Discussion may appear there first. Next to each limitation, keep the draft's explanation of how it affects the results and which conclusions still hold, or flag the missing explanation. Flag unexplained unexpected results, unjustified data exclusions, and decoy limitations (see Details). Every future-work statement must name the current limitation it addresses. Move a limitation between sections only under the [relocation rules](../cutting/idea-cuts.md). Delete a repeated full statement only when a request to shorten the text reaches it in the [triage order](../cutting/triage-order.md).

## Details

When a later claim depends on a limitation, keep the brief reminder of the limitation next to that claim. If the draft does not explain how a limitation affects the results, flag the missing explanation instead of working out for yourself which conclusions still hold. A decoy limitation is a stated limitation that names a minor weakness while a larger weakness documented elsewhere in the draft goes unmentioned.

## Examples

**Edit 1.** The battery tests reported in the draft cover only room temperature.

> **Before.** Future work will test the battery in freezing conditions.
>
> **After.** The battery tests cover only room temperature. Future work will test the battery in freezing conditions.

**Edit 2.** The observations specified in the draft cover only weekdays.

> **Before.** Unfortunately, the observations have limited coverage.
>
> **After.** The observations cover only weekdays.

**Edit 3.** Missing night readings prevent estimates of daily totals but leave the weekday daytime comparison valid, as stated elsewhere in the draft.

> **Before.** Night readings are missing.
>
> **After.** Night readings are missing, so daily totals cannot be estimated. The weekday daytime comparison remains valid.

**Edit 4.** Elsewhere, the draft says that absolute masses cannot be interpreted because the scale was not calibrated. After is a proposal to the author.

> **Before.** The only limitation is the slow display.
>
> **After.** One limitation is the slow display. Another limitation is that the scale was not calibrated, so absolute masses cannot be interpreted.

**Edit 5.** The author has asked for cuts, and triage has reached repeated full statements of limitations. The full limitation appears earlier in this section.

> **Before.** Demand peaks at noon. The tests exclude nights, so daily totals cannot be estimated.
>
> **After.** During the monitored daytime hours, demand peaks at noon.
