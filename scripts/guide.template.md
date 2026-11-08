# Writing guide

This guide is generated from rule pages, one page per rule. The pages are in the folder `rules/` next to this guide, with one subfolder for each section of the guide. Each page has the following format, in which the Details and Examples sections are optional:

```markdown
# <Name of the rule>

<The rule: one or more paragraphs or a list.>

## Details

<An explanation of the rule and its harder cases.>

## Examples

<Bad and Good versions of a passage.>
```

The guide copies each page's heading and rule text. In the guide, each rule begins with its name in bold as a link to the rule's page. The text after the name is the complete rule; follow it as written here. The Details and Examples sections explain the rule but never add a requirement. Open a rule's page only when the rule applies to the passage you are editing and its text in this guide leaves you unsure how to apply it. A link within the rule text points to another rule's page. That rule also appears in this guide under its name in bold.

## Table of contents

Below, the guide has six sections of rules:

- [Story](#story): the argument from problem to implication, section order and openings, contributions, results organized by questions, and numbers that support claims.
- [Claims](#claims): match each claim to its evidence by checking the reporting verb, scope, causal language, significance, hedges, over- and underclaiming, speculation, and limitations.
- [Cutting](#cutting): what may be deleted or relocated without the author's request, the triage order under a length limit, what to protect, and how to repair the text around a cut.
- [Prose](#prose): ordering, paragraphs, information flow, sentence structure, concision, plain wording, and comparison with prior work.
- [Conventions](#conventions): voice, tense, terminology, citations, notation, figures and tables, and typography.
- [Deslopping](#deslopping): the patterns of AI-written prose, in two tiers.

For a request narrower than a polish, apply the sections the request names and every rule linked from them. Check each chunk against every rule in the applicable section. If two rules prescribe different edits for one sentence and one links to the other, follow the linked rule. Otherwise choose the clearer sentence; if both are equally clear, use your judgment as an expert editor.

## Story

Organize the text around one argument: a problem the reader cares about, a gap with a cost, an idea that closes the gap, evidence that the idea works, and the implication. Check this argument across the whole text and its sections before editing sentences, since sentence edits cannot repair a broken argument. Use the [rules on claims](#claims) to set each statement's strength, the [rules on cutting](#cutting) to decide what stays, and the [rules on prose](#prose) to edit paragraphs and sentences.

Without the author's request, you may:

- Reorder sentences within a paragraph or paragraphs within a section to put the claim first.
- Rewrite a section's opening using content already in that section.
- Remove numbers from running text when a table already contains them.
- Rewrite a caption to state a conclusion already drawn in the body text.

Flag changes to the text's claims, section order, or list of contributions instead of making them. Never supply a cost, explanation, or number that the text lacks.

### The arc

{{story/five-line-summary}}

{{story/one-sentence-summary}}

{{story/section-stages}}

{{story/linear-argument}}

{{story/skim-test}}

### Problem and gap

{{story/open-with-problem}}

{{story/gap-cost}}

{{story/why-hard}}

### Contributions

{{story/contribution-claims}}

{{story/contribution-sections}}

### Sections

{{story/section-openings}}

{{story/section-connections}}

{{story/related-work-placement}}

### Evidence

{{story/results-by-question}}

{{story/one-question-per-paragraph}}

{{story/explain-evidence}}

{{story/source-of-gain}}

### Numbers

The most common failure in the argument of generated text is to obscure the point with results. Correct the order so that every number supports a claim stated first in words.

{{story/claim-before-number}}

{{story/headline-number}}

{{story/no-restated-table}}

{{story/numbers-to-claims}}

{{story/precision}}

{{story/caption-conclusion}}

### Endings

{{story/return-to-gap}}

{{story/conclusion-perspective}}

## Claims

Every claim must match its evidence. Both overclaiming and underclaiming are errors. An aspirational goal may motivate the text if the text states that the goal remains unattained.

### The verb ladder

{{claims/verb-ladder}}

### Scope

{{claims/scope}}

### Causal language

{{claims/causal-language}}

### Formal and informal claims

{{claims/formal-informal}}

### Uncertainty and significance

{{claims/uncertainty}}

### Hedges

{{claims/hedges}}

### Failure modes

{{claims/overclaiming}}

{{claims/underclaiming}}

### Speculation

{{claims/speculation}}

### Limitations

{{claims/limitations}}

## Cutting

Use the [spine test](#the-spine-test) to determine what the text needs and the request to determine what you may delete or relocate.

{{cutting/bloat}}

{{cutting/idea-level}}

### The spine test

{{cutting/spine-test}}

### Triage order

{{cutting/triage-order}}

### Protect

{{cutting/protect}}

### Sentence by sentence

{{cutting/sentence-by-sentence}}

### Stop rules

{{cutting/stop-rules}}

### After the pass

{{cutting/after-the-pass}}

## Prose

### Build understanding early

{{prose/build-understanding-early}}

### Paragraphs

{{prose/paragraphs}}

{{prose/topic-string}}

### Information flow within a sentence

{{prose/old-before-new}}

{{prose/stress-position}}

{{prose/other-sentence-orders}}

### Sentence structure

{{prose/character-action}}

{{prose/first-reading}}

{{prose/sentence-initial-conjunctions}}

{{prose/read-aloud}}

### Concision

{{prose/deletion-test}}

{{prose/direct-content}}

{{prose/policy-for-finding}}

{{prose/empty-verbs}}

{{prose/umbrella-nouns}}

{{prose/signposts}}

{{prose/intensifiers}}

### Plain wording

{{prose/literal-wording}}

{{prose/logical-words}}

{{prose/definitions-procedures}}

{{prose/referents}}

{{prose/ambiguous-this}}

{{prose/writerly-asides}}

{{prose/quantified-comparatives}}

{{prose/reasons}}

### Comparing with prior work

{{prose/prior-work}}

## Conventions

These conventions override generic writing advice.

### Voice and person

{{conventions/voice}}

### Tense

{{conventions/tense}}

### Terminology

{{conventions/terminology}}

{{conventions/refresh-shorthand}}

{{conventions/suggestive-terms}}

### Citation markers are not nouns

{{conventions/citation-markers}}

### Notation and equations

{{conventions/notation}}

### Figures and tables

{{conventions/figures-tables}}

### Typography and small style

{{conventions/typography}}

## Deslopping

Classify recognizable patterns of AI-written prose in two tiers.

1. **Blacklisted patterns.** Delete every instance, regardless of the co-occurrence test in tier two.
2. **Tolerable patterns.** All other patterns are tolerable. Edit one when doing so improves the sentence itself. Rewrite a whole passage only when it contains three or more tolerable instances.

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
