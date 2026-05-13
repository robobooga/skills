# Skills Repository

A personal collection of Claude Code skills — reusable slash commands and agents for tasks I find valuable enough to keep and share.

## What lives here

Each skill is a self-contained directory following the Claude Code skill format. Skills are open-source and meant to be useful to others as well.

## Adding a skill

Use the `skill-creator` skill (`/skill-creator`) to scaffold, test, and refine new skills before committing them here.

## Documentation

Whenever a new skill is created or an existing skill is renamed/removed, update `README.md`:
- Add a row to the skills table with the skill name (as a link to its directory), category, and a one-line description pulled from the skill's `description` frontmatter field.
- Keep the table sorted alphabetically by skill name within each category.

## Local settings

`.claude/settings.local.json` is gitignored — use it for machine-specific permissions, hooks, or overrides that shouldn't be committed.
