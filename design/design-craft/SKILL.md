---
name: design-craft
description: Build and refine interfaces with real taste — distilled from craft-design philosophy, product UI systems, brand/marketing design, and UX/accessibility best practice. Use when designing, building, reviewing, or polishing any UI — dashboards, apps, landing pages, components, forms, settings, onboarding, empty states. Covers visual direction, anti-AI-slop discipline, design tokens, surfaces/layering, typography, color, motion, UX copy, accessibility, and the validation gates that catch generic output before it ships. Not for backend-only work.
---

# Design Craft

A distilled discipline for making software that feels *designed*, not defaulted. In a world where everyone's software is "good enough," taste is the differentiator and beauty is leverage. This skill exists to stop you from shipping the generic thing your training pulls toward.

Use it to **build** new UI, **review/critique** existing UI, or **polish** before shipping. When critiquing code, output a `| Before | After | Why |` markdown table — one row per issue.

---

## The Stance

Internalize these before touching code. They are the difference between output that works and output that feels right.

- **Taste is trained, not innate.** It's the instinct to see beyond the obvious. Reverse-engineer interfaces you admire; ask *why* something feels good.
- **Unseen details compound.** Most polish users never consciously notice — that's the point. A thousand barely-audible voices singing in tune. The aggregate of invisible correctness is what people love without knowing why.
- **Beauty is leverage.** People choose tools on the whole experience, not just function. Good defaults and good motion are real differentiators. Beauty is underused in software.
- **Every choice must be a choice.** For every decision — layout, color temperature, typeface, spacing, hierarchy — you must be able to say *why*. "It's clean / it's common / it works" means you defaulted. Defaults are invisible; invisible choices compound into generic output.
- **Sameness is failure.** If another AI, given a similar prompt, would produce substantially the same thing, you failed. Not difference for its own sake — the interface should *emerge from the specific problem*. When you design from intent, sameness becomes impossible.

**The slop test (run it twice).** If someone could look at this and say "AI made that" without hesitation, it failed.
- *First-order:* Could someone guess the theme + palette from the **product category alone**? Then it's the first training reflex. Rework.
- *Second-order:* Could they guess it from **category + the obvious anti-reference** ("AI tool that's not SaaS-cream → editorial-typographic"; "fintech that's not navy-and-gold → terminal-dark")? Then it's the trap one tier deeper. Rework until neither answer is obvious.

---

## First Move: Pick the Register, Then the Intent

Two registers. Identify which before anything else — they have different bars and different permissions.

| | **Brand** (design IS the product) | **Product** (design SERVES the product) |
|---|---|---|
| Surfaces | Landing pages, marketing, portfolios, campaigns, long-form, about pages | Dashboards, admin, tools, settings, data tables, app shells, authed surfaces |
| Goal | Communicate. A visitor's *impression* is the deliverable. | Transact. The tool should *disappear into the task*. |
| Failure mode | Flatness, timidity, "safe = invisible." Average is no longer findable. | Strangeness without purpose — over-decorated buttons, gratuitous motion, invented affordances. |
| Bar | Distinctiveness. Visitor asks "how was this made?" not "which AI made this?" | Earned familiarity. A user fluent in Linear/Stripe/Notion *trusts* it instantly. |
| Permissions | Ambitious page-load motion, drenched color, art-direction per section, single dominant idea per fold. | System fonts, standard nav patterns, density, consistency over surprise. |

**Then state the intent** (keep it a compact working brief; ask one question only if genuinely ambiguous):

- **Who is this human?** Not "users." The actual person — where they are, what they did 5 minutes ago, what's on their mind. A teacher at 7am ≠ a dev debugging at midnight ≠ a founder between meetings.
- **What must they accomplish?** The verb. *Grade these. Find the broken deploy. Approve the payment.* This determines what leads, follows, hides.
- **What should it feel like?** Words that mean something. "Clean and modern" means nothing. Warm like a notebook? Cold like a terminal? Dense like a trading floor? Calm like a reading app?

**Intent must be systemic.** Saying "warm" then using cold grays is not following through. If warm: surfaces, text, borders, accents, type — *all* warm. Check every token against the stated intent.

