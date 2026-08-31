# Review records

This directory is reserved for durable review decisions and their supporting
notes. Until EdgeLoom publishes a versioned standalone review-record contract,
the Git pull request, commit history, and the `review` block in each mapping set
remain the authoritative review trail.

Candidate authors must not list themselves as independent reviewers. A mapping
must not move to `reviewed`, `verified`, or `deprecated` without the fields
required by the current mapping-set schema and a traceable governed decision.
Review state describes the catalog process only; it does not make EdgeLoom a
standards body, certification authority, or source of vendor endorsement.
