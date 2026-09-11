# Research brief: expanding the Cyprus Historical Explorer

## What the project is
A single-file HTML interactive atlas of Cypriot history (a rotatable globe + weighted
timeline of 16 eras). It already carries 46 settlements/sites with 183 "finds".
The owner wants MORE: more settlements, more finds, more detail. Depth level is
"accessible overview for an educated general reader" - vivid, concrete, accurate,
never padded.

Existing data (do not duplicate, but DO add finds to these):
/home/merkourio/Documents/Cyprus history map/research/atlas-data.json
Read it first (python3 -c with json) to see the exact tone and the fields.

## The 16 eras (id, span)
aceramic -10000..-5500 | ceramic -5500..-3900 | chalco -3900..-2500 | eba -2500..-1900
lba -1900..-1050 | iron -1050..-750 | archaic -750..-480 | classical -480..-323
hellenistic -323..-58 | roman -58..330 | byzantine 330..1191 | lusignan 1191..1489
venetian 1489..1571 | ottoman 1571..1878 | british 1878..1960 | republic 1960..2026

## Existing settlement ids
aetokremnos khirokitia sotira vrysi lemba erimi marki vounous enkomi hst maa kition
salamis palaepaphos neapaphos kourion amathus idalion tamassos marion soli lapithos
kyrenia nicosia famagusta limassol hilarion buffavento kantara kolossi kykkos
troodos_churches klimonas shillourokambos tenta kissonerga souskiou kaminoudhia
alambra kalavasos_ad golgoi ayiairini chytroi vouni pyla karpasia

## Output: ONE JSON file, exactly this shape
Write it to the path given in your task, and print nothing but a short summary.

```json
{
  "new_settlements": [
    {
      "id": "lowercase_ascii_slug_unique",
      "name": "Site name as an archaeologist would write it",
      "modern": "Where it is today, e.g. 'Kouklia, Paphos district'",
      "lon": 32.581, "lat": 34.707,
      "lab": "b",
      "kind": "town | village | sanctuary | church | fort | works",
      "sub": "Optional precise label for the site panel, e.g. 'Castle', 'Copper mine', 'Cemetery', 'Abbey'",
      "ranges": [[-1650, 400]],
      "desc": "2-5 sentences. What it is, why it matters, who dug it, what changed our understanding. Plain prose, British spelling, no bullet points, no hype.",
      "finds": [
        {"n": "Find name", "p": "Period or date, e.g. 'c. 1200 BCE' or '4th century CE'",
         "t": "1-3 sentences. Concrete: material, size, what it depicts, why it matters, and any live scholarly dispute.",
         "w": "Where it is NOW: 'Cyprus Museum, Nicosia' / 'In situ, X' / 'British Museum, London' / 'Medelhavsmuseet, Stockholm'"}
      ],
      "sources": ["https://...", "https://..."]
    }
  ],
  "extra_finds": [
    {"id": "existing_settlement_id", "finds": [ {"n":"","p":"","t":"","w":""} ]}
  ],
  "era_events": [
    {"id": "era_id", "events": [[1191, "One clause, present tense, no final period"]]}
  ],
  "rulers": [
    {"power": "power_id", "rulers": [{"n":"Name","d":"1489–1491","t":"One sentence."}]}
  ],
  "notes_for_owner": ["Anything uncertain, disputed, or deliberately left out"]
}
```

## Hard rules
1. **Coordinates must be real.** Give lon/lat to 3 decimals for the actual archaeological
   site or monument, not the modern village centre when they differ. Verify against a
   source (Wikipedia geo, Pleiades, official antiquities pages). If you cannot verify a
   coordinate, say so in notes_for_owner and omit the site rather than guessing.
2. **`ranges`** are [start_year, end_year] of occupation/use, negative for BCE. Multiple
   ranges allowed for a gap in occupation. A monument still standing and in use ends 2026.
3. **`kind`** is what kind of place it is, and never changes with the year: `town` a town
   or city, `village` a village, camp or burial ground, `sanctuary` a pre-Christian
   sanctuary or temple, `church` a church or monastery, `fort` a castle or fortification,
   `works` a mine, industrial site, piece of infrastructure or landmark. Political status
   is NOT a kind: a place that was a city-kingdom carries `control: [from, to, group]`
   and the map draws the kingdom ring only within those years. Add `sub` when a precise
   word serves the reader better than the kind, e.g. "Aqueduct" or "Royal necropolis".
4. **`lab`** is label placement: "t" top, "b" bottom, "l" left, "r" right. Pick whatever
   avoids the coast/other sites; it is cosmetic.
5. **Every new settlement needs 4-8 finds.** A "find" can be an object, a building, an
   inscription, a burial, a mosaic, a shipwreck, a fresco cycle, or a stratigraphic feature.
   Prefer things a visitor could actually see, plus the one or two famous portable objects.
6. **Sources**: 2-5 real, working URLs per settlement. Prefer the Department of Antiquities,
   UNESCO, excavation project pages, academic PDFs, then Wikipedia. Never invent a URL.
7. **Flag the shaky.** If a date, attribution or museum location rests on one popular source,
   put it in notes_for_owner. Never smooth over a dispute; a one-clause "still debated" in
   the text is better than false confidence.
8. British spelling. No em-dashes anywhere in the text you write. Use "BCE"/"CE".
9. Do not pad. Eight excellent sites beat twenty thin ones. But if your period genuinely
   has twenty good sites, give twenty.
