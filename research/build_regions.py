#!/usr/bin/env python3
"""Build the neighbouring polities around Cyprus, as dated snapshots clipped to the region.

Source: aourednik/historical-basemaps. Everything is clipped to a box around the eastern
Mediterranean, simplified, and the polity that already appears as the ruling empire that
year is left out so it is not drawn twice.
"""
import json,sys,re,math,os
from shapely.geometry import shape, box, Polygon, MultiPolygon, Point
from shapely.ops import unary_union, nearest_points
from shapely.prepared import prep

def atlas_land():
    """The coastline this atlas actually draws, so boundaries can be told apart:
    a segment that runs over water is the coast doing its job, not a frontier."""
    h=open(HTML,encoding='utf-8').read()
    i=h.index('const LAND_TOPO = ')+len('const LAND_TOPO = ')
    depth=0; j=i
    while True:
        c=h[j]
        if c in '[{': depth+=1
        elif c in ']}':
            depth-=1
            if depth==0: j+=1; break
        j+=1
    T=json.loads(h[i:j])
    sx,sy=T['transform']['scale']; tx,ty=T['transform']['translate']
    arcs=[]
    for a in T['arcs']:
        x=y=0; pts=[]
        for dx,dy in a:
            x+=dx; y+=dy; pts.append((x*sx+tx, y*sy+ty))
        arcs.append(pts)
    def ring(idx):
        out=[]
        for k in idx:
            a=arcs[~k][::-1] if k<0 else arcs[k]
            out.extend(a if not out else a[1:])
        return out
    polys=[]
    for g in T['objects']['land']['geometries']:
        mp=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]   # topojson indexes arcs
        for poly in mp:
            try:
                r=ring(poly[0])
                if len(r)>=4: polys.append(Polygon(r).buffer(0))
            except Exception: pass
    return unary_union([q for q in polys if q.is_valid and not q.is_empty])
CY=(33.2,35.1)
def km_to_cyprus(g):
    from shapely.geometry import Point
    a,b=nearest_points(g,Point(*CY))
    la=math.radians((a.y+b.y)/2)
    return math.hypot((a.x-b.x)*111.32*math.cos(la),(a.y-b.y)*110.57)

HB=os.path.dirname(os.path.abspath(__file__))+'/hb/'
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
BOX=box(19,22,56,44)   # eastern Mediterranean out to Persia
YEARS=[-500,-400,-323,-300,-200,-100,-1,100,200,300,400,500,600,700,800,900,
       1000,1100,1200,1279,1300,1400,1500,1530,1600,1650,1700,1783,1800,
       1880,1900,1914,1938,1945,1960,2000]
MIN_AREA=0.45         # square degrees after clipping; smaller reads as a sliver
NEAR_KM=1100          # a polity further than this counts only if the atlas names it
MAX_PER_YEAR=12       # the nearest few; more than this is clutter at region zoom
TOL=float(os.environ.get('TOL','0.06'))
# not countries: culture areas and nomadic ranges, which are huge and not what is wanted
# not countries: culture areas, nomadic ranges, and the source's own placeholders
SKIP=re.compile(r'nomad|pastoral|hunter|gatherer|tribes|culture|foragers|herders'
                r'|^\?+$|minor states|state societies|unclaimed|uninhabited|various',re.I)

def fname(y): return HB+('world_bc%d.geojson'%-y if y<0 else 'world_%d.geojson'%y)

def extents_by_year():
    """the ruling empire drawn for each year, so we can leave it out here"""
    h=open(HTML,encoding='utf-8').read()
    i=h.index('const EXTENTS = '); j=h.index('];',i)+1
    E=json.loads(h[i+len('const EXTENTS = '):j])
    for e in E:
        for s in e['snaps']:
            s['geom']=unary_union([Polygon(r[0]).buffer(0) for r in s['coords']])
    return E

def ruling_geom(E, y):
    """union of the outlines already drawn for this year, nearest snapshot per empire"""
    gs=[]
    for e in E:
        if y<e['from'] or y>e['to']: continue
        best=min(e['snaps'],key=lambda s:abs(s['y']-y))
        gs.append(best['geom'])
    return unary_union(gs) if gs else None

