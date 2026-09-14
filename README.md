# FPDS: Football Player Data Standard

FPDS is an open format for player information that agents, intermediaries, players and clubs send to each other.

**Status:** draft, version 0.1.0, not released. Nothing is stable yet. Breaking changes are expected before version 1.0.

---

## The problem

Player submissions travel between parties as free text, with no agreed structure and no sources:

> Good lad, played in X league, 10 goals, plays centre mid, available now.

This message does not answer the questions that a club needs to ask:

- Ten goals in how many minutes?
- Centre mid as a 6, an 8 or a 10?
- Is the player under contract, and until when?
- Does the sender have a mandate to offer the player?
- Who says so?

Each recruitment department finds this information by hand, hundreds of times in each transfer window. FPDS gives a submission a structure that answers these questions.

## What FPDS is

FPDS is a JSON Schema for one player submission. The core is small on purpose. It contains:

- **Submission.** Who sends it, when, and for which types of deal.
- **Identity.** Name, date of birth, nationalities and the FIFA Connect identifier.
- **Position.** Sixteen codes that separate a 6 from an 8 from a 10.
- **Contract.** Status, with FIFA definitions, expiry date and loan details.
- **Representation.** The agent, the licence and the mandate.
- **Performance.** Appearances and minutes, with goals, assists and clean sheets.
- **Consent.** The lawful basis for sharing the data, and whether the player is a minor.
- **Provenance.** The source of each claim.

Other fields enter the core only after public consultation. Until then, producers put them in `extensions`.

## What FPDS is not

- **FPDS is not a protocol.** It defines the structure of a document, not how two systems exchange it. A submission can travel by email, API, file transfer or message.
- **FPDS is not a database or a registry.** It does not tell you whether a claim is true. It tells you who made the claim.
- **FPDS does not replace FIFA TMS or the FIFA Clearing House.** Where FPDS and FIFA TMS use the same concept, FPDS follows FIFA.

## The provenance rule

This part of FPDS is the most important. A claim in a structure is not a verified claim. A standard that hides this difference makes the problem worse.

A submission can give a source for each value. Each key is a JSON Pointer to the value:

```json
"provenance": {
  "/performance/0/minutes": {
    "source": "third_party_data",
    "asserted_by": "Wyscout",
    "asserted_at": "2026-09-01T00:00:00Z"
  },
  "/contract/expiry_date": {
    "source": "verified",
    "asserted_by": "Widzew Lodz",
    "verified_against": "FIFA TMS"
  }
}
```

If a value has no entry, its source is the sender. That is `agent_stated` for an intermediary and `player_stated` for a player. Consumers show the source of each value. If an interface shows a verified minutes total and an unverified claim in the same way, the format has no purpose.

## How do I create an FPDS-conforming document?

You do not write FPDS by hand. Software makes the document for you.

- **Agents and players.** Use the free [builder](https://fpds.football/build/). You fill in a form, and the builder makes a file that ends with `.fpds.json`. You send the file by email or message, as you send a PDF now. Your data stays in your browser.
- **Clubs.** Open the file in the free [viewer](https://fpds.football/view/). The viewer shows the player, the source of each value, and any problems with the file. The file never leaves your browser.
- **Software providers.** Implement the schema now. §13 of [`SPEC.md`](SPEC.md) gives the steps for a conforming producer. Run the cases in [`tests/conformance/`](tests/conformance/) against your implementation. [`@fpds-football/fpds`](https://www.npmjs.com/package/@fpds-football/fpds) is a TypeScript library that validates documents.

A valid document has the correct structure. It does not prove that the information is true. The provenance of each value shows who made the claim.

## Take part

FPDS grows through public consultation with the football industry.

- **Agents, clubs, players and recruitment staff.** Answer an open consultation at [fpds.football](https://fpds.football). You do not need a GitHub account.
- **Developers and implementers.** Use [GitHub Discussions](https://github.com/fpds-football/spec/discussions) for technical questions. [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how to propose a change.

§14 of [`SPEC.md`](SPEC.md) lists all open questions.

## Repository layout

```
schema/v0.1/player.json     JSON Schema (draft 2020-12)
examples/valid/             submissions that are valid against the schema
tests/conformance/          the suite of cases that FPDS accepts and rejects
SPEC.md                     the normative specification
DECISIONS.md                the reasons for each decision
CHANGELOG.md                the changes between versions
GOVERNANCE.md               who decides, and the conflict of interest
```

The schema `$id` is `https://fpds.football/schema/v0.1/player.json`. This URL is permanent.

## Validate a submission

```bash
pip install check-jsonschema
```

```bash
check-jsonschema --schemafile schema/v0.1/player.json examples/valid/*.json
```

Some rules are not in the schema. §13.1 of `SPEC.md` lists them.

## Versioning

FPDS uses semantic versioning. The `fpds_version` field in each submission states the version that the submission uses. [`CHANGELOG.md`](CHANGELOG.md) states which changes are major, minor or patch.

## Licence

The schema and code use Apache License 2.0. The specification text and documentation use CC BY 4.0. The examples and conformance fixtures use CC0 1.0. [`LICENSING.md`](LICENSING.md) gives the full map.

## Governance

One person maintains FPDS now, and the draft is public. This is a weakness. A standard that one vendor controls is a vendor format with a different name.

If FPDS gets real adoption, governance moves to a neutral organisation, and more than one organisation holds commit rights. [`GOVERNANCE.md`](GOVERNANCE.md) states the conditions.
