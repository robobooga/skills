---
name: orchestrate
description: Run a wave of parallel work as an orchestrator — plan features with disjoint file ownership, spawn worker agents in isolated worktrees, review and merge their branches into an integration branch, and deliver one PR for the human to merge. Use when asked to "orchestrate", "pick up the work", "run the next wave", "parallelize this backlog", or coordinate several workers on one codebase.
---

# Orchestrate a wave

The orchestrator is accountable for every line its workers produce. Workers are fast; review is the product.

## 0. Learn the project

Before planning, read `CLAUDE.md` / `AGENTS.md`, the build manifest (`package.json`, `Makefile`, `pyproject.toml`, …) and any backlog or plan doc. Pin down:

- **Verify commands** — typecheck/lint, build, unit tests, e2e. These are the gate for every merge.
- **Backlog source** — a feature map, issues, TODO doc, or the user's request.
- **Hot files** — entry points, registries, shared type files: anything most features would want to edit.
- **Dependencies to share into worktrees** — e.g. `node_modules`, `.venv`, gitignored data or caches.
- **Existing worker agent** — if `.claude/agents/` has one, use it and skip the brief boilerplate it already carries.

If the verify commands can't be found, ask once; don't guess.

## 1. Sync and plan

1. `git fetch && git checkout <main> && git pull --ff-only`, then create or continue an integration branch `feat/<theme>`.
2. Pick a wave of items that can proceed in parallel **with disjoint files**. If two items need the same file, sequence them into separate waves.
3. Assign file ownership per worker:
   - Only one worker per wave may touch each hot file.
   - Shared type/schema files get additive-only changes.
   - Anyone else who needs wiring hands back an integration snippet for the next wave.
4. If the project tracks status, mark the items in progress and commit that on the integration branch.

## 2. Spawn workers

Match the worker to the difficulty: the strongest model for hard or cross-cutting systems, a mid-tier model for well-scoped features, UI and refactors, and the cheapest capable option (a small model, or a free local agent if the project has one) for mechanical one- or two-file edits with an exact spec. Never silently fall back from a free worker to a paid one — ask.

Spawn with `Agent`, `isolation: "worktree"`, in the background, passing `model` per job. Record each worker's name so you can `SendMessage` it later.

### The brief

If there's no project worker agent, every brief carries this standard block (move it into a `.claude/agents/worker.md` once the project has settled — then the brief shrinks to the job alone):

- **Setup:** confirm the worktree contains `<base commit>` (`git merge-base --is-ancestor <base> HEAD`, else reset to it); create branch `<name>`; symlink or copy the shared dependencies from the main checkout (`git worktree list | head -1`).
- **Ownership:** edit only the owned files. Needed a change elsewhere? Don't make it — describe it as an integration snippet. Never edit plan/status docs or agent rules; the orchestrator owns them.
- **Bugs:** reproduce with a failing test first, then fix the root cause, not the symptom.
- **Verify:** `<verify commands>` must all pass before reporting.
- **Commit early:** commit at every green checkpoint. A stopped worker loses everything uncommitted. Never `--no-verify`.
- **Report:** what changed, verification results, root cause with `file:line` (bugs), integration snippets, open questions tagged `NEEDS_HUMAN_INPUT`, final branch and commit sha.

Then the job itself:

- **Item ID(s)** and **base commit**.
- **Ownership:** files it owns, files it must not touch, and what the other workers in the wave are doing.
- **Requirements** with concrete acceptance criteria and any budgets (perf, size, latency). For bugs: the repro you already have, code pointers and suspects.
- **Extra verification:** e.g. screenshot paths in the scratchpad for visual work.

If a rule keeps having to be added to briefs, move it into the worker agent or `AGENTS.md` instead.

## 3. Review each branch as it lands

1. Check the diff stays inside ownership: `git diff --stat <integration>...<branch>`. Anything outside the owned paths needs a reason.
2. Read the full diff against the project's rules: architecture, error handling, resource cleanup, hot-path allocations, config vs hard-coded values, and test quality (behaviour, not implementation).
3. Look at any screenshots or artefacts yourself. If the work is wrong or incomplete, `SendMessage` the worker with specific fixes rather than merging it.
4. `git merge --no-ff <branch>` into the integration branch and resolve conflicts yourself. Re-run the full verify commands after **each** merge, not once at the end.
5. Mark the item done in the project's tracker once merged and green.

## 4. Integrate and deliver

1. After a wave, wire the new modules together using the snippets from worker reports — yourself or via one integration worker that owns the hot files.
2. Run the app and walk the golden path end to end (the `run` skill helps). No console errors; budgets hold.
3. Update the plan/status doc, and add rules to `CLAUDE.md` / `AGENTS.md` for anything future sessions must know.
4. Push the integration branch and open a PR to `<main>` with a summary, review pointers and a test plan. The human merges it.
5. Clean up: `git worktree remove` merged worker worktrees and `git branch -d` merged branches.

## 5. Escalate only real decisions

Batch `NEEDS_HUMAN_INPUT` items — taste, scope, UX, licences, money, anything irreversible — into the final message. Decide everything else yourself and note the default you chose.
