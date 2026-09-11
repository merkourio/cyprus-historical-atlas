# Cyprus Historical Explorer — execution plans

Written 2026-09-10. Features discussed but not built. Each plan is meant to be picked up
cold: what to build, **the code to write**, where it goes, the traps, and how to prove it.

**Deliverable** `../cyprus-historical-explorer.html` (single file, ~1,304 KB)
**Artifact** https://claude.ai/code/artifact/a7126452-48ed-4aeb-a9cc-303251acb4b9
**Project history** `EXPANSION-PLAN.md` in this folder.

Line numbers are from 2026-09-10 and will drift; the quoted anchor strings will not, so
search for those instead.

---

## 0. Read this first

### Editing the data
`POWERS`, `ERAS`, `SETTLEMENTS`, `NEIGHBOURS` only:

    python3 roundtrip.py dump out.json    # edit out.json, then
    python3 roundtrip.py load out.json

Generic JSON, so **new fields need no script change**. `EXTENTS` and `REGIONS` are not in
the set — they come from `build_extents.py` / `build_regions.py` and are injected by hand.

### Traps that have already cost time
- **Silent clipping.** `.app` is `overflow:hidden`. A new flex/grid row without
  `min-width:0` can force the app wider than the window; the symptom is sliced-off
  content, never a scrollbar. This cost the era bar 1,079 px once.
- **Canvas layers.** Anything on the globe that must not spill into the sea is drawn on
  the offscreen `landLayer` with `globalCompositeOperation="source-atop"`, then
  composited once. See the extents/region code in `draw()`.
- **Language.** Every visible string goes through `UI(key, en)` (interface) or
  `TS(ns, en)` / `T(ns, key, field)` (names), added to **both** `I18N.el` and `I18N.tr`.
  Missing keys fall back to English by design. `s.label` and the cached width `s._w` are
  language-specific and reset in `applyLanguage()` — any new cached measurement must be.
- **Dates.** Always `fmtYear` / `fmtRange`. Greek puts π.Χ. after the number, Turkish
  puts MÖ before it.
- **Sorting.** `localeCompare(x, lang)`, never `"en"`.
- **Filtering.** `shown(s)` is applied *before* dot positions are computed in `draw()`,
  so a hidden kind frees its declustering and label slot too.
- **Colour.** Compare composited over land, not raw hex (`check_pal.py`). Never let an
  optimiser pick a palette unsupervised — it produced hot-pink Venice and dark-green Rome.
- **Speed.** Frame times must be compared interleaved in ONE browser session.

### Harness
    python3 shot.py      # all eras, dot/label counts, JS errors (awaits webfonts)
    python3 geocheck.py  # 131 coordinates on the island polygon
    python3 extcheck.py  # empire outlines contain Cyprus when they should
    python3 check_pal.py # colour separation, composited
Standing sweep: **3 languages × 6 widths = 18**, asserting no tick overlap, nothing
clipped, no page errors. Nothing ships below 18/18.

### Where the counts come from
131 settlements, 1,145 finds, 23 sites in a single era, 46 spanning five or more, 9 with
a gap in occupation. The era counts use **inclusive** overlap (`a<=e.end && b>=e.start`),
so a site ending exactly on an era boundary belongs to both. A half-open rule gives 40
and 45 instead — state the rule whenever quoting the number.

### Budget
~1,304 KB now. **Ceiling 1,500 KB**; past that re-run the coastline audit in
`EXPANSION-PLAN.md` rather than accept it.

---

## Plan 1 — Search

23 of 131 sites appear in only one of the 16 eras; the panel list shows only what stands
at the current date, so those 23 are unreachable unless you already know when they
existed. The 1,145 finds are reachable only by opening the right site. The one dead end.

### 1.1 Markup — after the `langsel` div in `<header class="head">`

```html
<div class="search" id="search">
  <input id="searchInput" type="search" autocomplete="off" spellcheck="false"
         role="combobox" aria-expanded="false" aria-controls="searchResults"
         aria-autocomplete="list" data-i18n-ph="search.placeholder"
         placeholder="Search sites, finds, rulers">
  <div class="results" id="searchResults" role="listbox" hidden></div>
</div>
```

