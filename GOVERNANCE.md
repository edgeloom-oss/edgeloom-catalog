# Governance

The EdgeLoom Catalog is developed in public as an evidence repository for
relationships among device/protocol support, native platform exposure, and
neutral SDF representation. It is not a standards registry, driver store,
certification authority, product-compatibility guarantee, or statement of
industry adoption.

This document defines how catalog records gain project-trusted status while
keeping upstream source maturity, technical review, and project governance
separate.

## Principles

- **Evidence before status.** Source pins, digests, locators, limitations, and
  reproducible observations support a claim; project role or institutional
  affiliation does not substitute for them.
- **Candidate by default.** A new or materially changed mapping is a proposal,
  even when it is schema-valid or its source describes itself as official.
- **Independent review for stronger claims.** Authors do not independently
  review their own records. Conflicts of interest are disclosed and managed.
- **Public and traceable decisions.** Issues, pull requests, reviews, and
  immutable repository history are the decision record. Security and conduct
  reports are the necessary private exceptions.
- **Source and project status remain distinct.** Upstream `source_maturity`
  describes the pinned source. `review.lifecycle` describes EdgeLoom's
  treatment of a mapping. Neither field claims adoption or endorsement.
- **Credit follows work.** Authors, reviewers, source researchers, correction
  reporters, and maintainers receive credit for their contributions.

## Roles

### Participants and contributors

Anyone may file an issue, submit a candidate record, document a source,
reproduce evidence, suggest a correction, or review a public change. No prior
permission is required. All participation follows the
[Code of Conduct](CODE_OF_CONDUCT.md).

### Reviewers

Reviewers are contributors with demonstrated judgment in one or more relevant
areas, such as an ecosystem, protocol, device family, SDF modeling, provenance,
licensing evidence, or reproducibility. They may provide independent review and
triage records in their scope. Reviewers do not merge changes or grant
repository access unless they are also maintainers.

For a particular record, an independent reviewer:

- is not the record author;
- discloses material relationships that could affect the review;
- checks the pinned evidence and the stated mapping semantics rather than only
  schema validity; and
- leaves a durable review in the associated issue or pull request.

### Maintainers

Maintainers have repository write access and are responsible for:

- reviewing and merging pull requests;
- preserving validation, provenance, licensing, privacy, and security
  boundaries;
- applying lifecycle decisions and recording their rationale;
- maintaining CI, repository policy, and public documentation; and
- helping contributors reach a clear outcome, including explaining a decline.

The lead maintainer resolves a decision only after normal consensus work has
failed. The security steward coordinates private vulnerability reports. One
person may hold multiple roles while the project is small, but cannot be both
author and independent reviewer of the same record. Current assignments are in
[MAINTAINERS.md](MAINTAINERS.md).

## Record lifecycle

Schema validation checks structure and bounded semantic rules; it does not
authenticate identities, fetch every source, prove a hash, establish legal
permission, or decide whether a mapping is correct.

### Candidate

`candidate` is the default lifecycle for every new or materially changed
mapping set. Candidate records may be merged when they are useful, clearly
bounded, pass required checks, and do not overstate their evidence. Candidate
means proposed and reviewable, not verified, supported, safe, adopted, or
endorsed.

### Reviewed

A record may become `reviewed` when at least one independent reviewer has:

1. inspected the pinned artifacts and relevant locators;
2. assessed classification, direction, loss, unbound reasons, and limitations;
3. documented the result in the public review record; and
4. confirmed that the reviewed bytes are those proposed for acceptance.

The record names the reviewer and review time. The accepting pull request is
part of the governed history. A review may be scoped; anything not reproduced
or checked remains an explicit limitation.

### Verified

`verified` is a stronger, deliberately uncommon status. It requires everything
for `reviewed`, reproducible evidence sufficient for the stated scope, at least
one independent reviewer, and an explicit maintainer decision recorded in a
stable `decision_ref`. The decision record identifies the accepted scope,
evidence, reviewer, limitations, and exact catalog revision.

CI success, an upstream `official` label, popularity, maintainer authorship, or
an unrecorded conversation cannot independently confer `verified` status. There
is no single-maintainer exception to the independent-review requirement for a
verified record.

### Deprecated

`deprecated` preserves provenance and review history when evidence is stale,
superseded, withdrawn, or materially contradicted. The change explains why and,
when available, identifies a replacement. The lifecycle transition records an
independent reviewer and review time under the same identity boundary as a
reviewed record. Deprecation is not silent deletion.

## Changes and decisions

### Routine changes

Typos, documentation, tooling maintenance, and bounded candidate additions are
decided in their pull requests. Required checks must pass. A maintainer may
merge when the scope and evidence are understood and the status remains
accurate.

### Source updates and corrections

An upstream revision creates new evidence; it does not silently replace the
meaning of an accepted record. Source updates identify changed paths and
digests, then reassess affected mappings. A correction preserves the original
history and explains the factual or methodological problem. Materially changed
records return to `candidate` unless the required independent review is
repeated against the new bytes.

### Substantial changes

Changes to schemas, lifecycle definitions, trust boundaries, validation or
network behavior, licensing policy, or governance begin in a public issue
before implementation. The proposal states the problem, alternatives,
compatibility, security and privacy effects, status migration, and validation
plan. Substantial proposals normally remain open for comment for at least seven
days. Maintainers seek consensus; unresolved decisions are recorded with their
rationale.

### Security and urgent maintenance

Vulnerabilities follow [SECURITY.md](SECURITY.md) and may be handled privately
until coordinated disclosure. A maintainer may make an urgent CI, policy, or
security repair without the normal discussion period, but documents the reason
after the immediate risk has passed.

## Reviews, merges, and conflicts

- Authors do not approve their own pull requests.
- Non-trivial changes receive review from a maintainer or designated reviewer
  who did not author them.
- Candidate-only maintenance may use the small-project exception described in
  the core EdgeLoom governance when no second maintainer is available: CI must
  pass, the pull request must remain public long enough for practical review,
  and the exception must be visible in the pull request.
- The exception never upgrades a record to `verified` without an independent
  reviewer.
- Changes to workflows, governance, security policy, licensing boundaries, and
  public data contracts receive explicit maintainer review.
- Reviewers and maintainers disclose relationships that could reasonably
  affect a decision and recuse themselves when they cannot provide independent
  judgment.

## Becoming a reviewer or maintainer

A contributor may nominate themselves or another contributor in a public
governance issue. Maintainers consider evidence quality, review judgment,
communication, knowledge of project boundaries, sustained participation, and
adherence to the Code of Conduct.

Reviewer appointments state their scope and are recorded in
[MAINTAINERS.md](MAINTAINERS.md). Maintainer nominations remain open for at
least seven days and require consensus of active maintainers. New access follows
least privilege. A reviewer or maintainer may resign at any time; inactivity,
temporary suspension, and removal follow the core EdgeLoom governance process
with as much rationale public as privacy, security, and legal obligations allow.

## Changing this document

Governance changes use the substantial-change process. The accepted pull
request and resulting commit are the authoritative record.
