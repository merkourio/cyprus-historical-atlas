# Visual overhaul verification

13 October 2026. Baseline: `6680e8cc614ab586c9831f97972c2713df5963e3`.

## Completed checks

- Eight historical/geographic payloads compare equal to the baseline: POWERS,
  ERAS, SETTLEMENTS, NEIGHBOURS, EXTENTS, REGIONS, LAND_TOPO and CYPRUS_RING.
- The atlas retains 16 eras, 131 settlements and 1,145 finds.
- Weighted date mapping passes round-trip, clamping and era-boundary checks.
  Display/interaction skips year zero while preserving the evidence model.
- Both inline scripts pass JavaScript syntax checking. Research helper files
  pass Python compilation; their project paths are portable.
- Composited political palette and era palette checks report zero pairs below
  the existing thresholds, using the land colours actually shipped in both themes.
- Browser inspection covered widths 320, 390, 760, 900, 1280 and 1440 in English,
  Greek and Turkish, in light and dark: 36 combinations. No page overflow or
  overlapping timeline tick labels was observed in the tested overview state.
- Every era could be selected. An open reading section stayed open through a
  date change; exact date entry and a keyboard step crossed from 1 BCE to 1 CE.
- A Greek deep link restored date, region preset, selected Salamis and filters.
  Unknown date/site/view/filter parameters were handled without a runtime error.
- The mobile expanded record exposed a labelled modal state and a visible close
  control. The implementation includes focus containment, background inertness
  and focus restoration; complete assistive-technology testing remains open.
- After the independent review, exact-date entry was restored at intermediate
  widths. Nine targeted combinations (760×900, 900×900 and 844×390 in three
  languages) confirmed visible date controls and no page overflow. The duplicate
  inner Life on the island heading was removed.
- No browser runtime errors were recorded in the interaction sweep.
- Explicit filter isolation showed the expected works record (Skouriotissa);
  restoring all types worked. Sources exposed 11 links and opened reading/source
  sections in the tested Hellenistic state.

## Design review

Impeccable's independent finish review assessed the screenshots, implementation
and direction brief. Its initial verdict requested the intermediate-width date
entry fix and noted the repeated heading. A follow-up verdict scored both
resolved, with no regression observed in those scored areas. The follow-up ship
verdict applies to that fix list; it is not a new whole-surface certification.

The mechanical detector ran once. Its only advisory was a repeating-gradient
stripe. This is the existing shared-rule hatch in the political legend, carrying
historical meaning rather than decorating a surface.

Review evidence is retained locally under `.impeccable/review/`: desktop light and
dark captures, phone overview and expanded record, short landscape, responsive
and interaction JSON, initial review and fix verdict. Screenshots are development
evidence and are not part of the single-file deliverable. No raster artwork ships.

## Delivery and limitations

The HTML is 1,366,640 bytes (394,283 bytes with gzip level 9), below the
1,500,000-byte budget, and retains its external CDN
dependencies. The overhaul was prepared on `codex/atlas-visual-overhaul`; the owner authorised
publication on 14 October 2026. GitHub Pages publishes `main`, repository root. The historical datasets and the original local atlas remain intact.

The original browser research scripts were made portable but were not executed
in this session. Geography was validated through unchanged-payload comparisons;
the new UI was inspected through the controlled browser instead.

Still open before a broad public release:

- Interleaved frame/render timings on a stated desktop and mobile reference device.
- Physical-device touch, zoom, safe-area and software-keyboard testing.
- Full keyboard/screen-reader and 200% text-zoom audits; WCAG 2.2 AA is a target,
  not a certification claim.
- Reduced-motion, blocked-CDN/font recovery and direct-file behaviour on a browser
  matrix. These paths are implemented/source-inspected rather than exhaustively
  exercised here.
- Reader task testing and final owner review of the visual direction.

No external quality-board image or raster mockup was used as a fidelity authority;
the code-led direction brief and the recorded review define this pass's scope.
