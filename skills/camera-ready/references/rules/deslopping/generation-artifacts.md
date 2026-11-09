# Remove stray citation codes and placeholders, and flag missing information

Remove chat citation codes, such as `citeturn0search0` and `contentReference[oaicite:...]`, and unfilled placeholders, such as "[Insert citation]". Keep the surrounding claim and flag the missing information. For URLs with `utm_source=chatgpt.com`, leave the URL unchanged and flag the parameter for removal.

## Details

Also check for unfilled author fields, such as "[Author name here]", and for citation codes from other chat interfaces. The parameter `utm_source=chatgpt.com` identifies ChatGPT as the referring website. When you flag a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Example 1.** The opening date has no source in the draft. Alongside this edit, the editor flags the need for a source; deleting the citation code does not supply one.

> **Bad.** The bridge opened in 1986. citeturn0search0
>
> **Good.** The bridge opened in 1986.

**Example 2.** Good shows the clean URL proposed in the editor's flag. The draft's URL remains unchanged because the rule requires flagging this parameter for removal.

> **Bad.** Data are at https://example.org/data?utm_source=chatgpt.com.
>
> **Good.** Data are at https://example.org/data.
