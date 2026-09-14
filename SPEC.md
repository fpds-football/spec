# Football Player Data Standard (FPDS)

**Version:** 0.1.0 (draft, not released) **Schema:** `https://fpds.football/schema/v0.1/player.json`

In this document, the key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY have the meanings that RFC 2119 gives them. They have these meanings only when they are in capitals.

---

## 1. Scope

FPDS defines the structure of a **player submission**. A player submission is one document about one player. One party sends it to another party about a possible permanent transfer, loan or trial.

The sender is an intermediary or the player. §4 defines the two senders.

FPDS does not define transport, authentication, sessions or acknowledgements. It is a data standard, not a protocol.

## 2. Design principles

1. **Every number has its denominator.** Output without minutes is not information.
2. **Provenance is a field, not metadata.** A submission states who made each claim, and when.
3. **Unknown is a value, not a gap.** A required field that can be unknown has the value `unknown`. A missing optional field means "not stated". `null` is not a value in FPDS.
4. **The core is small, and extensions are open.** The core contains only the fields that FPDS cannot work without. New fields enter the core after public consultation.
5. **FPDS uses existing identifiers and definitions.** It uses FIFA Connect identifiers and FIFA definitions where they exist. It does not issue new player identifiers.

## 3. Document structure

A submission is one JSON object with these members:

| Member | Required | Contents | Section |
|---|---|---|---|
| `fpds_version` | yes | The version of FPDS that the document uses | §3 |
| `submission` | yes | The submission identifier, time, purposes and sender | §4 |
| `player` | yes | The identity of the player | §5 |
| `positions` | yes | The primary position and secondary positions | §6 |
| `contract` | yes | The contract status of the player | §7 |
| `representation` | when the sender is `intermediary` | The agent and the mandate | §8 |
| `performance` | no | Season records | §9 |
| `consent` | yes | The lawful basis for sharing the data | §10 |
| `provenance` | no | The source of each claim | §11 |
| `extensions` | no | Fields that are not in the core | §12 |

These rules apply to the full document:

- `fpds_version` is a semantic version string. For this version of the schema, it MUST match `0.1.x`.
- A document MUST NOT contain a member that this specification does not define, except inside `extensions`.
- A document MUST NOT contain `null` as a value.
- A date MUST use the format `YYYY-MM-DD` (ISO 8601). A timestamp MUST use the RFC 3339 format with a time zone, for example `2026-09-13T09:41:00Z`.
- Producers MUST NOT put a local date format, such as `07/03/1998`, in a date field. Consumers SHOULD show dates in the local format of the reader.
- A country code MUST be an ISO 3166-1 alpha-3 code in uppercase, for example `POL`.
- A document MUST be JSON encoded in UTF-8. Its media type is `application/json`.
- When a document is stored or sent as a file, the file name SHOULD end with `.fpds.json`, for example `joao-costa-2026-09-14.fpds.json`. People and software can then recognise the file as an FPDS document.

## 4. Submission

| Field | Type | Required | Notes |
|---|---|---|---|
| `submission_id` | UUID | yes | Identifies this version of the document. See §4.3. |
| `submitted_at` | timestamp | yes | The time that the producer made this version of the document. See §4.3. |
| `purposes` | array of enum | yes | One or more of `permanent_transfer`, `loan`, `trial`, `information_only`. |
| `sender` | enum | yes | `intermediary` or `player`. |

### 4.1 Purposes

`purposes` MUST contain at least one value, and each value MUST occur only once. A player can be available for more than one type of deal, for example `["permanent_transfer", "loan"]`.

`information_only` means that the sender does not offer the player for a deal. If `purposes` contains `information_only`, it MUST NOT contain another value.

### 4.2 Sender

| Value | Meaning |
|---|---|
| `intermediary` | An agent or another party sends the submission for the player or for a club. |
| `player` | The player sends their own submission. |

If `sender` is `intermediary`, the document MUST contain `representation`.

If `sender` is `player`, the document MAY contain `representation`. A player who has an agent can send their own profile and name the agent.

If `consent.is_minor` is `true`, `sender` MUST NOT be `player`. §10 gives the reason.

### 4.3 Submission ID and versions

