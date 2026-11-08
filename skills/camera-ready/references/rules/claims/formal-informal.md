# Identify the kind of evidence supporting each claim

When a sentence reads like a theorem but cites no result and states no conditions, clarify its status: link it to the result and its assumptions, restate the empirical or intuitive claim the draft supports, or flag it. When a theorem supports an empirical claim, check its assumptions in that setting and flag an invalid application. An unmet assumption does not make the theorem false. Never remove a condition from a theorem or other formal statement to simplify it; flag a condition that seems unnecessary. Distinguish proof, model calculation, simulation, and system measurement. Flag a claim that transfers a result from a model to real system behavior without supporting evidence; a valid claim about the model needs no deployment study.

## Details

Locate the formal result and its conditions before judging an application. A statement about every input or every execution may resemble a theorem even without the word "theorem". An empirical restatement is appropriate only when the draft supplies empirical support.

Check the assumptions against the setting of the conclusion. A theorem that assumes reliable delivery does not establish behavior under message loss. Applying a theorem where its assumptions fail is different from a flaw in the theorem; a suspected error in the proof still needs its own flag.

Calculating within a mathematical model, simulating a simplified system, and measuring an implementation provide different kinds of evidence. Each can support a legitimate claim within its conditions. A claim that transfers the result beyond those conditions needs evidence that the result applies there.

An apparently unnecessary mathematical restriction may determine the result's scope. A flag may include simpler conditions as a proposed revision only when the draft establishes that the simpler statement remains true and that the restriction adds no useful information. Never remove a condition for fluency.

## Examples

The draft reports the bridge's response only in a simulation, with no measurements of the actual bridge; the revision is proposed to the author.

- Bad: Under the tested load, the bridge bends by 2 cm.
- Good: In the simulation, under the tested load, the bridge bends by 2 cm.