`data-i18n-ph` is a new hook; extend `applyLanguage()`:

```js
document.querySelectorAll("[data-i18n-ph]").forEach(el=>{
  if(!el.dataset.enPh) el.dataset.enPh=el.placeholder;
  el.placeholder=UI(el.dataset.i18nPh,el.dataset.enPh);
});
```

### 1.2 CSS — beside `.langsel`

```css
.search{position:relative;flex:0 1 260px;min-width:150px}
.search input{width:100%;font-family:var(--font-body);font-size:13px;color:var(--ink);
  background:var(--surface-2);border:1px solid transparent;border-radius:3px;padding:6px 9px}
.search input:focus{outline:none;border-color:var(--copper);background:var(--surface)}
.results{position:absolute;top:calc(100% + 4px);left:0;right:0;z-index:20;max-height:min(60vh,420px);
  overflow-y:auto;background:var(--surface);border:1px solid var(--line);border-radius:4px;
  box-shadow:var(--shadow);padding:4px}
.results .grp{font-family:var(--font-mono);font-size:10px;letter-spacing:.07em;text-transform:uppercase;
  color:var(--muted);padding:6px 8px 2px}
.results button{display:block;width:100%;text-align:left;padding:5px 8px;border-radius:2px;font-size:13px;color:var(--ink)}
.results button .sub{display:block;font-size:11.5px;color:var(--muted)}
.results button:hover,.results button[aria-selected="true"]{background:var(--surface-2)}
.results .none{padding:8px;font-size:12.5px;color:var(--muted)}
@media (max-width:900px){ .search{order:3;flex:1 1 100%} }
```

`min-width` on `.search` is not optional — see the clipping trap.

### 1.3 Index — rebuilt on language change

```js
/* Flat search index. Rebuilt per language because names are translated. */
let SEARCH=[];
const fold=s=>s.normalize("NFD").replace(/\p{Diacritic}/gu,"").toLowerCase();
function buildSearch(){
  const mid=r=>Math.round((r[0]+r[1])/2);
  SEARCH=[];
  SETTLEMENTS.forEach(s=>{
    const nm=siteField(s,"name"), md=siteField(s,"modern");
    SEARCH.push({kind:"site",label:nm,sub:md,year:mid(s.ranges[0]),siteId:s.id});
    s.finds.forEach(f=>SEARCH.push({kind:"find",label:f.n,sub:nm,year:mid(s.ranges[0]),siteId:s.id}));
  });
  ERAS.forEach(e=>{
    SEARCH.push({kind:"era",label:eraName(e),sub:fmtRange(e.start,e.end),year:Math.round((e.start+e.end)/2)});
    (e.reading||[]).forEach(r=>SEARCH.push({kind:"reading",label:r.t,sub:r.a,year:Math.round((e.start+e.end)/2)}));
  });
  ERAS.forEach(e=>{
    const p=POWERS[e.power];
    (p.rulers||[]).forEach(r=>SEARCH.push({kind:"ruler",label:r.n,sub:r.d,year:Math.round((e.start+e.end)/2)}));
  });
  SEARCH.forEach(x=>{ x._l=fold(x.label); x._s=fold(x.sub||""); });
}
```

Call `buildSearch()` at the end of `applyLanguage()`. Duplicate rulers across eras are
harmless; dedupe by `kind|label` if it looks untidy.

### 1.4 Match and rank

```js
const KIND_RANK={site:0,find:1,ruler:2,era:3,reading:4};
function searchQuery(q){
  const f=fold(q.trim());
  if(f.length<2) return [];
  const out=[];
  for(const x of SEARCH){
    let score=null;
    if(x._l.startsWith(f)) score=0;
    else if(x._l.includes(f)) score=1;
    else if(x._s.includes(f)) score=2;
    if(score!==null) out.push({x,score});
  }
  out.sort((a,b)=>a.score-b.score
    || KIND_RANK[a.x.kind]-KIND_RANK[b.x.kind]
    || a.x.label.length-b.x.label.length);
  return out.slice(0,12).map(o=>o.x);
}
```

Linear over ~6,000 entries per keystroke measures well under a frame; do not add an
index until proven necessary.

