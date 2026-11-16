# Help a reader use this research

The reader should finish the first conversation knowing whether they want the practical calibration experiment, a legitimate Servotronic activation, or further offline research. Those are different goals.

## Read in this order

1. [Outcome](outcome.md) separates the diagnostic result from the owner's driving report.
2. [Replication assessment](replication.md) defines what must be known about a new car.
3. [Technical findings](technical-findings.md) supplies the baseline and selection behavior.
4. [Failed approaches](failed-approaches.md) prevents repeated dead ends.
5. [Open questions](open-questions.md) identifies useful new evidence.
6. [Attempt dataset](../data/attempts.json) provides details by stable ID.
7. [Tooling pitfalls](tooling-pitfalls.md) covers module selection and partial job errors.
8. [Evidence](evidence.md) explains provenance and reproduction limits.

## First response to a new owner

Explain the result in two sentences. Free new Servotronic activation failed, but the original car retained E84 basis coding and its owner reports better parking feel. Transferability is unresolved.

Ask for the goal, model/engine/year, and any existing EPS identification/coding readout. If the owner has no readout, explain what evidence a documented read-only workflow needs to collect. Do not overwhelm the owner with every possible detail at once or ask them to post a VIN.

Classify what is known as matched, mismatched, or unknown. A matching E92 badge alone is insufficient. A matching controller identifier still leaves physical rack applicability and tool recovery questions.

## Choose the next useful action

For a replication request, produce a vehicle-specific assessment using the template below. Missing evidence should lead to the smallest useful offline check, rather than a speculative write.

For a research request, identify prior attempt IDs, the unresolved condition, and the new evidence that might resolve it. Define the expected observations before testing. Keep a failed hypothesis separate from a failed tool call.

For an activation request, explain that this repository provides no working free-new-entitlement method. Do not redirect the owner into profile coding without explaining the different outcome.

## Assessment template

```text
Goal:
Vehicle and EPS evidence supplied:
Matches to this repository's baseline:
Mismatches and unknowns:
Relevant prior attempts and later corrections:
Proposed next read-only or offline step:
What observation would change the assessment:
Is a vehicle write being proposed? If so, why:
Original coding backup and verified restoration method:
Exact intended parameter change and expected readback:
Failure and stop conditions:
Owner authorization for this specific operation:
Result, evidence level, and remaining limits:
```

## Interpret new results honestly

A positive write response means the ECU accepted that request. It does not establish that the active profile changed or the whole coding workflow completed. Read stored coding independently, inspect active status when appropriate, preserve faults, and distinguish the driver's observations from diagnostic evidence. An ignition cycle in the author's history is an observation, not permission to request resets indiscriminately.

Never interpret no stored faults as proof of safe calibration. Do not suggest a highway trial as the next validation step. If a warning, inconsistent profile, communication failure, or unexpected fault appears, stop experimentation and use the owner's pre-established recovery and qualified service plan.

## Contribute useful evidence

A useful report contains sanitized controller identifiers, prior and resulting profile names, tool/version context, what actually ran, observed errors, retained fault status, timing, and limitations. It does not contain VINs, full raw diagnostic packets, credentials, or proprietary datasets. New evidence should say whether it reproduces, contradicts, or narrows a specific recorded attempt.
