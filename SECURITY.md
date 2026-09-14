# Security and privacy

FPDS is a document format. It has no servers, no runtime and no code that runs for you, so most types of vulnerability do not apply. Two types of problem still apply.

## Report a schema defect with security or privacy impact

A schema defect has security impact if a conforming implementation accepts a document that it must reject, and the document can mislead a consumer. Two examples:

- A rule that lets a producer mark a claim as `verified` without `verified_against`
- A rule that lets a minor appear as the sender of their own submission

Report these defects privately. Use one of these methods:

1. On GitHub, go to the **Security** tab and select **Report a vulnerability**. This method is better, because it keeps the report and the fix together.
2. Send an email to `security@fpds.football`.

You will receive an acknowledgement in five working days or less.

Do not open a public issue about the defect until the fix is published.

For a question about personal data in a consultation response, send an email to `privacy@fpds.football`.

## Privacy rules for implementers

FPDS documents contain personal data about people who can be identified. Often these people are minors. FPDS makes some decisions about this data. The decisions work only if implementations obey them.

**FPDS contains no medical data.** Diagnoses, injury details and medical history are special-category health data in most jurisdictions. A document that parties forward is the wrong place for them. `extensions` MUST NOT contain them either (§12 of `SPEC.md`).

**Implementations calculate `is_minor`. Producers do not set it.** The value comes from `player.date_of_birth` on the date of `submission.submitted_at`. If an implementation lets a producer set it independently, submissions about minors do not go through their safeguarding process.

**A minor cannot send their own submission.** The schema rejects a document where `is_minor` is `true` and `sender` is `player`.

**Provenance is not authentication.** It records who made a claim. It does not show that the claim is true, and it does not show that the named party sent the document. A submission that names a licensed agent is not evidence that the agent sent it. FPDS 0.1 has no signature mechanism. This is open question OQ-3 in `SPEC.md`.

**Parties forward submissions, and this is the main risk.** Submissions travel by email and by message. If it was lawful to send a submission to one club, it is not automatically lawful to forward it to five more clubs. The `consent` block states the lawful basis for the first share. It does not give permission to share the document again.

**Do not log full documents.** A submission contains identity, contract status and consent in one object. A debug log that contains submissions is a data-protection problem.
