# Writing guide

This guide is generated from a collection of writing rules. Each rule has its own page in the folder `rules/` next to this guide, and every page has the following format:

```markdown
# {{ Name of the rule }}

{{ A summary of the rule: what to look for, the edit or flag it calls for, and the exceptions that change the edit. }}

## Details

{{ Optional explanation, further cases, and procedures, omitted from the summary for concision. }}

## Examples

{{ Optional context that the example needs. }}

- Bad: {{ A passage that breaks the rule. }}
- Good: {{ The same passage, corrected under this rule alone. }}
```

The guide below reproduces each rule's heading and summary. Every rule page has at least one example, and some pages also have Details. Read a rule page fully when the rule applies to the text being edited and its summary does not settle the edit, or when the summary names a case that its page covers. An example shows one edit under its rule; it does not widen what the request lets you change.

## Table of contents

The guide has six sections of rules:

- [Story](#story): the argument from problem to implication, the title and headings, section order and openings, contributions, related work, results organized by questions, and numbers that support claims.
- [Claims](#claims): match each claim to its evidence by checking the reporting verb, scope, over- and underclaiming, consistency across the text, causal language, what an efficiency claim counts, significance, hedges, speculation, and limitations.
- [Cutting](#cutting): what may be deleted or relocated without the author's request, the triage order under a length limit, what to protect, and how to repair the text around a cut.
- [Prose](#prose): ordering, paragraphs, information flow, sentence structure, content in place of promises, concrete quantities, and plain wording.
- [Conventions](#conventions): voice, tense, terminology, mathematics, citations and credit, figures and tables, typography, and LaTeX source.
- [Deslopping](#deslopping): the patterns of AI-written prose, in two tiers.

For a request narrower than a polish, apply the sections the request names and every rule linked from them. Check each chunk against every rule in each applicable section. If two rules prescribe different edits for one sentence and one links to the other, follow the linked rule. Otherwise choose the clearer sentence; if both are equally clear, use your judgment as an expert editor.

## Story

Organize the text around one argument: a problem the reader cares about, a gap with a cost, an idea that closes the gap, evidence that the idea works, and the implication. Check this argument across the whole text and its sections before editing sentences, because sentence edits cannot repair a broken argument. Use the [rules on claims](#claims) to set each statement's strength, the [rules on cutting](#cutting) to decide what stays, and the [rules on prose](#prose) to edit paragraphs and sentences.

Without a separate request from the author, you may:

- Reorder sentences within a paragraph or paragraphs within a section to put the claim first.
- Rewrite a section's opening using content already in that section.
- Remove numbers from running text when a table already contains them.
- Rewrite a caption to state a conclusion already drawn in the body text.

Flag changes to the text's claims, section order, or list of contributions instead of making them. Never supply a cost, explanation, or number that the text lacks.

### The whole argument

{{story/five-line-summary}}

{{story/one-sentence-summary}}

{{story/section-stages}}

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

{{story/prior-work}}

{{story/novelty}}

{{story/related-work-placement}}

### Results

{{story/results-by-question}}

{{story/one-question-per-paragraph}}

{{story/explain-evidence}}

{{story/source-of-gain}}

### Numbers

The most common failure in the argument of AI-generated text is to obscure the point with results. Correct the order so that every number supports a claim stated first in words.

{{story/claim-before-number}}

{{story/headline-number}}

{{story/precision}}

### Discussion and conclusion

{{story/return-to-gap}}

{{story/conclusion-perspective}}

## Claims

Every claim must match its evidence. Both overclaiming and underclaiming are errors. An aspirational goal may motivate the text if the text states that the goal remains unattained.

### Strength and scope

{{claims/verb-ladder}}

{{claims/scope}}

{{claims/overclaiming}}

{{claims/underclaiming}}

{{claims/consistency}}

### Causation and formal support

{{claims/causal-language}}

{{claims/formal-informal}}

{{claims/cost-model}}

### Numerical comparisons

{{claims/uncertainty}}

{{claims/significance}}

### Qualification and limits

{{claims/hedges}}

{{claims/speculation}}

{{claims/limitations}}

## Cutting

Use the [spine test](rules/cutting/spine-test.md) to determine what the text needs, and use the request to determine what you may delete or relocate.

### Deciding what to cut

{{cutting/bloat}}

{{cutting/idea-level}}

{{cutting/spine-test}}

{{cutting/triage-order}}

{{cutting/protect}}

### Making the cut

{{cutting/sentence-by-sentence}}

{{cutting/stop-rules}}

{{cutting/after-the-pass}}

## Prose

{{prose/build-understanding-early}}

{{prose/deletion-test}}

### Paragraphs

{{prose/paragraphs}}

{{prose/list-structure}}

{{prose/transitions}}

{{prose/topic-order}}

{{prose/topic-string}}

### Information flow within a sentence

{{prose/old-before-new}}

{{prose/stress-position}}

{{prose/other-sentence-orders}}

### Sentence structure

{{prose/character-action}}

{{prose/first-reading}}

{{prose/parallel-form}}

{{prose/sentence-initial-conjunctions}}

{{prose/read-aloud}}

### Content instead of promises

{{prose/direct-content}}

{{prose/policy-for-finding}}

{{prose/signposts}}

{{prose/reasons}}

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

{{conventions/voice}}

{{conventions/actions}}

{{conventions/tense}}

### Terminology

{{conventions/terminology}}

{{conventions/parts-of-speech}}

{{conventions/acronyms}}

{{conventions/spelling}}

{{conventions/refresh-shorthand}}

{{conventions/suggestive-terms}}

### Mathematics

{{conventions/notation}}

{{conventions/math-prose}}

{{conventions/equation-meaning}}

{{conventions/math-type}}

{{conventions/displays}}

{{conventions/theorems}}

{{conventions/proofs}}

### Citations, figures, and tables

{{conventions/citation-markers}}

{{conventions/source-attribution}}

{{conventions/figures-tables}}

{{conventions/float-refs}}

### Typography

{{conventions/hyphens}}

{{conventions/number-forms}}

{{conventions/latin-abbreviations}}

{{conventions/clause-commas}}

{{conventions/formal-marks}}

{{conventions/units}}

{{conventions/latex-boundaries}}

## Deslopping

Classify recognizable patterns of AI-written prose in two tiers.

1. **Blacklisted patterns.** Delete every instance, regardless of the threshold for tolerable patterns below.
2. **Tolerable patterns.** All other patterns are tolerable. Edit an instance when doing so improves the sentence itself. Rewrite a whole passage only when it contains three or more instances of tolerable patterns.

{{deslopping/author-voice}}

### Blacklisted patterns

{{deslopping/em-dashes}}

{{deslopping/chatbot-artifacts}}

{{deslopping/generic-openings}}

{{deslopping/leaked-artifacts}}

### Tolerable patterns

{{deslopping/prose-rule-patterns}}

{{deslopping/compressed-constructions}}

{{deslopping/pause-punctuation}}

{{deslopping/reasoning-leakage}}

{{deslopping/diff-anchored-prose}}

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

{{deslopping/uniform-rhythm}}

{{deslopping/significance-inflation}}

{{deslopping/aphorisms}}

{{deslopping/relentless-positivity}}
