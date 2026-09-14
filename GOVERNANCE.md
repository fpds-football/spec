# Governance

**Current status: one maintainer, stated openly.**

One person maintains FPDS. That person makes decisions about the specification in public, after public consultation. There is no committee, no vote and no neutral organisation.

This is a weakness. This file states it because a standard that one vendor controls is a proprietary format with an open-source licence. People who evaluate FPDS need to know which type of standard it is now.

## The conflict of interest

The maintainer builds commercial software for football agents and clubs. This gives the maintainer a reason to change the specification to suit one product.

The maintainer makes three commitments against this:

1. **No field enters the core because one implementation wants it.** Extensions exist for that purpose. A field enters the core only when there is evidence that independent producers use it.
2. **The specification does not depend on any product.** It needs no hosted service, no registry, and no identifier that a specific party issues.
3. **The licences are irrevocable.** Apache 2.0 and CC BY 4.0 permit a fork at any time. If these commitments stop being true, a fork is the real protection, and it is stronger than any promise in this file.

## How decisions are made

### Before the first tagged release

Before `v0.1.0`, the maintainer can change the draft directly. `DECISIONS.md` records each of these decisions with the label "Pre-release, maintainer decision", so that nobody mistakes them for consulted decisions.

### After the first tagged release

After `v0.1.0`, every schema change needs a consultation. A consultation has three parts:

- A page on `fpds.football` in plain English, with a form for agents, clubs, players and other parties
- A GitHub Discussion for implementers
- A published summary when the consultation closes

These rules apply:

- A consultation stays open for at least 14 days before a schema change lands.
- The summary states the number of responses from each role, the main arguments and the decision with its reasons. The summary is anonymous by default.
- A change that makes a field required, removes a field or changes the type of a field needs a stated reason in `DECISIONS.md`.
- The proposals of the maintainer get the same 14 days and the same public process.
- If an objection gets no answer, the summary records it. The maintainer does not delete it.

Social media posts can bring people to a consultation. The consultation page and the GitHub Discussion are the record. The maintainer copies relevant points from other channels into the record.

## What changes this

If FPDS gets meaningful adoption, governance moves to a neutral organisation. More than one organisation then holds commit rights.

Meaningful adoption means all of these:

- Three or more independent implementations pass the conformance suite.
- Two or more organisations use FPDS in production. These organisations do not employ the maintainer, and the maintainer does not employ them.
- At least one club or league asks for submissions in FPDS format.

At that time, suitable structures are a UK community interest company, a small foundation, or an existing sports-data organisation. These structures are not suitable before that time. An empty foundation with one contributor looks worse than an honest repository with one maintainer.

## A place in future governance

If you want a place in future governance, say so early, in a GitHub Discussion. Governance that the first adopters help to design is better than governance that is given to them later.

## Version numbers and permanent URLs

The maintainer assigns version numbers under the rules in `CHANGELOG.md`.

Published schema URLs under `https://fpds.football/schema/` are permanent. Nobody will point them to a different file or remove them, including future maintainers. If this commitment breaks, it causes the most damage, so this file states it.
