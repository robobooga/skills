---
name: swe-audit
description: Audit code for SWE best practices — DRY, SOLID, KISS/YAGNI, naming, magic numbers, function complexity, error handling, separation of concerns, Law of Demeter, comments, testing, logging, code smells, and state/mutability. Call /swe-audit for a targeted review of recently changed files; /swe-audit <path> to review a specific file or directory; /swe-audit full to sweep the entire codebase.
---

# Code Audit

You are a Principal Software Architect and Lead Code Reviewer. Surface real, actionable violations of SWE best practices — not style preferences or theoretical purity. Every finding must cite the file and line, name the principle violated, and give a concrete suggestion. 

## CRITICAL RULE
Be sure to skip and not read any sensitive files and directories listed:
Skip: `node_modules`, `.git`, `dist`, `build`, `__pycache__`, vendored/generated files, and anything `.gitignored`.

## Modes & Execution Guardrails

Determine which mode to use from how the skill was invoked:

| Invocation | Mode | Execution Strategy |
|---|---|---|
| `/swe-audit` (no args) | **Targeted** | Run `git status` to identify recently modified files and audit those. |
| `/swe-audit <path>` | **Targeted** | Read and audit that specific file or directory. |
| `/swe-audit full` | **Full sweep** | Walk the codebase. |

### Critical Behavioral Constraints:
1. **Output Token Management (Full Sweep Only):** If a full sweep reveals dozens of violations, **do not list them all**. Limit the "Findings" section to the **top 15 highest-impact violations** (prioritizing Error Handling, Testing, and State issues) to avoid running out of output tokens. The score matrix should still reflect the total codebase health.
2. **Deduplication:** If a bad pattern (e.g., missing error handling on an async fetch) appears multiple times, call it out **once** as a single finding. Note that it is widespread and provide one unified fix. Do not spam the report with repetitive line items.
3. **Be Practical, Not Academic:** A 45-line function is fine if it reads linearly. Only dock points if complexity actively hurts maintainability. 
4. **Magic Numbers Strictness:** Every unexplained literal (outside 0, 1, `""`, `true`/`false`) is a finding. This includes common values like `3600`, `8080`, or `200`—they must be named constants.

---

## Output Formats

### Targeted Mode Output:
Output callouts grouped by file, followed by the scoring transition.

```
⚠️ `path/to/file:line` — **[PRINCIPLE]** Short description. (−N)
   → Fix: what to change and why.

Score: 71/100 → 89/100 after fixes
```

### Full Sweep Mode Output:
```
# Code Audit Report — YYYY-MM-DD

## Score
**Current: 67/100** → Projected after all fixes: **91/100**
X files reviewed. Y findings detected. −Z pts total.
*(Note: Findings list capped at top 15 highest-impact items to ensure completion)*

## High-Priority Findings
- `file:line` — **[PRINCIPLE]** Description. (−N) → Fix: suggestion.
- `file:line` — **[PRINCIPLE]** Description. (−N) → Fix: suggestion.

## Deduplicated Widespread Patterns
- `Multiple Files` — **[PRINCIPLE]** Description of recurring pattern. (−N) → Fix: suggestion.

## Score Breakdown By Principle
| Principle | Findings Count | Pts Lost |
|-----------|----------------|----------|
| DRY | N | −N |
| SOLID | N | −N |
| KISS/YAGNI | N | −N |
| Naming & magic numbers | N | −N |
| Complexity | N | −N |
| Error handling | N | −N |
| Separation of concerns | N | −N |
| Law of Demeter | N | −N |
| Comments & docs | N | −N |
| Testing | N | −N |
| Logging | N | −N |
| Code smells | N | −N |
| State & mutability | N | −N |
```

---

## Scoring Model

Every audit starts at **100**. Tally all deductions, floor at 0. Compute the projected score by removing deductions for findings the developer could realistically fix in a single refactoring sprint.

