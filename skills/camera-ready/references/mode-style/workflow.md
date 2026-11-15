# Style workflow

Style mode edits the style of any writing, such as a paragraph, a docstring, a code comment, or documentation, and removes AI patterns.

You have access to a [writing guide](guide.md) that compiles best-practice *rules* for writing. Read the guide in full before doing any work, and after each compaction, reread the guide before continuing. Apply only the rules in this guide.

## Requests

Note the target text and its audience. When the request does not name the audience, infer it from the text and the files around it, such as a project's README or a venue's template, and from what the text assumes its readers already know. Follow the matching row of the table below; for other requests, apply the relevant guide sections within the requested scope. The row limits every later step.

A request is a review only when it uses the word "review" for what you should do, as in "review my introduction". The words "check", "audit", and "critique" do not make it one, and neither does a mention of reviewers or reviews, as in "address the reviewers' comments". A review changes nothing, whatever else the request asks.

| Request | What you do | What you may change |
|---|---|---|
| polish | edit with every section of the guide, then check | prose, conventions, mechanical errors, bloat |
| tighten | as for polish, aiming to reduce word count | as for polish |
| review | find each finding against every guide section, or only the sections the request names; report each finding with its suggested replacement | nothing |
| deslopping pass | edit with the guide's AI patterns section and the rules it links, then check | minimal prose changes |
| one convention | edit with that convention and the rules it links, then check | that convention only; flag other errors |

A story, flow, or argument check, an overclaiming check, a hedging question, or a cut to a length needs paper mode: tell the author to start the request with `paper`, and do nothing else.

## Scope

Leave every claim as the author wrote it: change no claim's strength or scope, and add or remove no hedge. When a rule links to a rule page that the guide does not include, such as a page on claims or on cutting ideas, the case is outside style mode: leave the text and flag the problem.

In a code file, edit only the prose of comments and docstrings. Preserve the comment syntax, the docstring's field names and layout, identifiers, directives such as `# noqa`, code examples, and what the text says the code does. If a comment disagrees with the code, flag it instead of fixing it. Follow the conventions of the language and of the kind of text, not those of a paper.

## Workflow

Keep no notes, save no copy of the original, and ask no questions. A review goes from the reading to the report.

1. **Read.** Read the target text and enough of the text around it to resolve what it refers to, such as the enclosing section or function. Search further only when a finding needs a fact stated elsewhere.
2. **Edit.** Follow the edit rules. Open a linked rule page when a rule applies and its exceptions or examples matter. Test each sentence against the guide's rules:
   - Does the paragraph open with its point, and does each sentence open with information the previous one supplied?
   - Delete each clause in turn: does the sentence lose anything?
   - Are the actors subjects and the actions verbs? Is every referent clear, and is the subject near its verb?
   - Does any word add only emphasis, any verb leave its operation unstated, or any noun stand in for the measured quantity?
3. **Check.** Read each edit's old text beside its new text, and restore any fact, number, hedge, condition, scope, attribution, or logical relation that the edit added, dropped, or changed. Reread each edited passage with the sentences around it, and confirm that every reference still resolves. Count em dashes and the guide's other blacklisted patterns in the edited text, and fix those that remain.
4. **Report.** For named files, edit in place; otherwise return the edited text. Then list the flags, each phrased as a question for the author. For a review, return each finding with its exact words, rule, and suggested replacement. If no edit is needed, leave the text unchanged and say so in one line.
