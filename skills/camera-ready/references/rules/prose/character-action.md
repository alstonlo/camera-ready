# Put actors in subjects and actions in verbs

When a phrase pairs a weak verb with a nominalization ("perform an evaluation of", "lead to an improvement in"), or when a clause contains several nominalizations, make the actor the subject and the action the verb. Preserve every action. If the draft never states who performs an action, flag the missing actor. Keep a nominalization that names a technique ("quantization") or a recurring concept, refers to the previous sentence ("This reduction in noise ..."), replaces an awkward "the fact that" clause, or appears alone in a clear sentence. When an inanimate subject takes a verb of intending, thinking, perceiving, feeling, remembering, or eating ("hopes", "forgets", "swallows"), replace the verb with what literally happens. Keep established technical usage (see Details), and keep a component, instrument, or organism as the subject of an operation it performs. A result or figure may be the subject of a [reporting verb](../claims/verb-ladder.md) ("the results suggest"). Follow [voice](../conventions/active-voice.md) and [information flow](passives-fronting-inversions.md).

## Details

A nominalization is a noun that names an action, such as "evaluation", often ending in -tion, -ment, -ance, or -ing. To find actions written as nouns, list the main verbs in a passage. If "is", "has", or "leads to" appears repeatedly, check whether a nearby noun names the action. Repeated verbs invite inspection, not automatic rewriting. In theoretical work, an abstract concept may serve as the subject.

Keep established technical verbs with inanimate subjects, such as an enzyme recognizing its substrate, a sensor detecting light, a function expecting input, or a model learning. In contrast, a document cannot act. If the draft describes a specification or other document as acting (for example, making a decision), the sentence may need the person or component that acts as its subject. Take any replacement verb from what the draft says happens, without inferring unstated system behavior or assigning blame for a failure.

## Examples

**Example 1.**

> **Bad.** The technician’s inspection of the seal precedes the technician’s replacement of it.
>
> **Good.** The technician inspects the seal before replacing it.

**Example 2.** Good keeps "quantization" because it names the technique being evaluated; turning that noun into a verb would change the action described.

> **Bad.** We perform an evaluation of quantization.
>
> **Good.** We evaluate quantization.

**Example 3.** The draft identifies the authors as the people who detect the signals. Good keeps "This reduction in noise" because it connects the two sentences, while giving the detection an actor and a verb.

> **Bad.** Noise fell after filtering. This reduction in noise permits the detection of faint signals.
>
> **Good.** Noise fell after filtering. This reduction in noise permits us to detect faint signals.

**Example 4.** The draft states elsewhere that the recorder deletes the readings.

> **Bad.** The recorder forgets readings after an hour.
>
> **Good.** The recorder deletes readings after an hour.

**Example 5.** Good keeps "The results suggest" because results can support an inference without being treated as thinking agents.

> **Bad.** The results suggest that the coating causes a reduction in heat loss.
>
> **Good.** The results suggest that the coating reduces heat loss.
