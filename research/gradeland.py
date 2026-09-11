#!/usr/bin/env python3
"""Grade the world coastline by distance from Cyprus.

Every view in this atlas is centred on Cyprus, and the low zooms already draw only
6% of the coastline points, so full 50m detail is only ever wanted near the island.
Arcs are simplified with a tolerance that grows with distance. Arc endpoints are
preserved so the topology's arc indices and ring closure stay valid.
"""
import json,sys,math

CY=(33.2,35.1)
def km(a,b):
    la=math.radians((a[1]+b[1])/2)
    return math.hypot((a[0]-b[0])*111.32*math.cos(la),(a[1]-b[1])*110.57)

def decode(T):
    sx,sy=T['transform']['scale']; tx,ty=T['transform']['translate']
    out=[]
    for arc in T['arcs']:
        x=y=0; pts=[]
        for dx,dy in arc:
            x+=dx; y+=dy; pts.append((x*sx+tx, y*sy+ty))
        out.append(pts)
    return out

def dp(pts, tol_deg):
    """Douglas-Peucker keeping the first and last point."""
    if len(pts)<3 or tol_deg<=0: return pts
    keep=[False]*len(pts); keep[0]=keep[-1]=True
    stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop()
        if b<=a+1: continue
        x1,y1=pts[a]; x2,y2=pts[b]
        dx,dy=x2-x1,y2-y1
        n=math.hypot(dx,dy)
        worst=-1.0; wi=-1
        for i in range(a+1,b):
            x,y=pts[i]
            d=abs(dy*(x-x1)-dx*(y-y1))/n if n>1e-12 else math.hypot(x-x1,y-y1)
            if d>worst: worst,wi=d,i
        if worst>tol_deg:
            keep[wi]=True; stack.append((a,wi)); stack.append((wi,b))
    return [p for p,k in zip(pts,keep) if k]

def tol_for(pts):
    """km tolerance from the arc's distance to Cyprus"""
    d=min(km(p,CY) for p in pts[::max(1,len(pts)//12)])
    if d<1200: return 0.0
    if d<3000: return 2.0
    if d<6000: return 6.0
    return 14.0

def encode(arcs, q):
    xs=[p[0] for a in arcs for p in a]; ys=[p[1] for a in arcs for p in a]
    x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
    sx=(x1-x0)/(q-1); sy=(y1-y0)/(q-1)
    out=[]
    for a in arcs:
        px=py=0; e=[]
        for lon,lat in a:
            ix=round((lon-x0)/sx); iy=round((lat-y0)/sy)
            d=[ix-px,iy-py]; px,py=ix,iy
            e.append(d)
        ded=[e[0]]+[d for d in e[1:] if d!=[0,0]]
        out.append(ded if len(ded)>=2 else e[:2])
    return {'scale':[sx,sy],'translate':[x0,y0]}, out

def main():
    q=int(sys.argv[1]) if len(sys.argv)>1 else 50000
    h=open('/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html',encoding='utf-8').read()
    i=h.index('const LAND_TOPO = '); j=h.index('\n',i)
    raw=h[i+len('const LAND_TOPO = '):j].rstrip().rstrip(';')
    T=json.loads(raw)
    A=decode(T)
    n0=sum(len(a) for a in A)
    simp=[]; band={}
    for a in A:
        t=tol_for(a)
        band[t]=band.get(t,0)+len(a)
        simp.append(dp(a, t/111.0))
    n1=sum(len(a) for a in simp)
    tr,arcs=encode(simp,q)
    out={'type':'Topology','bbox':T.get('bbox'),'transform':tr,
         'objects':T['objects'],'arcs':arcs}
    s=json.dumps(out,separators=(',',':'))
    print('points by distance band (before): %s'%{('%dkm'%k if k else 'full'):v for k,v in sorted(band.items())})
    print('points %d -> %d (%.0f%% kept)'%(n0,n1,100*n1/n0))
    print('size   %.1f KB -> %.1f KB  (saved %.1f KB)'%(len(raw)/1024,len(s)/1024,(len(raw)-len(s))/1024))
    open(sys.argv[2],'w').write(s)
main()
