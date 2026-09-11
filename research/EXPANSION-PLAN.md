# Expansion run: complete, 2026-09-09

Baseline before the run: 46 settlements, 183 finds.
Result: **131 settlements, 1,145 finds**, 16 "Life on the island" panels, +145 era
events, +72 rulers, 510 source URLs.

Deliverable: ../cyprus-historical-explorer.html (1.20 MB)
Artifact: https://claude.ai/code/artifact/a7126452-48ed-4aeb-a9cc-303251acb4b9

## Pipeline, as run
1. Ten research agents wrote 01-*.json .. 10-*.json (kept in this folder).
2. `python3 reconcile.py .` folded 4 settlements that two agents had each proposed
   (kafizin, skouriotissa, stavrovouni, peristerona).
3. `python3 merge.py baseline-46.json <out>.json .` validated and merged.
   85 new settlements, every record accepted, no rejections.
4. `python3 roundtrip.py load <out>.json` wrote the data back into the HTML.

## Verification, all passing
- node --check on the extracted inline JS: clean, 0 console or page errors in a
  headless run across nine eras.
- All 131 coordinates fall inside the atlas's own coastline polygon. One
  pre-existing error found and fixed: `maa` sat 1.3 km out to sea, corrected to
  32.3621, 34.8528 from the OSM historic=archaeological_site node.
- 510 source URLs resolve. The only non-200s are the known publisher bot-blocks
  (academia.edu, ResearchGate, Taylor and Francis), which work in a browser.
- Prose lint over 5,272 text fields: no em-dashes, no double spaces, no BC/AD,
  no American spellings, no stray HTML. En dashes appear only in date ranges.
- Declustering and the "Standing at <year>" site list, decided in the previous
  run, are in place and were measured: at the island preset 43 dots is the worst
  case (Republic), of which 14 labels go quiet and return on hover or selection.

## Content edits made during the merge
- Dropped `Bellapais Abbey` from kyrenia's finds; superseded by the new
  7-find `bellapais` record.
- Dropped `Aphendrika, ancient Urania` from karpasia's finds; superseded by the
  new 6-find `aphendrika` record.
- Ayia Irini's figurine count harmonised to "about 2,000" and attributed to the
  Swedish excavators, per the research note that flagged it as single-sourced.
- Lemba's infant jar burials were reviewed and kept: the text already frames the
  rite as shared with Kissonerga and typical of the Erimi culture.

## Left for the owner to rule on
- Duplication that was deliberately NOT pruned, because the old entry still
  carries its own point:
  - salamis / "The Royal Tombs" alongside the new `salamis_tombs` record.
  - kourion / "The Kourion Treasure" alongside `kaloriziki`'s sceptre and Tomb 40.
  - troodos_churches is a group record whose nine one-line finds include four
    churches that now have their own dots (asinou, araka, ayios_nikolaos_stegis,
    lampadistis). Kept whole so the UNESCO group reads as a group.
- `kition` and `lapithos` are typed `kingdom` with ranges running to 2026, so a
  copper "City-kingdom" dot shows at 2000 CE. Pre-existing, defensible as
  continuous occupation, but it may read oddly.
- Coordinates for roughly 11 of agent 02's sites are village-derived and accurate
  to about a kilometre; the per-site provenance is in each file's
  notes_for_owner. All are on land and none collide after declustering.

## Empire outlines made year-accurate, 2026-09-09
Each empire used to carry ONE outline stretched across its whole window, so Rome's
117 CE maximum was drawn from 58 BCE and Britain's 1914 extent covered 1878 to 1960.
`EXTENTS` now holds dated snapshots per empire (`snaps: [{y, coords}]`, 38 in total,
from aourednik/historical-basemaps `world_<year>.geojson`) and `activeExtents(year)`
draws the one nearest the year on screen. The legend and the panel name the outline's
own date, so what you see is always labelled with the year it depicts.

Rebuild with `build_extents.py <out.json>` (needs shapely; downloads are cached in a
scratchpad `hb/` folder), then check with `extcheck.py`.

Rules that matter:
- A snapshot is only used for a window it is within 25 years of. This drops Rome's
  100 BCE outline, which predates the province and excluded Cyprus, and Venice's
  1600 outline, which postdates the loss of the island.
- `island: true` marks the ten empires that actually held Cyprus; the source geojson
  omits the island from many snapshots, so the ring is added back for those. Assyria
  and Saite Egypt are deliberately left without it: the Cypriot kings paid them
  tribute rather than being ruled, and the outlines say so.
