# Cutting

The [spine test](#the-spine-test) decides what the paper needs; the request decides what you may delete.

**Delete bloat without asking.** Bloat is [Blacklisted patterns](style.md#blacklisted-patterns) and sentences that announce content in place of stating it ([Say the thing](style.md#concision)); word-level tightening within a surviving sentence also needs no permission.

**Idea-level cutting needs the author's request.** Cut only when requested ("cut this to eight pages", "condense", or a hard venue limit); otherwise name the candidate and leave it in place ("this paragraph is off-spine; cut it?"). This requirement covers every sentence carrying something the author would miss: an idea, a result, a caveat, evidence, or a transition the argument needs.

## The spine test

State the paper's core claims in one to three sentences. That is the spine; justify each paragraph in one line as supporting it. Test content by **whether the spine needs it**, not whether it is true or interesting. A section you cannot give a short, specific title probably carries more than one point; flag it before cutting inside it. A cut is justified only if the argument reads at least as clearly without the content.

Work top down. Tag each paragraph *central*, *supporting*, *ancillary*, or *off-spine*. Cut or relocate what is off-spine, trim what is ancillary, and only then go sentence by sentence inside what survives.

## Triage order

Under a length constraint, cut in this order, most expendable first.

1. **Repeated restatement.** The same point made in the introduction, the section opener, and the conclusion. Keep the instance that carries the most weight, usually the one in the section that owns the point, and cut the echoes. Two kinds of repetition stay: the abstract, introduction, and conclusion are expected to restate the contributions, and a deliberate reminder refreshes a definition made pages earlier ([Refresh long-lived shorthand](style.md#terminology)). An expected restatement is still not a copy, so a conclusion sentence repeated word for word from the abstract gets the specifics the results established, or a flag.
2. **Over-explicit signposting** ([Fold self-referential signposts](style.md#concision)).
3. **Tangential background and related work.** Anything that does not motivate this paper's question. A citation list that states no relation to the gap this paper fills is expendable; the two or three works that define the gap are not.
4. **Minor results, secondary analyses, and exploratory findings.** A result that advances no central claim leaves the main text. Relocate rather than delete when it supports rigor: sensitivity analyses, robustness checks, and the negative result a skeptical reviewer will ask about. The account of what the authors tried first belongs here too; a failed alternative stays only as a stated negative result.
5. **Exhaustive parameter and implementation detail.** The main text stays reproducible in outline. The full sweep goes to the appendix.

## Protect

Some sentences add no new information, but the argument depends on them. Preserve the following content, relocating only as [Sentence by sentence](#sentence-by-sentence) allows:

- **Hedges, qualifiers, scope conditions, and limitations.** Deleting "these results come from a single dataset and may not generalize" silently upgrades every claim downstream. Cutting a caveat is a claims edit ([Claims](claims.md#claims)), so if a length request forces one, recalibrate the surviving claim ([After the pass](#after-the-pass)).
- **The evidence that earns a claim.** Cutting the supporting number or example while keeping the confident assertion leaves the claim unsupported.
- **Framing, orienting, and summary sentences.** When a minor result is cut, the sentence that said why this class of question matters usually stays and now frames the results that survive, and so does the summary sentence that states the high-level idea before the specifics arrive ([Say the thing](style.md#concision)).
- **Caption content that repeats the body text.** A caption is read on its own, so its overlap with the body is not an echo. Tighten a caption's wording, never its contents ([Figures and tables](style.md#figures-and-tables)).
- **Genuine transitions and back-references.** A transition that carries logic stays, as does a back-reference a later sentence depends on ([Paragraphs](style.md#paragraphs)).
- **Topic sentences.** A paragraph whose controlling idea was cut is a stub, not a shorter paragraph.
- **Reproducibility content.** The statistical tests used, the handling of missing data and multiple comparisons, and enough method for the reader outside the subfield to judge the study.
- **Fair characterization of prior work.** The sentence that credits a predecessor or states accurately what they did is not spare.

## Sentence by sentence

Inside a surviving paragraph, ask of each sentence in order:

1. **Does the spine need it?** If it supports no central claim, it is a candidate for deletion or relocation; steps 2 to 4 decide.
2. **Does the reader need it?** A sentence can add no new claim and still frame, transition, calibrate, or orient ([Protect](#protect)).
3. **What breaks without it?** Scan forward for dependents: a later "this" or "as shown above", a citation or term that appears only here, a claim whose hedge or evidence lived in this sentence, or the paragraph's topic string. Fix every dependent in the same edit or keep the sentence.
4. **Delete or relocate?** Delete when the content serves no one. Relocate to an appendix, supplement, or footnote when only a minority of readers, or one skeptical reviewer, needs it; reproducibility content is relocated, never deleted ([Protect](#protect)). Relocate only into a section that already exists; otherwise leave the content in place and flag what the appendix would have to contain.
5. **Read the seam.** Read the sentence before the gap and the sentence after it as a pair. The second must open with something the first supplied: a term, a result, or a referent. If the link now needs an inference the deleted sentence used to make, repair it with a clause added to an adjacent sentence, or reuse the old framing sentence to open what follows.

- Before: "We also swept the learning rate over five values; 3e-4 was best. We use it for all remaining experiments."
- Bad: "We use it for all remaining experiments." ("it" now points at nothing.)
- Good: "We use a learning rate of 3e-4 for all remaining experiments (sweep in Appendix B)."

## Stop rules

Three signals show that a cut should not stand as made:

- **The cut leaves the paragraph underdeveloped or breaks its topic string.** Merge it into a neighbor that shares its point; otherwise repair the missing development or link ([Paragraphs](style.md#paragraphs)).
- **You are cutting because the passage confuses you.** Diagnose first. Confusion usually signals a missing step rather than an excess one, and the fix is sometimes to add the step ([Plain wording](style.md#plain-wording)).
- **The reader outside the subfield can no longer follow the condensed version.** You are past the floor ([Non-negotiables](../SKILL.md#non-negotiables)), so restore framing and steps instead of cutting further.

## After the pass

- **Claims calibration.** For every surviving claim, confirm that its hedging and its evidence both survived, and run the [verb ladder](claims.md#the-verb-ladder) over the shortened text. A claim whose support moved to the appendix gets a pointer to it, and a rung down only when the surviving evidence supports less.
- **Narrative arc and pointers.** Read the whole text. The story must still run from problem to gap to approach to findings to implications without the reader supplying links you deleted. Then check for dangling references, uncited figures and tables, appendix pointers that name nothing, and terms now used before their first definition.
