# Cut in triage order under a length constraint

Under a length constraint, cut material in the following triage order while respecting [protected content](protected-sentences.md) and [relocation safeguards](sentence-dependencies.md):

1. **Repeated restatement.** Cut points repeated across the introduction, section openings, and conclusion, keeping the most useful statement (usually the one that develops the point). Always preserve one statement of each contribution in each of the abstract, the introduction, and the conclusion, along with [shorthand reminders](../conventions/shorthand-reminders.md). Keep a paragraph's closing restatement when readers need the intervening explanation to understand the opening claim. If a restatement copies another passage verbatim, such as a conclusion that repeats the abstract word for word, revise it using established results or flag it. Apply the [deletion test](../prose/deletion-test.md).
2. **Signposting left after bloat removal.** Cut remaining signposts, including the [roadmap](../prose/signposts.md) otherwise permitted at the end of the introduction, but preserve pointers to evidence and proofs.
3. **Tangential background and related work.** Cut background that does not motivate the research question, and cut citation lists unrelated to the gap. Keep the few works and comparisons that define the gap.
4. **Minor results, secondary analyses, and exploratory findings.** Remove from the main text any results that do not advance a central claim. Relocate sensitivity analyses and robustness checks needed for rigor, but keep in the main text any failure or counterevidence that alters a central claim. If a failed approach remains in the main text, state it as a negative result rather than narrating a history of attempts.
5. **Exhaustive parameters and procedural detail.** Keep enough detail in the main text to make the method reproducible in outline, including [explicit procedures](../prose/definitions-procedures.md), essential steps, and conditions; relocate complete parameter lists, full parameter sweeps, and subsidiary details.

## Details

This rule has no further details.

## Examples

> **Context.** The author requests a length cut, and this paragraph's opening sentence is clear on its own.
>
> **Bad.** The lid reduces evaporation in both jars. In both jars, less water evaporates with the lid.
>
> **Good.** The lid reduces evaporation in both jars.

> **Context.** The draft reports that the lid halves evaporation, and a length cut removes the conclusion's only statement of this contribution.
>
> **Bad.** The next step is a field trial.
>
> **Good.** The lid halves evaporation. The next step is a field trial.

> **Context.** A proposed cut removes the final sentence, even though the intended readers need the intervening explanation to understand the opening claim.
>
> **Bad.** An open vent prevents pressure buildup. Heating expands the gas, which escapes through the vent.
>
> **Good.** An open vent prevents pressure buildup. Heating expands the gas, which escapes through the vent. The vent thus prevents pressure buildup.

> **Context.** The author requests a length cut after redundant restatements have already been removed.
>
> **Bad.** Section 2 presents the design, and Section 3 presents the tests. Appendix A proves the stability bound.
>
> **Good.** Appendix A proves the stability bound.

> **Context.** The author requests a length cut after earlier triage tiers are exhausted, and the history of ceramic pots does not motivate the question about drainage.
>
> **Bad.** Ceramic pots have a long history. Unlike the pots tested by Lin (2020), ours have drainage holes.
>
> **Good.** Unlike the pots tested by Lin (2020), ours have drainage holes.

> **Context.** The author requests a length cut after earlier triage tiers are exhausted, and an existing Appendix B already contains the full pressure checks.
>
> **Bad.** The seal holds at 10 °C and 20 °C but leaks at 30 °C. We repeat each temperature test at three pressures.
>
> **Good.** The seal holds at 10 °C and 20 °C but leaks at 30 °C. Appendix B gives the pressure checks.

> **Context.** The author requests a length cut, and the failure of paper lids bears on a central claim.
>
> **Bad.** We first tried paper lids, then tried paper lids again. Paper lids leak.
>
> **Good.** Paper lids leak.

> **Context.** The author requests a length cut after earlier triage tiers are exhausted, and an existing Appendix C already lists the complete fan settings.
>
> **Bad.** We dry the seeds at 30 °C. The fan settings are 1, 2, 3, 4, and 5.
>
> **Good.** We dry the seeds at 30 °C; Appendix C lists the fan settings.

> **Context.** The conclusion copies the abstract's sentence "The lid reduces evaporation." word for word, whereas the Results section reports that the lid reduces water loss from 8 mL to 4 mL per day.
>
> **Bad.** The lid reduces evaporation.
>
> **Good.** The lid reduces water loss from 8 mL to 4 mL per day.
