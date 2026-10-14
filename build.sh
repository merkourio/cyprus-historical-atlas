#!/bin/sh
set -eu

cd "$(dirname "$0")"
mkdir -p dist/i18n
cp index.html cyprus-historical-explorer.html dist/
cp i18n/prose-el.js i18n/prose-tr.js dist/i18n/
