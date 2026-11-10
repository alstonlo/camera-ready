# Resolve references without changing the claim's status

Make each pronoun, demonstrative, comparative, and shorthand noun phrase identify one referent from the text alone. Name ambiguous baselines or previous runs with the draft's labels ("the v1.2 measurement in Section 4.1") and reuse those names. The first sentence under a section title or a run-in paragraph title must make sense without it ("**Gradient caching.** Gradient caching recomputes ...", not "**Gradient caching.** This technique recomputes ..."). Restore context lost during editing, and flag connections you cannot resolve rather than choosing a referent. Replace an ambiguous "this", "that", or "it" with wording that names the referent the draft supports, preserving its status and evaluation (a conjecture is not a finding, and a change is not necessarily an improvement): in "We prune low-magnitude weights and retrain. This improves generalization.", write "This pruning step improves generalization" if the draft identifies pruning as the cause. Allow bare "This" to introduce an interpretation after one unambiguous claim in openings such as "This means that", "This is because", and "This suggests that".

## Details

To test the first sentence under a heading, cover the heading and read the sentence alone. Check that the sentence still names its own subject.

## Examples

**Edit 1.** Suppose the draft names run A as the comparison for run C.

> **Before.** Runs A and B use dry sand. Run C drains faster than the earlier run. The earlier run leaves a puddle.

> **After.** Runs A and B use dry sand. Run C drains faster than run A. Run A leaves a puddle.

**Edit 2.**

> **Before.** **Copper mesh.** This catches the larger particles.

> **After.** **Copper mesh.** Copper mesh catches the larger particles.

**Edit 3.** Say an earlier cut removed the draft's identification of the red switch as the power switch, and the panel also has a blue switch.

> **Before.** Press the switch. This control then turns the pump off.

> **After.** Press the red power switch. This control then turns the pump off.

Before is the result of that cut, and After restores the lost identification. Once the switch is named, "This control" has a clear referent.

**Edit 4.** Suppose the draft identifies the conjecture as the reason for the next test.

> **Before.** We conjecture that salt weakens the seal; the lid also bends. This motivates the next test.

> **After.** We conjecture that salt weakens the seal; the lid also bends. This conjecture motivates the next test.

**Edit 5.** Say the draft leaves open whether higher pressure is beneficial.

> **Before.** We replaced the valve, and the pressure rose. This improvement triggered the alarm.

> **After.** We replaced the valve, and the pressure rose. This rise in pressure triggered the alarm.

**Edit 6.** Imagine the draft identifies the dish in the warm room as the one that froze.

> **Before.** We left one dish of water in a cold room and one in a warm room. It froze overnight. This suggests that the heating failed.

> **After.** We left one dish of water in a cold room and one in a warm room. The dish in the warm room froze overnight. This suggests that the heating failed.

The final "This" can stay because it now refers to one clear event: the dish in the warm room freezing.
