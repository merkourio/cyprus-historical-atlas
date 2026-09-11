#!/usr/bin/env python3
"""Rebuild EXTENTS as dated snapshots so an empire's border matches the year on screen.

Source: aourednik/historical-basemaps world_<year>.geojson, one file per snapshot year.
For each empire we take every snapshot inside its window (plus the nearest one just
outside, so the window's start has something close), union the matching features,
simplify to a point budget and round to 2 decimals.
"""
import json, glob, os, re, sys
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union

HB='/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad/hb/'
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'

def fname(y): return HB+('world_bc%d.geojson'%-y if y<0 else 'world_%d.geojson'%y)

# years to sample per empire, and how to recognise it in that year's file
SPEC={
 'assyria':  dict(years=[-700], names=['Assyria']),
 'persia':   dict(years=[-500,-400], names=['Achaemenid Empire']),
 'alexander':dict(years=[-323], names=['Empire of Alexander']),
 'ptolemies':dict(years=[-300,-200,-100], names=['Ptolemaic Kingdom']),
 'rome':     dict(years=[-100,-1,100,200,300],
                  names=['Roman Republic','Roman Empire','Rome',
                         'Rome (Constantinus)','Rome (Diocletianus)','Rome (Galerius)','Rome (Maximian)']),
 'byz1':     dict(years=[400,500,600,700], names=['Eastern Roman Empire']),
 'byz2':     dict(years=[800,900], names=['Byzantine Empire']),
 'byz3':     dict(years=[1000,1100], names=['Byzantine Empire']),
 'umayyad':  dict(years=[700], names=['Umayyad Caliphate']),
 'abbasid':  dict(years=[800,900], names=['Abbasid Caliphate']),
 'mamluk':   dict(years=[1400,1500], names=['Mamluke Sultanate']),
 'venice':   dict(years=[1500,1530,1600], names=['Venice']),
 'ottoman':  dict(years=[1600,1650,1700,1783,1800,1880], names=['Ottoman Empire']),
 'britain':  dict(years=[1880,1900,1914,1938,1945,1960], subject=r'brit|united kingdom'),
}
BUDGET=560          # points per snapshot
MIN_RING_AREA=0.35  # square degrees; smaller rings are specks at globe zoom
GRACE=25            # a snapshot may sit this far outside a window and still represent it
# The outlines and the atlas's own coastline come from different datasets at different
# resolutions, so an empire's edge can sit inland of the coast and leave a bare strip
# of land along it. The shading is composited onto land, so dilating the outline by a
# few kilometres closes that gap and the overspill into the sea is simply clipped away.
DILATE=0.09         # degrees

def cyprus_ring():
    """The atlas's own island outline, so the island is drawn accurately."""
    h=open(HTML,encoding='utf-8').read()
    i=h.index('const CYPRUS_RING'); j=h.index('=',i)+1; k=h.index(';\n',j)
    return Polygon(json.loads(h[j:k].strip()))
RING=None

def collect(year, spec):
    d=json.load(open(fname(year)))
    want=set(spec.get('names') or [])
    rx=re.compile(spec['subject'],re.I) if spec.get('subject') else None
    geoms=[]
    for f in d['features']:
        p=f['properties']; nm=str(p.get('NAME') or ''); sub=str(p.get('SUBJECTO') or '')
        keep = nm in want if want else False
        if rx and (rx.search(nm) or rx.search(sub)): keep=True
        if not keep or not f.get('geometry'): continue
        try:
            g=shape(f['geometry'])
            if not g.is_valid: g=g.buffer(0)
            if not g.is_empty: geoms.append(g)
        except Exception: pass
    if not geoms: return None
    u=unary_union(geoms)
    return u if not u.is_empty else None

def rings(g):
    polys = list(g.geoms) if isinstance(g,MultiPolygon) else [g]
    return [p for p in polys if isinstance(p,Polygon)]

def npoints(polys):
    return sum(len(p.exterior.coords) for p in polys)

