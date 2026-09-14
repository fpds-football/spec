# Security and privacy

FPDS is a document format. It has no servers, no runtime and no code that executes on your behalf, so the usual vulnerability surface does not apply here. Two things still do.

## Reporting a schema defect with security impact

A schema defect matters if it causes a conforming implementation to accept something it should reject, in a way that could mislead a consumer. For example: a constraint that permits an unverifiable claim to be marked `verified`, or a pattern that allows a `media` URL to carry an unexpected scheme.

Report these privately via GitHub's **Report a vulnerability** button on the Security tab, or to security@fpds.football. Expect an acknowledgement within five working days.

Do not open a public issue for these until a fix is published.

## Privacy properties implementers should know

FPDS documents contain personal data about identifiable individuals, frequently including minors. The format makes some deliberate choices about that, and they only hold if implementations respect them.

**Medical information is availability status only.** `medical` carries a status and an expected return date. Diagnoses and injury history are out of scope because in most jurisdictions they are special-category health data, and a forwardable document is the wrong container for them. Do not put them in `extensions` either.

**`subject_is_minor` is computed, not asserted.** It is derived from `date_of_birth` against the submission date. Implementations that let a producer set it independently defeat the safeguarding routing it exists to enable.

**`provenance` is not authentication.** It records who claimed something, not whether the claim is true and not that the named party actually sent the document. A submission naming a licensed agent is not evidence that the agent sent it. FPDS 0.1 defines no signing mechanism; whether it should is open question 3 in `SPEC.md`.

**Forwarding is the normal case and the main risk.** These documents travel by email and messaging. A submission that was lawful to send to one club is not automatically lawful to forward to five more. The `consent` block states the basis on which the data was shared, not a licence to redistribute it.

**Do not log whole documents.** Submissions combine identity, contract terms and consent state in a single object. Debug logs holding them become a data-protection problem quickly.
