# Writing guide

This guide is generated from a collection of writing rules. Each rule has its own page in the `rules/` folder next to this guide's folder and follows this format:

```markdown
# {{ Name of the rule }}

{{ A summary of the rule: what to look for, the edit to make or problem to flag, and the exceptions that change the edit. }}

## Details

{{ Explanations, further cases, and procedures left out of the summary, or the sentence "This rule has no further details." }}

## Examples

**Edit 1.** {{ Optional context, phrased as a hypothetical: "Suppose the draft ..." }}

> **Before.** {{ A passage that breaks the rule. }}

> **After.** {{ The same passage, corrected under this rule alone. Leave out this quote when the passage needs only a flag for the author. }}

{{ Optional explanation of the edit, when it is not obvious. Without an edited passage, the explanation is required and states the flag for the author. }}
```

The guide below collects each rule page's title and summary into one document. Read the full page when a rule applies to your text and you need further details or examples. Each example assumes that every fact it states is accurate, and each illustrates only its own rule, so an example may break other rules.

## Table of contents

The guide has four sections of rules:

- [Cuts](#cuts): empty wording that you may delete without asking the author.
- [Prose](#prose): explanation order, paragraphs, information flow from familiar to new, sentence structure, direct content instead of promises, concrete quantities, and plain wording.
- [Conventions](#conventions): voice, tense, terminology, mathematics, citations and credit, figures and tables, and mechanics.
- [AI patterns](#ai-patterns): blacklisted and tolerable patterns common in AI-written prose.

For a request narrower than a full polish, apply the sections it names and every rule they link to in this guide. Check each chunk of text against every rule in each applicable section. When two rules call for different edits to a sentence and one links to the other, follow the linked rule. Otherwise, choose the clearer sentence, or use your judgment as an expert editor if both are equally clear.

## Cuts

**[Delete empty wording without asking](../rules/cuts/bloat.md).** Delete [chatbot replies](../rules/slop/chatbot-phrases.md), [generic openings](../rules/slop/generic-openings-closings.md), and [generation artifacts](../rules/slop/generation-artifacts.md), and repair [em dashes](../rules/slop/em-dashes.md). Delete content announcements and signposts only when the [signpost rule](../rules/prose/signposts.md) allows. Shorten remaining sentences without cutting [ideas](../rules/cuts/idea-cuts.md).

## Prose

**[Explain ideas in the order readers need](../rules/prose/explanation-order.md).** At any point, readers should understand as much as the preceding text could have explained:

- State the main idea before how it works, and a finding and its interpretation before the supporting evidence.
- Put a section's claim in its first paragraph, and open each paragraph as the [paragraph rule](../rules/prose/paragraph-development.md) directs.
- Define unfamiliar terms before using them.

To test the order, cover everything after a given sentence and ask what the reader knows so far. If a covered sentence would explain more of the visible text than an uncovered one, move it earlier. A sentence that only adds precision to an understood claim can stay. You may reorder sentences within a paragraph and paragraphs within a section, but flag moves between sections. Within a sentence, follow [old before new](../rules/prose/old-before-new.md) and [stress position](../rules/prose/stress-position.md).

**[Apply the deletion test without changing meaning](../rules/prose/deletion-test.md).** Test every clause by deleting it. Keep a deletion only if the word or clause adds nothing and the sentence remains as easy to understand. Every deletion, replacement, or restructuring must keep the [structural words](../rules/prose/first-reading.md) needed on the first reading and preserve who does what, what each word refers to, whether something is possible, required, or actual, definitions, logical relations, distinctions, cases covered, and the author's stance. Apply the [claim rules](../rules/claims/scope.md) to any substantive change. If you are unsure whether an edit changes the meaning, keep the original and flag the ambiguity.

### Paragraphs

**[Develop one point per paragraph](../rules/prose/paragraph-development.md).** State the point as a specific claim in the first sentence rather than [announcing](../rules/prose/signposts.md) a theme. Only when readers need context to understand the claim, give at most one sentence of context from the draft before it. A results paragraph may open with the specific question it tests if the next sentence answers it, followed by evidence. A descriptive or procedural paragraph may open with its first fact or step, except where a Methods section opens with its key idea ([section openings](../rules/story/section-openings.md)). Judge a paragraph by whether its point is developed and coherent, not by sentence count. Keep both sides of a comparison in one paragraph when they support one point. Split a paragraph where its point changes; merge short paragraphs only when they develop the same point.

**[Use lists when readers need separate items](../rules/prose/list-structure.md).** Use a list when readers must tell items apart or follow them one by one. Rewrite bullets as connected prose if they make an argument but hide its reasons or connections. Group long lists by categories established in the draft, keeping every item and qualification and distinguishing primary from secondary items. Suggest a table for comparisons across shared properties. Remove item numbers that imply an unsupported order or ranking unless the text refers to them. For contributions or objectives, flag rather than make any regrouping, renumbering, or conversion to prose.

**[Use connecting words only for relations the draft supports](../rules/prose/transitions.md).** Replace "as", "since", or "while" when readers cannot tell whether it signals time, cause, or contrast. Use "conversely" only when the second statement reverses the first. Remove redundant connecting words, but keep those readers need. Flag "therefore" if the preceding statements do not support the conclusion. Follow the [causal-evidence rule](../rules/claims/causal-language.md) for causal words.

**[Finish one topic before starting another](../rules/prose/topic-order.md).** Repair any unexplained return to an earlier topic (A, B, A). In a comparison organized by named properties, each property can be the topic: compare all methods on one property before moving to the next, rather than regrouping by method.

**[Check sentence openings with the topic string](../rules/prose/topic-string.md).** When individual sentences are clear but the paragraph is hard to follow, check its connections:

1. List each sentence's opening words (the topic string). Check that they advance the paragraph's point rather than merely repeat words. If concepts share a theme but their connection is unclear, state it from the draft or flag the gap. Consecutive sentences may keep the same topic, and a new term at a sentence's end need not recur unless the text promises to explain it. If most sentences start with new material, rewrite them to start with [old information](../rules/prose/old-before-new.md).
2. Insert the implied connective in brackets at each sentence boundary ("[however]", "[therefore]"). If no connective fits or you cannot tell which fits, supply the missing link from the draft or flag it. If "[therefore]" fits but a reader from the intended audience could not explain why the second sentence follows, flag the missing step in the argument.
3. If two adjacent paragraphs could swap places without other edits, add a [summary naming their parallel items](../rules/prose/direct-content.md) when they present parallel items, or state how the second depends on the first.

### Information flow within a sentence

**[Put old information before new](../rules/prose/old-before-new.md).** Open each sentence with a term from the preceding text, or a part, property, or alternative readers can infer from it. A concept known in the field is not old information until the text introduces it. Among several old items, open with the one the sentence discusses, or the most recent if they are equally relevant. When changing voice or clause order, keep the paragraph's topic as the main subject. Keep useful passives under [alternative sentence orders](../rules/prose/passives-fronting-inversions.md).

**[Put important new information in the stress position](../rules/prose/stress-position.md).** The stress position is the end of a sentence or independent clause. Check sentence, paragraph, and section endings for undeserved emphasis; move incidental material earlier. Move a qualifier such as "in these tests" from after the main point to the front instead of deleting it, unless it is a short condition that is clear at the end ([first reading](../rules/prose/first-reading.md)). If several important items share one ending, split the sentence to give each its own ending. Check whether a paragraph's first sentence ends with the topic the paragraph develops. When joining or subordinating clauses, preserve the relative emphasis of findings and qualifications. Move an essential qualification out of parentheses if they make it look optional. Keep each scope condition with the claim it limits. Follow [pause punctuation](../rules/slop/pause-punctuation.md) when using colons or semicolons.

**[Keep old information first in passives, fronting, and inversions](../rules/prose/passives-fronting-inversions.md).** In a passive with a by-phrase, keep the subject at least as familiar as the actor in that phrase. A fronted phrase or an inversion ("Closest to our work is X") must begin with old information; otherwise, use ordinary subject-verb-object order. That order may depart from [old before new](../rules/prose/old-before-new.md) and [final emphasis](../rules/prose/stress-position.md) when it is clearer. Keep a passive, "there is", or "it ... that" construction when it introduces new information without making it the subject.

### Sentence structure

**[Put actors in subjects and actions in verbs](../rules/prose/character-action.md).** Rewrite a nominalization as a verb when it follows a weak verb ("perform an evaluation of") or shares a clause with other nominalizations. List a paragraph's main verbs: if most are "is", "has", or "leads to", check for actions expressed as nouns or left unstated. Flag any actor or action of one actor on another that the draft omits. Keep a nominalization that names a technique ("quantization") or recurring concept, refers to the previous sentence ("This reduction in noise ..."), replaces an awkward "the fact that" clause, or appears alone in a clear sentence.

Keep subject-verb pairings literal. Replace a figurative actor ("the schedule launches the jobs") with the actual actor; a component, instrument, or organism may be the subject of an operation it performs ("the filter removes duplicates"). Keep an instrument or organism as that subject. When an inanimate subject takes a verb of intending, thinking, perceiving, feeling, remembering, or eating, replace the verb with the literal action stated in the draft. Keep established technical verbs with inanimate subjects ("the function expects an integer", "the model learns"), and a result or figure as the subject of a [reporting verb](../rules/claims/verb-ladder.md) ("the results suggest"). Follow [voice](../rules/conventions/active-voice.md) and [information flow](../rules/prose/passives-fronting-inversions.md).

**[Make every sentence clear on the first reading](../rules/prose/first-reading.md).** Length alone is not a defect. Put subjects next to verbs and verbs next to their objects or required phrases ("compare X with Y"). Shorten long opening phrases or clauses. Move a long subject clause toward the end ("It remains open whether the gain survives at larger scale") and, when grammar allows either order, put the longer of two phrases last, unless the long part states old information. Keep short, familiar asides. Move an interruption that introduces new material or a full clause to the beginning or end, make it a separate sentence, or cut it if it adds nothing, unless it states old information readers need there. Never nest one such interruption inside another before the main verb.

Rewrite strings of three or more nouns with a preposition or clause. Break up long sequences of modifiers, usually more than three words before the head noun. Count an established technical name ("large language model") as one noun.

Keep articles so that sentences read as prose, not notes. Keep optional words that mark the start of a long or hard-to-predict clause. Restore "that" after verbs such as "assume", "suppose", "show", "prove", or "find" when readers could first take the next noun as the verb's object; after other verbs, adjectives, and conjunctions when a long clause follows; and before a long relative clause. Restore "that were" in a shortened clause such as "the samples stored in the cabinet" when readers could take "stored" as the main verb. Use "in order to" when bare "to" could look like a value ("we limit the batch size in order to fit in memory"). Do not add optional words to short, predictable clauses, or "that" after "we have".

Read from left to right for words that mislead at first: "We prove that A and B imply C" first reads as proving A, so write "We prove that the two conditions A and B together imply C". Make clear which noun a relative clause or verb-form phrase describes. Put "only" immediately before the word it restricts: "We only evaluate on two datasets" restricts the verb; "We evaluate on only two datasets" restricts the count, which is usually intended. Put a condition before its claim unless it is short and clear at the end. Give a long condition its own sentence, and list three or more steps or conditions instead of packing them into one sentence. If a sentence still contains too many concepts, follow [definitions and procedures](../rules/prose/definitions-procedures.md).

**[Read the sentence aloud](../rules/prose/read-aloud.md).** Listen for hesitation, uncertainty about what to stress, or missing connections. Fix the structure, not just the punctuation. Even a sentence that reads smoothly can be unclear if it relies on pauses, stress, or background knowledge. Do not add a [writerly aside](../rules/prose/writerly-asides.md) telling readers how to read it.

**[Give parallel ideas the same grammatical form](../rules/prose/parallel-form.md).** Ideas are parallel when they have the same logical role. Preserve their meaning: do not rename unlike objects or drop conditions to force symmetry. When "and" or "or" leaves unclear which modifiers or verbs apply to each item, repeat words or split the sentence. If the draft leaves the intended reading unclear, flag the ambiguity instead of choosing one. Compare things of the same kind, restoring an omitted quantity or verb when needed to make the comparison clear. When joining items as equals hides a causal or qualifying relation, state the relation the draft supports. Keep natural variation that is clear.

**[Do not open a sentence with "And", "But", "So", or "Plus"](../rules/prose/sentence-initial-conjunctions.md).** Keep the relation the conjunction signaled:

- Correction or limitation: Replace "But" with "However," or join the previous sentence with ", but ...". Keep a cited author's objection attributed to that author.
- Last item in a series: Use "Finally" or join the item to the series. Do not use "In addition", "Moreover", or "Furthermore", which add support.
- Consequence: Replace "So" with "Thus," "Hence," or "Therefore," or join the previous sentence with ", so ...".

Vary the connective. Keep clear uses of these conjunctions within a sentence.

### Content instead of promises

**[State the content directly](../rules/prose/direct-content.md).** When a sentence only promises later content, calls a topic complex, or names a quantity or category while deferring its content, replace it with the draft's content, or flag the gap. Delete trailing promises such as "and we discuss each below" when the content is already present. Keep summaries of the main idea, counts whose items follow immediately, and statements of real uncertainty, a real dispute, an unresolved definition, or a [limitation](../rules/claims/limitations.md). A sentence is empty if, read alone, it amounts to "there are some, and they are below".

**[State findings instead of how they are reported](../rules/prose/reporting-policies.md).** Replace a sentence that only states a reporting policy ("we report both metrics") with the draft's conclusions, measurements, and outcomes, or flag the missing results. Keep an actual reporting or analysis procedure when it explains what the authors did rather than replacing a result.

**[State the content a signpost announces](../rules/prose/signposts.md).** Replace a signpost with the content it announces and, if needed, a location reference. Keep references that locate content, subject to the [abstract rule](../rules/story/section-functions.md), and [genuine transitions and summaries](../rules/cuts/protected-sentences.md). Keep a roadmap of at most two sentences at the end of an introduction or chapter opening unless the contributions already name their sections ([contribution claims](../rules/story/contribution-claims.md)). Delete announcements that state no content, roadmaps within a section that repeat its subheadings, and signposts that take more effort to understand than they save.

For each roadmap you keep, check that its item count, order, names, and distinctions match the actual sections or items. Correct mismatches that the draft resolves unambiguously, and flag conflicting categories.

**[State the reasons for a choice](../rules/prose/choice-reasons.md).** Replace "for various reasons" or a list's final "etc." with the draft's reasons or items, or flag the gap, unless the omissions are obvious. When a claim depends on an unexplained method choice, give the draft's reason or flag its absence. Do not ask authors to justify routine choices whose role is clear. A reason for a choice is not evidence that the choice caused a result ([causal language](../rules/claims/causal-language.md)).

### Concrete quantities and operations

**[Replace empty verbs with specific changes or operations](../rules/prose/empty-verbs.md).** When "affects", "varies", or "has implications for" leaves a change unspecified, state its direction and size, or flag the missing measurement. When "provides", "enables", or "allows" states only an outcome, give the operation that produces it, or flag the missing operation. Keep wording that already explains the change or capability. For an explicitly untested hypothesis, state the hypothesized direction without requiring a measured size.

**[Name the measured quantity instead of an umbrella noun](../rules/prose/umbrella-nouns.md).** Replace umbrella nouns such as "performance" or "quality" with the measured quantity. Keep a defined collective label when the statement applies to all quantities it covers.

**[Replace vague comparisons with measurements](../rules/prose/quantified-comparatives.md).** For comparatives such as "more" or "faster", give the reported measurement and name what it is compared with. A label such as "large" needs a stated comparison or threshold and cannot replace the measurement. Do not calculate a ratio, such as a speedup or fold change, that the draft does not report.

**[Cut words that add only emphasis](../rules/prose/intensifiers.md).** Replace "very", "extremely", and similar words with the [measurement](../rules/prose/quantified-comparatives.md) when the draft supplies it; otherwise, cut only the emphasis. Treat softeners such as "essentially" and "largely" as [hedges](../rules/claims/hedges.md). Delete "Note that" and similar prompts unless they prevent a likely misreading. Keep "obviously", "clearly", or "trivially" only before a derivation or proof step that is routine for the intended audience. Flag unexplained nonroutine steps and wording that substitutes for an argument.

### Plain wording

**[Say what literally happens](../rules/prose/literal-wording.md).** Name the actual event, object, and quantity in words you would use at a whiteboard. Replace "utilize" or "leverage" with "use" when the meaning is the same. Replace abstract words such as "approach", "framework", "strategy", or "issue" with the specific things they stand for, unless defined and reused as shorthand. Name an object before describing its role in the authors' setup: write "the word *true* or *false*" before calling it "the assessment word".

Replace figurative verbs with the literal events stated in the draft, without guessing from the image. Rewrite a noun used as a temporary verb as a verb phrase naming the action ("we footnote the caveat" becomes "we state the caveat in a footnote"), following the [parts-of-speech rule](../rules/conventions/parts-of-speech.md). Rewrite unusual word pairs that readers must decode ("verified red") in ordinary wording ("verified that the test fails on the original code"). Keep established technical terms, verbs, and word combinations. Replace opaque phrasal verbs only with exact equivalents.

Keep analogies whose correspondence the draft makes clear. Replace decorative or misleading imagery with literal wording, and never add a new analogy. For slogan-like sentences, follow the [aphorism rule](../rules/slop/aphorisms.md). When explaining an unfamiliar term, keep the population, metric, and denominator it covers. Clarify ambiguous prepositions and which item "replace" or "substitute" removes and which takes its place, using only meanings the draft establishes; otherwise, flag the ambiguity.

**[Use logical words unambiguously](../rules/prose/logical-words.md).**

- Replace ambiguous "any" with "every" or "at least one", as the draft means.
- If "all" with a plural noun could suggest that objects share one value, use "each" with a singular noun ("each sample is held at its own temperature").
- Distinguish "not all" from "none". When it affects the claim, clarify whether "some" allows all cases or means fewer than all.
- Rewrite a negative statement as a positive one only when both hold in exactly the same cases ("not nonincreasing" does not mean "increasing"), including values equal to a threshold. Keep a deliberate denial as a denial. With "not" and "because", clarify whether the denial concerns the outcome or its proposed cause.
- When "can" or "should" could mean observation, capability, possibility, prediction, recommendation, or obligation, use the meaning the draft establishes, or flag the ambiguity. Follow [hedges](../rules/claims/hedges.md) and [performed actions](../rules/conventions/performed-actions.md). Keep impossibility, prohibition, and lack of obligation distinct when negating modal verbs.
- Keep "then" after an "if" clause whose conclusion is a formula or technical claim. Combine nested conditions ("if A, then if B, then C") into one ("if A and B, then C") only when both govern the same conclusion, and keep necessary and sufficient conditions distinct. When "if" introduces a comparison rather than a condition, state the comparison separately from the claim.
- Replace an ambiguous slash in prose with the words it stands for, such as "or" or "and", keeping standard abbreviations and notation.
- Preserve whether a list is complete; "includes" alone does not imply omitted members.
- When "contains" could mean membership or subset inclusion, state which.

**[Spell out definitions and procedures](../rules/prose/definitions-procedures.md).** Describe every metric, rule, or procedure readers rely on well enough to interpret and recompute its results, usually in one or two full sentences.

- Definitions: Name the kind of thing and its distinguishing traits; expanding an acronym is not enough. Pair formal definitions readers need with plain explanations. For related concepts, state their shared category and differences. When definitions compete, state which the paper adopts and the draft's reason, without inventing alternatives.
- Procedures: Do not flag standard steps covered by a precise citation. Keep every modification and the explanation readers need at that point. If a procedure only lists steps, state its purpose from the draft, or flag its absence.
- Settings: During a story or overclaiming check, or when a result depends on an unstated setting, check that the draft gives the settings its kind of work needs, such as algorithm preconditions, random seeds, software versions, calibration, data exclusions, or participant recruitment and blinding. Flag each missing item without supplying a plausible default. Delete or move details needed for reproduction only as the [cutting rules](../rules/cuts/sentence-dependencies.md) allow.
- Hard explanations: When you cannot follow an explanation, use an example already in the draft to find the missing step, or flag the gap. Build difficult explanations from a simple case through necessary complications, using the draft's cases.
- Examples: Flag a worked example that does not match the stated method or definition, without changing either. Reuse an illustrative input across methods unless it hides their differences. Prefer an available real input that explains the operation; keep toy cases when they explain it better. State what each example illustrates without inventing outcomes.

**[Resolve references without changing the claim's status](../rules/prose/referents.md).** Make each pronoun, demonstrative, comparative, and shorthand noun phrase identify one referent from the text alone. Name ambiguous baselines or previous runs with the draft's labels and reuse those names. The first sentence under a section title or run-in paragraph title must make sense without the title. Restore context lost during editing, and flag connections you cannot resolve rather than choosing a referent.

Replace an ambiguous "this", "that", or "it" by naming the referent the draft supports. Preserve its status and evaluation: a conjecture is not a finding, and a change is not necessarily an improvement. Allow bare "This" to introduce an interpretation after one unambiguous claim, as in "This means that", "This is because", and "This suggests that".

**[State claims and reasons in complete, literal sentences](../rules/prose/writerly-asides.md).** Replace conversational idioms such as "Call it a wash" and editorial commands with complete, literal statements of the claim and the draft's reason for it, or flag a missing reason. Keep a deliberately short sentence when it is complete and literal. Follow [intensifiers](../rules/prose/intensifiers.md) for "Note that" and similar prompts. Preserve the author's supported stance under [author voice](../rules/slop/author-voice.md).

## Conventions

When a convention in this section conflicts with general writing advice, follow the convention.

### Voice and tense

**[Use active voice and keep the actor consistent](../rules/conventions/active-voice.md).** Use active "we" for the authors' actions and decisions, but not for the research community or people in general; "we" may include the reader in derivations and proofs. In method descriptions, consistently use either the method ("the algorithm refines the estimate") or "we" ("we refine the estimate") as the actor. Use "we" for design choices ("we set k = 5"). Keep a single author's choice of "I" or "we" and apply it consistently. Do not assign an action to the authors when the draft omits the actor.

Keep passives:

- When the actor is obvious, irrelevant, or unknown.
- When they put [old information first](../rules/prose/passives-fronting-inversions.md).
- When a long actor belongs at the end.
- In clear passive modifiers ("the samples selected by technicians").

**[State performed actions directly](../rules/conventions/performed-actions.md).** When the draft shows that an action was performed, replace "can", "aims to", or "seeks to" with a direct verb. Keep them for an unused capability or unreached goal when removing them would [change the claim](../rules/claims/scope.md). Replace the ungrammatical "allows to model" with "models" or "allows us to model", as the draft means.

**[Match tense to the time frame](../rules/conventions/tense.md).**

- Use present tense for the paper's contents ("Section 4 shows"), results, method and setup, established facts, and prior work that still applies.
- Use past tense for events at a specific time outside the described procedure ("we collected 500 documents in 2024"), and keep it for reported findings ("Lee found that the alloy was weaker"), hypotheticals ("if the sample were larger"), and a draft's consistent past tense for experiments.
- Use future tense only for plans not yet completed, as in a proposal.
- Prefer simple to perfect tense ("Smith et al. show" or "showed", not "have shown"), but keep perfect tense for current relevance ("no prior work has evaluated X at this scale") or an event before another past event ("had tested").

Keep tense consistent within each time frame. Do not turn a general research recommendation into the authors' own promise. Replace a relative date, such as "last year", with the draft's calendar date, or flag it.

### Terminology

**[Use one term per concept](../rules/conventions/term-consistency.md).** Do not alternate terms such as "device", "sensor", and "system" for variety, including in captions and figure labels; vary sentence structure and function words instead. Keep different names only for distinct concepts, such as types, scopes, or measured quantities. Use the field's standard term when the draft makes clear that its own term means exactly the same thing ("learning rate", not "step factor"), but flag the authors' label for something they introduce rather than renaming it. A clear pronoun or bare demonstrative may refer back to the term in the same or next sentence, but use the specific name rather than a general category noun ("this compound"). To find synonyms, list the names the draft uses for each recurring concept, and flag any inconsistency that prose edits cannot fix, such as a mismatched figure label. When describing a parallel or more general case, repeat the earlier wording exactly, then state what differs. When naming a formula's role helps readers follow without looking back, use its established role, such as a bound or definition, rather than calling it an equation.

**[Avoid using one technical term as both a noun and a verb](../rules/conventions/parts-of-speech.md).** If using a technical term as both noun and verb in one sentence forces rereading ("we sample 1,000 samples"), replace the verb with an ordinary one ("we draw 1,000 samples") or split the sentence. Otherwise, leave it alone.

**[Spell out acronyms and introduce few new ones](../rules/conventions/acronyms.md).** Spell out an acronym when repeated use begins; use the full term for isolated earlier mentions. Define it separately in the abstract and body, and again at the start of each major section or chapter where it returns. Prefer the full term unless the acronym is standard or shortens a long, recurring name; spell out an acronym that appears once or twice, has another common expansion in the field, or saves no syllables when read aloud ("TS" for time step). Flag an acronym in the title that the intended audience would not know before reading the abstract. Propose spelling it out, but leave the title unchanged. Flag opaque coined labels rather than renaming them, unless [term consistency](../rules/conventions/term-consistency.md) calls for the standard term. If you would spell out an acronym that also appears in tables, figures, or code, flag the replacement instead.

**[Remind readers what shorthand means after a gap](../rules/conventions/shorthand-reminders.md).** When shorthand or a symbol returns after a long gap or section boundary, remind readers of its name and either its definition or where it was defined ("the contrastive loss L_c defined in Section 3"). Phrase this as a reminder rather than a new definition. Replace ambiguous labels such as "the rate" with the original full name, and name a distant display referred to by number alone ("the energy balance (9)").

**[State what ambiguous or suggestive terms mean](../rules/conventions/suggestive-terms.md).**

- Suggestive coinages name technical objects with colloquial expressions (an "intelligent" coating). Flag them even when defined, and suggest literal alternatives, unless a standard term means exactly the same thing ([term consistency](../rules/conventions/term-consistency.md)).
- Overloaded terms change a precise meaning used elsewhere ("deconvolution" for transposed convolution), and technical words can be used loosely ("exponential" for rapid growth). Replace either with the precise wording when the draft establishes the intended meaning; otherwise, flag it.
- For words with several meanings in the field ("generalization": train-to-test performance, transfer, or validity outside the experiment), state which meaning applies.
- Keep established technical wording ("the enzyme recognizes its substrate"), but explain the literal operation at first use.
- When an ordinary word collides with a nearby technical term ("a normal sample" near "normal distribution"), replace the ordinary word and keep the technical term.
- Replace an intention or mental state attributed to a system ("the particle wants to minimize its energy") with the literal operation or the authors' design goal, or flag it.

Follow [definitions and procedures](../rules/prose/definitions-procedures.md) for unfamiliar categories and competing definitions.

### Mathematics

**[Define each symbol by its first use and give it one meaning](../rules/conventions/symbol-definitions.md).** An informal definition suffices at first use; [refresh it after a gap](../rules/conventions/shorthand-reminders.md). Give each object one symbol, and introduce no symbol the text does not use again. Flag conflicting meanings, symbols used contrary to their standard meaning in the field, unused definitions, easily confused symbols, dense notation, and functions equated with their values ("$V = 0.31$" meaning "$V(x_0) = 0.31$"). Keep local definitions near the passages that use them. Move scattered definitions of symbols used throughout the paper into an existing Preliminaries or Notation section only if the request [allows relocation](../rules/cuts/idea-cuts.md); otherwise, flag them. Do not create a Preliminaries or Notation section. Suggest, rather than make, any renaming or other notation improvement, such as replacing an index that distinguishes nothing with words, giving a recurring complex expression a short name, or grouping related quantities in a vector, set, or other collection.

Flag unspecified factor order in noncommuting products and inconsistent use of definition signs. For ranges, flag unclear finite bounds, endpoint inclusion, index origin, element types, or empty-range conventions. Supply conventions only from the draft; never assume commutativity or merge boundary cases to shorten notation.

**[Write mathematics as grammatical prose](../rules/conventions/math-prose.md).** An equality can supply a sentence's verb. Check the grammar by mentally replacing each formula with words that play the same role.

- Begin sentences and clauses with words, not bare symbols. Spell out sentence-initial numbers regardless of the number-spelling cutoff.
- Separate adjacent formulas with words ("Consider S_q, where q < p"), even across sentence boundaries.
- Reword a sentence-final symbol that could be read as part of the next name or abbreviation.
- Except in work on logic, write quantifiers and implications in prose as words ("for all" for $\forall$).
- Never let a relation symbol stand for words in a verbal phrase ("is at most 0.1", not "is $\le 0.1$").
- A trailing "where" clause may define symbols, but put definitions needed to understand a claim before it.
- End a displayed formula with a period if the sentence ends or a comma if it continues.
- Put a colon before a display only after a complete clause ("we define the loss as follows:"), never after an incomplete one ("the loss is:").
- In LaTeX source, put no blank lines around a displayed formula that continues its paragraph.

**[Explain why an equation or definition is needed](../rules/conventions/formal-material-purpose.md).** Flag any central equation, definition, or intermediate result (lemma, theorem, or algorithm) whose purpose the draft does not state; do not infer a purpose. Within a section, move the draft's explanation of why the material is needed before the material itself; flag a move from another section. Follow [formal support](../rules/claims/evidence-kind.md) when an application depends on unstated conditions.

**[Use the correct type for operators, subscripts, and signs](../rules/conventions/math-typography.md).** Use upright type for multi-letter operators (`\log`, `\operatorname{softmax}`) and word subscripts (`\mathcal{L}_{\text{train}}`), but italic for variable subscripts (`x_i`). Use × (`\times`) for multiplication and multiplicative factors rather than x or `*`, except in code. Write negative values in math mode (`$-0.3$`) to give them minus signs rather than hyphens. Fix LaTeX typography only when mathematical meaning stays unchanged, and flag any change to symbols, grouping, delimiters, or operator meaning. Propose a clearer form for ambiguous notation, such as a slash fraction whose denominator has no clear end, only when the draft establishes the intended meaning. Flag stacked inline fractions that disrupt line spacing, exponent fractions too small to read, and oversized delimiters; suggest slash fractions or smaller delimiters only with grouping preserved.

**[Number referenced and central displays](../rules/conventions/display-numbering.md).** Number central displays, such as the objective and the main bound, even when the text does not refer to them; leave unreferenced intermediate steps unnumbered. Identify rejected formulas and counterexamples beside their displays using the draft's stated status; retain central counterexamples and negative results.

**[Make theorem statements self-contained](../rules/conventions/theorem-statements.md).** Introduce a theorem, lemma, or algorithm with a complete sentence. In the formal statement, name its objects and include any needed definition reference ("The function H defined in (5) is continuous"). Define every symbol before use, and keep motivation and informal comments outside the statement. If hypotheses run for several lines, flag the statement and suggest extracting them into named conditions defined before it.

**[Open each proof with its strategy and state when each goal is met](../rules/conventions/proof-strategy.md).** Make clear whether each statement is assumed, defined, established, or deferred to a later proof. Treat cases in the announced order and under their announced names. When moving from constructing an object to using it, state the property that justifies the next step. Add strategy or progress statements only from the draft; otherwise, flag the omission. Follow [intensifiers](../rules/prose/intensifiers.md) for "clearly" and "it is easy to see". Flag deferred proofs whose stated dependencies form a cycle; a forward reference alone is not a defect. Flag missing equality links between successive bounds when the draft establishes that their right-hand sides are equal.

### Citations, figures, and tables

**[Keep citation markers out of subject and object positions](../rules/conventions/citation-markers.md).**

- Replace a citation marker used as a subject or object ("[8] introduces") with a textual citation that names the authors.
- When asserting an established result, shorten "In a recent study, ... showed that X" to "X (citation)". Keep cited authors as the subject when reporting, characterizing, or contrasting a claim the paper does not assert, following [prior work](../rules/story/prior-work-comparisons.md).
- Place each citation beside the clause it supports when the draft identifies the connection; otherwise, flag a trailing cluster that obscures which source supports which claim. Flag any passage that leaves unclear where a source's material begins or ends.
- Use the document's citation package commands, such as natbib's `\citet` (textual) and `\citep` (parenthetical), with a non-breaking space before a parenthetical citation (`result~\citep{key}`).
- Use upright "et al." only for three or more authors.

**[Flag missing citations and citation keys absent from the references](../rules/conventions/missing-citations.md).** Flag technical claims presented as prior knowledge without an identifiable source, and citation keys missing from the supplied references. Common knowledge needs no citation, but never delete an existing citation as unnecessary. Preserve secondhand wording such as "as cited in". Follow [vague attribution](../rules/slop/vague-attribution.md) for "Studies show". For a specific passage or result cited from a book or long survey, flag a missing page, section, or theorem locator.

**[Write captions that stand alone and state the finding](../rules/conventions/captions.md).** Complete a caption that only names its figure or table with facts from the citing paragraph; flag any needed facts absent from the draft. In each caption:

- Identify quantities, units, axes, and conditions.
- Explain each visual encoding (line styles, colors, shaded regions, [error bars](../rules/claims/variability.md)), and state whether higher or lower is better when that is not obvious.
- State the supported finding, check that it matches the body text, and name compared methods or conditions directly, not by color alone.

In tables, flag unexplained blanks, dashes, and columns with mixed or missing units. Flag claims drawn from visual slopes or distances that the plot's stated axis ranges, dual vertical axes, or fitted-curve range do not support, and any extrapolated value described as measured; a truncated axis is not by itself an error.

Flag table layouts that separate comparison partners or obscure groups; suggest placing entries together and ordering them to show the intended comparison, preserving meaningful chronological or semantic order.

**[Cite each figure and table in the sentence that states its finding](../rules/conventions/figure-table-references.md).** Replace announcements like "In Figure 6 we show the results" with the finding and its reference ("Accuracy falls as the noise rate rises (Figure 6)"). In the abstract, follow the [abstract rule](../rules/story/section-functions.md). Point to the specific panel or comparison the draft identifies, with numbered references rather than relative pointers such as "below". When a claim needs an exact value that readers can only estimate from a plot, state the draft's value in the sentence or caption, or flag its absence. Flag unresolved citation or reference markers ("??"). Write `Figure~\ref{...}` with a non-breaking space, and capitalize "Figure", "Table", "Section", and "Theorem" for numbered items. Place an existing `\label` after its `\caption`.

### Mechanics

**[Make each free style choice consistent](../rules/conventions/style-choices.md).** For equally accepted forms, follow venue requirements; otherwise, use the form established in the draft, choosing the more frequent form when the draft mixes them. Never change an accepted form merely by preference. Common choices include:

- The variety of English (US, UK, Canadian, or another).
- The spelling, spacing, and hyphenation of each term ("dataset" or "data set"). Keep an established field term unhyphenated when the draft consistently writes it that way.
- Heading case. Where neither case predominates, use sentence case.
- The cutoff below which numbers are spelled out as words.
- The serial comma.

**[State units clearly and never change a number's value or precision](../rules/conventions/units-and-numbers.md).** Give every measurement and axis its unit, separated from the number by a non-breaking space (`0.3~s`). Preserve established number formats. Match forms within a comparison only when value and precision stay unchanged. Use the draft to resolve ambiguous unit meanings, measurement bases, binary or decimal prefixes, and duration formats, or flag the ambiguity. Flag, rather than perform, any unit conversion.

## AI patterns

Patterns common in AI-written prose, called AI slop, fall into two groups:

1. **Blacklisted patterns.** Remove every instance, even a single one, or flag it where the rule says to. The three-instance threshold below does not apply.
2. **Tolerable patterns.** Edit a single instance when the edit makes the sentence clearer. Rewrite a whole passage only when it contains three or more instances of tolerable patterns.

**[Preserve the author's voice](../rules/slop/author-voice.md).** Keep the draft's [varied rhythm](../rules/slop/repetitive-syntax.md) and the authors' own opinions and reactions. Never add opinions, reactions, emphasis, sentence fragments, opposing positions, or unstated details. [Verify that each rewrite keeps the meaning](../rules/prose/deletion-test.md). Never treat ["we"](../rules/conventions/active-voice.md), [present tense](../rules/conventions/tense.md) for the text or prior work, or [repeated technical terms](../rules/conventions/term-consistency.md) as defects merely because generated prose uses them. [Matching a claim's confidence to its evidence](../rules/claims/scope.md) adds no opinion.

### Blacklisted patterns

**[Delete em dashes](../rules/slop/em-dashes.md).** Delete every em dash (`---` in LaTeX) and every en dash used as a pause. Use a colon, semicolon, or parentheses instead only if the replacement passes the [pause punctuation](../rules/slop/pause-punctuation.md) test. Parentheses must also keep essential qualifications from looking optional under [stress position](../rules/prose/stress-position.md). Otherwise, rewrite the sentence without the pause, preserving its emphasis. Keep hyphens in compound words and en dashes (`--`) in numeric ranges and names formed from two people's names ("Kullback–Leibler").

**[Delete conversational replies left by a chatbot](../rules/slop/chatbot-phrases.md).** Delete conversational replies to the user, such as "Certainly!" or "As of my last update". Keep such wording in material the paper analyzes.

**[Delete generic openings and closings](../rules/slop/generic-openings-closings.md).** Delete filler that could fit any paper in the field, even if it names the topic. This includes popularity claims that sound factual ("There has been much recent interest in X"). If the draft gives a specific reason the topic matters, use it instead. If readers need background first, follow [brief setup](../rules/prose/paragraph-development.md).

**[Remove stray citation codes and placeholders, and flag missing information](../rules/slop/generation-artifacts.md).** Remove artifacts left by an unedited paste, such as chat citation codes (`citeturn0search0`, `contentReference[oaicite:...]`) and unfilled placeholders ("[Insert citation]"). Keep the surrounding claim and flag the missing information. Flag URL parameters that identify an AI tool as the referrer, such as `utm_source=chatgpt.com`, for removal.

### Tolerable patterns

**[Apply prose rules to ornate words, actions written as nouns, counts, and lists](../rules/slop/prose-rule-patterns.md).** Apply [literal wording](../rules/prose/literal-wording.md) to ornate words such as "delve" and "pivotal", keeping a word when it is precise. Apply [character and action](../rules/prose/character-action.md) to clauses that express several actions as nouns, [direct content](../rules/prose/direct-content.md) to deferred counts, and [list structure](../rules/prose/list-structure.md) to bulleted arguments.

**[Expand compressed wording that slows the first reading](../rules/slop/compressed-constructions.md).** Check for [inanimate subjects given human actions](../rules/prose/character-action.md), [nouns used as verbs and unusual word pairs](../rules/prose/literal-wording.md), and [noun strings, omitted "that" or articles, and long gaps between subject and verb](../rules/prose/first-reading.md). Keep short forms that are clear on the first reading.

**[Repair pause punctuation between a claim and its evidence](../rules/slop/pause-punctuation.md).** Read the clause before each colon or semicolon on its own. If it states no specific fact ("Annealing helps: conductivity rises by 40%"), join the claim to its evidence in words or delete the vague clause when the evidence states the whole claim. Replacing the mark with a period does not fix the vague clause. If the clause states a specific fact, keep a semicolon before a related fact or a colon before an explanation or example. Never use a colon that implies an unsupported identity, cause, or complete list. A colon may also introduce a list, a displayed formula under [mathematical punctuation](../rules/conventions/math-prose.md), a quoted definition, or a label, unless it separates a vague claim from its evidence.

Restore any missing verb in a phrase after a comma ("adds 3 ms, below the limit" becomes "adds 3 ms, which is below the limit"). Keep appositives, clear participial phrases, and parallel phrases that share an earlier verb ("the tank holds 5 L, the bottle 1 L").

**[Replace narration of the thinking process with conclusions and evidence](../rules/slop/reasoning-leakage.md).** Replace narration of the writer's thinking, such as "Let us think step by step" or numbered accounts of that process, with conclusions and evidence. Keep mathematical setup ("Let X be"), proof steps, substantive reasoning that the result depends on, and model reasoning quoted or analyzed as experimental material.

**[Describe the work without narrating manuscript revisions](../rules/slop/revision-narration.md).** Replace revision phrases such as "In this revised version, we clarify" or "As suggested by the reviewer" with the scientific content. Keep such accounts only in response letters and change logs. Preserve all added explanations, evidence, and justifications, and any comparison between method versions that is part of the study.

**[Name the cited source when an attribution is vague](../rules/slop/vague-attribution.md).** For vague attributions such as "studies show", "experts believe", or "X has been shown to", name a source only when the draft cites one for that claim, following the [citation-marker](../rules/conventions/citation-markers.md) and [prior-work](../rules/story/prior-work-comparisons.md) rules. If no source is cited for that claim, flag the missing attribution. An objection clearly framed as hypothetical and then answered needs no cited objector. The phrase "Some may argue" alone does not provide that framing.

**[Replace negative parallelism with the positive claim](../rules/slop/negative-parallelism.md).** When a contrast rejects an alternative invented for emphasis, state the supported result or measurement directly. Look for "not only ... but also", "not just ...", and paired sentences such as "The headline is not the speedup. The real story is ...". Keep contrasts that exclude real alternatives ("we measure X, not Y").

**[Make both sides of a false concession specific](../rules/slop/false-concession.md).** In a concession such as "While X has advanced, Y remains a challenge", replace each vague side with the draft's specific finding. Flag any side the draft leaves unspecified. Keep concessions whose sides are both specific.

**[Revise rule-of-three lists written for rhythm](../rules/slop/rule-of-three.md).** In a list such as "faster, cheaper, and more robust", remove empty or redundant words and flag unsupported items. Never drop a substantive item just to change the count.

**[Replace false ranges with the settings tested](../rules/slop/false-ranges.md).** When the endpoints of "from X to Y" lie on no ordered scale ("from image classification to reinforcement learning"), replace the phrase with the settings tested. Keep ranges on ordered scales, such as "from 10² to 10⁶ parameters". Never shorten a longer list to its endpoints.

**[Delete transition chains that announce more text](../rules/slop/transition-chains.md).** Delete repeated openings such as "Moreover", "Furthermore", and "Additionally", letting paragraph order convey the sequence. Never replace them with unsupported causal, temporal, or contrastive links. Keep transitions that show a [valid logical relation](../rules/prose/transitions.md).

**[Replace needless substitutes for "is", "has", or action verbs](../rules/slop/copula-avoidance.md).** Replace phrases such as "serves as", "acts as", "represents", or "boasts" with "is" or "has" when the meaning stays the same. Replace a following action noun with its verb ("serves as a temperature monitor" becomes "monitors temperature"). Keep these verbs when they express a role distinct from identity or a precise technical meaning.

**[Delete or replace empty commentary in trailing "-ing" phrases](../rules/slop/trailing-ing.md).** Delete a trailing "-ing" phrase that adds no checkable claim ("highlighting its importance"), or replace it with a specific claim the draft supports. Rewrite a trailing "-ing" phrase whose actor is unclear as a clause that names the actor, following [first reading](../rules/prose/first-reading.md).

**[Delete sentences that only label results important or surprising](../rules/slop/self-labeling.md).** Delete sentences that only label a result important or surprising ("This is the key result"). If the draft explains why the result matters, organize the passage around that reason; otherwise, add no explanation. Keep a word that expresses the authors' stance and introduces a claim ("Interestingly,").

**[Replace rhetorical questions used as transitions with their answers](../rules/slop/rhetorical-questions.md).** Delete a question that only introduces the next topic, even if the next sentence answers it, and make its answer the paragraph's first sentence. Keep a research question that states what the text tests. Keep a mid-paragraph question only if it turns preceding details into a puzzle that the next sentence answers. Rewrite a question that assumes readers agree with a claim ("Does this not prove ...?") as a statement of that claim, choosing its verb from the [verb ladder](../rules/claims/verb-ladder.md).

**[Vary sentence structure to show how ideas connect](../rules/slop/repetitive-syntax.md).** Look for consecutive sentences or paragraphs that repeat an opening, clause pattern, or length. Vary their structure and how they join according to relations the draft states, such as a shared object, condition, time, or consequence. Use the [topic string](../rules/prose/topic-string.md) rather than random length changes. Preserve [parallel wording for parallel ideas](../rules/prose/parallel-form.md), and keep sentences complete and literal, without [writerly asides](../rules/prose/writerly-asides.md).

**[State what a result implies without exaggerating its importance](../rules/slop/significance-inflation.md).** Delete phrases that exaggerate importance, such as "marking a pivotal moment" or "paving the way", or replace them with the supported implication and its conditions. Keep substantive implications that lack evidence. Mark a speculative explanation or mechanism under [speculation](../rules/claims/speculation.md), and flag any other unsupported implication.

**[Replace slogan-like analogies with literal explanations](../rules/slop/aphorisms.md).** Replace a slogan-like analogy of the form "X is the Y of Z" only with a mechanism the draft states. Delete a slogan that makes no substantive claim. If an analogy asserts an unexplained mechanism, keep it and flag the missing explanation.

**[Make reported failures as noticeable as successes](../rules/slop/relentless-positivity.md).** When a draft presents every result as a success, give its failures and counterevidence comparable prominence and [match each claim to its evidence](../rules/claims/scope.md). Never invent a failure or add a caveat or hedge for balance.
