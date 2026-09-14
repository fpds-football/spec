# FPDS - Football Player Data Standard

An open format for sharing player information between agents, intermediaries and clubs.

**Status:** draft, v0.1.0. Nothing here is stable yet. Breaking changes are expected before v1.0.

---

## The problem

Player submissions travel between parties as free text with no agreed structure and no provenance:

> Good lad, played in X league, 10 goals, plays centre mid, available now.

Ten goals in how many minutes, and against what level of opposition? Centre mid as a 6, an 8 or a 10? Available on what terms — contract expiry, release clause, sell-on? And does the sender hold the mandate?

Every recruitment department reconstructs that context by hand, hundreds of times a window. FPDS is an attempt to stop that.

## What FPDS is

A JSON schema for a single player submission. Around twenty fields, covering:

- **Identity** - name, date of birth, nationalities, external identifiers
- **Position** - a controlled vocabulary that distinguishes a 6 from an 8 from a 10
- **Contract** - expiry, release clause, sell-on, loan status
- **Representation** - who is submitting, under what mandate, with what licence number
- **Performance** - appearances, minutes and output, always with the denominator
- **Eligibility** - passports, work permit and squad-registration considerations
- **Provenance** - every claim marked as verified or asserted

## What FPDS is not

- **Not a protocol.** It defines the shape of a payload, not how two systems exchange it. A submission can travel by email, API, file drop or a message attachment.
- **Not a database or a registry.** It does not tell you whether a claim is true. It tells you who claimed it.
- **Not a replacement for FIFA TMS or the FIFA Clearing House.** Where field names overlap with TMS, FPDS follows TMS.

## The provenance rule

This is the part that matters. A structured claim is not a verified claim, and a standard that blurs the two makes things worse rather than better.

Every value in a submission carries a provenance entry, keyed by JSON Pointer:

```json
"provenance": {
  "/performance/0/goals": {
    "source": "third_party_data",
    "asserted_by": "Wyscout",
    "asserted_at": "2026-09-01T00:00:00Z"
  },
  "/contract/expiry_date": {
    "source": "agent_stated",
    "asserted_by": "agent:FIFA-GBR-004821",
    "asserted_at": "2026-09-10T14:22:00Z"
  }
}
```

Anything without a provenance entry defaults to `agent_stated`. Consumers should render that distinction visibly. An interface that shows a verified minutes total and an unverified release clause in the same typeface has thrown away the point of the format.

## Repo layout

```
/schema/v0.1/player.json    JSON Schema (2020-12)
/examples/                  worked examples that validate against the schema
SPEC.md                     the normative document
CHANGELOG.md                what changed between versions
```

Schema `$id` values resolve at `https://fpds.football/schema/v0.1/player.json`. These URLs are permanent.

## Validating

```bash
pip install check-jsonschema
check-jsonschema --schemafile schema/v0.1/player.json examples/*.json
```

## Versioning

Semver. The `fpds_version` field in every submission states which version it was written against. Additive changes are minor; removing or retyping a field is major.

## Licence

Spec text and documentation: CC BY 4.0. Schema files and code: Apache-2.0.

## Governance

Right now this is one person's draft, published openly. That is a weakness, not a feature - a standard shaped by a single vendor is a vendor format wearing a costume.

If FPDS gets real adoption, governance moves somewhere neutral with commit rights held by more than one organisation. Anyone who wants a say in that should say so early.

## Contributing

Open a discussion rather than a pull request at this stage. The field list is still contested and it is more useful to argue about what belongs in it than to fix typos.

Two questions the draft most needs answers to:

1. **Clubs and recruitment staff** - what would you need in here before you would ask agents to submit in this format?
2. **Agents** - what in this draft would stop you using it?
