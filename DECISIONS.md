# Decisions

This file records why FPDS is the way it is. `CHANGELOG.md` records what changed. This file records the reasons.

Each entry has an ID, a date, a status, the decision, the reason, and the alternatives that were considered. An ID is permanent. If a later decision replaces an entry, the old entry stays and its status changes to "Superseded by D-n".

## Status labels

- **Pre-release, maintainer decision.** The maintainer made this decision before the first tagged release, without public consultation. `GOVERNANCE.md` permits this before v0.1.0. Consultation can reopen any of these decisions.
- **Consulted.** The decision followed a public consultation. The entry links to the consultation summary.
- **Superseded.** A later entry replaces this decision.

---

## Process and repository

### D-1. Fix the draft before the first tag

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Version 0.1.0 is not released. All known defects are corrected in 0.1.0 before the `v0.1.0` tag.

**Reason.** Nothing is published. The domain does not resolve, there are no tags, and nobody has built against the schema. Schema `$id` URLs become permanent at the first tag. It is better that the permanent URL starts with a correct schema.

**Alternatives considered.** Tag now, then release the corrections as 0.1.1 and 0.2.0. This carries known defects into a permanent URL for no benefit.

### D-2. The GitHub organisation is `fpds-football`

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** The repository is `github.com/fpds-football/spec`. Sibling implementations are `fpds-football/fpds-ts` and `fpds-football/fpds-py`.

**Reason.** The git remote already uses `fpds-football`. Some files used `fpds`. Links in `CHANGELOG.md` become permanent at the first tag, so one name must apply everywhere.

**Alternatives considered.** The `fpds` organisation. It is not the organisation that exists.

### D-3. Three licences

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** The schema and code use Apache License 2.0. The specification text, other Markdown files and the website use CC BY 4.0. The examples and conformance fixtures use CC0 1.0. `LICENSING.md` maps each path to its licence.

**Reason.** Apache 2.0 includes a patent grant, which protects implementers. CC BY 4.0 lets anyone republish the text with credit. Implementers copy examples and fixtures into their own test suites, and CC0 removes all attribution requirements for that use.

**Alternatives considered.** Apache 2.0 for the examples and fixtures. This adds notice requirements to files that have nothing to protect.

### D-4. All prose uses Simple English

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** All prose follows ASD-STE100 Simplified Technical English in pragmatic mode. Existing text is rewritten too. Three exceptions apply:

1. RFC 2119 keywords in capitals (`MUST`, `SHOULD`, `MAY`) stay. They are technical terms. Lowercase "should", "may" and "could" are replaced.
2. Spelling is British. This agrees with field names such as `fifa_agent_licence`.
3. `index.html` follows the structural rules but keeps its headline voice.

**Reason.** Many readers of FPDS are not native English speakers, and many are not technical. Short sentences with one meaning per word translate well. The RFC 2119 exception keeps normative levels exact. A change from `SHOULD` to "must" changes the obligation.

**Alternatives considered.** American spelling, as the standard specifies. One spelling across prose and schema is more important.

### D-5. Host the site on Cloudflare Pages

- **Date:** 2026-09-14
- **Status:** Superseded by D-30

**Decision.** The site deploys through the Cloudflare Pages Git integration from `main`. A build step copies only `index.html`, `schema/`, `consult/` and a `_headers` file into `_site/`. Schema files have the content type `application/schema+json` and the header `Access-Control-Allow-Origin: *`. Before the tag, the cache time is short. The GitHub Pages workflow, `CNAME` and `.nojekyll` are removed.

**Reason.** The domain is registered at Cloudflare. The Git integration needs no API token in GitHub. A build step that copies files from the repository means the published schema cannot drift from the source. Publishing only named paths keeps internal files such as `CLAUDE.md` and `tests/` off the site.

**Alternatives considered.** GitHub Pages, which the original additions assumed. A GitHub Action that deploys with `wrangler`, which needs a stored Cloudflare token.

### D-6. The 14-day rule starts at the first tag

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Before `v0.1.0`, the maintainer can change the draft directly. After `v0.1.0`, every schema change needs a consultation that stays open for at least 14 days. A consultation is the website page, the form and the GitHub Discussion together (see D-25). This file records every decision, and pre-release decisions carry their own label.

