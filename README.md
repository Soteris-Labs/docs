# Soteris partner docs

Partner-facing documentation for Soteris, served by Mintlify. Merging to `main` deploys to production, with no staging step after merge.

`AGENTS.md` is the operating manual. Read it before touching a page, a color, or the config.

## Layout

- `site/` is the Mintlify content root: `docs.json`, `style.css`, `images/`, and the six page sections. Mintlify is pointed at it through the dashboard setting "docs.json is in a subdirectory" (`/site`). Page URLs are relative to `site/`, so moving the root did not change any link.
- The repo root holds only this file, `AGENTS.md`, and `LICENSE`.

## Commands

Run both from inside `site/`.

- `mint dev` previews the site locally with hot reload.
- `mint broken-links` checks every link. It must pass before any commit.

## Sign-off

No merge without Tommy and Cam. The review is the safety net, because merge is deploy.
