# LG webOS state case — private review branch

This branch adds one integration-family candidate, not a supported-device list
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

## Reproduce after reviewing the proposed core revision

This draft requires the corresponding unpublished core branch. `CORE_REVISION`
is pinned to local implementation commit `8ef52b7c7ff4c664e44cf30d47077e01908f14d0`. That commit must become
publicly accessible through a separately approved push/review before normal
remote catalog CI or another contributor can reproduce it by fetching GitHub.
Do not merge this catalog increment against the old core pin.

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

Draft schema review, coordinated core availability, catalog CI and PI approval
precede any merge, hosting update, public issue or outreach. Existing Yale data
and previously frozen packages remain unchanged. New records are AI-assisted,
founder-directed curation, not independent community participation.