**Reason.** The 14-day rule protects people who depend on the specification. Before the first release, nobody depends on it. A public record of the reasons keeps the pre-release work open to examination.

**Alternatives considered.** Apply the rule now, with a Discussion for each decision and a wait of 14 days. There is no audience yet to read those Discussions.

### D-7. Contact addresses

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Three addresses forward through Cloudflare Email Routing: `conduct@fpds.football`, `security@fpds.football` and `privacy@fpds.football`. `SECURITY.md` lists GitHub private security advisories first and the email address second. Before launch, the maintainer sends a test message to each address.

**Reason.** `CODE_OF_CONDUCT.md` and `SECURITY.md` already name two of these addresses. A reporting address that does not work is worse than no address. The consultation forms collect personal data, so the privacy notice needs a contact.

**Alternatives considered.** A general `hello@` address. General contact goes through the consultation pages and GitHub instead.

### D-8. Remove `APPLY.md`

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `APPLY.md` is deleted. Its lasting content moves to a "Maintaining" section in `CONTRIBUTING.md`.

**Reason.** `APPLY.md` was a one-time instruction for an archive of additions. Most of it is now incorrect, because it describes GitHub Pages and the `fpds` organisation.

**Alternatives considered.** Keep it as a historical record. The git history does this.

---

## Scope

### D-9. Start with a small core, and add after consultation

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** FPDS starts with the smallest useful core. When a decision needs input from the football industry, v0.1.0 ships the smaller or stricter option. The question goes to §14 of `SPEC.md`.

**Reason.** Semantic versioning makes this choice safe in one direction only. To add a field, add an enum value or relax a constraint is a minor version. To remove a field, remove an enum value or tighten a constraint is a major version. If v0.1.0 is small and strict, every result of consultation is a minor version.

**Alternatives considered.** Decide each case separately. This produces inconsistent results and fields that cannot be removed later.

### D-10. Open questions live in §14, with IDs

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** §14 of `SPEC.md` is the only list of open questions. Each question has an ID (`OQ-1`, `OQ-2`, and so on) and a line that states what v0.1.0 ships until the question is answered. Each consultation page and each GitHub Discussion links to its ID. They do not copy the text of the question.

**Reason.** One list cannot drift from itself. The "v0.1.0 ships" line tells implementers what to do now.

**Alternatives considered.** A separate `CONSULTATION.md`. This makes a second list to keep synchronised with the normative text.

### D-11. The v0.1.0 core fields

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** The core has these fields:

| Member | Fields |
|---|---|
| (top level) | `fpds_version` |
| `submission` | `submission_id`, `submitted_at`, `purposes` |
| `player` | `full_name`, `date_of_birth`, `nationalities`, `current_club.name`, `current_club.country`, `external_ids.fifa_connect_id` |
| `positions` | `primary_position`, `secondary_positions` |
| `contract` | `status`, `expiry_date`, `parent_club.name`, `parent_club.country` |
| `representation` | `agent_name`, `fifa_agent_licence`, `mandate_status` |
| `performance[]` | `season`, `competition`, `competition_country`, `appearances`, `minutes`, `goals`, `assists`, `clean_sheets` |
| `consent` | `lawful_basis`, `consent_date`, `is_minor` |
| (top level) | `provenance`, `extensions` |

A field is in the core only if FPDS does not work without it. That is, the document is unusable without the field, or the field carries a design principle: output with minutes, provenance, and the protection of minors.

These fields and blocks from the first draft are not in the core. Each is a candidate for consultation:

- The `availability` block: `available_for`, `available_from`, `asking_price`, `loan_fee`, `wage_contribution_expected`
- The `eligibility` block: `passports`, `work_permit_required`, `gbe_points`, `homegrown_status`, `international_caps`
- The `medical` block: `current_status`, `expected_return_date`
- The `media` block: `type`, `url`, `recorded_on`
- `contract.release_clause`, `contract.sell_on_percentage`, `contract.option_to_extend`, and the `money` definition
- `representation.agency`, `representation.mandate_expiry`
- `player.known_as`, `player.preferred_foot`, `player.height_cm`, `current_club.competition`, `current_club.id`
- `external_ids.transfermarkt_id`, `external_ids.wyscout_id`, `external_ids.opta_id`
- `performance[].competition_tier`, `performance[].starts`
- `submission.note`

