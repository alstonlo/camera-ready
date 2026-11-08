# Comparing with prior work

- **Compare, do not list.** End each paragraph or group of paragraphs on prior work by stating how this work differs on a named dimension (an assumption, a metric, a cost, a setting, or a guarantee). Use terms the reader can check. If the draft does not state the difference, flag it rather than supplying one.
- **Characterize prior work in its own terms.** State what a cited work does and under what assumptions before describing what it lacks for this work's setting. Do not describe a difference in scope as a defect ("ignores", "fails to") unless the draft shows the failure. Preserve the sentence crediting the predecessor, which is [protected](../cutting/protect.md). Retain the cited work's own strength of claim; if the source says its results suggest X, do not write that it shows X.
- **Mark what is new.** When a passage combines the text's own contribution with standard or borrowed components, distinguish them clearly ("we use the probe of Smith et al. [4]; our change is to ..."). If the text leaves the novelty ambiguous, flag it rather than deciding it.

A comparison that is vague on both sides is the [false concession](../deslopping/false-concession.md) pattern. Leave the related-work section where it is, and flag it only when it comes before the method and cannot be understood without it.

## Examples

- Bad: "Gradient caching [12] reduces memory. Memory-efficient attention [8] reduces memory. Our method reduces memory."
- Good: "Gradient caching [12] and memory-efficient attention [8] both reduce training memory, the first by recomputing representations in a second forward pass and the second by tiling the attention computation. Our method also reduces training memory but needs no second forward pass."