### 1.5 Render and activate

```js
const searchInput=$("#searchInput"), searchResults=$("#searchResults");
let searchHits=[], searchCursor=-1;
const SEARCH_GROUP={site:"search.sites",find:"search.finds",ruler:"search.rulers",
                    era:"search.eras",reading:"search.reading"};
function renderSearch(){
  if(!searchHits.length){
    searchResults.innerHTML=searchInput.value.trim().length>=2
      ? `<div class="none">${UI("search.none","Nothing found")}</div>` : "";
    searchResults.hidden=!searchInput.value.trim();
    searchInput.setAttribute("aria-expanded",String(!searchResults.hidden));
    return;
  }
  let html="",last=null;
  searchHits.forEach((x,i)=>{
    if(x.kind!==last){ last=x.kind; html+=`<div class="grp">${UI(SEARCH_GROUP[x.kind],x.kind)}</div>`; }
    html+=`<button type="button" role="option" id="sr${i}" data-i="${i}"
      aria-selected="${i===searchCursor}">${x.label}${x.sub?`<span class="sub">${x.sub}</span>`:""}</button>`;
  });
  searchResults.innerHTML=html;
  searchResults.hidden=false;
  searchInput.setAttribute("aria-expanded","true");
  if(searchCursor>=0) searchInput.setAttribute("aria-activedescendant","sr"+searchCursor);
}
function pickSearch(x){
  if(!x) return;
  /* A result whose kind is filtered out would open onto an invisible dot. */
  if(x.siteId){
    const s=SETTLEMENTS.find(t=>t.id===x.siteId);
    if(s && !kindOn[s.kind]){ kindOn[s.kind]=true; applyFilter(); }
  }
  setYear(x.year);
  if(x.siteId){
    const s=SETTLEMENTS.find(t=>t.id===x.siteId);
    openSite(x.siteId);
    presetView=null;
    flyTo(Math.max(view.scale,PRESET.island()), [s.lon,s.lat], reduceMotion?0:900);
  }
  closeSearch();
}
function closeSearch(){
  searchResults.hidden=true; searchHits=[]; searchCursor=-1;
  searchInput.value=""; searchInput.setAttribute("aria-expanded","false");
  searchInput.removeAttribute("aria-activedescendant");
}
searchInput.addEventListener("input",()=>{ searchHits=searchQuery(searchInput.value); searchCursor=searchHits.length?0:-1; renderSearch(); });
searchInput.addEventListener("keydown",ev=>{
  if(ev.key==="ArrowDown"||ev.key==="ArrowUp"){
    ev.preventDefault(); if(!searchHits.length) return;
    searchCursor=(searchCursor+(ev.key==="ArrowDown"?1:-1)+searchHits.length)%searchHits.length;
    renderSearch();
    searchResults.querySelector('[aria-selected="true"]')?.scrollIntoView({block:"nearest"});
  } else if(ev.key==="Enter"){ ev.preventDefault(); pickSearch(searchHits[searchCursor]); }
  else if(ev.key==="Escape"){ ev.preventDefault(); closeSearch(); searchInput.blur(); }
});
searchResults.addEventListener("click",ev=>{
  const b=ev.target.closest("[data-i]"); if(b) pickSearch(searchHits[+b.dataset.i]);
});
document.addEventListener("click",ev=>{ if(!$("#search").contains(ev.target)) searchResults.hidden=true; });
document.addEventListener("keydown",ev=>{
  if(ev.key==="/"&&!/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)){ ev.preventDefault(); searchInput.focus(); }
});
```

**Trap.** The existing global `Escape` handler calls `closeSite()`. The search handler
above runs on the input and calls `stopPropagation` implicitly by preventing default —
if the drawer still closes behind the search, add `ev.stopPropagation()`.

### 1.6 i18n
```json
"search.placeholder":"Search sites, finds, rulers", "search.none":"Nothing found",
"search.sites":"Places", "search.finds":"Finds", "search.rulers":"Rulers",
"search.eras":"Eras", "search.reading":"Reading"
```
Greek: Αναζήτηση τόπων, ευρημάτων, ηγεμόνων / Δεν βρέθηκε τίποτα / Τόποι / Ευρήματα /
Ηγεμόνες / Εποχές / Αναγνώσματα.
Turkish: Yer, buluntu, hükümdar ara / Bir şey bulunamadı / Yerler / Buluntular /
Hükümdarlar / Dönemler / Okumalar.

