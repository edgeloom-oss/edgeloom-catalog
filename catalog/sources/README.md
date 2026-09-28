# Source manifests

This directory holds EdgeLoom `source-manifest` documents. A
manifest pins one upstream Git repository to a full commit ID and records the
path, SHA-256 digest, media type, evidence layer, artifact role, source maturity,
and declared license evidence for each referenced artifact.

A source manifest is provenance metadata. It does not establish that an
artifact is correct, secure, adopted, authoritative, or legally reusable.
Before adding a canonical manifest, a contributor must document the upstream
source, the immutable revision, the available license evidence, and any
unresolved ambiguity relevant to the proposed use. The catalog does not vendor
or execute upstream driver code.

Use stable lowercase filenames such as `<ecosystem>-<scope>.yaml`. Keep paths
relative to the pinned upstream Git tree, and use digests computed from the
exact bytes at the declared commit.

The current EdgeLoom validator checks each manifest's schema and local semantic
constraints. It does not fetch the upstream repository or independently
confirm the declared artifact bytes, license, or source-maturity statement.

The first non-synthetic manifests pin current SmartThings lock artifacts,
community zwave-js YRD156 configuration evidence, and OCF-derived SDF artifacts
hosted by OneDM. Their presence is not an adoption or endorsement claim.
