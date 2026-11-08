# Delete chatbot artifacts

Delete conversational wording left by an assistant, such as "Certainly!", "Great question", "I hope this helps", or "As of my last update".

## Details

Also delete offers to continue, disclaimers about the assistant's status, and direct replies to the requester. Preserve conversational wording when it appears inside a prompt, model output, or study stimulus that the paper analyzes.

## Examples

> **Bad.** Certainly! The freezer holds twelve trays.
>
> **Good.** The freezer holds twelve trays.

> **Bad.** The freezer holds twelve trays. Let me know if you need more details.
>
> **Good.** The freezer holds twelve trays.

> **Bad.** Here is the paragraph you requested. The freezer holds twelve trays.
>
> **Good.** The freezer holds twelve trays.

> **Bad.** As an AI assistant, I cannot visit the lab. The freezer holds twelve trays.
>
> **Good.** The freezer holds twelve trays.

> **Context.** The paper analyzes responses to the quoted prompt.
>
> **Bad.** Certainly! The test prompt is "Great question!".
>
> **Good.** The test prompt is "Great question!".
