# Security Policy

## Supported versions

The EdgeLoom Catalog has not published a release. Security fixes currently land
on `main`; snapshots or forks are not separately supported.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| Unreleased snapshots and forks | No |

## Reporting a vulnerability

**Do not open a public issue for a security problem.**

Email Chenglong Fu at `chenglong.fu@charlotte.edu` with `EdgeLoom Catalog
security` in the subject. This is the current private reporting channel; do not
open a public issue or pull request.

Include the affected commit, what an attacker gains, the record or workflow
that triggers the issue, reproduction steps, and any relevant validator
version. Remove credentials, private device data, and real access codes from
the report unless a secure follow-up channel has been agreed.

You can expect acknowledgement within five working days and an initial
assessment within ten. We will provide an update at least every two weeks until
the report is closed and credit you in the advisory unless you ask us not to.
We ask for up to 90 days before public disclosure and will communicate if a fix
requires more time.

## Scope

In scope:

- catalog records and validation behavior maintained in this repository;
- repository automation, permissions, generated indexes, and publication
  configuration;
- an unsafe path, parser, fetch, or rendering behavior that can be triggered by
  an untrusted contribution; and
- exposure of secrets or private data through repository-managed processes.

Vulnerabilities in the EdgeLoom CLI, schemas, or package should be reported to
the [core EdgeLoom security process](https://github.com/edgeloom-oss/edgeloom/security/policy).
Vulnerabilities in SmartThings, Home Assistant, a device, firmware, an upstream
driver, or an SDF source should be reported to that project's or vendor's
security contact. A public catalog correction may link a coordinated advisory
after disclosure.

## Trust boundaries

**Catalog contributions are untrusted input.** YAML, JSON, Markdown, links,
paths, identifiers, and metadata may be malicious or malformed. Validation and
rendering must bound parsing and output, reject unsafe paths, and avoid
interpreting record content as executable code or trusted markup.

**Upstream artifacts are untrusted and are not executed.** A pinned commit and
digest identify bytes; they do not establish that those bytes are safe. Catalog
checks must not run a driver, build script, repository hook, fetched executable,
or generated command from an upstream source. Inspect untrusted material in a
disposable environment when manual analysis requires more than static reading.

**Source and review fields are assertions.** Repository URLs, revisions,
digests, license expressions, source maturity, reviewer identities, and
lifecycles can be structurally valid while false. Project-trusted review status
comes from governed repository history, not from a submitted field or passing
CI. A source labeled `official` is not thereby safe, adopted, endorsed, or
verified by EdgeLoom.

**External links may change.** A link is provenance or context, not permission
to fetch, install, or execute its target. Future network validation must define
an explicit protocol, host, redirect, size, timeout, and private-address policy
before it is enabled in CI.

**The catalog contains no secrets by design.** Do not submit access tokens,
private keys, cookies, hub credentials, real door-lock PINs or user codes,
household identifiers, or private telemetry. Synthetic identifiers are
required in examples. Treat accidental exposure as a security report and
rotate the affected secret immediately.

**Third-party rights remain upstream.** The repository license does not
relicense referenced artifacts. Licensing or provenance ambiguity is normally a
public data-quality issue; deliberate evasion of validation, unauthorized
publication of sensitive material, or a workflow exploit should be reported
privately.

## Intended behavior

The catalog deliberately records gaps, lossy mappings, ambiguous mappings, and
unbound features. A well-supported negative or uncertain result is not a
vulnerability. Likewise, a `candidate` record is expected to be incomplete
pending review. Use the correction or independent-review issue forms for
ordinary evidence disagreements without disclosing an unpatched security flaw.
