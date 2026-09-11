import asyncio,sys
from playwright.async_api import async_playwright
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
N='/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad'
out=sys.argv[1] if len(sys.argv)>1 else 'emblems'
GRID='''()=>{
  const wrap=document.createElement("div");
  wrap.style.cssText="position:fixed;inset:0;z-index:99;background:var(--ground);padding:18px;overflow:auto;display:grid;grid-template-columns:repeat(4,1fr);gap:14px";
  const order=Object.keys(POWERS);
  order.forEach(pid=>{
    const p=POWERS[pid], key=p.icon, f=ICONS[key];
    const cell=document.createElement("div");
    cell.style.cssText="display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px;background:var(--surface);border:1px solid var(--line);border-radius:6px";
    const era=ERAS.find(e=>e.power===pid);
    cell.style.setProperty("--era", era?era.color:"#888");
    cell.innerHTML=`<div class="emblem" style="width:88px;height:88px;border-radius:8px"><svg viewBox="0 0 48 48" style="width:72px;height:72px">${f?f():""}</svg></div>
      <div style="font-family:var(--font-mono);font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em">${key}</div>
      <div style="font-family:var(--font-display);font-size:12.5px;text-align:center;line-height:1.2">${p.name}</div>`;
    wrap.appendChild(cell);
  });
  document.body.appendChild(wrap);
}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for scheme in ('light','dark'):
            pg=await b.new_page(viewport={'width':1080,'height':1400},color_scheme=scheme)
            await pg.goto('file://'+HTML); await pg.wait_for_timeout(3000)
            await pg.evaluate(GRID); await pg.wait_for_timeout(400)
            await pg.screenshot(path='%s/%s-%s.png'%(N,out,scheme),full_page=True)
            await pg.close()
        await b.close()
asyncio.run(main())
