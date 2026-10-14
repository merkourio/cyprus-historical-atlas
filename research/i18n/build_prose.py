#!/usr/bin/env python3
"""Build the lazy-loaded prose packs i18n/prose-<lang>.js from translator output.

  python3 research/i18n/build_prose.py

Reads research/i18n/prose/out/cNN.<lang>.json ({english: translation}) and keeps only
keys that are still current English strings in the page (via roundtrip-style parsing),
so stale translations of edited text drop out and fall back to English. Reports
coverage and strings whose digits differ between English and translation.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
from roundtrip import parse_block  # noqa: E402

LANGS = ['el', 'tr']


def current_strings():
    lines = open(os.path.join(ROOT, 'cyprus-historical-explorer.html'), encoding='utf-8').read().split('\n')
    d = {n: parse_block(lines, n) for n in ['POWERS', 'ERAS', 'SETTLEMENTS']}
    out = set()
    for pid, p in d['POWERS'].items():
        out.add(p['desc'])
        for r in p.get('rulers', []):
            out.update([r['n'], r['d'], r['t'], pid + '|' + r['n']])
    for e in d['ERAS']:
        out.update(t for _, t in e['events'])
        out.add(e['region'])
        out.update((e.get('life') or {}).values())
        out.update(r['n'] for r in e.get('reading', []))
    for s in d['SETTLEMENTS']:
        out.add(s['desc'])
        for f in s['finds']:
            out.update([f['n'], f['p'], f['t'], f['w']])
    return {x for x in out if isinstance(x, str) and x.strip()}


def digits(s):
    return sorted(re.findall(r'\d+', s.replace(',', '').replace('.', '')))


def main():
    cur = current_strings()
    os.makedirs(os.path.join(ROOT, 'i18n'), exist_ok=True)
    for lang in LANGS:
        pack = {}
        for f in sorted(glob.glob(os.path.join(HERE, 'prose', 'out', '*.%s.json' % lang))):
            pack.update(json.load(open(f, encoding='utf-8')))
        # hand-made fixes, including power-qualified ruler names ("lusignan|John I")
        ov = os.path.join(HERE, 'prose', 'overrides.json')
        if os.path.exists(ov):
            pack.update(json.load(open(ov, encoding='utf-8')).get(lang, {}))
        pack = {k: v.strip() for k, v in pack.items()
                if k in cur and isinstance(v, str) and v.strip() and '<' not in v}
        odd = [k for k, v in pack.items() if digits(k) != digits(v)]
        dest = os.path.join(ROOT, 'i18n', 'prose-%s.js' % lang)
        body = json.dumps(pack, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
        with open(dest, 'w', encoding='utf-8') as fh:
            fh.write('/* Cyprus Historical Explorer: %s prose, keyed by the English text. '
                     'Built by research/i18n/build_prose.py. */\n' % lang)
            fh.write('window.CY_PROSE=window.CY_PROSE||{};window.CY_PROSE[%s]=%s;\n' % (json.dumps(lang), body))
        cur_n = len([k for k in cur if '|' not in k])
        print('%s: %d / %d strings (%.1f%%), %d bytes, %d with differing digits'
              % (lang, len(pack), cur_n, 100 * len(pack) / cur_n, os.path.getsize(dest), len(odd)))
        if '-v' in sys.argv:
            for k in odd[:40]:
                print('   ', k[:90], '|', pack[k][:90])


if __name__ == '__main__':
    main()