### 1.7 Verify
- All 23 single-era sites reachable from cold load by name. Generate the list with:

      python3 roundtrip.py dump /tmp/rt.json
      python3 - <<'EOF'
      import json; d=json.load(open("/tmp/rt.json")); E=d["ERAS"]
      for s in d["SETTLEMENTS"]:
          n={e["id"] for e in E for a,b in s["ranges"] if a<=e["end"] and b>=e["start"]}
          if len(n)==1: print(s["id"], s["name"])
      EOF
- "Kyrenia ship" matches the find *The Kyrenia Ship* and opens `kyrenia` at a live year.
- Greek/Turkish names match typed with **and** without diacritics (`Αμαθους` finds
  `Αμαθούς`; `Gazimagusa` finds `Gazimağusa`).
- Picking a filtered-out kind re-enables it.
- `/` focuses; Escape clears without closing an open drawer unintentionally.
- 18/18 sweep with the field populated.

**Budget** ~5 KB code, no data. Assert `buildSearch()` stays under 15 ms.

---

## Plan 2 — Make the time dimension legible

Three separate, independently shippable pieces. 2a is the cheapest and the most useful.

### 2a — Life-span strip in the site drawer

Today the drawer prints ranges as text (`fmtRange` joined by `·`) plus a status line. For
the 46 sites spanning five or more eras, and the 9 with gaps, that text hides the shape:
Hala Sultan Tekke (`hst`) is `[[-1650,-1150],[649,2026]]` — a Bronze Age town, then a 1,800-year
silence, then a shrine. A 3 mm strip tells that instantly.

**Where** in `renderDrawer(s)`, immediately after

```js
<div class="status ${active?"active":"inactive"}">${status}</div>
```

insert `${spanHtml(s)}`.

**Geometry.** The strip must use the same non-linear time axis as the slider, so
`yearToT()` — *not* a linear year scale. Bands come from `ERAS[].t0/.t1/.color`, which is
exactly how the slider gradient is already built (line 751).

```js
/* Occupation strip. Uses timeline-t, not years, so it lines up with the slider
   and the era bar above it rather than compressing 10,000 BCE into a hairline. */
function spanHtml(s){
  const W=100, seg=r=>{ const a=yearToT(r[0])*W, b=yearToT(r[1])*W;
    return {a, w:Math.max(0.6,b-a)}; };                    /* min width keeps a 50-year phase visible */
  const bands=ERAS.map(e=>`<rect x="${(e.t0*W).toFixed(2)}" y="0" width="${((e.t1-e.t0)*W).toFixed(2)}"
      height="14" fill="${e.color}" opacity=".22"></rect>`).join("");
  const live=s.ranges.map(r=>{ const g=seg(r);
    return `<rect class="on" x="${g.a.toFixed(2)}" y="3" width="${g.w.toFixed(2)}" height="8" rx="1"></rect>`; }).join("");
  const now=(yearToT(year)*W).toFixed(2);
  const first=s.ranges[0][0], last=s.ranges[s.ranges.length-1][1];
  return `<div class="span">
    <svg viewBox="0 0 ${W} 14" preserveAspectRatio="none" role="img"
         aria-label="${UI("span.alt","Occupation over time")}: ${s.ranges.map(r=>fmtRange(r[0],r[1])).join("; ")}">
      ${bands}${live}<line class="cur" x1="${now}" x2="${now}" y1="0" y2="14"></line>
    </svg>
    <div class="ends"><span>${fmtYear(first)}</span><span>${fmtYear(last)}</span></div>
  </div>`;
}
```

`preserveAspectRatio="none"` lets one viewBox stretch to any drawer width, so nothing
needs re-measuring on resize — but it also means stroke widths distort, hence the
current-year marker is drawn as a `<rect>` if a `<line>` looks wrong at narrow widths.

