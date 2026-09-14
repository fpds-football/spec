# Football Player Data Standard (FPDS)

**Version:** 0.1.0 (draft) **Date:** 2026-09-13 **Schema:** `https://fpds.football/schema/v0.1/player.json`

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are to be interpreted as described in RFC 2119.

---

## 1. Scope

FPDS defines the structure of a **player submission**: a single document describing one player, sent from one party to another for the purpose of a potential transfer, loan, trial or registration.

FPDS does not define transport, authentication, session handling or acknowledgement. It is a data standard, not a protocol.

## 2. Design principles

1. **Every number carries its denominator.** Output without minutes is not information.
2. **Provenance is a first-class field, not metadata.** A submission states who claimed what and when.
3. **Absence is explicit.** `null` with a stated reason beats a missing key.
4. **Small core, open extensions.** Twenty fields in the core. Everything else goes in `extensions`.
5. **Follow existing identifiers.** FIFA Connect where it exists. Do not mint new player IDs.

## 3. Document structure

A submission is a single JSON object with these top-level members:

|Member|Required|Description|
|---|---|---|
|`fpds_version`|yes|Semver string of the spec version used|
|`submission`|yes|Who sent this, when, and why|
|`player`|yes|Identity block|
|`positions`|yes|Primary and secondary positions|
|`contract`|yes|Current contractual situation|
|`representation`|yes|Mandate and licensing|
|`availability`|no|What is being offered and on what terms|
|`performance`|no|Season-by-season record|
|`eligibility`|no|Passports, permits, registration categories|
|`medical`|no|Availability status only — see §9|
|`media`|no|Video and report links|
|`consent`|yes|Lawful basis for sharing this data|
|`provenance`|no|Claim-level sourcing, keyed by JSON Pointer|
|`extensions`|no|Implementation-specific additions|

## 4. Identity

### 4.1 `player`

|Field|Type|Required|Notes|
|---|---|---|---|
|`full_name`|string|yes|As it appears on the passport|
|`known_as`|string|no|Common or shirt name|
|`date_of_birth`|date|yes|ISO 8601 `YYYY-MM-DD`|
|`nationalities`|array of string|yes|ISO 3166-1 alpha-3, sporting nationality first|
|`preferred_foot`|enum|no|`left`, `right`, `both`, `unknown`|
|`height_cm`|integer|no||
|`current_club`|object|yes|`name`, `country`, `competition`, `id`|
|`external_ids`|object|no|See §4.2|

### 4.2 Identifiers

There is no universal player key in practice, so FPDS carries whatever is available:

```json
"external_ids": {
  "fifa_connect_id": "1234567890",
  "transfermarkt_id": "418560",
  "wyscout_id": "351942",
  "opta_id": "p123456"
}
```

`fifa_connect_id` SHOULD be populated where known. Consumers matching submissions against their own records SHOULD use the composite of `full_name`, `date_of_birth` and `nationalities` as a fallback key, with fuzzy matching on name.

Implementations MUST NOT treat `full_name` alone as identifying.

## 5. Positions

`primary_position` is required and MUST be one of:

|Code|Meaning|
|---|---|
|`GK`|Goalkeeper|
|`RB` / `LB`|Full-back|
|`RWB` / `LWB`|Wing-back|
|`CB`|Centre-back|
|`DM`|Defensive midfielder — the 6|
|`CM`|Central midfielder — the 8|
|`AM`|Attacking midfielder — the 10|
|`RM` / `LM`|Wide midfielder|
|`RW` / `LW`|Winger|
|`SS`|Second striker|
|`ST`|Centre-forward|

`secondary_positions` is an array of the same codes.

The distinction between `DM`, `CM` and `AM` is the single most abused piece of information in player submissions and is deliberately non-optional. "Centre mid" is not a valid value.

## 6. Contract

|Field|Type|Notes|
|---|---|---|
|`status`|enum|`under_contract`, `free_agent`, `on_loan`, `youth_scholarship`, `unattached`, `unknown`|
|`expiry_date`|date|Required when `status` is `under_contract` or `on_loan`|
|`option_to_extend`|boolean||
|`release_clause`|money object|`amount`, `currency`, `conditions`|
|`sell_on_percentage`|number|0–100|
|`parent_club`|object|Required when `status` is `on_loan`|

Money objects use ISO 4217 currency codes and integer minor units, to avoid float rounding:

