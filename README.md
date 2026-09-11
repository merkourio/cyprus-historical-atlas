# Cyprus Historical Atlas

An interactive, single-file atlas for browsing the history of Cyprus by timeline.

Open `cyprus-historical-explorer.html` in a browser — no build step, no server, no dependencies beyond the CDN libraries it loads at runtime.

## What it does

- A rotatable D3 orthographic globe (World / Region / Island presets) showing 131 settlements across 16 eras, from prehistory to the present.
- Era-aware city-kingdom territories, empire borders, and neighbouring polities, each drawn from the snapshot nearest the year on screen.
- A site drawer with 1,145+ archaeological finds, sourced events, rulers, and a "Life on the island" panel (population, economy, language, religion) per era.
- Recommended reading per era, fact-checked against Open Library / Crossref.
- English, Greek, and Turkish interface (site names, eras, powers); scholarly prose stays English.
- Kind-based filtering via the legend, zoom-aware label decluttering, and a resizable side panel.

## Repo layout

- `cyprus-historical-explorer.html` — the deliverable: a self-contained page with all data, styles, and logic inline.
- `research/` — the data pipeline and working notes behind the atlas: per-era research JSON, merge/reconcile/roundtrip scripts, empire-extent and neighbouring-region builders, palette and emblem checkers, i18n sources, and planning docs (`BRIEF.md`, `EXPANSION-PLAN.md`, `ROADMAP.md`).

## Status

Content fact-checked by research agents against cited sources (`research/*.json` carry `sources` per era/site). See `research/ROADMAP.md` for planned next features and `research/EXPANSION-PLAN.md` for how the current dataset was built.
