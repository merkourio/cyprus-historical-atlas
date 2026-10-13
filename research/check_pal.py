import sys,json,re
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from atlas import load, HTML
from colour import hex2rgb, over, dE
HERE=Path(__file__).resolve().parent
ERA=json.load(open(sys.argv[1] if len(sys.argv)>1 else HERE/'era-colors.json'))
EXT=json.load(open(sys.argv[2] if len(sys.argv)>2 else HERE/'extent-colors.json'))
A=json.loads(sys.argv[3]) if len(sys.argv)>3 else {'overlord':.44,'co-power':.52,'suzerain':.28}
# Compare over the land colours actually shipped in each theme.
LAND=[hex2rgb(c) for c in dict.fromkeys(re.findall(r'--land:\s*(#[0-9a-fA-F]{6})',Path(HTML).read_text()))]
E=load('EXTENTS')
slots={}
for e in E:
    s=slots.setdefault(e['name'],{'role':e['role'],'from':e['from'],'to':e['to']})
    s['from']=min(s['from'],e['from']); s['to']=max(s['to'],e['to'])
def coact(a,b): return not (slots[a]['to']<slots[b]['from'] or slots[b]['to']<slots[a]['from'])
def adj(a,b): return abs(slots[a]['to']-slots[b]['from'])<80 or abs(slots[b]['to']-slots[a]['from'])<80
names=list(slots)
print('=== EXTENTS, as painted (alphas %s) ==='%A)
bad=0
for i in range(len(names)):
    for j in range(i+1,len(names)):
        a,b=names[i],names[j]
        # one polity under two names: sharing a colour is the point
        if {a,b}=={'Eastern Roman Empire','Byzantine Empire'}: continue
        d=min(dE(over(hex2rgb(EXT[a]),bg,A[slots[a]['role']]),
                 over(hex2rgb(EXT[b]),bg,A[slots[b]['role']])) for bg in LAND)
        co,ad=coact(a,b),adj(a,b)
        need=14 if co else (10 if ad else 6)
        if d<need:
            bad+=1
            print('  %5.1f (need %d) %-24s %-24s %s'%(d,need,a[:24],b[:24],'CO-ACTIVE' if co else 'consecutive' if ad else ''))
print('  pairs below threshold: %d'%bad)
ER=load('ERAS'); ids=[e['id'] for e in ER]
print('\n=== ERA BAR, full opacity ===')
bad2=0
for i in range(len(ids)):
    for j in range(i+1,len(ids)):
        d=dE(hex2rgb(ERA[ids[i]]),hex2rgb(ERA[ids[j]]))
        need=20 if j==i+1 else 12
        if d<need:
            bad2+=1
            print('  %5.1f (need %d) %-12s %-12s %s'%(d,need,ids[i],ids[j],'adjacent' if j==i+1 else ''))
print('  pairs below threshold: %d'%bad2)

if bad or bad2:
    sys.exit(1)