D-28 later added `submission.sender`, and made `representation` required only when the sender is an intermediary.

**Reason.** The first draft had 64 fields and described itself as "twenty-ish". Each field in v0.1.0 is a permanent commitment until a major version. A small core also gives each later addition its own consultation.

The removal of some fields has a specific reason:

- Vendor identifiers put commercial products in the core, against `GOVERNANCE.md` commitment 2. `fifa_connect_id` stays, because design principle 5 follows FIFA identifiers.
- `gbe_points` and `homegrown_status` apply to England only. `work_permit_required` does not say which country. They answer open question 4 before consultation, and they conflict with `GOVERNANCE.md` commitment 1.
- `release_clause`, `sell_on_percentage` and `asking_price` are commercially sensitive, in the same class as the wage question.
- `submission.note` is free text, which is the problem that FPDS exists to remove.

**Alternatives considered.** A 36-field core that kept `known_as`, the contract terms, the full `representation` block, `medical` and `media`. The maintainer chose a smaller set, so that the industry decides these fields through consultation.

### D-12. `clean_sheets` is in the core

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `performance[].clean_sheets` is the number of appearances in which the team of the player conceded no goals while the player was on the pitch. It applies to all positions. Like `goals` and `assists`, it requires `minutes`.

**Reason.** Without this field, the performance record describes only outfield players. The definition makes the value objective, so provenance can mark it as verified. Data providers use different definitions, so the specification must state one.

**Alternatives considered.** A goalkeeper-only field. A centre-back's clean sheets also have meaning. `goals_conceded` and `saves` are candidates for consultation.

---

## Field rules

### D-13. Dates are single ISO 8601 values

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `date_of_birth` is one string in `YYYY-MM-DD` format. Every date field in the schema has the pattern `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` in addition to `format: date`. Producers MUST NOT put a local date format such as `07/03/1998` in a date field. Consumers show dates in the local format of the reader.

**Reason.** An ISO date has one meaning. Confusion between day and month occurs only when a date is shown, not when it is stored. In JSON Schema 2020-12, `format` is an annotation by default, so many validators accept `07/03/1998`. The pattern makes all validators reject it.

**Alternatives considered.** Separate fields for birth year, birth month and birth day. Three integers accept 30 February unless the schema adds complex rules. Consumers must also rebuild the date to calculate `is_minor`. Partial dates of birth are open question OQ-6.

### D-14. Unknown is a value, not a gap

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Design principle 3 changes from "Absence is explicit" to "Unknown is a value, not a gap":

- A required field that can be unknown has the enum value `unknown`.
- A missing optional field means "not stated". Consumers MUST NOT infer anything from its absence.
- `null` is not valid anywhere in a document.

**Reason.** The first draft said that `null` with a reason is better than a missing key. The schema did not permit `null` and had no field for a reason. The schema already used `unknown` enum values, so the principle now agrees with the schema.

**Alternatives considered.** Permit `null` with a reason. This adds a new mechanism to a draft that is intended to be small. The difference between "not disclosed" and "not known" is open question OQ-7.

### D-15. Two season formats

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `season` accepts `YYYY/YY` for a season that crosses two calendar years, and `YYYY` for a calendar-year season. The separator is a slash only. In the `YYYY/YY` format, the second part MUST be the year after the first part.

**Reason.** Many leagues play in calendar years, for example in Brazil, the United States, Norway, Sweden, Japan and Ireland. One submission can contain seasons of both types. A hyphen makes the value look like an ISO date.

**Alternatives considered.** The `YYYY/YY` format only. This excludes calendar-year leagues.

### D-16. Rules that implementations must enforce

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** §13 of `SPEC.md` lists the rules that JSON Schema cannot express. A conforming implementation MUST enforce each rule. The list contains:

1. `consent.is_minor` agrees with `date_of_birth` on the date of `submission.submitted_at`.
2. In a `YYYY/YY` season, the second part is the year after the first part.
3. Each provenance key resolves to a value in the same document.
4. `extensions` values contain no diagnoses, injury details or medical history.