A receiver uses `submission_id` to recognise the same document when it arrives more than once. This includes a copy that another party forwards. `submission_id` does not identify the player, and it does not prove who sent the document.

- `submission_id` MUST be a UUID as defined in RFC 9562, in lowercase, with hyphens. For example: `b7f3c2e1-4a9d-4f11-9c3e-2a1d5f8b0c44`.
- A producer SHOULD use UUID version 4 (random) or version 7 (time-ordered).
- Each version of a document has its own `submission_id`. If any value in the document changes, the producer MUST make a new `submission_id` and a new `submitted_at`.
- If a party sends or forwards a document without changes, `submission_id` and `submitted_at` MUST NOT change.
- `submitted_at` is the time that the producer made this version. It is not the time that a party sent the document.
- The receiver MUST NOT give `submission_id` any other meaning.

FPDS 0.1 does not link a new version to the version that it replaces. This is open question OQ-24.

## 5. Identity

| Field | Type | Required | Notes |
|---|---|---|---|
| `full_name` | string | yes | The name as it appears on the passport. |
| `date_of_birth` | date | yes | |
| `nationalities` | array of country codes | yes | At least one. Sporting nationality first. Each value occurs only once. |
| `current_club` | club | see §7 | The club where the player plays now. |
| `external_ids.fifa_connect_id` | string | no | The FIFA Connect identifier of the player. |

A club has two required fields: `name` and `country`.

`fifa_connect_id` SHOULD be present when the sender knows it.

There is no universal player identifier in practice. A consumer that matches a submission against its own records SHOULD use `full_name`, `date_of_birth` and `nationalities` together as a fallback key. The consumer SHOULD use fuzzy matching on the name. An implementation MUST NOT use `full_name` alone to identify a player.

## 6. Positions

| Field | Type | Required |
|---|---|---|
| `primary_position` | position code | yes |
| `secondary_positions` | array of position codes | no. Maximum four. Each code occurs only once, and the array MUST NOT contain the primary position. |

A position code MUST be one of these values. Codes are uppercase.

| Code | Meaning |
|---|---|
| `GK` | Goalkeeper |
| `RB` / `LB` | Right-back / left-back |
| `RWB` / `LWB` | Right wing-back / left wing-back |
| `CB` | Centre-back who plays on the left and on the right |
| `LCB` / `RCB` | Centre-back who plays on the left only / on the right only |
| `CDM` | Defensive midfielder (the 6) |
| `CM` | Central midfielder (the 8) |
| `CAM` | Attacking midfielder (the 10) |
| `RM` / `LM` | Right midfielder / left midfielder, in a line of four or five |
| `RW` / `LW` | Right winger / left winger |
| `ST` | Striker |

A centre-back who plays on the two sides is `CB`. The sender MUST NOT describe this player as `LCB` with `RCB` as a secondary position.

Player submissions often misuse the difference between `CDM`, `CM` and `CAM`. FPDS makes this difference mandatory. "Centre mid" is not a valid value.

## 7. Contract

| Field | Type | Notes |
|---|---|---|
| `status` | enum | Required. See §7.1. |
| `expiry_date` | date | See §7.2. |
| `parent_club` | club | See §7.2. |

### 7.1 Status

The words "professional" and "amateur" have the meanings in Article 2 of the FIFA Regulations on the Status and Transfer of Players. A professional has a written contract and receives more than their expenses. All other players are amateurs.

| Value | Meaning |
|---|---|
| `under_contract` | A professional with a contract at `current_club`. |
| `on_loan` | A professional with a contract at `parent_club`, who plays for `current_club` on loan. |
| `amateur` | A player who is registered with a club and is not a professional. Academy players who are not professionals are `amateur`. |
| `free_agent` | A player who is not registered with any club. |
| `unknown` | The sender does not know the contract status. |

### 7.2 Fields for each status

| `status` | `player.current_club` | `expiry_date` | `parent_club` |
|---|---|---|---|
| `under_contract` | MUST be present | MUST be present | MUST NOT be present |
| `on_loan` | MUST be present | MUST be present | MUST be present |
| `amateur` | MUST be present | MUST NOT be present | MUST NOT be present |
| `free_agent` | MUST NOT be present | MUST NOT be present | MUST NOT be present |
| `unknown` | MAY be present | MUST NOT be present | MUST NOT be present |

