# Read the topic string

When individual sentences are clear but the paragraph does not cohere, list the opening of each sentence. This list is the paragraph's topic string. If most openings introduce new material, rewrite so that each sentence [opens with old information](../../references/guide.md#information-flow-within-a-sentence). Then test each sentence boundary by inserting the implied connective in brackets ("[however]", "[therefore]"). If no connective fits, or you cannot determine which fits, the link is missing. Supply it if the text states it elsewhere; otherwise flag it. If "[therefore]" fits but the reader outside the subfield could not explain why the second sentence follows, flag the missing step in the argument. Inserting the connective cannot supply that step. Finally, check that each new term in a sentence's stress position is used later, unless it is the paragraph's conclusion.

If two adjacent paragraphs can exchange places without further edits, determine whether the section lists parallel items. If so, add a [summary sentence](../../references/guide.md#concision) naming them. Otherwise revise the second paragraph to state how it depends on the first.

## Examples

- Bad: "Contrastive pretraining needs large batches. Memory limits batch size on a single GPU. Gradient caching was proposed by Gao et al. (2021). Our method reaches the same accuracy at batch size 256."
- Good: "Contrastive pretraining needs large batches, but memory limits the batch size on a single GPU. This limit is removed by gradient caching (Gao et al., 2021), which recomputes representations in a second forward pass. Our method also removes the limit, without the second pass, and at batch size 256 it matches the accuracy of gradient caching."
