# Candidate external corroboration

These original records compare selected pinned upstream declarations. They
are not upstream redistribution, independent EdgeLoom reviews, hardware tests,
same-layer mapping edges or certification. Use the core's draft
`catalog-corroboration` v0.1 contract at `CORE_REVISION`; it is not in PyPI 0.2.0.

Each record binds to one explicit device feature, pins its source manifest
bytes, preserves conditions and competing observations, and declares a bounded
source-family dependency graph. A platform-generic path cannot claim a device
identity match. A model-only match is visibly weaker than a full signature or
protocol tuple. The checks validate declarations, not their meaning.

Relationship labels (`supports`, `conflicts`, `context`, `unresolved`) are
curator interpretations. No voting, independent-source score or automatic
promotion occurs. The sidecar accepts only `candidate` with no reviewer
credits; a proper review follows [governance](../../GOVERNANCE.md).

The first records cover:

- [YRD156 configuration paths](yrd156-ha-configuration-path.json): community
  parameter imports versus generic HA actions; Door Lock CC equivalence remains
  unresolved, and shared backend ancestry is explicit.
- [YRD156 unknown-state context](yrd156-ha-unknown-state.json): generic HA code
  plus a clearly identified Schlage simulation fixture, not Yale hardware.
- [YRD210 battery adaptation](yrd210-battery-normalization.json): ZHA's cluster
  doubling versus Z2M's skipped halving; downstream entity values are not tested.
- [YRD210 lock exposure](yrd210-lock-exposure.json): cluster presence versus
  declared command/state and actual-state fields; no SDF binding is asserted.

To contribute: pin a merged source and its helpers/license, state exactly what
its matcher selects, preserve dependency ancestry and unresolved paths, link
the sidecar from its device feature, then run `catalog check` and deterministic
builds. Fetch is explicit and bounded; no upstream code is imported/executed.
Do not submit real PINs, credentials, private identifiers or telemetry.