D-38 later added a rule about secondary positions. D-39 later removed the medical rule from this list.

**Reason.** Project policy says that a `MUST` needs enforcement. Where the schema cannot enforce a rule, the specification states which party enforces it. One list makes these rules easy to find and to test.

**Alternatives considered.** Keep these rules in their sections only. They are then easy to miss.

### D-17. `purposes` is an array

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `submission.purpose` (a string) becomes `submission.purposes` (an array with at least one unique item). The values are `permanent_transfer`, `loan`, `trial` and `information_only`. `information_only` cannot occur with another value. The value `free_agent_offer` is removed. The word "registration" is removed from the scope in §1.

**Reason.** "Available on loan or permanent" is a common offer, and one value cannot express it. "Free agent" is a contract status, not a type of deal, and `contract.status` already records it. Registration is the work of FIFA TMS and national associations, not FPDS.

**Alternatives considered.** Keep one value. This forces the sender to hide an option.

### D-18. The `submission` block is specified

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** `SPEC.md` specifies the `submission` block. `submission_id` is unique for each sender and has no meaning for the receiver. `submitted_at` is the reference date for the calculation of `is_minor`.

**Reason.** The first draft required the block but did not specify it. §10 said to calculate minor status "against the date of submission" but did not name the field.

**Alternatives considered.** None.

### D-19. Consent and minors

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- A minor is a person under 18 years old on the date of `submission.submitted_at`. This agrees with Article 19 of the FIFA Regulations on the Status and Transfer of Players.
- `consent_obtained` is removed.
- If `lawful_basis` is `consent`, `consent_date` is required.
- The `lawful_basis` values are `consent`, `contract`, `legitimate_interest`, `legal_obligation` and `not_stated`. They agree with the lawful bases in Article 6 of the GDPR. Producers in other jurisdictions use the nearest value.

**Reason.** The first draft did not give an age, so implementations did not calculate minor status consistently. `consent_obtained` repeated `lawful_basis` and was able to contradict it. A claim of consent without a date is weak.

**Alternatives considered.** Keep `consent_obtained`. Add a field for the person who gave consent. Consent from a parent or guardian is open question OQ-8.

### D-20. Boolean names start with `is_` or `has_`

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Each boolean field name starts with `is_` or `has_`. `consent.subject_is_minor` becomes `consent.is_minor`.

**Reason.** A prefix shows the type in the name. `has_` permits natural names for possession, where `is_` alone gives unclear names.

**Alternatives considered.** `is_` only. An enum `extension_option` with the values `none`, `club`, `player`, `mutual` and `unknown` was agreed to replace `option_to_extend`. D-11 then removed the field from the core, so `is_minor` is the only boolean in v0.1.0.

### D-21. Sixteen position codes

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Position codes are uppercase. The codes are:

`GK`, `RB`, `LB`, `RWB`, `LWB`, `CB`, `LCB`, `RCB`, `CDM`, `CM`, `CAM`, `RM`, `LM`, `RW`, `LW`, `ST`

`CB` is a centre-back who plays on the two sides. `LCB` and `RCB` are centre-backs who play on one side only. A centre-back who plays on the two sides is `CB`, not `LCB` with `RCB` as a secondary position.

**Reason.** More people recognise `CDM`, `CM` and `CAM` than `DM`, `CM` and `AM`. The codes keep the difference between a 6, an 8 and a 10. Clubs ask for left-sided centre-backs, so `LCB` and `RCB` have a recruitment use. Wide midfielders in a 4-4-2 have a different profile from wingers, so `RM` and `LM` stay. Uppercase agrees with scouting platforms and broadcast graphics.

**Alternatives considered.** Side-specific codes for all central positions (`LCDM`, `RCDM`, `LCM`, `RCM`, `LCAM`, `RCAM`). These are slots in a formation, not player types. The same player gets a different code in a different formation. `SS` (second striker) is removed, because its meaning is contested. Other side-specific positions are open question OQ-10.

### D-22. Contract status and current club

- **Date:** 2026-09-14
- **Status:** Superseded by D-27

**Decision.**