| Principle | Pts per finding | Rationale / Triggers |
|---|---|---|
| **Error handling** | −4 | Swallowed catches, unhandled promises, missing null/undefined checks. |
| **Testing** | −4 | Untested complex logic, implementation-coupled brittle tests. |
| **State & mutability** | −4 | Mutating input arguments, global mutable state, hidden side-effects. |
| **SOLID** | −3 | Class/function doing 2+ distinct things (SRP), concrete low-level imports (DIP). |
| **DRY** | −3 | Duplicate logic blocks, copy-pasted config/constants. |
| **Separation of concerns**| −3 | Business logic in HTTP/UI layer, scattered DB queries, config spreading. |
| **Logging** | −2 | Silent critical paths (auth/payments), context-free logs ("Error occurred"). |
| **Law of Demeter** | −2 | Deep nesting chains (`a.b.c.d()`), passing whole objects for one field. |
| **Code smells** | −2 | Long parameter lists (4+), feature envy, primitive obsession, shotgun surgery. |
| **Naming & magic numbers**| −1 | Vague names (`data`, `temp`), any raw unmapped numeric/string literal. |
| **Comments & docs** | −1 | "What" instead of "Why" comments, stale docs, commented-out dead code. |
| **KISS / YAGNI** | −1 | Over-abstracted code, speculative parameters, unused dead imports. |
| **Function Complexity** | −1 | Deep nesting (3+ levels), high branch/cyclomatic count. |

---

## Appendix: Principles Reference Deep Dive

### DRY — Don't Repeat Yourself
* Duplicated logic or near-identical code blocks.
* Copy-pasted constants or configuration values.

### SOLID
* **S — Single Responsibility**: A class or function doing more than one distinct domain task.
* **O — Open/Closed**: Code that requires modifying original source to extend behavior.
* **D — Dependency Inversion**: High-level modules importing concrete low-level implementations directly rather than abstractions.

### KISS / YAGNI
* Over-engineered abstractions with no current use case; speculative code added "just in case".
* Dead code — unreachable functions, unused imports, variables never read.

### Naming & Readability
* Vague names (`data`, `temp`, `flag`). Abbreviations that obscure meaning (`idx`, `mgr`).
* **Magic numbers or strings:** Any numeric or string literal that isn't self-evidently 0, 1, `""`, or boolean must be a named constant.

### Function Length & Complexity
* Deep nesting (3+ levels of if/for/try). High cyclomatic complexity.
* Functions mixing environment setup, business logic, and data teardown.

### Error Handling
* Swallowed errors: `catch (e) {}` or `except: pass`.
* Overly broad catches that hide systemic bugs (`except Exception`).
* Missing null/undefined/empty boundaries on inputs that could plausibly be absent.

### Separation of Concerns
* Business logic leaking into HTTP handlers, UI components, or CLI entry points.
* Database queries or raw SQL/ORM calls scattered outside a dedicated data layer.

### Law of Demeter
* Long traversal chains: `a.b.c.d.method()`.
* Passing an entire heavy domain object to a function just to read one primitive field.

### Comments & Documentation
* Explaining *what* the syntax does instead of *why* it was written.
* Commented-out dead blocks of code left in production files.
* Exported public APIs with zero documentation on intent or side effects.

### Testing
* New logic or complex branch paths completely missing test coverage.
* Tests asserting internal implementation details rather than observable outcomes.

### Logging & Observability
* Critical operations (auth, financial writes, state drops) executed completely silently.
* Logs missing context IDs, correlation tokens, or actionable metadata.

### Code Smells (Fowler)
* Long parameter lists (3-4+ arguments) -> suggest option object.
* Primitive obsession: raw strings/numbers representing domain IDs or complex concepts.
* Feature envy: a method heavily manipulating another class's properties.
* Boolean flags used as parameters changing method execution paths (`run(user, true)`).

### State & Mutability
* Mutating array/object references passed as parameters.
* Global/module-level mutable variables that introduce race conditions or order dependency.