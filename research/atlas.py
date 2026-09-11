"""Parse the atlas's top-level data consts, whether written on one line or many."""
import json
HTML='/home/merkourio/Documents/Cyprus history map/cyprus-historical-explorer.html'
def load(name, path=HTML):
    h=open(path,encoding='utf-8').read()
    i=h.index('const %s = '%name)+len('const %s = '%name)
    depth=0; j=i
    while True:
        c=h[j]
        if c in '[{': depth+=1
        elif c in ']}':
            depth-=1
            if depth==0: j+=1; break
        j+=1
    return json.loads(h[i:j])
