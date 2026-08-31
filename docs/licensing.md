# Licensing and upstream material

The repository license and an upstream artifact's license answer different
questions. Keep them explicit and separate.

## Repository-authored material

The repository's Apache License 2.0 covers only material authored for and
licensed by this project, such as its original documentation, scripts,
templates, mapping assertions, and synthetic examples. It does not relicense
third-party code, models, profiles, manuals, datasets, trademarks, or other
upstream material.

## Third-party sources

The default catalog pattern is to record:

- the upstream HTTPS Git repository;
- a full immutable commit object ID;
- a repository-relative artifact and license-evidence path;
- the artifact's SHA-256 digest; and
- the upstream license declaration and its locator.

These fields preserve provenance. They do not constitute a legal conclusion,
grant redistribution rights, or imply that EdgeLoom, the contributor, or the
upstream publisher endorses the mapping.

Do not copy an upstream driver, SDF model, profile, manual, dataset, or other
artifact into this repository merely for convenience. Prefer the pinned
reference and digest. If storing third-party bytes becomes necessary, the
contribution must first document applicable terms, required notices,
attribution, modification status, and redistribution authority. Unclear
authority is a reason to keep the record reference-only or defer it.

## Contribution checklist

For every non-synthetic source, a contributor should provide:

1. a pinned upstream location and artifact digest;
2. the license expression reported by the source, preferably as an SPDX
   expression when one is available;
3. a pinned path and optional locator showing where that declaration appears;
4. any attribution or notice obligations relevant to the proposed use; and
5. a clear distinction between quoted upstream facts and original catalog
   analysis.

A manifest's license fields record supplied evidence; validation does not
interpret license compatibility. Reviewers should reject unsupported license
claims and should not treat an absent notice as permission.

Security vulnerabilities belong in the private process described by
[SECURITY.md](../SECURITY.md), not in a public licensing discussion. General
contribution and decision procedures are in
[CONTRIBUTING.md](../CONTRIBUTING.md) and
[GOVERNANCE.md](../GOVERNANCE.md).

This document describes project policy and is not legal advice.
