# Device navigation entries

These records supply explicit device identity and human-authored feature
navigation for the generated browser. They consume the core's draft
`catalog-device` v0.1 contract rather than changing existing mapping contracts.

The YRD156 entry groups three existing candidate mapping sets. Associations
are source-grounded declarations, not device coverage, compatibility, or patch
availability. The YRD210 Zigbee entry joins candidate-only corroboration, not
SDF mappings. Features can reference mapping sets, corroboration records, or
both, but cannot be empty. Corroboration joins are checked against the exact
device and feature IDs; partial upstream identity matches remain visible.
Firmware and handler-path uncertainty remain explicit.

An empty `hardware_evidence` list means no hardware observation is recorded.
Future links would be reported observations, not automatically authenticated
tests or an automatic promotion of mapping review lifecycle.
