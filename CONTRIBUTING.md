# Contributing

Thank you for helping build the EdgeLoom Catalog. Contributions may include
source manifests, document citations, implementation explanations, reported
observations, evidence-backed mappings, corrections, independent reviews,
documentation, validation improvements, and issue triage. Start with the
[bundle contribution guide](docs/bundle-contributions.md) to contribute one
useful piece of evidence without authoring a mapping.

This repository records claims about upstream artifacts; it does not distribute
drivers, certify devices, or make a platform or standard authoritative. Changes
to the EdgeLoom CLI, schemas, or validators belong in the
[`edgeloom`](https://github.com/edgeloom-oss/edgeloom) repository.

## Choose the right contribution

- Use the **mapping submission** form for a new candidate mapping set.
- Use the **source update** form to pin a new upstream revision or replace a
  source manifest.
- Use the **device document or source** form for an official manual, vendor
  page or other implementation reference. State exact-model, family or
  unresolved applicability.
- Use the **correction** form when an accepted record is factually wrong,
  incomplete, stale, or no longer reproducible.
- Use the **independent review** form to volunteer a review or record review
  evidence before proposing a lifecycle change.
- Use the **device observation or request** form to report what your driver or
  device does, or suggest a model. No mapping authoring is required.
- A source-only comparison can be a candidate
  [corroboration sidecar](catalog/corroboration/README.md), not an independent
  review. Use the correction/observation form to suggest one.
- Report vulnerabilities privately through [SECURITY.md](SECURITY.md), never
  in a public issue or pull request.

Search existing issues and pull requests before opening a new one. A focused
correction is preferable to an unrelated collection of catalog changes.

## Evidence and source requirements

Every submission must make its provenance and limitations reviewable:

1. Pin Git sources to an immutable, full 40-character commit ID. Do not use a
   branch or tag as the recorded revision.
2. Record the repository-relative path and SHA-256 digest of every artifact
   used as evidence.
3. Cite license evidence from the same pinned tree. A license field is a source
   assertion, not a legal determination by EdgeLoom.
4. Separate device/protocol support, native platform exposure, and neutral SDF
   representation. Do not infer one layer from another without evidence.
5. Classify mappings as `one-to-one`, `lossy`, `ambiguous`, or `unbound` and
   state known limitations. Record the relevant loss dimension or unbound
   reason when required by the schema.
6. Use `unknown` for upstream maturity when the pinned source does not support
   a stronger claim. Names such as `official`, `community`, and `experimental`
   describe the source, not EdgeLoom adoption or endorsement.

Manuals and mutable web pages use the draft `document-source` contract with
publisher, version, access date, applicability, precise locations and rights.
Use `link-only` when bytes were not inspected; `digest-recorded` records an
inspected file without claiming it is archived. Open an issue for sources the
contracts cannot express. Do not manufacture provenance to make a record validate.

Canonical YAML and JSON records must be no larger than 1 MiB each. Put source
manifests in `catalog/sources/`, mapping sets in `catalog/mappings/`, and
device entries in `catalog/devices/`, external comparisons in
`catalog/corroboration/`, document metadata in `catalog/documents/`, reported
executions in `catalog/observations/`, bundle manifests in `catalog/bundles/`,
and prose evidence records in `catalog/evidence/`;
CI forces the corresponding schema for
every structured file in those locations. `catalog/reviews/` remains
Markdown-only until the core project publishes a standalone review-record
contract.

Source inspection and upstream fixture references are not actual executions.
Observation records need a reported execution, its method and environment,
procedure, expected/observed results, time, outcome and limitations. Proposed
tests stay in a bundle's `test_plan`. Synthetic examples remain explicitly
labeled and separate from real contributed observations.

## Review lifecycle

New and materially changed mapping sets are `candidate` by default. Passing
schema checks means only that a record is structurally valid.

- `reviewed` requires a substantive review by someone other than the record
  author, a review timestamp, and acceptance through repository history.
- `verified` additionally requires reproducible supporting evidence and a
  stable `decision_ref` to the governed decision. The author cannot serve as
  the independent reviewer.
- `deprecated` retains the historical record while directing users to the
  reason or replacement.

Do not set `verified` merely because CI passes, an upstream artifact calls
itself official, or a maintainer authored the record. See
[GOVERNANCE.md](GOVERNANCE.md) for the decision process.

The new draft corroboration sidecar is candidate-only and accepts no reviewer
credits. Preserve contradictory observations, partial identity match fields
and source lineage. Do not call a generic action a model-specific success,
a fixture a physical test, or multiple dependent repos independent review.

Draft bundles and observations also remain candidate. Bundle reviews identify
the constituent record IDs and exact digests checked, reviewer, scope and public
decision URL; they do not promote a whole package to verified. Changing a cited
record requires updating the package digest and reconsidering affected review
references. Schema and trust-boundary discussion is tracked in
[core issue #63](https://github.com/edgeloom-oss/edgeloom/issues/63).

## Third-party material

Reference and hash upstream artifacts rather than copying them into this
repository. The root [Apache-2.0 license](LICENSE) covers repository-authored
content and accepted contributions; it does not relicense third-party drivers,
profiles, SDF models, manuals, trademarks, or other upstream material.

Do not vendor third-party bytes unless the pull request includes clear
redistribution permission, required notices, provenance, and explicit
maintainer review. Update [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) when
such an exception is accepted.

## Safety and privacy

Never submit:

- access tokens, credentials, private keys, cookies, or workflow secrets;
- real door-lock PINs, user codes, household identifiers, or private device
  telemetry;
- personal information that is not already intentionally public; or
- scripts or instructions that execute an upstream driver or other untrusted
  source as part of catalog validation; or
- symbolic links inside `examples/`, `docs/`, or `catalog/`, because validation
  inputs must remain contained in this checkout.

Use synthetic values in examples and redact logs before posting them. Catalog
review is static evidence review; it is not authorization to install or execute
an upstream artifact.

## Pull request workflow

1. Open the appropriate issue when the change needs source, scope, or review
   coordination.
2. Fork the repository and create a focused branch.
3. Add or update records without weakening their provenance, limitations, or
   lifecycle status.
4. Run the repository checks documented in the README and the pull request
   template.
5. Complete every applicable section of the pull request template and link the
   issue, evidence, and governed decision record.

Maintainers review scope, schema validity, deterministic checks, provenance,
license evidence, privacy, security, and status claims. Requested changes are a
normal part of review. Significant decisions and declined changes remain in
the public issue or pull request whenever security, privacy, or conduct rules do
not require confidentiality.

Unless explicitly stated otherwise, contributions authored for this repository
are accepted under the [Apache License 2.0](LICENSE). Only submit work you have
the right to contribute under those terms.

## Recognition and conduct

We preserve commit authorship and credit mapping authors, evidence contributors,
reviewers, and correction reporters in repository history. Sustained
contributors may become reviewers or maintainers through the process in
[GOVERNANCE.md](GOVERNANCE.md). Current responsibility is recorded in
[MAINTAINERS.md](MAINTAINERS.md).

Bundle credits can distinguish authorship, source research, observations,
reviews, corrections and maintenance. Disclose AI assistance and source checks
in the contribution; assistance does not count as an independent reviewer or
an experimental participant. Upstream attribution does not imply participation
in, review of, or endorsement of this catalog.

By participating, you agree to follow the
[Code of Conduct](CODE_OF_CONDUCT.md).
