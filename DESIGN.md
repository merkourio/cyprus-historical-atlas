---
name: Cyprus Historical Explorer
description: A cool scholarly archaeological register linking time, place and evidence.
colors:
  ground: '#edf1f2'
  surface: '#fff'
  surface-2: '#eff3f5'
  ink: '#152c3a'
  ink-2: '#3e5666'
  muted: '#536a78'
  line: '#d2dce1'
  focus: '#245de4'
  sea: '#cbdde6'
  sea-line: '#a0becb'
  space: '#d8e5eb'
  sea-deep: '#b8d0dc'
  land: '#ebeddf'
  land-line: '#617b75'
  relief: '#d3d9c3'
  copper: '#a55021'
  verdigris: '#28776b'
  slate: '#536c7e'
  gold: '#866718'
  k-town: '#a55021'
  k-village: '#72634d'
  k-sanctuary: '#927018'
  k-church: '#725891'
  k-fort: '#3b6c8f'
  k-works: '#28776b'
  ground-dark: '#14212b'
  surface-dark: '#192b37'
  surface-2-dark: '#233a48'
  ink-dark: '#edf3f5'
  ink-2-dark: '#c4d3db'
  muted-dark: '#a8bbc7'
  line-dark: '#3b5262'
  focus-dark: '#91b6ff'
  sea-dark: '#183d50'
  sea-line-dark: '#386379'
  space-dark: '#123244'
  sea-deep-dark: '#123345'
  land-dark: '#47615e'
  land-line-dark: '#a5bab0'
  relief-dark: '#546963'
  copper-dark: '#efaa77'
  verdigris-dark: '#82c6b4'
  slate-dark: '#aabcca'
  gold-dark: '#e6c474'
  k-town-dark: '#efaa77'
  k-village-dark: '#c8b59b'
  k-sanctuary-dark: '#e6c474'
  k-church-dark: '#c0a8df'
  k-fort-dark: '#9ac2e0'
  k-works-dark: '#82c6b4'
typography:
  display:
    fontFamily: Source Serif 4, Noto Serif, Georgia, serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.1
  headline:
    fontFamily: Source Serif 4, Noto Serif, Georgia, serif
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.16
    letterSpacing: -0.02em
  brand:
    fontFamily: Source Serif 4, Noto Serif, Georgia, serif
    fontSize: 23px
    fontWeight: 600
    lineHeight: 1.2
  title:
    fontFamily: Source Serif 4, Noto Serif, Georgia, serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: Source Sans 3, Arial, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  navigation:
    fontFamily: Source Sans 3, Arial, sans-serif
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.55
  label:
    fontFamily: Source Sans 3, Arial, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.55
  caption:
    fontFamily: Source Sans 3, Arial, sans-serif
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
rounded:
  compact: 2px
  control: 3px
  overlay: 4px
  sheet: 12px
spacing:
  micro: 4px
  compact: 8px
  control-gap: 12px
  body-gap: 16px
  map-inset: 20px
  gutter: 24px
  section: 28px
  reading-end: 30px
components:
  button-selected:
    backgroundColor: '{colors.ink}'
    textColor: '{colors.surface}'
    rounded: '{rounded.control}'
    padding: 9px 10px
  button-step:
    backgroundColor: '{colors.surface-2}'
    textColor: '{colors.ink}'
    rounded: '{rounded.control}'
    width: 44px
    height: 44px
  button-date:
    backgroundColor: '{colors.surface-2}'
    textColor: '{colors.ink}'
    rounded: '{rounded.control}'
    padding: 5px
  input-date:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.ink}'
    rounded: '{rounded.control}'
    padding: 7px
  navigation-tab:
    textColor: '{colors.ink}'
    typography: '{typography.navigation}'
    padding: 16px 6px 13px
  filter-row:
    textColor: '{colors.ink}'
    typography: '{typography.label}'
    padding: 7px 0
  map-container:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.ink}'
    rounded: '{rounded.overlay}'
    padding: 12px 14px
  record-status:
    backgroundColor: '{colors.surface-2}'
    textColor: '{colors.ink}'
    padding: 12px 14px
---

# Design System: Cyprus Historical Explorer