For `under_contract`, `expiry_date` is the end date of the contract at `current_club`. For `on_loan`, `expiry_date` is the end date of the contract at `parent_club`. `parent_club` is the club that holds the registration of the player.

## 8. Representation

| Field | Type | Required | Notes |
|---|---|---|---|
| `agent_name` | string | yes | The name of the agent. |
| `fifa_agent_licence` | string | no | The FIFA licence number of the agent, if the agent has one. |
| `mandate_status` | enum | yes | `exclusive`, `non_exclusive`, `club_mandate`, `none`, `unknown`. |

§4.2 states when `representation` is required.

| `mandate_status` | Meaning |
|---|---|
| `exclusive` | The agent has an exclusive mandate from the player. |
| `non_exclusive` | The agent has a mandate from the player, and other agents can also have one. |
| `club_mandate` | The agent acts for a club, not for the player. |
| `none` | The agent has no mandate. |
| `unknown` | The sender does not state the mandate. |

Consumers SHOULD process submissions with `none` or `unknown` differently from submissions with a mandate. Recruitment departments lose much time on submissions from parties that have no authority to make them.

## 9. Performance

`performance` is an array of season records. Each record has these fields:

| Field | Type | Required | Notes |
|---|---|---|---|
| `season` | string | yes | See §9.1. |
| `competition` | string | yes | The name of the competition. |
| `competition_country` | country code | yes | |
| `appearances` | integer | yes | Zero or more. |
| `minutes` | integer | yes | Zero or more. |
| `goals` | integer | no | Zero or more. |
| `assists` | integer | no | Zero or more. |
| `clean_sheets` | integer | no | Zero or more. See §9.2. |

`minutes` is required in every record. Output without minutes is not information.

A record MUST NOT contain per-90 figures. Consumers calculate them from `minutes` and the output. If a document contains both the figure and its inputs, the two can disagree.

A missing output field means "not stated". It does not mean zero.

### 9.1 Season

`season` has one of two formats:

| Format | Use | Example |
|---|---|---|
| `YYYY/YY` | A season that crosses two calendar years | `2025/26` |
| `YYYY` | A season in one calendar year | `2026` |

The separator is a slash. In the `YYYY/YY` format, the second part MUST be the year after the first part.

### 9.2 Clean sheets

`clean_sheets` is the number of appearances in which the team of the player conceded no goals while the player was on the pitch. It applies to all positions.

## 10. Consent and minors

| Field | Type | Required | Notes |
|---|---|---|---|
| `lawful_basis` | enum | yes | `consent`, `contract`, `legitimate_interest`, `legal_obligation`, `not_stated`. |
| `consent_date` | date | when `lawful_basis` is `consent` | The date that the data subject gave consent. |
| `is_minor` | boolean | yes | See §10.1. |

The values of `lawful_basis` agree with the lawful bases in Article 6 of the GDPR. A producer in another jurisdiction uses the value that is nearest to its own law. `not_stated` means that the sender does not state a lawful basis.

### 10.1 Minors

A minor is a person who is less than 18 years old. This agrees with Article 19 of the FIFA Regulations on the Status and Transfer of Players.

`is_minor` MUST be `true` if the player is less than 18 years old on the date of `submission.submitted_at`. Otherwise it MUST be `false`. The producer MUST calculate `is_minor` from `player.date_of_birth`. The producer MUST NOT set it independently.

These rules apply to the calculation:

- The date of `submitted_at` is the calendar date in the timestamp, with the time zone offset that the timestamp states. For example, the date of `2026-09-14T23:30:00-05:00` is 14 September 2026.
- A player becomes 18 years old at the start of their 18th birthday.
- A player born on 29 February becomes 18 years old on 1 March, when the year of their 18th birthday is not a leap year. On 28 February of that year, the player is still a minor.

A minor MUST NOT send their own submission, so `sender` MUST NOT be `player` when `is_minor` is `true`. Profiles of minors that go directly to clubs are a safeguarding risk.

FIFA regulations on the protection of minors and national safeguarding rules apply to submissions about minors. FPDS does not encode those rules. Implementations that process data about minors need their own legal advice. The `is_minor` flag lets systems send these submissions through a different process.

