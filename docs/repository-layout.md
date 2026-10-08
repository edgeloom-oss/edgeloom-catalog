# Repository layout

EdgeLoom separates executable tooling from reviewable catalog data. The
[core repository](https://github.com/edgeloom-oss/edgeloom) defines and releases
the schemas, validators, CLI, adapters, and renderers. This repository stores
records that conform to those contracts.

## Bootstrap layout

```text
.
├── catalog/
│   ├── sources/       # pinned source manifests
│   ├── mappings/      # mapping sets
│   ├── devices/       # explicit identity and feature navigation (draft contract)
│   ├── corroboration/ # candidate cross-source observations and declared lineage
│   ├── evidence/      # repository-authored evidence records
│   └── reviews/       # governed review records
├── examples/          # synthetic, non-production examples
├── docs/              # policy and contributor documentation
├── scripts/           # repository containment around the pinned core CLI
└── .github/           # contribution templates and CI configuration
```

The versioned schema definitions remain in the core repository. Catalog
validation selects the explicit EdgeLoom revision in
[`CORE_REVISION`](../CORE_REVISION) rather than copying and modifying those
definitions here. The repository script supplies file-location, type, size, and
symlink checks; the pinned core owns schemas, cross-record reference/digest
checks, fetch behavior and report rendering. No contract is redefined here.

## Record flow

1. A source manifest identifies an HTTPS Git repository, a full commit object
   ID, a repository-relative artifact path, and a SHA-256 digest.
2. A mapping set cites those manifests and records relationships, evidence,
   semantic loss, uncertainty, and limitations.
3. A device entry associates explicit protocol identity and readable feature
   questions with mapping-set IDs. Associations are declarations, not support.
4. Independent review may advance the mapping through the lifecycle described
   in [Status and review](status-and-review.md).
5. The core renderer produces deterministic JSON, Markdown and static HTML,
   including candidate records with their status and limitations visible.
   Generated output is not a second source of truth. The homepage embeds a
   commit-pinned snapshot; it does not query mutable upstream APIs in a browser.

Paths in mapping records are resolved from the catalog repository root. They
must not depend on a contributor's home directory, checkout location, branch
name, or unpinned network content.

## Upstream material

The normal contribution is a reference plus immutable commit and digest, not a
copy of an upstream driver, model, profile, manual, or dataset. If a future use
case requires storing third-party bytes, redistribution authority and
attribution must be documented before those bytes enter the repository. See
[Licensing](licensing.md).

The catalog now includes a bounded founder-seeded YRD156 candidate pilot in
addition to synthetic examples. No real mapping has completed independent
review or become verified, and an independent Pages site remains outside the
current repository contents.