**Name a reference (brand).** Before committing, name the aesthetic lane out loud — "Stripe purple-on-white restraint," "Klim orange drench," "Linear terminal-dark." Unnamed ambition decays into beige. Then the inverse test: describe what you're about to build the way a competitor would describe theirs. If that sentence fits the modal page in the category, restart.

---

## Kill the Defaults

Defaults disguise themselves as *infrastructure* — the parts that feel like they just need to work, not be designed. There are no structural decisions. Everything is design.

- **Typography isn't a container — it IS the design.** The type that's warm-and-handmade is not the type that's cold-and-precise, even if both are "clean and readable." Reaching for your usual font = not designing.
- **Navigation isn't scaffolding — it IS the product.** A page floating in space is a component demo. Nav teaches people how to think about the space.
- **Data isn't presentation.** A number on screen is not design. What does it *mean* to the person looking? A progress ring and a stacked label both show "3 of 10" — one tells a story.
- **Token names are design decisions.** `--ink` / `--parchment` evoke a world; `--gray-700` / `--surface-2` evoke a template. Someone reading only your tokens should guess what product this is.

### Font reflex-reject (greenfield brand choices)

These are training-data defaults. If your first three picks include any of them, reject and look further (Pangram Pangram, Future Fonts, Klim, Velvetyne, real catalogs):

> Inter · Roboto · Arial · DM Sans · DM Serif · Space Grotesk · Space Mono · Plus Jakarta Sans · Outfit · Instrument Sans/Serif · Fraunces · Playfair Display · Cormorant · Crimson · Lora · Newsreader · Syne · IBM Plex (Sans/Serif/Mono)

**Selection procedure:** (1) Write three concrete brand-voice words — physical-object words ("warm, mechanical, opinionated"), not "modern/elegant." (2) Find the font for the brand *as a physical object* — a museum caption, a 1970s terminal manual, a fabric label, a diner receipt. (3) Cross-check: "elegant" ≠ necessarily serif, "technical" ≠ necessarily sans. If the final pick matches your reflex, start over. *(Product UI is exempt — a well-tuned system sans like Inter/SF is a legitimate product choice. The reflex list is for brand surfaces.)*

### Color reflexes

- **The cream/sand/beige body background is the saturated AI default.** The whole warm-neutral band (OKLCH L 0.84–0.97, C < 0.06, hue 40–100) reads as paper/parchment no matter what you name it. Token names like `--paper`, `--cream`, `--sand`, `--linen`, `--ivory` are tells. "Warm/editorial/magazine" briefs do NOT mean a warm-tinted near-white bg — that's the AI move. Carry warmth through accent + type + imagery instead. Pick: a saturated brand color as the body, a true off-white at chroma 0, or a darker tinted mid-tone that's clearly the brand's own.
- **Use OKLCH.** Tint neutrals 0.005–0.015 toward the brand hue — don't default-tint warm "because it feels that way" (that's the monoculture move).
- **Pick a color strategy before colors:** *Restrained* (tinted neutrals + one accent ≤10% — product default) → *Committed* (one saturated color carries 30–60%) → *Full palette* (3–4 named roles) → *Drenched* (the surface IS the color). Brand earns Committed/Drenched; product floors at Restrained.
- **Dark vs light is never a default.** Write one sentence of physical scene (who, where, what ambient light, what mood). If it doesn't force the answer, add detail until it does.

### Absolute bans

Match-and-refuse. If you're about to write one, rewrite the element with different structure.

- **Side-stripe borders** (`border-left` > 1px as a colored accent on cards/alerts). Use full borders, bg tints, or leading icons.
- **Gradient text** (`background-clip: text` on a gradient). Solid color; emphasis via weight/size.
- **Glassmorphism as decoration.** Rare and purposeful, or nothing.
- **The hero-metric template** (big number, small label, supporting stats, gradient accent). SaaS cliché.
- **Identical card grids** (same-size cards, icon + heading + text, repeated endlessly). Nested cards are *always* wrong.
- **Tiny uppercase tracked eyebrow above every section** ("ABOUT" / "PROCESS"). One named kicker is voice; an eyebrow on every section is AI grammar.
- **Numbered section markers as scaffolding** (01 / 02 / 03). Earn it only when the section IS a real sequence.
- **Emoji as structural icons.** Vector icons (Lucide, Phosphor, Heroicons) — one set, consistent stroke width.
- **Purple gradients on white.** The single most recognizable AI fingerprint.

