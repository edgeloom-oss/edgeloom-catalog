# Reported executions

No physical-device or simulated execution records have been contributed to
this directory yet. The YRD210 bundle contains proposed tests and explicit
gaps, not invented observations.

The draft `catalog-observation` schema records one reported execution: subject,
feature, method, environment and versions, procedure, expected and observed
results, repetition count, time, reporter, evidence and limitations. Start with
the [observation form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-observation.yml);
maintainers can help turn a report into a structured candidate record.

Use `physical-device` only for an actual device execution and `simulation` for
an executed simulation. A test idea belongs in a bundle's `test_plan`; reading
code or an upstream fixture belongs in source/corroboration evidence. Synthetic
schema examples belong in `examples/` and must say `synthetic-example`.

Report failures and inconclusive outcomes as well as successes. Unknown
firmware or versions stay explicit. Remove credentials, access codes, household
and private device identifiers from every public attachment. See
[contribution guidance](../../docs/bundle-contributions.md).
