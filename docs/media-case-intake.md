# LG webOS state case — source-only candidate

This case adds one integration-family candidate, not a supported-device list
or a test of the founder's television. It contains:

- `catalog/devices/lg-webos-tv-family.json`: explicit family scope, source-declared
  connection context and three features.
- `catalog/sources/ha-webostv-6a811d3.json`: seven inspected files at one immutable
  Home Assistant commit, with SHA-256 and upstream license references.
- `catalog/documents/ha-webostv-documentation-20261010.json`: link-only official
  integration documentation, not a manufacturer manual.
- `catalog/bundles/lg-webos-state-availability.json`: the exact three-record
  package, reasoning, conditions and open questions.

The source-level findings distinguish media-player state, coordinator availability
and the separate screen entity. The integration manifest declares local push,
but the coordinator also has a recovery timer. No wire-level trace or client
dependency execution was performed. The Home Assistant source and documentation
are related publisher evidence, not independent corroboration.

## Reproduce with the pinned core revision

This draft requires the development revision selected in `CORE_REVISION`,
`d7e801d10f02b6effe4d8403ec997913bfd7bb2c`, including the mobile-safe renderer.
Use that exact commit, not the PyPI 0.2.0 package. Its history must remain
reachable when integrating the corresponding core and catalog PRs.

From the reviewed core checkout:

```sh
python -m edgeloom.cli catalog check /path/to/edgeloom-catalog
python -m edgeloom.cli bundle check /path/to/edgeloom-catalog lg-webos-state-availability
python -m edgeloom.cli catalog build /path/to/edgeloom-catalog --output /path/to/new-preview
python -m edgeloom.cli bundle verify /path/to/new-preview/bundles/lg-webos-state-availability/bundle.zip
```

Contract checks are offline; `catalog fetch` is separately opt-in and retrieves
only pinned public source bytes. It never connects to a television.

## What is still needed

1. Exact public model/region, firmware and installed HA integration/version for
   a selected TV; no serial number, IP/MAC, pairing code or household identity.
2. Manufacturer manual appropriate to that exact model and revision, with rights
   recorded. Do not substitute a nearby model or a generic webOS guide.
3. Review of source locators and dependency-level state decoding.
4. A separately agreed read-only observation protocol and a suitable observation
   contract extension. v0.1 observation records cannot describe this IP/family
   subject; no fake Zigbee record should be used.

No device discovery, pairing, screen control, wake, playback or household state
collection is part of this branch. Keep ordinary viewing activity and private
inventory out of public evidence. Source contributors retain upstream credit;
do not list them as EdgeLoom reviewers without an actual scoped review.

## Publication gate

Coordinated core availability, catalog CI and explicit maintainer approval
precede merge and snapshot publication; software releases and outreach remain
separate decisions. The schema remains draft and this evidence remains candidate.
Existing Yale data
and previously frozen packages remain unchanged. New records are AI-assisted,
founder-directed curation, not independent community participation.
