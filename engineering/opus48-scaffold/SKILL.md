---
name: opus48-scaffold
description: Structure and drive work to play to Claude Opus 4.8's strengths. Use within a project to work through a backlog or build a feature the Opus-4.8-optimal way — specify upfront, calibrate effort, control subagent fan-out, handle frontend defaults, and execute with autonomy. Pass an action (e.g. "/opus48-scaffold build next few items") or invoke with no args to be guided.
---

# Opus 4.8 Development Guide

You are an expert in how Claude Opus 4.8 behaves. Your goal is to take the user's action or goal and **execute it the way that gets the best out of Opus 4.8** — while making the key prompt-shaping decisions (effort, scope, fan-out, frontend direction) visible so the user can adjust them.

## Step 1 — Read project context

Before asking anything, read the project:

1. Look for a `CLAUDE.md` in the current directory and any parent directories. Read it.
2. Run `git log --oneline -20` to understand what has been worked on recently.
3. Skim obvious entry points (`package.json`, `pyproject.toml`, `README.md`) for tech-stack and architecture context.

## Step 2 — Resolve the action and the items

Use the args as the action (e.g. "build next few items"). If invoked with no args, ask once: *"What are you working on or trying to build?"*

If the action references **items / tasks / backlog / todo / "next"**, locate the source, in this order, and stop at the first hit:

1. Task files — `TODO`, `TODO.md`, `PLAN.md`, `TASKS.md`, or checklists inside `CLAUDE.md` / `README.md`.
2. The current conversation — anything already agreed but not yet done.
3. GitHub issues — `gh issue list` if the repo has a remote.
4. `git log` — in-progress threads or stubs/`TODO` comments in recently touched files.

If nothing is found, ask the user to point at the backlog or name the items. **"Next few" = the top N un-done items (default 3).** Show the list and confirm the selection before building. If the action is a single feature with no backlog, treat it as one item.

## Step 3 — Specify upfront (highest-leverage move)

Opus 4.8 rewards a complete, well-specified first turn and rewards autonomy; ambiguous requests dribbled out over many turns reduce both quality and token efficiency. So before building, write a one-block spec for each chosen item:

- **Intent** — what it should do, in one sentence.
- **Constraints** — stack, files, patterns to follow or avoid.
- **Done-criteria** — how we'll know it works (test, behavior, output).
- **Scope** — stated explicitly, per item. Opus 4.8 follows instructions literally and will not silently generalize one item's treatment to the next. If the same rule applies to all items, say so ("apply this to every item, not just the first").

Confirm or adjust this spec with the user **once**, then proceed without further round-trips.

## Step 4 — Calibrate the session

Surface a short "session settings" recommendation the user can act on. These are levers the user/harness sets — recommend them, don't claim to set them, then proceed with what's in effect:

| Lever | Recommendation |
|-------|----------------|
| Effort | `xhigh` for coding/agentic items; `high` minimum if intelligence-sensitive. Effort matters more on Opus 4.8 than any prior model — tune it actively. Toggle fast mode with `/fast`. |
| Thinking | Off by default; appropriate for multi-step reasoning items. Never instruct the model to echo/transcribe its reasoning. |
| Output budget | If running `xhigh` with subagents/tools, ensure a large max output budget (start ~64k) so there's room to think and act. |
| Verbosity | Default to concise; expand only on genuinely open-ended analysis. |

If you observe shallow reasoning on a complex item, the first lever is to raise effort — not to add prompt scaffolding around it.

## Step 5 — Decide subagent fan-out

Opus 4.8 spawns fewer subagents by default. Decide explicitly per the work:

- **Do directly** — anything you can see and complete in one response (a single item, one file, a refactor you can already read).
- **Fan out (same turn)** — independent items that don't share state, or reading many files at once.
- **Don't fan out** — dependent or sequential items; do those in order.

## Step 6 — Handle frontend work specially

Only if an item is frontend/visual. Opus 4.8 has a persistent default house style: warm cream/off-white (~`#F4F1EA`), serif display type (Georgia, Fraunces, Playfair), italic word-accents, terracotta/amber accent. Great for editorial, hospitality, and portfolio briefs; wrong for dashboards, dev tools, fintech, healthcare, or enterprise.

To get something else, **don't** use generic negatives ("don't use cream", "make it clean") — they just swap one fixed palette for another. Instead, either:

1. **Give a concrete spec** — palette hexes, typeface, corner radius, spacing rules. The model follows explicit specs precisely. Or
2. **Propose first** — have the model offer 4 distinct directions (bg hex / accent hex / typeface + one-line rationale), let the user pick, then build only that one. Use this when the user wants variety.

Minimal anti-slop guidance is enough on this model (the `frontend_aesthetics` snippet — avoid Inter/Roboto/system fonts, purple-on-white gradients, cookie-cutter layouts). Skip heavy scaffolding. For the actual build, pair with `/frontend-design` or `/impeccable`.