- `contract.status` has the values `under_contract`, `free_agent`, `on_loan`, `youth_scholarship` and `unknown`. `free_agent` means "not under contract with any club". The value `unattached` is removed.
- `player.current_club` is required when `status` is `under_contract`, `on_loan` or `youth_scholarship`. It MUST NOT be present when `status` is `free_agent`. It is optional when `status` is `unknown`.
- When `status` is `on_loan`, `current_club` is the club where the player plays on loan. `parent_club` is the club that holds the registration of the player.

**Reason.** The first draft required `current_club` for all players. An example worked around this with a club named "Unattached", which is the free text that FPDS exists to remove. The first draft did not define `free_agent` or `unattached`. Two undefined values give inconsistent data. Under D-9, v0.1.0 ships one value. If consultation shows that a second value is necessary, its addition is a minor version.

**Alternatives considered.** Keep `unattached` with a definition. Make `current_club` optional for free agents, so that it can hold the previous club. The split of `free_agent` is open question OQ-9.

### D-23. Provenance rules

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- Each provenance key MUST resolve to a value in the same document.
- An entry applies to the value at its pointer and to all values below it. The most specific entry has priority.
- `asserted_by` is free text for display. It does not identify a party.

**Reason.** Without these rules, a consumer can show sourcing for a claim that does not exist. Producers can mark a full object with one entry. A structured `asserted_by` needs an issuer or a registry, which `GOVERNANCE.md` commitment 2 does not permit. A structured format is open question OQ-11.

**Alternatives considered.** A format such as `agent:<licence>` or `club:<fifa_connect_id>`.

### D-24. Extension keys use a reverse-DNS prefix

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- Each key in `extensions` MUST start with a reverse domain name, then a slash, then a field name. An example is `com.example/scouting_grade`. The schema enforces this with `propertyNames`.
- The `football.fpds` prefix is reserved. No key uses it in v0.1.0. Examples in the specification use `com.example`.
- `extensions` MUST NOT contain diagnoses, injury details or medical history. An availability status is permitted.

**Reason.** Without a prefix, two producers can use the same key with different meanings. A domain name shows who defined a key, and FPDS needs no registry to issue names. If the specification defines keys under its own prefix, those keys become a second core without consultation. The first draft stated the medical restriction only in internal notes. `medical` is not in the core, so the restriction must be in the specification.

**Alternatives considered.** Prefixes as a recommendation only. Producers then omit them.

---

## Consultation

### D-25. Consultation has two layers

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- **Participation.** Each open consultation has a page at `fpds.football/consult/`. The page is in Simple English and contains no JSON. It has a Tally form that asks for the role of the respondent, the answer, an optional comment and an optional email address. The form has a privacy notice. LinkedIn posts link to these pages.
- **Record.** GitHub holds the specification, `CHANGELOG.md`, this file, and one Discussion for each open question.
- **Summary.** When a consultation closes, the maintainer publishes a summary on the page and in the Discussion. The summary is anonymous by default. It shows the number of responses for each role, the main arguments and the decision with its reasons.

**Reason.** Agents and club staff do not use GitHub. If GitHub is the only way to take part, developers and data vendors give most of the input. A published summary with counts by role shows whose input formed each decision.

**Alternatives considered.** GitHub Discussions only. A self-hosted form on Cloudflare, which means storing personal data in FPDS infrastructure.

### D-26. Three consultations at launch

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** Three consultations open at launch:

1. Release clauses and sell-on percentages (OQ-14)
2. Medical availability (OQ-15)
3. Wages and salary (OQ-2)

After launch, a new consultation opens every two to three weeks. Each stays open for at least 14 days. §14 lists all open questions. Questions without an open consultation say "consultation not yet open". Technical questions, such as the format of `asserted_by` and signed submissions, use GitHub Discussions only. The "Two questions the draft needs answered" section of `index.html` becomes "Open consultations".

**Reason.** Twenty questions at one time give low response rates and too little evidence for each decision. These three topics interest agents and clubs most, and the wage question has the largest effect on adoption.

**Alternatives considered.** Open all consultations at launch.

---

## Decisions made during implementation

### D-27. Five contract statuses with FIFA definitions

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** This entry replaces D-22.

