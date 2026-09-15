# Changelog

This file records all important changes to FPDS. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). FPDS uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Version numbers describe the **specification**, not this repository. The `fpds_version` field in each submission states the version that the submission uses.

`DECISIONS.md` records the reasons for each change.

Each type of change has a version level:

- **Major.** Remove a field, change the type of a field, make an optional field required, or remove a value from an enum. Existing producers stop working.
- **Minor.** Add an optional field, add a value to an enum, or relax a constraint. Existing documents stay valid.
- **Patch.** Correct the text, the examples, or the schema where the schema does not agree with the intention of the specification.

## [Unreleased]

The first public draft, version 0.1.0. It is not stable. Breaking changes are expected before version 1.0.

### Added

- A player submission document with eleven top-level members. §1 states that user interfaces call a submission a player profile. Six members are required, and `representation` is required when the sender is an intermediary.
- A `submission` block with `submission_id`, `submitted_at`, `purposes` and `sender`.
- `submission_id`, a lowercase UUID. Each version of a document has its own ID, so a receiver can recognise a repeated or forwarded copy.
- A checklist in §13 for conforming producers, and a recommended file name ending `.fpds.json`.
- `purposes`, an array that states one or more types of deal. `information_only` cannot occur with another value.
- `sender`, with the values `intermediary` and `player`. A player can send their own profile. A minor cannot.
- Sixteen position codes that separate `CDM`, `CM` and `CAM`, with `LCB` and `RCB` for centre-backs who play on one side.
- Five contract statuses with FIFA definitions: `under_contract`, `on_loan`, `amateur`, `free_agent` and `unknown`. Each status states which of `current_club`, `expiry_date` and `parent_club` are present.
- A `representation` block with `mandate_status`, so that a submission states whether the sender has authority to make it.
- Season records that require `minutes`, with `goals`, `assists` and `clean_sheets`. Seasons use `YYYY/YY` or `YYYY`.
- A `media` array of links to video. Each item has `type` (`video`), `video_type` (`highlights` or `full_match`) and an `https` `url`. A URL with user information is invalid.
- A `consent` block with `lawful_basis`, `consent_date` and `is_minor`. A minor is a person less than 18 years old.
- Provenance for each claim, with keys that are JSON Pointers. The source `verified` requires `verified_against`. A value without an entry has the sender as its source.
- An `extensions` object with keys that have a reverse-DNS prefix. The `football.fpds` prefix is reserved.
- A pattern on each date and timestamp field, so that validators reject local date formats.
- A list of permitted country codes in the schema: ISO 3166-1 alpha-3, plus `ENG`, `SCO`, `WAL`, `NIR` and `XKX`.
- A list in §13.1 of the rules that implementations enforce because the schema cannot. One rule states that secondary positions do not repeat the primary position.
- A conformance suite in `tests/conformance/`.

### Known open questions

§14 of `SPEC.md` lists 28 questions. OQ-17 has an answer for video (D-43), and 27 questions are open. Three consultations are open at launch: wages (OQ-2), release clauses and sell-on percentages (OQ-14), and medical availability (OQ-15).

[Unreleased]: https://github.com/fpds-football/spec/commits/main
