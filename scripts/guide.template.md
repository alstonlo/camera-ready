# Writing guide

This guide is generated from a collection of writing rules. Each rule has its own page in the `rules/` folder next to this guide and follows this format:

```markdown
# {{ Name of the rule }}

{{ A summary of the rule: what to look for, the edit to make or problem to flag, and the exceptions that change the edit. }}

## Details

{{ Explanations, further cases, and procedures left out of the summary, or the sentence "This rule has no further details." }}

## Examples

**Edit 1.** {{ Optional context, phrased as a hypothetical: "Suppose the draft ..." }}

> **Before.** {{ A passage that breaks the rule. }}

> **After.** {{ The same passage, corrected under this rule alone. }}

{{ Optional explanation of the edit, when it is not obvious. }}
```

The guide below reproduces each rule's heading and summary, and each rule page adds `Details` and at least one example. Read the full page when a rule applies to your text but the summary does not show which edit to make. Each example shows one edit that its rule calls for. No example permits a change beyond what the user asked for.

## Table of contents

The guide has six sections of rules:

- [Story](#story): the argument from problem to implications, titles and headings, section order and openings, contributions, related work, results by question, and numbers that support claims.
- [Claims](#claims): reporting verbs matched to evidence, scope, overclaiming and underclaiming, consistency across the text, causal language, what an efficiency claim counts, statistical significance, hedges, speculation, and limitations.
- [Cutting](#cutting): what you may delete or move without asking the author, the triage order under a length limit, sentences to protect, and how to repair text around a cut.
- [Prose](#prose): explanation order, paragraphs, information flow from familiar to new, sentence structure, direct content instead of promises, concrete quantities, and plain wording.
- [Conventions](#conventions): voice, tense, terminology, mathematics, citations and credit, figures and tables, and typography.
- [Deslopping](#deslopping): blacklisted and tolerable patterns common in AI-written prose.

For a request narrower than a full polish, apply the sections it names and every rule they link to. Check each chunk of text against every rule in each applicable section. When two rules call for different edits to a sentence and one links to the other, follow the linked rule. Otherwise, choose the clearer sentence, or use your judgment as an expert editor if both are equally clear.

## Story

Organize the text around one five-part argument: a problem the reader cares about; a gap in what is known or possible, with the cost of leaving it open; an idea that fills the gap; evidence that the idea works; and what the findings imply.

Check this argument across the whole text and within each section before editing individual sentences, because sentence edits cannot fix a missing or illogical step. Use the [rules on claims](#claims) to match each claim to its evidence, the [rules on cutting](#cutting) to decide what stays, and the [rules on prose](#prose) to edit paragraphs and sentences.

Without a separate request from the author, you may:

- Reorder sentences in a paragraph or paragraphs in a section to put the claim first.
- Rewrite a section's opening using content already in that section.
- Remove numbers from running text when a table already gives them.
- Rewrite a caption to state a conclusion already drawn in the body.

Flag any change to the claims, section order, or list of contributions instead of making it yourself, except claim edits that the [rules on claims](#claims) allow. Never add a cost, explanation, or number absent from the draft.

### The whole argument

{{story/argument-summary}}

{{story/section-functions}}

{{story/linear-argument}}

{{story/skim-test}}

{{story/titles}}

### Problem, gap, and contribution

{{story/open-with-problem}}

{{story/gap-cost}}

{{story/why-hard}}

{{story/contribution-claims}}

### Section openings and connections

{{story/section-openings}}

{{story/headings}}

### Related work

{{story/prior-work-comparisons}}

{{story/novelty}}

{{story/prior-work-placement}}

### Results

{{story/results-by-question}}

{{story/one-question-per-paragraph}}

{{story/explain-evidence}}

{{story/component-effects}}

### Numbers

The most common flaw in the argument of AI-generated text is listing results before stating what they show, or never stating the point. Reorder the text so that every number supports a claim already stated in words.

{{story/claim-before-number}}

{{story/number-precision}}

### Discussion and conclusion

{{story/return-to-gap}}

{{story/conclusion-perspective}}

## Claims

Every claim must match its evidence. Claiming either more or less than the evidence supports is an error. An unreached goal may motivate the work if the text states that the goal remains unreached.

### Strength and scope

{{claims/verb-ladder}}

{{claims/scope}}

{{claims/unsupported-labels}}

{{claims/underclaiming}}

{{claims/internal-consistency}}

### Causation and formal support

{{claims/causal-language}}

{{claims/evidence-kind}}

{{claims/efficiency-claims}}

### Numerical comparisons

{{claims/variability}}

{{claims/statistical-significance}}

### Qualification and limits

{{claims/hedges}}

{{claims/speculation}}

{{claims/limitations}}

## Cutting

Use the [spine test](rules/cutting/spine-test.md) to find the core claims and the paragraphs readers need to understand or evaluate them. Then check the request to see what you may delete or move.

### Deciding what to cut

{{cutting/bloat}}

{{cutting/idea-cuts}}

{{cutting/spine-test}}

{{cutting/triage-order}}

{{cutting/protected-sentences}}

### Making the cut

{{cutting/sentence-dependencies}}

{{cutting/stop-rules}}

{{cutting/post-cut-check}}

## Prose

{{prose/explanation-order}}

{{prose/deletion-test}}

### Paragraphs

{{prose/paragraph-development}}

{{prose/list-structure}}

{{prose/transitions}}

{{prose/topic-order}}

{{prose/topic-string}}

### Information flow within a sentence

{{prose/old-before-new}}

{{prose/stress-position}}

{{prose/passives-fronting-inversions}}

### Sentence structure

{{prose/character-action}}

{{prose/first-reading}}

{{prose/read-aloud}}

{{prose/parallel-form}}

{{prose/sentence-initial-conjunctions}}

### Content instead of promises

{{prose/direct-content}}

{{prose/reporting-policies}}

{{prose/signposts}}

{{prose/choice-reasons}}

### Concrete quantities and operations

{{prose/empty-verbs}}

{{prose/umbrella-nouns}}

{{prose/quantified-comparatives}}

{{prose/intensifiers}}

### Plain wording

{{prose/literal-wording}}

{{prose/logical-words}}

{{prose/definitions-procedures}}

{{prose/referents}}

{{prose/writerly-asides}}

## Conventions

When a convention in this section conflicts with general writing advice, follow the convention.

### Voice and tense

{{conventions/active-voice}}

{{conventions/performed-actions}}

{{conventions/tense}}

### Terminology

{{conventions/term-consistency}}

{{conventions/parts-of-speech}}

{{conventions/acronyms}}

{{conventions/shorthand-reminders}}

{{conventions/suggestive-terms}}

### Mathematics

{{conventions/symbol-definitions}}

{{conventions/math-prose}}

{{conventions/formal-material-purpose}}

{{conventions/math-typography}}

{{conventions/display-numbering}}

{{conventions/theorem-statements}}

{{conventions/proof-strategy}}

### Citations, figures, and tables

{{conventions/citation-markers}}

{{conventions/missing-citations}}

{{conventions/captions}}

{{conventions/figure-table-references}}

### Typography

{{conventions/quantities}}

{{conventions/marks-and-forms}}

## Deslopping

Patterns common in AI-written prose fall into two groups:

1. **Blacklisted patterns.** Delete every instance, even a single one. The three-instance threshold below does not apply.
2. **Tolerable patterns.** Edit a single instance when the edit makes the sentence clearer. Rewrite a whole passage only when it contains three or more instances of tolerable patterns.

{{deslopping/author-voice}}

### Blacklisted patterns

{{deslopping/em-dashes}}

{{deslopping/chatbot-phrases}}

{{deslopping/generic-openings-closings}}

{{deslopping/generation-artifacts}}

### Tolerable patterns

{{deslopping/prose-rule-patterns}}

{{deslopping/compressed-constructions}}

{{deslopping/pause-punctuation}}

{{deslopping/reasoning-leakage}}

{{deslopping/revision-narration}}

{{deslopping/vague-attribution}}

{{deslopping/negative-parallelism}}

{{deslopping/false-concession}}

{{deslopping/rule-of-three}}

{{deslopping/false-ranges}}

{{deslopping/transition-chains}}

{{deslopping/copula-avoidance}}

{{deslopping/trailing-ing}}

{{deslopping/self-labeling}}

{{deslopping/rhetorical-questions}}

{{deslopping/repetitive-syntax}}

{{deslopping/significance-inflation}}

{{deslopping/aphorisms}}

{{deslopping/relentless-positivity}}