```css
.span{margin:10px 0 14px}
.span svg{display:block;width:100%;height:14px;background:var(--surface-2);border-radius:2px}
.span .on{fill:var(--ink)}
.span .cur{stroke:var(--copper);stroke-width:1.5;vector-effect:non-scaling-stroke}
.span .ends{display:flex;justify-content:space-between;font-family:var(--font-mono);
  font-size:10px;color:var(--muted);margin-top:3px}
```

`vector-effect:non-scaling-stroke` is what keeps the marker 1.5 px wide under the
non-uniform scale. Without it the line is invisible.

Because `renderDrawer` is re-run from `render()` on every year change, the marker
follows the slider for free.

**Verify.** `hst` shows two blocks with a wide gap; `kyrenia` shows one
continuous block; a single-era site shows a block at least 0.6 units wide. All 9 gap sites must render two or more blocks:
`erimi`, `hst`, `marion`, `mylouthkia`, `agios_georgios_pegeia`, `yeronisos`,
`pyla_koutsopetria`, `evrychou`, `skouriotissa`.

### 2b — "What changed this era"

The panel says what *is*, never what *happened at the seam*. Founded/abandoned counts are
derivable from existing data with no new research.

```js
/* Sites whose first or last occupation falls inside this era. Derived, not authored:
   the ranges already carry it, so it cannot drift out of step with the map. */
function eraChanges(e){
  const inEra=y=>y>=e.start&&y<e.end;
  const founded=[], left=[];
  SETTLEMENTS.forEach(s=>{
    if(!shown(s)) return;
    const first=s.ranges[0][0], last=s.ranges[s.ranges.length-1][1];
    if(inEra(first)) founded.push(s);
    if(inEra(last)&&last<Y_MAX) left.push(s);
  });
  return {founded,left};
}
function changesHtml(e){
  const {founded,left}=eraChanges(e);
  if(!founded.length&&!left.length) return "";
  const list=(arr,key,en)=>arr.length?`<dt>${UI(key,en)}</dt><dd>${
    arr.slice().sort((a,b)=>siteField(a,"name").localeCompare(siteField(b,"name"),lang))
       .map(s=>`<button class="sref" data-site="${s.id}">${siteField(s,"name")}</button>`)
       .join(`<span class="sep">·</span>`)}</dd>`:"";
  return `<h3>${UI("changes.title","What changed")}</h3><dl class="changes">
    ${list(founded,"changes.founded","First occupied")}
    ${list(left,"changes.left","Last occupied")}</dl>`;
}
```

Insert `${changesHtml(e)}` in `render()`'s `panel.innerHTML` between `${lifeHtml(e)}` and
`${onGlobeHtml()}`. The `.sref` buttons need **no handler**. Line 1268 already delegates on the panel —
`panel.addEventListener("click",ev=>{const b=ev.target.closest("[data-site]"); if(b) openSite(b.dataset.site);})`
— so reusing the `data-site` attribute is the whole wiring.

**Honesty trap.** "First occupied" is the first date **in our data**, which for many
prehistoric sites is the first *excavated* phase, not the founding. The heading must read
"First occupied" / "Last occupied", never "Founded" / "Abandoned", and the section needs
a one-line note: *"Dates are the earliest and latest occupation attested by excavation,
not necessarily the founding or the end."* Add as `UI("changes.note", …)`.

`shown(s)` in the filter means the counts respond to the site filter, which is right —
but re-render on filter change, so `applyFilter()` must call `render()` (it already does).

### 2c — Where the finds are now

1,145 finds each carry `f.w` (present location). Inverting that index answers "what can I
actually go and see in the Cyprus Museum?" — a question the atlas currently cannot answer
at all.

`f.w` is free prose, so it needs normalising before it can be a key:

```python
# research/museums.py — run once, inspect, then hand-map the tail
# python3 roundtrip.py dump /tmp/rt.json   first
import json, collections
d = json.load(open("/tmp/rt.json"))
c = collections.Counter()
for s in d["SETTLEMENTS"]:
    for f in s["finds"]:
        c[f["w"].strip()] += 1
for k, n in c.most_common():
    print(f"{n:4d}  {k}")
```

