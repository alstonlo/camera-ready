# Remove stray citation codes and placeholders, and flag missing information

Chat citation codes include `citeturn0search0` and `contentReference[oaicite:...]`; an unfilled placeholder may read "[Insert citation]". Keep the surrounding claim and flag the missing information. For URLs with `utm_source=chatgpt.com`, leave the URL unchanged and flag the parameter for removal.

## Details

Also check for unfilled author fields, such as "[Author name here]", and for citation codes from other chat interfaces. The parameter `utm_source=chatgpt.com` identifies ChatGPT as the referring website. When you flag a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Edit 1.** Suppose the draft gives no source for the opening date and the editor flags the missing source separately.

> **Before.** The bridge opened in 1986. citeturn0search0

> **After.** The bridge opened in 1986.

**Edit 2.** Say an editor flags this URL for the author. After shows the proposed replacement; the URL in the draft stays unchanged.

> **Before.** Data are at https://example.org/data?utm_source=chatgpt.com.

> **After.** Data are at https://example.org/data.

Showing the suggested URL in the flag lets the author see the requested change while preserving the draft's link.
