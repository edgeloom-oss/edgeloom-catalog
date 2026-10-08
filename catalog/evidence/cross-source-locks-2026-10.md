# Cross-source lock evidence — 6 October 2026

This review-branch slice adds four candidate corroboration records to the
existing YRD156 mappings and one distinct Zigbee identity, Yale / YRD210 PB DB.
There are two indexed identities, three mapping sets, six mapping assertions,
four corroboration records and nine source observations. Counts do not imply
supported-device coverage or independent review. No existing mapping was
promoted; hardware evidence remains empty.

Canonical findings and conditions live in the
[corroboration records](../corroboration/README.md), not duplicated here.
The new manifests pin HA core `067f88281665776424fbb4826697c46d5e7a6837`,
ZHA handlers `d6fcec59eff9f63f154723500be9378be926d927`, and Z2M converters
`5750b44559405203b202e0f5539dc0d6f46f1c8d`, including selected license bytes.
Upstream content is referenced, not committed or executed.

The principal interpretation limits are:

- HA's generic path depends on the Z-Wave JS stack; the lineage edge is not an
  exact installed-version lock or second device attestation.
- The HA missing-value test uses a Schlage fixture. It is source-inspected,
  not run by this project and not a YRD156 test.
- ZHA's exact signature includes endpoints and clusters; Z2M's selected entry
  has a model-only matcher and descriptive vendor metadata.
- Battery transformations occur at different layers. No claim is made about
  a final HA percentage until the downstream entity path and raw/final
  observations are established.
- No new SDF mapping, Homebridge ingestion, AI extraction, hardware pass or
  independent review is established by this slice.

Offline CI checks contracts, source-manifest digests, joins and acyclic declared
lineage, then builds twice and compares bytes. Optional explicit fetch/build
can match source bytes and locate strict JSON pointers; Python/TypeScript
selectors remain manual-review. Publication and release require separate
maintainer decisions after the stacked PRs are accepted.
