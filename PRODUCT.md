# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Educated general readers exploring Cyprus through places and historical periods, as described in the existing research brief and the implementation plan the owner asked to execute. Research and travel use are secondary possibilities, not confirmed primary audiences.

## Product Purpose

Make it possible to choose a date, understand who controlled Cyprus, inspect settlements and archaeological finds, and consult the evidence behind the account.

## Operating Context

An interactive atlas published through GitHub Pages and distributed as a single HTML file. A rotatable orthographic globe links a weighted historical timeline, period narratives, settlement records, finds and sources.

## Capabilities and Constraints

Preserve the 16 eras, 131 settlement records, 1,145 finds, coordinates, occupation ranges, historical extents, provenance and date semantics. Keep the custom D3 canvas/SVG globe and one-file HTML delivery. Libraries and webfonts currently load from external CDNs; single-file does not mean offline. Keep English, Greek and Turkish interface support; historical prose remains English. The implementation plan preserves these contracts and proposes a 1,500,000-byte artifact ceiling.

Do not introduce historical border claims or content corrections through visual styling. Full-text search, autoplay, guided routes and prose translation are separate roadmap work.

## Brand Commitments

Existing product name: Cyprus Historical Explorer. The owner requested the detailed Impeccable visual-overhaul plan and then instructed its execution. The plan's contemporary scholarly-atlas direction is the implementation starting point; final visual review remains open.

## Evidence on Hand

`cyprus-historical-explorer.html`, `README.md`, `research/BRIEF.md`, `research/ROADMAP.md`, research JSON and per-record sources. Baseline repository commit: `6680e8cc614ab586c9831f97972c2713df5963e3`.

## Product Principles

- Preserve the relationship between selected dates and approximate historical evidence.
- Keep map exploration and reading in a coherent workflow.
- Make all settlement records reachable without requiring spatial interaction.
- Preserve reading context when time, selection and filters change.

## Accessibility & Inclusion

The accepted implementation plan targets WCAG 2.2 AA, keyboard access, reduced motion, a complete text alternative to map exploration, readable mobile controls and honest language fallback.
