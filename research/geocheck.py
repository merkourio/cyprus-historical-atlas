import asyncio, json
from playwright.async_api import async_playwright
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
base={s['id'] for s in json.load(open('/home/merkourio/Documents/Cyprus history map/research/atlas-data.json'))['SETTLEMENTS']}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto('file://'+HTML); await pg.wait_for_timeout(3000)
        r=await pg.evaluate('''()=>SETTLEMENTS.map(s=>{
            let on=d3.geoContains(CYPRUS,[s.lon,s.lat]);
            // distance in km to the nearest point on the coastline if off-land
            let best=1e9;
            if(!on){
              const walk=g=>{ if(g.type==="Polygon") g.coordinates.forEach(r=>r.forEach(c=>{
                    const d=d3.geoDistance([s.lon,s.lat],c)*6371; if(d<best) best=d; }));
                 else if(g.type==="MultiPolygon") g.coordinates.forEach(pl=>pl.forEach(r=>r.forEach(c=>{
                    const d=d3.geoDistance([s.lon,s.lat],c)*6371; if(d<best) best=d; })));
                 else if(g.type==="FeatureCollection") g.features.forEach(f=>walk(f.geometry));
                 else if(g.type==="Feature") walk(g.geometry);
                 else if(g.type==="GeometryCollection") g.geometries.forEach(walk); };
              walk(CYPRUS);
            }
            return {id:s.id,name:s.name,lon:s.lon,lat:s.lat,type:s.type,on,km:on?0:best};
        })''')
        await b.close()
    off=[x for x in r if not x['on']]
    print('settlements checked: %d   on the island polygon: %d   off: %d\n'%(len(r),len(r)-len(off),len(off)))
    off.sort(key=lambda x:-x['km'])
    for x in off:
        print('  %-24s %-44s %8.4f,%7.4f  %5.2f km off the coastline   %s'%(
          x['id'],x['name'],x['lon'],x['lat'],x['km'],'NEW' if x['id'] not in base else 'pre-existing'))
asyncio.run(main())
