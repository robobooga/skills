---
name: summarize
description: Summarize the current session into a structured handoff document. Use this skill whenever the user wants to save their progress, wrap up a session, hand off to another LLM or model, pause and resume later, capture what was learned, or get a session recap. Trigger on phrases like "summarize this session", "save my progress", "write a handoff", "I need to stop here", "capture the context", "what did we do today", "session summary", "save for later", or any time the user is clearly wrapping up or transitioning away from the current work.
---

# Summarize Session

Produce a structured handoff document from the current conversation. The goal is a tight, information-dense artifact that lets someone — or another AI — pick up exactly where things left off without needing to re-read the thread.

## What to extract

Read the full conversation and pull out:

1. **Goal** — What was the user trying to accomplish? One or two sentences. Be specific; don't just say "we worked on the project."

2. **Accomplished** — What actually got done? Concrete deliverables, fixes, decisions finalized. If the session was exploratory and nothing shipped, say so honestly.

3. **Key Decisions** — Non-obvious choices that were made and why. Include what was ruled out if that context matters. Skip decisions so obvious they don't need recording.

4. **Points of Interest** — Findings worth preserving: gotchas discovered, surprising behaviors, useful patterns, relevant file paths, external docs or links that were consulted.

5. **Open Questions** — Things that were left unresolved: unknowns, deferred decisions, bugs not yet fixed, ideas not yet explored.

6. **Next Steps** — Concrete actions to continue the work, ordered by priority. Be specific enough that someone cold could act on them.

7. **File Index** — Files that were created, meaningfully edited, or are otherwise central to the work. One line each: path + what it is/does.

8. **Continuation Prompt** — A dense paragraph written in second person, addressed to a new AI assistant. It should give the new assistant enough context to be immediately useful without re-reading the thread. Include: the goal, current state, what to tackle next, and any critical context (constraints, conventions, gotchas). This is the most valuable part of the document — take care with it.

## Output template

Use exactly this structure. Omit sections that have nothing meaningful to say (e.g. no files touched → omit File Index), but always include Goal, Accomplished, Open Questions, Next Steps, and Continuation Prompt.

```
# Session Summary — [YYYY-MM-DD]

## Goal
[1-2 sentences]

## Accomplished
- [item]
- [item]

## Key Decisions
- **[decision]**: [why, and what was considered but ruled out]

## Points of Interest
- [finding / gotcha / useful pattern / link]

## Open Questions
- [unresolved issue or thing to investigate]

## Next Steps
1. [specific action]
2. [specific action]

## File Index
- `path/to/file` — [what it is]

## Continuation Prompt
> You're helping me continue work on [X]. [1-3 sentences on what was accomplished and the current state.] The immediate next thing to tackle is [Y]. Key context to know: [critical constraints, conventions, or gotchas that would trip someone up without this summary.]
```

## Saving the file

1. Determine the current working directory from conversation context (files edited, commands run, etc.).
2. Save the summary as `session-summary-YYYY-MM-DD.md` in that directory, using today's date.
3. Tell the user the full path.
4. If the working directory is ambiguous, ask before saving.

## Calibration notes

- **Length**: Tight is better. A focused 15-bullet summary beats a padded 3-page one. Cut anything that won't help the next person orient quickly.
- **Tone**: Match the user's context. A solo dev hacking on a side project needs different framing than an engineer writing up a production incident.
- **Partial sessions**: If the user calls `/summarize` mid-session (not at the end), note that explicitly in the Goal section so the reader knows the work is ongoing.
- **Target audience**: If the user specifies a target ("summarize for a junior dev", "hand this off to GPT-4o"), adapt the assumed knowledge level in the Continuation Prompt accordingly.
