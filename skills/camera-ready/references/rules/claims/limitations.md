# State limitations precisely and explain their effects

State each limitation fully, precisely, and without apology where it first affects a method or inference, and keep brief reminders that limit later claims. A limitation of an interpretation introduced in the Discussion may appear there first. Next to each limitation, keep the draft's explanation of how it affects the results and which conclusions still hold, or flag the missing explanation. Flag unexplained unexpected results, unjustified data exclusions, and decoy limitations (see Details). Every future-work statement must name the current limitation it addresses. Move a limitation between sections only under the [relocation rules](../cutting/idea-cuts.md). Delete a repeated full statement only when a request to shorten the text reaches it in the [triage order](../cutting/triage-order.md).

## Details

When a later claim depends on a limitation, keep the brief reminder of the limitation next to that claim. If the draft does not explain how a limitation affects the results, flag the missing explanation instead of working out for yourself which conclusions still hold. A decoy limitation is a stated limitation that names a minor weakness while a larger weakness documented elsewhere in the draft goes unmentioned.

## Examples

**Example 1.** The draft states that the battery tests cover only room temperature.

> **Bad.** Future work will test the battery in freezing conditions.
>
> **Good.** The battery tests cover only room temperature. Future work will test the battery in freezing conditions.

**Example 2.** The draft states that observations cover only weekdays.

> **Bad.** Unfortunately, the observations have limited coverage.
>
> **Good.** The observations cover only weekdays.

**Example 3.** The draft says that missing night readings prevent estimating daily totals but leave the weekday daytime comparison valid. The Good line is a proposed revision for the author.

> **Bad.** Night readings are missing.
>
> **Good.** Night readings are missing, so daily totals cannot be estimated. The weekday daytime comparison remains valid.

**Example 4.** Elsewhere, the draft says that the scale was not calibrated, so absolute masses cannot be interpreted. The Good line is a proposed revision for the author.

> **Bad.** The only limitation is the slow display.
>
> **Good.** One limitation is the slow display. Another limitation is that the scale was not calibrated, so absolute masses cannot be interpreted.

**Example 5.** The author asks for a shorter text, and cutting has reached repeated full statements of limitations. An earlier passage in the same section states that the tests exclude nights, so daily totals cannot be estimated.

> **Bad.** Demand peaks at noon. The tests exclude nights, so daily totals cannot be estimated.
>
> **Good.** During the monitored daytime hours, demand peaks at noon.