- `contract.status` has the values `under_contract`, `on_loan`, `amateur`, `free_agent` and `unknown`.
- "Professional" and "amateur" have the meanings in Article 2 of the FIFA Regulations on the Status and Transfer of Players.
- `amateur` is a player who is registered with a club and is not a professional. `free_agent` is a player who is not registered with any club.
- `youth_scholarship` is removed.
- For each status, §7.2 of `SPEC.md` states whether `current_club`, `expiry_date` and `parent_club` MUST be present, MUST NOT be present, or MAY be present.

**Reason.** Under D-22, a registered amateur player had no correct status. `youth_scholarship` did not apply, and `free_agent` did not permit a current club. The academy example had this problem. FIFA defines "professional" and "amateur", so the two words have the same meaning in all federations. "Scholarship" is an English term. Under D-9, fields that do not apply to a status are forbidden, not optional.

**Alternatives considered.** A `semi_pro` status. Semi-professional describes the level of a league or of pay, not a contract. Many semi-professional players have written contracts, so the value overlaps with `under_contract`. The level of a competition is open question OQ-1. Academy categories are open question OQ-13.

### D-28. A player can send their own submission

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- `submission.sender` is required, with the values `intermediary` and `player`.
- If `sender` is `intermediary`, `representation` is required. If `sender` is `player`, `representation` is optional.
- If `consent.is_minor` is `true`, `sender` MUST NOT be `player`. The schema enforces this.
- v0.1.0 has no sender value for a parent, a guardian or a club. This is open question OQ-12.

**Reason.** Players without an agent share their own profiles. Under D-11, `representation.agent_name` was required, so a player without an agent had to write a placeholder such as "Not represented". A profile that a minor sends directly to clubs is a safeguarding risk.

**Alternatives considered.** Limit v0.1.0 to intermediaries. This excludes players without representation, which is a large group.

### D-29. A value without provenance has the sender as its source

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** The provenance source `player_stated` is added. If a value has no provenance entry, its source is `agent_stated` when the sender is `intermediary`, and `player_stated` when the sender is `player`.

**Reason.** The first draft gave `agent_stated` as the source for all values without an entry. After D-28, that source is incorrect for a submission that the player sends.

**Alternatives considered.** Keep `agent_stated` as the only default. It then states that an agent made a claim when no agent took part.

### D-30. Host the site on Cloudflare Workers static assets

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** This entry replaces D-5.

- The site deploys through Cloudflare Workers Builds from the `fpds-football/spec` repository.
- The build command is `sh scripts/build-site.sh`. The deploy command is `npx wrangler deploy`.
- `wrangler.jsonc` in the repository contains the project name, the compatibility date and the assets directory `_site`.
- The build step, the published paths and the `_headers` rules from D-5 do not change.

D-41 later reduced the published paths to the schema only.

**Reason.** Cloudflare now calls the Pages workflow "legacy", and Workers is the default for new projects. Workers static assets serve `_headers` in the same way as Pages. A configuration file in the repository keeps the deployment settings under version control, not only in the dashboard.

**Alternatives considered.** Continue with the legacy Pages workflow. It works now, but it is not the direction of the platform. Put the settings as flags in the deploy command. The settings then exist only in the dashboard.

---

## Tools for creating and reading submissions

### D-31. Rules for `submission_id`

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- `submission_id` MUST be a lowercase RFC 9562 UUID with hyphens. Version 4 or version 7 is recommended. The schema enforces the format.
- Each version of a document has its own `submission_id`. If any value changes, the producer makes a new ID and a new `submitted_at`.
- A document that a party sends or forwards without changes keeps its ID.
- `submitted_at` is the time that the producer made the version, not the time that a party sent it.
- §4.3 of `SPEC.md` states the purpose: a receiver uses the ID to recognise a repeated or forwarded copy.
- A link from a new version to the version that it replaces is open question OQ-24.

**Reason.** The first text said "unique for each sender", but FPDS has no reliable way to identify a sender. A UUID is unique without a registry, and any software can make one offline. Recognition of forwarded copies helps clubs with submissions from parties that have no mandate (§8).

**Alternatives considered.** Remove `submission_id` from v0.1.0. Documents made before a later addition then have no ID. Keep a free string. Receivers then cannot rely on uniqueness.

