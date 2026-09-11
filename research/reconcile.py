#!/usr/bin/env python3
"""Fold duplicate settlement records that two research agents proposed independently.

  python3 reconcile.py <research-dir>

Two agents covering neighbouring periods often write up the same site from their
own end of its life. Dropping one loses real material, so each pair is merged:
the record with more finds supplies the coordinates, the shorter name wins, the
ranges are unioned, and the finds are concatenated and deduped. The merged record
stays in the primary's file; the duplicate is removed from the other.
"""
import json, glob, os, sys, collections

# most specific kind wins when two agents disagree about the same place
RANK = {'town': 0, 'fort': 1, 'church': 2, 'sanctuary': 3, 'works': 4, 'village': 5}


def union_ranges(ranges):
    rs = sorted([list(r) for r in ranges])
    out = [rs[0]]
    for a, b in rs[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def main():
    rdir = sys.argv[1]
    files = sorted(glob.glob(os.path.join(rdir, '[0-9][0-9]-*.json')))
    data = {f: json.load(open(f, encoding='utf-8')) for f in files}

    where = collections.defaultdict(list)
    for f in files:
        for s in data[f].get('new_settlements') or []:
            where[s['id']].append(f)

    merged = 0
    for sid, fs in where.items():
        if len(fs) < 2:
            continue
        recs = []
        for f in fs:
            recs.append((f, next(s for s in data[f]['new_settlements'] if s['id'] == sid)))
        # primary: most finds, then the earliest file
        recs.sort(key=lambda x: (-len(x[1].get('finds') or []), x[0]))
        pf, prim = recs[0]
        others = recs[1:]

        rec = dict(prim)
        rec['name'] = min([r['name'] for _, r in recs], key=len)
        rec['kind'] = min([r['kind'] for _, r in recs], key=lambda t: RANK.get(t, 9))
        subs = [r['sub'] for _, r in recs if r.get('sub')]
        if subs:
            rec['sub'] = max(subs, key=len)
        rec['desc'] = max([r['desc'] for _, r in recs], key=len)
        rec['ranges'] = union_ranges([x for _, r in recs for x in r['ranges']])
        seen = set()
        finds = []
        for _, r in recs:
            for fd in r.get('finds') or []:
                k = fd['n'].strip().lower()
                if k not in seen:
                    seen.add(k)
                    finds.append(fd)
        rec['finds'] = finds
        src = []
        for _, r in recs:
            for u in r.get('sources') or []:
                if u not in src:
                    src.append(u)
        if src:
            rec['sources'] = src

        data[pf]['new_settlements'] = [rec if s['id'] == sid else s
                                       for s in data[pf]['new_settlements']]
        for of, _ in others:
            data[of]['new_settlements'] = [s for s in data[of]['new_settlements']
                                           if s['id'] != sid]
            data[of].setdefault('notes_for_owner', []).append(
                'RECONCILED: %s was also proposed in %s, which now carries the merged '
                'record. This file contributed its finds, ranges and sources to it.'
                % (sid, os.path.basename(pf)))
        print('%-22s %s -> %s  %d finds, ranges %s, kind %s, name %r' % (
            sid, [os.path.basename(f) for f, _ in recs], os.path.basename(pf),
            len(finds), rec['ranges'], rec['kind'], rec['name']))
        merged += 1

    for f in files:
        json.dump(data[f], open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('reconciled %d duplicate settlements across %d files' % (merged, len(files)))


if __name__ == '__main__':
    main()
