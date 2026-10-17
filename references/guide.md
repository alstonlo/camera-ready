# Writing Guide

Five sections, in the order of application:

- [Claims](#claims): match each claim to its evidence, through the reporting verb, scope, causal language, significance, hedges, over- and underclaiming, speculation, and limitations.
- [Cutting](#cutting): what may be deleted or relocated without the author's request, the triage order under a length limit, what to protect, and how to repair the text around a cut.
- [Prose](#prose): ordering, paragraphs, information flow, sentence structure, concision, plain wording, and comparison with prior work.
- [Deslopping](#deslopping): the patterns of AI-written prose, in two tiers.
- [Conventions](#conventions): voice, tense, terminology, citations, notation, figures and tables, and typography.

| Request | Sections applied |
|---|---|
| polish, tighten | all five |
| cut to a length | all five, with deletion and relocation allowed |
| overclaiming check, hedging question | Claims |
| de-AI pass | Deslopping and the prose rules it links to |
| one convention | that convention alone |

A request narrower than a polish also applies every rule the listed sections link to. Applying a section to a chunk means checking the chunk against every rule in it. Two rules can prescribe different edits for one sentence. Where one of the two links to the other, the linked rule decides. Otherwise the clearer sentence wins, and then your judgement as an expert editor.

## Claims

Every claim must match its evidence; overclaiming and underclaiming are both failures. An aspirational goal may motivate the text if the text marks it as not attained.

### The verb ladder

Pick the reporting verb from the evidence, never from enthusiasm.

| Verb | Evidence required |
|---|---|
| we **prove** | a theorem with stated assumptions, and nothing else |
| we **show / demonstrate / establish** | direct evidence that rules out the plausible alternatives |
| we **find / observe / report** | a directly measured empirical result |
| results **suggest / indicate**; we **hypothesize / conjecture** | an inference or interpretation that could reasonably be wrong |

A benchmark result never proves a mechanism, and a figure or table "shows" only what it displays; the claim read from it takes its own rung.

A claim hedged in the results must not reappear unhedged in the abstract, introduction, conclusion, or any other summary of the results. For each claim in the abstract, introduction, or another summary, find the result that supports it. Where the draft holds the support and the claim lacks a pointer, add one ("(Section 5)", "(Table 2)"). Where no support exists, flag the claim.

### Scope

Evidence sets both a claim's scope and its confidence (plain or hedged). From broadest to narrowest, scope ranges from a guarantee ("X always holds"), through a systematic claim ("X generally happens across contexts") and a narrow claim ("X is best for settings V and W"), to an existence claim ("we find one case where X"). Pick the broadest scope and the plainest confidence the evidence supports. When support is uncertain, leave the claim in place and flag it; that caution is no reason to hedge or drop a claim the evidence does support, which would be [underclaiming](#failure-modes).

Scope every headline claim to its conditions, datasets, and settings; absolutes ("always", "unique") claim the case you did not test. A bare generic plural claims the whole class, so "Transformers fail to retrieve early tokens" asserts it of every Transformer. When the evidence covers only the models tested, write "the four Transformers we test fail to retrieve early tokens".

A result reported without a comparison supports "X works", not "X is better" or "X is practical", so flag the missing baseline when the draft claims more. A qualitative example (a generated sample, a saliency map, a case study) supports only an existence claim. Offered as evidence for anything broader, it needs the text to say how it was chosen (at random, as typical, or as the best case), so flag it when the draft does not say.

### Causal language

Use "causes", "leads to", "improves because", and any other wording that credits a design choice only where the evidence supports causation, as an ablation that isolates the component does. Correlational results take "is associated with", "correlates with", or "coincides with". When the text introduces several changes together and isolates none, the text may credit the combination but no single change, and must not imply that every change is necessary.

### Formal and informal claims

Keep every claim visibly formal or visibly informal. A sentence that reads like a theorem ("all local minima have error close to that of the global minimum") but points to no result and states no conditions is neither; tie it to a stated result with its assumptions, rewrite it as the empirical or intuitive claim it is, or flag it when the draft supports neither. When the text invokes a theorem to support an empirical claim, check that the theorem's conclusion bears on that claim under the text's conditions; a convergence result for convex objectives does not support a claim about non-convex training, so flag the link.

### Uncertainty and significance

A comparison between two numbers is a claim, and its evidence includes how much the numbers vary. For every reported comparison, the reader must be able to find three things in the sentence, the caption, or a convention the text states once: how many runs each number covers and how it summarizes them (mean, median, or best run); whether the ± is a standard deviation, a standard error, or a confidence interval; and what varies (seed, data split, or the test examples a bootstrap resamples). Flag the gap when the draft omits one.

- Bad: "Our method significantly outperforms the baseline (71.2 ± 0.4 vs 68.4 ± 0.6)."
- Good: "Our method outperforms the baseline by 2.8 points (71.2 ± 0.4 vs 68.4 ± 0.6; mean ± standard deviation over five seeds)."

The two sides of a comparison must be computed the same way, so a best-run number is not comparable with a mean of final results, and a number copied from another publication is comparable only under the same evaluation protocol. Flag every comparison where the text does not show that its two sides were computed alike.

Reserve "significant(ly)" for the result of a statistical test that the text names, paired with the p-value or significance level and, where the draft reports it, the effect size. Where it means large or important, replace it with the magnitude; where it claims statistical significance but names no test, flag it. When the draft tests significance on several datasets or metrics, check that it says how it corrects for multiple comparisons, and flag it if it does not.

Failure to reject a hypothesis of no difference does not establish equality, so "the two methods perform the same (paired bootstrap, p = 0.21)" becomes "we find no significant difference between the two methods (paired bootstrap, p = 0.21)". When intervals overlap and the text names no test, flag the claimed superiority; overlap alone decides nothing in either direction. When the ranking of methods changes with the aggregate metric, scope each claim to the metric that produced it.

### Hedges

Place the hedge where data becomes interpretation, so that the measurement is unhedged and the mechanism is hedged, never the reverse.

- Bad: "Accuracy appears to drop by roughly 4.2 points when we remove the auxiliary loss, which shows the loss is a regularizer."
- Good: "Accuracy drops 4.2 points when we remove the auxiliary loss (Table 3), which suggests the loss acts as a regularizer."

Procedures are unhedged wherever the text describes them, in a Methods section or elsewhere; only the rationale for a choice may carry a hedge. Results, Discussion, and Conclusion sections, and any other passage that interprets a measurement, follow this boundary between measurement and interpretation. An abstract or other summary compresses each claim but keeps its rung on the [verb ladder](#the-verb-ladder) and its hedge.

Use at most one hedge per claim, in a standard academic form ("may", "likely", "suggests", "appears to"). Softeners ("somewhat", "relatively", "essentially", and similar; not the [intensifiers](#concision) that are simply cut) weaken a claim without saying where it fails, so where the draft holds the condition under which the claim fails, or the size of the effect, state that in place of the softener; otherwise keep it and flag it, since deleting a claim's only hedge upgrades it. A qualifier whose deletion changes what is claimed ("usually", "on average", "in most runs") is a scope condition, not a hedge, and is [protected](#protect).

- Bad: "Our method is relatively robust to label noise."
- Good: "Our method loses 2 points of accuracy at 20% label noise, against 9 points for the baseline."

### Failure modes

**Overclaiming.** The following are banned for empirical results: *solves, proves, optimal, guarantees, first to* (unless the draft verifies the claim), unsupported superlatives, "human-level" or "state-of-the-art" without naming the task, benchmark, and metric, and "novel" as filler.

**Underclaiming.** State contributions plainly and completely, and do not weaken a real result with reflexive hedges. Each item in a "Contributions" list states a claim a reader could check and, where the draft has one, a pointer to its support. An item whose whole claim is *study, explore, investigate, describe*, or *discuss* claims nothing, so rewrite it from what the corresponding section reports, or flag it.

- Bad: "We study the theoretical properties of the estimator."
- Good: "We prove that the estimator is unbiased under assumption A1 (Section 4)."

### Speculation

Never state speculation in the grammatical form of established fact. Mark it with "We conjecture" or "One possible explanation is", or confine it to a Motivation or Discussion paragraph that the text marks, as a whole, as speculation.

An explanation built on an undefined term is speculation however it is phrased. "The gain comes from reduced internal covariate shift" cannot be checked until the text says how the shift is measured, so flag the term or mark the sentence as a hypothesis. A bare negative claim ("X does not imply Y") needs its status stated (a counterexample, a reference, or a statement that the question is open), so flag it when the draft gives none.

### Limitations

State each limitation once and precisely, without apology, and without a decoy limitation that hides the real weakness; flag a decoy, and cut a duplicate only when a length request reaches it in the [triage order](#triage-order). Frame each one by its impact on the findings ("results may not transfer to larger models, since every run uses the same 100M-parameter backbone"). A limitation phrased as future work must still say what the current results do not cover.

## Cutting

The [spine test](#the-spine-test) decides what the text needs; the request decides what you may delete or relocate.

**Delete bloat without asking.** Bloat is a [blacklisted pattern](#blacklisted-patterns), a sentence that announces content in place of stating it, and a signpost that the [concision rules](#concision) say to delete; word-level tightening within a surviving sentence also needs no permission.

**Idea-level cutting needs the author's request.** Cut or relocate only when requested ("cut this to eight pages", "condense", or a hard length limit); otherwise name the candidate and leave it in place ("this paragraph is off-spine; cut it?"). This requirement covers every sentence carrying something the author would miss: an idea, a result, a caveat, evidence, or a transition the argument needs. Reordering within a section to [build understanding early](#build-understanding-early) is a prose edit; moving content between sections or out of the main text is relocation.

### The spine test

State the text's core claims in one to three sentences. That is the spine; justify each paragraph in one line as supporting it. Test content by **whether the spine needs it**, not whether it is true or interesting. A section you cannot give a short, specific title probably carries more than one point; flag it before cutting inside it. A cut is justified only if the argument reads at least as clearly without the content.

Work top down. Tag each paragraph *central*, *supporting*, *ancillary*, or *off-spine*. Cut or relocate what is off-spine and trim what is ancillary, as far as the request allows, and only then go [sentence by sentence](#sentence-by-sentence) inside what survives.

### Triage order

Under a length constraint, cut in this order, most expendable first.

1. **Repeated restatement.** The same point made in the introduction, the section or chapter opener, and the conclusion. Keep the instance that carries the most weight, usually the one in the section that owns the point, and cut the echoes. Two kinds of repetition are not echoes and stay: one restatement of each contribution in the abstract, introduction, and conclusion, and a deliberate reminder that [refreshes a shorthand](#terminology) defined pages earlier. A permitted restatement is still not a copy, so a conclusion sentence repeated word for word from the abstract gets the specifics the results established, or a flag.
2. **Signposting that survives the bloat pass**, such as the two-sentence roadmap the [fold rule](#concision) allows; a pointer to a claim's support or a proof's home is not signposting and stays.
3. **Tangential background and related work.** Anything that does not motivate the text's question. A citation list that states no relation to the gap the text fills is expendable; the two or three works that define the gap are not.
4. **Minor results, secondary analyses, and exploratory findings.** A result that advances no central claim leaves the main text. Relocate rather than delete when it supports rigor: sensitivity analyses, robustness checks, and the negative result a skeptical reviewer will ask about. The account of what the authors tried first is in this tier too; a failed alternative stays in the main text only as a stated negative result.
5. **Exhaustive parameter and implementation detail.** The main text stays reproducible in outline, keeping its [spelled-out procedures](#plain-wording) and its [protected content](#protect); the full sweep goes to the appendix.

### Protect

Some sentences add no new information, but the argument depends on them. Preserve the following content, relocating only as the [sentence-by-sentence pass](#sentence-by-sentence) allows:

- **Hedges, qualifiers, scope conditions, and limitations.** Deleting "these results come from a single dataset and may not generalize" silently upgrades every claim downstream; an echo of a limitation stated in full elsewhere follows the [triage order](#triage-order). Cutting a caveat is a [claims edit](#claims), so if a length request forces one, recalibrate the surviving claim [after the pass](#after-the-pass).
- **The evidence that earns a claim.** Cutting the supporting number or example while keeping the confident assertion leaves the claim unsupported.
- **Framing, orienting, and summary sentences.** When a minor result is cut, the sentence that said why this class of question matters usually stays and now frames the results that survive, and so does the summary sentence that [states the high-level idea](#concision) before the specifics arrive.
- **Caption content that repeats the body text.** A caption is read on its own, so its overlap with the body is not an echo. Tighten a caption's wording, never the [contents a caption needs](#figures-and-tables).
- **Genuine transitions and back-references.** A transition that [carries logic](#paragraphs) stays, as does a back-reference a later sentence depends on.
- **Topic sentences.** A paragraph whose topic sentence was cut is a stub, not a shorter paragraph.
- **Reproducibility content.** The statistical tests used, the handling of missing data and multiple comparisons, and enough method for the reader outside the subfield to judge the study.
- **Fair characterization of prior work.** The sentence that credits a predecessor or states accurately what they did is not spare.

### Sentence by sentence

Inside a surviving paragraph, ask of each sentence in order:

1. **Does the spine need it?** If it supports no central claim, it is a candidate for deletion or relocation; steps 2 to 4 decide.
2. **Does the reader need it?** A sentence can add no new claim and still be [protected](#protect) because it frames, transitions, calibrates, or orients.
3. **What breaks without it?** Scan forward for dependents: a later "this" or "as shown above", a citation or term that appears only here, a claim whose hedge or evidence lived in this sentence, or the paragraph's topic string. Fix every dependent in the same edit or keep the sentence.
4. **Delete or relocate?** Delete when the content serves no one. Relocate to an appendix, supplement, or footnote when only a minority of readers, or one skeptical reviewer, needs it; reproducibility content is [protected](#protect), so it is relocated, never deleted. Relocate into an appendix or supplement only when it already exists; otherwise leave the content in place and flag what it would have to contain. A footnote may be new.
5. **Read across the gap.** Read the sentence before the gap and the sentence after it as a pair. The second must open with something the first supplied: a term, a result, or a referent. If the link now needs an inference the deleted sentence used to make, repair it with a clause added to an adjacent sentence, or reuse the old framing sentence to open what follows.

- Before: "We also sweep the learning rate over five values; 3e-4 is best. We use it for all remaining experiments."
- Bad: "We use it for all remaining experiments." ("it" now points at nothing.)
- Good: "We use a learning rate of 3e-4 for all remaining experiments (sweep in Appendix B)."

### Stop rules

Three signals show that a cut should not stand as made:

- **The cut leaves the paragraph underdeveloped or breaks its topic string.** Merge it into a neighbor that shares its point; otherwise repair the missing development or the broken [topic string](#paragraphs).
- **You are cutting because the passage confuses you.** Diagnose first. Confusion usually signals a missing step rather than an excess one, so supply the [missing step or referent](#plain-wording) when the draft states it elsewhere, and otherwise flag it.
- **The reader outside the subfield can no longer follow the condensed version.** Clarity for that reader is the floor, so restore framing and steps instead of cutting further.

### After the pass

- **Claims calibration.** For every surviving claim, confirm that its hedging and its evidence both survived, and run the [verb ladder](#the-verb-ladder) over the shortened text. A claim whose support moved to the appendix gets a pointer to it, and a rung down only when the surviving evidence supports less.
- **Narrative arc and pointers.** Read the whole text. The story must still run from problem to gap to approach to findings to implications without the reader supplying links you deleted. Then check for dangling references, uncited figures and tables, appendix pointers that name nothing, and terms now used before their first definition.

## Prose

### Build understanding early

Wherever a reader stops, they should hold as much understanding as the text up to that point could have given them.

Put the big picture before the details that refine it:

- The high-level idea precedes the fine-grained mechanism.
- The result and its interpretation precede the supporting evidence.
- The paragraph's claim is its first sentence (or, in a results paragraph, its second sentence, after the [question it answers](#paragraphs)), and the section's claim is its first paragraph.
- A definition precedes its first use, and context precedes anything new that depends on it.

Test an ordering by covering everything after a given sentence and asking what the reader knows so far. If a covered sentence would have taught the reader more than an uncovered one, move it up. This rule orders paragraphs within a section and sentences within a paragraph; inside a single sentence the new information goes last, in the [stress position](#information-flow-within-a-sentence).

### Paragraphs

- One point per paragraph, stated in a topic sentence that makes the paragraph's specific claim rather than naming a theme. "Results were mixed" and "We now analyze robustness" [announce](#concision); "The gain vanishes without pretraining" claims. A results paragraph may instead open with the specific question it tests, provided the next sentence answers it; the evidence follows the answer.
- Judge a paragraph by whether its point is developed and coherent, not by its sentence count. Merge a short paragraph into its neighbor only when the two share a point, and split a paragraph at the seam when its sentences support two different topic sentences.
- Transitions must carry logic (*therefore, however, because, in contrast*), and the logic must hold. A "therefore" whose premises do not entail the next sentence asserts an inference the text has not made, so flag the gap rather than keep the word.
- Do not alternate between two topics (A, B, A); finish one before starting the other. Express parallel ideas in parallel grammatical form.

**Read the topic string.** When a paragraph reads clearly sentence by sentence but does not cohere, list what opens each sentence; that list is the paragraph's topic string. When most openings are new to the passage, rewrite so that each sentence [opens with old information](#information-flow-within-a-sentence). Then test each sentence boundary by inserting, in brackets, the connective it implies ("[however]", "[therefore]"). If no connective fits, or you cannot tell which fits, the link is missing; supply it if the text states it elsewhere, and otherwise flag it. When "[therefore]" fits but the reader outside the subfield could not say why the second sentence follows, the missing link is a step, not a word, so flag the step rather than insert the connective. Finally, check that the new term in each sentence's stress position is used later, unless it is the paragraph's conclusion.

- Bad: "Contrastive pretraining needs large batches. Memory limits batch size on a single GPU. Gradient caching was proposed by Gao et al. (2021). Our method reaches the same accuracy at batch size 256."
- Good: "Contrastive pretraining needs large batches, but memory limits the batch size on a single GPU. This limit is removed by gradient caching (Gao et al., 2021), which recomputes representations in a second forward pass. Our method also removes the limit, without the second pass, and at batch size 256 it matches the accuracy of gradient caching."

If two adjacent paragraphs can swap places with no edits, either the section is a list of parallel items, which gets a [summary sentence](#concision) naming them, or the second paragraph must state what it builds on.

### Information flow within a sentence

**Old before new.** Open the sentence with material that links back to what the passage has already said: a term from an earlier sentence, or something the reader can infer from one (a part, a member, an attribute, or an alternative of it). A concept every reader in the field knows but the passage has not yet mentioned is familiar, not old. When a sentence has two old elements, open with the one mentioned more recently.

**Stress position at the end.** Readers emphasize what arrives at the point of syntactic closure, so put the new information you want remembered there ("In our experiments, adding the auxiliary loss improves accuracy by 12%", not "Accuracy improves by 12% when we add the auxiliary loss, in our experiments").

For a sentence in plain subject-verb-object order, these are principles, not rules; violate them knowingly, not by accident. A sentence that departs from that order has no such freedom, because the departure exists to put old before new. A passive with a by-phrase needs a subject at least as familiar as the by-phrase, and a fronted phrase or an inversion ("Closest to our work is X") must open with something the passage has already raised. When such a construction opens with new material, rewrite it in plain order.

- Bad: "We add a contrastive loss. A memory bank of 65k negatives is required by this loss."
- Good: "We add a contrastive loss. This loss requires a memory bank of 65k negatives."

Conversely, do not undo a passive, a "there is", or an "it ... that" sentence whose job is to move new material out of the subject.

### Sentence structure

**Character-action principle.** The grammatical subject names the actor and the verb names the action. Undo a nominalization (an action hidden in a *-tion, -ment, -ance, -ing* noun) when it moves the clause's main action into a noun behind a light verb ("perform an evaluation of", "lead to an improvement in"), or when several stack in one clause. Keep a nominalization that names a technique ("quantization"), that refers back to the previous sentence ("This reduction in memory ..."), that replaces an awkward "the fact that", or that sits alone in an otherwise clear sentence.

- Bad: "The optimization of the objective through the application of gradient descent led to an improvement in accuracy."
- Good: "We optimize the objective with gradient descent, which improves accuracy."

Keep the subject-verb pairing literal, since "the schedule launches the jobs" is active but figurative; name the true actor ("we launch the jobs on the schedule"). A component that performs the operation may be the subject ("the filter removes duplicates"); a schedule performs nothing, and a result or figure takes a [reporting verb](#the-verb-ladder) ("the results suggest"). To find hidden actions, list the paragraph's main verbs. When most are *is*, *has*, or *leads to*, the actions sit in nouns or are missing. If the passage never says what one actor does to another, flag the gap rather than supply the action.

**Make every sentence parse on the first pass.** Length alone is not the fault, so do not split a sentence only to shorten it. Find what forces a reread and fix that.

- Keep the subject next to its verb, a verb next to its object, and a verb next to the phrase it requires ("compare X with Y"). A short aside made of things the passage has already named can stay, but an interruption that brings in new material or a full clause ("the gain, once the cache is warm, disappears") moves to the front or the end, gets its own sentence, or is cut. Never nest one such interruption inside another before the main verb.
- Put the longer of two phrases last when the grammar allows either order, and move a long clause out of subject position ("It remains open whether the gain survives at larger scale"), unless the long phrase is the old one.
- Give each item that deserves emphasis its own stress position, at the end of the sentence or of a clause before a semicolon. When a sentence carries more such items than it has stress positions, split it.
- Unstack noun modifiers. More than three words before the head noun is the usual sign, so "the multi-head cross-attention key-value cache eviction policy" becomes "the policy for evicting keys and values from the multi-head cross-attention cache". A compound the field treats as one term ("large language model") counts as one word.
- Keep the small words that mark structure. A reduced relative clause reads first as a main clause ("the models trained on noisy labels degrade"), so write "the models that were trained on ..." wherever the short form can be misparsed. Keep the articles; a telegraphic sentence ("Model reaches 90% accuracy on benchmark") is a note rather than prose.
- Keep "that" after "assume", "suppose", "show", "prove", and "find" when what follows could be read as the object ("Assume that A is a group", not "Assume A is a group"). Do not add it after "we have".
- Put "only" immediately before the word it restricts. "We only evaluate on two datasets" restricts the verb; "We evaluate on only two datasets" restricts the count, which is usually what is meant.
- Put a claim's conditions before its conclusion, unless a short trailing condition is unambiguous ("unbiased under assumption A1"). When the conditions run long, give them their own sentence ("Suppose that A, B, and C hold. Then X."), and enumerate three or more steps or conditions packed into one sentence.
- Check that the sentence cannot be misread from left to right. "We prove that A and B imply C" first reads as proving A, so write "We prove that the two conditions A and B together imply C".

**No sentence-initial "And", "But", "So", or "Plus".** Do not open a sentence with "And", "But", "So", or "Plus"; the replacement must keep the relation the conjunction signaled.

- A "But" that corrects or limits the previous sentence becomes "However," or joins that sentence as ", but ...". A "But" that introduces a cited author's objection keeps the objection theirs: "Lee (2021) objects that the bound is loose", not "However, the bound is loose (Lee, 2021)".
- An "And" that adds the last item of a series becomes "Finally," or joins the series. Do not substitute "In addition", "Moreover", or "Furthermore", which mark further support for a claim rather than the next item.
- A "So" that introduces a consequence becomes "Thus," "Hence," or "Therefore," or joins the previous sentence as ", so ...". Vary the connective.

Mid-sentence coordination is correct and stays ("we expect a gain but find none").

**Read the sentence aloud.** Where the voice stalls or has to guess which word takes the stress, find the structural cause and repair the structure rather than the punctuation. This is a diagnostic, not a license for [writerly asides](#plain-wording).

### Concision

**Delete-test every clause.** For each word, phrase, and clause, ask what it adds. If the sentence keeps its meaning and stays as easy to read, the cut stands. The test cuts words that carry nothing, never words that carry a referent, a scope, a logical connection, or authorial stance.

**Say the thing, do not announce it.** A sentence that names a quantity or a category of content and then defers the content ("Three changes alter the reported accuracies, and we note each where it lands") gives the reader nothing to picture, check, or disagree with, so state the changes where the draft holds them, and otherwise flag the promise. Test it by covering the rest of the paragraph; if what remains amounts to "there are some, and they are below", the sentence is empty, and the trailing promise ("..., and we discuss each below") is cut where the draft states the content. The opposite pattern is protected: a summary sentence that states the high-level idea, or that counts items which follow at once ("We make four observations. First, ... Second, ..."). A count fails only when its items are deferred or absent.

**Policy in place of finding** puts a rule where a result belongs ("Where a conclusion depends on the choice of metric, we report both metrics"), so name the conclusions, the metrics, and what each one gives. **Empty verbs** such as *affects, varies*, and *has implications for* assert that something happened without a direction or a magnitude, so say which way and by how much; *provides, enables*, and *allows* have the same fault for mechanisms when what follows names only an outcome ("the cache enables fast retrieval"), so name the operation, or flag it when the draft does not state one. **Umbrella nouns** such as *performance* and *quality* hide which quantity was measured, so name it: accuracy, latency, peak memory, or BLEU.

**Fold self-referential signposts into the content.** Replace a sentence about the text ("The previous section analyzed the encoder. This section presents the decoder.") with the content plus the pointer ("The decoder maps each latent code produced by the encoder of Section 3 to a token sequence."). A pointer to the section that holds something ("the proof is in Appendix B") stays, as does a roadmap of at most two sentences at the end of the introduction or of the opening of a thesis chapter. Delete a signpost that names no content ("Section 7 concludes"), a roadmap inside a section that restates its subheadings, and a signpost that costs more to parse than it saves. Transitions and summary sentences are not signposts and are [protected](#protect).

**Cut intensifiers.** *very, quite, extremely, highly*, and similar add no information; give the [measurement](#plain-wording) instead. A word that softens a claim instead (*essentially, largely, somewhat, relatively*; "the gap is essentially closed") is a [hedge](#hedges), and the rules on hedges decide it. Cut *Note that* and *It is worth noting that* unless they warn the reader off a likely misreading. *obviously, clearly, trivially*, and *it is easy to see* have one legitimate use, in a derivation or proof, for a step that is routine for the reader outside the subfield; cut them on an empirical or comparative claim ("clearly outperforms"), and flag the step when it is not routine or replaces a missing argument.

### Plain wording

**Say what literally happens.** Name the actual event, object, and quantity in the words you would use at a whiteboard.

- *Figurative verbs.* A loader "retires" malformed rows, results "move", a filter "passes on" borderline examples. Write the literal event instead: the rows are deleted, the accuracy drops, the filter accepts (or rejects) them.
- *Phrasal verbs.* A verb plus a particle ("carry out", "come up with", "figure out", and similar) has several meanings its parts do not predict. Replace it with the single verb that names the operation ("run", "propose", "determine") unless it is the standard term and no single verb carries the same meaning.
- *Inflated words.* Write "use" for "utilize" or "leverage", and "try to determine" for "endeavor to ascertain".
- *Abstraction.* Metaconcept nouns (*approach, framework, strategy, issue*, and similar) wrap an idea in a container, so "we adopt a data-augmentation strategy to address the issue of overfitting" becomes "we augment the training data to reduce overfitting". Functional labels name an object by its job in the authors' setup ("the assessment word" for "the word *true* or *false*"), so name the object, then its role if the text needs it.

- Bad: "Losses above the threshold are winsorized."
- Good: "Losses above 10.0 are set to 10.0 before averaging (winsorization)."

A term of art may still be the right word; keep it and state the literal operation alongside it at first use, as in the example.

**Use the words of logic in one sense.** "Any" can mean "every" or "some", so write whichever is meant ("the bound holds for every learning rate below 1/L"). Prefer "each" with a singular noun over "all" with a plural when the plural lets the reader think the objects share one value ("each run uses its own tuned learning rate"). Merge "if A, then if B, then C" into "if A and B, then C", and keep "then" after an "if" clause whose consequent is a formula or a technical claim. Keep a negated monotonicity term negated, since "not nonincreasing" does not mean "increasing". "Contains" does not say whether something is an element or a subset, so where it matters, say which.

**Spell out definitions and procedures.** State every metric, rule, or procedure the reader must rely on in enough detail that they could recompute it, which usually takes one or two full sentences. Beside a formal definition the reader must use later, give a plain-language gloss.

- Bad: "Coverage is computed per document and averaged."
- Good: "For each document, coverage is the fraction of its reference sentences matched by at least one generated sentence; we report the mean over the 500 test documents."

**Anchor every referent.** Every pronoun, demonstrative, comparative, and shorthand noun must point to one thing the reader outside the subfield can name from the text alone. "The previous run" and "the baseline" presume context the reader lacks, so name the referent at first use ("the v1.2 measurement in Section 4.1") and reuse that name afterwards. A sentence that made sense only because of context the edit removed is a non sequitur however true it is, so keep the connecting context or flag the orphan. Readers skip headings, so the first sentence under a section title or a run-in paragraph title must make sense without it ("**Gradient caching.** Gradient caching recomputes ...", not "**Gradient caching.** This technique recomputes ...").

**Attach a noun to "this" when the referent is not unique.** When "this", "that", or "it" could point to more than one earlier noun or clause ("We prune low-magnitude weights and retrain. This improves generalization."), add a noun that names what the referent is ("This pruning step improves generalization"). A bare "this" in the fixed interpretive openers "This means that", "This is because", and "This suggests that" may stay when it follows a single clear claim.

**No writerly asides.** Conversational idiom and clipped instructions ("Call it a wash.") are essayist register. Replace them with a sentence that states the claim and its reason ("Treat this as an upper bound." becomes "This estimate is an upper bound, because the scan also counts duplicates."). A deliberately short sentence is welcome when it is complete and literal.

**Quantify comparatives.** Give the measurement rather than the comparative ("Our method runs in 0.3 s per example versus 1.1 s for the baseline (3.7× faster)", not "Our method is much faster"). Quantify judiciously, leading with the headline number, stating the pattern in words, and pointing to the table for the rest.

**Give the reasons.** Never "for various reasons" or a trailing "etc." unless the remaining items are obvious.

### Comparing with prior work

- **Compare, do not list.** Each paragraph or cluster on prior work ends by saying how this work differs, on a named dimension (an assumption, a metric, a cost, a setting, or a guarantee) and in terms the reader can check. If the draft does not state the difference, flag it rather than supplying one.
- **Characterize prior work in its own terms.** Say what a cited work does and under what assumptions before saying what it lacks for this work's setting. Do not turn a scoped difference into a defect ("ignores", "fails to") unless the draft shows the failure, and keep the sentence that credits the predecessor, which is [protected](#protect). Keep the cited work's own strength of claim; if the source says its results suggest X, do not write that it shows X.
- **Mark what is new.** When a passage mixes the text's own contribution with standard or borrowed components, the reader must be able to tell which is which ("we use the probe of Smith et al. [4]; our change is to ..."). When the text leaves the novelty ambiguous, flag it rather than deciding it.

- Bad: "Gradient caching [12] reduces memory. Memory-efficient attention [8] reduces memory. Our method reduces memory."
- Good: "Gradient caching [12] and memory-efficient attention [8] both reduce training memory, the first by recomputing representations in a second forward pass and the second by tiling the attention computation. Our method also reduces training memory but needs no second forward pass."

A comparison that is vague on both sides is the [false concession](#tolerable-patterns) pattern. Leave the related-work section where it is, and flag it only when it comes before the method and cannot be understood without it.

## Deslopping

AI-written prose falls into recognizable patterns, in two tiers.

1. **Blacklisted patterns are absolute.** Delete every instance; the co-occurrence test of tier 2 does not apply.
2. **Every other pattern is tolerable.** Fix a tolerable pattern when the fix makes the sentence better on its own terms, and rewrite a whole passage only when three or more tolerable instances co-occur in it.

**Do not over-sanitize, and never inject.** Preserve [varied rhythm](#tolerable-patterns) and genuine authorial stance, and never add a voice the draft lacks: added stance, manufactured emphasis, staccato fragments, a contrarian foil, or a specific the draft does not contain; [marking a claim's confidence to match its evidence](#claims) is calibration, not stance. Generic de-AI advice wrongly edits first-person "we", present tense for the text and prior work, and deliberately repeated terminology; the conventions on [voice](#voice-and-person), [tense](#tense), and [terminology](#terminology) govern these.

### Blacklisted patterns

**Em dashes.** Delete every em dash, including `---` in LaTeX source and an en dash (–) standing in for the same pause. Where a colon, semicolon, or pair of parentheses in the same slot passes the [pause punctuation](#tolerable-patterns) test, substitute it; otherwise rebuild the sentence so that it needs no pause. The en dash is correct in a numeric range and a name joined from two people ("Sections 3–5", "Kullback–Leibler divergence"; `--` in source), so sweep `--` only where it is neither. Hyphens in compounds stay.

**Chatbot artifacts.** Delete "Certainly!", "Great question", "I hope this helps", "As of my last update", and similar.

**Generic openings and closings.** A sentence that could be prepended to any text in the field ("In the ever-evolving field of deep learning", "The future looks bright") is bloat, and the defensible-sounding forms count too ("There has been much recent interest in X"). Delete it, which [needs no request](#cutting), and where the draft states the reason X matters, put that reason in its place.

**Leaked generation artifacts.** Chat-UI citation tokens (`citeturn0search0`, `contentReference[oaicite:...]`), AI-referrer URL parameters (`utm_source=chatgpt.com`), and unfilled template placeholders ("[Your Name]", "[Insert citation]") are residue of an unedited paste; strip every one, keep the sentence it sat in, and flag what each placeholder stood for so the author can supply it.

### Tolerable patterns

**Patterns with a prose rule.** Scan for these and apply the linked rule: an [ornate word where a plain one exists](#plain-wording) (*delve, underscore, showcase, pivotal*, and similar), unless it is the precise word; a clause that [stacks nominalizations](#sentence-structure); a [count and a promise in place of the items](#concision); and the shortest fluent wording chosen over the plainest.

**Pause punctuation.** The pattern is an assertion too vague to say anything alone ("Retrieval itself helps"), then a colon or semicolon, then a full sentence of evidence with no grammatical link to it, and it is a fault whether or not an em dash was ever there. Subordinate one half into the other ("..., as shown by Vasquez (2024), who reports ...") rather than swapping the mark for a period, and cut a left half that asserts nothing the right half does not carry. The test is the left half read alone; a left half that states a specific fact keeps the mark, as do a list colon, a colon that introduces a display, a quoted definition, or a label, and a semicolon between two specific facts.

Once the colons are gone, the same pattern appears as a trailing comma phrase with its verb deleted ("adds 0.9M parameters, under 0.002% of the backbone"), so put the verb back ("which is under"); an appositive, a participial adjunct, or a parallel elaboration that elides a stated verb ("the first by ..., the second by ...") stays. Count instances across the passage before deciding on a passage-wide rewrite; three in a passage is a habit.

**Reasoning-chain leakage.** "Let us think step by step", "Breaking this down", and numbered pseudo-monologue narrate the author's own thinking. State the conclusion, then the evidence. Mathematical setup ("Let X be", "Consider a graph G") is standard register and stays.

**Diff-anchored prose.** The text narrates the revision instead of the current state ("In this revised version, we now clarify", "As suggested by the reviewer, we have added"). That belongs in a response letter or a change log, so say what the method does.

**Vague attribution.** "Studies show", "experts believe", and the agentless passive ("X has been shown to") attribute a claim to no one. Where the draft cites the source nearby, name it ("Smith et al. (2020) report that X"); otherwise flag the claim.

**Negative parallelism.** "It is not just an optimizer, it is a paradigm shift" and "not only faster but also more accurate" negate a foil to inflate the claim, and the pattern survives splitting into separate sentences ("The headline is not the speedup. The real story is ..."). State the positive claim directly, with numbers; a contrast that excludes a real alternative ("we measure X, not Y") is fine.

**False concession.** "While X has made significant strides, Y remains a challenge" states no specific comparison. Name both sides; a concession whose halves are both specific stays ("the gain holds on the two smaller benchmarks but not the largest").

**Reflexive rule-of-three.** Triads like "faster, cheaper, and more robust" are forced for rhythm rather than written because there are three items. Genuine three-element lists stay.

**False ranges.** A "from X to Y" whose endpoints bound nothing ("tasks ranging from image classification to reinforcement learning") manufactures breadth. Name the settings tested; a range over a real ordered axis ("from 10² to 10⁶ parameters") stays.

**Transition chains.** When *Moreover, Furthermore, Additionally* stacked at paragraph heads merely announce more text, delete them and let order do the work. Keep those that mark a [real logical relation](#paragraphs).

**Copula avoidance.** "serves as", "acts as", "represents", "boasts", and similar stand where "is" or "has" belongs. Write "is" or "has", or the verb the noun hides ("serves as a feature extractor" becomes "extracts features"). An "acts as" that claims a function, not an identity ("acts as a regularizer"), stays.

**Trailing "-ing" pseudo-analysis.** Delete a trailing participial clause that adds no checkable claim ("..., highlighting its importance, reflecting broader trends"), or rewrite it as a specific claim the draft supports.

**Self-labeling significance.** The text points back at its own material to tag which part matters ("This last result is the surprising one"). Restructure until the item carries its own weight and cut the label; a frame phrase that carries authorial stance as the claim arrives ("Interestingly,") stays.

**Rhetorical questions as transitions.** "But how well does this scale?" pivots between paragraphs. State the answer as the topic sentence instead; research questions the text then answers ("RQ1: ...") stay.

**Uniform rhythm.** Every sentence runs 15 to 25 words and every paragraph has the same shape. Vary length, but only with sentences that stay complete and literal, never with [writerly asides](#plain-wording).

**Significance inflation.** An ordinary detail is tied to a grand trend ("marking a pivotal moment", "paving the way"). Delete the phrase, or replace it with the specific, scoped implication the draft states.

**Aphorism formulas.** "X is the Y of Z" ("attention is the currency of deep learning") asserts a resemblance in place of a mechanism. Give the mechanism.

**Relentless positivity and sycophantic framing.** Every result is framed as a triumph. Give failures comparable prominence to successes, and [calibrate both to the evidence](#claims).

## Conventions

These conventions override generic writing advice.

### Voice and person

- Default to active voice with first-person "we" for the authors' actions and decisions. In derivations and proofs, "we" may also mean the author and reader together.
- Pick one agent for the steps of a method or algorithm, either the method ("the algorithm refines the estimate") or "we" ("we refine the estimate"), and keep it for the whole description. The authors' choices about the method ("we set k = 5") always take "we".
- Cut indirection. Where the text does what follows, "We can compute X" becomes "We compute X", and "aims to" and "seeks to" become the verb itself; a capability the text does not exercise, or a goal marked as unattained, keeps its wording, since changing it would [change the claim](#claims). The ungrammatical "allows to model" becomes "models" or "allows us to model", whichever the draft means.
- Passive voice is legitimate where the agent is obvious or irrelevant ("Images are normalized to zero mean"), where it keeps [old information in the subject position](#information-flow-within-a-sentence), and where it moves a long agent to the end.
- In single-authored writing, keep the author's choice of "I" or "we" and apply it consistently. Do not change "we" to "I".

### Tense

Present tense for the text's contents ("Section 4 shows", not "we will show"), its results, its method and setup ("we train for 10 epochs"), established facts, and prior work that lives on ("Smith et al. propose"). Past tense for events at a specific time outside the described procedure ("we collected 500 documents in 2024"); where the draft uses past tense for its experiments consistently, keep it. Future tense only for work the text plans and has not done, as in a proposal. Within a paragraph, keep one tense for one subject when the time frame is unchanged. Prefer the simple tense to the perfect ("Smith et al. show", or "showed", not "have shown"), and keep the perfect only where current relevance is the point ("no prior work has evaluated X at this scale").

### Terminology

Same concept, same word, everywhere. No elegant variation, that is, no cycling through synonyms ("network", "model", "architecture", "system"). Vary sentence structure and function words, never technical terms. To find variation, list every word the text uses for each of its most frequent concepts; more than one entry per concept is the error unless the text defines them as different things. When a later passage treats a parallel or more general case, reuse the earlier wording word for word and then state the difference.

Where the text lets you, give each technical term one part of speech. "Sample", "estimate", and "model" all serve as noun and verb, and a sentence that uses one in both roles ("we sample 1,000 samples") makes the reader resolve each occurrence. Where the text needs both roles, keep them out of the same sentence ("we draw 1,000 samples").

Spell out an acronym at first use, and again at the start of each major section or chapter where it reappears; an abstract does not count as first use. Do not coin an acronym for a term the reader meets only once or twice, and prefer the spelled-out term unless the acronym is standard in the field or replaces a long multi-word name the text uses throughout. Spell out an acronym that saves no syllables when read aloud ("BS" for batch size) and one with a second common expansion in the field ("LR"). Where the acronym also appears in tables or figures, flag the change rather than leave prose and floats inconsistent.

**Refresh long-lived shorthand.** When a shorthand returns after a gap or at a section boundary, re-anchor it to its definition ("the graph-search step (Dijkstra's algorithm)", "the contrastive loss L_c defined in Section 3"). The risk is highest when the shorthand's surface form is generic ("search" for Dijkstra's algorithm, "the loss" in a text that defined three). Refresh with the same term plus its anchor, never with a synonym, and make the reminder read as a reminder.

Watch for suggestive, overloaded, and suitcase terms. A suggestive coinage gives a technical object a name with a colloquial meaning ("thought vector", "the model understands"). An overloaded term bends a precise meaning from elsewhere ("deconvolution" for transposed convolution). A suitcase word packs several meanings ("generalization" can mean train-to-test performance, transfer, or validity outside the experiment), so state which is meant. When the text coins the term itself, flag it and suggest a literal name; when the term is established in the field ("curiosity" as an intrinsic reward), keep it and gloss the literal operation at first use. "The network learns features" is accepted shorthand; "the model tries to reason" is not, because intention belongs to the authors ("we train the model to").

### Citation markers are not nouns

A bracketed or parenthetical citation marker is not a noun, so it is never the subject or object of a sentence; the author name is a noun and may be either.

- Bad: "[10] was the first..." / "(Smith, 2001) shows that..."
- Good: "Smith et al. [10] were the first..." / "Widgets reduce latency (Smith, 2001)." / "Smith (2001) shows that..."

In LaTeX, use `\citet` for textual citations and `\citep` for parenthetical ones, with a non-breaking space before the citation (`widgets~\citep{smith2001}`). "et al." is only for three or more authors; the period goes on "al." only, and it is not italicized.

Move a citation out of a lead-in when the sentence states an established result the text relies on ("In a recent study, Smith et al. (2015) showed that X" becomes "X (Smith et al., 2015)"). Keep the authors as the subject when the sentence characterizes, contrasts, or reports a claim of theirs that the text does not itself assert.

### Notation and equations

- Define each symbol at or before its first use, at least informally, and [refresh it on reuse](#terminology) ("the sample space 𝒳", not bare "𝒳" pages later).
- If the text already has a Preliminaries or Notation section, global notation belongs there; move a definition there only when the request [allows relocation](#cutting), and flag it otherwise. Do not create such a section (that reorders the text); flag the scattered definitions instead.
- Introduce no symbol the text does not use again ("Every continuous function on a compact set is bounded" needs no "f"). Do not give one symbol two meanings, or one object two symbols. If L(θ) is the training loss, do not write "L = 0.31" for its final value; write "L(θ_T) = 0.31".
- Never start a sentence or a clause with a symbol ("A function f is semicontinuous if...", not "f is semicontinuous if..."), and spell out a number that starts a sentence. Separate symbols in adjacent formulas with words ("Consider S_q, where q < p").
- In running prose, write "for all", "there exists", and "implies", not ∀, ∃, and ⇒, except in work on logic, and do not use a relation symbol as a word inside a verbal phrase ("the step size is at most 0.1", not "is ≤ 0.1").
- Set multi-letter operators and word subscripts upright (`\log`, `\operatorname{softmax}`, `\mathcal{L}_{\text{train}}`). A subscript that is itself a variable stays italic (`x_i`).
- Equations are parts of sentences. "=" is the verb, a displayed equation ending a sentence takes a period, and one continuing takes a comma. Put no colon before a display that completes the sentence ("the loss is", not "the loss is:"); a colon is correct after a complete clause ("we define the loss as follows:"). In LaTeX source, leave no blank line before or after a display that continues the paragraph.
- A trailing "where" that glosses the symbols of a display is the convention ("..., where λ controls the trade-off"). A trailing "where" that defines a term the claim depends on ("Every convex polynomial has even degree, where a function is convex if ...") moves ahead of the claim. Inside a theorem statement, define each symbol before using it.
- Replace every non-trivial formula with "blah" and reread. The prose must still read as sentences.
- Number every display the text refers to, and the text's central displays (the objective, the update rule, the main bound) even when the text does not. Leave intermediate steps unnumbered.
- The sentence before a theorem, lemma, or algorithm is complete or ends in a colon. The statement is self-contained, naming its objects ("The function H defined in (5) is continuous"), and holds no motivation or commentary. When the hypotheses run past a few lines, flag the statement and suggest named conditions defined before the theorem ("Assumption 1 (smoothness)").
- Open a proof by naming its strategy ("We prove the claim by induction on t"), and mark subgoals as they are met. The reader must always know whether each statement is assumed, proved, or claimed with its proof deferred.

### Figures and tables

- **Captions.** A caption lets a reader who has skipped to the figure read it correctly. State what is plotted or tabulated (the quantities, their units where applicable, the axes of a plot, and whether higher or lower is better when that is not obvious), under what conditions (dataset, model, setting), what each visual encoding denotes (line styles, colors, shaded regions, and [error bars](#uncertainty-and-significance)), and the one point the figure exists to show. A caption that names the figure and stops ("Results on ImageNet.") is incomplete; complete it from the paragraph that references the figure, in the same wording, and flag it when the draft holds the facts nowhere. Check that the caption and the body text describe the figure the same way.
- **References in text.** Every float is referenced in the sentence that makes its claim, and that sentence states the claim ("Accuracy falls as the noise rate rises (Figure 6)" or "Figure 6 shows that accuracy falls as the noise rate rises", not "In Figure 6 we show the results"). When the claim rests on a value the reader could only estimate from the plot, the number belongs in the sentence or the caption; if neither gives it, flag it. Write `Figure~\ref{...}` with a non-breaking space, and capitalize "Figure 6", "Table 2", "Section 4", and "Theorem 1". In LaTeX source, `\label` goes after `\caption`. A "?" or "??" in rendered text marks an undefined `\cite` or `\ref`, so flag each one.

- Bad caption: "Figure 3: Ablation results."
- Good caption: "Figure 3: Top-1 accuracy (%) of ResNet-50 on ImageNet-1k when each component is removed, mean ± standard deviation over three seeds. Removing the auxiliary loss causes the largest drop."

### Typography and small style

- Hyphenate compound modifiers before nouns ("real-time inference", "three-layer network"); the predicate form takes no hyphens ("inference runs in real time"). An established term of the field stays open when the draft writes it open consistently ("a large language model").
- Spell out a small count used as an adjective in running prose ("two passes"). Keep numerals for measured quantities, hyperparameter values even when small ("10 epochs"), anything with a unit ("batch size 256", "0.3 s"), and a value or a name ("when k is 2", "Method 2"). Where the draft or its style guide applies a different cutoff consistently, keep it.
- "i.e." means that is and "e.g." means for example; never interchange them. Comma after both in US style, and neither is italicized. "cf." means compare, not see.
- Commas mark a non-restrictive clause ("the encoder, which has 12 layers, ..."), so check that they match the intended meaning. The commas carry the distinction, not the choice between "which" and "that", so leave restrictive "which" alone unless the governing style guide requires "that". A symbol that names the noun before it takes no commas ("a directed graph G with source s").
- No contractions, exclamation marks, emoji, or Title Case Headings beyond the governing style guide. Italics mark definitions, not emphasis. Quotation marks are for quoted text, a word mentioned as a word, and a term the authors use without endorsing it (the model's "reasoning"), which then needs a statement of what it refers to; no scare quotes around ordinary words.
- Write × (`$\times$`) for multiplication and speedup factors, not the letter x or *, and a minus sign (`$-0.3$`), not a hyphen, for negative numbers. Separate a number from its unit with a non-breaking space (`0.3~s`).
- Give units for measured quantities and axes where applicable. Consistent US or UK spelling throughout. Where the draft mixes two acceptable forms ("dataset" and "data set"), standardize on the form the draft uses most unless the style guide specifies one.