- `rome.to` and `byz1.to` were pulled back a year so successive entries for the same
  lineage no longer both draw on the shared boundary year.
- Verified with 21 point-in-polygon assertions against known history (Egypt not Roman
  in 100 BCE, Ravenna Byzantine in 600, Athens not Ottoman in 1880, Delhi not British
  in 1960) and by checking that the ruling power's outline contains Cyprus in every
  sampled year except the two tribute cases.

### Border artefacts fixed, same day
The first version of the dated outlines had three faults, all visible once you zoomed
past the region view:
1. A single global simplification tolerance flattened every polygon equally, so the
   small islands the source draws separately, Cyprus and Crete among them, collapsed
   into triangles. The tolerance is now scaled per polygon, `min(tol, sqrt(area)/9)`,
   so an island keeps its shape while a continent loses its wiggles.
2. The accurate island ring was CONCATENATED onto the source geometry rather than
   unioned, so the island polygon and the source's own coarse island triangle overlapped
   inside one path. Overlapping parts of a path cancel when filled and leave an interior
   edge when stroked: that was the straight red chord across Cyprus and the half-shaded
   island. The ring now replaces the source's version and everything is passed through
   `unary_union` at build time, so no snapshot has any self-overlap (asserted).
3. The outlines and the atlas's own coastline are different datasets, so an empire's
   edge could sit inland and leave a bare strip of land along the coast. Outlines are
   dilated by 0.09 degrees and eroded slightly, which closes most of that gap; the
   shading is composited onto land, so the overspill into the sea is clipped away.

Even so, a crisp line drawn close up turns a rough snapshot into a precise claim about
where a coast ran, so the extent STROKE now fades out between scale 2200 and 5200,
well before the shading does. Past that zoom the land-clipped fill carries the extent
on its own and cannot disagree with the coastline.

Point budget is 560 per snapshot, 14,234 points over 38 snapshots, 196 KB of the file.
Frame time is unchanged at 3 to 5 ms.

## Code and weight audit, 2026-09-09
File went from 1401 KB to 1083 KB, 23% smaller, with the island view pixel-identical.

Where the weight was, before: LAND_TOPO 533 KB, SETTLEMENTS 472 KB, EXTENTS 196 KB,
ERAS 93 KB, POWERS 31 KB, CSS 19 KB, everything else under 10 KB.

**The coastline is now graded by distance from Cyprus** (`gradeland.py`). Every view in
this atlas is centred on the island, so full Natural Earth 50m detail is kept within
1200 km and simplified progressively beyond it (2 km, 6 km, 14 km bands). 60,635 points
become 22,793, saving 318 KB. Arc endpoints are preserved so the TopoJSON arc indices
and ring closure stay valid.

The level-of-detail fractions were retuned from 0.06/0.30 to **0.16/0.55**. These are
not arbitrary: at region zoom only two polygons survive culling and one is Afro-Eurasia,
which is never culled, so its share of these budgets is what sets the frame time. 0.55
measured both the fastest and the closest to the original of everything tried; 0.80 was
slower AND less faithful, and gentler grading bands (1.5/4/8 and 1/3/6 km) were bigger
AND slower, so the aggressive grading is Pareto-optimal.

Measured against the pre-audit file, interleaved in one browser to cancel drift:
- DOMContentLoaded 383 ms -> 293 ms (23% faster)
- world 5.72 -> 5.85 ms/frame, region 4.20 -> 4.18, island 3.67 -> 4.02 (+10%)
- pixel diff: island 0.00%, close 0.26%, world 0.44%, region 0.38%, all confined to
  distant coastlines (Red Sea, Gulf, Black Sea), nothing near Cyprus

The +10% at island zoom is the one cost. 4 ms is far inside budget and it buys 318 KB.

**Dead code removed**
- `const LAND = topojson.feature(...)` was never read, and it built a GeoJSON of every
  coastline on earth at load. Removing it is most of the startup win.
- `const KINGDOM_ERA=[-900,-312]` never read.
- `.ctrl i.dash` had no code path that emits it.
- `emblem(p, y)` still branched on `iconAfter`, which no power carries any more; it is
  now `emblem(p)`. If an era-dependent emblem is ever wanted, that branch comes back.
- The duplicate `.now` rule was merged.

**Checked and found already clean:** no duplicate source URLs or find names inside any
settlement or era, no stray whitespace in any prose field, every data field on
SETTLEMENTS / ERAS / POWERS / EXTENTS is read somewhere, no unused CSS class selectors
remain, no console/debug leftovers, and no stale selectors from the kind and emblem
renames earlier in the day.

