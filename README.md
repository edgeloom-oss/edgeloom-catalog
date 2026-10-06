# EdgeLoom Catalog

EdgeLoom Catalog is a reviewable, evidence-backed dataset for relating
smart-home device and protocol support, native platform exposure, and neutral
[SDF](https://www.rfc-editor.org/rfc/rfc9880.html) representations. It is the
data companion to the
[EdgeLoom toolchain](https://github.com/edgeloom-oss/edgeloom).

> **Pilot status:** this repository contains a founder-seeded YRD156 lock pilot
> with pinned SmartThings, zwave-js, and OCF-derived SDF references. Every real
> mapping remains `candidate`: none has completed independent review or become
> `verified`. The repository does not publish a GitHub Pages site.

## Inspect a device

The first device entry groups **one Yale YRD156 model**, three feature mapping
sets and six candidate assertions. Inspect
[`catalog/devices/yale-yrd156.yaml`](catalog/devices/yale-yrd156.yaml) or follow
the core's [five-minute walkthrough](https://github.com/edgeloom-oss/edgeloom/blob/codex/catalog-usable-evidence/docs/catalog-quickstart.md)
to generate a searchable browser, shareable device page and Markdown report.
No account, hub, AI key or physical lock is required.

The browser/report tooling is a **development increment**, not part of the
PyPI 0.2.0 package. Use the exact core pin below. A generated snapshot is
prepared for the existing EdgeLoom homepage; publication still requires
maintainer approval. This repository has no independent Pages deployment.

## Project boundary

The two repositories have deliberately separate responsibilities:

| Repository | Owns |
| --- | --- |
| [`edgeloom`](https://github.com/edgeloom-oss/edgeloom) | Versioned schemas, validators, CLI behavior, adapters, renderers, and software releases |
| `edgeloom-catalog` | Pinned source manifests, catalog-authored mapping assertions, evidence references, review records, and any future generated catalog view |

The catalog consumes versioned contracts from an exact core pin; it does not
fork or redefine them locally. See [Repository layout](docs/repository-layout.md)
for the intended data flow.

## Validate the catalog

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

For the current tree, the checks should report nine explicitly typed documents
and a successful offline join of three sources, three mapping sets and one
device entry. Existing source/mapping contracts remain v0.1; the new
`catalog-device` v0.1 navigation contract is explicitly draft.
The shared script also rejects unrecognized structured files, symbolic links,
and documents over 1 MiB before invoking the pinned core contracts. It does not
fetch or execute any artifact named by a source manifest. The pinned core also
recomputes referenced manifest digests and checks artifact IDs, mapping IDs and
device protocol associations. Passing checks never promotes a record's review
lifecycle or authenticates device identity, interpretation or hardware behavior.

For a platform-neutral local report after installing the pinned core:

```bash
edgeloom catalog check .
edgeloom catalog build . --output _site
# Optional explicit network step; cached third-party bytes are not committed:
edgeloom catalog fetch . --cache .cache/source-bytes
edgeloom catalog build . --cache .cache/source-bytes --output _site
```

CI builds twice without fetching upstream material and compares every output
byte. Source-byte, locator, review and hardware-evidence states remain separate.
Strict JSON pointers may resolve; selectors, Lua and JSON5 need manual review.

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

The initial candidate findings, provenance inventory, and verification limits
are summarized in the [YRD156 lock pilot](catalog/evidence/lock-pilot-2026-08.md).

## Contributing and reporting

Before proposing a source or mapping, read:

- [Contributing](CONTRIBUTING.md) for contribution and validation expectations;
- [Governance](GOVERNANCE.md) for decisions, review roles, and conflicts of
  interest;
- [Security](SECURITY.md) for private vulnerability reporting; and
- [Licensing](docs/licensing.md) for upstream attribution and redistribution
  boundaries.

For a device observation or request, use the
[simple feedback form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-observation.yml).
You do not need to write a mapping. Never post PINs, access codes, credentials,
private device/household identifiers, or private telemetry.

Apache License 2.0 applies only to material authored for this repository.
Third-party artifacts retain their own terms, which source manifests record
without relicensing or legal interpretation.
