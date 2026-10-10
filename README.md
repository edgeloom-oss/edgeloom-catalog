# EdgeLoom Catalog

EdgeLoom Catalog is a reviewable, evidence-backed dataset for relating
smart-home device and protocol support, native platform exposure, and neutral
[SDF](https://www.rfc-editor.org/rfc/rfc9880.html) representations. It is the
data companion to the
[EdgeLoom toolchain](https://github.com/edgeloom-oss/edgeloom).

> **Pilot status:** this repository contains a founder-seeded YRD156 lock pilot
> with pinned SmartThings, zwave-js, and OCF-derived SDF references, HA context,
> and a YRD210 Zigbee comparison from ZHA/Zigbee2MQTT. Every real
> mapping remains `candidate`: none has completed independent review or become
> `verified`. The repository does not publish a GitHub Pages site.

## Inspect a device

The catalog indexes **two explicit device identities**, three feature
mapping sets, six mapping assertions and four external-corroboration records
(nine source observations). These are inventory counts, not supported-device
counts. Inspect [YRD156](catalog/devices/yale-yrd156.yaml) or
[YRD210 PB DB (Zigbee)](catalog/devices/yale-yrd210-pb-db.json), or follow
the core's [five-minute walkthrough](https://github.com/edgeloom-oss/edgeloom/blob/main/docs/catalog-quickstart.md)
to generate a searchable browser, shareable device page and Markdown report.
No account, hub, AI key or physical lock is required.

The browser/report tooling is a **development increment**, not part of the
PyPI 0.2.0 package. Use the exact core pin below. The
[published catalog browser](https://edgeloom-oss.github.io/edgeloom/catalog/)
is a commit-pinned snapshot on the EdgeLoom homepage; a local development
checkout may contain newer records. This repository has no independent Pages
deployment.

## Contribute the evidence behind an implementation

The draft [Device Evidence Bundle](catalog/bundles/README.md) combines a scoped
device identity, official document references, implementation explanations,
reported executions, open questions and review references in a versioned package.
The [YRD210 battery sample](catalog/bundles/yale-yrd210-battery.json) adds an
official manual citation and a proposed observation procedure to the existing
code comparisons. It has no physical-device results or independent reviews.

You can contribute one source, observation, correction or scoped review;
maintainers assemble the bundle. See [how to contribute](docs/bundle-contributions.md)
and the public [format proposal](https://github.com/edgeloom-oss/edgeloom/issues/63).
Draft bundles are a development addition, not yet a published software release
or an automatically updated website snapshot.

## Project boundary

The two repositories have deliberately separate responsibilities:

| Repository | Owns |
| --- | --- |
| [`edgeloom`](https://github.com/edgeloom-oss/edgeloom) | Versioned schemas, validators, CLI behavior, adapters, renderers, and software releases |
| `edgeloom-catalog` | Pinned source manifests, document references, mapping assertions, observations, bundle manifests, review references and contributor credit |

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

The checks validate explicitly typed records and join the six Git sources,
three mapping sets, two device entries and four corroboration records offline.
They also validate document, observation and bundle records under the new draft
contracts. The first bundle cites six records, including one official document
record; no observation record has been added. Existing source/mapping contracts
remain v0.1. The device, corroboration, document, observation and bundle v0.1
contracts are explicitly draft.
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

## Compare without borrowing review

[External corroboration](catalog/corroboration/README.md) compares declarations
with pinned evidence, scoped identity matches, conditions and declared lineage.
HA's Z-Wave JS path is not an independent device authority. ZHA quirk matching
needs a full signature; the chosen Z2M definition matches only a model string.
Code, simulated fixtures and human review are separate evidence types. Neither
multiple sources nor an upstream CI pass promotes a candidate.

The [first comparison slice](catalog/evidence/cross-source-locks-2026-10.md)
keeps battery adaptation layers and command versus observed lock-state fields
visible. No new SDF binding, hardware validation, Homebridge adapter or AI
ingestion is claimed.

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
For a manual or other reference, use the
[source form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-source.yml).
You do not need to write a mapping. Never post PINs, access codes, credentials,
private device/household identifiers, or private telemetry.

Apache License 2.0 applies only to material authored for this repository.
Third-party artifacts retain their own terms, which source manifests record
without relicensing or legal interpretation.