**Harness fix:** `shot.py` now awaits `document.fonts.ready`. Without it, label
placement depends on whether the webfont had loaded when `ctx.measureText` ran, which
produced a false regression signal during this audit.

## Neighbouring polities at region zoom, 2026-09-09
Pull back from the island and the countries around Cyprus now appear, for the date on
the timeline: thin boundaries with a very faint fill, composited onto land like the
empire shading so nothing spills into the sea. `REGIONS` holds 36 dated snapshots,
179 polities, clipped to a box from 19E to 56E and 22N to 44N. Build with
`build_regions.py <out.json>`; the result is also kept as `region-polities.json`.

Selection rules, in order:
- Whichever empire holds Cyprus that year is left out, because EXTENTS already draws it.
  This is done by GEOMETRY, not by name: the source spells the same polity several ways
  ("Mamluk" against "Mamluke"), and a name test silently double-draws it.
- A polity is kept if the era already names it in NEIGHBOURS, or if it comes within
  1100 km of the island. Distance alone cannot separate Persia, which matters, from the
  Khazars, which do not; the atlas's own curated labels are the relevance signal.
- Culture areas, nomadic ranges and the source's placeholders ("minor states", "?") are
  filtered out. Nearest twelve per snapshot.
- `n` is carried ONLY for polities the era does not already name, so nothing is labelled
  twice, and a source name is dropped rather than allowed to overprint an era label.

**It starts at the Classical era**, `REGION_FROM = -480`. The source's earlier files are
not dependable: they still show the Hittites in 700 BCE and the united monarchy of David
in 600 BCE. The Archaic era and the Bronze Age keep their labels and no shapes. They
could be added with hand-checking if the loose attributions are pruned first.

Note the source also shows Crete as Ottoman in 1600, when Venice held it until 1669.
1600, 1650 and 1700 draw no neighbours at all, which is right: the eastern Mediterranean
really was entirely Ottoman, with only Safavid Persia beyond the box.

Cost: +115 KB (file 1083 -> 1201 KB) and +0.3 to +3.0 ms per frame at region zoom, which
keeps every era in the same 4 to 5 ms band. Zero at island and world zoom, where the
layer does not draw. Opacity ramps on `min(ramp(s,600,1500), 1-ramp(s,5000,sitesAt()))`,
so shapes and the era's labels arrive together.

## Powers made visually distinct, 2026-09-09
The empire fills are painted at low alpha over land, which squeezes every colour toward
the land colour: measured as actually painted, nearly every pair of empires sat below
dE 12, and two pairs that appear on screen TOGETHER were indistinguishable. The Umayyad
and Abbasid Caliphates were literally the same hex, and Alexander against the Ptolemies
was dE 2.1. The era bar was no better: aceramic against iron was dE 6.0.

Three changes, in order of how much they did:
1. **Stronger fills.** overlord .34 -> .44, co-power .28 -> .52, suzerain .20 -> .28.
   This mattered most: at the old alpha, an optimiser searching the whole colour space
   could only reach a weighted minimum of 8.5, so no palette could have fixed it.
2. **A second channel.** Co-powers are now hatched as well as tinted (`powerHatch`),
   which echoes the shared-rule hatch already used on the island, separates the two
   caliphates from the Byzantine overlord they sit beside, and survives colour blindness.
3. **A repaired palette**, verified rather than eyeballed. `check_pal.py` measures every
   pair as composited over both light and dark land and reports anything under its
   threshold: 15 for empires that share the screen, 11 for consecutive ones, 8 otherwise;
   20 for adjacent era bands, 12 for the rest. Both palettes now report zero failures.

The palette was hand-picked and then only nudged: a first optimiser run produced a
technically superior palette that was also hot pink and cyan, throwing away Rome-red and
Byzantium-purple. `relax.py` instead treats distinctness as a constraint to satisfy and
minimises drift from the intended colours. Total drift is 33.5 dE across 14 empires, and
only two colours moved noticeably: the Ptolemies toward cyan to clear the Umayyad green,
and the Mamluks lighter to clear the Abbasid bronze. Ten of fourteen moved by under 1.

The three Byzantine windows deliberately share one colour: one polity, three entries.

Rebuild or re-check with `check_pal.py <era.json> <extent.json> '<alphas>'`. Cost: the
hatch adds at most 0.31 ms per frame.

### Neighbour boundaries stopped disagreeing with the coast, 2026-09-09
Reported as "the borders look strange, as if the overlay and the map don't match".

