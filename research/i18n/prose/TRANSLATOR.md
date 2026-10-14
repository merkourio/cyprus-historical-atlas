# Translator instructions (one chunk, one language)

Dir: /home/merkourio/Nextcloud/Codex/Personal Brand/Cyprus-Historical-Atlas/research/i18n/prose

Input:  chunks/cNN.json — array of {"en": English string, "ctx": where it appears}
Output: out/cNN.LANG.json — ONE JSON object mapping every English string (exact, byte-identical key) to its translation.

1. Read glossary-LANG.md first and follow it (terms, names, dates, style). Also consult i18n-existing.json → LANG for the already-approved names of sites, eras, powers, neighbouring polities ("nb"/"poly"), and sub-kinds; use exactly those forms.
2. Translate every string. Register: clear, vivid, educated popular history, as in a good museum guide or atlas, not stiff and not chatty. Keep the meaning faithful: do not soften, sharpen, add or drop facts. Keep every number, measurement, and date (convert date format per glossary: "c. 4500–3800 BCE" → el "περ. 4500–3800 π.Χ.", tr "yak. MÖ 4500–3800"; keep the digits). Keep book/article titles, museum inventory numbers and Latin/scientific names as they are. Short labels (find titles, periods, museum locations like "In situ", "Cyprus Museum, Nicosia") must stay short. Repeated strings get consistent translations. Use the "ctx" field to choose the right sense, but never translate ctx itself.
3. Where you are unsure, pick the most plausible rendering and move on — no notes, no brackets, no question marks in output.
4. Write the output with a Python script (json.dump(..., ensure_ascii=False, indent=0)) to avoid escaping errors. For a big chunk you may build it in several parts (out/cNN.LANG.part1.json …) and merge them into out/cNN.LANG.json at the end, deleting the parts.
5. Validate before finishing: the output keys must equal the set of "en" values in the chunk, every value a non-empty string with no "<" characters; and print the count of strings whose digit sequences differ from the English, then fix any that are real mistakes.
6. Reply with only one line: "cNN LANG: N/N strings, M digit mismatches (explained)".
