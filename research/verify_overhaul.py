"""Verify preserved atlas evidence and characterise its weighted time mapping.

Usage: python3 research/verify_overhaul.py [baseline HTML]
The baseline is optional; pass it to verify every historical/geographic payload.
Browser interaction and responsive checks are recorded separately.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from atlas import HTML, load

TARGET = Path(HTML)
PAYLOADS = ['POWERS', 'ERAS', 'SETTLEMENTS', 'NEIGHBOURS', 'EXTENTS', 'REGIONS',
            'LAND_TOPO', 'CYPRUS_RING']


def main():
    current = {key: load(key) for key in PAYLOADS}
    if len(sys.argv) > 1:
        baseline = {key: load(key, sys.argv[1]) for key in PAYLOADS}
        assert current == baseline, 'Historical or geographic payload changed'
        print('Historical and geographic payloads unchanged: 8/8')
    assert len(current['ERAS']) == 16
    assert len(current['SETTLEMENTS']) == 131
    assert sum(len(st['finds']) for st in current['SETTLEMENTS']) == 1145
    assert TARGET.stat().st_size < 1_500_000, 'HTML exceeds artifact budget'
    text = TARGET.read_text()
    assert 'name="viewport"' in text
    scripts = re.findall(r'<script>([\s\S]*?)</script>', text)
    with tempfile.TemporaryDirectory() as tmp:
        for i, script in enumerate(scripts):
            path = Path(tmp) / f'inline-{i}.js'
            path.write_text(script)
            subprocess.run(['node', '--check', str(path)], check=True)
        # Use the shipped date-mapping functions with real era data. Occupation
        # and year-zero display semantics remain unchanged in the evidence model.
        scale = text.split('/* ---------- SCALE ---------- */')[1].split('const I18N')[0]
        path = Path(tmp) / 'dates.js'
        path.write_text('const ERAS=' + json.dumps(current['ERAS']) + ';\n' + scale + '''
const assert = require('node:assert/strict');
for (const era of ERAS) {
  for (const year of [era.start, era.end, (era.start+era.end)/2]) {
    assert.ok(Math.abs(tToYear(yearToT(year))-year)<0.000001);
  }
}
assert.equal(yearToT(Y_MIN-1),0);
assert.equal(yearToT(Y_MAX+1),1);
assert.equal(tToYear(-1),Y_MIN);
assert.equal(tToYear(2),Y_MAX);
assert.equal(eraOf(-58).id,'roman');
assert.equal(eraOf(330).id,'byzantine');
assert.equal(eraOf(1960).id,'republic');
console.log('Weighted timeline boundary and round-trip checks passed');
''')
        subprocess.run(['node', str(path)], check=True)
    print(f'16 eras / 131 sites / 1,145 finds; HTML {TARGET.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
