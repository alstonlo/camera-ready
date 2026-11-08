# Replace reasoning-chain leakage with conclusions and evidence

Replace "Let us think step by step", "Breaking this down", and numbered internal monologues with the conclusion and evidence. Preserve mathematical setup such as "Let X be", proof steps, and substantive reasoning that justifies the result.

## Details

Keep a model's reasoning trace when the paper quotes or analyzes it as experimental material.

## Examples

> **Bad.** Let us think step by step. The load exceeds the shelf limit by 4 kg.
>
> **Good.** The load exceeds the shelf limit by 4 kg.

> **Bad.** First, I should compare the load and the limit. Next, I can conclude that the load exceeds the limit by 4 kg.
>
> **Good.** The load exceeds the limit by 4 kg.

> **Bad.** Let us think step by step. Let n be an even integer. Then n = 2k for some integer k.
>
> **Good.** Let n be an even integer. Then n = 2k for some integer k.

> **Bad.** Breaking this down, the box holds six vials, so two boxes hold twelve.
>
> **Good.** The box holds six vials, so two boxes hold twelve.

> **Context.** The paper analyzes the quoted model output.
>
> **Bad.** Let us think step by step. The model output begins "First, I should compare the load and the limit."
>
> **Good.** The model output begins "First, I should compare the load and the limit."