def eras_and_labels():
    h=open(HTML,encoding='utf-8').read()
    lines=h.split('\n')
    def parse(name):
        s=next(i for i,l in enumerate(lines) if l.startswith('const %s = '%name))
        op=lines[s].rstrip()[-1]; cl={'{':'};','[':'];'}[op]
        e=next(i for i in range(s+1,len(lines)) if lines[i].strip()==cl)
        body='\n'.join(lines[s:e+1]); return json.loads(body[body.index('=')+1:].rstrip().rstrip(';'))
    return parse('ERAS'), parse('NEIGHBOURS')

def polys(g):
    return [p for p in (g.geoms if isinstance(g,MultiPolygon) else [g]) if isinstance(p,Polygon)]

LANDPREP=None
def main():
    global LANDPREP
    LANDPREP=prep(atlas_land())
    print('atlas coastline loaded, for telling frontiers from coast')
    E=extents_by_year()
    ERAS,NB=eras_and_labels()
    out=[]
    total=0
    print('%-7s %-5s %s'%('year','n','polities'))
    for y in YEARS:
        if not os.path.exists(fname(y)):
            print('  !! missing %s'%fname(y)); continue
        # Exclude by geometry, not by name: the source spells the same polity several
        # ways ("Mamluk" against "Mamluke"), so a name test silently double-draws it.
        rul=ruling_geom(E,y)
        era=next((e for e in ERAS if e['start']<=y<=e['end']), None)
        labels=[(lo,la) for lo,la,_ in (NB.get(era['id'],[]) if era else [])]
        d=json.load(open(fname(y)))
        merged={}
        for f in d['features']:
            nm=f['properties'].get('NAME')
            if not nm or not f.get('geometry'): continue
            if SKIP.search(nm): continue
            try:
                g=shape(f['geometry'])
                if not g.is_valid: g=g.buffer(0)
                c=g.intersection(BOX)
            except Exception: continue
            if c.is_empty or c.area<MIN_AREA: continue
            if nm.lower()=='cyprus': continue
            if rul is not None:
                try:
                    if c.intersection(rul).area > 0.6*c.area: continue
                except Exception: pass
            merged.setdefault(nm,[]).append(c)
        items=[]
        for nm,parts in merged.items():
            c=unary_union(parts).simplify(TOL,preserve_topology=False)
            rings=[]
            for p in polys(c):
                if p.area<MIN_AREA*0.5: continue
                r=[[round(x,2),round(v,2)] for x,v in p.exterior.coords]
                ded=[r[0]]
                for q in r[1:]:
                    if q!=ded[-1]: ded.append(q)
                if len(ded)<4: continue
                if ded[0]!=ded[-1]: ded.append(ded[0])
                # a segment is a frontier only if it runs over land for its whole length;
                # anything else is the coast, which the coastline already draws
                mask=''
                for k in range(len(ded)-1):
                    x1,y1=ded[k]; x2,y2=ded[k+1]
                    inland=all(LANDPREP.contains(Point(x1+(x2-x1)*f, y1+(y2-y1)*f))
                               for f in (0.08,0.5,0.92))
                    mask+='1' if inland else '0'
                rings.append([ded,mask])
            u=unary_union(parts)
            dist=km_to_cyprus(u)
            named=any(u.contains(Point(lo,la)) for lo,la in labels)
            # relevant if the atlas already names it, or if it is simply next door.
            # Distance alone cannot tell Persia from the Khazars; the curated labels can.
            if dist>NEAR_KM and not named: continue
            if rings: items.append({'n':nm,'c':[[r[0]] for r in rings],
                                    'm':[r[1] for r in rings],
                                    'a':round(u.area,2),'d':dist,'_g':u,'_named':named})
        # nearest first, then the largest of those: the point is who was next door
        items.sort(key=lambda it:(it['d'], -it['a']))
        items=items[:MAX_PER_YEAR]
        # the atlas already names some of these in its own hand-placed era labels, so
        # only carry a name for the ones it does not
        for it in items:
            rp=it['_g'].representative_point()
            if not it['_named']: it['l']=[round(rp.x,2),round(rp.y,2)]
            else: it.pop('n')
            for k in ('a','d','_g','_named'): it.pop(k)
        pts=sum(len(r[0]) for it in items for r in it['c'])
        total+=pts
        out.append({'y':y,'p':items})
        shown=[it.get('n','(named on the map already)') for it in items]
        print('%-7d %-5d %s'%(y,len(items),', '.join(shown)[:130]))
    json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'))
    print('\n%d snapshots, %d points, tol=%s -> %.1f KB'%(
        len(out),total,TOL,os.path.getsize(sys.argv[1])/1024))
main()
