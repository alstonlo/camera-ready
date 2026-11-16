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

{{cuts/bloat}}

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

### Mechanics

{{conventions/style-choices}}

{{conventions/units-and-numbers}}

## AI patterns

Patterns common in AI-written prose, called AI slop, fall into two groups:

1. **Blacklisted patterns.** Remove every instance, even a single one, or flag it where the rule says to. The three-instance threshold below does not apply.
2. **Tolerable patterns.** Edit a single instance when the edit makes the sentence clearer. Rewrite a whole passage only when it contains three or more instances of tolerable patterns.

{{slop/author-voice}}

### Blacklisted patterns

{{slop/em-dashes}}

{{slop/chatbot-phrases}}

{{slop/generic-openings-closings}}

{{slop/generation-artifacts}}

### Tolerable patterns

{{slop/prose-rule-patterns}}

{{slop/compressed-constructions}}

{{slop/pause-punctuation}}

{{slop/reasoning-leakage}}

{{slop/revision-narration}}

{{slop/vague-attribution}}

{{slop/negative-parallelism}}

{{slop/false-concession}}

{{slop/rule-of-three}}

{{slop/false-ranges}}

{{slop/transition-chains}}

{{slop/copula-avoidance}}

{{slop/trailing-ing}}

{{slop/self-labeling}}

{{slop/rhetorical-questions}}

{{slop/repetitive-syntax}}

{{slop/significance-inflation}}

{{slop/aphorisms}}

{{slop/relentless-positivity}}
