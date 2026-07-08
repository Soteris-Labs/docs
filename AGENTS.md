# Soteris docs operating manual

This is the wake-up handbook for anyone, agent or human, making a small tweak and shipping it. Read it before touching a page, a color, or the config. The design system is deliberately narrow so that changes stay safe.

## What this site is

Partner-facing documentation for Soteris engagement states, records, and verification. Pages are MDX files with YAML frontmatter. Configuration lives in `docs.json`. Site-wide styling lives in `style.css`. The register is flat and terminal: mono headings, one accent color, tactile texture used once per screen. It is not an API reference.

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

There are four content shapes and each maps to exactly one component. Sentences inside a callout are moved verbatim from the prose. They are never rewritten.

| Content shape | Component | Color |
| --- | --- | --- |
| Neutral boundary statement ("this page names X, not Y") | `<Note>` | neutral ink or cream tones |
| Live or available confirmation ("stable to map against") | `<Check>` | ok green |
| Partner-behavior warning ("do not model termination") | `<Warning>` | warn yellow |
| Moat statement (the never-publish side) | `<Danger>` | danger red |

Danger appears exactly three times corpus-wide, on these pages only: `verification/what-verification-excludes`, `start/disclosure-boundary`, and `reference/exposure-checklist`. That scarcity is the point. Do not add a fourth. Warning appears where a partner could build the wrong thing. Check appears where we confirm something is safe to rely on. Everything else is Note.

Typed callouts (`Note`, `Warning`, `Info`, `Tip`, `Check`, `Danger`) accept only children. Do not add props to them. If you need a custom icon or color, use `<Callout>`, but the palette law still holds.

## Voice digest

The full brief is in the plan file `docs-voice-brief.md`. The ten rules that matter here:

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

These docs describe the interface, not our judgment. They publish the shape a partner reasons with, and nothing about how we reach a conclusion. Before you add or change content, run it against the tests on `reference/exposure-checklist`. If a line would fail a test, it does not ship. The content law is `cam-review/EXPOSURE_POLICY.md` in the plan; it decides what may be said.

Tommy and Cam sign off before any merge. Merge to `main` is deploy. There is no staging step after merge, so the review is the safety net.

## Preview and ship

- Preview locally with `mint dev`. It hot-reloads pages, `docs.json`, and `style.css`.
- Run `mint broken-links` before any commit. It must pass.
- Every page must render in `mint dev` with no MDX errors.
- Prose integrity is a hard bar. Every sentence in the current corpus must survive verbatim through any styling change. Moves are allowed, edits are not. No new claims, no dropped claims. The only additions styling may make are code-fence titles and component wrapper syntax.
- Keep facts intact: 15 states, 10 outcome statuses, and every Live and Contract-preview label unchanged.

## Swapping placeholders

Placeholder images live in `images/placeholders/`. Each one is a brand SVG that carries the literal word PLACEHOLDER on its face, so a stand-in can never ship unnoticed. To swap one, replace the file with the real diagram and remove the word "Placeholder" from the caption in the `<Frame>` that holds it. Never ship a page whose rendered output still says PLACEHOLDER, in the image or the caption.
