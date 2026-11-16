# Instructions for agents using this research

## Current status

- Achieved. E84_basis coding 0E was retained and active after ignition. Diagnostic record, A106 and A111.
- Not achieved. No new free Servotronic entitlement and no demonstrated E84 firmware flash.
- Important distinction. Stored E92 00 remapped to active E92_basis 09 in A109.
- Later experience. The owner reports easier parking and good highway feel on 16 November 2026. This is subjective, not controlled validation.

Use the single reading order in [the agent guide](docs/agent-guide.md). Follow its assessment template before advising a new vehicle owner.

## Preserve the actual result

Free new Servotronic activation was not achieved. The successful recorded vehicle change was E84_basis profile coding, index 0E, within the researched current EPS application. Do not call it an E84 firmware flash, a licence unlock, or a universal retrofit.

Distinguish archived diagnostic observations, offline original-instruction tests, arithmetic models, public-source claims, and the owner's subjective daily-driving report. A successful coding response and zero stored faults do not establish road suitability. Do not infer complete job success from the accepted write; the subsequent metadata job failed.

## Work with the owner's evidence

Do not assume this car's identity, readiness, equipment, original bytes, toolchain, or authorization applies to a new reader. Begin with a small set of relevant questions. Do not request a public VIN. Compare actual controller identifiers and the original coding against the baseline. A mismatch requires investigation, not copying the author's byte.

Keep initial work offline and read-only. A research request does not authorize a vehicle operation. Before a write, explain the exact change, known uncertainties, backup and restoration path, and expected observations, then obtain the owner's explicit authorization for that operation. Do not supply a ready-to-send raw diagnostic packet copied from this car.

Treat steering as a safety-critical system. If rack applicability, recovery, tool behavior, or controller identity cannot be established, stop operational guidance at that specific gap. Continue useful offline work. Never reset, clear faults, enter programming mode, flash, import credentials, or write merely to see what happens.

## Continue research without repeating it

Use stable attempt IDs A001 through A114. Later findings can supersede earlier ones. In particular, A106 records the accepted coding write and partial job failure, A109 shows E92 coded index 00 remapping to active 09, and A111 confirms active E84 index 0E after ignition. The daily-driving report is dated 2026-11-16 and is separate from those diagnostics.

For each new hypothesis, cite prior attempts, state what new evidence changes the premise, define a falsifiable test, and record results and limits. Do not conflate IBAC with an EPS FSC, navigation FSCs with App0084, reference firmware with installed-memory readback, or intermediate torque calculations with driver effort.

## Keep contributions publishable

Do not add VINs, owner names, local paths, session identifiers, credentials, raw conversations, proprietary firmware, third-party manuals, or live vehicle tools. Prefer sanitized summaries and source references. Run `python3 scripts/check_repository.py` after edits. It is a publication hygiene check, not a vehicle compatibility or safety test.