```json
{ "amount": 250000000, "currency": "GBP" }
```

That is £2,500,000.

## 7. Representation

|Field|Type|Required|Notes|
|---|---|---|---|
|`agent_name`|string|yes||
|`agency`|string|no||
|`fifa_agent_licence`|string|no|Licence number where held|
|`mandate_status`|enum|yes|`exclusive`, `non_exclusive`, `club_mandate`, `none`, `unknown`|
|`mandate_expiry`|date|no||

`mandate_status` of `unknown` is permitted, but consumers SHOULD treat submissions with `none` or `unknown` differently from mandated ones. A large share of wasted recruitment time comes from submissions by parties with no authority to make them.

## 8. Performance

An array of season records. Each record:

|Field|Type|Required|
|---|---|---|
|`season`|string (`2025/26`)|yes|
|`competition`|string|yes|
|`competition_country`|string (alpha-3)|yes|
|`competition_tier`|integer|no|
|`appearances`|integer|yes|
|`starts`|integer|no|
|`minutes`|integer|**yes**|
|`goals`|integer|no|
|`assists`|integer|no|

`minutes` is required whenever any output figure is present. A record stating `goals` without `minutes` is invalid.

Per-90 figures MUST NOT be included as stored fields. They are derived, and storing them invites inconsistency between the derived value and its inputs.

## 9. Medical

FPDS carries **availability status only**:

- `current_status`: `available`, `unavailable`, `managed_load`, `unknown`
- `expected_return_date`: date

Diagnoses, injury history and medical records are out of scope. In most jurisdictions this is health data attracting a higher standard of protection, and it does not belong in a document forwarded between parties. Where it must be exchanged, it should travel under a separate, consented process.

## 10. Consent and minors

|Field|Type|Required|
|---|---|---|
|`lawful_basis`|enum|yes|
|`consent_obtained`|boolean|yes|
|`consent_date`|date|no|
|`subject_is_minor`|boolean|yes|

`subject_is_minor` MUST be computed from `date_of_birth` against the date of submission and MUST NOT be asserted independently.

Submissions concerning minors are subject to FIFA regulations on the protection of minors and to national safeguarding rules. FPDS does not attempt to encode those rules. Implementations handling minors' data should take their own legal advice; the flag exists so that systems can route these submissions differently rather than treat them as routine.

## 11. Provenance

`provenance` is an object whose keys are JSON Pointers (RFC 6901) into the same document, and whose values are:

|Field|Type|Notes|
|---|---|---|
|`source`|enum|`verified`, `third_party_data`, `club_stated`, `agent_stated`, `estimated`, `unknown`|
|`asserted_by`|string|Party or provider|
|`asserted_at`|timestamp|ISO 8601|
|`verified_against`|string|Required when `source` is `verified`|

Any value with no corresponding provenance entry is treated as `agent_stated`. This keeps the burden low: an agent typing a submission by hand need write no provenance at all, and the document is still honest about what it is.

Consumers SHOULD render sourcing visibly. Presenting a verified figure and an unverified one identically defeats the purpose of the format.

## 12. Extensions

`extensions` is a free-form object. Keys SHOULD be namespaced by a reverse-DNS prefix to avoid collisions:

```json
"extensions": {
  "football.fpds.example/scouting_grade": "B+",
  "com.exampleclub/internal_ref": "SCT-2026-118"
}
```

Consumers MUST ignore extensions they do not recognise. Fields that prove broadly useful are candidates for promotion into the core in a later minor version.

## 13. Conformance

A **conforming producer** emits documents that validate against the published schema for the version stated in `fpds_version`.

A **conforming consumer** accepts any valid document for a version it supports, ignores unrecognised extension keys, and does not reject a document solely for containing optional fields it does not use.

## 14. Open questions for v0.2

These are unresolved and feedback is specifically wanted:

1. Should `competition_tier` be a free integer, or a controlled league-strength index? An integer is honest but not comparable across countries.
2. Is a wage or salary block in scope, or is it too commercially sensitive to travel in a forwardable document?
3. Should there be a signed-submission mechanism, so a receiving club can verify a submission genuinely came from the licensed agent it names?
4. Does `eligibility` need country-specific sub-objects (GBE points for England, non-EU slots for Italy and Spain), or does that belong in `extensions`?
5. Should FPDS define a rejection or receipt document, or does that push it into protocol territory it should stay out of?
