# Remove stray citation codes and placeholders, and flag missing information

Remove chat citation codes, such as `citeturn0search0` and `contentReference[oaicite:...]`, and unfilled placeholders, such as "[Insert citation]". Keep the surrounding claim and flag the missing information. For URLs with `utm_source=chatgpt.com`, leave the URL unchanged and flag the parameter for removal.

## Details

Also check for unfilled author fields, such as "[Author name here]", and for citation codes from other chat interfaces. The parameter `utm_source=chatgpt.com` identifies ChatGPT as the referring website. When you flag a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Edit 1.** No source for the opening date appears in the draft; the editor flags the missing source separately.

> **Before.** The bridge opened in 1986. citeturn0search0
>
> **After.** The bridge opened in 1986.

**Edit 2.** In the editor's flag to the author, After is a proposal. The draft's URL remains unchanged.

> **Before.** Data are at https://example.org/data?utm_source=chatgpt.com.
>
> **After.** Data are at https://example.org/data.
