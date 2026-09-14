# Contributing to FPDS

FPDS is at v0.1.0 and the field list is still contested. At this stage, arguments about what belongs in the spec are worth more than pull requests fixing it.

## Where to start

**Open a Discussion, not an issue or a PR**, unless you are fixing something factually wrong. Discussions are for:

- Fields you think should exist and don't
- Fields you think shouldn't exist and do
- Places where the spec conflicts with how transfers actually work
- Anything in §14 of `SPEC.md` (the open questions)

The two questions the draft most needs answered:

1. **Clubs and recruitment staff** — what would need to be in here before you would ask agents to submit in this format?
2. **Agents** — what in this draft would stop you using it?

Answers of the form "I wouldn't use this because X" are the most useful thing you can contribute.

## Proposing a field

A field proposal should say:

| | |
|---|---|
| **Name and type** | What it's called and what shape it is |
| **Why the core** | Why this belongs in the core rather than `extensions` |
| **Who produces it** | Which party has this information and can be expected to fill it in |
| **Who consumes it** | What decision changes because this field is present |
| **What happens when it's absent** | Every field must degrade gracefully |

The bar is deliberately high. Every field added now is one that cannot be removed before a major version, and a spec that tries to describe everything gets implemented by nobody. If a field is useful to you and not obviously useful to everyone, it belongs in `extensions` — and if enough implementations converge on the same extension key, that is the evidence for promoting it into the core later.

## Changing the schema

Schema changes must come with tests. Concretely:

1. Edit `schema/v0.1/player.json`
2. Add or update fixtures under `tests/conformance/v0.1/`
3. Add a worked example under `examples/valid/` if the change affects how a real submission looks
4. Add a counter-example under `examples/invalid/` showing what the change now rejects
5. Update `SPEC.md` — the schema and the prose must not disagree
6. Add a `CHANGELOG.md` entry under `Unreleased`

CI runs the conformance suite on every push. A schema change that doesn't change any test result is either untested or unnecessary.

## Writing style for SPEC.md

- RFC 2119 keywords (MUST, SHOULD, MAY) in capitals, used deliberately. If you write MUST, a conforming implementation has to reject documents that break it, and the schema has to enforce it.
- Normative statements go in `SPEC.md`. Rationale, worked examples and opinion go in `README.md` or a discussion.
- British or American spelling both fine. Don't change existing text to switch between them.

## Reference implementations

Implementations live in sibling repositories, not here. This repo contains the schema, the spec text and the conformance fixtures — nothing that has to be installed from a package manager.

If you write an implementation in a language that doesn't have one, open a discussion and it can be linked from the README. The only requirement for being listed is that it passes the conformance suite in `tests/`.

## Licensing of contributions

By contributing you agree that your contributions are licensed under the same terms as the material they modify: Apache-2.0 for schema, fixtures and code, CC BY 4.0 for spec text and documentation. See `LICENSING.md`.

There is no CLA. If FPDS later moves to neutral governance, contributions travel with it under these licences.
