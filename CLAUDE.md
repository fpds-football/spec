# FPDS: working notes for Claude Code

This repository is the specification for the Football Player Data Standard. It is a **specification repository, not a library**. Nothing in it goes to a package manager.

## Hard rules

**Do not change the `$id` base URL.** Each schema `$id` is under `https://fpds.football/schema/`. These URLs are permanent. Nobody points a published URL to a different file or removes it. If a change alters an existing `$id`, stop and ask.

**Do not add a reference implementation.** Implementations go in separate repositories: `fpds-football/fpds-ts` first, then `fpds-football/fpds-py`. `tests/run_conformance.py` is CI infrastructure, not an implementation. Do not let it grow into one.

**Keep the schema and `SPEC.md` in agreement.** If they disagree, one of them has a defect. Do not change one without the other.

**Each schema change needs a conformance case that fails before the change and passes after it.** If no case is added and all cases still pass, the change does nothing or the suite has a gap. Tell the user which.

**Make sure that each rejection case fails for the reason in its description.** A patch that breaks a different rule gives a false pass.

**Record each decision in `DECISIONS.md`.** Give the decision, the reason, the alternatives and the date. Do not reuse or renumber IDs. If a decision replaces an entry, change the status of the old entry to "Superseded by D-n".

**Before `v0.1.0`, the maintainer can change the draft directly. After `v0.1.0`, a schema change needs a consultation that is open for at least 14 days.** `GOVERNANCE.md` describes the process.

## Commands

```bash
pip install -r tests/requirements.txt
python3 tests/run_conformance.py
check-jsonschema --schemafile schema/v0.1/player.json examples/valid/*.json
check-jsonschema --check-metaschema schema/v0.1/player.json
```

JSON files have a canonical format: two-space indent, a newline at the end, and `ensure_ascii=False`. CI gives a warning when a file does not match.

## Rules for schema design

Obey these rules for every change. If a change breaks one, tell the user. Do not break it quietly.

- **When a decision needs industry input, ship the smaller or stricter option and add the question to §14 of `SPEC.md`.** An addition or a relaxation later is a minor version. A removal or a restriction later is a major version.
- **Do not design a new field without consultation.** Propose an open question in §14 instead. The maintainer uses consultations to get industry input and public content.
- **Boolean field names start with `is_` or `has_`.**
- **Use words that have the same meaning in all countries.** Where FIFA defines a term, use the FIFA definition. Do not use English-only terms such as "scholarship".
- **Do not use `null`.** A required field that can be unknown has the value `unknown`. A missing optional field means "not stated".
- **Forbid fields that do not apply.** Do not make them optional.
- **A `MUST` needs enforcement.** The schema enforces it, or §13.1 of `SPEC.md` lists it as a rule for implementations.
- **Keep `$defs` inline in `player.json`.** Separate files are useful only when there is a second document type.
- **Do not add `examples/invalid/`.** The conformance cases are the invalid examples.

## Decisions already made

Do not argue against these unless the user asks. `DECISIONS.md` gives the reasons.

- **The core is the basic set in D-11 and D-28.** Fields from the first draft that are not in the core are open questions in §14.
- **`submission_id` is a lowercase UUID, one for each version of a document** (D-31). A change to any value gives a new ID and a new `submitted_at`. Forwarding does not.
- **`submission.sender` is `intermediary` or `player`.** `representation` is required for an intermediary. A minor cannot be the sender.
- **Five contract statuses with FIFA definitions:** `under_contract`, `on_loan`, `amateur`, `free_agent`, `unknown`. §7.2 of `SPEC.md` states which fields each status permits.
- **Sixteen uppercase position codes.** They separate `CDM`, `CM` and `CAM`, and include `LCB` and `RCB`. "Centre mid" is not valid.
- **`minutes` is required in each season record.** Per-90 figures are not stored.
- **Seasons are `YYYY/YY` or `YYYY`.**
- **Dates and timestamps have patterns**, because `format` is only an annotation in many validators.
- **`consent.is_minor` means less than 18 years old** on the date of `submitted_at`. Implementations calculate it from `date_of_birth`.
- **Provenance is for each claim, with JSON Pointer keys.** A value without an entry has the sender as its source. Provenance is not authentication.
- **No medical data in the core.** `extensions` MUST NOT contain diagnoses, injury details or medical history.
- **Extension keys use a reverse-DNS prefix.** The `football.fpds` prefix is reserved and unused.
- **Money uses integer minor units with an ISO 4217 code.** No field uses money in v0.1.0. Use this rule when money fields return.

## Conformance fixture format

Each case is a set of RFC 6902 JSON Patch operations on a valid base document. A case shows only the thing that it tests. Inside a JSON Pointer, `/` in a key becomes `~1`. This matters for `provenance`, because its keys are pointers: `/provenance/~1contract~1expiry_date`.

If a patch removes a value, also remove its provenance entry. `tests/README.md` gives the full format.

## Versioning

Semantic versioning describes the specification, not the repository.

- **Major:** remove a field, change the type of a field, make an optional field required, or remove an enum value.
- **Minor:** add an optional field, add an enum value, or relax a constraint.
- **Patch:** correct the text, or correct the schema where it does not agree with the stated intention of the specification.

Each change gets a `CHANGELOG.md` entry under `Unreleased`.

## Writing style

All prose uses Simple English (ASD-STE100, pragmatic mode). Use the `simple-english` skill.

- Keep RFC 2119 keywords in capitals: `MUST`, `SHOULD`, `MAY`. Do not use "should", "may", "might", "could" or "would" in lowercase.
- Use British spelling.
- Write descriptions with a maximum of 25 words in each sentence. Write instructions with a maximum of 20 words.
- Do not use semicolons or contractions.
- Put normative statements in `SPEC.md`. Put reasons in `DECISIONS.md`. Put opinion in a Discussion.
- `index.html` follows the structural rules but keeps its headline voice.

## Open questions

§14 of `SPEC.md` lists the open questions with IDs (`OQ-n`). Each has a "v0.1.0 ships" column. Do not answer an open question without the user.

Three consultations open at launch: wages (OQ-2), release clauses and sell-on percentages (OQ-14), and medical availability (OQ-15). The wage question has the most commercial effect. Some agencies can refuse to adopt FPDS because of it.

## Hosting and infrastructure

- **The GitHub organisation is `fpds-football`.** Do not use `fpds`.
- **The site uses Cloudflare Workers static assets, and the domain is registered at Cloudflare.** `wrangler.jsonc` contains the configuration. Do not assume GitHub Pages or Cloudflare Pages.
- **The site publishes only `index.html`, `schema/`, `consult/` and `_headers`.** Do not publish the repository root.
- **Consultation forms use Tally.** GitHub is the record, and the website is where non-technical people take part.
- **Three repositories** (D-32). This repository holds the schema, the specification and the conformance suite. `fpds-football/fpds-ts` is the TypeScript validation library. `fpds-football/site` holds the website, the builder and the viewer.
- **The builder and the viewer run only in the browser** (D-33 to D-37). Player data never goes to a server. Do not add a feature that sends player data over the network.

## Context

The maintainer builds commercial software for football agents and clubs (Player Status, and Relai, an operating system for football agents). `GOVERNANCE.md` states this conflict and three commitments against it. If a change makes FPDS better for one product and less useful for other parties, tell the user.

One person governs FPDS now. If adoption is real, governance moves to a neutral organisation. `GOVERNANCE.md` states the conditions.
