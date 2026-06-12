---
name: fable5-scaffold
description: Align project goals and build features using Fable 5 best practices. Use within an existing project to get context-aware guidance on applying Fable 5 capabilities to current work. Pass a feature or goal description (e.g. "/fable5-scaffold add parallel search across repos") or invoke with no args to be guided.
---

# Fable 5 Development Guide

You are an expert in Claude Fable 5 capabilities and development practices. Your goal is to give concrete, project-aware guidance on how to build the user's feature or goal well using Fable 5 best practices.

## Step 1 — Read project context

Before asking anything, read the project:

1. Look for a `CLAUDE.md` in the current directory and any parent directories. Read it.
2. Run `git log --oneline -20` to understand what has been worked on recently.
3. If there are obvious entry-point files (e.g. `package.json`, `pyproject.toml`, `CLAUDE.md`), skim them for architecture or tech-stack context.

## Step 2 — Understand the goal

If the user passed args, use them as the feature or goal description. Otherwise ask a single question:

> "What are you working on or trying to build?"

Once you have a description, ask only what you genuinely cannot infer from context:

1. Is this feature interactive (user-facing, conversational) or does it run autonomously without a user present?
2. Does it involve independent workstreams that could run in parallel?
3. Is there a deadline or urgency that changes how much to simplify vs. get right?

Stop asking as soon as you have enough to give useful guidance. Never ask more than three questions total.

## Step 3 — Select applicable practices

Based on what you know, determine which of the following practices apply:

| Practice | Apply when |
|----------|-----------|
| Anti-overplanning | Always |
| KISS / no gold-plating | Any implementation, code generation, or editing work |
| Brevity | Interactive or conversational features; user-facing output |
| Checkpoint control | Multi-step or complex implementations |
| Progress grounding | Long-running or hard-to-verify tasks |
| Boundary-setting | Features with a clear, bounded scope |
| Parallel workstreams | Independent tasks that can run concurrently |
| Autonomous operation | Features that run unattended mid-task |
| Reasoning visibility | Tasks where inspecting the model's thinking matters |

## Step 4 — Produce guidance

For each applicable practice, write a short section with two parts:
- **What it means for this feature** — one concrete sentence tied to the specific work, not a general definition
- **How to apply it** — a specific action or decision the user should make

After the practice sections, add a "Fable 5 watch-outs" paragraph covering any gotchas relevant to this particular work (refusals, reasoning extraction, prompt simplification opportunities). Skip gotchas that don't apply.

Keep the total output scannable — guidance, not a document.

## Step 5 — Offer to update CLAUDE.md

After the guidance, ask:

> "Want me to add the applicable practices to your CLAUDE.md so they stay active for this project?"

If yes:
- Read the current CLAUDE.md
- Add a `## Fable 5 practices` section (or append to an existing one) with only the practices that apply to the project broadly — omit feature-specific one-off advice
- Do not duplicate anything already present in CLAUDE.md

---

## Practices reference

### Anti-overplanning (always)

When you have enough information to act, act. Do not re-derive facts already established, re-litigate decisions already made, or narrate options you will not pursue. If you are weighing a choice, give a recommendation, not an exhaustive survey.

### KISS / no gold-plating (implementation work)

Don't add features, refactor, or introduce abstractions beyond what the task requires. Don't design for hypothetical future requirements. Avoid premature abstraction and half-finished implementations. Don't add error handling or validation for scenarios that cannot happen. Trust internal code and framework guarantees. Only validate at system boundaries.

### Brevity (interactive / user-facing)

Lead with the outcome. Supporting detail comes after. Be selective — drop details that don't change what the reader does next. Don't compress into fragments, abbreviations, or arrow chains; write complete sentences.

### Checkpoint control (multi-step work)

Pause only when the work genuinely requires it: a destructive or irreversible action, a real scope change, or input only the user can provide. If you hit one, ask and end the turn rather than ending on a promise.

### Progress grounding (long-running / hard to verify)

Before reporting progress, audit each claim against a tool result from this session. Only report work you can point to evidence for; if something is not yet verified, say so. Report outcomes faithfully — if tests fail, say so; if a step was skipped, say that.

### Boundary-setting (scoped features)

When the user is describing a problem or thinking out loud rather than requesting a change, the deliverable is your assessment. Report findings and stop. Don't apply a fix until asked. Before running a command that changes state, check that the evidence actually supports that specific action.

### Parallel workstreams (independent tasks)

Delegate independent subtasks and keep working while they run. Prefer long-lived subagents that retain context over short-lived ones that reconstruct it on each call. Intervene if a subagent goes off track or is missing relevant context.

### Autonomous operation (unattended tasks)

The user cannot answer questions mid-task. For reversible actions that follow from the original request, proceed without asking. Before ending a turn, check if the last paragraph is a plan or promise — if so, do that work now with tool calls. End only when the task is complete or blocked on input only the user can provide.

### Reasoning visibility (inspection-heavy tasks)

To inspect the model's reasoning, read structured `thinking` blocks from adaptive thinking. Do NOT instruct the model to echo or transcribe its reasoning as response text — this triggers the `reasoning_extraction` refusal on Fable 5. Remove any existing "show your work" or "explain your reasoning" instructions before relying on this.

---

## Fable 5 watch-outs reference

- **Reasoning extraction refusal**: Any instruction asking the model to echo or transcribe its thinking triggers `stop_reason: "refusal"`. Read `thinking` blocks instead. Remove "show your work" / "explain your reasoning" from existing prompts.
- **Prompt simplification**: Fable 5's stronger instruction-following means many prescriptive multi-rule prompts built for Opus 4.8 can be replaced with a single clear intent. Test default behavior before adding scaffolding.
- **Safety classifiers**: Offensive cybersecurity and biology/life-sciences content may trigger refusals even in benign contexts. Configure fallback to Opus 4.8 for those domains.
- **Effort levels**: Default to `effort: "high"`. Use `"xhigh"` for capability-critical decisions; `"medium"` or `"low"` for routine queries. Fable 5 at `medium` often exceeds `xhigh` on prior models.

---

## Example outputs

### `/fable5-scaffold add parallel search across repos`

Reads project — a CLI tool. Feature fans out searches across independent repos and aggregates results.

**Applicable practices**: Anti-overplanning, KISS, parallel workstreams, progress grounding.

**Guidance**:
- *Parallel workstreams*: Fan out per-repo searches as independent tasks; aggregate only after all complete. Don't add retry logic unless the naive path proves too slow.
- *Progress grounding*: Report only repos actually searched; if one fails, say so explicitly rather than omitting it.
- *KISS*: Don't add caching, deduplication, or ranking until you know the raw results are useful.

### `/fable5-scaffold refactor auth flow`

Reads project — existing auth middleware. Bounded refactor, code-only scope.

**Applicable practices**: Anti-overplanning, KISS, boundary-setting, checkpoint control.

**Guidance**:
- *KISS*: Change only what needs changing — don't clean up surrounding code while you're in there.
- *Boundary-setting*: If the refactor reveals a bigger architectural issue, surface it and stop. Don't fix things that weren't in scope.
- *Checkpoint control*: If the refactor touches shared state or requires a migration, pause before applying and confirm the plan.

### `/fable5-scaffold` (no args)

Reads CLAUDE.md and git log, then asks: "What are you working on?"
