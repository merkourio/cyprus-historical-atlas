#!/usr/bin/env python3
"""Dump/load the data consts of cyprus-historical-explorer.html to/from JSON.

  python3 roundtrip.py dump [atlas-data.json]
  python3 roundtrip.py load [atlas-data.json]

Handles POWERS, ERAS, SETTLEMENTS, NEIGHBOURS. Each const in the HTML is written
as `const NAME = {` / one record per line / `};` at column zero, which is exactly
what this script re-emits, so a dump-load cycle with no edits is a no-op.
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(os.path.dirname(HERE), 'cyprus-historical-explorer.html')
CONSTS = ['POWERS', 'ERAS', 'SETTLEMENTS', 'NEIGHBOURS']


def find_block(lines, name):
    """Return (start_idx, end_idx) inclusive of `const NAME = ...;`."""
    start = next(i for i, l in enumerate(lines) if l.startswith('const %s = ' % name))
    opener = lines[start].rstrip()[-1]
    closer = {'{': '};', '[': '];'}[opener]
    end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == closer)
    return start, end


def parse_block(lines, name):
    start, end = find_block(lines, name)
    body = '\n'.join(lines[start:end + 1])
    body = body[body.index('=') + 1:].rstrip().rstrip(';')
    return json.loads(body)


def emit(name, value):
    j = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
    if isinstance(value, dict):
        rows = ['  %s:%s' % (j(k), j(v)) for k, v in value.items()]
        open_c, close_c = '{', '};'
    else:
        rows = ['  %s' % j(v) for v in value]
        open_c, close_c = '[', '];'
    rows = [r + ',' for r in rows[:-1]] + rows[-1:]
    return ['const %s = %s' % (name, open_c)] + rows + [close_c]


def main():
    mode = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'atlas-data.json')
    lines = open(HTML, encoding='utf-8').read().split('\n')

    if mode == 'dump':
        data = {n: parse_block(lines, n) for n in CONSTS}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print('dumped -> %s' % path)
        for n in CONSTS:
            print('  %-12s %d' % (n, len(data[n])))
        print('  finds        %d' % sum(len(s.get('finds', [])) for s in data['SETTLEMENTS']))
        return

    if mode == 'load':
        data = json.load(open(path, encoding='utf-8'))
        # rewrite from the bottom up so earlier line numbers stay valid
        spans = sorted(((find_block(lines, n), n) for n in CONSTS), reverse=True)
        for (start, end), n in spans:
            lines[start:end + 1] = emit(n, data[n])
        out = '\n'.join(lines)
        open(HTML, 'w', encoding='utf-8').write(out)
        print('loaded %s -> %s' % (path, HTML))
        for n in CONSTS:
            print('  %-12s %d' % (n, len(data[n])))
        print('  finds        %d' % sum(len(s.get('finds', [])) for s in data['SETTLEMENTS']))
        return

    sys.exit('usage: roundtrip.py dump|load [json]')


if __name__ == '__main__':
    main()
