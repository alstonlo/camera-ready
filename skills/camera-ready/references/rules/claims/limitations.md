# State limitations precisely and explain their effects

State each limitation fully, precisely, and without apology where it first affects a method or inference, and keep brief reminders that limit later claims. A limitation of an interpretation introduced in the Discussion may appear there first. Next to each limitation, keep the draft's explanation of how it affects the results and which conclusions still hold, or flag the missing explanation. Flag unexplained unexpected results, unjustified data exclusions, and decoy limitations (see Details). Every future-work statement must name the current limitation it addresses. Move a limitation between sections only under the [relocation rules](../cutting/idea-cuts.md). Delete a repeated full statement only when a request to shorten the text reaches it in the [triage order](../cutting/triage-order.md).

## Details

When a later claim depends on a limitation, keep the brief reminder of the limitation next to that claim. If the draft does not explain how a limitation affects the results, flag the missing explanation instead of working out for yourself which conclusions still hold. A decoy limitation is a stated limitation that names a minor weakness while a larger weakness documented elsewhere in the draft goes unmentioned.

## Examples

**Edit 1.** The draft reports that the battery tests cover only room temperature. The edit adds this limitation before the freezing tests proposed as future work, so readers know which gap those tests would address.

> **Before.** Future work will test the battery in freezing conditions.
>
> **After.** The battery tests cover only room temperature. Future work will test the battery in freezing conditions.

**Edit 2.** The draft specifies that observations cover only weekdays. The edit removes "Unfortunately" and replaces "have limited coverage" with "cover only weekdays", so the limitation is precise and stated without apology.

> **Before.** Unfortunately, the observations have limited coverage.
>
> **After.** The observations cover only weekdays.

**Edit 3.** Elsewhere, the draft explains which conclusions the missing readings prevent and which remain valid. The edit adds that daily totals cannot be estimated but the weekday daytime comparison remains valid, so readers see both the limitation's effect and the conclusion it still permits.

> **Before.** Night readings are missing.
>
> **After.** Night readings are missing, so daily totals cannot be estimated. The weekday daytime comparison remains valid.

**Edit 4.** The calibration problem and its effect on absolute masses are documented elsewhere in the draft. The edit, a proposal to the author, replaces "The only limitation" with "One limitation" and adds that the uncalibrated scale prevents interpreting absolute masses, so the slow display does not conceal the larger weakness.

> **Before.** The only limitation is the slow display.
>
> **After.** One limitation is the slow display. Another limitation is that the scale was not calibrated, so absolute masses cannot be interpreted.

**Edit 5.** The author asks for cuts, and the triage order has reached repeated full statements of limitations; an earlier passage in this section gives the full limitation. The edit removes the repeated full limitation and adds "During the monitored daytime hours" to the peak claim, because the observations do not establish a peak across the whole day.

> **Before.** Demand peaks at noon. The tests exclude nights, so daily totals cannot be estimated.
>
> **After.** During the monitored daytime hours, demand peaks at noon.
