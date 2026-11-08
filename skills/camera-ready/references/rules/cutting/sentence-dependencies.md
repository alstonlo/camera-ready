# Repair dependencies when cutting or relocating sentences

For each sentence within [the request's scope](idea-cuts.md), follow four steps:

1. **Check its role.** Ask whether a core claim or the reader needs the sentence, and apply "Protect sentences the argument depends on" before considering deletion.
2. **Check dependencies.** Check whether other text depends on the sentence through a later reference such as "this" or "as shown above", a term defined or citation supplied only here, a hedge or piece of evidence for a claim elsewhere, or the paragraph's topic string. Repair every dependency in the same edit, or keep the sentence.
3. **Choose deletion or relocation.** Delete only content that no reader needs. Relocate content that only some readers or a skeptical reviewer will need, and never delete details needed for reproducibility. Move material to an appendix or supplement only if that destination already exists; otherwise, keep the material in place and flag what the destination would need to contain. Make relocated material understandable on its own, point to it from the relevant place in the main text, and keep enough of the method and rationale in the main text for readers to judge the results. If the venue permits footnotes, you may move subsidiary comments into footnotes. Keep essential steps of a method, derivation, or algorithm in the main explanation, along with definitions used later; see the page for parenthetical asides.
4. **Read across the gap.** Confirm that the sentence after the gap opens with a referent or result supplied by the remaining text. Restore any lost link using content from the draft, or keep the original framing sentence.

## Details

Check for dependencies throughout the rest of the text, not only in the sentence immediately after the gap. When pointing to a large supplement, name the specific section, figure, or procedure rather than the supplement as a whole, and never guess a section number.

Keep an essential step or the only definition of a term used later out of footnotes and parenthetical asides. Move that material into the main explanation when relocation is authorized, or flag its placement if not. A brief notation definition may remain in parentheses when it is clear and easy to find.

## Examples

A length cut removes the preceding sentence, which reported that the blue dye was easiest to see.

> Bad: We use it for all remaining experiments.
>
> Good: Because the blue dye was easiest to see, we use it for all remaining experiments.

A cut removes "Recovery time R is the time to return to 20 °C.", the draft's only definition of R, even though later sections use R.

> Bad: We record R after each trial.
>
> Good: Recovery time R is the time to return to 20 °C. We record R after each trial.

The author authorizes relocation, and the full protocol appears in Section S2 of an existing supplement.

> Bad: We dry each sample at 30 °C using the protocol in the supplement.
>
> Good: We dry each sample at 30 °C using the protocol in Supplement Section S2.

The author authorizes relocation. This sentence opens the relocated protocol, and the step that preceded it in the draft was rinsing the tray.

> Bad: We repeat this step twice.
>
> Good: We rinse the tray twice.

The draft states, "We calibrate at 0 °C and 20 °C." A proposed length cut replaces that sentence with a pointer to Appendix A, even though the draft has no appendix.

> Bad: The calibration settings appear in Appendix A.
>
> Good: We calibrate at 0 °C and 20 °C.

The author authorizes relocation, and the draft identifies removing the cap as an essential step.

> Bad: We heat the sample (first removing the cap).
>
> Good: We remove the cap, then heat the sample.

The author authorizes relocation, the venue permits footnotes, and the comment about the supplier is subsidiary. The example is in LaTeX source.

> Bad: We use glass jars. The supplier also sells lids separately.
>
> Good: We use glass jars.\footnote{The supplier also sells lids separately.}