## 11. Provenance

`provenance` is an object. Each key is a JSON Pointer (RFC 6901) to a value in the same document. Each value is an object with these fields:

| Field | Type | Required | Notes |
|---|---|---|---|
| `source` | enum | yes | See the table below. |
| `asserted_by` | string | no | The party or data provider that made the claim. |
| `asserted_at` | timestamp | no | The time of the claim. |
| `verified_against` | string | when `source` is `verified` | The record that the claim was checked against. |

| `source` | Meaning |
|---|---|
| `verified` | Somebody checked the claim against an official record. |
| `third_party_data` | A data provider supplied the value. |
| `club_stated` | A club stated the value. |
| `agent_stated` | An agent stated the value. |
| `player_stated` | The player stated the value. |
| `estimated` | The value is an estimate. |
| `unknown` | The source is not known. |

### 11.1 Rules

- Each key MUST resolve to a value in the same document.
- An entry applies to the value at its pointer and to all values below that pointer. If a more specific entry exists, the more specific entry applies.
- If a value has no entry, its source is the sender. The source is `agent_stated` when `sender` is `intermediary`, and `player_stated` when `sender` is `player`.
- `asserted_by` is free text for display. It does not identify a party.
- Provenance records who made a claim. It is not authentication, and it does not prove that the named party sent the document.

A producer does not need to write provenance. A document without provenance is still correct about what it is: every value comes from the sender.

Consumers SHOULD show the source of each value. If a consumer shows a verified value and an unverified value in the same way, provenance has no purpose.

## 12. Extensions

`extensions` is an object for fields that are not in the core.

- Each key MUST have the format `<reverse domain name>/<field name>`, for example `com.example/scouting_grade`.
- The reverse domain name MUST have two or more labels. Each label contains only lowercase letters, digits and hyphens, and does not start or end with a hyphen.
- The field name MUST start with a lowercase letter. It contains only lowercase letters, digits and underscores.
- The domain name SHOULD be a domain that the producer controls.
- A key MUST NOT start with the reserved prefix `football.fpds`.
- A producer MUST NOT put diagnoses, injury details or medical history in `extensions`. A value that states only whether a player is available is permitted.
- Consumers MUST ignore extension keys that they do not recognise.

Software cannot always decide whether a value contains medical information, so the producer is responsible for the medical rule. A consumer or a validator MAY show a warning when an extension appears to contain medical information. A warning does not make a document invalid.

This example shows two producers with fields of the same name:

```json
"extensions": {
  "com.example/scouting_grade": "B+",
  "uk.co.example/eligibility": { "gbe_points": 15 }
}
```

A field that many independent producers use is a candidate for the core. §14 and `GOVERNANCE.md` describe how a field enters the core.

## 13. Conformance

A **producer** is software that makes FPDS documents. Examples are agency software, a scouting platform, a club system, and a form that makes a file. People do not usually write FPDS documents by hand.

A **conforming producer** makes documents that are valid against the published schema for the version in `fpds_version`, and that obey the rules in §13.1. For each document, a conforming producer does these steps:

1. Set `fpds_version` to the version of FPDS that it uses.
2. Make a new `submission_id` and set `submitted_at` to the current time (§4.3).
3. Calculate `consent.is_minor` from `player.date_of_birth` and `submitted_at` (§10.1).
4. Remove each field that does not apply, for example `expiry_date` for a `free_agent` (§7.2).
5. Make sure that `extensions` contains no medical information (§12).
6. Validate the document against the schema and the rules in §13.1.
7. Write the document as UTF-8 JSON (§3).

If a producer changes a document that it received or made before, it does all the steps again. Step 2 then gives the changed document a new `submission_id`.

A **conforming consumer** accepts all valid documents for the versions that it supports. It ignores extension keys that it does not recognise. It does not reject a document only because the document contains optional fields that the consumer does not use.

A validator MUST treat the `format` keywords `date` and `date-time` in the schema as assertions, not only as annotations. The conformance suite in `tests/conformance/` makes this assumption.

### 13.1 Rules that the schema cannot enforce

