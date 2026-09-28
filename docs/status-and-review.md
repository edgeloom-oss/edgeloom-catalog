# Status and review

Catalog records use two separate status axes. **Source maturity** describes the
context of an upstream artifact. **Review lifecycle** describes how this
project has evaluated a catalog-authored mapping. One must never be inferred
from the other.

Schema validation checks structure and bounded semantics. It does not
authenticate contributors, prove an upstream status claim, dereference a
review decision, establish correctness, or confer approval.

## Source maturity

A source manifest records one of these values for each artifact:

| Value | Meaning recorded by the catalog |
| --- | --- |
| `official` | Published or maintained by the organization responsible for the referenced source, based on cited evidence |
| `community` | Maintained by a community rather than the responsible vendor or standards organization |
| `experimental` | Presented as an experiment, prototype, playground artifact, or similarly non-production work |
| `draft` | Work whose upstream status is explicitly draft or provisional |
| `deprecated` | Marked obsolete or superseded by its upstream source |
| `unknown` | Available evidence does not support a more specific classification |

These labels describe provenance context, not quality, safety, compatibility,
adoption, or endorsement. The manifest must retain the evidence on which the
classification rests. When evidence is insufficient, use `unknown`.

## Review lifecycle

| Value | Project meaning |
| --- | --- |
| `candidate` | An authored assertion submitted with evidence and limitations; it has not completed independent review |
| `reviewed` | At least one reviewer other than the author has examined the cited evidence, scope, classification, and limitations; unresolved uncertainty may remain |
| `verified` | Independent review and the governed acceptance criteria have been met, with a stable public decision reference and reproducible evidence for the stated scope |
| `deprecated` | The record is retained for provenance but should not support new conclusions because it is superseded, invalidated, or no longer maintainable |

`Verified` is deliberately narrow. It means that this project accepted a
bounded record under its documented process. It is not certification, a
standards determination, a vendor statement, proof of deployment, or evidence
of adoption.

## Review requirements

- The author cannot serve as the record's independent reviewer.
- A reviewer checks the pinned inputs, digests, locators, mapping
  classification, loss dimensions, uncertainty, and stated limitations.
- Records at `reviewed`, `verified`, or `deprecated` include the reviewer and
  review time required by the core schema.
- Promotion to `verified` also includes a stable decision reference. A string
  that merely matches the schema does not authenticate that decision.
- Conflicts of interest and material disagreement remain visible in the public
  review record; they are not removed by normalization.
- A changed upstream commit or artifact digest requires a new assessment. A
  previous review does not automatically cover changed bytes.

The Git history, pull-request discussion, and applicable
[Governance](../GOVERNANCE.md) process supply the human trust context around
machine-valid records.

## Current pilot boundary

Synthetic examples may exercise lifecycle values to test validation, but they
are not catalog findings. The repository's first real YRD156 records are
founder-authored `candidate` mappings with no independent reviewer. They are
not reviewed, verified, adopted, certified, endorsed, or proven compatible.
