#!/usr/bin/env python3
"""Run the FPDS conformance suite.

This is repository infrastructure, not a reference implementation. The fixtures
under tests/conformance/ are the normative artefact; this script is one way of
executing them. Any implementation in any language can run the same fixtures by
applying the JSON Patch to the base document and checking the result against the
schema. See tests/README.md for the fixture format.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonpatch
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    sys.exit("Missing dependencies. Run: pip install jsonschema jsonpatch rfc3339-validator")

ROOT = Path(__file__).resolve().parent.parent
FIXTURE_DIR = ROOT / "tests" / "conformance"

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
RESET = "\033[0m"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def run_fixture(path: Path) -> tuple[int, int]:
    fixture = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        load(fixture["schema"]), format_checker=FormatChecker()
    )
    base = load(fixture["base"])

    print(f"\n{fixture['description']}  {DIM}({path.relative_to(ROOT)}){RESET}")

    passed = failed = 0
    for case in fixture["tests"]:
        document = jsonpatch.JsonPatch(case["patch"]).apply(base)
        errors = sorted(validator.iter_errors(document), key=lambda e: list(e.path))
        actually_valid = not errors

        if actually_valid == case["valid"]:
            passed += 1
            print(f"  {GREEN}pass{RESET}  {case['description']}")
        else:
            failed += 1
            print(f"  {RED}FAIL{RESET}  {case['description']}")
            expected = "valid" if case["valid"] else "invalid"
            print(f"        expected {expected}, got {'valid' if actually_valid else 'invalid'}")
            for error in errors[:3]:
                pointer = "/" + "/".join(str(p) for p in error.path)
                print(f"        {DIM}{pointer}: {error.message}{RESET}")

    return passed, failed


def main() -> int:
    fixtures = sorted(FIXTURE_DIR.rglob("*.json"))
    if not fixtures:
        sys.exit(f"No fixtures found under {FIXTURE_DIR}")

    total_passed = total_failed = 0
    for path in fixtures:
        passed, failed = run_fixture(path)
        total_passed += passed
        total_failed += failed

    print(f"\n{len(fixtures)} fixture files, {total_passed + total_failed} cases")
    if total_failed:
        print(f"{RED}{total_failed} failed{RESET}, {total_passed} passed")
        return 1
    print(f"{GREEN}all {total_passed} passed{RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