### D-32. Three repositories

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- `fpds-football/spec` holds the schema, the specification and the conformance suite. It publishes only `https://fpds.football/schema/*`.
- `fpds-football/fpds-ts` is a TypeScript validation library, published to npm. Its CI runs the full conformance suite from this repository and makes sure that its copy of the schema is identical.
- `fpds-football/site` holds the homepage, the consultations, the builder and the viewer. It publishes all other paths on `fpds.football`.
- `index.html` and `consult/` move from this repository to `fpds-football/site`.

**Reason.** A specification repository that contains an application in one language becomes a project about that language. `fpds-ts` must be an independent implementation that anyone can use, not a part of the website. If the site deployment fails, the permanent schema URL still works.

**Alternatives considered.** One new repository with the library and the application together. The library then looks like a part of the website.

### D-33. Technology for the site and the library

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- The site uses TanStack Start. Content pages are prerendered to static HTML. The builder and the viewer run only in the browser.
- The site uses TanStack Form and Tailwind CSS.
- `fpds-ts` uses Ajv for JSON Schema 2020-12, compiled at build time. It returns error codes with messages in plain English.
- Tests use Vitest and Playwright. The package manager is pnpm.
- Pages of the builder and the viewer send no player data over the network. A test enforces this.

**Reason.** Prerendered content pages give correct link previews on LinkedIn and in messages. Ajv compiled at build time needs no runtime code generation, so the site keeps a strict Content Security Policy. Error messages in plain English help people who are not technical.

**Alternatives considered.** Astro with React components. It is good for content, but TanStack Start also supports server functions if consultation forms move in-house later.

### D-34. How the builder works

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- A pane on the left lists the sections. Each section shows a status: complete, required fields missing, optional, or not applicable.
- The centre shows the fields of the selected section. A live preview shows the submission as a club sees it.
- The export button stays disabled until the document is valid, and it lists the missing items.
- The builder hides fields that do not apply, and shows a short note that gives the reason.
- The builder calculates `is_minor`. A minor has a clear badge and a safeguarding notice.
- The builder never changes a choice of the user without permission. It shows a conflict on the related fields, with a fix that the user can select.
- If a change hides a field that has a value, the builder keeps the value until the user confirms.
- Each value has a source selector. The default is the sender.
- `fpds-ts` gives the state of each field: required, optional, not applicable or calculated. The builder contains no rules of its own. A test makes sure that the field states agree with the validator for each conformance case.

**Reason.** Conditional fields are the most difficult part of FPDS for a person to understand. One source for the rules prevents a difference between the builder and the schema.

**Alternatives considered.** Show all fields and validate at export. Users then make errors that the builder can prevent.

### D-35. A submission travels as a file

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- The builder exports a file that ends with `.fpds.json`. The sender attaches the file to an email or a message.
- The viewer at `fpds.football/view` opens a file in the browser. It shows the sources of values, a badge for minors and warnings.
- The viewer has a print layout, so a club can save a PDF for internal use.
- The viewer can open a file in the builder. A change then gives the document a new `submission_id` (D-31).
- There are no share links. This is open question OQ-25.

**Reason.** A link must keep the data on a server or put the data in the URL. A URL with player data stays in browser history, chat logs and link previews. People already understand a file attachment as a document.

**Alternatives considered.** A share link with the document encoded in the URL.

### D-36. Unfinished work in the builder

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- The builder saves work automatically in session storage. The browser deletes it when the tab closes.
- "Save draft" downloads a file that ends with `.fpds-draft.json`. The file contains a draft marker. The viewer does not show a draft as a submission.
- The builder does not keep data in the browser after the tab closes.
- A "Clear everything" button is always visible.

**Reason.** Agents stop and start their work. Data about players, often minors, must not stay on a shared computer. A draft file must never look like a valid submission.

**Alternatives considered.** Local storage that stays after the tab closes. Export of invalid documents with a warning.

### D-37. How the viewer shows problems

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- If a file is not valid against the schema, or breaks a rule in §13.1, the viewer shows the submission with a red "Not a valid FPDS submission" banner and a list of the problems in plain English.
- If `is_minor` does not agree with the date of birth, the viewer also shows the calculated value.
- The viewer shows unrecognised extensions in a closed section with their prefix, and without source marks.
- The viewer does not show the fields of an unsupported version, a draft file, or a file that is not FPDS. It gives the reason.
- Each rendered submission has this note: "FPDS checks the structure of this file. It does not check that the information is true."
- The viewer never shows a badge such as "Verified by FPDS".

