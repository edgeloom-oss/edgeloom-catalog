# Contribute evidence behind a device implementation

A useful contribution can be one manual reference, one explanation of code,
one reported execution, one correction or one scoped review. Maintainers join
these contributions into a versioned Device Evidence Bundle. You do not need
to author a complete driver or an SDF mapping to participate.

The draft format is discussed in
[EdgeLoom issue #63](https://github.com/edgeloom-oss/edgeloom/issues/63). The
[YRD210 sample](../catalog/bundles/yale-yrd210-battery.json) is candidate version
`0.1.0`. It explains battery adaptations using the existing source comparisons
and a manufacturer manual; it has no actual hardware observation or independent
review. Canonical means the project's maintained, versioned collection, not
manufacturer certification or a claim that all other interpretations are wrong.

## Pick a small task

| You have | Submit | What maintainers can record |
| --- | --- | --- |
| A manual, vendor page or implementation reference | [Source form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-source.yml) | A document source, pinned Git source or cited explanation |
| A result from your device or an executed simulation | [Observation form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-observation.yml) | A candidate observation with the actual method and outcome |
| An implementation explanation or contradiction | [Correction form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=correction.yml) | A correction or an explicitly unresolved source comparison |
| Time to inspect another contributor's evidence | [Review form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=independent-review.yml) | A review of specific records and their exact digests |

Include the bundle ID, version and feature when known. For the first case these
are `yale-yrd210-battery`, `0.1.0` and `battery`. Unknown information is useful
when labeled; do not guess firmware, a source revision or an experimental result.

## Source contributions

For a manual, provide its original URL, publisher, revision, access date, page
or section and the model or family it actually covers. Quote sparingly or
paraphrase the relevant fact. A family manual can give context even when its
applicability to one firmware or protocol variant is unresolved.

The YRD210 example follows Yale's official support directory to the Rev G PDF.
The catalog records the inspected PDF's SHA-256 and page locations; it does not
redistribute the PDF. A recorded digest identifies inspected bytes but cannot
make a mutable URL immutable or ensure those bytes remain available. A source
you have only linked can remain `link-only` without an invented hash.

For implementation code, supply a repository, full commit, path and relevant
function or locator. Maintainers can help create a source manifest and calculate
digests. Describe why a parameter, conversion or exceptional case exists, and
which parts of that explanation are inferred. Preserve conflicting evidence.

## Observation contributions

An observation records an execution that actually happened. Include:

- Public manufacturer/model and protocol, firmware or explicit unknown, and
  relevant signature information.
- Platform and driver versions, setup, procedure, expected and actual results.
- Time with timezone, repetition count, pass/fail/inconclusive outcome and
  sanitized supporting evidence.
- Conditions, missing information, and what the result cannot establish.

`physical-device` and `simulation` are different methods. Reading a driver or
an upstream test fixture is source inspection, not a reported execution. A
test that somebody could perform belongs in a bundle's `test_plan`. Synthetic
schema examples belong in `examples/`, labeled `synthetic-example`, rather than
in the real observation inventory.

For the battery case, a useful report associates a raw battery attribute with
the displayed value for the same report/time and identifies the selected
implementation. Record what is observable on an already configured device you
control. The proposed test does not require changing drivers, re-pairing the
lock, exhausting batteries or operating a household door. Remove network
identifiers, serial numbers, PINs, access codes and private telemetry from logs.
Use [SECURITY.md](../SECURITY.md) for vulnerability reporting.

## Review and credit

A reviewer identifies the exact record IDs and SHA-256 digests checked, the
scope, findings, limitations and a public issue or pull-request URL. A source
review and a reproduced hardware observation cover different claims. Review
references do not turn the draft bundle or observation into `verified`.

Authors cannot independently review their own records. Declare relationships
that could affect independence. A new record hash requires reconsidering any
review that cited the old bytes; no review silently carries over to a changed
record. The bundle includes its declared reviews and the governed history
establishes who made and accepted them.

Credits describe actual work: authoring, source research, observations, review,
corrections or maintenance. Upstream driver authors remain credited through
their source repositories and license notices; their work does not imply they
reviewed or endorsed EdgeLoom. State AI assistance in the issue or pull request
and which source details you checked. The initial bundle and document metadata
were prepared with Codex assistance under `github:@infinitywings`'s direction;
they earn no independent-review or physical-observation credit.

## Maintainer assembly and local preview

1. Add a source or observation in its typed directory, or update a cited
   explanation after reviewing its evidence. Keep existing record IDs stable
   when correcting the same record; repository history retains previous bytes.
2. Select a bundle version. List every referenced record by ID, path and actual
   SHA-256, including transitive device, mapping, corroboration and source links.
3. Connect the feature explanation to precise JSON pointers in those records.
   Preserve applicability conditions, uncertainties and conflicting results.
   A partial package needs no fabricated SDF mapping.
4. Add only reviews that cover the selected record hashes and have a durable
   public decision URL. Update credits, limitations and the version history.
5. Use the core revision in `CORE_REVISION` to validate, preview and export:

```bash
edgeloom bundle check . yale-yrd210-battery
edgeloom bundle build . yale-yrd210-battery --output _bundle-preview
edgeloom bundle export . yale-yrd210-battery --output yale-yrd210-battery.zip
edgeloom bundle verify yale-yrd210-battery.zip
```

These commands belong to the development increment, not PyPI 0.2.0. Follow the
[README's pinned-core setup](../README.md#validate-the-catalog). Use a fresh
output path for each preview/export. Keep generated outputs out of commits.
The archive contains catalog-authored metadata and reports, not referenced
third-party bytes. Verification checks consistency without downloading manuals,
executing drivers or operating a device; it does not authenticate a publisher
or prove a behavior claim.

Bundle content version, schema version and driver revision serve different
purposes. The export records the selected catalog revision and generator/core
information; a modified checkout is labeled `working-tree`. A publication
decision is separate from local build success. Include the exact source commit,
bundle version and archive digest when sharing an accepted release, so readers
can identify the evidence you meant.
