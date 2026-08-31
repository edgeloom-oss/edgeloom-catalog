# Third-Party Material and Notices

The repository's [Apache License 2.0](LICENSE) applies to original
repository-authored content and contributions intentionally submitted for
inclusion under that license. It does **not** relicense third-party device
drivers, platform profiles, SDF models, vendor manuals, specifications,
trademarks, or other upstream material referenced by catalog records.

At repository bootstrap, no third-party driver, platform-profile, SDF-model,
vendor-manual, or device-configuration bytes are intentionally vendored. Source
manifests and mapping records are designed to identify upstream locations,
immutable revisions, paths, digests, and license evidence without copying the
referenced artifacts into this repository.

## Recorded license information

A license expression or evidence path in a source manifest records what a
contributor found in the pinned upstream source. It is not legal advice, an
EdgeLoom grant of rights, or proof that every file in the upstream repository
has the same license. Reviewers should check the evidence at the exact recorded
revision and describe ambiguity rather than infer permission.

## Requirements before vendoring

If a future contribution needs to include third-party bytes, its pull request
must, before merge:

1. identify the exact source, version or commit, and included paths;
2. demonstrate permission to redistribute those bytes;
3. preserve all required copyright, attribution, license, and notice text;
4. record modifications and any generated transformations;
5. add the material and applicable terms to this file; and
6. receive explicit maintainer review.

Material with unknown, conflicting, non-redistributable, or source-specific
terms remains reference-only. A public URL, upstream Git repository, or
machine-readable license field does not by itself establish redistribution
permission.

## Names and trademarks

Names such as SmartThings, Home Assistant, OneDM, Z-Wave, and product or
manufacturer names may appear solely to identify referenced ecosystems and
artifacts. Their appearance does not imply sponsorship, partnership,
certification, adoption, or endorsement by their owners or by EdgeLoom. All
third-party names and trademarks remain the property of their respective
owners.

## Contributor Covenant

[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) is adapted from the
[Contributor Covenant, version 2.1](https://github.com/EthicalSource/contributor_covenant/blob/2.1/content/version/2/1/code_of_conduct.md),
which is licensed under the
[Creative Commons Attribution 4.0 International License](https://github.com/EthicalSource/contributor_covenant/blob/2.1/LICENSE.md).
The local adaptation supplies the EdgeLoom Catalog reporting contact and
project-specific enforcement wording; its attribution section retains the
upstream credit and source link.

The Contributor Covenant attribution notes that its Community Impact
Guidelines were inspired by Mozilla's code-of-conduct enforcement work. No
separate Mozilla policy text is intentionally vendored here. Mozilla's official
[Community Participation Guidelines](https://www.mozilla.org/en-US/about/governance/policies/participation/)
state that those guidelines are distributed under a Creative Commons
Attribution-ShareAlike license.