**Reason.** Clubs receive files from many producers. A flawed file still has value, but it must never look conforming. For minors, safeguarding is more important than the value in the file.

**Alternatives considered.** Refuse all invalid files. Clubs then lose useful information because of small errors.

### D-38. Specification changes for the tools

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- §13 defines a producer and gives a checklist of steps for a conforming producer.
- §11 no longer refers to a sender who types a submission by hand.
- §13.1 adds rule 5: `secondary_positions` does not contain the primary position. After D-39, this rule is rule 4.
- §3 states that a document is UTF-8 JSON with the media type `application/json`, and that a file name SHOULD end with `.fpds.json`.
- §14 adds OQ-24 and OQ-25.
- `README.md` has a section: "How do I create an FPDS-conforming document?"

**Reason.** An agent first asks how to make a document that conforms. The specification did not answer. The builder prevents a secondary position that repeats the primary position, so the specification must agree. JSON Schema can express that rule only with sixteen conditions, so it is in §13.1. A file name that people recognise helps in email and messages. It is not a MUST, because FPDS does not define transport.

**Alternatives considered.** "Compliant" in place of "conforming". §13 already defines "conforming", and one word has one meaning.

### D-39. Minor status details, and the medical rule

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- §10.1 states that the date of `submitted_at` is the calendar date in the timestamp, with the time zone offset that the timestamp states.
- §10.1 states that a player becomes 18 at the start of their 18th birthday. A player born on 29 February becomes 18 on 1 March in a year that is not a leap year.
- The rule about medical information in `extensions` leaves the list in §13.1. §12 makes the producer responsible for it. A consumer or validator MAY show a warning, and a warning does not make a document invalid.
- The producer checklist in §13 has a step for the medical rule.
- The rule about secondary positions becomes rule 4 in §13.1.

**Reason.** The first implementation, `fpds-ts`, found these gaps. Without a stated time zone and a stated leap-day rule, two implementations can calculate a different minor status for the same document. 1 March keeps the player a minor for longer, which is the safer choice for safeguarding. §13.1 said that implementations MUST enforce the medical rule, but software cannot decide with certainty whether text contains medical information. A MUST that nobody can enforce is not a real requirement.

**Alternatives considered.** 28 February for a birthday on 29 February. It ends the protection of a minor one day earlier. The date of `submitted_at` in UTC. It gives a different date from the date that the producer wrote. Keep the medical rule in §13.1 with a keyword check. A keyword check gives false results in the two directions.

### D-40. The builder keeps its draft by JSON Pointer, not in TanStack Form

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.** The builder keeps the draft as a plain object and changes it by JSON Pointer. It does not use TanStack Form. This entry changes one part of D-33.

**Reason.** `@fpds-football/fpds` gives field states, issues and provenance keys as JSON Pointers. TanStack Form uses paths such as `performance[0].minutes`. With TanStack Form, the builder must convert between the two kinds of path everywhere, and provenance keys contain `/` characters. A store by JSON Pointer uses one kind of key from the library to the screen. The builder also does not use the validation of a form library, because all rules come from `@fpds-football/fpds`.

**Alternatives considered.** TanStack Form, as D-33 planned.

### D-41. This repository publishes only the schema

- **Date:** 2026-09-14
- **Status:** Pre-release, maintainer decision

**Decision.**

- `index.html` and `consult/` are removed from this repository. `fpds-football/site` holds them now (D-32).
- The build publishes only `_headers` and `schema/`. CI fails if the build contains any other path.
- The `spec` Worker has a route, `fpds.football/schema/*`, and no custom domain. The `fpds-site` Worker holds the custom domain `fpds.football`.
- `_headers` has no Content Security Policy for pages, because this Worker serves no pages.

**Reason.** The site now serves every path except `/schema/*`, so copies of the pages in this repository are never served, and they can drift from the real pages. When this repository publishes only the schema, a change to the website cannot affect the permanent schema URL.

**Alternatives considered.** Keep the pages here as a fallback. Nobody can reach them, and two copies of the same text drift.
