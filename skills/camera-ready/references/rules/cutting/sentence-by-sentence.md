# Cut sentence by sentence, repairing what each cut breaks

For each sentence in a surviving paragraph, ask these questions in order:

1. **Does the spine need it?** If the sentence supports no central claim, consider deleting or relocating it according to steps 2 to 4.
2. **Does the reader need it?** A sentence can add no new claim and still be [protected](protect.md) because it frames the argument, connects ideas, calibrates a claim, or orients the reader.
3. **What breaks without it?** Check later passages for dependencies: a later "this" or "as shown above", a citation or term that appears only here, a claim whose hedge or evidence is in this sentence, or the paragraph's topic string. Repair every dependency in the same edit or keep the sentence.
4. **Delete or relocate?** Delete content that no reader needs. Relocate it to an appendix, supplement, or footnote when only a minority of readers, or one skeptical reviewer, needs it. Reproducibility content is [protected](protect.md): relocate it, never delete it. Use an appendix or supplement only if it already exists; otherwise leave the content in place and flag what the appendix or supplement would need to contain. A footnote may be new.
5. **Read across the gap.** Read the sentences before and after the gap together. The second must open with a term, result, or referent supplied by the first. If the link requires an inference that the deleted sentence made, add a clause to an adjacent sentence to restore it, or reuse the original framing sentence to open what follows.

## Examples

- Before: "We also sweep the learning rate over five values; 3e-4 is best. We use it for all remaining experiments."
- Bad: "We use it for all remaining experiments." ("it" now points at nothing.)
- Good: "We use a learning rate of 3e-4 for all remaining experiments (sweep in Appendix B)."
