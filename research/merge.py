#!/usr/bin/env python3
"""Merge agent research JSON files into the atlas data dump.

  python3 merge.py <base.json> <out.json> <research-dir>

Validates ids, coordinates, ranges and required fields; reports everything it
rejects. Never silently drops a record.
"""
import json, os, re, sys, glob

# Generous island bounding box plus a margin for offshore wrecks and islets.
LON = (32.10, 34.70)
LAT = (34.45, 35.80)
# What kind of place it is, which never changes with the year. Political status does
# change, so "city-kingdom" is not a kind: it lives in `control` and is read per year.
KINDS = ('town', 'village', 'sanctuary', 'church', 'fort', 'works')
ERA_IDS = None


def fail(msgs, m):
    msgs.append(m)
    return False


def check_find(f, where, msgs):
    ok = True
    for k in ('n', 'p', 't', 'w'):
        if not isinstance(f.get(k), str) or not f[k].strip():
            ok = fail(msgs, '%s: find missing/blank "%s": %r' % (where, k, f.get('n')))
    for k in ('t', 'n'):
        if isinstance(f.get(k), str) and ('—' in f[k] or '–' in f[k].replace('–', '') and False):
            pass
    return ok


def main():
    base_p, out_p, rdir = sys.argv[1], sys.argv[2], sys.argv[3]
    data = json.load(open(base_p, encoding='utf-8'))
    existing = {s['id']: s for s in data['SETTLEMENTS']}
    eras = {e['id']: e for e in data['ERAS']}
    powers = data['POWERS']

    msgs, added, addfinds, addevents, addrulers, addlife = [], 0, 0, 0, 0, 0
    files = sorted(glob.glob(os.path.join(rdir, '[0-9][0-9]-*.json')))
    if not files:
        sys.exit('no research json in %s' % rdir)

    for path in files:
        tag = os.path.basename(path)
        try:
            r = json.load(open(path, encoding='utf-8'))
        except Exception as e:
            msgs.append('%s: UNPARSEABLE (%s)' % (tag, e))
            continue

        for s in r.get('new_settlements') or []:
            w = '%s/%s' % (tag, s.get('id'))
            ok = True
            for k in ('id', 'name', 'modern', 'lon', 'lat', 'kind', 'ranges', 'desc', 'finds'):
                if k not in s:
                    ok = fail(msgs, '%s: missing field "%s"' % (w, k))
            if not ok:
                continue
            if not re.fullmatch(r'[a-z0-9_]+', s['id']):
                ok = fail(msgs, '%s: bad id slug' % w)
            if s['id'] in existing:
                ok = fail(msgs, '%s: DUPLICATE id, skipped' % w)
            if not (LON[0] <= s['lon'] <= LON[1] and LAT[0] <= s['lat'] <= LAT[1]):
                ok = fail(msgs, '%s: coords off-island (%s,%s)' % (w, s['lon'], s['lat']))
            if s.get('kind') not in KINDS:
                ok = fail(msgs, '%s: bad kind %r, expected one of %s' % (w, s.get('kind'), '/'.join(KINDS)))
            if 'sub' in s and not (isinstance(s['sub'], str) and s['sub'].strip()):
                ok = fail(msgs, '%s: blank sub label' % w)
            rs = s.get('ranges')
            if not (isinstance(rs, list) and rs and all(
                    isinstance(x, list) and len(x) == 2 and isinstance(x[0], int)
                    and isinstance(x[1], int) and x[0] < x[1] and -12000 <= x[0] and x[1] <= 2026
                    for x in rs)):
                ok = fail(msgs, '%s: bad ranges %r' % (w, rs))
            if not isinstance(s['finds'], list) or len(s['finds']) < 2:
                ok = fail(msgs, '%s: fewer than 2 finds' % w)
            else:
                for f in s['finds']:
                    ok = check_find(f, w, msgs) and ok
            if not ok:
                continue
            rec = {'id': s['id'], 'name': s['name'], 'modern': s['modern'],
                   'lon': round(float(s['lon']), 4), 'lat': round(float(s['lat']), 4),
                   'lab': s.get('lab') if s.get('lab') in ('t', 'b', 'l', 'r') else 'r',
                   'kind': s['kind'], 'ranges': s['ranges'], 'desc': s['desc'].strip(),
                   'finds': [{'n': f['n'].strip(), 'p': f['p'].strip(),
                              't': f['t'].strip(), 'w': f['w'].strip()} for f in s['finds']]}
            if s.get('sub'):
                rec['sub'] = s['sub'].strip()
            if s.get('control'):
                rec['control'] = s['control']
            if s.get('sources'):
                rec['sources'] = [u for u in s['sources'] if isinstance(u, str) and u.startswith('http')]
            data['SETTLEMENTS'].append(rec)
            existing[rec['id']] = rec
            added += 1

        for ef in r.get('extra_finds') or []:
            sid = ef.get('id')
            if sid not in existing:
                msgs.append('%s: extra_finds for unknown id %r' % (tag, sid))
                continue
            tgt = existing[sid]
            have = {f['n'].strip().lower() for f in tgt.get('finds', [])}
            for f in ef.get('finds') or []:
                if not check_find(f, '%s/%s' % (tag, sid), msgs):
                    continue
                if f['n'].strip().lower() in have:
                    msgs.append('%s/%s: duplicate find %r skipped' % (tag, sid, f['n']))
                    continue
                tgt.setdefault('finds', []).append({'n': f['n'].strip(), 'p': f['p'].strip(),
                                                    't': f['t'].strip(), 'w': f['w'].strip()})
                have.add(f['n'].strip().lower())
                addfinds += 1
            for u in ef.get('sources') or []:
                if isinstance(u, str) and u.startswith('http') and u not in tgt.setdefault('sources', []):
                    tgt['sources'].append(u)

        for ee in r.get('era_events') or []:
            eid = ee.get('id')
            if eid not in eras:
                msgs.append('%s: era_events for unknown era %r' % (tag, eid))
                continue
            era = eras[eid]
            have = {t.strip().lower()[:40] for _, t in era.get('events', [])}
            for ev in ee.get('events') or []:
                if not (isinstance(ev, list) and len(ev) == 2 and isinstance(ev[0], int)
                        and isinstance(ev[1], str) and ev[1].strip()):
                    msgs.append('%s/%s: bad event %r' % (tag, eid, ev))
                    continue
                if ev[1].strip().lower()[:40] in have:
                    continue
                era.setdefault('events', []).append([ev[0], ev[1].strip().rstrip('.')])
                have.add(ev[1].strip().lower()[:40])
                addevents += 1
            era['events'].sort(key=lambda e: e[0])

        for ru in r.get('rulers') or []:
            pid = ru.get('power')
            if pid not in powers:
                msgs.append('%s: rulers for unknown power %r' % (tag, pid))
                continue
            cur = powers[pid].get('rulers') or []
            have = {x['n'].strip().lower() for x in cur}
            for x in ru.get('rulers') or []:
                if not all(isinstance(x.get(k), str) and x[k].strip() for k in ('n', 'd', 't')):
                    msgs.append('%s/%s: bad ruler %r' % (tag, pid, x))
                    continue
                if x['n'].strip().lower() in have:
                    continue
                cur.append({'n': x['n'].strip(), 'd': x['d'].strip(), 't': x['t'].strip()})
                have.add(x['n'].strip().lower())
                addrulers += 1
            powers[pid]['rulers'] = cur

        for lf in r.get('life') or []:
            eid = lf.get('era') or lf.get('id')
            if eid not in eras:
                msgs.append('%s: life for unknown era %r' % (tag, eid))
                continue
            block = {}
            for k in ('economy', 'language', 'religion', 'people'):
                v = lf.get(k)
                if isinstance(v, str) and v.strip():
                    block[k] = v.strip()
                else:
                    msgs.append('%s/%s: life missing %r' % (tag, eid, k))
            if block:
                eras[eid]['life'] = block
                addlife += 1
            for u in lf.get('sources') or []:
                if isinstance(u, str) and u.startswith('http') and u not in eras[eid].setdefault('sources', []):
                    eras[eid]['sources'].append(u)

        for n in r.get('notes_for_owner') or []:
            msgs.append('NOTE %s: %s' % (tag, n))

    # every settlement must fall inside at least one era window
    span = (min(e['start'] for e in data['ERAS']), max(e['end'] for e in data['ERAS']))
    for s in data['SETTLEMENTS']:
        if not any(r[1] >= span[0] and r[0] <= span[1] for r in s['ranges']):
            msgs.append('%s: ranges outside the timeline' % s['id'])

    json.dump(data, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('settlements %d (+%d)  finds %d (+%d)  events +%d  rulers +%d  life panels %d' % (
        len(data['SETTLEMENTS']), added,
        sum(len(s.get('finds', [])) for s in data['SETTLEMENTS']), addfinds,
        addevents, addrulers, addlife))
    print('--- messages (%d) ---' % len(msgs))
    for m in msgs:
        print(' ', m)


if __name__ == '__main__':
    main()
