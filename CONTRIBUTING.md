# Contributing to FPDS

FPDS is a draft, version 0.1.0. The core is small on purpose. New fields enter the core only after public consultation with the football industry.

At this stage, arguments about what belongs in the specification are more useful than pull requests.

## Agents, clubs, players and recruitment staff

Answer an open consultation at [fpds.football](https://fpds.football). You do not need a GitHub account, and you do not need to read JSON.

The most useful answers have the form "I do not use this because X" or "I need Y before I ask agents to use this".

## Developers and implementers

Use GitHub for technical work:

| Purpose | Where |
|---|---|
| Propose a field, or argue against a field | A Discussion in **Field proposals** |
| Ask how something works | A Discussion in **Q&A** |
| The schema and `SPEC.md` disagree | An issue with the **Schema defect** form |
| A sentence in `SPEC.md` has two meanings | An issue with the **Spec ambiguity** form |
| A defect with security or privacy impact | A private report. See [`SECURITY.md`](SECURITY.md). |

§14 of `SPEC.md` lists the open questions. Each question has an ID, for example `OQ-14`. Put the ID in the title of a Discussion about that question.

## Propose a field

A field proposal answers these questions:

| Question | What to write |
|---|---|
| **Name and type** | The name of the field and its structure |
| **Why the core** | Why the field belongs in the core, not in `extensions` |
| **Who produces it** | Which party has this information and can supply it |
| **Who consumes it** | Which decision changes when the field is present |
| **When it is absent** | What a consumer does when the field is not present |
| **Evidence** | Which independent producers already send this information, for example as an extension key |

The requirements are strict on purpose. A field that FPDS adds now stays until a major version. If a specification tries to describe everything, nobody implements it.

If a field is useful to you but not to everyone, put it in `extensions`. If many independent producers use the same extension, that is evidence for a proposal to add it to the core.

## Rules for the schema

These rules apply to every schema change:

1. **When a decision needs industry input, ship the smaller or stricter option.** Add the question to §14 of `SPEC.md`. An addition or a relaxation later is a minor version. A removal or a restriction later is a major version.
2. **Boolean field names start with `is_` or `has_`.**
3. **Use words that have the same meaning in all countries.** Where FIFA defines a term, use the FIFA definition.
4. **Do not use `null`.** A required field that can be unknown has the value `unknown`.
5. **Forbid fields that do not apply.** Do not make them optional.

## Change the schema

Each schema change needs tests. Do these steps:

1. Edit `schema/v0.1/player.json`.
2. Add or update cases in `tests/conformance/v0.1/`. At least one case fails before the change and passes after it.
3. Make sure that each rejection case fails for the reason in its description.
4. If the change affects how a real submission looks, update an example in `examples/valid/`.
5. Update `SPEC.md`. The schema and the text must agree.
6. Add an entry to `DECISIONS.md` with the reason.
7. Add an entry to `CHANGELOG.md` under `Unreleased`.
8. Run the checks:

```bash
pip install -r tests/requirements.txt
```

```bash
python3 tests/run_conformance.py
```

```bash
check-jsonschema --schemafile schema/v0.1/player.json examples/valid/*.json
```

CI runs the same checks on each push. If a schema change does not change any test result, the change has no test, or it has no effect.

Do not add an `examples/invalid/` folder. The conformance cases are the invalid examples.

After `v0.1.0`, a schema change lands only after a consultation of at least 14 days. [`GOVERNANCE.md`](GOVERNANCE.md) describes the process.

## Writing style

All prose uses Simple English (ASD-STE100, pragmatic mode), with two exceptions.

- **RFC 2119 keywords.** `MUST`, `SHOULD` and `MAY` in capitals have their RFC 2119 meanings. If you write `MUST`, the schema enforces the rule, or §13.1 of `SPEC.md` lists it. Do not use "should", "may", "might", "could" or "would" in lowercase.
- **Spelling.** Use British spelling, for example "licence" and "organisation".

Also use these rules:

- Descriptions have a maximum of 25 words in each sentence. Instructions have a maximum of 20 words.
- Write one instruction in each sentence. Put a condition before the instruction.
- Do not use semicolons or contractions.
- Use one word for one thing in the full document.
- Put normative statements in `SPEC.md`. Put reasons in `DECISIONS.md`. Put opinion in a Discussion.

## Implementations

Implementations are in separate repositories, not in this repository. This repository contains the schema, the specification and the conformance cases. It contains nothing to install from a package manager.

If you write an implementation, tell us in a Discussion, and we will add a link to it. The only requirement is that the implementation passes the conformance suite in `tests/`.

## Licence of contributions

Your contribution uses the licence of the material that it changes. [`LICENSING.md`](LICENSING.md) gives the map. There is no contributor licence agreement. If FPDS moves to neutral governance, contributions move with it under the same licences.

---

## Maintaining

This section is for the maintainer.

### Hosting

The site at `https://fpds.football` uses Cloudflare Pages.

1. In Cloudflare, create a Pages project from the `fpds-football/spec` repository.
2. Set the production branch to `main`.
3. Set the build command to `sh scripts/build-site.sh`, and the output directory to `_site`. Leave the framework preset empty.
4. Add `fpds.football` as a custom domain for the project.
5. Make sure that `https://fpds.football/schema/v0.1/player.json` returns the schema with the content type `application/schema+json`.

The site publishes only `index.html`, `schema/`, `consult/` and `_headers`. Do not publish the repository root.

### Email

Use Cloudflare Email Routing to forward these addresses to the inbox of the maintainer:

- `conduct@fpds.football`
- `security@fpds.football`
- `privacy@fpds.football`

Before launch, send a test message to each address.

### GitHub settings

- Turn on Discussions. Make the categories **Field proposals**, **Q&A** and **Show and tell**.
- Turn on Issues. `.github/ISSUE_TEMPLATE/config.yml` turns off blank issues.
- Turn on private vulnerability reporting.
- Protect `main`. Require the `validate` workflow to pass.

### Consultations

For each consultation:

1. Make a page in `consult/` in Simple English, with no JSON.
2. Make a Tally form with a privacy notice. Put the form on the page.
3. Open a GitHub Discussion that links to the ID in §14 of `SPEC.md`.
4. Change the "Consultation" column in §14 to a link to the page.
5. Keep the consultation open for at least 14 days.
6. Publish the summary on the page and in the Discussion.
7. Record the decision in `DECISIONS.md`.

### Release

1. Make sure that `CHANGELOG.md`, `SPEC.md` and the schema agree.
2. Move the `Unreleased` entries in `CHANGELOG.md` to a version heading with the date.
3. Tag the release, for example `v0.1.0`, and make a GitHub release.