## Overview

**Creative North Star: "The Archaeological Field Register"**

The archaeological field register is the established visual world: cool writing surfaces, mineral sea, stone land and ruled evidence records. Substantive serif headings lend historical weight; compact sans-serif controls keep exploration direct. The interface is dense enough to operate an atlas while preserving a readable narrative measure.

This is a code-led system extracted from cyprus-historical-explorer.html and the accepted surface direction. There is no approved image composition or shipping raster asset. Maps, symbols and emblems are drawn with canvas/SVG; historical heraldry retains its actual tinctures.

**Key Characteristics:**
- Cool scholarly material, with explicit light and dark themes.
- Compact rectangular controls and ruled record sections.
- A linked map, continuous time dock and preserved reading context.
- Category symbols, rings and dashed states accompany color.

The finish verdict records the resolved P2 direct-date layout and P3 duplicate Life heading, with disposition `ship` for those scored fixes. It is not a new whole-surface certification. Performance timing, real-device audit and WCAG conformance remain unverified.

## Colors

The palette joins cool blue-black ink and white paper to mineral-blue sea and muted stone geography. Frontmatter values are normative; `-dark` tokens record the implemented theme overrides of the corresponding base CSS properties.

### Primary
- **Cobalt focus (`focus`)** marks keyboard outlines, links, active information tabs and selected map sites; pale cobalt is its dark-theme counterpart.

### Secondary
- **Copper, verdigris, slate and gold** provide mineral accents. Copper also marks capital rings and date errors.
- **Settlement category colors (`k-town`, `k-village`, `k-sanctuary`, `k-church`, `k-fort`, `k-works`)** identify towns, villages, sanctuaries, churches, forts and works. Keep category semantics intact across themes.

### Neutral
- **Writing white (`surface`)** holds narrative and tool surfaces; **cool secondary paper (`surface-2`)** holds status blocks and secondary controls; **ground** sits behind the shell.
- **Blue-black ink (`ink`)**, **secondary ink (`ink-2`)** and **muted slate (`muted`)** separate primary prose, supporting text and metadata. **Rule grey (`line`)** divides records and sections.
- **Mineral sea (`sea`, `sea-deep`, `sea-line`, `space`)** and **stone land (`land`, `land-line`, `relief`)** define geographic material rather than UI hierarchy.

**The Evidence Color Rule.** Settlement, era and control colors identify data; reserve the focus token for interaction and selection.

Historical era, extent and control colors remain data-defined in the artifact, including fixed control colors and a two-color diagonal hatch. They are not interchangeable theme accents. The sidecar ramps are synthesized visualization aids, not new shipping CSS palettes.

## Typography

**Display Font:** Source Serif 4, with Noto Serif, Georgia and serif fallbacks.
**Body Font:** Source Sans 3, with Arial and sans-serif fallbacks.
**Label/Mono Font:** The body family with tabular numerals; there is no separate UI monospace family. A map scale annotation additionally has Menlo/monospace fallbacks.

The pairing combines catalogue authority with clear working text. Fonts load externally from Google Fonts; the single HTML delivery is not offline.

### Hierarchy
- **Display:** the selected year; compact modes reduce it to (28px) or (26px).
- **Headline:** period and record titles, with balanced wrapping.
- **Brand:** header title; mobile uses (24px).
- **Title:** historical subsections and disclosure summaries.
- **Body:** prose with a maximum measure of (70ch).
- **Navigation, label and caption:** tabs, filters and supporting metadata. Labels use ordinary sentence case, not a universal uppercase treatment.
- **Map annotations:** serif italic geographic/political text (11–13px); settlement labels use sans serif semibold (13px) with a land-colored halo. These canvas/SVG treatments supplement the main hierarchy.

**The Two Voices Rule.** Use the serif for substantive historical headings and geographic annotation; use the sans serif for prose, labels and controls.

## Layout

The desktop shell occupies (100dvh), with an automatic header, flexible workspace and time dock. The workspace uses a reading column (380px default), a (7px) resizer and the remaining map width. The resizer exposes a (300–560px) range. Reading padding is (26px 25px 30px), and map tools commonly sit (20px) from their edges. The spacings in frontmatter are observed recurring dimensions, not a claim of a rigid arithmetic scale.