Measured rather than guessed. The empire shading turned out to be innocent: masking the
pixels it paints against the land layer showed 98.6% on solid land and the rest a one
pixel antialiased rim. The neighbour polities were the problem: **38.2% of their boundary
vertices were not on land at all**. They are simplified at 0.09 degrees, roughly 10 km,
while the coastline they sit on is Natural Earth 50m, so along a ragged coast like Lycia
their boundary wandered out to sea and back. The stroke is clipped to land, so what
reached the screen was a line running a few kilometres off the shore, cutting across
peninsulas and stopping in open water. That is the "out of register" look.

The fix is not to simplify less, which would cost size, but to stop drawing the part of
the boundary that was never informative: where a polity meets the sea, the COASTLINE is
the border, and a second line beside it says nothing. `build_regions.py` now loads the
atlas's own LAND_TOPO, and marks each boundary segment as an inland frontier only if all
of three sample points along it fall on land. 63.3% of segments qualify; the other 36.7%
are no longer stroked. The fills are untouched, so every polity still reads as an area.

The mask is a bit-string per ring, +9 KB. It is indexed against the RAW rings in `c`,
not against `geom`, because the geometry pass reverses a ring's winding when it is
inside out and that would silently shift every index by an unknown amount.

Off-land painting by the layer is now 0.1 to 0.2%, all of it the antialiased coast rim.
Frame time is unchanged, between -0.08 and +0.29 ms.

## Greek and Turkish, 2026-09-09
The atlas holds 6,159 translatable strings and 505,000 characters, and 97% of that is
scholarly prose: 131 site descriptions, 4,580 find fields, 259 era events, 426 ruler
entries. Translating all of it into two languages means about a million characters of
specialist archaeological text that could not be reviewed, in a project whose accuracy
six research agents established. So the work was staged, with the owner's agreement.

**Done now: the whole shell, 852 strings per language.** Interface, hints, legends,
buttons, panel and drawer headings, status lines, the count readout, 16 era names and
short forms, 16 powers with origin and seat, 14 empire names, 5 geographic labels,
86 neighbour labels, 48 polity names, 46 site-type labels, and all 131 site names with
their modern locations. Sources in `research/i18n/`.

**Still English:** site descriptions, finds, era events, life panels, ruler notes. Every
lookup falls back to English, so a missing translation degrades to the original rather
than to nothing, and the prose can be filled in incrementally without touching the code.
A note in the panel says so plainly, in the reader's own language.

Place names use each language's own form, as chosen: Λευκωσία / Lefkoşa, Κερύνεια /
Girne, Αμμόχωστος / Gazimağusa, Μόρφου / Güzelyurt, Πενταδάκτυλος / Beşparmak.

Things worth knowing:
- **Fraunces and IBM Plex Mono ship no Greek subset**, checked against the Google Fonts
  API rather than assumed. Noto Serif and Noto Sans Mono are in the stacks behind them;
  because the browser fetches only the subsets it needs, English and Turkish readers
  download nothing extra.
- Dates are localised, not just translated: `π.Χ.` follows the number in Greek while
  `MÖ` precedes it in Turkish, and the locale sets the digit grouping. Only years of
  five figures and up are grouped, so a CE year reads 1960 rather than 1,960.
- The site list sorts with the reader's own collation, not English.
- Language lives in localStorage under `cy-lang` and in the URL as `#lang=`, and a first
  visit honours `navigator.language`.

## Filtering by kind of site, 2026-09-09
The legend now doubles as the filter, because that is where a reader already goes to
find out what the colours mean; no new panel, no new vocabulary to learn.

- Click a kind to hide it. Click again to bring it back.
- Shift-click (or alt-click) isolates one kind; shift-click the same one again restores
  the rest. This is the move that makes the atlas answer questions like "where are the
  monasteries" or "where are the castles".
- Clicking the last visible kind restores everything instead of emptying the map, which
  would otherwise look like a bug.
- A "Show all kinds" reset appears only while something is hidden, and the site count
  says "filtered" so a short list is never mysterious.

The filter runs through one predicate, `shown(s)`, applied in three places: the dots on
the map, the "Standing at" list in the panel, and `activeCount`. Hiding a kind before
positions are computed means it also frees its declustering and label slot, so the
remaining sites spread out rather than staying squeezed around gaps.

Deliberately session-only, not persisted: a filter that survived a reload would leave
sites missing with no visible cause. If a site is open in the drawer when its kind is
switched off, the drawer closes with it.

The legend entries are real buttons with `aria-pressed`, so the filter works from the
keyboard, and its labels and tooltip are translated into Greek and Turkish.

