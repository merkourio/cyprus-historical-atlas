import json,urllib.request,urllib.parse,time,re,sys
N='/tmp/claude-1000/-home-merkourio-whisper-cpp/39b7e747-2e77-4940-b299-245648dc3693/scratchpad/'
UA='CyprusAtlasResearch/1.0 (markos@kollekt.dk)'
d=json.load(open(N+'reading-draft.json'))
seen={}; out=[]
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':UA})
    for a in range(3):
        try: return json.load(urllib.request.urlopen(r,timeout=30))
        except Exception as e: time.sleep(2)
    return None
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def surname(a): 
    a=a.split(' and ')[0].split(',')[0].replace('(ed.)','').replace('(eds)','').strip()
    return norm(a).split()[-1] if norm(a) else ''
def openlib(e):
    q=urllib.parse.urlencode({'title':e['t'][:80],'limit':8})
    j=get('https://openlibrary.org/search.json?'+q)
    if not j or not j.get('docs'):
        q=urllib.parse.urlencode({'q':e['t'][:60]+' '+surname(e['a']),'limit':8})
        j=get('https://openlibrary.org/search.json?'+q)
    if not j: return None
    sn=surname(e['a']); tn=norm(e['t'])[:40]
    for doc in j.get('docs',[]):
        auth=' '.join(doc.get('author_name',[])).lower()
        title=norm(doc.get('title',''))
        if (sn and sn in norm(auth)) and (title[:25] in tn or tn[:25] in title or any(w in title for w in tn.split()[:3] if len(w)>5)):
            return {'title':doc.get('title'),'author':', '.join(doc.get('author_name',[])[:2]),'year':doc.get('first_publish_year')}
    return None
def crossref(e):
    q=urllib.parse.urlencode({'query.bibliographic':e['t']+' '+surname(e['a']),'rows':5})
    j=get('https://api.crossref.org/works?'+q)
    if not j: return None
    tn=norm(e['t'])[:40]
    for it in j.get('message',{}).get('items',[]):
        title=norm(' '.join(it.get('title',[])))
        if tn[:25] in title or title[:25] in tn:
            yr=(it.get('issued',{}).get('date-parts',[[None]])[0][0])
            return {'title':' '.join(it.get('title',[])),'author':', '.join(a.get('family','') for a in it.get('author',[])[:2]),'year':yr}
    return None
def wiki(e):
    t=e['t'].split(',')[0].split(' Book')[0]
    q=urllib.parse.urlencode({'action':'query','list':'search','srsearch':t+' '+e['a'].split()[0],'format':'json','srlimit':3})
    j=get('https://en.wikipedia.org/w/api.php?'+q)
    if not j: return None
    hits=j.get('query',{}).get('search',[])
    return {'title':hits[0]['title']} if hits else None
for era,items in d.items():
    for e in items:
        key=(e['a'],e['t'])
        if key in seen: continue
        if e['k'] in ('article','essay'): r=crossref(e); via='crossref'
        elif e['k']=='primary' and e['y']<1500: r=wiki(e); via='wikipedia'
        else: r=openlib(e); via='openlibrary'
        if r is None and via=='openlibrary': r=crossref(e); via='crossref'
        if r is None and via!='wikipedia': r=wiki(e); via='wikipedia'
        seen[key]=(r,via)
        time.sleep(0.6)
        print('%-4s %-11s %-30s | %-62s -> %s'%('OK' if r else 'MISS',via,e['a'][:30],e['t'][:62],(r or {}).get('title','')[:50] if r else ''))
json.dump({'%s|%s'%k:v for k,v in seen.items()},open(N+'reading-verify.json','w'),ensure_ascii=False,indent=1)
miss=[k for k,(r,_) in seen.items() if r is None]
print('\nverified %d / %d unique works; unverified: %d'%(len(seen)-len(miss),len(seen),len(miss)))
for k in miss: print('   ',k)
