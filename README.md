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
| [summarize](productivity/summarize/) | productivity | Summarize the current session into a structured handoff document for resuming later or passing to another LLM. |

## Adding a skill

1. Run `/skill-creator` in Claude Code to scaffold, test, and refine the skill.
2. Place it under the appropriate category folder: `<category>/<skill-name>/SKILL.md`.
3. Update the table above.

## License

MIT
