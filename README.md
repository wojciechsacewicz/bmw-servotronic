# BMW E92 steering research

I tried to unlock Servotronic for free on my BMW E92. I failed to unlock it.

But the research with Codex led to something that made the car much nicer to drive. We selected the **E84 basis steering profile already present in the EPS software**. As of 16 November 2026, I've been driving with it daily for roughly a week or two, possibly longer. Parking is much easier, and the steering still feels very good on the highway. For me, it was a game changer.

That is my experience with one car. This repository explains how we got there, everything we tried, what failed, and what remains unknown.

## What actually worked?

The recorded change was **coding a different calibration profile**, not flashing E84 firmware. The existing EPS application stayed the subject of the investigation. The saved readbacks show `E84_basis`, index `0E`, retained and active after an ignition cycle on 1 November 2026.

The controller described it as `E84 ohne SA216`, meaning E84 without the Servotronic option. We did not generate a working FSC, establish a new Servotronic entitlement, or demonstrate a firmware replacement.

| Question | Result | Evidence |
| --- | --- | --- |
| Free Servotronic activation? | Not achieved. | Historical research, A114. |
| E84 basis profile selected? | Confirmed by stored and active-profile diagnostic readback. | Diagnostic record, A111. |
| Did it survive an ignition cycle? | Yes, in the saved 1 November readback. | Diagnostic record, A111. |
| Does it feel better? | Yes, according to my daily-driving experience reported on 16 November. | Owner report. |
| Proven suitable for every E92? | No. Exact rack compatibility and controlled road testing remain unresolved. | Research limitation. |

[Evidence levels and source coverage](docs/evidence.md) explains what each label means.

## Start here

- **I want the story.** Read [what changed and how it feels](docs/outcome.md), then [the research timeline](docs/timeline.md).
- **I want help with my car.** Give your agent the prompt below. Start with identifying your own EPS and saving its original coding.
- **I want to research this further.** Read [the technical findings](docs/technical-findings.md), [failed approaches](docs/failed-approaches.md), and [open questions](docs/open-questions.md).
- **I want every recorded attempt.** Read [all 114 attempts](docs/attempts.md), or use [the structured dataset](data/attempts.json).

## Give this repository to your AI agent

Copy this prompt alongside the repository link or a local checkout:

```text
Read this repository's AGENTS.md and docs/agent-guide.md first.
Help me assess whether the recorded E84 basis coding experiment applies
to my BMW. Begin with my goal and the minimum vehicle/controller details.
Compare my evidence against the recorded baseline. Explain what matched,
what did not, and what is still unknown. Use the failed-route ledger so we
do not repeat approaches without new evidence. Before any vehicle write,
show me a vehicle-specific plan, original coding backup, restoration plan,
expected readback, and stop conditions. Do not treat the author's driving
experience or a matching model name as proof of compatibility.
```

Your agent should guide you through [the replication assessment](docs/replication.md). This repository supplies research context, not an automatic coding tool or a universal flash recipe.

## What was the test car?

The working identification was a 2012 BMW E92 LCI 318i with an N43 engine, model code `KD91`. The EPS reported application `6855892`, coding index `03`, hardware number `6851800`, and program reference `0512IC0F780A`. Its original active profile was `E92_basis`, index `09`. The target Servotronic entitlement was `0084/0001` and was absent in the saved diagnostic response.

Those identifiers are useful comparison points. They do not identify the complete physical rack or prove that another car can use the same calibration.

## What is included?

This is a curated research record, with an agent entry point, a readable account, a complete sanitized attempt ledger, and selected detailed evidence records. [Evidence and reproducibility](docs/evidence.md) explains what a reader can verify and what depends on private original captures.

VINs, raw conversations, personal paths, vehicle connection tools, downloaded BMW firmware, coding datasets, third-party manuals, and local environments are excluded. No working FSC generator or bypass patch is included. The original private evidence was preserved separately during cleanup.

## Repository map

- [Agent guide](docs/agent-guide.md) is the single reading order for assistants.
- [Timeline](docs/timeline.md) traces the investigation.
- [Tooling pitfalls](docs/tooling-pitfalls.md) covers wrong-module selection and partial job errors.
- [Source and contribution notes](RIGHTS.md) describes the publication boundary.

To check the public files without connecting to a car:

```sh
python3 scripts/check_repository.py
```

BMW and Servotronic are referenced to identify the systems studied. This project is independent of BMW.
