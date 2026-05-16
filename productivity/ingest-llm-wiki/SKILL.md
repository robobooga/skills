---
name: ingest-llm-wiki
description: This skill should be used when the user says "ingest [file]", "process this raw file", "add [file] to the wiki", "what files are pending ingestion", "what hasn't been ingested yet", or drops a file in raw/ and asks Claude to handle it.
version: 0.1.0
---

# Ingest a Raw Source into the Engineering Brain Wiki

## Setup

This skill requires `wiki-status.py` in your project. Copy `scripts/wiki-status.py` (bundled with this skill) to `scripts/wiki-status.py` in your project root.

---

## Finding pending files

If no specific file is provided, run the status script first:

```bash
python scripts/wiki-status.py
```

Show the pending files to the user and ask which one to ingest. If the requested file is already ingested (it appears in `wiki/sources/`), say so and stop — do not re-ingest.

---

## The 7-step ingest workflow

Execute these steps in order. Do not skip any step.

### Step 1 — Read the source

Read the full content of `raw/<filename>`. For PDFs, read all pages. For transcripts, read the complete text.

### Step 2 — Surface key takeaways and confirm framing

Before writing any wiki pages, present to the user:
- A 2–4 sentence TL;DR
- 5–10 specific, citation-worthy takeaways
- The proposed slug for the source page (kebab-case, e.g. `ulrich-drepper-cpu-memory`)
- The list of new wiki pages you plan to create and existing pages you plan to update

Wait for the user to confirm or redirect before proceeding to Step 3.

### Step 3 — Create the source page

Create `wiki/sources/YYYY-MM-DD-<slug>.md`:

```markdown
---
type: source
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
sources: []
---

# <Title>

**Source:** `raw/<filename>`
**Type:** transcript | article | paper | book-chapter | …
**Author / Origin:** …
**Date of source:** …
**Ingested:** YYYY-MM-DD

## TL;DR
2–4 sentences.

## Key takeaways
- Bulleted, specific, citation-worthy claims.

## Detailed notes
Structured by section or theme. Quote sparingly; cite timestamps or page numbers.

## Wiki updates from this source
- Created `[[concept-x]]`, `[[principle-y]]`
- Updated `[[topic-z]]` with new section on …
- Flagged contradiction with `[[concept-w]]`: …

## Open questions
- Things worth investigating further.
```

### Step 4 — Touch related pages

For every concept, principle, topic, or entity the source introduces or significantly modifies:

**If the page does not exist, create it.**

**Concept page** — `wiki/concepts/<slug>.md`:
```markdown
---
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: [[YYYY-MM-DD-source-slug]]
---

# <Concept name>

## Definition
One paragraph. Plain English first; precise after.

## Key properties
- …

## Why it matters
When and where this shows up.

## Common misconceptions
- …

## Related
- `[[other-concept]]` — how they relate

## Sources
- `[[YYYY-MM-DD-source-slug]]` — what it contributed
```

**Principle page** — `wiki/principles/<slug>.md`:
```markdown
---
type: principle
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: [[YYYY-MM-DD-source-slug]]
---

# <Principle, imperative form>

## Stance
One sentence — the rule.

## Why
The reasoning, ideally with a concrete failure mode it prevents.

## When it applies
Edge cases, exceptions, when *not* to follow it.

## Related
- `[[concept-x]]`, `[[principle-y]]`

## Sources
- `[[YYYY-MM-DD-source-slug]]`
```

**Topic page** — `wiki/topics/<slug>.md`:
```markdown
---
type: topic
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: [[YYYY-MM-DD-source-slug]]
---

# <Topic>

## What this covers
One paragraph.

## Concepts
- `[[concept-a]]` — short hook

## Principles
- `[[principle-a]]` — short hook

## Sources
- `[[YYYY-MM-DD-source]]` — short hook

## Open threads
- Questions / gaps worth pursuing.
```

**If the page already exists, update it:** add the new source's contribution to the relevant sections, revise any claims the source extends or contradicts, add it to `## Sources`, and update the `updated:` frontmatter date.

A single source typically touches 5–15 wiki pages. Prefer many small focused pages over few large ones. Dangling `[[links]]` to pages not yet written are fine; isolated pages with no inbound links are not.

### Step 5 — Update `index.md`

For each newly created page, add one line under the appropriate section:
```
- [[slug]] — one-line hook
```

Also add the new source under `## Sources`. If a section doesn't exist yet, create it.

`index.md` is at the repo root, not inside `wiki/`.

### Step 6 — Append to `log.md`

Append exactly one new entry at the bottom of `log.md` (also at the repo root):

```
## [YYYY-MM-DD] ingest | <Title>

Pages created: [[concept-a]], [[principle-b]], …
Pages updated: [[topic-c]], …
```

### Step 7 — Report back

Tell the user:
- List of pages created (with a one-line description each)
- List of pages updated (with what changed)
- Any contradictions found with existing pages
- Anything surprising or non-obvious from the source
- Suggested follow-up sources or open questions worth pursuing

---

## Style rules

Apply these throughout every page you write or update:

- **Be specific.** Vague generalities don't deserve a page.
- **Cross-reference aggressively.** Every page should link to related pages. Dangling `[[links]]` are fine; isolated pages are not.
- **Prefer many small pages** over few large ones. Splitting is cheap; giant pages are hard to search.
- **Update, don't append-and-forget.** When a new source revises an existing claim, edit the affected page and note the revision in `## Sources`.
- **Plain English first, precise definitions after.** This brain serves a human, not a textbook.
- **No filler.** No "this section will discuss …". Just say it.
- **Quote sparingly, paraphrase mostly.** When you do quote, cite (timestamp or page number).
