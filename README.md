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

## Visual overhaul

The working overhaul uses one timeline dock with a named period selector and exact
year entry. A reading column separates Overview, Places and Sources; selecting a
place opens a stable record in that column, or a collapsible phone sheet. Changing
the date updates the record's occupation status without replacing its contents.

The interface includes explicit light/dark/system themes, non-colour site symbols,
keyboard-accessible records, touch-friendly filter isolation, zoom controls and
links carrying the period, language, preset view, selected site and filters.

For a local preview, serve this directory with a local static server and open
`cyprus-historical-explorer.html`. Direct file opening remains supported with the
same externally loaded map libraries and webfonts. It is not an offline bundle.

## Verification

```sh
python3 research/verify_overhaul.py
python3 research/check_pal.py
```

Pass a baseline HTML path to `verify_overhaul.py` to compare all eight historical
and geographic payloads. The weighted date tests and inline JavaScript syntax
checks require Node.js. The existing browser research scripts require Playwright;
their paths now resolve from this checkout.

See [VALIDATION.md](VALIDATION.md) for recorded checks and remaining acceptance
work. This branch has been reviewed locally; it has not been published to Pages.

## Repo layout

- `cyprus-historical-explorer.html` — the deliverable: a self-contained page with all data, styles, and logic inline.
- `research/` — the data pipeline and working notes behind the atlas: per-era research JSON, merge/reconcile/roundtrip scripts, empire-extent and neighbouring-region builders, palette and emblem checkers, i18n sources, and planning docs (`BRIEF.md`, `EXPANSION-PLAN.md`, `ROADMAP.md`).

## Status

Content fact-checked by research agents against cited sources (`research/*.json` carry `sources` per era/site). See `research/ROADMAP.md` for planned next features and `research/EXPANSION-PLAN.md` for how the current dataset was built.