def build(year, spec, island=False):
    g=collect(year,spec)
    if g is None: return None,'no matching feature'
    polys=[p for p in rings(g) if p.area>=MIN_RING_AREA]
    if not polys: polys=sorted(rings(g),key=lambda p:-p.area)[:1]
    # The source draws Cyprus and Crete as their own small polygons. A single global
    # tolerance flattens them into triangles, so scale the tolerance to each polygon:
    # a small island keeps its shape, a continental landmass loses its wiggles.
    tol=0.03
    while tol<10:
        s=[]
        for q in polys:
            t=min(tol, (q.area**0.5)/9)
            r=q.simplify(t,preserve_topology=False)
            if r.is_valid and not r.is_empty and r.area>=MIN_RING_AREA*0.6: s.append(r)
        if s and npoints(s)<=BUDGET: polys=s; break
        tol*=1.4
    else:
        polys=[q.simplify(6,preserve_topology=False) for q in polys]

    if island:
        # drop the source's own rendering of the island and use the atlas outline, so
        # the two never overlap: overlapping parts of one path cancel when filled
        polys=[q for q in polys
               if not (q.intersection(RING).area>0.5*q.area and q.area<3*RING.area)]
        polys.append(RING)
    # dissolve any residual overlap so the path has no interior edges to stroke
    u=unary_union([q.buffer(DILATE,join_style=2) for q in polys]).buffer(-DILATE*0.35,join_style=2)
    polys=[q for q in rings(u) if q.area>=MIN_RING_AREA*0.6]
    polys=[q.simplify(0.02,preserve_topology=False) for q in polys]
    out=[]
    for p in sorted(polys,key=lambda p:-p.area):
        ring=[[round(x,2),round(y,2)] for x,y in p.exterior.coords]
        # drop consecutive duplicates left by rounding
        ded=[ring[0]]
        for c in ring[1:]:
            if c!=ded[-1]: ded.append(c)
        if len(ded)<4: continue
        if ded[0]!=ded[-1]: ded.append(ded[0])
        if max(c[0] for c in ded)-min(c[0] for c in ded)>180:
            continue   # a ring that wraps the antimeridian renders wrong on the globe
        out.append([ded])
    return (out or None), 'tol=%.2f'%tol

# the empires that actually held Cyprus; the rest only took tribute or shared it
ISLAND={'persia','alexander','ptolemies','rome','byz1','byz2','byz3','venice','ottoman','britain'}

def main():
    global RING
    RING=cyprus_ring()
    h=open(HTML,encoding='utf-8').read()
    i=h.index('const EXTENTS = '); j=h.index('];',i)+1
    old=json.loads(h[i+len('const EXTENTS = '):j])

    out=[]
    print('%-10s %-6s %-7s %-6s %s'%('empire','snaps','points','rings','years'))
    for e in old:
        eid=e['id']
        base={k:e[k] for k in ('id','name','from','to','color','role','note')}
        if eid not in SPEC:
            base['snaps']=e['snaps']          # curated, no source year to rebuild from
            pts=sum(len(r) for s in e['snaps'] for poly in s['coords'] for r in poly)
            print('%-10s %-6d %-7d %-6d %-14s (kept as is)'%(eid,len(e['snaps']),pts,
                  sum(len(s['coords']) for s in e['snaps']),[s['y'] for s in e['snaps']]))
            out.append(base); continue
        snaps=[]
        for y in SPEC[eid]['years']:
            if not (e['from']-GRACE <= y <= e['to']+GRACE):
                continue                       # too far outside the window to represent it
            coords,info=build(y,SPEC[eid],island=eid in ISLAND)
            if coords is None:
                print('  !! %s %d: %s'%(eid,y,info)); continue
            snaps.append({'y':y,'coords':coords})
        if not snaps:
            mid=(e['from']+e['to'])//2
            y=min(SPEC[eid]['years'],key=lambda v:abs(v-mid))
            coords,_=build(y,SPEC[eid],island=eid in ISLAND)
            snaps=[{'y':y,'coords':coords}] if coords else e['snaps']
        base['snaps']=snaps
        pts=sum(len(r) for s in snaps for poly in s['coords'] for r in poly)
        print('%-10s %-6d %-7d %-6d %s'%(eid,len(snaps),pts,
              sum(len(s['coords']) for s in snaps),[s['y'] for s in snaps]))
        out.append(base)

    json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'))
    tot=sum(len(r) for e in out for s in e['snaps'] for poly in s['coords'] for r in poly)
    print('\n%d empires, %d snapshots, %d points total'%(
        len(out),sum(len(e['snaps']) for e in out),tot))
    print('json %.1f KB -> %s'%(os.path.getsize(sys.argv[1])/1024,sys.argv[1]))

main()
