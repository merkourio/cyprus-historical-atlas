import asyncio, sys, json
from playwright.async_api import async_playwright
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
N='/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad'
CASES=[('aceramic',-9000),('lba',-1400),('archaic',-600),('classical',-450),
       ('roman',150),('byzantine',700),('lusignan',1300),('ottoman',1700),('republic',2000)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1600,'height':1000},device_scale_factor=1)
        errs=[]
        pg.on('console', lambda m: errs.append('CONSOLE %s: %s'%(m.type,m.text)) if m.type=='error' else None)
        pg.on('pageerror', lambda e: errs.append('PAGEERROR: %s'%e))
        await pg.goto('file://'+HTML)
        await pg.evaluate('()=>document.fonts.ready')
        await pg.wait_for_timeout(3500)
        report=[]
        for name,yr in CASES:
            await pg.evaluate('y=>{setYear(y); presetView="island"; flyTo(PRESET.island(),CYPRUS_CENTER,0);}', yr)
            await pg.wait_for_timeout(700)
            r=await pg.evaluate('''()=>{
              const shown=SETTLEMENTS.filter(s=>s._q&&s.el.style.display!=="none");
              const act=SETTLEMENTS.filter(s=>isActive(s,year));
              const quiet=shown.filter(s=>s.el.classList.contains("quiet"));
              return {year, era:eraOf(year).name, active:act.length, shown:shown.length,
                      labelled:shown.length-quiet.length, quiet:quiet.length,
                      count:document.querySelector("#count").textContent,
                      listed:document.querySelectorAll(".sitelist button").length,
                      panelH:document.querySelector("#panel").scrollHeight};
            }''')
            report.append((name,r))
            await pg.screenshot(path='%s/r-%s.png'%(N,name))
        # zoomed-in check: do hidden dots come back
        await pg.evaluate('()=>{setYear(-1400); flyTo(PRESET.island()*4,[33.0,35.0],0);}')
        await pg.wait_for_timeout(700)
        z=await pg.evaluate('()=>({shown:SETTLEMENTS.filter(s=>s._q&&s.el.style.display!=="none").length, count:document.querySelector("#count").textContent})')
        await pg.screenshot(path=N+'/r-zoomed.png')
        await b.close()
        for name,r in report:
            print('%-11s %-22s active=%-3d drawn=%-3d labelled=%-3d hidden_lbl=%-3d listed=%-3d | %s'%(
              name,r['era'],r['active'],r['shown'],r['labelled'],r['quiet'],r['listed'],r['count']))
        print('\nzoomed 4x on the centre: drawn=%d | %s'%(z['shown'],z['count']))
        print('\nJS errors: %d'%len(errs))
        for e in errs[:15]: print('  ',e)
asyncio.run(main())