JSON Schema cannot express these rules. Software can check each rule with certainty. A conforming implementation MUST enforce each one.

1. `consent.is_minor` agrees with `player.date_of_birth` on the date of `submission.submitted_at` (§10.1).
2. In a `YYYY/YY` season, the second part is the year after the first part (§9.1).
3. Each key in `provenance` resolves to a value in the same document (§11.1).
4. `positions.secondary_positions` does not contain the value of `positions.primary_position` (§6).

The rule about medical information in `extensions` is not in this list, because software cannot check it with certainty. §12 makes the producer responsible for it.

## 14. Open questions

These questions are not answered. Each question has an ID that does not change. The "v0.1.0 ships" column states what implementations do until the question has an answer.

Agents, clubs and other parties answer questions through the consultation pages on `https://fpds.football`. Technical questions use GitHub Discussions only. `DECISIONS.md` records each answer.

| ID | Question | v0.1.0 ships | Consultation |
|---|---|---|---|
| OQ-1 | Does FPDS need a level for each competition? Is a free integer sufficient, or is a league-strength index necessary? | No competition level | Not yet open |
| OQ-2 | Is information about wages or salary in scope, or is it too commercially sensitive for a document that parties forward? | No wage fields | [Open](https://fpds.football/consult/wages) |
| OQ-3 | Does FPDS need signed submissions, so that a club can make sure that a submission came from the agent that it names? | No signatures | GitHub Discussion |
| OQ-4 | Do eligibility rules for each country (for example, GBE points in England) belong in the core, or in extensions? | No eligibility fields | Not yet open |
| OQ-5 | Does FPDS define a receipt or rejection document, or is that a protocol? | No receipt document | GitHub Discussion |
| OQ-6 | How does FPDS describe a player whose full date of birth is not known? | A full date of birth is required | Not yet open |
| OQ-7 | Does FPDS need to show the difference between "not disclosed" and "not known"? | A missing field means "not stated" | GitHub Discussion |
| OQ-8 | How does a submission record the consent of a parent or guardian for a minor? | No field for who gave consent | Not yet open |
| OQ-9 | Does `free_agent` need to separate players whose professional contract ended from players who were never professionals? | One value, `free_agent` | Not yet open |
| OQ-10 | Does FPDS need side-specific codes for more central positions? | `LCB` and `RCB` only | Not yet open |
| OQ-11 | Does `asserted_by` need a structured format? | Free text | GitHub Discussion |
| OQ-12 | Can a parent, a guardian or a club send a submission? | `intermediary` or `player` only | Not yet open |
| OQ-13 | Do clubs need youth or academy categories in addition to `amateur`? | `amateur` only | Not yet open |
| OQ-14 | Do release clauses and sell-on percentages belong in a submission? | No release clause or sell-on fields | [Open](https://fpds.football/consult/release-clauses) |
| OQ-15 | Does a submission state medical availability, and where does availability end and health data start? | No medical fields | [Open](https://fpds.football/consult/medical-availability) |
| OQ-16 | Does a submission state contract extension options, and which party holds them? | No extension option field | Not yet open |
| OQ-17 | Does a submission include links to video and scouting reports? | No media fields | Not yet open |
| OQ-18 | Is the agent licence sufficient, or do clubs need the agency name and the mandate expiry date? | `agent_name`, `fifa_agent_licence`, `mandate_status` | Not yet open |
| OQ-19 | Does a submission include the common name or shirt name of the player? | Full name only | Not yet open |
| OQ-20 | Does a submission state commercial terms, such as asking price, loan fee and availability date? | `purposes` only | Not yet open |
| OQ-21 | Which identifiers other than FIFA Connect belong in the core? | `fifa_connect_id` only | GitHub Discussion |
| OQ-22 | Which performance figures other than goals, assists and clean sheets belong in the core (for example starts, goals conceded, saves)? | Goals, assists, clean sheets | Not yet open |
| OQ-23 | Does a submission include a physical profile, such as preferred foot and height? | No physical profile | Not yet open |
| OQ-24 | Does a new version of a submission link to the version that it replaces? | No link between versions | GitHub Discussion |
| OQ-25 | Does FPDS define a way to share a submission as a link, not as a file? | Files only | GitHub Discussion |
