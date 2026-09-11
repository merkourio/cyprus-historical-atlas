import asyncio
from playwright.async_api import async_playwright
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
N='/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad'
GRID='''()=>{
  const w=document.createElement("div");
  w.style.cssText="position:fixed;inset:0;z-index:99;background:var(--ground);padding:16px;overflow:auto";
  const keys=Object.keys(ICONS);
  const row=(size,label)=>{
    let h=`<div style="font-family:var(--font-mono);font-size:11px;color:var(--muted);margin:14px 0 6px">${label}</div><div style="display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end">`;
    keys.forEach(k=>{
      const era=ERAS.find(e=>ICONS[POWERS[e.power].icon]===ICONS[k]);
      h+=`<div style="--era:${era?era.color:'#777'};display:flex;flex-direction:column;align-items:center;gap:3px">
            <div class="emblem" style="width:${size+12}px;height:${size+12}px"><svg viewBox="0 0 48 48" style="width:${size}px;height:${size}px">${ICONS[k]()}</svg></div>
            ${size>60?`<div style="font-family:var(--font-mono);font-size:9px;color:var(--muted)">${k}</div>`:""}
          </div>`;
    });
    return h+"</div>";
  };
  w.innerHTML=row(40,"TRUE DISPLAY SIZE, 40 px")+row(120,"ZOOMED, 120 px");
  document.body.appendChild(w);
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1180,'height':900})
        await pg.goto('file://'+HTML); await pg.wait_for_timeout(3000)
        await pg.evaluate(GRID); await pg.wait_for_timeout(400)
        await pg.screenshot(path=N+'/sizes.png',full_page=True)
        await b.close()
asyncio.run(main())
