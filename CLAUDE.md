# FPDS — working notes for Claude Code

This is the specification repository for the Football Player Data Standard. It is a **spec repo, not a library**. Nothing here is published to a package manager.

## Hard rules

**Never change the `$id` base URL.** Every schema `$id` resolves under `https://fpds.football/schema/`. These URLs are a permanent commitment and published ones are never repointed or removed. If a change would alter an existing `$id`, stop and ask.

**No reference implementation in this repo.** A spec repo that ships a library in one language becomes a project about that language. Implementations go in sibling repos (`fpds-football/fpds-ts` first, `fpds-football/fpds-py` later). `tests/run_conformance.py` is CI plumbing and is exempt — it is not an implementation and should not grow into one.

**The schema and SPEC.md must never disagree.** If they do, that is a bug in one of them. Do not change one without the other.

**Every schema change needs a conformance case that fails before it and passes after it.** If all existing cases stay green and none are added, either the change does nothing or the suite has a gap. Say which.

## Commands

```bash
pip install -r tests/requirements.txt
python3 tests/run_conformance.py                                      # 43 cases
check-jsonschema --schemafile schema/v0.1/player.json examples/valid/*.json
check-jsonschema --check-metaschema schema/v0.1/player.json
```

JSON files are canonically formatted: two-space indent, trailing newline, `ensure_ascii=False`. CI warns on drift.

## Design decisions already made

Do not relitigate these without being asked. If a change would reverse one, flag it rather than doing it quietly.

- **Money is an integer in minor units** with an ISO 4217 code. `250000000` is £2,500,000. Ugly to read, but floats and transfer fees are a bad combination.
- **No stored per-90 figures.** They are derived from minutes and output. Storing both invites the two disagreeing. The schema rejects them via `additionalProperties: false`.
- **`minutes` is required whenever any output figure is present.** Output without a denominator is not information. This is the spec's first design principle.
- **`medical` carries availability status only.** No diagnoses, no injury history, and not in `extensions` either. That is special-category health data in most jurisdictions and does not belong in a forwardable document.
- **`subject_is_minor` is computed from `date_of_birth`**, never asserted independently. JSON Schema cannot enforce this; implementations must.
- **Provenance is claim-level**, keyed by JSON Pointer, and defaults to `agent_stated` when absent. `verified` requires `verified_against`. Provenance records who claimed something — it is not authentication and does not prove the named party sent the document.
- **Position codes distinguish `DM`, `CM` and `AM`.** This is deliberate and non-optional. "Centre mid" is not a valid value.
- **Twenty-ish fields in the core, everything else in `extensions`**, namespaced by reverse DNS. Resist scope creep hard. A field added now cannot be removed before a major version.
- **`$defs` stay inline in `player.json`.** Splitting them into separate files only pays off once there is a second document type, and until then it makes the schema harder to copy.
- **No `examples/invalid/`.** The conformance fixtures are that, and duplicating them means they drift.

## Conformance fixture format

Cases are RFC 6902 JSON Patch operations applied to a known-good document, so each case shows only the thing under test. `/` inside a JSON Pointer key escapes as `~1`, which matters because the `provenance` object is keyed by pointers: `/provenance/~1contract~1expiry_date`.

Full format in `tests/README.md`. A patch with six operations in it is usually two cases.

## Versioning

Semver, describing the spec rather than the repo.

- **Major** — removing a field, retyping a field, making an optional field required, removing an enum value.
- **Minor** — adding an optional field, adding an enum value, relaxing a constraint.
- **Patch** — prose corrections, or the schema not matching the stated intent of the spec.

Schema changes should have had a discussion thread open for at least 14 days before landing. Every change gets a `CHANGELOG.md` entry under `Unreleased`.

## Tone for spec text

RFC 2119 keywords in capitals, used deliberately: if it says MUST, the schema has to enforce it and a conforming implementation has to reject violations. Normative statements in `SPEC.md`; rationale and opinion in `README.md` or a discussion. Plain prose, no hedging, British spelling in new text but don't convert existing text either way.

## Open questions

Five sit in §14 of `SPEC.md` and are genuinely unresolved. The wage/salary field is the most commercially loaded — it is the reason some agencies would refuse to adopt this. Don't resolve any of them unilaterally.

## Context worth knowing

The maintainer builds commercial software in this space (Player Status, and Relai, an operating system for football agents). That conflict is stated openly in `GOVERNANCE.md` along with three commitments against it. Changes that would make FPDS more convenient for one product and less useful for everyone else are exactly what those commitments exist to catch — say so if you see one.

Governance is currently one person. It moves somewhere neutral if adoption gets real, with the threshold written down in `GOVERNANCE.md`.
