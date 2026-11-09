# Remove stray citation codes and placeholders, and flag missing information

Remove chat citation codes, such as `citeturn0search0` and `contentReference[oaicite:...]`, and unfilled placeholders, such as "[Insert citation]". Keep the surrounding claim and flag the missing information. For URLs with `utm_source=chatgpt.com`, leave the URL unchanged and flag the parameter for removal.

## Details

Also check for unfilled author fields, such as "[Author name here]", and for citation codes from other chat interfaces. The parameter `utm_source=chatgpt.com` identifies ChatGPT as the referring website. When you flag a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Example 1.** In this draft, the sentence gives an opening date without a citation. The editor removes the stray citation code and flags the missing source.

> **Bad.** The bridge opened in 1986. citeturn0search0
>
> **Good.** The bridge opened in 1986.

**Example 2.** In this draft, a URL includes an AI referrer parameter. The editor leaves the URL in place and flags the parameter for removal. The Good line shows the clean URL proposed in the flag.

> **Bad.** Data are at https://example.org/data?utm_source=chatgpt.com.
>
> **Good.** Data are at https://example.org/data.
