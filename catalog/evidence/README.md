# Evidence records

This directory is reserved for reproducible evidence records that support
catalog entries. Evidence should identify exact artifact bytes, record the
checks that were performed, and separate tool-observed results from
operator-supplied source, license, and status assertions.

Evidence records may be produced locally with `edgeloom audit` and validated
with the versioned `evidence-record` schema. They must not contain credentials,
private device data, or unredacted personal information. A passing record is
evidence about the recorded check; it is not a security certification or proof
of ecosystem adoption.
