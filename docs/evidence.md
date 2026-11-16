# Evidence, source coverage, and reproduction limits

This public repository is a curated account of a private investigation. It lets readers inspect the complete sanitized attempt record and understand the findings. It does not make every original experiment independently reproducible.

## Evidence levels

| Level | Example | What it establishes |
| --- | --- | --- |
| Saved vehicle diagnostic observation | A111 stored and active E84 0E after ignition | Reported configuration and status at that time. |
| Bounded original-instruction execution | Selector remap or numerical consumer | Behavior of the examined instructions under specified synthetic inputs. |
| Arithmetic model | A104 float32 recurrence | Consequences of an inferred model and its assumptions. |
| Public-source research | Parts catalogue or forum anecdote | What the source said within the documented scope. |
| Owner report | Easier parking and good highway feel | One person's perceived outcome on one car. |

No level substitutes for complete vehicle validation. In particular, DriveDown snapshots do not measure assistance under load, and reference firmware is not installed-memory readback.

## Sources for this summary

The summary was compiled from the retained attempt ledger, research reports, and saved diagnostic records from 30 October to 1 November 2026, plus the owner's 16 November driving report. Raw transcripts, machine paths, and session identifiers are excluded.

## What the public reader can reproduce

Run `python3 scripts/check_repository.py` to check document links, attempt structure, publication boundaries, and common private identifiers. Inspect [attempts.json](../data/attempts.json) for the complete sanitized results and limitations. The human-readable ledger is generated from the same retained fields.

Readers cannot rerun the firmware experiments from this checkout alone. Original BMW firmware, coding definitions, third-party decoder/manual sources, diagnostic captures, and the original analytical environment are not bundled. A proper reproduction needs independently and lawfully obtained matching inputs, their hashes, the exact tools, and explicit experiment assumptions. The original offline helpers are retained privately with those inputs; this repository does not pretend its hygiene checker reproduces their results.

## Selected evidence records

The values below were transcribed from retained reports. Hashes identify the original report bytes, not a proof of their conclusions and not a downloadable public artifact.

| Record | Key observation | Original report SHA-256 |
| --- | --- | --- |
| A106 coding trial | Accepted 0E write; independent readback; later metadata job failed. | `7340d0764e1809ff4393b7cf61ac72d37d1b1532348064d45a4a78c043c922d7` |
| A111 after ignition | Stored 0E, checksum 0A, active E84 0E, zero stored faults, DriveDown. | `74aa03813d302e44d964a905c6ab1b2a50712b4d65f2977fab0368f7d0163585` |
| A113 hardware research | Shared replacement listing; fitted rack identity unresolved. | `07289a44433488841cb0eb98a8445abd4bd3b1c8bf8c1258d6085f002f62b7a6` |
| A104 model | Conditional float32 recurrence, 192 cases; not complete controller execution. | `a278e423677482dae276e345ffae0f9a44219d351e65fcfa2d1b446dac574450` |

Current reference application 6855892 was identified in the original calibration report by SHA-256 `dfb548d495979b4a315090da09a02cb0e96d7a2f04c29cc535b6ba74e7f0426c`. The C03 schema hash was `1e405a49ad6eae2e5cc1a8531ce23e51a2784aa699a916aefaff471bc9eda0e8`. These identify research inputs, not a currently verified installed image.

## Historical external references

The following references were retained in the original research. Access dates describe that investigation. They were not freshly verified during this publication cleanup, so availability and content may have changed.

- [BMW replacement assembly 32106793457](https://www.hubauer-shop.de/en/exch-steering-box-electr-32106793457.html), accessed 1 November 2026. The recorded listing included KD91 and VL31. This supports model-level replacement applicability, not identical fitted production racks or calibration approval.
- [RealOEM 32106872478](https://www.realoem.com/bmw/enUS/partxref?diagId=32_2693&id=VG91-EUR-02-2008-E90-BMW-320d&mg=32&q=32106872478&series=E92N&sg=12) and [32106872479](https://www.realoem.com/bmw/enUS/partxref?diagId=32_1660&id=UM52-EUR---E88-BMW-120i&mg=32&q=32106872479&series=E84&sg=12), accessed 1 November 2026. Different replacement numbers and supersession chains must not be flattened into original-parts identity.
- [BMW E84 technical training](https://bmwrepairguide.com/virtual-library/technical-training/ST1205-E84-Complete-Vehicle.pdf#page=36), accessed 1 November 2026. Market-specific electric/hydraulic distinctions do not establish a European E92 rack match.
- [Hex-Rays E1F decoder source at the researched commit](https://github.com/HexRaysSA/ida-sdk/blob/04c0a982c80fd08388e7a3c26ff711fc1c38344d/src/module/nec850/ana.cpp), retrieved 1 November 2026. This resolved a specific instruction-decoding barrier in A102.
- [CarTechnology conversion discussion](https://www.cartechnology.co.uk/printthread.php?tid=9795), checked 1 November 2026. Indexed fragments named conversion 0047 and a loader manual, but direct access returned 403 and the alleged solution post was unread. No successful activation is attributed to that unread post.
- [BMWFAQ coding discussion](https://www.bmwfaq.org/threads/bmw-coding-serie-3.610553/page-72), accessed 1 November 2026. The retained report described mixed subjective results and incomplete exact-controller evidence.
- [E90Post Servotronic discussion](https://www.e90post.com/forums/showthread.php?t=1069188&p=17078573), followed during the 31 October forum work. A request or private code offer is not proof of a public working new-entitlement method.

The E90Post triage eventually reached one linked page for each of 138 search results. It did not read every page of every multipage thread. Search-index snippets, inaccessible posts, and forum anecdotes remain weaker than matched controller observations.
