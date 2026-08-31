# EdgeLoom Catalog

EdgeLoom Catalog is a reviewable, evidence-backed dataset for relating
smart-home device and protocol support, native platform exposure, and neutral
[SDF](https://www.rfc-editor.org/rfc/rfc9880.html) representations. It is the
data companion to the
[EdgeLoom toolchain](https://github.com/edgeloom-oss/edgeloom).

> **Bootstrap status:** this repository is limited to repository scaffolding
> and synthetic examples. It contains no real pilot catalog data or verified
> mappings, and it does not publish a GitHub Pages site.

## Project boundary

The two repositories have deliberately separate responsibilities:

| Repository | Owns |
| --- | --- |
| [`edgeloom`](https://github.com/edgeloom-oss/edgeloom) | Versioned schemas, validators, CLI behavior, adapters, renderers, and software releases |
| `edgeloom-catalog` | Pinned source manifests, catalog-authored mapping assertions, evidence references, review records, and any future generated catalog view |

The catalog consumes contracts released by the core toolchain; it does not
fork or redefine them locally. See [Repository layout](docs/repository-layout.md)
for the intended data flow.

## Validate the bootstrap

CI runs EdgeLoom core from the exact commit recorded in
[`CORE_REVISION`](CORE_REVISION) with the hash-locked Linux runtime in
[`requirements-ci.txt`](requirements-ci.txt), then validates only files in this
checkout. On Linux x86_64, reproduce the CI check with CPython 3.11:

```bash
git clone https://github.com/edgeloom-oss/edgeloom.git .edgeloom-core
git -C .edgeloom-core checkout "$(cat CORE_REVISION)"
python3.11 -m venv .venv
.venv/bin/python -m pip install --no-deps --only-binary=:all: \
  --require-hashes -r requirements-ci.txt
PYTHON_BIN="$PWD/.venv/bin/python" ./scripts/validate-catalog.sh
```

The final line should report two explicitly typed documents and no failures.
The shared script also rejects unrecognized structured files, symbolic links,
and documents over 1 MiB before invoking the pinned core contracts. It does not
fetch or execute any artifact named by a source manifest. Cross-file digest and
artifact reference checks remain part of human review until the core toolchain
adds a directory-level resolver.

## What this catalog is not

This project is not an authoritative registry, a standards body, a
certification program, a vendor approval process, or an adoption directory.
A record does not imply that its source, platform, manufacturer, or standards
community endorses EdgeLoom. A mapping describes a bounded, cited observation,
including loss and uncertainty; it does not establish universal compatibility.

## Provenance and review

Catalog records prefer references to upstream material pinned by repository,
full commit identifier, repository-relative path, and SHA-256 digest. The
catalog does not mirror upstream artifacts by default. This keeps provenance
visible without presenting a mutable copy as authoritative.

Two independent axes prevent status from becoming an endorsement:

- **Source maturity** records context about an upstream artifact, such as
  `official`, `community`, `experimental`, `draft`, `deprecated`, or `unknown`.
- **Review lifecycle** records the catalog's treatment of a mapping:
  `candidate`, `reviewed`, `verified`, or `deprecated`.

Neither value is authenticated by schema validation alone. Review trust comes
from the governed repository history. The precise meanings and promotion rules
are documented in [Status and review](docs/status-and-review.md).

## Contributing and reporting

Before proposing a source or mapping, read:

- [Contributing](CONTRIBUTING.md) for contribution and validation expectations;
- [Governance](GOVERNANCE.md) for decisions, review roles, and conflicts of
  interest;
- [Security](SECURITY.md) for private vulnerability reporting; and
- [Licensing](docs/licensing.md) for upstream attribution and redistribution
  boundaries.

Apache License 2.0 applies only to material authored for this repository.
Third-party artifacts retain their own terms, which source manifests record
without relicensing or legal interpretation.