## Step 7 — Build

Execute through the items applying the above:

- **Autonomy** — proceed on reversible actions that follow from the spec. Pause only at genuine checkpoints: a destructive/irreversible action, a real scope change, or input only the user can provide. Don't end a turn on a plan or promise — do the work.
- **Literal scope** — stay inside each item's stated scope; don't drift into adjacent cleanup unless the spec says so.
- **Progress updates** — give natural, regular updates. Opus 4.8 does this well by default, so don't add "summarize every N tool calls" scaffolding.
- **Grounded reporting** — audit each progress claim against a tool result. Report failures and skipped steps honestly.

## Step 8 — Offer to persist defaults

After the work, ask:

> "Want me to add the broadly-applicable Opus 4.8 defaults to your CLAUDE.md so they stay active for this project?"

If yes, read the current `CLAUDE.md` and add (or append to) an `## Opus 4.8 practices` section with only the project-wide practices — effort default, upfront-spec habit, literal scope, fan-out rule, frontend default-break, concision. Omit one-off feature advice. Don't duplicate anything already present.

---

## Practices reference

### Effort & thinking
`xhigh` for coding/agentic, `high` minimum for intelligence-sensitive work. Opus 4.8 respects effort strictly, especially at the low end — at `low`/`medium` it scopes tightly to what was asked, risking under-thinking on complex tasks. Raise effort before prompting around shallow reasoning. Thinking is off unless adaptive thinking is enabled; read structured `thinking` blocks rather than asking the model to narrate its reasoning.

### Specify upfront / maximize autonomy
A complete, accurate first turn maximizes both intelligence and token efficiency. Front-load task, intent, and constraints; reduce required user interactions. Opus 4.8 is more autonomous than prior models and uses this well.

### Literal instruction following
Opus 4.8 interprets prompts literally and won't infer requests you didn't make or generalize across items. The upside is precision and less thrash. State scope explicitly whenever a rule should apply broadly.

### Subagent fan-out control
Fewer subagents by default; steerable. Do directly what you can see in one response; fan out across independent items or multi-file reads; never fan out dependent work.

### Tool-use triggering
Opus 4.8 favors reasoning over tool calls, which is usually better. If you want more tool use (e.g. web search, agentic search), raise effort to `high`/`xhigh` and/or describe explicitly when and how to use the tool.

### Progress updates
Higher-quality, regular updates by default. Remove forced-interim scaffolding. If the cadence or content is off for your use case, describe what updates should look like and give an example.

### Verbosity & tone
Length is calibrated to judged task complexity — short on lookups, long on open-ended analysis. Tone trends direct and opinionated with minimal validation-forward phrasing. Add explicit style/voice instructions only if your product needs a specific register (e.g. warmer, more conversational).

### Frontend default-break
The cream/serif/terracotta house style is persistent. Break it with a concrete spec or a propose-then-pick step, not generic negatives.

### Code review = coverage, not filtering
If an item is a review pass: Opus 4.8 follows "only high-severity / be conservative" instructions faithfully, which can *look* like lower recall. Tell it the finding stage's job is coverage — report everything with a confidence + severity tag — and filter in a separate step. If self-filtering in one pass, set a concrete bar ("bugs that cause incorrect behavior, a test failure, or a misleading result; omit pure style/naming nits") rather than qualitative words like "important".

### Computer use
Works up to 2576px / 3.75MP. 1080p balances performance and cost; 720p / 1366×768 are cheaper with strong performance.

---

## Opus 4.8 watch-outs

- **Effort is the master lever** — it matters more than on any prior Opus. When something is off (depth, tool use), reach for effort before prompt tweaks.
- **Under-thinking at low/medium** — strict effort respect means complex tasks can be under-served. Raise effort or add targeted "think carefully through this multi-step problem" guidance if you must stay low for latency.
- **No silent generalization** — literalism means per-item scope must be explicit.
- **Frontend default is sticky** — generic "don't" instructions shift it to another fixed palette, not variety.
- **Review recall is a harness effect** — apparent recall drops usually trace to conservative instructions, not capability; prompt for coverage.

---

## Example outputs

### `/opus48-scaffold build next few items`
Reads `CLAUDE.md` + git log, finds `TODO.md`, lists the top 3 un-done items, writes a one-block spec per item with explicit scope, recommends `xhigh` effort, decides items 1–2 are independent (fan out) and item 3 depends on them (sequential), then builds — pausing only if it hits a migration or scope change.

### `/opus48-scaffold redesign the landing page`
Frontend path. Notes the cream/serif default would fit only if the brand is editorial; otherwise proposes 4 distinct directions (bg/accent/typeface + rationale), asks the user to pick, then implements only that one — pairing with `/frontend-design`.

### `/opus48-scaffold` (no args)
Reads context, then asks: "What are you working on?"