At widths up to (1100px), the reading-column CSS fallback becomes (340px), and the dock splits into control, scale-note and direct-date rows. The direct-date row remains visible: a label, year field, BCE/CE selector and Go button. At widths up to (759px), the shell flows vertically, the map leads (55dvh, bounded to 340–540px), and reading follows. The time dock stays sticky at the bottom with safe-area padding. Records become a fixed bottom sheet (55dvh), expandable to (92dvh). The desktop divider is removed.

At widths from (760px) and heights up to (500px), compact landscape adjustments tighten the header/dock, place map tools in a horizontal row, and bound the control legend. This is separate from the mobile layout. Coarse pointers set non-site buttons to a minimum (44px) height and enlarge the range thumb; site hit circles retain a radius of (22px).

## Elevation & Depth

The interface combines flat ruled reading surfaces with modest floating tool elevation. Map view selectors, legends, filters and tools use the shared theme shadow. The mobile record sheet has an upward shadow; the range thumb has a smaller shadow. Exact shadow values live in sidecar extensions.

**The Floating Tools Rule.** Keep reading surfaces flat and ruled; use elevation to distinguish controls floating over the map and the mobile record sheet.

## Shapes

Controls use compact rectangular corners; map tool containers are gently softened. Mobile record sheets have rounded top corners only. Category dots remain circular. Definition lists, finds and site rows use rules and whitespace rather than enclosing every item in a card. A capital is an outer ring, an inactive historical site is dashed and hollow, and a selected site has an enlarged focus-colored outline.

## Components

### Buttons

Language and map-view selection use an ink fill with surface-colored text. Era steps and Go use secondary paper; textual return/expand controls use focus-colored text. Hover changes text to the focus token. Disabled buttons use opacity (.45). Focus-visible controls and links receive a (2px) focus outline with a (4px) offset. Sidecar previews retain the actual state CSS; only the range thumb and site marker use special selection outlines.

### Inputs / Fields

Theme, year and BCE/CE fields use a (1px) rule-colored border and compact control corners. Date validation appears in copper beneath the fields, or above the mobile row on a surface background. The range is a weighted, data-colored track with a high-contrast rectangular thumb; its date semantics must not be inferred from equal spatial widths.

### Navigation

Overview, Places and Sources form a ruled tab row. Selection uses a (3px) cobalt bottom rule and cobalt text. Language and map view groups expose pressed states. The Places list gives access to all settlement records without requiring spatial interaction.

### Filters and Metadata

Settlement filters are text rows with category dots, not pill chips. A disabled category gains muted text and a strike-through. Record metadata is wrapping text with a semibold category label; status information uses secondary paper.

### Cards / Containers

Reading records are flat, with rules separating evidence. Floating map containers use the overlay radius and shared shadow. Source disclosures and Life on the island are ruled sections; the Life definition list has a single outer section heading.

### Map and Time Dock

The custom D3 orthographic globe combines canvas geography with SVG settlement markers. Site symbols, selected outlines, capital rings and ghost states complement the legend. The time dock links the selected year, era selector, previous/next actions, weighted scrubber, scale note and direct-date controls. Keep the open record and reading position stable during exploration.

Camera movement is one interruptible transition (650ms, D3 cubic in/out); reduced motion snaps to the new view. No intro flight is part of this world. Tab/language transitions run for (150ms), and record arrival clips into place over (180ms, ease-out), only when reduced motion is not requested.

## Do's and Don'ts

### Do:
- Do preserve the cool register palette and its paired dark-theme roles.
- Do retain category symbols, capital rings and dashed out-of-date markers alongside color.
- Do keep direct year entry available at intermediate widths and on mobile.
- Do preserve the selected record and its scroll context while time or filters change.
- Do honor visible focus, reduced motion and coarse-pointer sizing.

### Don't:
- Don't introduce artificial ageing, parchment textures or decorative photography.
- Don't turn record sections into a stack of rounded promotional cards.
- Don't recolor historical heraldry or imply new historical border claims through styling.
- Don't claim performance timing, real-device coverage or WCAG certification from the scoped finish verdict.
