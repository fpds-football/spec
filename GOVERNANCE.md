# Governance

**Current status: benevolent dictator, openly stated.**

FPDS is maintained by one person. Decisions about the spec are made by that person, in public, on the basis of arguments made in Discussions. There is no committee, no vote and no neutral home.

This is a weakness and it is documented here rather than hidden, because a standard controlled by a single vendor is a proprietary format in open-source clothing, and everyone evaluating FPDS deserves to know which one this currently is.

## The conflict of interest

The maintainer builds commercial software in this space. That creates an obvious incentive to shape the spec around one product's needs.

Three commitments against that:

1. **No field enters the core because one implementation wants it.** Extension keys exist for that. Promotion into the core requires evidence of independent convergence.
2. **The spec carries no dependency on any product.** No hosted service, no registry, no identifier that has to be issued by anyone.
3. **The licences are irrevocable.** Apache-2.0 and CC BY 4.0 mean a fork is always available if this stops being true. That is the real protection, and it is stronger than any promise in this file.

## Decision-making now

- Proposals are raised as Discussions and stay open for at least 14 days before any schema change lands.
- Changes that affect required fields, remove fields or retype fields need a stated rationale in the changelog.
- The maintainer's own proposals get the same 14 days and the same public thread. Objections that go unanswered are recorded in the discussion rather than closed.

## What would change this

If FPDS reaches meaningful adoption — clubs asking for submissions in this format, more than one independent implementation in production — governance moves to a neutral home with commit rights held by more than one organisation.

Meaningful adoption, concretely:

- Three or more independent implementations passing the conformance suite
- Two or more organisations that neither employ nor are employed by the maintainer using it in production
- At least one club or league requesting submissions in the format

At that point the sensible structures are a UK CIC, a lightweight foundation, or hosting under an existing sports-data body. Not before. An empty foundation with one contributor looks worse than an honest solo repository.

## Interested in a seat at that table?

Say so early, in a Discussion. Governance designed with the first few adopters is better than governance imposed on them afterwards.

## Versioning authority

Version numbers are assigned by the maintainer according to the semver rules in `README.md`. Published schema URLs under `https://fpds.football/schema/` are permanent and will not be repointed or removed, regardless of who maintains FPDS later. This is the single commitment that would be most damaging to break and the one that most deserves to be written down.
