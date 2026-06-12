# Skills

A personal collection of Claude Code skills — reusable slash commands and agents for tasks worth keeping and sharing.

## Installing a skill

Uses the [`npx skills`](https://github.com/vercel-labs/skills) CLI. Install a specific skill by name:

```bash
npx skills add robobooga/skills --skill summarize
```

Or install everything at once and pick interactively:

```bash
npx skills add robobooga/skills
```

After installing, the skill is available as a slash command in Claude Code (e.g. `/summarize`).

## Available skills

| Skill | Category | Description |
|-------|----------|-------------|
| [fable5-scaffold](engineering/fable5-scaffold/) | engineering | Align project goals and build features using Fable 5 best practices — reads existing project context, identifies applicable practices (KISS, brevity, parallel workstreams, progress grounding, etc.), and optionally writes them to CLAUDE.md. |
| [swe-audit](engineering/swe-audit/) | engineering | Audit code for SWE best practices — DRY, SOLID, KISS/YAGNI, naming, magic numbers, complexity, error handling, separation of concerns, Law of Demeter, comments, testing, logging, code smells, and state/mutability. Targeted and full-sweep modes. |
| [deep-dive](productivity/deep-dive/) | productivity | Interview the user about their current task to surface goals, assumptions, and risks — building a clear shared plan before diving in. |
| [explain-simply](productivity/explain-simply/) | productivity | Explain any document, concept, or text in plain everyday language with analogies — no background knowledge required. |
| [ingest-llm-wiki](productivity/ingest-llm-wiki/) | productivity | Ingest a raw source file (PDF, transcript, article) into a structured personal wiki with concept, principle, and topic pages. |
| [summarize](productivity/summarize/) | productivity | Summarize the current session into a structured handoff document for resuming later or passing to another LLM. |

## License

MIT
