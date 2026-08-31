# Mapping sets

This directory holds EdgeLoom `catalog-mapping-set` documents. Every mapping
set must keep three evidence layers distinct:

1. device or protocol support;
2. native platform exposure; and
3. neutral SDF representation.

Mappings may be `one-to-one`, `lossy`, `ambiguous`, or `unbound`. They must cite
evidence and state limitations. New work starts as `candidate`; the lifecycle
field is not an adoption, certification, compatibility, or standards claim.

Paths in `source_manifests` are resolved from the catalog repository root, and
their SHA-256 values are intended to pin the exact manifest bytes reviewed with
the mapping. At present, the EdgeLoom core validator checks an individual
mapping set and its declared manifest IDs, but it does not open referenced
manifest paths, recompute their digests, or resolve artifact IDs across files.
Reviewers must check those cross-file relationships explicitly until a
directory-level resolver is implemented in EdgeLoom core.

The initial YRD156 records are founder-authored candidates. They deliberately
include loss, ambiguity, and unbound gaps; none is independently reviewed or
verified.
