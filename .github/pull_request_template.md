## Summary

<!-- What record, source, review, policy, or validation behavior changes? -->

## Change type

- [ ] Candidate mapping submission
- [ ] Source manifest or pinned-source update
- [ ] Correction or deprecation
- [ ] Independent review / lifecycle change
- [ ] Documentation, governance, or repository tooling

## Scope and impact

<!-- Identify affected record IDs, ecosystems, device domains, platforms,
protocols, and consumers. Explain whether existing records change meaning. -->

## Evidence and provenance

<!-- For data changes, list the upstream HTTPS repository, full 40-character
commit, paths, SHA-256 digests, evidence locators, and license-evidence paths.
State what was reproduced and what remains inferred. Write "Not applicable"
only for a change with no catalog-data effect. -->

## Mapping and limitations

<!-- Explain the three evidence layers, mapping classification and direction,
loss dimensions or unbound reason, and known limitations. Do not convert
uncertainty into a stronger claim merely to satisfy a schema. -->

## Review lifecycle

- Proposed lifecycle: `candidate` / `reviewed` / `verified` / `deprecated`
- Record author:
- Independent reviewer(s), if required:
- Review timestamp, if required:
- Governed `decision_ref`, required for `verified`:

<!-- New and materially changed mappings are candidate by default. Schema or CI
success is not review. The author cannot be the independent reviewer, and a
verified record requires governed acceptance as described in GOVERNANCE.md. -->

## Validation

- [ ] Ran `./scripts/validate-catalog.sh` with the core revision pinned by CI,
      or explained why this does not apply
- [ ] Verified every changed artifact digest against the pinned bytes, or no
      artifact digest changed
- [ ] Added or updated synthetic tests/examples when validation behavior changed,
      or not applicable
- [ ] Confirmed that validation neither fetches nor executes upstream code

## Licensing, privacy, and security

- [ ] Linked license evidence from the pinned source and described ambiguity
      without treating EdgeLoom as legal authority
- [ ] Did not add third-party artifact bytes, or documented redistribution
      permission and updated `THIRD_PARTY_NOTICES.md`
- [ ] Did not add secrets, credentials, private keys, real lock PINs/user codes,
      private telemetry, or household identifiers
- [ ] Reviewed effects on untrusted YAML/JSON/Markdown, paths, links, rendering,
      network access, and GitHub workflows
- [ ] Used the private process in `SECURITY.md` for any unpatched vulnerability

## Related record

<!-- Link the issue, prior record, source-update discussion, independent review,
or governed decision. -->
