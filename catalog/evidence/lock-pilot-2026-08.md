# YRD156 lock pilot: candidate evidence summary

This bounded pilot tests whether EdgeLoom's catalog contracts can preserve the
provenance, loss, ambiguity, and gaps found when relating a real SmartThings
Z-Wave lock driver to neutral SDF artifacts. It is a founder-authored submission
by `github:@infinitywings`. It has not completed independent review.

## Candidate records

| Mapping set | Assertions | Candidate finding |
| --- | ---: | --- |
| `smartthings-yrd156-lock-state` | 2 | On the migrated handler path, the strict locked/unlocked subset can be related one-to-one; the complete SmartThings event representation is lossy because it also includes `unknown` and method/user metadata. |
| `smartthings-yrd156-auto-relock-gap` | 2 | Community configuration evidence describes an auto-relock duration, while the pinned base-lock profile does not expose that setting and the bounded lock-status SDF object does not model it. |
| `smartthings-yrd156-access-identities` | 2 | On the migrated handler path, SmartThings user/credential identity metadata has no corresponding field in the bounded lock-code SDF object; value-level correspondence remains ambiguous and no PIN transform is proposed. |

All six assertions belong to mapping sets whose lifecycle is `candidate`. The
classification labels describe individual relationships; they do not advance
the review lifecycle of a record.

## Pinned source inventory

| Source | Commit | Recorded status | License evidence |
| --- | --- | --- | --- |
| [SmartThingsEdgeDrivers](https://github.com/SmartThingsCommunity/SmartThingsEdgeDrivers/tree/6b8a9cf69462d314a7c81b7a709037744d7d788d) | `6b8a9cf69462d314a7c81b7a709037744d7d788d` | `official` for the referenced SmartThings source | Root `LICENSE`, Apache-2.0 |
| [zwave-js](https://github.com/zwave-js/zwave-js/tree/c4c599e1e6a0f6fab1f356f92307b8f94e895e60) | `c4c599e1e6a0f6fab1f356f92307b8f94e895e60` | `community`; not manufacturer or Z-Wave Alliance authority | Root `LICENSE`, MIT |
| [OneDM OCF models](https://github.com/one-data-model/ocf-models/tree/c97d095c239539b8242ceb4f12cf6deaeedb16e2) | `c97d095c239539b8242ceb4f12cf6deaeedb16e2` | `unknown`; hosting does not establish adoption | Root `LICENSE`, BSD-3-Clause |

The OneDM source is described precisely as OCF-derived SDF artifacts hosted by
the One Data Model organization. It is not presented as an adopted OneDM lock
standard. Source manifests contain the path and SHA-256 digest of every
referenced artifact; no third-party source bytes are stored in this repository.

## Verification performed

- Read each artifact from its pinned Git commit and recomputed its SHA-256.
- Recomputed each catalog source-manifest digest and checked every mapping-set
  reference against the exact manifest bytes.
- Checked manifest IDs, artifact IDs, evidence references, node layers, and
  locators across files without executing upstream Lua.
- Validated all source manifests and mapping sets with the exact EdgeLoom core
  commit in `CORE_REVISION`.
- Confirmed the repository contains no real PIN, lock code, user identifier,
  device credential, or vendored upstream artifact.

## Limits and review questions

- No physical YRD156, SmartThings hub, user account, or production deployment
  was tested. Published source behavior is not hardware evidence.
- No pinned record establishes the `SLGA_MIGRATED` state of a real YRD156. The
  lock-state and access-identity records describe the current, post-migration
  handler path only; legacy/default handler behavior remains outside them.
- The zwave-js material is community-maintained configuration evidence.
- The OCF-derived SDF files are independent objects rather than a complete lock
  product profile; syntax or repository placement does not prove semantics,
  interoperability, safety, adoption, or active maintenance.
- Contract version 0.1 has no `driver-source` artifact role, so pinned Lua is
  transparently represented under the generic `evidence` role.
- The current core validator does not recompute cross-file manifest digests or
  resolve artifact IDs across files. Those checks were performed for this
  submission but still require independent reviewer reproduction.
- A reviewer should challenge the migration-path boundary, binary-subset
  boundary, negative evidence for absent auto-relock exposure, and the
  credential/code distinction before considering promotion to `reviewed`.

`Verified` would still mean only that EdgeLoom accepted a bounded record under
its governed process. It would not be a certification, vendor statement,
standards determination, deployment claim, or adoption claim.
