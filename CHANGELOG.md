# Changelog

All notable changes to FPDS are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and FPDS uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Version numbers describe the **spec**, not this repository. The `fpds_version` field in every submission states which version it was written against.

What counts as what:

- **Major** — removing a field, retyping a field, making an optional field required, or removing a value from an enum. Breaks existing producers.
- **Minor** — adding an optional field, adding a value to an enum, relaxing a constraint. Existing documents remain valid.
- **Patch** — corrections to prose, examples, or schema bugs where the schema did not match the stated intent of the spec.

## [Unreleased]

Nothing yet.

## [0.1.0] - 2026-09-13

First public draft. Nothing here is stable and breaking changes are expected before 1.0.

### Added

- Player submission document with thirteen top-level members, seven of them required
- Position taxonomy distinguishing `DM`, `CM` and `AM`
- Contract block with conditional requirements: `expiry_date` required when under contract or on loan, `parent_club` required when on loan
- Representation block carrying `mandate_status`, so a submission states whether the sender holds authority to make it
- Performance records requiring `minutes` alongside any output figure
- Claim-level `provenance` keyed by JSON Pointer, with `verified` requiring a `verified_against` value
- Money as integer minor units with an ISO 4217 currency code
- `medical` restricted to availability status, with diagnoses and injury history explicitly out of scope
- `consent` block with `subject_is_minor` derived from date of birth
- Namespaced `extensions` object, which consumers must ignore when unrecognised

### Known open questions

Five unresolved questions are listed in §14 of `SPEC.md`. The wage and salary question is the most commercially loaded and the most likely to change the shape of 0.2.

[Unreleased]: https://github.com/fpds-football/spec/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/fpds-football/spec/releases/tag/v0.1.0