### The four catch-tests (run before showing the user)

- **Swap test:** If you swapped your typeface for your usual one, or your layout for a standard template, would it feel meaningfully different? Where swapping wouldn't matter is where you defaulted.
- **Squint test:** Blur your eyes. You should still perceive hierarchy — what's above what, where regions divide — but nothing should jump out harshly. Craft whispers.
- **Signature test:** Can you point to five specific elements where your signature appears? "The overall feel" doesn't count. A signature you can't locate doesn't exist.
- **Token test:** Read your CSS variables aloud. Do they belong to *this* product's world, or any project?

If any fails, iterate before showing. **Your first output is probably generic — that's normal. The work is catching it before the user has to.**

---

## Craft Foundations (the quality floor)

This applies regardless of register or style. Subtle layering is the backbone — you should *barely notice the system working*.

### Tokens
Every color traces to a small set of primitives: **foreground** (text), **background** (surface), **border**, **brand**, **semantic** (destructive/warning/success/info). No random hex — everything maps to a primitive.
- **Four text levels**, used consistently: primary (default) → secondary (supporting) → tertiary (metadata) → muted (disabled/placeholder). Only using two = hierarchy too flat.
- **Border progression**, not binary: default → subtle → strong (hover) → stronger (focus ring). Match intensity to the boundary's importance.
- **Dedicated control tokens** (control-bg, control-border, control-focus) so inputs tune independently from layout surfaces.

### Surfaces & layering
Surfaces stack: dropdown > card > page. Build a numbered elevation scale. Each jump is only **a few percentage points of lightness** — invisible in isolation, felt when stacked. In dark mode, higher = slightly lighter and lean on borders (shadows barely show).
- **Sidebars:** same background as the canvas + a subtle border. Different colors fragment the space into "sidebar world" and "content world."
- **Inputs are inset:** slightly *darker* than their surroundings, not lighter. Signals "type here" without heavy borders.
- **Dropdowns:** exactly one level above their parent surface.
- **Borders:** low-opacity rgba (≈0.05–0.12 alpha in dark) — disappears when you're not looking, findable when you need structure. Solid hex borders look harsh.

### Spacing
Pick a base unit (4 or 8px) and use multiples — micro (icon gaps) → component (within buttons/cards) → section (between groups) → major (between areas). Random values signal no system. **Padding symmetrical** — TLBR match unless content genuinely needs asymmetry.

### Typography
Build levels distinguishable at a glance via **size + weight + letter-spacing** (not size alone). Headlines: heavier, tighter tracking for presence. Body: comfortable weight. Labels: medium at small sizes. Data: monospace with `tabular-nums` for column alignment.
- Body line length **65–75ch**. Step ratio **≥1.25** (brand) / 1.125–1.2 (dense product). Flat scales read as uncommitted.
- **≤3 families** (display + body + optional mono). Pair on a contrast axis (serif + sans, geometric + humanist) — never two similar sans. One well-tuned family with weight contrast usually beats three.
- `text-wrap: balance` on h1–h3; `text-wrap: pretty` on long prose. Hero `clamp()` max ≤6rem. Display letter-spacing floor ≥ −0.04em. No all-caps body copy.

### Depth — pick ONE and commit
Borders-only (dense tools) · subtle single shadow (approachable) · layered shadow (premium, dimensional) · surface-color shift (tints without shadow). **Don't mix.** Radius: small for inputs/buttons, medium for cards, large for modals — a scale, not random.

```css
--shadow-layered:
  0 0 0 0.5px rgba(0,0,0,0.05),
  0 1px 2px rgba(0,0,0,0.04),
  0 2px 4px rgba(0,0,0,0.03),
  0 4px 8px rgba(0,0,0,0.02);
```

### Color carries meaning
Gray builds structure; color communicates — status, action, emphasis, identity. **One accent used with intention beats five used without.** Unmotivated color is noise. Verify contrast: body text ≥4.5:1, large/bold ≥3:1, placeholders the same 4.5:1. The single biggest reason AI designs feel hard to read: muted gray text "for elegance" on a tinted near-white. When close, bump toward the ink end.

