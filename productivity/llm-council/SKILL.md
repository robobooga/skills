---
name: llm-council
description: Pressure-test a decision, plan, or project with a council of six independent advisors who answer separately, peer-review each other anonymously, then get synthesized into a single verdict by a chairman. Use when the user wants a hard, multi-angle gut-check before committing. Trigger on phrases like "council this", "convene the council", "war room this", "pressure-test this", "stress-test this decision", "red team this", "what would the council say", "get the council on this", or any time the user wants a tough, many-perspectives review of an idea, product, or engineering call.
---

# LLM Council

Run one decision through six independent advisors, then anonymous peer review, then a chairman synthesis. The value is in the structure: advisors answer alone so they don't converge, review blind so they critique ideas not authors, and the chairman has to reconcile the clash instead of averaging it away.

Use this for decisions worth the spend — architecture calls, product bets, "should we build this at all", positioning, big refactors, hiring/scoping trade-offs. Don't council trivia (see Important notes).

## When to run

The user hands you something to judge. Examples (kept generic — works for any project):

- "Council this: should we rewrite the ingestion pipeline in Rust or keep patching the Python one?"
- "War room this landing page — does the value prop land?"
- "Pressure-test the plan to ship the billing feature this quarter."
- "Should this project even exist? Council it."

## The advisors

Six lenses, not six job titles. The tensions between them are the point — keep each in character and let them disagree.

