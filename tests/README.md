# Conformance suite

The fixtures under `conformance/` are the machine-readable statement of what FPDS accepts and rejects. Where `SPEC.md` and the fixtures disagree, one of them is a bug and the disagreement should be reported.

An implementation "passes the conformance suite" if, for every case, it reaches the same accept/reject verdict as the fixture states. That is the only requirement for being listed as an FPDS implementation.

## Fixture format

Each file describes one area of the spec. Cases are expressed as a [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) applied to a known-good document, rather than as whole documents, so that a case shows only the thing under test.

```json
{
  "description": "Contract status conditionals (SPEC section 6)",
  "schema": "schema/v0.1/player.json",
  "base": "examples/valid/midfielder-under-contract.json",
  "tests": [
    {
      "description": "under_contract without an expiry date is rejected",
      "patch": [{ "op": "remove", "path": "/contract/expiry_date" }],
      "valid": false
    }
  ]
}
```

| Key | Meaning |
|---|---|
| `schema` | Path from the repository root to the schema the cases are checked against |
| `base` | Path to a valid document that every patch in this file is applied to |
| `tests[].patch` | RFC 6902 operations. An empty array tests the base document unmodified |
| `tests[].valid` | Whether the patched document must be accepted |

Remember that `/` inside a JSON Pointer key is escaped as `~1`. The `provenance` object is keyed by pointers, so its entries appear in patches as `/provenance/~1contract~1expiry_date`.

## Running the suite

```bash
pip install -r tests/requirements.txt
python3 tests/run_conformance.py
```

`run_conformance.py` is repository infrastructure, not a reference implementation. It happens to be Python because CI runners have Python; nothing about FPDS depends on it. An implementation in another language should run these fixtures through its own validator rather than shelling out to this script.

## Adding a case

Every schema change needs at least one case that fails before the change and passes after it. If a change to `schema/v0.1/player.json` leaves all 43 existing cases green and adds none, either the change does nothing or the suite has a gap.

Cases should test one thing. A patch with six operations in it is usually two cases.

## What the suite does not cover

Constraints the spec states but JSON Schema cannot enforce:

- **`subject_is_minor` must be computed from `date_of_birth`.** The schema can only check that the field is a boolean. A conforming implementation has to derive it, and the suite cannot catch one that doesn't.
- **Provenance pointers must resolve.** A `provenance` key can be a well-formed JSON Pointer that points at nothing. The schema accepts it; a good implementation warns.
- **Appearances, starts and minutes must be mutually plausible.** 30 appearances in 40 minutes validates.

These belong in implementation test suites rather than here. If enough implementations converge on the same checks, that is an argument for finding a way to express them in the schema.
