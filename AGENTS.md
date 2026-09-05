# Soteris docs operating manual

This is the wake-up handbook for anyone, agent or human, making a small tweak and shipping it. Read it before touching a page, a color, or the config. The design system is deliberately narrow so that changes stay safe.

## What this site is

Partner-facing documentation for Soteris engagement states, records, and verification. Everything Mintlify serves lives in `site/`, the content root: pages are MDX files with YAML frontmatter, configuration is `site/docs.json`, site-wide styling is `site/style.css`, and images sit in `site/images/`. The repo root holds only this manual, the README, and the license. This layout requires Mintlify's "docs.json is in a subdirectory" setting to point at `/site`; verify that setting before publishing a root move. The register is flat and terminal: mono headings, one accent color, tactile texture used once per screen. It is not an API reference.

This repo owns published partner documentation. Portal owns product decisions and official product state; attestation owns agent engineering records; HQ owns shared Git and skill policy. Platform is archived history. Do not infer new product behavior from a documentation move. For work in the shared checkout, read `hq/AGENTS.md` and its relevant skills before GitHub operations.

## Palette law

Seven colors exist. No other color may be introduced anywhere, in `style.css`, in a page, or in `docs.json`. A grader enforces this with a regex over every file.

Brand (four):

- `#100907` ink. Dark background, and text on cream.
- `#E9DDC4` cream. Light background.
- `#FFF4E1` paper. Light elevated surfaces, and text on ink.
- `#F88B43` accent. The one loud thing: links, active nav, primary accents.

Callout semantics (three), used only inside callouts:

- `#4C8B57` ok green. Check callouts.
- `#C9A227` warn yellow. Warning callouts.
- `#A63A2E` danger red. Danger callouts.

In `style.css` these seven are defined once as custom properties on `:root`. Every other value is derived from them with `var()` and `color-mix()`, or from `currentColor`. When you extend the stylesheet, do the same. Never paste a new hex.

## Status chip convention

Lifecycle states and status labels inside tables render as mono inline-code chips. Wrap the label in backticks so it renders as code: `` `Live` ``, `` `Contract preview` ``, `` `Available` ``, `` `proposal_accepted_paid` ``. The words never change. Only the backtick wrapper is added. State names already use backticks; the Live, Contract-preview, and Available statuses join them.

## Callout semantic map

The published corpus uses `<Info>` blocks styled by `site/style.css`; rendered
labels come from the existing stylesheet.
Preserve their content and component shape during a move or styling correction.
The older multi-color Note/Check/Warning/Danger scheme is historical guidance,
not a requirement to convert the current pages back. A new visual convention
requires its own reviewed change.

Typed callouts accept children only. Do not introduce props or new colors as
part of a structural move. Sentences moved into or out of a callout must survive
verbatim unless a separate content edit is approved.

## Voice digest

These ten rules are the repository's voice guidance. A local planning file is
not a prerequisite for working in this checkout:

1. Problem first, then mechanism. Name the gap in one or two flat sentences, then state what the system does.
2. Flat and declarative. Checkpoints are facts, never celebrated.
3. Second person imperative for instructions. Third person declarative for explanation.
4. State scope boundaries as plain paired facts: what a thing does, then what it does not do.
5. Be honest about what does not exist yet, mid-sentence, without apology.
6. Banned marketing words: powerful, seamless, robust, comprehensive, cutting-edge, innovative, streamline, leverage, utilize, facilitate, empower, unlock, supercharge.
7. Banned fillers: very, really, just, simply, actually, basically, "in order to". No adjective triplets. No "whether you are X or Y".
8. No rhetorical questions, no CTAs, no social proof, no emoji, no congratulating the reader.
9. No em dashes, ever. Use periods or commas. This is a standing rule.
10. One idea per sentence. Most sentences stay under about twenty-five words. If a sentence could appear in any product's docs, cut it.

## Exposure rule

These docs describe the interface, not our judgment. They publish the shape a partner reasons with, and nothing about how we reach a conclusion. The repository-owned content boundary is `site/start/disclosure-boundary.mdx`; its operational tests are in `site/reference/exposure-checklist.mdx`. If a line fails a test, it does not ship. Resolve uncertain exposure decisions with Tommy and Cam on the owning Linear issue. Private review material stays in its approved private source and is not copied into this public repository.

Tommy and Cam sign off before any merge. Merge to `main` is deploy. There is no staging step after merge, so the review is the safety net.

## Preview and ship

- Preview locally with `mint dev`, run from inside `site/`. It hot-reloads pages, `docs.json`, and `style.css`.
- Run `mint broken-links` from inside `site/` before any commit. It must pass.
- Every page must render in `mint dev` with no MDX errors.
- Prose integrity is a hard bar. Every sentence in the current corpus must survive verbatim through any styling change. Moves are allowed, edits are not. No new claims, no dropped claims. The only additions styling may make are code-fence titles and component wrapper syntax.
- Keep facts intact: 15 states, 10 outcome statuses, and every Live and Contract-preview label unchanged.

## Swapping placeholders

The current diagrams live in `site/images/diagrams/`, with light and dark
variants referenced by the published pages. Preserve both variants when moving
assets. The former `images/placeholders/` directory is historical. Never ship a
new placeholder or a page whose image or caption still says PLACEHOLDER.

## Navigation and entry points

Navigation and page order live in `site/docs.json` under `navigation.groups`. A new page file does not appear in the site until it is listed there. Adding an `.mdx` file is not enough.

The `sidebarTitle` frontmatter controls the label a page shows in the sidebar. Without it, the sidebar falls back to the page title.

### Page frontmatter

The current corpus uses `title` and `description` on every page. `sidebarTitle`
is optional, for long titles. This entire published surface is public; a tag or
missing tag does not grant permission to publish private material. Preserve the
existing frontmatter during a root move.

Entry points depend on who is arriving:

- Partners arriving cold start at `/start/overview`.
- Partners direct-linked to the state machine land on `/workflow/exception-paths`.
- AI agents start at `/start/agent-guide`.

`README.md` is a pointer. This file, `AGENTS.md`, is the manual.