### States are not optional
Every interactive element: default, hover, focus-visible, active, disabled. Every data view: loading (skeleton, not a centered spinner), empty (teaches the interface, not "nothing here"), error (states cause + recovery path). Missing states feel broken. Build custom components for `<select>` / `<input type="date">` — native renders unstyleable OS chrome.

---

## Motion

Motion is part of the build, not an afterthought — but most things should animate *less* than you think.

**1. Should it animate at all?** (frequency decides)

| Frequency | Decision |
|---|---|
| 100+×/day (keyboard shortcuts, command palette) | **No animation. Ever.** |
| Tens×/day (hover, list nav) | Drastically reduce or remove |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-run (onboarding, celebration) | Can add delight |

Never animate keyboard-initiated actions — they're repeated hundreds of times daily and animation makes them feel slow. Raycast has no open/close animation. That's correct.

**2. Purpose.** Every animation answers "why does this animate?" — spatial consistency, state indication, feedback, or preventing jarring change. "It looks cool" + seen often = don't.

**3. Easing.** Entering/exiting → **ease-out** (instant feedback). Moving/morphing on-screen → ease-in-out. Hover/color → ease. Constant (marquee, progress) → linear. **Never ease-in for UI** — it delays the moment the user is watching most. Built-in CSS easings are too weak; use custom curves:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);      /* UI interactions */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);  /* on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);   /* iOS-like drawer */
```

**4. Duration.** Button press 100–160ms · tooltips 125–200ms · dropdowns 150–250ms · modals/drawers 200–500ms. **UI animations stay under 300ms.** A 180ms dropdown feels more responsive than 400ms. Exit faster than enter (~60–70%). Perceived speed matters as much as real speed — a faster spinner makes loading *feel* faster.

**Component rules that compound:**
- **Buttons feel responsive:** `transform: scale(0.97)` on `:active`, `transition: transform 160ms ease-out`.
- **Never animate from `scale(0)`** — nothing in the real world appears from nothing. Start `scale(0.95)` + `opacity: 0`.
- **Origin-aware popovers:** scale from their trigger (`transform-origin: var(--radix-popover-content-transform-origin)`), not center. *Exception: modals stay centered.*
- **Transitions over keyframes** for rapidly-triggered UI (toasts, toggles) — transitions retarget mid-flight; keyframes restart from zero.
- **`@starting-style`** for enter animations without JS. **Stagger** lists 30–80ms between items.
- **Springs** for drag/momentum/interruptible gestures ("alive" feel). Apple-style `{ duration: 0.5, bounce: 0.2 }`; keep bounce 0.1–0.3 and avoid it in most UI.
- **Performance:** animate only `transform` and `opacity` (GPU; skips layout/paint). Blur/backdrop-filter/clip-path/mask are legitimate premium materials when smooth (keep blur <20px). Don't update inheritable CSS vars on a parent during drag — set `transform` on the element directly.
- **Reduced motion is not optional.** Every animation needs a `@media (prefers-reduced-motion: reduce)` path — usually a crossfade. Keep opacity/color, drop movement. Gate hover effects behind `@media (hover: hover) and (pointer: fine)`.

**By register:** product motion is 150–250ms, conveys state only, no orchestrated page-loads (users are in flow). Brand can afford one well-orchestrated page-load reveal — but not fade-on-scroll on every section (that uniform reflex is the tell, and class-gated reveals ship blank on hidden tabs / headless renderers).

---

## Copy & Voice

UX copy is design. Every word earns its place — no restated headings, no intros that repeat the title.

- **No em dashes** (and no `--`). Use commas, colons, semicolons, periods, parentheses.
- **No marketing buzzwords:** streamline / empower / supercharge / leverage / unleash / seamless / world-class / enterprise-grade / next-generation / game-changer. Pick a specific noun + a verb describing what it literally does.
- **No aphoristic cadence** as default voice (serious statement → punchy short negation, repeated). If 3+ blocks land on a short rebuttal sentence, rewrite. Specific, not aphoristic.
- **Buttons: verb + object.** "Save changes" > "OK"; "Delete project" > "Yes." The label says what will happen.
- **Links read standalone.** "View pricing plans" > "Click here" (screen readers announce out of context).
- **No all-caps body** — reserve caps for short labels (≤4 words) and badges.
- **Alt text is voice:** "Coastal fettuccine, hand-cut, served on the terrace" > "pasta dish."

---

## Accessibility & UX Floor

Non-negotiable, both themes, before shipping:

- **Contrast:** body ≥4.5:1, large/bold ≥3:1, UI glyphs/data lines ≥3:1. Test dark mode independently. Color is never the *only* signal — pair with icon/text/pattern.
- **Touch targets ≥44×44pt** with ≥8px spacing; expand hit area for small icons. Tap feedback within ~100ms. Primary action: one per screen; secondary visually subordinate.
- **Keyboard:** full nav, tab order matches visual order, visible `:focus-visible` rings (never remove them), Esc/cancel in modals and multi-step flows, focus the first invalid field after a failed submit.
- **Semantic first:** real headings (sequential, no skips), landmarks, `<label for>`, button/link semantics, `aria-label` on icon-only controls, `aria-live`/`role="alert"` for errors and toasts (toasts don't steal focus).
- **Forms:** visible labels (not placeholder-only), error below the field stating cause + fix, validate on blur not keystroke, mark required, semantic input types for the right mobile keyboard, undo for destructive actions.
- **Performance/layout:** reserve space for async content (CLS < 0.1), `width`/`height` or `aspect-ratio` on media, lazy-load below the fold, modern formats (WebP/AVIF), virtualize 50+ item lists, skeleton (not spinner) past ~300ms. Verify image URLs resolve before referencing — guessed IDs ship as broken-image placeholders; prefer fewer images you're sure of.
- **Responsive is structural** (collapse sidebar, reflow table, breakpoint columns), not fluid typography. Test 375px and landscape; headings must not overflow at any width. `min-h-dvh` over `100vh` on mobile. Respect safe areas.
- **Build pipeline:** edit source and run the project's build; never write to `dist/`/`.next/` directly (skips hashing, optimization, splitting).

---

## Workflow

**Greenfield:**
1. **Register + intent** — pick brand/product; state who/what/feel; name the aesthetic reference.
2. **Explore the domain** — concepts, metaphors, vocabulary, and the colors that *exist in this product's world*. Name one **signature** element that could only exist for THIS product. Name the 3 obvious defaults you'll reject.
3. **Propose** a direction that references all of the above. Confirm only when ambiguous or costly to change; otherwise state the assumption and proceed.
4. **Set the system** — OKLCH palette + strategy, type, spacing base, depth approach, surface scale — each choice tied back to intent.
5. **Build** to production quality: real content/imagery (no placeholders, no colored `<div>` where a hero photo belongs), full state coverage, semantic markup, intentional motion.
6. **Critique against the gates** (below), patch what fails, **then** show.

**Existing project:** read the tokens, theme, and a representative component *first*. Use what's there; identity-preservation beats the reflex lists — variants on a shipping surface don't second-guess committed brand choices. Extend the system, don't reinvent it.

**Before showing — the gates (don't compress):**
- Slop test (first + second order) · swap / squint / signature / token tests
- Contrast verified both themes · every state present (hover/focus/active/disabled/loading/empty/error)
- Responsive composes (not shrinks) at mobile/tablet/desktop · no overflow · reduced-motion path
- **Verify visually** when the harness allows (browser/screenshot) — a screenshot you didn't read doesn't count. Fix visible overlap, broken spacing, blank states, unreadable text before presenting.

Don't invent defects to demonstrate iteration — a confident "first pass clean, shipping" beats a fake fix. The exit bar: **defensible in a high-end studio review.**

**When reviewing others' code,** lead with the highest-impact issues and use the table:

| Before | After | Why |
| --- | --- | --- |
| `transition: all 300ms` | `transition: transform 200ms var(--ease-out)` | Name exact properties; `all` animates layout props and drops frames |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` | Nothing in the real world appears from nothing |
| `--gray-700` on a "warm bakery" brief | `--crumb` / `--rye`, tied to the domain | Token names are design decisions; generic names betray a template |
| Gray body text on tinted near-white | Bump toward ink, verify ≥4.5:1 | The #1 reason AI UI reads as hard to read |
