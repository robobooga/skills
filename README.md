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
| [design-craft](design/design-craft/) | design | Build and refine interfaces with real taste — register-aware (brand vs product), anti-AI-slop discipline, design tokens, surfaces/layering, typography, color (OKLCH), motion, UX copy, accessibility, and the validation gates that catch generic output before it ships. |
| [fable5-scaffold](engineering/fable5-scaffold/) | engineering | Align project goals and build features using Fable 5 best practices — reads existing project context, identifies applicable practices (KISS, brevity, parallel workstreams, progress grounding, etc.), and optionally writes them to CLAUDE.md. |
| [opus48-scaffold](engineering/opus48-scaffold/) | engineering | Structure and drive work to play to Claude Opus 4.8's strengths — specify upfront, calibrate effort, control subagent fan-out, handle frontend defaults, and execute with autonomy. Works through a backlog (e.g. "build next few items") or a single feature. |
| [security-audit](engineering/security-audit/) | engineering | Audit code for security vulnerabilities — injection, broken auth/access control, secrets exposure, crypto failures, SSRF, XXE, XSS, insecure deserialization, unsafe file handling, and known-vulnerable dependencies. Every finding traces untrusted input to a dangerous sink and rates exploitability. Targeted and full-sweep modes. |
| [swe-audit](engineering/swe-audit/) | engineering | Audit code for SWE best practices — DRY, SOLID, KISS/YAGNI, naming, magic numbers, complexity, error handling, separation of concerns, Law of Demeter, comments, testing, logging, code smells, and state/mutability. Targeted and full-sweep modes. |
| [deep-dive](productivity/deep-dive/) | productivity | Interview the user about their current task to surface goals, assumptions, and risks — building a clear shared plan before diving in. |
| [explain-simply](productivity/explain-simply/) | productivity | Explain any document, concept, or text in plain everyday language with analogies — no background knowledge required. |
| [ingest-llm-wiki](productivity/ingest-llm-wiki/) | productivity | Ingest a raw source file (PDF, transcript, article) into a structured personal wiki with concept, principle, and topic pages. |
| [llm-council](productivity/llm-council/) | productivity | Pressure-test a decision, plan, or project with six independent advisors who answer separately, peer-review each other anonymously, then get synthesized into one verdict by a chairman. |
| [summarize](productivity/summarize/) | productivity | Summarize the current session into a structured handoff document for resuming later or passing to another LLM. |

## License

MIT
