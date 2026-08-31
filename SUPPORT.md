# Support

The EdgeLoom Catalog is an early-stage open-source evidence repository. Public
questions and corrections are welcome, but support is provided on a best-effort
basis and no record is a compatibility, safety, certification, or deployment
guarantee.

## Choose the right channel

- **Propose a mapping:** use the mapping-submission issue form.
- **Update a pinned source:** use the source-update issue form.
- **Report stale, incorrect, or conflicting evidence:** use the correction
  issue form.
- **Volunteer an independent review:** use the independent-review issue form.
- **Ask about the EdgeLoom CLI or schemas:** use the
  [core EdgeLoom discussions](https://github.com/edgeloom-oss/edgeloom/discussions).
- **Report a vulnerability:** do not post publicly; follow
  [SECURITY.md](SECURITY.md).
- **Report harassment or other conduct concerns:** use the private contact in
  [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Before opening an issue, search accepted records, open issues, and pull
requests. Include stable source URLs, full commit IDs, repository-relative
paths, digests, evidence locators, and the affected mapping ID when available.
State what you reproduced and what remains inferred.

Never post access tokens, private keys, hub credentials, real door-lock PINs or
user codes, private device telemetry, or personal household information. Use
synthetic values and redact logs.

We aim to triage actionable public reports within seven days. A response may
request stronger evidence, identify a duplicate or current limitation, route a
tooling issue to the core repository, or accept the work for review. Security
response targets are defined separately in [SECURITY.md](SECURITY.md).

## Status expectations

All new or materially changed mappings are `candidate` by default. Structural
validation and issue triage do not make a record `reviewed` or `verified`.
Lifecycle requirements are documented in [GOVERNANCE.md](GOVERNANCE.md).

The repository currently supports `main`; there is no released catalog API or
stability guarantee. Consumers should pin an exact catalog commit and preserve
the status, source maturity, evidence, and limitation fields they display.
