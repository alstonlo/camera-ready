# Writing guide

Apply the five sections in this order:

- [Claims](#claims): match each claim to its evidence by checking the reporting verb, scope, causal language, significance, hedges, over- and underclaiming, speculation, and limitations.
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

For a request narrower than a polish, also apply every rule linked from the listed sections. Check each chunk against every rule in the applicable section. If two rules prescribe different edits for one sentence and one links to the other, follow the linked rule. Otherwise choose the clearer sentence; if both are equally clear, use your judgment as an expert editor.

## Claims

Every claim must match its evidence. Both overclaiming and underclaiming are errors. An aspirational goal may motivate the text if the text states that the goal remains unattained.

### The verb ladder

Choose the reporting verb that the evidence supports, regardless of enthusiasm for the result.

| Verb | Evidence required |
|---|---|
| we **prove** | a theorem with stated assumptions, and nothing else |
| we **show / demonstrate / establish** | direct evidence that rules out the plausible alternatives |
| we **find / observe / report** | a directly measured empirical result |
| results **suggest / indicate**; we **hypothesize / conjecture** | an inference or interpretation that could reasonably be wrong |

A benchmark result never proves a mechanism. A figure or table "shows" only what it displays; choose the verb for a claim inferred from it according to the evidence for that claim.

A claim hedged in the results must retain its hedge in the abstract, introduction, conclusion, and any other summary. For each claim in a summary, find the supporting result. If the draft contains that result but the claim lacks a reference to it, add one ("(Section 5)", "(Table 2)"). If no support exists, flag the claim.

### Scope

Evidence determines both a claim's scope and its confidence (plain or hedged). From broadest to narrowest, scope ranges from a guarantee ("X always holds"), through a systematic claim ("X generally happens across contexts") and a narrow claim ("X is best for settings V and W"), to an existence claim ("we find one case where X"). Choose the broadest scope and the most direct statement of confidence the evidence supports. When support is uncertain, leave the claim in place and flag it. This caution does not justify hedging or dropping a claim that the evidence does support; doing so would be [underclaiming](#failure-modes).

Limit every headline claim to its conditions, datasets, and settings. Absolutes ("always", "unique") extend a claim to untested cases. A bare generic plural claims the whole class, so "Transformers fail to retrieve early tokens" asserts it of every Transformer. When the evidence covers only the models tested, write "the four Transformers we test fail to retrieve early tokens".

A result reported without a comparison supports "X works", not "X is better" or "X is practical". Flag the missing baseline when the draft claims more. A qualitative example (a generated sample, a saliency map, a case study) supports only an existence claim. If the text offers it as evidence for a broader claim, it must say how the example was chosen (at random, as typical, or as the best case). Flag any missing account of that choice.

### Causal language

Use "causes", "leads to", "improves because", and other wording that credits a design choice only when the evidence supports causation, as an ablation that isolates the component does. Describe correlational results with "is associated with", "correlates with", or "coincides with". When the text introduces several changes together without isolating any, it may credit the combination but no single change. It must not imply that every change is necessary.

### Formal and informal claims

Make clear whether each claim is formal or informal. A sentence that reads like a theorem ("all local minima have error close to that of the global minimum") but cites no result and states no conditions leaves its status unclear. Link it to a stated result with its assumptions, rewrite it as the empirical or intuitive claim it is, or flag it if the draft supports neither. When the text invokes a theorem to support an empirical claim, check that the theorem's conclusion applies under the text's conditions. Flag a link that does not hold, such as a convergence result for convex objectives used to support a claim about non-convex training.

### Uncertainty and significance

A comparison between two numbers is a claim whose evidence includes their variability. For every reported comparison, the sentence, caption, or a convention stated once in the text must specify:

- How many runs each number covers and how it summarizes them (mean, median, or best run).
- Whether ± denotes a standard deviation, standard error, or confidence interval.
- What varies (seed, data split, or the test examples a bootstrap resamples).

Flag any missing information.

- Bad: "Our method significantly outperforms the baseline (71.2 ± 0.4 vs 68.4 ± 0.6)."
- Good: "Our method outperforms the baseline by 2.8 points (71.2 ± 0.4 vs 68.4 ± 0.6; mean ± standard deviation over five seeds)."

Both sides of a comparison must be computed the same way. A best-run number is not comparable with a mean of final results; a number copied from another publication is comparable only under the same evaluation protocol. Flag every comparison for which the text does not establish that both sides were computed alike.

Reserve "significant(ly)" for results of a named statistical test. Pair the test with its p-value or significance level and, if the draft reports it, its effect size. If the word means large or important, replace it with the magnitude. If it claims statistical significance without naming a test, flag it. When the draft tests significance on several datasets or metrics, flag any missing explanation of how it corrects for multiple comparisons.

Failure to reject a hypothesis of no difference does not establish equality. Replace "the two methods perform the same (paired bootstrap, p = 0.21)" with "we find no significant difference between the two methods (paired bootstrap, p = 0.21)". When intervals overlap and the text names no test, flag any claim of superiority. Overlap alone establishes neither superiority nor its absence. When the ranking of methods changes with the aggregate metric, limit each claim to the metric that produced it.

### Hedges

Hedge the interpretation of a measurement, including a proposed mechanism, and leave the measurement itself unhedged.

- Bad: "Accuracy appears to drop by roughly 4.2 points when we remove the auxiliary loss, which shows the loss is a regularizer."
- Good: "Accuracy drops 4.2 points when we remove the auxiliary loss (Table 3), which suggests the loss acts as a regularizer."

Describe procedures without hedges, whether in a Methods section or elsewhere. Only the rationale for a choice may be hedged. In Results, Discussion, and Conclusion sections, and in any other passage that interprets a measurement, preserve this distinction between measurement and interpretation. An abstract or other summary may compress a claim but must retain its strength on the [verb ladder](#the-verb-ladder) and its hedge.

Use at most one hedge per claim, in a standard academic form ("may", "likely", "suggests", "appears to"). Softeners ("somewhat", "relatively", "essentially", and similar) weaken a claim without saying where it fails. If the draft states the condition under which the claim fails or the size of the effect, replace the softener with that information. Otherwise keep it and flag it, since deleting a claim's only hedge strengthens the claim. These softeners differ from [intensifiers](#concision), which are simply cut. A qualifier whose deletion changes what is claimed ("usually", "on average", "in most runs") is a scope condition, not a hedge, and is [protected](#protect).

- Bad: "Our method is relatively robust to label noise."
- Good: "Our method loses 2 points of accuracy at 20% label noise, against 9 points for the baseline."

### Failure modes

**Overclaiming.** The following are banned for empirical results: *solves, proves, optimal, guarantees, first to* (unless the draft verifies the claim), unsupported superlatives, "human-level" or "state-of-the-art" without naming the task, benchmark, and metric, and "novel" as filler.

**Underclaiming.** State contributions plainly and completely, without weakening a real result through reflexive hedging. Each item in a "Contributions" list must state a claim the reader can check and refer to its support where the draft provides it. An item that only says *study, explore, investigate, describe*, or *discuss* states no claim. Rewrite it using the findings in the corresponding section, or flag it.

- Bad: "We study the theoretical properties of the estimator."
- Good: "We prove that the estimator is unbiased under assumption A1 (Section 4)."

### Speculation

Never state speculation in the grammatical form of established fact. Mark it with "We conjecture" or "One possible explanation is", or confine it to a Motivation or Discussion paragraph that the text marks, as a whole, as speculation.

An explanation based on an undefined term is speculation, however it is phrased. The claim "The gain comes from reduced internal covariate shift" cannot be checked until the text states how the shift is measured. Flag the term or mark the sentence as a hypothesis. A bare negative claim ("X does not imply Y") needs a counterexample, a reference, or a statement that the question is open. Flag the claim if the draft provides none.

### Limitations

State each limitation once and precisely, without apology. Flag a decoy limitation that hides the real weakness, and cut a duplicate only when a length request reaches it in the [triage order](#triage-order). Explain how each limitation affects the findings ("results may not transfer to larger models, since every run uses the same 100M-parameter backbone"). A limitation phrased as future work must still say what the current results do not cover.

## Cutting

Use the [spine test](#the-spine-test) to determine what the text needs and the request to determine what you may delete or relocate.

**Delete bloat without asking.** Bloat includes [blacklisted patterns](#blacklisted-patterns), sentences that announce content instead of stating it, and signposts that the [concision rules](#concision) require you to delete. Tightening the wording of a surviving sentence also needs no permission.

**Idea-level cutting needs the author's request.** Cut or relocate ideas only when requested ("cut this to eight pages", "condense", or a hard length limit). Otherwise identify the candidate and leave it in place ("this paragraph is off-spine; cut it?"). This requirement covers every sentence containing something the author would miss: an idea, a result, a caveat, evidence, or a transition the argument needs. Reordering within a section to [build understanding early](#build-understanding-early) is a prose edit. Moving content between sections or out of the main text is relocation.

### The spine test

State the text's core claims in one to three sentences. These claims form the spine of the text. For each paragraph, write one line explaining how it supports them. Keep content according to **whether the spine needs it**; truth or interest alone is insufficient. If you cannot give a section a short, specific title, it probably makes more than one point. Flag it before cutting within it. A cut is justified only if the argument reads at least as clearly without the content.

Review paragraphs before sentences. Tag each paragraph *central*, *supporting*, *ancillary*, or *off-spine*. As far as the request allows, cut or relocate paragraphs that are off-spine and trim ancillary ones. Then edit the surviving paragraphs [sentence by sentence](#sentence-by-sentence).

### Triage order

Under a length constraint, cut in this order, most expendable first.

1. **Repeated restatement.** Cut repetitions of the same point in the introduction, section or chapter opening, and conclusion. Keep the instance that contributes most to the argument, usually in the section that develops the point. Preserve two kinds of repetition: one restatement of each contribution in the abstract, introduction, and conclusion, and a deliberate reminder that [refreshes a shorthand](#terminology) defined pages earlier. Even a permitted restatement must not be a copy. If a conclusion sentence repeats the abstract word for word, revise it with the specifics established by the results, or flag it.
2. **Signposting that survives the bloat pass.** This includes the two-sentence roadmap allowed by the [rule on combining signposts with content](#concision). Preserve references to a claim's support or to the location of a proof; these are not signposting.
3. **Tangential background and related work.** Cut material that does not motivate the text's question. A citation list that states no relation to the gap the text fills is expendable; the two or three works that define the gap are not.
4. **Minor results, secondary analyses, and exploratory findings.** Remove a result from the main text if it advances no central claim. Relocate material that supports rigor: sensitivity analyses, robustness checks, and the negative result a skeptical reviewer will ask about. Accounts of what the authors tried first also belong in this tier. A failed alternative stays in the main text only as a stated negative result.
5. **Exhaustive parameter and implementation detail.** Keep enough detail in the main text to make the work reproducible in outline, including its [spelled-out procedures](#plain-wording) and [protected content](#protect). Move the full sweep to the appendix.

### Protect

Some sentences add no new information, but the argument depends on them. Preserve the following content, relocating only as the [sentence-by-sentence pass](#sentence-by-sentence) allows:

- **Hedges, qualifiers, scope conditions, and limitations.** Deleting "these results come from a single dataset and may not generalize" silently strengthens every subsequent claim. Handle a repeated limitation stated in full elsewhere according to the [triage order](#triage-order). Cutting a caveat is a [claims edit](#claims). If a length request requires such a cut, recalibrate the surviving claim [after the pass](#after-the-pass).
- **The evidence that supports a claim.** Cutting the supporting number or example while keeping the confident assertion leaves the claim unsupported.
- **Framing, orienting, and summary sentences.** When cutting a minor result, usually keep the sentence explaining why this class of question matters; it now frames the surviving results. Also keep a summary sentence that [states the high-level idea](#concision) before the specifics.
- **Caption content that repeats the body text.** Readers use captions independently of the body, so this repetition is necessary. Tighten a caption's wording while preserving its [required content](#figures-and-tables).
- **Genuine transitions and back-references.** A transition that [carries logic](#paragraphs) stays, as does a back-reference a later sentence depends on.
- **Topic sentences.** Cutting a paragraph's topic sentence leaves it incomplete.
- **Reproducibility content.** Preserve the statistical tests used, the handling of missing data and multiple comparisons, and enough detail about the method for the reader outside the subfield to judge the study.
- **Fair characterization of prior work.** Preserve sentences that credit a predecessor or accurately state what they did.

### Sentence by sentence

For each sentence in a surviving paragraph, ask these questions in order:

1. **Does the spine need it?** If the sentence supports no central claim, consider deleting or relocating it according to steps 2 to 4.
2. **Does the reader need it?** A sentence can add no new claim and still be [protected](#protect) because it frames the argument, connects ideas, calibrates a claim, or orients the reader.
3. **What breaks without it?** Check later passages for dependencies: a later "this" or "as shown above", a citation or term that appears only here, a claim whose hedge or evidence is in this sentence, or the paragraph's topic string. Repair every dependency in the same edit or keep the sentence.
4. **Delete or relocate?** Delete content that no reader needs. Relocate it to an appendix, supplement, or footnote when only a minority of readers, or one skeptical reviewer, needs it. Reproducibility content is [protected](#protect): relocate it, never delete it. Use an appendix or supplement only if it already exists; otherwise leave the content in place and flag what the appendix or supplement would need to contain. A footnote may be new.
5. **Read across the gap.** Read the sentences before and after the gap together. The second must open with a term, result, or referent supplied by the first. If the link requires an inference that the deleted sentence made, add a clause to an adjacent sentence to restore it, or reuse the original framing sentence to open what follows.

- Before: "We also sweep the learning rate over five values; 3e-4 is best. We use it for all remaining experiments."
- Bad: "We use it for all remaining experiments." ("it" now points at nothing.)
- Good: "We use a learning rate of 3e-4 for all remaining experiments (sweep in Appendix B)."

### Stop rules

Revise a cut when any of these three conditions applies:

- **The cut leaves the paragraph underdeveloped or breaks its topic string.** Merge the paragraph with an adjacent one that makes the same point. Otherwise restore the missing development or repair the [topic string](#paragraphs).
- **You are cutting because the passage confuses you.** Identify the cause first. Confusion usually indicates a missing step rather than an unnecessary one. Supply the [missing step or referent](#plain-wording) if the draft states it elsewhere; otherwise flag it.
- **The reader outside the subfield can no longer follow the condensed version.** Restore the framing and steps that reader needs instead of cutting further.

### After the pass

- **Claims calibration.** Confirm that every surviving claim retains its hedging and evidence, and apply the [verb ladder](#the-verb-ladder) to the shortened text. If a claim's support moved to the appendix, add a reference to it. Weaken the claim only if the surviving evidence supports less.
- **Narrative arc and pointers.** Read the whole text. The argument must still connect the problem, gap, approach, findings, and implications without requiring the reader to reconstruct deleted links. Check for dangling references, uncited figures and tables, references to nonexistent appendix material, and terms now used before their first definition.

## Prose

### Build understanding early

At any point in the text, the reader should understand as much as the preceding material could have explained.

Present the main ideas before the details:

- The high-level idea precedes the detailed mechanism.
- The result and its interpretation precede the supporting evidence.
- State the paragraph's claim in its first sentence. A results paragraph may state it in the second sentence, after the [question it answers](#paragraphs). State the section's claim in its first paragraph.
- A definition precedes its first use, and context precedes anything new that depends on it.

Test the order by covering everything after a given sentence and asking what the reader knows so far. If a covered sentence would explain more than an uncovered one, move it earlier. Apply this rule to paragraphs within a section and sentences within a paragraph. Within a sentence, put new information last, in the [stress position](#information-flow-within-a-sentence).

### Paragraphs

- Make one point per paragraph, stated as a specific claim in its topic sentence. "Results were mixed" and "We now analyze robustness" [announce](#concision) a theme; "The gain vanishes without pretraining" states a claim. A results paragraph may instead open with the specific question it tests, provided the next sentence answers it. Put the evidence after the answer.
- Judge a paragraph by whether its point is developed and coherent, regardless of its sentence count. Merge a short paragraph with an adjacent one only when they make the same point. Split a paragraph where its sentences begin to support a different topic sentence.
- Use transitions that express a valid logical relation (*therefore, however, because, in contrast*). If the premises before "therefore" do not entail the next sentence, flag the missing inference rather than keep the word.
- Do not alternate between two topics (A, B, A); finish one before starting the other. Express parallel ideas in parallel grammatical form.

**Read the topic string.** When individual sentences are clear but the paragraph does not cohere, list the opening of each sentence. This list is the paragraph's topic string. If most openings introduce new material, rewrite so that each sentence [opens with old information](#information-flow-within-a-sentence). Then test each sentence boundary by inserting the implied connective in brackets ("[however]", "[therefore]"). If no connective fits, or you cannot determine which fits, the link is missing. Supply it if the text states it elsewhere; otherwise flag it. If "[therefore]" fits but the reader outside the subfield could not explain why the second sentence follows, flag the missing step in the argument. Inserting the connective cannot supply that step. Finally, check that each new term in a sentence's stress position is used later, unless it is the paragraph's conclusion.

- Bad: "Contrastive pretraining needs large batches. Memory limits batch size on a single GPU. Gradient caching was proposed by Gao et al. (2021). Our method reaches the same accuracy at batch size 256."
- Good: "Contrastive pretraining needs large batches, but memory limits the batch size on a single GPU. This limit is removed by gradient caching (Gao et al., 2021), which recomputes representations in a second forward pass. Our method also removes the limit, without the second pass, and at batch size 256 it matches the accuracy of gradient caching."

If two adjacent paragraphs can exchange places without further edits, determine whether the section lists parallel items. If so, add a [summary sentence](#concision) naming them. Otherwise revise the second paragraph to state how it depends on the first.

### Information flow within a sentence

**Old before new.** Open each sentence with material that connects to the preceding text: a term from an earlier sentence or something the reader can infer from it, such as a part, member, attribute, or alternative. A concept is not old information merely because readers in the field know it. When a sentence has two old elements, open with the one mentioned more recently.

**Stress position at the end.** Readers give emphasis to the end of a complete clause or sentence. Put the new information you want them to remember there ("In our experiments, adding the auxiliary loss improves accuracy by 12%", not "Accuracy improves by 12% when we add the auxiliary loss, in our experiments").

In a sentence with ordinary subject-verb-object order, you may depart from these principles deliberately. Other sentence orders must put old information before new. A passive with a by-phrase needs a subject at least as familiar as the by-phrase. A fronted phrase or an inversion ("Closest to our work is X") must open with something the passage has already mentioned. If such a construction opens with new material, rewrite it in ordinary subject-verb-object order.

- Bad: "We add a contrastive loss. A memory bank of 65k negatives is required by this loss."
- Good: "We add a contrastive loss. This loss requires a memory bank of 65k negatives."

Preserve a passive, a "there is", or an "it ... that" sentence when it keeps new material out of the subject position.

### Sentence structure

**Character-action principle.** Use the grammatical subject to name the actor and the verb to name the action. A nominalization expresses an action as a noun, often ending in *-tion, -ment, -ance,* or *-ing*. Rewrite it as a verb when it expresses the clause's main action after a verb with little meaning of its own ("perform an evaluation of", "lead to an improvement in"), or when several nominalizations occur together in one clause. Keep a nominalization that names a technique ("quantization"), refers to the previous sentence ("This reduction in memory ..."), replaces an awkward "the fact that", or appears alone in an otherwise clear sentence.

- Bad: "The optimization of the objective through the application of gradient descent led to an improvement in accuracy."
- Good: "We optimize the objective with gradient descent, which improves accuracy."

Keep the subject-verb pairing literal. The active but figurative "the schedule launches the jobs" needs the actual actor ("we launch the jobs on the schedule"). A component that performs the operation may be the subject ("the filter removes duplicates"); a schedule performs no operation. Use a [reporting verb](#the-verb-ladder) for a result or figure ("the results suggest"). To find actions expressed as nouns or left unstated, list the paragraph's main verbs. If most are *is*, *has*, or *leads to*, the actions are in nouns or missing. If the passage never says what one actor does to another, flag the missing action.

**Make every sentence clear on the first reading.** Identify and fix what forces the reader to reread. Do not split a sentence solely to shorten it.

- Keep the subject next to its verb, a verb next to its object, and a verb next to the phrase it requires ("compare X with Y"). A short aside containing only previously mentioned material may stay. If an interruption introduces new material or a full clause ("the gain, once the cache is warm, disappears"), move it to the beginning or end, make it a separate sentence, or cut it. Never nest one such interruption inside another before the main verb.
- When grammar allows either order, put the longer of two phrases last, unless it contains the old information. Likewise, move a long clause out of the subject position ("It remains open whether the gain survives at larger scale"), unless it contains the old information.
- Give each item that deserves emphasis its own stress position, at the end of a sentence or of a clause before a semicolon. Split a sentence if it has more items to emphasize than stress positions.
- Separate long sequences of noun modifiers, usually those with more than three words before the head noun. For example, "the multi-head cross-attention key-value cache eviction policy" becomes "the policy for evicting keys and values from the multi-head cross-attention cache". Count a compound the field treats as one term ("large language model") as one word.
- Keep small words that clarify structure. A reduced relative clause can initially read as a main clause ("the models trained on noisy labels degrade"). Write "the models that were trained on ..." wherever the shorter form permits this misreading. Keep articles so that sentences read as prose rather than notes ("Model reaches 90% accuracy on benchmark").
- Keep "that" after "assume", "suppose", "show", "prove", and "find" when what follows could be read as the object ("Assume that A is a group", not "Assume A is a group"). Do not add it after "we have".
- Put "only" immediately before the word it restricts. "We only evaluate on two datasets" restricts the verb; "We evaluate on only two datasets" restricts the count, which is usually what is meant.
- Put a claim's conditions before its conclusion, unless a short trailing condition is unambiguous ("unbiased under assumption A1"). Give long conditions their own sentence ("Suppose that A, B, and C hold. Then X."). Enumerate steps or conditions when three or more are packed into one sentence.
- Check that the sentence cannot be misread from left to right. "We prove that A and B imply C" first reads as proving A, so write "We prove that the two conditions A and B together imply C".

**No sentence-initial "And", "But", "So", or "Plus".** Do not open a sentence with "And", "But", "So", or "Plus"; the replacement must keep the relation the conjunction signaled.

- A "But" that corrects or limits the previous sentence becomes "However," or joins that sentence as ", but ...". A "But" that introduces a cited author's objection keeps the objection theirs: "Lee (2021) objects that the bound is loose", not "However, the bound is loose (Lee, 2021)".
- An "And" that adds the last item of a series becomes "Finally," or joins the series. Do not substitute "In addition", "Moreover", or "Furthermore", which mark further support for a claim rather than the next item.
- A "So" that introduces a consequence becomes "Thus," "Hence," or "Therefore," or joins the previous sentence as ", so ...". Vary the connective.

Mid-sentence coordination is correct and stays ("we expect a gain but find none").

**Read the sentence aloud.** If you hesitate or cannot tell which word to stress, identify and repair the structural cause. A punctuation change alone is insufficient. Use this test to diagnose the sentence while avoiding [writerly asides](#plain-wording).

### Concision

**Test every clause by deleting it.** Ask what each word, phrase, and clause adds. Keep a cut if the sentence retains its meaning and remains as easy to read. Cut only words that add nothing; preserve those that supply a referent, scope, logical connection, or authorial stance.

**State the content directly.** A sentence that gives a quantity or category but defers the content ("Three changes alter the reported accuracies, and we note each where it lands") gives the reader nothing to picture, check, or disagree with. State the changes if the draft provides them; otherwise flag the promise. To test the sentence, cover the rest of the paragraph. If the sentence amounts to "there are some, and they are below", it is empty. Cut a trailing promise ("..., and we discuss each below") when the draft states the content. Preserve a summary sentence that states the high-level idea or counts items that follow immediately ("We make four observations. First, ... Second, ..."). A count fails only when its items are deferred or absent.

**Policy in place of finding.** When a sentence gives a rule where a result belongs ("Where a conclusion depends on the choice of metric, we report both metrics"), name the conclusions, the metrics, and the result for each metric.

**Empty verbs.** Verbs such as *affects, varies*, and *has implications for* assert a change without giving its direction or magnitude. State which way the quantity changes and by how much. The verbs *provides, enables,* and *allows* leave a mechanism unexplained when followed only by an outcome ("the cache enables fast retrieval"). Name the operation, or flag it if the draft does not state one.

**Umbrella nouns.** Nouns such as *performance* and *quality* leave the measured quantity unspecified. Name it: accuracy, latency, peak memory, or BLEU.

**Combine signposts with the content they introduce.** Replace a sentence about the text ("The previous section analyzed the encoder. This section presents the decoder.") with the content and a reference to its location ("The decoder maps each latent code produced by the encoder of Section 3 to a token sequence."). Keep a reference that locates content ("the proof is in Appendix B"). Also keep a roadmap of at most two sentences at the end of the introduction or of the opening of a thesis chapter. Delete signposts that name no content ("Section 7 concludes"), roadmaps within a section that repeat its subheadings, and signposts that require more effort to understand than they save. Transitions and summary sentences are [protected](#protect), rather than treated as signposts.

**Cut intensifiers.** Words such as *very, quite, extremely,* and *highly* add no information. Give the [measurement](#plain-wording) instead. Words that soften a claim (*essentially, largely, somewhat, relatively*; "the gap is essentially closed") are [hedges](#hedges); apply the rules on hedges to them. Cut *Note that* and *It is worth noting that* unless they warn against a likely misreading. Use *obviously, clearly, trivially,* and *it is easy to see* only for a step in a derivation or proof that is routine for the reader outside the subfield. Cut them from empirical or comparative claims ("clearly outperforms"), and flag any step that is not routine or is used in place of an argument.

### Plain wording

**Say what literally happens.** Name the actual event, object, and quantity in the words you would use to explain them at a whiteboard.

- *Figurative verbs.* In descriptions such as a loader that "retires" malformed rows, results that "move", or a filter that "passes on" borderline examples, replace the figurative verb with the literal event: the rows are deleted, the accuracy drops, or the filter accepts (or rejects) the examples.
- *Phrasal verbs.* A verb with a particle ("carry out", "come up with", "figure out", and similar) has several meanings that its parts do not predict. Replace it with a single verb naming the operation ("run", "propose", "determine"), unless it is the standard term and no single verb has the same meaning.
- *Inflated words.* Write "use" for "utilize" or "leverage", and "try to determine" for "endeavor to ascertain".
- *Abstraction.* General nouns such as *approach, framework, strategy,* and *issue* describe an idea indirectly. For example, "we adopt a data-augmentation strategy to address the issue of overfitting" becomes "we augment the training data to reduce overfitting". Functional labels name an object by its role in the authors' setup ("the assessment word" for "the word *true* or *false*"). Name the object first, then its role if needed.

- Bad: "Losses above the threshold are winsorized."
- Good: "Losses above 10.0 are set to 10.0 before averaging (winsorization)."

A technical term may still be the right word. Keep it and explain the literal operation at first use, as in the example.

**Use logical words unambiguously.** Replace "Any" with "every" or "some", according to the intended meaning ("the bound holds for every learning rate below 1/L"). Prefer "each" with a singular noun to "all" with a plural when the plural could imply that the objects share one value ("each run uses its own tuned learning rate"). Combine "if A, then if B, then C" into "if A and B, then C". Keep "then" after an "if" clause when the conclusion is a formula or technical claim. Preserve the negation of a monotonicity term, since "not nonincreasing" does not mean "increasing". Where the distinction matters, specify whether "Contains" means membership or inclusion as a subset.

**Spell out definitions and procedures.** Describe every metric, rule, or procedure the reader must rely on in enough detail to recompute it, usually in one or two full sentences. Explain a formal definition in plain language alongside the definition when the reader must use it later.

- Bad: "Coverage is computed per document and averaged."
- Good: "For each document, coverage is the fraction of its reference sentences matched by at least one generated sentence; we report the mean over the 500 test documents."

**Make every referent clear.** Every pronoun, demonstrative, comparative, and shorthand noun must refer to one thing the reader outside the subfield can identify from the text alone. "The previous run" and "the baseline" assume context the reader lacks. Name the referent at first use ("the v1.2 measurement in Section 4.1") and reuse that name afterward. If an edit removes the context that connected a sentence to the argument, restore that context or flag the disconnected sentence, even if it is true. Readers skip headings, so the first sentence under a section title or a run-in paragraph title must make sense without it ("**Gradient caching.** Gradient caching recomputes ...", not "**Gradient caching.** This technique recomputes ...").

**Add a noun when "this" has an ambiguous referent.** When "this", "that", or "it" could refer to more than one earlier noun or clause ("We prune low-magnitude weights and retrain. This improves generalization."), add a noun naming the referent ("This pruning step improves generalization"). A bare "this" may stay in the standard interpretive openings "This means that", "This is because", and "This suggests that" when it follows a single clear claim.

**No writerly asides.** Conversational idioms and clipped instructions ("Call it a wash.") belong to an essayistic style. Replace them with sentences that state the claim and its reason ("Treat this as an upper bound." becomes "This estimate is an upper bound, because the scan also counts duplicates."). A deliberately short sentence is welcome when it is complete and literal.

**Quantify comparatives.** Give the measurement in place of a qualitative comparison ("Our method runs in 0.3 s per example versus 1.1 s for the baseline (3.7× faster)", not "Our method is much faster"). Lead with the headline number, describe the pattern in words, and refer to the table for the remaining values.

**Give the reasons.** Do not write "for various reasons" or end a list with "etc." unless the remaining items are obvious.

### Comparing with prior work

- **Compare, do not list.** End each paragraph or group of paragraphs on prior work by stating how this work differs on a named dimension (an assumption, a metric, a cost, a setting, or a guarantee). Use terms the reader can check. If the draft does not state the difference, flag it rather than supplying one.
- **Characterize prior work in its own terms.** State what a cited work does and under what assumptions before describing what it lacks for this work's setting. Do not describe a difference in scope as a defect ("ignores", "fails to") unless the draft shows the failure. Preserve the sentence crediting the predecessor, which is [protected](#protect). Retain the cited work's own strength of claim; if the source says its results suggest X, do not write that it shows X.
- **Mark what is new.** When a passage combines the text's own contribution with standard or borrowed components, distinguish them clearly ("we use the probe of Smith et al. [4]; our change is to ..."). If the text leaves the novelty ambiguous, flag it rather than deciding it.

- Bad: "Gradient caching [12] reduces memory. Memory-efficient attention [8] reduces memory. Our method reduces memory."
- Good: "Gradient caching [12] and memory-efficient attention [8] both reduce training memory, the first by recomputing representations in a second forward pass and the second by tiling the attention computation. Our method also reduces training memory but needs no second forward pass."

A comparison that is vague on both sides is the [false concession](#tolerable-patterns) pattern. Leave the related-work section where it is, and flag it only when it comes before the method and cannot be understood without it.

## Deslopping

Classify recognizable patterns of AI-written prose in two tiers.

1. **Blacklisted patterns.** Delete every instance, regardless of the co-occurrence test in tier two.
2. **Tolerable patterns.** All other patterns are tolerable. Edit one when doing so improves the sentence itself. Rewrite a whole passage only when it contains three or more tolerable instances.

**Preserve the author's voice.** Keep [varied rhythm](#tolerable-patterns) and genuine authorial stance. Never introduce a voice the draft lacks through added stance, manufactured emphasis, staccato fragments, a contrarian foil, or a detail absent from the draft. [Matching a claim's confidence to its evidence](#claims) calibrates the claim without adding stance. Follow the conventions on [voice](#voice-and-person), [tense](#tense), and [terminology](#terminology) when using first-person "we", present tense for the text and prior work, and deliberately repeated terminology. Generic de-AI advice wrongly changes these features.

### Blacklisted patterns

**Em dashes.** Delete every em dash, including `---` in LaTeX source and an en dash (–) used for the same pause. Substitute a colon, semicolon, or pair of parentheses only if it passes the [pause punctuation](#tolerable-patterns) test in that position. Otherwise rewrite the sentence to remove the need for a pause. Keep an en dash in a numeric range or a name formed from two people's names ("Sections 3–5", "Kullback–Leibler divergence"; `--` in source). Replace `--` only when used for neither purpose. Preserve hyphens in compounds.

**Chatbot artifacts.** Delete "Certainly!", "Great question", "I hope this helps", "As of my last update", and similar.

**Generic openings and closings.** Delete a sentence that could be added to any text in the field ("In the ever-evolving field of deep learning", "The future looks bright"), including apparently defensible versions ("There has been much recent interest in X"). Removing this bloat [needs no request](#cutting). If the draft states why X matters, replace the generic sentence with that reason.

**Leaked generation artifacts.** Remove every chat-interface citation token (`citeturn0search0`, `contentReference[oaicite:...]`), AI-referrer URL parameter (`utm_source=chatgpt.com`), and unfilled template placeholder ("[Your Name]", "[Insert citation]") left by an unedited paste. Keep the surrounding sentence and flag the information missing from each placeholder so the author can supply it.

### Tolerable patterns

**Patterns with a prose rule.** Check for [ornate words with plain alternatives](#plain-wording) (*delve, underscore, showcase, pivotal*, and similar), clauses with [several nominalizations](#sentence-structure), and [counts that promise items without stating them](#concision). Apply the linked rules, keeping an ornate word when it is precise. Also check for wording chosen for brevity and fluency at the expense of plainness.

**Pause punctuation.** Check for a vague assertion ("Retrieval itself helps") followed by a colon or semicolon and a full sentence of evidence without a grammatical link to the assertion. This construction needs revision whether or not it previously contained an em dash. Make one clause subordinate to the other ("..., as shown by Vasquez (2024), who reports ..."); replacing the punctuation with a period does not fix the problem. Cut the first clause if the second already states its entire claim. To test the construction, read the first clause alone. Keep the punctuation if that clause states a specific fact. Also keep colons that introduce lists, displays, quoted definitions, or labels, and semicolons between two specific facts.

After removing colons, check for the same pattern in a trailing phrase separated by a comma and missing its verb ("adds 0.9M parameters, under 0.002% of the backbone"). Restore the verb ("which is under"). Preserve appositives, participial adjuncts, and parallel elaborations that omit a previously stated verb ("the first by ..., the second by ..."). Count instances across the passage before deciding whether to rewrite it as a whole; three instances establish a recurring pattern.

**Reasoning-chain leakage.** Phrases such as "Let us think step by step" and "Breaking this down", along with numbered internal monologues, narrate the author's thinking. State the conclusion, then the evidence. Preserve standard mathematical setup ("Let X be", "Consider a graph G").

**Diff-anchored prose.** Accounts of revisions ("In this revised version, we now clarify", "As suggested by the reviewer, we have added") belong in a response letter or change log. In the text itself, state what the method does.

**Vague attribution.** Phrases such as "Studies show", "experts believe", and the agentless passive "X has been shown to" leave the source unnamed. If the draft cites the source nearby, name it ("Smith et al. (2020) report that X"); otherwise flag the claim.

**Negative parallelism.** Phrases such as "It is not just an optimizer, it is a paradigm shift" and "not only faster but also more accurate" inflate a claim by rejecting an artificial alternative. Splitting the contrast into separate sentences preserves the problem ("The headline is not the speedup. The real story is ..."). State the positive claim directly, with numbers. Keep a contrast that excludes a real alternative ("we measure X, not Y").

**False concession.** A sentence such as "While X has made significant strides, Y remains a challenge" states no specific comparison. Name both sides. Keep a concession when both sides are specific ("the gain holds on the two smaller benchmarks but not the largest").

**Reflexive rule-of-three.** Revise triads such as "faster, cheaper, and more robust" when they group items solely for rhythm. Keep lists whose content calls for three elements.

**False ranges.** A "from X to Y" construction suggests breadth when its endpoints bound no actual range ("tasks ranging from image classification to reinforcement learning"). Name the settings tested. Keep ranges along an ordered axis ("from 10² to 10⁶ parameters").

**Transition chains.** Delete repeated paragraph openings such as *Moreover, Furthermore,* and *Additionally* when they merely announce more text. Let the paragraph order convey the sequence. Keep those that express a [real logical relation](#paragraphs).

**Copula avoidance.** Replace "serves as", "acts as", "represents", "boasts", and similar phrases with "is" or "has" when that is their meaning. If the noun expresses an action, use its verb ("serves as a feature extractor" becomes "extracts features"). Keep "acts as" when it states a function rather than an identity ("acts as a regularizer").

**Trailing "-ing" pseudo-analysis.** Delete a trailing participial clause that adds no checkable claim ("..., highlighting its importance, reflecting broader trends"), or rewrite it as a specific claim the draft supports.

**Self-labeling significance.** When a sentence labels the importance of an earlier result ("This last result is the surprising one"), restructure the passage to make that importance clear and cut the label. Preserve a phrase that expresses authorial stance as the claim is introduced ("Interestingly,").

**Rhetorical questions as transitions.** Replace a question used to connect paragraphs ("But how well does this scale?") with its answer as the topic sentence. Keep research questions that the text then answers ("RQ1: ...").

**Uniform rhythm.** If every sentence is 15 to 25 words long and every paragraph has the same structure, vary their lengths. Keep sentences complete and literal, without adding [writerly asides](#plain-wording).

**Significance inflation.** Delete phrases that link an ordinary detail to a grand trend ("marking a pivotal moment", "paving the way"), or replace them with the specific implication and scope stated in the draft.

**Aphorism formulas.** Replace analogies in the form "X is the Y of Z" ("attention is the currency of deep learning") with an explanation of the mechanism.

**Relentless positivity and sycophantic framing.** When every result is presented as a triumph, give failures comparable prominence to successes and [calibrate both to the evidence](#claims).

## Conventions

These conventions override generic writing advice.

### Voice and person

- Default to active voice with first-person "we" for the authors' actions and decisions. In derivations and proofs, "we" may also mean the author and reader together.
- Choose one agent for the steps of a method or algorithm: either the method ("the algorithm refines the estimate") or "we" ("we refine the estimate"). Use that agent throughout the description. Always use "we" for the authors' choices about the method ("we set k = 5").
- State actions directly. When the work described includes the action, replace "We can compute X" with "We compute X", and replace "aims to" and "seeks to" with the verb itself. Preserve the wording of an unused capability or a goal explicitly marked as unattained, since changing it would [change the claim](#claims). Replace the ungrammatical "allows to model" with "models" or "allows us to model", according to the draft's meaning.
- Passive voice is appropriate when the agent is obvious or irrelevant ("Images are normalized to zero mean"), when it keeps [old information in the subject position](#information-flow-within-a-sentence), or when it moves a long phrase naming the agent to the end.
- In single-authored writing, keep the author's choice of "I" or "we" and apply it consistently. Do not change "we" to "I".

### Tense

Use present tense for the text's contents ("Section 4 shows", not "we will show"), its results, its method and setup ("we train for 10 epochs"), established facts, and prior work of continuing relevance ("Smith et al. propose"). Use past tense for events at a specific time outside the described procedure ("we collected 500 documents in 2024"). Preserve a draft's consistent use of past tense for its experiments. Use future tense only for planned work that has not been done, as in a proposal. Within a paragraph, use the same tense for a subject whose time frame does not change. Prefer simple tense to perfect tense ("Smith et al. show", or "showed", not "have shown"). Keep the perfect only when current relevance is the point ("no prior work has evaluated X at this scale").

### Terminology

Use the same word for a concept throughout the text. Do not alternate synonyms ("network", "model", "architecture", "system") for variety. Vary sentence structure and function words while keeping technical terms consistent. To find inconsistent usage, list every word used for each of the text's most frequent concepts. More than one entry per concept is an error unless the text defines the terms as different things. When a later passage treats a parallel or more general case, repeat the earlier wording exactly, then state the difference.

Where possible, use each technical term as one part of speech. "Sample", "estimate", and "model" can be nouns or verbs. Using one in both roles within a sentence ("we sample 1,000 samples") requires the reader to identify the part of speech at each occurrence. If the text needs both roles, keep them in separate sentences ("we draw 1,000 samples").

Spell out an acronym at first use and again at the start of each major section or chapter where it reappears. An abstract does not count as first use. Do not coin an acronym for a term used only once or twice. Prefer the spelled-out term unless the acronym is standard in the field or replaces a long multi-word name used throughout the text. Spell out acronyms that save no syllables when read aloud ("BS" for batch size) or have another common expansion in the field ("LR"). If the acronym also appears in tables or figures, flag the change to avoid making them inconsistent with the prose.

**Refresh long-lived shorthand.** When shorthand returns after a gap or at a section boundary, remind the reader of its definition ("the graph-search step (Dijkstra's algorithm)", "the contrastive loss L_c defined in Section 3"). Generic shorthand is especially easy to misread ("search" for Dijkstra's algorithm, "the loss" in a text that defined three). Reuse the same term with a reference to its definition, and phrase the reminder as a reminder. Do not substitute a synonym.

Check for suggestive, overloaded, and suitcase terms. A suggestive coinage names a technical object with a colloquial expression ("thought vector", "the model understands"). An overloaded term changes a precise meaning used elsewhere ("deconvolution" for transposed convolution). A suitcase word has several meanings ("generalization" can mean train-to-test performance, transfer, or validity outside the experiment); state which meaning applies. If the text coins the term, flag it and suggest a literal name. If the term is established in the field ("curiosity" as an intrinsic reward), keep it and explain the literal operation at first use. Preserve the accepted shorthand "The network learns features". Replace "the model tries to reason", because intention belongs to the authors ("we train the model to").

### Citation markers are not nouns

A bracketed or parenthetical citation marker cannot be the subject or object of a sentence because it is not a noun. An author name is a noun and may be either.

- Bad: "[10] was the first..." / "(Smith, 2001) shows that..."
- Good: "Smith et al. [10] were the first..." / "Widgets reduce latency (Smith, 2001)." / "Smith (2001) shows that..."

In LaTeX, use `\citet` for textual citations and `\citep` for parenthetical ones, with a non-breaking space before the citation (`widgets~\citep{smith2001}`). Use "et al." only for three or more authors. Put the period on "al." only, and do not italicize the phrase.

Move a citation out of a lead-in when the sentence states an established result the text relies on ("In a recent study, Smith et al. (2015) showed that X" becomes "X (Smith et al., 2015)"). Keep the authors as the subject when the sentence characterizes, contrasts, or reports a claim of theirs that the text does not itself assert.

### Notation and equations

- Define each symbol at or before its first use, at least informally, and [refresh it on reuse](#terminology) ("the sample space 𝒳", not bare "𝒳" pages later).
- If the text already has a Preliminaries or Notation section, move global notation there only when the request [allows relocation](#cutting). Otherwise flag the misplaced definitions. If no such section exists, flag the scattered definitions. Do not create the section, since that would reorder the text.
- Introduce no symbol the text does not use again ("Every continuous function on a compact set is bounded" needs no "f"). Do not give one symbol two meanings, or one object two symbols. If L(θ) is the training loss, do not write "L = 0.31" for its final value; write "L(θ_T) = 0.31".
- Never start a sentence or a clause with a symbol ("A function f is semicontinuous if...", not "f is semicontinuous if..."), and spell out a number that starts a sentence. Separate symbols in adjacent formulas with words ("Consider S_q, where q < p").
- In running prose, write "for all", "there exists", and "implies" in place of ∀, ∃, and ⇒, except in work on logic. Do not use a relation symbol as a word within a verbal phrase ("the step size is at most 0.1", not "is ≤ 0.1").
- Set multi-letter operators and word subscripts upright (`\log`, `\operatorname{softmax}`, `\mathcal{L}_{\text{train}}`). A subscript that is itself a variable stays italic (`x_i`).
- Treat equations as parts of sentences, with "=" as the verb. End a displayed equation with a period if it ends the sentence and a comma if the sentence continues. Put no colon before a display that completes the sentence ("the loss is", not "the loss is:"). A colon is correct after a complete clause ("we define the loss as follows:"). In LaTeX source, leave no blank line before or after a display that continues the paragraph.
- Use a trailing "where" to explain the symbols in a display ("..., where λ controls the trade-off"). If a trailing "where" defines a term on which the claim depends ("Every convex polynomial has even degree, where a function is convex if ..."), move that definition before the claim. Within a theorem statement, define each symbol before using it.
- Replace every non-trivial formula with "blah" and reread. The prose must still read as sentences.
- Number every display referred to in the text. Also number central displays (the objective, the update rule, the main bound), even without a reference to them. Leave intermediate steps unnumbered.
- Make the sentence before a theorem, lemma, or algorithm complete or end it with a colon. Make the statement self-contained by naming its objects ("The function H defined in (5) is continuous"), and exclude motivation and commentary. If the hypotheses exceed a few lines, flag the statement and suggest named conditions defined before the theorem ("Assumption 1 (smoothness)").
- Open a proof by naming its strategy ("We prove the claim by induction on t"), and mark each subgoal when it is met. Make clear throughout whether each statement is assumed, proved, or claimed with its proof deferred.

### Figures and tables

- **Captions.** Write captions that let readers interpret a figure correctly without reading the body text. State what is plotted or tabulated: the quantities, units where applicable, plot axes, and whether higher or lower is better when that is not obvious. Name the conditions (dataset, model, setting), explain each visual encoding (line styles, colors, shaded regions, and [error bars](#uncertainty-and-significance)), and state the figure's main point. A caption that only names the figure ("Results on ImageNet.") is incomplete. Complete it with the wording from the paragraph that references the figure; flag missing facts if they appear nowhere in the draft. Check that the caption and body text describe the figure consistently.
- **References in text.** Refer to every float in the sentence stating its claim ("Accuracy falls as the noise rate rises (Figure 6)" or "Figure 6 shows that accuracy falls as the noise rate rises", not "In Figure 6 we show the results"). If the claim depends on a value the reader can only estimate from the plot, give that number in the sentence or caption. Flag it if neither states the value. Write `Figure~\ref{...}` with a non-breaking space, and capitalize "Figure 6", "Table 2", "Section 4", and "Theorem 1". In LaTeX source, put `\label` after `\caption`. Flag every "?" or "??" in rendered text, which marks an undefined `\cite` or `\ref`.

- Bad caption: "Figure 3: Ablation results."
- Good caption: "Figure 3: Top-1 accuracy (%) of ResNet-50 on ImageNet-1k when each component is removed, mean ± standard deviation over three seeds. Removing the auxiliary loss causes the largest drop."

### Typography and small style

- Hyphenate compound modifiers before nouns ("real-time inference", "three-layer network"). Leave the predicate form unhyphenated ("inference runs in real time"). Preserve an established field term without hyphens when the draft consistently writes it that way ("a large language model").
- Spell out small counts used as adjectives in running prose ("two passes"). Keep numerals for measured quantities, hyperparameter values even when small ("10 epochs"), quantities with units ("batch size 256", "0.3 s"), and values or names ("when k is 2", "Method 2"). Preserve a different cutoff if the draft or its style guide applies it consistently.
- Use "i.e." to mean that is and "e.g." to mean for example; never interchange them. In US style, follow both with a comma. Italicize neither. Use "cf." to mean compare, not see.
- Check that commas marking a non-restrictive clause match the intended meaning ("the encoder, which has 12 layers, ..."). Commas distinguish non-restrictive from restrictive clauses; the choice between "which" and "that" does not. Leave restrictive "which" unchanged unless the governing style guide requires "that". Do not put commas around a symbol naming the preceding noun ("a directed graph G with source s").
- Do not use contractions, exclamation marks, emoji, or title case headings beyond the governing style guide. Use italics for definitions, not emphasis. Use quotation marks for quoted text, words mentioned as words, and terms the authors use without endorsing them (the model's "reasoning"). Explain what any such unendorsed term refers to. Do not put scare quotes around ordinary words.
- Write × (`$\times$`) for multiplication and speedup factors, not the letter x or *, and a minus sign (`$-0.3$`), not a hyphen, for negative numbers. Separate a number from its unit with a non-breaking space (`0.3~s`).
- Give units for measured quantities and axes where applicable. Use US or UK spelling consistently throughout. If the draft mixes two acceptable forms ("dataset" and "data set"), use the more frequent form unless the style guide specifies one.
