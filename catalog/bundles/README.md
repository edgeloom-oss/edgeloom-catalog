# Device Evidence Bundles

A bundle is a versioned explanation of a device's capabilities: document
citations, implementation choices, reported observations, proposed tests,
unresolved questions and scoped review references. Its manifest locks exact
catalog record paths and SHA-256 digests. The format is draft v0.1, proposed in
[core issue #63](https://github.com/edgeloom-oss/edgeloom/issues/63).

Start with [Yale YRD210 battery](yale-yrd210-battery.json). Version `0.1.0`
preserves six referenced records: the device, two source manifests, two
cross-source comparisons and one manufacturer-document record. It has no
physical-device observations or independent reviews. The lock-state comparison
is included because the referenced device points to it; its unresolved scope
remains visible alongside the battery investigation.

The source manifest describes upstream driver bytes, but exports contain only
catalog-authored records and reports. A document digest does not cause its PDF
to be downloaded or redistributed. Firmware uncertainty, empty observation
inventory and disagreements are useful parts of the package.

Use the exact core revision in `CORE_REVISION` for the proposed `bundle check`,
`build`, `export` and `verify` commands. They are development commands, not part
of the PyPI 0.2.0 release. See [bundle contributions](../../docs/bundle-contributions.md)
for a walkthrough and small tasks that help complete the evidence.
