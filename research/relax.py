"""Walk the polished colours back toward the hand-picked ones, keeping every pair above
its threshold. Distinctness is a constraint to satisfy, not a quantity to maximise."""
import sys,json,math,random
sys.path.insert(0,'/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad')
from atlas import load
from colour import hex2rgb, over, dE, lab
from hcl import hcl, rgb2hex, inrange
HAND=json.load(open(sys.argv[1])); START=json.load(open(sys.argv[2]))
A=json.loads(sys.argv[3]); MARGIN=float(sys.argv[4])
LAND=[hex2rgb('#F3F0E6'),hex2rgb('#2E4B54')]
E=load('EXTENTS')
slots={}
for e in E:
    s=slots.setdefault(e['name'],{'role':e['role'],'from':e['from'],'to':e['to']})
    s['from']=min(s['from'],e['from']); s['to']=max(s['to'],e['to'])
names=list(slots); SAME={'Eastern Roman Empire','Byzantine Empire'}
def coact(a,b): return not (slots[a]['to']<slots[b]['from'] or slots[b]['to']<slots[a]['from'])
def adj(a,b): return abs(slots[a]['to']-slots[b]['from'])<80 or abs(slots[b]['to']-slots[a]['from'])<80
def need(a,b): return 15 if coact(a,b) else (11 if adj(a,b) else 8)
def margin(cur):
    m=1e9
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            a,b=names[i],names[j]
            if {a,b}==SAME: continue
            d=min(dE(over(cur[a],bg,A[slots[a]['role']]),over(cur[b],bg,A[slots[b]['role']])) for bg in LAND)
            m=min(m,d-need(a,b))
    return m
def drift(cur): return sum(dE(hex2rgb(HAND[n]),cur[n]) for n in names if n!='Byzantine Empire')
cur={n:hex2rgb(START[n]) for n in names}
assert margin(cur)>=0, 'start must be feasible'
random.seed(5)
for it in range(14000):
    n=random.choice(names)
    if n=='Byzantine Empire': continue
    t=1-it/14000
    old=cur[n]
    # step toward the hand-picked colour, with a little jitter
    h=hex2rgb(HAND[n])
    f=random.uniform(0.05,0.5)
    cand=tuple(round(old[k]+(h[k]-old[k])*f + random.gauss(0,5*t)) for k in range(3))
    cand=tuple(max(0,min(255,c)) for c in cand)
    cur[n]=cand
    if n=='Eastern Roman Empire': cur['Byzantine Empire']=cand
    if margin(cur)>=MARGIN and drift(cur)<drift({**cur,n:old}):
        continue
    cur[n]=old
    if n=='Eastern Roman Empire': cur['Byzantine Empire']=old
print('final margin %+.1f, total drift from the hand palette %.1f'%(margin(cur),drift(cur)))
print('\n%-26s %-9s %-9s drift'%('polity','intended','final'))
for n in names:
    print('  %-24s %-9s %-9s %.1f'%(n[:24],HAND[n],rgb2hex(cur[n]),dE(hex2rgb(HAND[n]),cur[n])))
json.dump({n:rgb2hex(cur[n]) for n in names},open(sys.argv[5],'w'),indent=1)
