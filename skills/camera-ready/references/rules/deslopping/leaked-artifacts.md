# Remove leaked generation artifacts and flag the gaps

Remove leaked chat citation tokens such as `citeturn0search0` and `contentReference[oaicite:...]`, and unfilled placeholders such as "[Insert citation]". Keep the surrounding claim and flag the missing information. Flag the AI-referrer parameter `utm_source=chatgpt.com` for removal rather than changing the URL.

## Details

Other cues include unfinished author fields and the variants of these citation tokens that other chat interfaces produce. Read the surrounding sentence to identify what information the placeholder was meant to supply.

Removing a placeholder does not make its claim supported. Keep the claim and name the missing source or information in the report. The URL parameter is flagged rather than removed because URLs are protected; do not silently rewrite a URL while cleaning the prose.

## Examples

The draft supplies the opening date but no source; Good is the proposed text revision, with the missing citation flagged for the author.

- Bad: The bridge opened in 1986. [Insert citation]
- Good: The bridge opened in 1986.
