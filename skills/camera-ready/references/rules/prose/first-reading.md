# Make every sentence clear on the first reading

Length alone is not a defect. Put subjects next to verbs and verbs next to their objects or required phrases ("compare X with Y"): "the five expression types (attribute access, subscripts, calls, nested calls, and string literals) leave the cursor in place" becomes "the five expression types leave the cursor in place: attribute access, subscripts, calls, nested calls, and string literals". Shorten a long opening phrase or clause. Move a long subject clause toward the end ("It remains open whether the gain survives at larger scale"), and, when grammar allows either order, put the longer of two phrases last, unless the long part states the old information. Keep short, familiar asides. Move an interruption that introduces new material or a full clause ("the gain, once the cache is warm, disappears") to the beginning or end, make it a separate sentence, or cut it if it adds nothing, unless it states old information readers need there. Never nest one such interruption inside another before the main verb.

Rewrite strings of three or more nouns with a preposition or a clause: "the retrieval failure recovery path" becomes "the code path that runs when retrieval fails". Also break up long sequences of modifiers, usually more than three words before the head noun. Count an established technical name ("large language model") as one noun.

Keep articles so that sentences read as prose, not notes ("Model reaches 90% accuracy on benchmark"). Keep optional words that mark where a long or hard-to-predict clause begins. Restore "that" after verbs such as "assume", "suppose", "show", "prove", or "find" when readers could at first take the next noun as the verb's object ("We assume that the samples ..."); after other verbs, adjectives ("certain that ..."), and conjunctions ("so that") when a long clause follows; and before a long relative clause ("the bound that the analysis in Section 4 gives"). Restore "that were" in a shortened clause such as "the samples stored in the cabinet" when readers could take "stored" for the main verb. Use "in order to" when a bare "to" could look like a value ("we limit the batch size in order to fit in memory"). Do not add optional words to short, predictable clauses, or "that" after "we have".

Read from left to right for words that mislead at first: "We prove that A and B imply C" first reads as proving A, so write "We prove that the two conditions A and B together imply C". Make clear which noun a relative clause or verb-form phrase describes. Put "only" immediately before the word it restricts: "We only evaluate on two datasets" restricts the verb, and "We evaluate on only two datasets" restricts the count, which is usually what is meant. Put a condition before its claim unless it is short and clear at the end ("unbiased under assumption A1"), give a long condition its own sentence ("Suppose that A, B, and C hold. Then X."), and list three or more steps or conditions instead of packing them into one sentence. If a sentence still packs in too many concepts, follow [definitions and procedures](definitions-procedures.md).

## Details

In a string of nouns, first find the main noun ("cover" in "roof water drain cover") to determine which object the phrase names.

For a nested or trailing "which" or "that" clause, identify the noun each clause describes, then repeat that noun, join parallel clauses with "and" or "or", or split the sentence. Any summary noun used to refer back must keep the earlier statement's [claim status](referents.md); do not call a conjecture a finding.

If an aside contains its own commas and punctuation alone leaves the main clause hard to find, restructure the sentence. For a participial phrase (one beginning with a verb form such as "wearing gloves" or "stored in ice"), make clear who performs or undergoes the action, and whether the phrase states means, time, condition, or consequence. Flag the relation if the draft leaves it unclear. When you turn three or more steps or conditions into a numbered list, or when you split or repunctuate a sentence, keep each condition attached to the same claims as before. Also recheck the subject of each joined verb, the noun each modifier describes, and the [emphasis of findings and qualifications](stress-position.md).

A readability score does not measure whether readers in the field can follow a sentence. Do not replace an accurate technical term merely to improve a score.

## Examples

**Edit 1.** Suppose the preceding text discusses the leak and introduces trial 2.

> **Before.** That the lid leaks is, as trial 2 shows, certain. The tank, which holds water from the stream beside the shed, stays full.

> **After.** That the lid leaks is, as trial 2 shows, certain. The tank stays full. It holds water from the stream beside the shed.

The first sentence keeps the leak as its subject because readers already know about it. The short aside refers to a familiar trial and does not make the sentence hard to follow.

**Edit 2.**

> **Before.** We inspect the scanning electron microscope sample holder cover.

> **After.** We inspect the cover of the sample holder for the scanning electron microscope.

The words "scanning electron microscope" stay together because they name one instrument.

**Edit 3.**

> **Before.** Wearing gloves, the vial was opened by the technician.

> **After.** Wearing gloves, the technician opened the vial.

**Edit 4.**

> **Before.** We assume the samples in the red tray contain salt.

> **After.** We assume that the samples in the red tray contain salt.

**Edit 5.**

> **Before.** Open the valve only if the lid is shut, the pump is off, and the tank is cool.

> **After.** Open the valve only if all three conditions hold:
> 1. The lid is shut.
> 2. The pump is off.
> 3. The tank is cool.
