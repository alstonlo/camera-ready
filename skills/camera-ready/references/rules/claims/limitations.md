# State limitations precisely and explain their effects

State each limitation in full, precisely and without apology, where it first affects a method or inference, and keep brief reminders that bound later claims. Next to the limitation, keep the draft's explanation of how it affects the results and which conclusions still hold; flag a missing explanation. Flag unexplained anomalies and unjustified exclusions. Also flag a decoy limitation, which names a minor weakness while hiding a larger one documented in the draft. Any future-work statement must identify the current limit it addresses. When the Discussion introduces an interpretation, a limitation of that interpretation may appear there first. Move a limitation to another section only as the [relocation rules](../cutting/idea-cuts.md) allow; delete duplicate full accounts only when a length request reaches them in the [triage order](../cutting/triage-order.md).

## Details

When the draft does not explain how a limitation affects the results, flag the missing explanation rather than inferring which conclusions still hold.

## Examples

The draft states that the battery tests cover only room temperature.

> Bad: Future work will test the battery in freezing conditions.
>
> Good: The battery tests cover only room temperature; future work will test the battery in freezing conditions.

The draft states that observations cover only weekdays.

> Bad: The observations have limited coverage.
>
> Good: The observations cover only weekdays.

> Bad: Unfortunately, the measurements exclude nights.
>
> Good: The measurements exclude nights.

> Bad: We estimate weekly demand from the readings. The readings cover weekdays only.
>
> Good: The readings cover weekdays only. We estimate weekly demand from the readings.

The draft states that missing night readings prevent a daily-total estimate but leave the weekday daytime comparison valid; the revision is proposed to the author.

> Bad: Night readings are missing.
>
> Good: Night readings are missing, so daily totals cannot be estimated; the weekday daytime comparison remains valid.

The draft's full limitation states that monitoring excludes nights, and a later paragraph summarizes the daytime finding.

> Bad: Demand peaks at noon.
>
> Good: During the monitored daytime hours, demand peaks at noon.

The draft attributes the sudden mass increase to water entering the container; the revision is proposed to the author.

> Bad: The mass rises abruptly on day 4.
>
> Good: The mass rises abruptly on day 4 because water enters the container.

The draft states that sensor failure left tray 6 without any readings; the revision is proposed to the author.

> Bad: We exclude tray 6.
>
> Good: We exclude tray 6 because sensor failure leaves it without any readings.

The draft states that an uncalibrated scale prevents interpreting absolute masses; the revision is proposed to the author.

> Bad: The only limitation is the slow display.
>
> Good: One limitation is the slow display; the uncalibrated scale also prevents interpreting absolute masses.

The Discussion first proposes a migration explanation and states that no migration measurements were collected; the revision is proposed to the author.

> Bad: Discussion: Migration may explain the decline.
>
> Good: Discussion: Migration may explain the decline, but no migration measurements were collected.

The author requests shortening duplicate full accounts; an earlier passage in the same section states that the tests exclude nights, so daily totals cannot be estimated.

> Bad: Demand peaks at noon. The tests exclude nights, so daily totals cannot be estimated.
>
> Good: During the monitored daytime hours, demand peaks at noon.
