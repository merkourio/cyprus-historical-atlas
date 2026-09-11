import sys,json
sys.path.insert(0,'/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad')
from atlas import load
from colour import hex2rgb, over, dE
ERA=json.load(open(sys.argv[1])); EXT=json.load(open(sys.argv[2]))
A=json.loads(sys.argv[3])   # alphas
LAND=[hex2rgb('#F3F0E6'),hex2rgb('#2E4B54')]
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
