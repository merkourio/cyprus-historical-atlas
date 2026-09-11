import asyncio
from itertools import groupby
from playwright.async_api import async_playwright
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1400,'height':900})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file://'+HTML); await pg.wait_for_timeout(2800)
        bad=[]
        for y in range(-700,1961,7):
            r=await pg.evaluate('''y=>{const ex=activeExtents(y).filter(x=>x.role==="overlord");
                return ex.length?ex.map(x=>({n:x.name,yr:x.year,has:d3.geoContains(x.geom,CYPRUS_CENTER)})):null;}''',y)
            if r:
                for x in r:
                    if not x['has']: bad.append((y,x['n'],x['yr']))
        print("years sampled where the ruling power's outline excludes Cyprus: %d"%len(bad))
        for key,grp in groupby(bad,key=lambda t:(t[1],t[2])):
            ys=[g[0] for g in grp]
            print('  %-26s outline %-6s years %d..%d'%(key[0],key[1],min(ys),max(ys)))
        dup=[]
        for y in range(-750,1990,3):
            names=await pg.evaluate('y=>activeExtents(y).map(x=>x.name)',y)
            if len(names)!=len(set(names)): dup.append((y,names))
        print('\nyears with a duplicated empire name:',len(dup),dup[:4])
        print('page errors:',len(errs))
        await b.close()
asyncio.run(main())
