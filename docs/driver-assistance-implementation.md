# Reusable driver artifacts implementation plan

Status: design draft; integration baseline updated 10 October 2026. The PI approved
SmartThings Edge-first driver assistance and requested coordinated planning.
This document changes no record, core pin, runtime behavior or publication state.

The catalog will supply reusable implementation knowledge to EdgeLoom's
Find → Customize → Contribute workflow. Core owns the contracts, matching,
generators, checks and rendering. This repository owns source-grounded records,
declarative recipes, evidence, reviews and attribution. The companion design is
[driver-assistance architecture](https://github.com/edgeloom-oss/edgeloom/blob/main/docs/driver-assistance-architecture.md)
in EdgeLoom core. Publishing the design does not implement its proposed commands.

## Baseline

Core [PR 64](https://github.com/edgeloom-oss/edgeloom/pull/64) and
[PR 65](https://github.com/edgeloom-oss/edgeloom/pull/65) are merged, with the
media/contracts baseline at `5bd3c8a2d209799d183f7b95ad0653f169dd7e7b`.
Catalog [PR 6](https://github.com/edgeloom-oss/edgeloom-catalog/pull/6) is merged
at `f246a43a37c7f9df74de661f7eb7ef16ba01d00d`, adding the LG family case beside
the Yale bundle. `CORE_REVISION` remains
`d7e801d10f02b6effe4d8403ec997913bfd7bb2c`, a preserved ancestor of core main.
This is a reachable development pin, not a new PyPI release. Records remain
candidates without physical observations or independent community reviews.

Recheck remote heads before choosing an implementation base. Recipe contracts,
matching, workpacks and candidate generation below remain planned work.

## Artifact structure

Keep `catalog/sources`, `documents`, `devices`, `mappings`, `corroboration`,
`observations`, `bundles`, `evidence` and `reviews`. Add `catalog/recipes` only
after core supplies its versioned contract and resolver. No schema is copied
and independently modified in this repository.

Each implementation recipe must explain:

- The desired behavior, baseline behavior and bounded capability gain.
- Device/platform/protocol/firmware applicability, including explicit unknowns.
- How a protocol field or API maps to implementation code and a native capability.
- Which exact source records and locations justify each important choice.
- Preconditions, dependencies, permissions by execution location and recovery limits.
- An approved core generator/template reference, or `reference-only` when none exists.
- Expected output changes and proposed tests, distinct from tests actually run.
- Original authors, contributor roles, reuse rights, review scope and limitations.

Recipes are data, not executable hooks. Upstream drivers and manuals stay at
their original locations by default. Any future vendored snippet or patch needs
redistribution permission, byte-level provenance and review before acceptance.

Extend device feature navigation and bundle closure through explicit new contract
versions. Keep original v0.1 records/schema behavior and older exports intact.
Do not invent an SDF mapping just to accept a useful recipe or source.

## First curation set

| Case | Contribution value | Boundary |
| --- | --- | --- |
| Existing Yale battery bundle | Explanation, normalization context and concrete evidence gaps | Not an established fix or physical validation |
| One bounded SmartThings Zigbee recipe | First customization task consumed by a reviewed core generator | Exact base/template required; synthetic checks labeled |
| bscpylgtv | Traceable extension/control references | Source/rights/applicability checks still required; not a SmartThings driver |
| webOS Homebrew Channel | Explain external service and privilege prerequisites | No automatic install, root or firmware changes |
| PicCap and pinned hyperion-webos dependency | Explain a multi-component capability-extension chain | No inherited TV/hardware compatibility claim or assumed SmartThings binding |

The last three are source-only recipes initially. Keep source family, firmware,
runtime location and privilege requirements explicit. They need not delay the
first Zigbee workflow and must not appear in an installable-driver category.

## Contributor flow

1. A user describes a desired feature, or a developer supplies a public URL and
   a short explanation. Known model/platform information helps but unknown is allowed.
2. The local tool or a maintainer prepares a draft. The contributor does not
   need to author hashes, a complete recipe or a complete bundle at first contact.
3. Maintainer-assisted enrichment pins Git sources or records document metadata,
   identifies exact applicability, preserves disagreements and reviews reuse rights.
4. A scoped PR adds or corrects a record and its affected references. Credit
   distinguishes source research, implementation, testing, review and maintenance.
5. CI checks structure and consistency. Human review decides acceptance; neither
   AI extraction nor passing CI proves device behavior or earns independent review.

Use local ignored work directories for requests, workpacks and candidate output.
They are not ingested into canonical directories automatically. Existing and new
issue forms warn about public visibility and avoid credentials, serial numbers,
private IP/MAC addresses, household names and raw telemetry.

## Coordinated work packages

| Package | Catalog changes | Core dependency | Completion check |
| --- | --- | --- | --- |
| C0 Baseline | Audit pin and dependency state; preserve existing records | Review of bundle/media dependency chain | Exact compatible pair is documented and reachable |
| C1 Recipe seeds | Add typed candidate recipes and reuse current source references | Recipe contract, resolver and synthetic fixtures | Source closure, applicability, rights and credit checked |
| C2 Reuse context | Feature terms, prerequisites, expected changes and contribution prompts | Explainable search and workpack export | One request produces a useful task with explicit unknowns |
| C3 Candidate evidence | Add reviewed explanation/test specification and exact output references | Candidate checking and one supported generator | Code/checks are tied to the pinned base and source evidence |
| C4 Low-friction entry | Simplify/add request and source forms, walkthrough and review checklist | Static UI and local contribution draft output | One URL submission can be enriched without full-schema authoring |
| C5 Observation and snapshot | Sanitized actual observation when available; scoped review and versioned data snapshot | Applicable observation schema and paired integration validation | No promotion beyond the measured scope; publication separately approved |

C1 source curation can proceed alongside core synthetic tests after the contract
is fixed. C4 wording can proceed alongside candidate-check development after the
workpack/UI contract is stable. Acceptance and publication remain coordinated.

## CI and versioning work

- Add recipe paths/kinds to `scripts/validate-catalog.sh` only when the pinned core
  supports them. Unknown structured-record locations continue to fail closed.
- Lock all new record references and validate device/feature/recipe joins and
  transitive closure. Changed bytes invalidate earlier hash-scoped reviews.
- Generalize the current Yale-only export check to enumerate supported bundles;
  build twice, compare outputs and verify each export offline.
- Keep synthetic examples out of real observations and keep screenshots or device
  logs sanitized and rights-reviewed. A planned experiment is not an observation.
- Preserve `CORE_REVISION` as the exact generator/validator pin. Schema version,
  recipe content version, bundle version, upstream driver revision and tool version
  remain distinct. Do not promise untested cross-version compatibility.
- Keep canonical source records separate from generated site files. The public
  browser remains a core-hosted, commit-pinned view; this plan adds no second site.

## Acceptance before community promotion

A contributor can submit one useful source without building an entire driver.
A user can understand why a result is relevant and whether it is only source
evidence, a customization candidate or a tested implementation in a stated setup.
One completed development task has a reproducible input pack, a reviewable
candidate output and an exact path for contributing the useful result back.

Physical devices are not required for the contracts, matching or task-pack MVP.
Before claiming SmartThings runtime behavior, identify an available SmartThings
setup and exact device/firmware; Home Assistant-only observations cannot establish
that result. Any media/IP observation needs its own supported contract first.

No release, merge, public post, contributor contact, device operation or deployment
is performed by this planning increment.
