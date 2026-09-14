# Conformance suite

The fixtures in `conformance/` state what FPDS accepts and what it rejects, in a format that a machine can read. If `SPEC.md` and a fixture disagree, one of them has a defect. Report the disagreement as an issue.

An implementation passes the conformance suite if it gives the same verdict as the fixture for every case. A verdict is "valid" or "invalid". This is the only requirement for an implementation to be listed as an FPDS implementation.

## Fixture format

Each file covers one area of the specification. Each case is a [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) that the runner applies to a valid base document. A patch shows only the thing that the case tests.

```json
{
  "description": "Contract status, current club and loans (SPEC section 7)",
  "schema": "schema/v0.1/player.json",
  "base": "examples/valid/midfielder-under-contract.json",
  "tests": [
    {
      "description": "under_contract without an expiry date is rejected",
      "patch": [
        { "op": "remove", "path": "/contract/expiry_date" },
        { "op": "remove", "path": "/provenance/~1contract~1expiry_date" }
      ],
      "valid": false
    }
  ]
}
```

| Key | Meaning |
|---|---|
| `schema` | The path from the repository root to the schema for the cases |
| `base` | The path to a valid document. The runner applies each patch in the file to this document. |
| `tests[].patch` | RFC 6902 operations. An empty array tests the base document without changes. |
| `tests[].valid` | `true` if the patched document is valid, `false` if it is invalid |

Inside a JSON Pointer, `/` in a key becomes `~1`. The keys of the `provenance` object are pointers, so a patch writes the entry for `/contract/expiry_date` as `/provenance/~1contract~1expiry_date`.

Keep each patched document consistent. If a patch removes a value, it also removes the provenance entry for that value. Otherwise the case breaks rule 3 in §13.1 of `SPEC.md`.

## Run the suite

```bash
pip install -r tests/requirements.txt
python3 tests/run_conformance.py
```

`run_conformance.py` is repository infrastructure. It is not a reference implementation. It uses Python because CI runners have Python, and FPDS does not depend on it. An implementation in another language runs these fixtures through its own validator.

The runner treats `format: date` and `format: date-time` as assertions. §13 of `SPEC.md` requires this. If your validator treats `format` as an annotation only, some cases give the wrong verdict.

## Add a case

Each schema change needs at least one case that fails before the change and passes after it. If a schema change adds no case and all cases still pass, the change does nothing, or the suite has a gap.

Each case tests one thing. A patch with six operations usually contains two cases. Operations that only keep the document consistent, such as the removal of a provenance entry, do not count.

Before you add a case, make sure that the runner rejects the document for the reason in the description, not for a different reason.

## What the suite does not test

The suite tests only what JSON Schema can express. §13.1 of `SPEC.md` lists the rules that implementations enforce themselves:

1. `consent.is_minor` agrees with `player.date_of_birth` on the date of `submission.submitted_at`.
2. In a `YYYY/YY` season, the second part is the year after the first part.
3. Each key in `provenance` resolves to a value in the same document.
4. `extensions` contains no diagnoses, injury details or medical history.
5. `positions.secondary_positions` does not contain the primary position.

These rules belong in the test suites of implementations. If many implementations make the same checks, that is a reason to find a way to put the checks in the schema.

The suite also does not test whether values are plausible. For example, 30 appearances in 40 minutes is valid.
