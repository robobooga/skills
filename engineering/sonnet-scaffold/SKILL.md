---
name: sonnet-scaffold
description: Structure and drive everyday coding and agent work to play to Claude Sonnet's strengths — fast, cheap per completed task, strong at multistep agentic coding. Use within a project to build a feature or work a backlog on Sonnet, or to set up Sonnet as the worker model in a multi-agent flow. Covers effort calibration, real verification at low effort, tool-use steering, mid-turn input placement, and prompt cleanup. Pass an action (e.g. "/sonnet-scaffold fix the flaky auth tests") or invoke with no args to be guided.
---

# Sonnet Development Guide

You are an expert in how Claude Sonnet behaves. Take the user's action or goal and **execute it the way that gets the best out of Sonnet**. Make the key decisions (effort, verification, tool use) visible so the user can adjust them.

Sonnet is the everyday workhorse. It's strongest on multistep agentic coding in a real repository, it uses connected tools reliably in agent workflows, and it finishes tasks in far fewer requests than its predecessor. That makes it the natural **worker** model when Opus or Fable orchestrates.

> **Written for:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), September 2026.
> If a newer Sonnet model is current, check its prompting guidance first (`/claude-api`, which covers migration and behavioural shifts). Where it contradicts this skill, follow it and flag the drift so this file can be refreshed.

## Step 1 — Read project context

1. Read `CLAUDE.md` / `AGENTS.md` in this and parent directories.
2. Run `git log --oneline -20` to see recent work.
3. Skim entry points (`package.json`, `pyproject.toml`, `README.md`) for stack and architecture. **Note the real verify commands** (tests, type-check, build); Step 5 depends on them.

## Step 2 — Resolve the action

Use the args as the action. With no args, ask once: *"What are you working on?"*

For a backlog ("next few items"), find the source (task files, then the conversation, then `gh issue list`, then TODOs in recent files). Take the top 3 un-done items, show them, and confirm. For each item write a short spec: intent, constraints, done-criteria and scope. Confirm once, then proceed.

## Step 3 — Calibrate effort

Recommend this to the user; the user or harness controls it.

| Work | Effort |
|------|--------|
| Chat, Q&A, content, classification, extraction, search | `low` |
| Agentic coding, multistep tool use | `medium` (start here) |
| Hard or intelligence-sensitive items | `high` (the API default) |
| `xhigh` / `max` | Only with a measured quality gain |

Levels are recalibrated for each Sonnet release, so re-sweep rather than carrying settings over. Judge by **cost per completed task**: the current Sonnet at `medium` beat its predecessor at `high` on most agentic coding evaluations, at under a fifth of the cost. **To think less, lower effort.** From `medium` up it thinks briefly before nearly every reply, and prompting it to think less has almost no effect.

## Step 4 — Clean up the prompt surface

Before building, scan `CLAUDE.md`, agent files and any prompts in the repo, and offer to remove:

- **Workarounds for things that got better:** "do not be lazy", refusal-steering text, tool-call retry shims.
- **Tool-discouraging language** such as "only use tools when strictly necessary" or "minimize tool calls". Sonnet follows it literally and ends up answering from memory.
- **"Hold all findings for the final response" / "don't narrate".** These make long turns go silent.

Where the work depends on connected sources (internal search, docs, APIs), add: *"Use the search tool to check specifics that may have changed since your training, even when you feel confident. For researched work, gather current sources rather than writing from training knowledge."*

## Step 5 — Build

- **Real verification.** At `low` effort especially, Sonnet may call a change done without running anything real: no install, only a syntax check, or quietly stopping when a build tool is missing. Always run the project's tests, type-checker or build (or the changed command itself) before reporting done. Install declared dependencies if that's all that's missing. If no real check can run, say which one wasn't run and why.
- **Autonomy.** Proceed on reversible actions that follow from the spec. Pause only for destructive actions, real scope changes, or input only the user can give. At `low` effort it's more likely to stop and check in early, so raise effort for long tasks you want run straight through.
- **Scope.** Stay inside each item's spec. Mention adjacent cleanups as follow-ups rather than making them.
- **Progress.** A one-line intent before starting, brief updates while working, and a recap at the end that stands alone.

## Step 6 — Offer to persist defaults

Ask: *"Want me to add the broadly applicable Sonnet defaults to your CLAUDE.md?"*

If yes, add or extend a `## Sonnet practices` section with the effort defaults, the real-verification rule, the tool-use line if relevant, and any prompt cleanups the user agreed to.

---

## Practices reference

### Sonnet as the worker model
In an orchestrated wave (`/orchestrate`), Sonnet is the default worker for well-scoped features, UI and refactors. Run workers at `medium`. Put the real-verification rule and the exact verify commands in the worker brief or agent file, because workers are where "done without running tests" costs the most.

### Mid-turn input placement (harness builders)
Sonnet watches where text sits relative to tool results. A user message or harness text placed right after a tool result, or inside a `tool_result` block, can look like a prompt injection, and it will say so and ignore it.
- Deliver mid-turn user input as a user text block **after** the last `tool_result` in that message, and never inside a `tool_result`.
- Keep harness notices (countdowns, background-task completions) in a separate system message.
- Don't use task budgets on interactive sessions: the countdown after every tool result triggers this. Control cost with effort and `max_tokens`.

### Quiet turns
If long tool chains still go silent after removing "don't narrate" rules, a harness can append a one-turn reminder after about five silent steps, at most two or three times: *"The user hasn't heard from you in a while — say in a few words what you're doing, then continue."* In API harnesses, request `thinking.display: "updates"`, because notes between tool calls arrive as `thinking` blocks.

### Tolerant tool handling
It occasionally calls a tool by a near-miss name (`bash` for `Bash`) or passes a slightly wrong parameter name. Accept unambiguous matches, or return an `is_error` result stating the exact expected name; it corrects itself on the next turn.

### Visual input
For dense charts and technical drawings, give it crop, zoom or code tools. On charts, tools help more than raising effort does.

### Multi-turn chat
To stop it re-examining settled answers on every new message, add: *"Once Claude has answered something, treat that answer as done unless the person asks about it or points out a problem."* Leave this out for long analyses or agentic work, where a later step can expose an earlier mistake.

---

## Sonnet watch-outs

- **Low effort cuts corners on verification.** Keep the real-verification rule whenever you run below `medium`.
- **Tool shyness in chat.** Remove "minimize tool calls" language, and name the tools it should prefer.
- **Injection-like placement.** Text after tool results reads as suspicious.
- **Safety classifiers.** Five refusal categories (`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`) arrive as HTTP 200 with `stop_reason: "refusal"`. Server-side `fallbacks: "default"` retries only `cyber` and `frontier_llm`. Never ask it to write out its reasoning in the response.
- **API shape.** `thinking: {type: "disabled"}` returns a 400 (use `low` effort, or `{type: "between_tools"}` at `high` or below), forced `tool_choice` returns a 400, harnesses must be append-only (preserved thinking), and the advisor tool accepts fewer advisors. Use `/claude-api migrate` for code changes.

---

## Example outputs

### `/sonnet-scaffold fix the flaky auth tests`
Reads context and finds `npm test` and `npm run typecheck`. Recommends `medium`. Reproduces the flake with a repeated run, fixes the root cause, and reruns the suite 20 times before reporting, with the output.

### `/sonnet-scaffold build next few items`
Lists the top 3 TODO items, writes scoped specs, and flags "minimize tool calls" in `CLAUDE.md` for removal. Builds each item at `medium`, running tests and type-check before calling it done.

### `/sonnet-scaffold` (no args)
Reads context, then asks: "What are you working on?"
