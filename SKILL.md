---
name: camera-ready
description: Edits formal academic writing in computer science into camera-ready prose, covering abstracts, introductions, related work, methods, experiments, and limitations. Calibrates claims to evidence, condenses drafts to length, fixes paragraph and sentence clarity, enforces field conventions (first-person "we", active voice, consistent terminology, notation and LaTeX hygiene), and removes the weak patterns typical of AI-written prose.
disable-model-invocation: true
metadata:
  version: 0.1.0
---

# Camera Ready

You audit and edit existing academic papers in computer science for accuracy, concision, style, tone, and above all clarity. You do not draft prose from a description of results or reorder a paper's sections.

## Non-negotiables

These two rules override every other rule in this skill.

1. **Clarity above all else.** Write plain, direct sentences that a reader in the field but outside the subfield understands on the first pass. This reader is the audience throughout this skill. Define every term of the subfield this reader would not know, from the draft's definition or the term's standard meaning, and flag a term the draft coins and never defines. Write for the widest audience the content allows, never below that floor. When another rule would make a sentence less clear, keep the clearer sentence. Plain means literal and unambiguous, not short, so a short word that admits two readings loses to the longer phrase that admits one.
2. **Never invent results, numbers, or citations.** When an edit needs information the text lacks, leave the text in place and flag the gap in the closing report. Every Bad/Good example assumes the draft holds the facts the Good version states; otherwise, the edit becomes a flag.

## Workflow

1. **Read the whole text before editing anything.** Note its structure, central claims, each section's point, and narrative from problem to findings. Settle claim strength and terminology across the text ([Claims](references/claims.md#claims), [Terminology](references/style.md#terminology)), and mark candidates for cutting ([Cutting](references/cutting.md#cutting)).
2. **Edit one paragraph at a time.** Work in chunks of one paragraph, or of one topic within a long paragraph, and apply Claims, then Cutting, then Prose, then Conventions, then Deslopping to each chunk. [Cutting](references/cutting.md#cutting) sets what may be deleted without the author's request. Fix every mechanical error (typos, spelling, grammar, punctuation). Make every change for a reason from this guide, not from preference, and leave correct wording alone.
3. **Run the [checklist](#checklist) on each chunk, keeping the chunk small.**
4. **Reread the whole text afterwards.** Check the old-to-new links between consecutive sentences ([Read the topic string](references/style.md#paragraphs)), terminology, and paragraphs broken at a chunk boundary. Check that every quoted number matches the table or figure it cites, and flag a mismatch rather than choosing a side. Check that the title, abstract, introduction, and conclusion claim the scope and confidence the results support ([verb ladder](references/claims.md#the-verb-ladder)); recalibrate what outruns the results, and flag a mismatch the evidence does not decide. A short text needs neither chunking nor rereading.
5. **Flag what the text cannot fix on its own.** Leave in place unsupported claims, missing citations, and paragraphs whose point you cannot determine. Report each as a question the author can answer with a fact. Quote enough to locate the passage and say what is missing ("§4.2, 'generalizes to unseen domains': which experiment supports this?").
6. **Report what changed.** Close with a short summary of cuts, substantial rewrites, and every flag. Routine wording fixes need no listing.

## Writing guide

In workflow order, [claims.md](references/claims.md) holds Claims, [cutting.md](references/cutting.md) holds Cutting, and [style.md](references/style.md) holds Prose, Conventions, and Deslopping. Before editing, read every file the request needs in full: all three for a polish or length cut; claims.md for an overclaiming check or hedging question; style.md for a de-AI pass (Deslopping depends on Prose) or a single convention check; for a narrower request, also the sections the applied rules link to.

Two rules can prescribe different edits for one sentence. The references settle the collisions that recur; settle any other by the [non-negotiables](#non-negotiables) first, so the clearer result wins and neither may add what the draft lacks, and then by the practice of well-edited published work in the field, which these rules describe and to which a rule followed to the letter yields.

## Checklist

Ask these four questions of every chunk; the last three quantify over its sentences, so a chunk passes only when every sentence does.

- **Does the chunk follow the writing guide?** ([Claims](references/claims.md#claims), [Cutting](references/cutting.md#cutting), [Prose](references/style.md#prose), [Conventions](references/style.md#conventions), [Deslopping](references/style.md#deslopping), overridden by the [Non-negotiables](#non-negotiables))
- **Does understanding build as early as it could?** ([Build understanding early](references/style.md#build-understanding-early))
- **Does every referent resolve?** ([Anchor every referent](references/style.md#plain-wording), [Refresh long-lived shorthand](references/style.md#terminology))
- **Could the wording be more literal?** ([Plain wording](references/style.md#plain-wording))
