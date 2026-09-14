# Applying `fpds-repo-additions.zip`

Everything in the zip is either new or a safe overwrite. It does not touch `README.md`, `SPEC.md`, `LICENSE`, `LICENSE-DOCS` or `LICENSING.md` — those stay as they are.

```bash
cd path/to/your/spec-repo
unzip -o ~/Downloads/fpds-repo-additions.zip
git status
```

Then one manual step, because git needs to see it as a move:

```bash
git rm examples/midfielder-under-contract.json
```

The same file now lives at `examples/valid/midfielder-under-contract.json`. Its content is unchanged apart from canonical JSON formatting.

## Two edits before you commit

**`README.md` — the repo layout block.** Replace it with:

```
schema/v0.1/player.json     JSON Schema (2020-12)
examples/valid/             worked submissions that validate
tests/conformance/          the machine-readable accept/reject suite
SPEC.md                     the normative document
CHANGELOG.md                what changed between versions
GOVERNANCE.md               who decides, and the conflicts of interest
```

**`CODE_OF_CONDUCT.md` and `SECURITY.md`** both reference `conduct@fpds.football` and `security@fpds.football`. Set those up as forwarding aliases on the domain, or change them to an address that exists. A reporting address that bounces is worse than no code of conduct.

## Verify locally

```bash
pip install -r tests/requirements.txt
python3 tests/run_conformance.py
check-jsonschema --schemafile schema/v0.1/player.json examples/valid/*.json
```

43 cases, all passing as shipped.

## Turning on Pages

`Settings → Pages → Source: GitHub Actions`. The `pages.yml` workflow publishes the repository root, so `https://fpds.football/schema/v0.1/player.json` resolves to the real schema file and `https://fpds.football/` serves `index.html`.

DNS at your registrar:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<your-org>.github.io` |

Then tick "Enforce HTTPS" once the certificate provisions, which usually takes under an hour.

## Repo settings worth setting now

- Discussions **on**, with categories: `Field proposals`, `Q&A`, `Show and tell`. The issue template config links to the first two.
- Issues **on** but limited to the two forms provided — blank issues are disabled in `config.yml`.
- Branch protection on `main`: require the `validate` workflow to pass.
- Tag `v0.1.0` and cut a release once this lands.