1. **The Marketer** — product–market fit and the business. Is there a real buyer? Who pays, why, and instead of what? Positioning vs competition, GTM and distribution, is this a viable model or a feature in search of a market.
2. **The Engineer** — how it actually works. Security, scalability, modularity, dependencies, failure modes, maintenance and tech-debt cost over time. Can we build it, ship it, and keep it alive without bleeding.
3. **The Contrarian** — devil's advocate and hater. Assumes there's a fatal flaw and hunts it. Nitpicks, counter-arguments, the unglamorous reasons this goes wrong. Argues against the room on principle.
4. **The General Public** — zero context, just stumbled onto this. Reacts only to what's actually in front of them, not what's in the founder's head. Catches curse-of-knowledge, unclear value, "I don't get what this is."
5. **The Dreamer** — low-risk upside and adjacent expansions. What this could become, the undervalued angle, the cheap option that opens doors. Explicitly low-risk — opportunity, not reckless growth.
6. **The Lazy One** (Occam's razor) — the simplest path that works. Don't change what isn't broken, don't reinvent the wheel, does this even need to exist. What stdlib / native / existing thing already covers it.

**Why these six:** Marketer (will it sell) pulls against Engineer (can we build and keep it safe). Dreamer (do more) pulls against Lazy (do less, or nothing). The Contrarian attacks everyone. The General Public keeps the room honest with fresh eyes. You get coverage of business, build, risk, naivety, ambition, and restraint — and built-in friction so no single bias wins by default.

## Step 1 — Frame the question (with context scan)

Before convening, ground the question:

- Scan available context: the user's message, `CLAUDE.md`, any `memory/` notes, and any files or links the question references. Read enough to give the advisors real footing — they answer better with the actual artifact than a paraphrase.
- Restate the decision **neutrally** as one clear question. Strip leading language ("isn't it obviously better to…"). Include the minimum context an outsider needs to answer well.
- If the question is genuinely ambiguous or missing something load-bearing, ask the user once, then proceed.

Keep the framed question short. It goes verbatim into every advisor prompt.

## Step 2 — Convene the council

Spawn **all six advisors in parallel** (one sub-agent each, in a single batch). Give every advisor the same framed question and context, and the same instructions — only the lens differs.

Sub-agent prompt template:

> You are **{advisor name}**: {one-line description of the lens from the list above}.
>
> The question: **{framed question}**
>
> Context: {relevant context gathered in Step 1}
>
> Answer **only** through your lens. Be direct and unhedged — no "it depends," no both-sides-ism, no disclaimers. Take a position and defend it. Say the uncomfortable thing your lens sees that the others will miss. 150–300 words. End with your one-sentence bottom line.

Collect all six responses verbatim.

## Step 3 — Anonymous peer review

Anonymize the six responses as **Response A–F**, assigned in **random order** (so position doesn't leak identity). Keep your own private mapping of letter → advisor for the transcript.

Spawn **six reviewers in parallel**, each given all six anonymized responses and asked the same three questions:

> Below are six anonymous responses to the same question. Read all six.
>
> {Response A … Response F}
>
> Answer:
> 1. Which response is **strongest**, and why?
> 2. Which has the **biggest blind spot or error**, and what is it?
> 3. What did **all of them miss**?

Collect the six reviews verbatim.

## Step 4 — Chairman synthesis

You are the chairman. Take all six **de-anonymized** advisor responses plus all six reviews and produce one verdict. Do not average — reconcile. Structure:

- **Where they agree** — the consensus, if any, and how load-bearing it is.
- **Where they clash** — the real disagreements and what each side is actually optimizing for.
- **Blind spots** — what the reviews surfaced that no single advisor caught.
- **Recommendation** — your call, with reasoning. You may side with a lone dissenter over the majority if they're right; say so explicitly when you do.
- **The one thing to do first** — the single highest-leverage next action.

## Output

Two things, in this order:

1. **Print the chairman verdict in chat** — the full Step 4 synthesis. This is what the user reads.
2. **Save one transcript file** to the system temp directory so it never lands in a project repo. Resolve the temp dir from the environment (`%TEMP%` on Windows, `$TMPDIR` or `/tmp` on Unix) and write:

   `<tempdir>/council/council-transcript-<YYYYMMDD-HHMMSS>.md`

   Create the `council/` subdir if needed. The transcript contains, in order: the original question, the framed question, all six advisor responses (labelled by advisor), all six reviews **with the A–F → advisor mapping revealed**, and the full chairman synthesis.

Tell the user the saved path on one line. Do **not** write anything into the working directory or project repo.

## Example

**User:** "Council this: should we add a plugin system to the CLI so users can extend it, or keep it closed and just ship the features ourselves?"

**Framed question:** "Should the CLI expose a public plugin API for third-party extensions, or stay closed with first-party features only?"

**Convene (parallel):**
- *Marketer* — A plugin ecosystem is a moat and a distribution channel; community plugins become marketing. But only if there's already demand; no users, no plugins.
- *Engineer* — A public API is a forever contract. Sandboxing, versioning, security review of third-party code, support load. Triples the maintenance surface.
- *Contrarian* — You'll ship a plugin API three people use, then can't change your internals without breaking them. Classic premature platform.
- *General Public* — "I just wanted the tool to do the thing. I don't know what a plugin is and I don't want to install one."
- *Dreamer* — Start with internal-only extension points you also use; the public API can come later for free once they've proven out.
- *Lazy One* — Does this need to exist? Ship the top three requested features directly. A plugin system is work you do so you can do more work.

**Peer review (anonymized A–F, parallel):** reviewers converge that the strongest case is "extension points yes, public contract no," the biggest blind spot is nobody priced the security/support cost of running untrusted code, and all of them assumed demand that hasn't been demonstrated.

**Chairman verdict:** Agreement that a public plugin API now is premature. Clash is Marketer's moat vs Engineer/Lazy's cost — and the moat only exists with a user base that isn't there yet. Blind spot: untrusted-code risk. **Recommendation:** build internal extension points (siding with the Dreamer/Lazy framing), keep them private, revisit a public API only when users are asking and you can fund the security/support cost. **First thing to do:** ship the single most-requested feature as an internal plugin to prove the seam, not the platform.

## Important notes

- **Always spawn in parallel** — advisors in one batch, reviewers in one batch. Sequential spawning lets later answers drift toward earlier ones; the independence is the whole method.
- **Always anonymize before review** — randomized A–F. Reviewers must critique ideas, not authors.
- **The chairman can side with the dissenter.** Majority isn't truth. If one lens is right and five are wrong, say so.
- **Don't council trivial questions.** Six advisors plus six reviews plus a synthesis is real spend. For a quick judgment call, just answer. Reserve the council for decisions where being wrong is expensive.

---

Methodology adapted from Andrej Karpathy's "LLM Council" (independent advisors → anonymous peer review → chairman synthesis). The six-advisor cast here is customized for evaluating projects and product/engineering decisions.
