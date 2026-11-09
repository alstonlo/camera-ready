# Remove stray citation codes and placeholders, and flag missing information

Remove chat citation codes, such as `citeturn0search0` and `contentReference[oaicite:...]`, and unfilled placeholders, such as "[Insert citation]". Keep the surrounding claim and flag the missing information. For URLs with `utm_source=chatgpt.com`, leave the URL unchanged and flag the parameter for removal.

## Details

Also check for unfilled author fields, such as "[Author name here]", and for citation codes from other chat interfaces. The parameter `utm_source=chatgpt.com` identifies ChatGPT as the referring website. When you flag a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Edit 1.** The opening date has no source in the draft. The edit removes "citeturn0search0" and keeps the opening-date claim, so that the stray citation code is gone without deleting the claim. Alongside this edit, the editor flags the need for a source for the date, because deleting the code does not supply one.

> **Before.** The bridge opened in 1986. citeturn0search0
>
> **After.** The bridge opened in 1986.

**Edit 2.** The edit, a proposal to the author shown in the editor's flag, removes "?utm_source=chatgpt.com" from the URL so that it no longer identifies ChatGPT as the referring website. The draft's URL remains unchanged because the rule requires flagging this parameter for removal.

> **Before.** Data are at https://example.org/data?utm_source=chatgpt.com.
>
> **After.** Data are at https://example.org/data.
