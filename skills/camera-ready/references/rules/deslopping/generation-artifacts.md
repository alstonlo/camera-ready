# Remove stray citation codes and placeholders, and flag missing information

Remove artifacts left by an unedited paste, such as chat citation codes (`citeturn0search0`, `contentReference[oaicite:...]`) and unfilled placeholders ("[Insert citation]"). Keep the surrounding claim and flag the missing information. Flag URL parameters that identify an AI tool as the referrer, such as `utm_source=chatgpt.com`, for removal.

## Details

- Check for citation codes from other chat interfaces too.
- When flagging a removed placeholder or citation code, state what information the surrounding sentence needs.

## Examples

**Edit 1.** Suppose the draft gives no source for the opening date and the editor flags the missing source separately.

> **Before.** The bridge opened in 1986. citeturn0search0

> **After.** The bridge opened in 1986.

**Edit 2.** Suppose the editor flags this URL. The After passage shows the proposed replacement; the draft's URL stays unchanged.

> **Before.** Data are at https://example.org/data?utm_source=chatgpt.com.

> **After.** Data are at https://example.org/data.

The flag shows the suggested URL without changing the draft's link.
