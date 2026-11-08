# Writing guide

This guide is generated from a collection of writing rules. Each rule has its own page in the `rules/` folder next to this guide and follows this format:

```markdown
# {{ Name of the rule }}

{{ A summary of the rule: what to look for, the edit or flag that it calls for, and the exceptions that change the edit. }}

## Details

{{ Explanation, further cases, and procedures omitted from the summary for concision, or, if there are none, the sentence "This rule needs no details beyond its summary." }}

## Examples

{{ Optional context that the example needs. }}

> Bad: {{ A passage that breaks the rule. }}
>
> Good: {{ The same passage, corrected under this rule alone. }}
```

The guide below reproduces each rule's heading and summary; each rule page adds `Details` and at least one example. Read a rule page in full when the rule applies to the text you are editing and the summary does not settle the edit, or when the summary names a case that its page covers. Each example illustrates one edit under its rule and does not widen what the request permits you to change.

## Table of contents

The guide has six sections of rules:

- [Story](#story): the argument from problem to implication, titles and headings, section order and openings, contributions, related work, results organized by question, and numbers that support claims.
- [Claims](#claims): reporting verbs that match claims to their evidence, scope, overclaiming and underclaiming, consistency across the text, causal language, what an efficiency claim counts, statistical significance, hedges, speculation, and limitations.
- [Cutting](#cutting): what to delete or relocate without a separate request from the author, the triage order under a length limit, what to protect, and how to repair the text around a cut.
- [Prose](#prose): explanation order, paragraphs, information flow, sentence structure, direct content in place of promises, concrete quantities, and plain wording.
- [Conventions](#conventions): voice, tense, terminology, mathematics, citations and credit, figures and tables, typography, and LaTeX source.
- [Deslopping](#deslopping): two tiers of patterns common in AI-written prose.

When a request is narrower than a full polish, apply the sections it names and every rule they link to. Check each chunk against every rule in each applicable section. When two rules prescribe different edits for the same sentence and one links to the other, follow the linked rule. Otherwise, choose the clearer sentence; if both are equally clear, use your judgment as an expert editor.

## Story

Organize the text around one argument: a problem the reader cares about, a gap with a cost, an idea that closes the gap, evidence that the idea works, and the implication. Check this argument across the whole text and its sections before editing individual sentences, because sentence-level edits cannot repair a broken argument. Use the [rules on claims](#claims) to set each statement's strength, the [rules on cutting](#cutting) to decide what stays, and the [rules on prose](#prose) to edit paragraphs and sentences.

Without a separate request from the author, you may:

- Reorder sentences within a paragraph or paragraphs within a section to put the claim first.
- Rewrite a section's opening using content already in that section.
- Remove numbers from running text when a table already contains them.
- Rewrite a caption to state a conclusion already drawn in the body text.

Flag any changes to the text's claims, section order, or list of contributions instead of making them yourself. Never supply a cost, explanation, or number that the draft does not contain.

### The whole argument

{{story/five-line-summary}}

{{story/one-sentence-summary}}

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

{{story/section-connections}}

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

The most common flaw in the argument of AI-generated text is burying the point in the results. Reorder the text so that every number supports a claim already stated in words.

{{story/claim-before-number}}

{{story/headline-number}}

{{story/number-precision}}

### Discussion and conclusion

{{story/return-to-gap}}

{{story/conclusion-perspective}}

## Claims

Every claim must match its evidence: both overclaiming and underclaiming are errors. An aspirational goal may motivate the work as long as the text states that the goal remains unattained.

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

Use the [spine test](rules/cutting/spine-test.md) to determine what the argument needs, and check the request to see what you may delete or relocate.

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

{{prose/parallel-form}}

{{prose/sentence-initial-conjunctions}}

{{prose/read-aloud}}

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

{{prose/ambiguous-this}}

{{prose/writerly-asides}}

## Conventions

These conventions override generic writing advice.

### Voice and tense

{{conventions/active-voice}}

{{conventions/performed-actions}}

{{conventions/tense}}

### Terminology

{{conventions/term-consistency}}

{{conventions/parts-of-speech}}

{{conventions/acronyms}}

{{conventions/spelling}}

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

{{conventions/hyphens}}

{{conventions/number-forms}}

{{conventions/latin-abbreviations}}

{{conventions/nonrestrictive-commas}}

{{conventions/punctuation-typography}}

{{conventions/units}}

{{conventions/latex-boundaries}}

## Deslopping

Divide recognizable patterns of AI-written prose into two tiers:

1. **Blacklisted patterns.** Delete every instance; the threshold for tolerable patterns below does not apply.
2. **Tolerable patterns.** Treat all other patterns in this section as tolerable. Edit a single instance when doing so improves the sentence itself, and rewrite a whole passage only when it contains three or more instances of tolerable patterns.

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