## Population per era, 2026-09-09
Each era now carries a population figure as the first row of "Life on the island", with
the basis stated beside it in smaller type. **Four eras have a figure. Twelve say
"Unknown" outright**, which was the point: the gap is the finding, not an omission.

Where the numbers come from, all from sources the project already holds:
- **Venetian, about 106,000 to 200,000.** A Cypriot deputation told Venice in 1490 the
  island held some 106,000 souls; a Venetian survey later counted 147,701; 197,000 was
  claimed for the eve of the conquest. Hill, *A History of Cyprus* vol. 3.
- **Ottoman, about 50,000 to 185,000.** A sharp fall after 1571, then slow recovery;
  18th and early 19th century travellers and Ottoman counts sit well under 100,000.
  *Excerpta Cypria*.
- **British, 186,173 rising to 573,566.** The first reliable series, censuses 1881-1960.
- **Republic, about 1.2 million.** 573,566 at independence; the 2021 census counted
  923,272 in the government-controlled area, so the whole island is roughly 1.2 million.
  That split is stated rather than papered over.

For the twelve unknown eras the note says why, and gives what the archaeology can say
instead: Khirokitia a few hundred people, Marki-Alonia about four hundred, Kissonerga
twelve hectares. The Roman note records that Dio Cassius put the dead of the revolt of
115-117 at 240,000 and that modern historians treat the figure as far too high, which is
more useful than inventing a total.

Deliberately not done: a made-up number for antiquity. Estimates for Roman or Bronze Age
Cyprus vary by whole multiples between scholars, and this atlas has been careful
elsewhere about not smoothing over what is not known.

All 32 strings are translated into Greek and Turkish, with the digit grouping each
language uses (106.000 in both, 1,2 εκατομμύρια / 1,2 milyon).

## Recommended reading per era, 2026-09-09
Each era now carries a "Recommended reading" list in the panel: **91 entries, 79 distinct
works**, four to seven per era. Each is tagged Book, Academic, Article, Essay, Primary
source or Fiction, and carries a half-sentence on what it is and why it belongs here.
Data in `ERAS[].reading` and `recommended-reading.json`.

**Every entry was verified against a bibliographic database before it went in**
(`verify_reading.py`, results in `reading-verify.json`): Open Library for books, Crossref
for articles, Wikipedia for the ancient and medieval texts. 82 works were drafted; 79
verified. **Three were dropped rather than kept on trust**: Młynarczyk's Nea Paphos
monograph, Stewart's *Domes of Heaven*, and Yaşın's *Don't Go Back to Kyrenia*. All three
may well exist, but a reading list in an atlas that has been fact-checked should not carry
a title that two databases cannot find.

Fiction where the island has any: Boccaccio's Decameron I.9 (Lusignan), *Othello*
(Venetian), Montis's *Closed Doors* answering Durrell and Seferis's *Logbook III*
(British), Shafak's *The Island of Missing Trees* and Hislop's *The Sunrise* (Republic).
None for antiquity or prehistory, so none was invented.

Titles stay as published; the heading and the six kind tags are translated. The notes are
English for now, like the rest of the long-form prose.

## 2026-09-10 — ROADMAP.md expanded with implementation detail

Rewrote `ROADMAP.md` (16.4 KB → 29.8 KB, 690 lines) so each plan carries the code to
write, not a description of it: markup with its anchor string, full function bodies, CSS
following the existing custom-property conventions, i18n keys in all three languages, and
the verification steps.

Verified against the deliverable before writing: every identifier used in a snippet
exists (63 checked, 0 missing), every quoted anchor string is present, the cited line
numbers (735, 751, 1268) are correct, and every CSS custom property referenced is
defined. Corrected while checking:
- site ids — `soloi`→`soli`, `hala-sultan-tekke`→`hst`
- `CY_CENTRE`→`CYPRUS_CENTER`; `KINDS` does not exist (use `Object.keys(kindOn)`)
- route filter example used kinds that do not exist; the six real ones are
  town/village/sanctuary/church/fort/works
- `data-i18n-ph` and `data-i18n-title` are both new hooks — the doc now says so instead
  of implying they exist
- 2b needs no click handler: line 1268 already delegates `[data-site]` on the panel
- pointed the 23-single-era snippet and `museums.py` at a `roundtrip.py` dump rather
  than at files that do not contain what was claimed

Recorded the counting rule behind the quoted figures: 23 single-era / 46 spanning five or
more eras use inclusive overlap (`a<=e.end && b>=e.start`); a half-open rule gives 40 and
45. Anyone quoting the number should quote the rule with it.

No change to `cyprus-historical-explorer.html`.
