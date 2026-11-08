# Remove leaked generation artifacts and flag the gaps

Remove citation tokens leaked from chat interfaces, such as `citeturn0search0` and `contentReference[oaicite:...]`, along with unfilled placeholders such as "[Insert citation]". Keep the surrounding claim and flag the missing information. When a URL contains the AI-referrer parameter `utm_source=chatgpt.com`, leave the URL unchanged in the text and flag the parameter for removal.

## Details

Also check for unfinished author fields and citation tokens from other chat interfaces. When flagging a removed placeholder or token, state what information the surrounding sentence requires.

## Examples

> **Context.** The draft gives the opening date without a source; the edit removes the placeholder and flags the missing citation.
>
> **Bad.** The bridge opened in 1986. [Insert citation]
>
> **Good.** The bridge opened in 1986.

> **Context.** The draft gives the opening date without a source; the edit removes the leaked token and flags the missing citation.
>
> **Bad.** The bridge opened in 1986. citeturn0search0
>
> **Good.** The bridge opened in 1986.

> **Context.** The draft gives the survey month but omits the author's name; the edit removes the placeholder and flags the missing name.
>
> **Bad.** The survey was conducted in May. [Author name here]
>
> **Good.** The survey was conducted in May.

> **Context.** The edited text leaves the URL unchanged, while a flag proposes removing the referrer parameter as shown in Good.
>
> **Bad.** Data are at https://example.org/data?utm_source=chatgpt.com.
>
> **Good.** Data are at https://example.org/data.
