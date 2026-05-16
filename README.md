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
| [explain-simply](productivity/explain-simply/) | productivity | Explain any document, concept, or text in plain everyday language with analogies — no background knowledge required. |
| [ingest-llm-wiki](productivity/ingest-llm-wiki/) | productivity | Ingest a raw source file (PDF, transcript, article) into a structured personal wiki with concept, principle, and topic pages. |
| [summarize](productivity/summarize/) | productivity | Summarize the current session into a structured handoff document for resuming later or passing to another LLM. |

## License

MIT
