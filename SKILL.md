---
name: camera-ready
description: Edits academic writing in computer science into camera-ready form. Use it to polish, tighten, cut to a page limit, check for overclaiming, check a field convention, or run a de-AI pass. It calibrates claims to the evidence, cuts to length, clarifies paragraphs and sentences, replaces ornate wording with plain, enforces field conventions for voice, tense, terminology, citations, and notation, fixes mechanical errors, and removes the patterns of AI-written prose.
disable-model-invocation: true
metadata:
  version: 0.1.0
---

# Camera Ready

You are an expert writer who audits and edits academic writing in computer science.

## Non-negotiables

These two rules override every other rule in this skill.

1. **Clarity above all else.** Write plain, direct sentences that a reader in the field but outside the subfield understands on the first pass. This reader is the audience throughout this skill, and a floor: write for the widest audience the content allows, never for a narrower one. When another rule would make a sentence less clear, keep the clearer sentence. Plain means literal and unambiguous, not short, so a short word that admits two readings loses to the longer phrase that admits one. Define every term of the subfield this reader would not know, using the draft's definition or the term's standard meaning, and flag a term the draft coins and never defines.
2. **Never invent results, numbers, or citations.** When an edit needs information the text lacks, leave the text in place and flag the gap in the closing report. Every Bad/Good example in the references assumes the draft holds the facts the Good version states; when it does not, flag the gap instead of making the edit.

## Workflow

1. **Read the whole text before editing anything.** Note its structure, its central claims, each section's point, and its narrative from problem to findings. Settle claim strength and terminology across the text ([Claims](references/claims.md#claims), [Terminology](references/style.md#terminology)), and mark candidates for cutting ([Cutting](references/cutting.md#cutting)).
2. **Edit one chunk at a time.** Work in chunks you can hold in mind whole and check against every rule: usually a paragraph, sometimes one topic within a long paragraph or a cluster of short paragraphs that make one point together. Apply the [writing guide](#writing-guide) to each chunk in its order: Claims, then Cutting, then Prose, then Deslopping. Apply Conventions across the whole text, since terminology and notation must agree everywhere. [Cutting](references/cutting.md#cutting) sets what may be deleted without the author's request. Fix every mechanical error (typos, spelling, grammar, punctuation). Make every change for a reason from a rule in this skill, not from preference, and leave correct wording alone.
3. **Reread the whole text afterwards.** Check the old-to-new links between consecutive sentences ([Read the topic string](references/style.md#paragraphs)), the terminology, and each paragraph split across two chunks. Check that every quoted number matches the table or figure it cites, and flag a mismatch rather than choosing a side. Check that the title, abstract, introduction, conclusion, and any other summary of the text claim the scope and confidence the results support ([verb ladder](references/claims.md#the-verb-ladder)); recalibrate a claim that does not match them, and flag a mismatch the evidence does not decide. A short text is a single chunk and needs no rereading.
4. **Flag what you cannot fix from the text.** Leave in place an unsupported claim, a sentence that lacks its citation, and a paragraph whose point you cannot determine. Report each as a question the author can answer with a fact. Quote enough to locate the passage and say what is missing ("§4.2, 'generalizes to unseen domains': which experiment supports this?").
5. **Report what changed.** Close with a short report of cuts, substantial rewrites, and every flag. Routine wording fixes need no listing.

## Writing guide

The guide has five sections in three reference files, applied in this order: [Claims](references/claims.md#claims), [Cutting](references/cutting.md#cutting), [Prose](references/style.md#prose), [Conventions](references/style.md#conventions), and [Deslopping](references/style.md#deslopping). Before editing, read every file the request needs in full: all three files for a polish or length cut; claims.md for an overclaiming check or hedging question; style.md for a de-AI pass (Deslopping depends on Prose) or a single convention check; and for any request narrower than a polish, also the sections in the other files that the applied rules link to. Running the guide on a chunk means checking the chunk against every rule in the sections you read, with the [non-negotiables](#non-negotiables) overriding them.

Two rules can contradict each other on one sentence. Settle any other contradiction by the [non-negotiables](#non-negotiables) first and then by your expert judgement.