Expect a long tail ("Cyprus Museum, Nicosia", "Cyprus Museum", "in situ", "Nicosia,
Cyprus Museum"). Do **not** regex-normalise blindly — build an explicit
`{raw: canonical}` map in `research/museum-map.json`, add a `f.m` canonical key via
`roundtrip.py`, and leave `f.w` untouched as the displayed string. Anything unmapped
falls into "Other / not recorded" rather than being guessed.

Then a view that groups by `f.m`, each entry linking back to its site and year. This is
the largest of the three pieces (data work plus a new view) and should be done last.

**Budget** 2a ~1.5 KB, 2b ~1.5 KB, 2c ~6 KB of new keys plus view.

---

## Plan 3 — Guided routes

Sixteen eras and 131 sites with no suggested path in. A route is a scripted sequence of
states — year, camera, optional site, optional filter — with a line of text per step. It
reuses `setYear`, `flyTo`, `openSite` and `kindOn` and introduces no new rendering.

### 3.1 Data shape

```js
/* Routes are pure state scripts: every step is a set of existing controls, so a route
   can never show something the free-roaming map cannot. */
const ROUTES=[{
  id:"copper",
  title:"The copper island",
  blurb:"How one metal named the island and paid for its palaces.",
  steps:[
    {y:-2400, view:"island", filter:["village","works"],
     text:"Copper working begins in the foothills of the Troodos."},
    {y:-1300, view:"island", site:"enkomi",
     text:"Enkomi turns ore into ingots and ships them east; Alashiya appears in the Amarna letters."},
    {y:-1200, view:"region",
     text:"The palace economies that bought the copper collapse within a generation."},
    {y:50,    view:"island", site:"soli",
     text:"Roman Soli works the same seams; Pliny still calls the best copper Cyprian."},
    {y:1974,  view:"island", site:"skouriotissa",
     text:"Skouriotissa is still mined — the longest-worked copper source on earth."}
  ]
}, /* … */];
```

Every `y` must lie inside `[Y_MIN, Y_MAX]` and every `site` must exist. Assert both at
load in a debug build:

```js
ROUTES.forEach(r=>r.steps.forEach((st,i)=>{
  console.assert(st.y>=Y_MIN&&st.y<=Y_MAX, r.id, i, "year out of range");
  console.assert(!st.site||SETTLEMENTS.some(s=>s.id===st.site), r.id, i, "unknown site");
}));
```

Better: check them in `atlas.py` at build time and never ship the assertions.

### 3.2 Runner

```js
let route=null, routeStep=0;
function startRoute(id){
  route=ROUTES.find(r=>r.id===id); routeStep=-1;
  if(route){ routeSavedFilter={...kindOn}; nextRouteStep(); }
}
function nextRouteStep(d=1){
  if(!route) return;
  routeStep=Math.max(0,Math.min(route.steps.length-1,routeStep+d));
  const st=route.steps[routeStep];
  if(st.filter){ Object.keys(kindOn).forEach(k=>kindOn[k]=st.filter.includes(k)); applyFilter(); }
  setYear(st.y);
  if(st.site) openSite(st.site); else closeSite();
  presetView=st.view||presetView;
  const centre=st.site
    ? (s=>[s.lon,s.lat])(SETTLEMENTS.find(s=>s.id===st.site))
    : CYPRUS_CENTER;
  flyTo(PRESET[st.view||"island"](), centre, reduceMotion?0:1200);
  renderRouteBar();
}
function endRoute(){
  if(routeSavedFilter){ Object.assign(kindOn,routeSavedFilter); applyFilter(); }
  route=null; renderRouteBar();
}
```

**Traps.**
- `setYear` calls `render()`, which rebuilds `panel.innerHTML` — so the route bar must
  live **outside** `#panel`, or it is destroyed on every step. Put it in the stage, above
  the timeline.
- Restore the filter on exit (`routeSavedFilter`). Leaving a route with three of six
  kinds hidden and no explanation is the kind of bug that reads as data loss.
- Any manual interaction (slider, era bar, globe drag) should leave the route rather
  than silently desync. Call `endRoute()` from the slider `input` handler guarded by a
  flag set during `nextRouteStep`.

### 3.3 Route bar

```html
<div class="routebar" id="routebar" hidden>
  <div class="rtitle"></div>
  <p class="rtext"></p>
  <div class="rnav">
    <button id="rPrev">‹</button>
    <span class="rcount mono"></span>
    <button id="rNext">›</button>
    <button id="rEnd" data-i18n="route.exit">Leave route</button>
  </div>
</div>
```

Keep it to two lines of text at 320 px. Position it `absolute` over the stage bottom,
not in the flex flow — a new flow row is exactly the change that clipped the app before.

### 3.4 Which routes

Four is the right number; each must be defensible from data already in the file.
Candidates: **The copper island** (economy, 2400 BCE–now), **Twelve kings and an
empire** (the city-kingdoms and their end, 800–294 BCE), **Crusader detour** (1191–1489,
Richard to Caterina), **The line** (1878–1974, and honest that the 1974 division line is
not drawn on the map).

**Budget** ~4 KB code plus ~1 KB per route including el/tr text. All route prose needs
translating — it is short enough to do properly rather than stage.

---

## Plan 4 — Smaller things, roughly in order of value

### 4a — Play the timeline

**Markup** — in `<footer class="timeline">`, before `#prevEra`:

```html
<button class="step play" id="playBtn" data-i18n-title="btn.play"
        title="Play through time" aria-label="Play through time" aria-pressed="false">▶</button>
```

`data-i18n-title` is a new hook, like `data-i18n-ph` in Plan 1 — neither exists yet, so
add both to `applyLanguage()` in one pass. Declare `const playBtn=$("#playBtn")` beside
the other element handles at line 735.

**Loop.** Step in timeline-*t*, never in years — a linear year step spends 80% of the
run in prehistory and flickers through the last 3,000 years in two seconds.

```js
/* Playback moves at constant speed along the timeline's own axis, so each era gets
   screen time in proportion to its band, exactly like the slider. */
let playTimer=null;
const PLAY_SECONDS=90;                       /* whole span, start to finish */
function togglePlay(){ playTimer?stopPlay():startPlay(); }
function startPlay(){
  if(reduceMotion) return;                   /* honour the media query, do not animate */
  if(yearToT(year)>=1) setYear(Y_MIN);
  let last=null;
  playTimer=d3.timer(()=>{
    const now=performance.now(), dt=last==null?0:(now-last)/1000; last=now;
    const t=yearToT(year)+dt/PLAY_SECONDS;
    if(t>=1){ setYear(Y_MAX); stopPlay(); return; }
    setYear(roundYear(tToYear(t)));
  });
  playBtn.textContent="❚❚"; playBtn.setAttribute("aria-pressed","true");
}
function stopPlay(){
  if(playTimer){ playTimer.stop(); playTimer=null; }
  playBtn.textContent="▶"; playBtn.setAttribute("aria-pressed","false");
}
```

**Traps.**
- `setYear` → `render()` rebuilds `panel.innerHTML` **every frame**. At 60 fps that is a
  full re-layout of a long panel and it will drop frames. Either throttle the panel
  rebuild (only when `eraOf(year).id` changes) or accept ~10 steps/second by driving the
  timer with `d3.interval(…, 100)` instead. Measure before choosing — interleaved, in one
  browser session, per the harness rule.
- Playing must stop on any manual slider input, era-bar click, or `Escape`.
- `reduceMotion` already gates `flyTo`; gate playback the same way rather than inventing
  a second preference.
- `history.replaceState` runs inside `render()`. Sixty replaceState calls a second is
  abusive to the history API — throttle it (see 4b) before shipping play.

### 4b — Deep links that carry the whole view

`render()` currently writes `#y=…` and `&lang=…`. `v` (view) is read at startup and never
written, so a shared link always lands on the island view. Extend to `y`, `lang`, `v`,
`site`, `f`.

```js
/* Everything a reader could have set, so a pasted link reproduces the screen.
   Throttled because render() runs on every year step, playback included. */
let hashPending=null;
function syncHash(){
  if(hashPending) return;
  hashPending=setTimeout(()=>{
    hashPending=null;
    const p=[`y=${year}`];
    if(lang!=="en") p.push(`lang=${lang}`);
    if(presetView&&presetView!=="island") p.push(`v=${presetView}`);
    if(selected) p.push(`site=${selected}`);
    const off=Object.keys(kindOn).filter(k=>!kindOn[k]);
    if(off.length) p.push(`f=${off.join(",")}`);
    history.replaceState(null,"","#"+p.join("&"));
  },250);
}
```

Replace the `history.replaceState(…)` line at the end of `render()` with `syncHash()`.

Startup, extending the existing block that reads `y` and `v`:

```js
const wantSite=hash.get("site");
const off=(hash.get("f")||"").split(",").filter(Boolean);
off.forEach(k=>{ if(k in kindOn) kindOn[k]=false; });      /* ignore unknown keys silently */
…
if(wantSite&&SETTLEMENTS.some(s=>s.id===wantSite)) openSite(wantSite);
```

Order matters: filters before the first `render()`, `openSite` after the SVG dots exist.
An unknown `site` or `f` value must be ignored, never throw — links will outlive ids.

Then a copy-link affordance. `navigator.clipboard.writeText(location.href)` needs a
secure context; from `file://` it fails, so keep a `document.execCommand("copy")`
fallback or the button is dead in local testing.

### 4c — Chronology view

A scrolling column of all ~160 events (16 eras × ~10) as an alternative to the map.
`ERAS[].events` is already `[[year, text], …]`, so the data is done:

```js
const ALL_EVENTS=ERAS.flatMap(e=>e.events.map(([y,t])=>({y,t,era:e})))
                     .sort((a,b)=>a.y-b.y);
```

Render as a list with a sticky era heading, each row clickable to `setYear(y)`. The cost
is not the list, it is deciding what happens to the globe — either a split view (globe
shrinks) or a mode switch (globe hidden). A mode switch is cheaper and does not fight the
resizable-panel logic in `layout()`/`setPanelW()`.

Worth doing only if the era-bar and slider prove insufficient in use. Park it.

### 4d — Terrain

Troodos and Kyrenia range shading would explain most of the settlement pattern —
copper in the foothills, ports on the coastal plain, the Mesaoria between them.

**Do not fetch a raster.** Everything must stay in one file, and a hillshade tile of
usable resolution is larger than the entire current document. Options in cost order:

1. **Two hand-drawn massif polygons** (Troodos, Pentadaktylos) filled with a soft radial
   gradient. ~1 KB. Drawn on `landLayer` under `source-atop` so they cannot spill into
   the sea, before the empire fills.
2. **Contour rings** at ~500/1000/1500 m, simplified hard. Source SRTM via
   `rasterio` + `matplotlib.contour`, then Douglas-Peucker with the same
   distance-graded tolerance used by `gradeland.py`. ~15–30 KB, honest, and reusable for
   an elevation label on Olympus.
3. Anything raster-based. Out of budget.

Start with 1, and only go to 2 if it reads as decorative rather than informative.

---

## Suggested order

1. **1 — Search.** Fixes the one real dead end (23 sites and 1,145 finds unreachable).
2. **2a — Life-span strip.** Cheapest real gain in the file; ~1.5 KB.
3. **4b — Deep links.** Small, and every later feature wants to be linkable.
4. **2b — What changed.** Derived from data already present.
5. **3 — Routes.** The biggest change in how the thing is used; do it once the pieces it
   scripts are all in place.
6. **4a — Play.** Fun, but needs the render-throttle work first.
7. **2c / 4d / 4c.** Data-heavy or discretionary.

---

## Open items

- **The 1974 line.** Declined once, deliberately. If it is ever drawn it needs a label
  that names it neutrally (a ceasefire line, not a border), and the source stated. The
  atlas currently says nothing, which is a choice worth keeping until it is made
  deliberately again.
- **Prose translation.** Site descriptions, 4,580 find fields, era narratives and ruler
  notes are still English under Greek and Turkish shells. Lookups fall back, so it can
  land in batches; the era-level spine (`e.region` and each power's `p.desc`) is the natural first one.
- **Known source quirks**, documented rather than silently corrected: Crete shown as
  Ottoman in 1600, Belgrade as Austrian in 1700, Hittites still drawn at 700 BCE. If a
  future pass fixes them, fix `build_extents.py`, not the injected data.
