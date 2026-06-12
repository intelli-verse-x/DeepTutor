# DeepTutor Website

This directory contains the public DeepTutor website and documentation at `deeptutor.info`.

## Stack

- Astro + Starlight for docs
- English source locale at `/docs/`
- Simplified Chinese mirror at `/zh-cn/docs/`
- Custom landing pages at `/` and `/zh-cn/`
- Static screenshots in `public/screenshots/`
- Cloudflare Pages helpers in `functions/`

## Local Development

```bash
cd site
npm install
npm run dev
```

Build the static site:

```bash
npm run build
```

Preview the built output:

```bash
npm run preview
```

## Documentation Layout

```text
src/content/docs/docs/                 # English docs, route prefix /docs/
src/content/docs/zh-cn/docs/           # Chinese docs, route prefix /zh-cn/docs/
astro.config.mjs                       # Starlight config, sidebar, i18n
src/pages/index.astro                  # English landing page
src/pages/zh-cn/index.astro            # Chinese landing page
public/screenshots/                    # Docs and landing screenshots
```

When adding a docs page, add both locale files in the same relative path. Example:

```text
src/content/docs/docs/partners/channels.md
src/content/docs/zh-cn/docs/partners/channels.md
```

Then add a sidebar item in `astro.config.mjs` with a Chinese translation label.

## Current Docs Map

- `docs/get-started/` — install paths, providers, Docker, multi-user, troubleshooting
- `docs/explore/` — Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory, Settings
- `docs/partners/` — Partner architecture and channel configuration
- `docs/cli/` — CLI, command reference, agent handoff, server API

Legacy `docs/tutorbot/` pages are retained as migration notices so old links do not hard 404. Product-facing docs should point to `docs/partners/`.

## Screenshot Policy

Prefer screenshots synced from the main repository's canonical assets in `assets/figs/`, or freshly captured from a running local DeepTutor UI. Keep docs references under `/screenshots/...` and verify the files exist before building.

## Checks

Before publishing, run:

```bash
npm run build
```

Useful extra checks from the repository root:

```bash
python - <<'PY'
from pathlib import Path
root = Path('site/src/content/docs')
en = {p.relative_to(root / 'docs').as_posix() for p in (root / 'docs').rglob('*.md')}
zh = {p.relative_to(root / 'zh-cn/docs').as_posix() for p in (root / 'zh-cn/docs').rglob('*.md')}
print('only_en', sorted(en - zh))
print('only_zh', sorted(zh - en))
PY
```

Both lists should be empty; otherwise language switching can fall back to the wrong locale.
