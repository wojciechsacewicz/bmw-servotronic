# Research attempt ledger

This sanitized historical ledger preserves IDs A001 through A114 from 30 October through 1 November 2026. It records unsuccessful routes, useful observations, tooling failures, and later corrections. Non-research entries are kept only as numbered placeholders.

These are historical investigator conclusions, not independently reproduced results from this public checkout. Private transcript references and artifact paths are excluded. Read later entries before acting on an early conclusion. The owner added the daily-driving report on 16 November in [the outcome](outcome.md).

For a shorter route comparison, read [failed approaches](failed-approaches.md). The machine-readable source is [attempts.json](../data/attempts.json).

## Attempt index

The status labels preserve the scope of each historical conclusion. For example, `verified_synthetic` does not mean verified on the car. A later entry can narrow an earlier conclusion even when no explicit supersession was recorded.

| ID | Attempt | Historical status | Explicit later record |
| --- | --- | --- | --- |
| [A001](#a001-local-tools-and-missing-rea) | Local tools and missing REA | `verified_static` | - |
| [A002](#a002-separate-generic-coding-backups-from-actual-eps-evidence) | Separate generic coding backups from actual EPS evidence | `verified_static` | - |
| [A003](#a003-fa-date-versus-the-e92-selector) | FA date versus the E92 selector | `verified_static` | - |
| [A004](#a004-keps-token-route) | KEPS token route | `inconclusive` | - |
| [A005](#a005-max-assistance-is-already-set) | MAX assistance is already set | `verified_static` | - |
| [A006](#a006-date-side-effects-and-parser-trap) | Date side effects and parser trap | `verified_static` | - |
| [A007](#a007-audit-of-claimed-zero-cost-coding-success) | Audit of claimed zero-cost coding success | `inconclusive` | - |
| [A008](#a008-existing-entitlement-repair-branch) | Existing-entitlement repair branch | `ruled_out_for_new_entitlement` | - |
| [A009](#a009-firmware-architecture-and-archive-roles) | Firmware architecture and archive roles | `verified_static` | - |
| [A010](#a010-container-checks-and-record-type-limitation) | Container checks and record-type limitation | `verified_static` | - |
| [A011](#a011-generic-swt-and-reset-bearing-checkfsc) | Generic SWT and reset-bearing CheckFsc | `verified_static` | - |
| [A012](#a012-current-firmware-entitlement-dependent-remap) | Current firmware entitlement-dependent remap | `verified_static` | - |
| [A013](#a013-original-current-selector-synthetic-execution) | Original current-selector synthetic execution | `verified_synthetic` | - |
| [A014](#a014-fsc-padding-digest-and-signed-fields) | FSC padding, digest and signed fields | `verified_static` | - |
| [A015](#a015-identity-setter-and-zero-version-hypotheses) | Identity setter and zero-version hypotheses | `inconclusive` | - |
| [A016](#a016-program-integrity-differs-from-feature-fsc) | Program integrity differs from feature FSC | `verified_static` | - |
| [A017](#a017-original-program-signatures-and-ram-only-negative-control) | Original program signatures and RAM-only negative control | `verified_static` | A018 |
| [A018](#a018-full-normalized-program-signature-comparison) | Full normalized program-signature comparison | `verified_static` | - |
| [A019](#a019-four-public-objects-shared-divisor-check) | Four public objects shared-divisor check | `verified_static` | - |
| [A020](#a020-fsc-verification-public-key-provenance) | FSC verification public-key provenance | `verified_static` | - |
| [A021](#a021-fsc-key-against-four-other-public-moduli) | FSC key against four other public moduli | `verified_static` | - |
| [A022](#a022-initial-older67929476776704-selectors) | Initial older6792947/6776704 selectors | `verified_synthetic` | A045, A046 |
| [A023](#a023-6792947-numerical-downstream-consumer) | 6792947 numerical downstream consumer | `verified_synthetic` | - |
| [A024](#a024-old-shared-suppression-mask-producers) | Old shared suppression-mask producers | `verified_static` | - |
| [A025](#a025-rejected-alternate-decoder-continuation) | Rejected alternate-decoder continuation | `inconclusive` | - |
| [A026](#a026-historical-missing-owner-identity-blocker) | Historical missing-owner-identity blocker | `verified_static` | A027, A050 |
| [A027](#a027-initial-real-eps-reads-and-transport-recovery) | Initial real EPS reads and transport recovery | `vehicle_read_verified` | - |
| [A028](#a028-actual-missing-app00840001-fsc) | Actual missing App00840001 FSC | `vehicle_read_verified` | - |
| [A029](#a029-normal-session-flash-read-preflight) | Normal-session FLASH read preflight | `verified_static` | A030 |
| [A030](#a030-actual-normal-session-flash-read-denied) | Actual normal-session FLASH read denied | `vehicle_read_verified` | - |
| [A031](#a031-system-state-namespace-correction) | System-state namespace correction | `verified_static` | - |
| [A032](#a032-eeprom-read-prerequisite-no-live-probe) | EEPROM read prerequisite, no live probe | `verified_static` | - |
| [A033](#a033-factory-authentication-client-dependencies) | Factory authentication client dependencies | `verified_static` | - |
| [A034](#a034-open-provider-authentication-stub) | Open provider authentication stub | `verified_static` | - |
| [A035](#a035-original-winkfp-provider-binding) | Original WinKFP provider binding | `verified_static` | A075 |
| [A036](#a036-authentication-to-flash-permission-relationship) | Authentication-to-FLASH permission relationship | `inconclusive` | - |
| [A037](#a037-candidate-boot-provider-direct-side-effects) | Candidate boot provider direct side effects | `verified_static` | - |
| [A038](#a038-authentication-persistence-callbacks) | Authentication persistence callbacks | `verified_static` | - |
| [A039](#a039-programming-mode-transition-withheld) | Programming-mode transition withheld | `not_executed` | - |
| [A040](#a040-isolated-host-capability-test) | Isolated host capability test | `host_check_verified` | - |
| [A041](#a041-same-family-missing-intermediate-original) | Same-family missing intermediate original | `inconclusive` | A076 |
| [A042](#a042-bounded-v41v502-acquisition) | Bounded v41/v50.2 acquisition | `verified_static` | - |
| [A043](#a043-2010-v41-candidate-retains-current-gate) | 2010 v41 candidate retains current gate | `verified_synthetic` | - |
| [A044](#a044-bounded-v38v39-acquisition) | Bounded v38/v39 acquisition | `verified_static` | - |
| [A045](#a045-closer-earlier-originals-omit-current-selector-remap) | Closer earlier originals omit current selector remap | `verified_synthetic` | A071 |
| [A046](#a046-earlier-selector-to-calibration-consumption) | Earlier selector-to-calibration consumption | `verified_synthetic` | - |
| [A047](#a047-exact-calibration-family-comparison) | Exact calibration-family comparison | `verified_static` | - |
| [A048](#a048-boot-transition-declarations) | Boot transition declarations | `verified_static` | A083 |
| [A049](#a049-original-hwhhelpmanual-compatibility-semantics) | Original HWH/help/manual compatibility semantics | `verified_static` | - |
| [A050](#a050-dedicated-physical-hardware-identification) | Dedicated physical hardware identification | `vehicle_read_verified` | - |
| [A051](#a051-supplier-backup-zif-read) | Supplier backup ZIF read | `vehicle_read_verified` | - |
| [A052](#a052-final-ordinary-diagnostic-snapshot) | Final ordinary diagnostic snapshot | `vehicle_read_verified` | - |
| [A053](#a053-ident-software-tuple-does-not-identify-boot) | IDENT software tuple does not identify boot | `verified_static` | - |
| [A054](#a054-narrow-original-app-to-boot-contract) | Narrow original app-to-boot contract | `verified_static` | A072 |
| [A055](#a055-candidate-normal-boot-handoff-acceptance) | Candidate normal boot handoff acceptance | `inconclusive` | A072 |
| [A056](#a056-registered-normal-start-validation-task) | Registered normal-start validation task | `inconclusive` | A072, A073, A077 |
| [A057](#a057-remaining-midrange-archive-leads) | Remaining midrange archive leads | `access_limited` | - |
| [A058](#a058-bounded-local-own-entitlement-search) | Bounded local own-entitlement search | `inconclusive` | - |
| [A059](#a059-public-f30-repair-archive-leads) | Public F30 repair archive leads | `access_limited` | - |
| [A060](#a060-vin-onlyoffline-generator-claims) | VIN-only/offline generator claims | `not_demonstrated_for_target` | - |
| [A061](#a061-hidden-skip-predicates-and-actual-observability) | Hidden skip predicates and actual observability | `inconclusive` | A084 |
| [A062](#a062-durable-offline-snapshot) | Durable offline snapshot | `verified_static` | - |
| [A063](#a063-non-research-entry) | Non-research entry | `non_research_placeholder` | - |
| [A064](#a064-uncompleted-memory-access-investigation) | Uncompleted memory-access investigation | `not_completed_or_administrative` | - |
| [A065](#a065-interrupted-research-and-replacement-analysis) | Interrupted research and replacement analysis | `not_completed_or_administrative` | - |
| [A066](#a066-non-research-entry) | Non-research entry | `non_research_placeholder` | - |
| [A067](#a067-host-receive-timeouts-and-recovery) | Host receive timeouts and recovery | `failed_then_recovered` | - |
| [A068](#a068-host-job-execution-type-error) | Host job execution type error | `failed_then_recovered` | - |
| [A069](#a069-usb-adapter-absent-after-disconnection) | USB adapter absent after disconnection | `failed_then_recovered` | - |
| [A070](#a070-permanent-private-project-and-recovery-record) | Permanent private project and recovery record | `preservation_verified` | - |
| [A071](#a071-captured-coding-format-versus-earlier-original-c03-applications) | Captured coding format versus earlier original C03 applications | `verified_static` | - |
| [A072](#a072-original-boot-integrity-and-marker-helper-contracts) | Original boot integrity and marker-helper contracts | `verified_static` | A073, A074 |
| [A073](#a073-candidate-boot-hash-start-initialization-provenance) | Candidate boot hash-start initialization provenance | `verified_static` | - |
| [A074](#a074-original-application-peripheral-and-ram-initialization-delta) | Original application peripheral and RAM initialization delta | `verified_static` | - |
| [A075](#a075-original-host-interpreter-and-buffer-prerequisites) | Original host interpreter and buffer prerequisites | `verified_static` | - |
| [A076](#a076-physical-hardware-versus-catalogue-program-identifier) | Physical hardware versus catalogue program identifier | `verified_static` | - |
| [A077](#a077-registered-validation-task-activator-and-handoff-order) | Registered validation task activator and handoff order | `verified_static` | - |
| [A078](#a078-exact6794011-swt-task-and-numerical-inhibition-delta) | Exact6794011 SWT task and numerical inhibition delta | `verified_static` | A079, A080 |
| [A079](#a079-exact-older-scheduler-table-binding) | Exact older scheduler table binding | `verified_static` | - |
| [A080](#a080-registered-older-service31-rejects-current-swt-status-route) | Registered older service31 rejects current SWT status route | `verified_synthetic` | - |
| [A081](#a081-older-reference-comparison-predicts-non-normal-programming-status) | Older reference comparison predicts non-normal programming status | `verified_synthetic` | - |
| [A082](#a082-rooted-additional-hardware-initialization-leaf-equivalence) | Rooted additional hardware-initialization leaf equivalence | `verified_static` | - |
| [A083](#a083-original-earlier-boot-prefix-pair-and-retained-transition-graph) | Original earlier boot-prefix pair and retained transition graph | `verified_static` | - |
| [A084](#a084-exact-skip-bit-paired-data-provenance-and-scope-correction) | Exact skip bit paired-data provenance and scope correction | `verified_static` | - |
| [A085](#a085-ordinary-coding-and-primary-name-feasibility-boundary) | Ordinary coding and primary-name feasibility boundary | `inconclusive` | - |
| [A086](#a086-exact-identifier-public-case-search-and-diminishing-return-checkpoint) | Exact identifier public-case search and diminishing-return checkpoint | `inconclusive` | - |
| [A087](#a087-historical-original-item-catalogue-check) | Historical original-item catalogue check | `inconclusive` | - |
| [A088](#a088-user-linked-dutch-and-e90post-follow-up-with-broader-forum-triage) | User-linked Dutch and E90Post follow-up with broader forum triage | `inconclusive` | - |
| [A089](#a089-e90post-lighter-steering-search-and-interrupted-thread-triage) | E90Post lighter-steering search and interrupted thread triage | `inconclusive` | - |
| [A090](#a090-complete-e90post-result-page-triage) | Complete E90Post result-page triage | `inconclusive` | - |
| [A091](#a091-compare-current-eps-basis-variant-calibration-objects) | Compare current EPS basis variant calibration objects | `verified_static` | - |
| [A092](#a092-complete-current-eps-profile-selection-matrix) | Complete current EPS profile selection matrix | `verified_synthetic` | - |
| [A093](#a093-complete-profile-calibration-families-and-original-numerical-execution) | Complete profile calibration families and original numerical execution | `verified_synthetic` | - |
| [A094](#a094-independent-eps-flags-and-diagnostic-provenance-of-calibration-inputs) | Independent EPS flags and diagnostic provenance of calibration inputs | `verified_static` | - |
| [A095](#a095-original-oem-documentation-explicitly-supports-older-program-datasets) | Original OEM documentation explicitly supports older program datasets | `verified_static` | - |
| [A096](#a096-bounded-public-search-for-confirmed-eps-reverse-flash-outcomes) | Bounded public search for confirmed EPS reverse-flash outcomes | `inconclusive` | - |
| [A097](#a097-current-basis-profiles-traced-into-requested-motor-torque) | Current basis profiles traced into requested motor torque | `verified_bounded_synthetic` | - |
| [A098](#a098-operational-effect-of-conditional-reference-mismatch-and-host-predicate-correction) | Operational effect of conditional reference mismatch and host predicate correction | `verified_bounded_synthetic` | - |
| [A099](#a099-exact-downgrade-regression-and-improvement-assessment) | Exact downgrade regression and improvement assessment | `inconclusive` | - |
| [A100](#a100-exact-floating-point-dialect-specification-search-for-unresolved-profile-scalar) | Exact floating-point dialect specification search for unresolved profile scalar | `inconclusive` | - |
| [A101](#a101-fresh-eps-coding-read-and-write-readiness) | Fresh EPS coding read and write readiness | `vehicle_read_verified` | - |
| [A102](#a102-primary-e1f-decoder-source-resolves-torque-domain-profile-scalar-path) | Primary E1F decoder source resolves torque-domain profile scalar path | `verified_static` | - |
| [A103](#a103-trace-and-simulate-e90-basis-coding-write-path) | Trace and simulate E90 basis coding write path | `verified_synthetic` | - |
| [A104](#a104-conditional-float32-dynamics-of-newly-decoded-torque-correction) | Conditional float32 dynamics of newly decoded torque correction | `verified_synthetic` | - |
| [A105](#a105-eps-c_ci_lesen-live-and-original-ipo-replay) | EPS C_CI_LESEN live and original IPO replay | `vehicle_read_verified` | - |
| [A106](#a106-owner-triggered-ncsx-e84-basis-write-with-immediate-ecu-readback) | Owner-triggered NCSX E84 basis write with immediate ECU readback | `vehicle_write_partial_completion` | - |
| [A107](#a107-read-only-postcoding-eps-health-snapshot) | Read-only postcoding EPS health snapshot | `vehicle_read_verified` | - |
| [A108](#a108-all22-profile-contribution-comparison-and-fa-badge-interpretation) | All22 profile contribution comparison and FA badge interpretation | `verified_bounded_synthetic` | - |
| [A109](#a109-live-e92-coding00-selects-reported-e92-basis09) | Live E92 coding00 selects reported E92 basis09 | `vehicle_read_verified` | - |
| [A110](#a110-current-stored-e84-basis-but-active-e92-basis-in-diagmode) | Current stored E84 basis but active E92 basis in DiagMode | `vehicle_read_verified` | - |
| [A111](#a111-e84-basis-retained-and-active-after-ignition-cycle) | E84 basis retained and active after ignition cycle | `vehicle_read_verified` | - |
| [A112](#a112-reddit-ibac-claim-checked-against-bmw-procedure-and-current-selector-evidence) | Reddit IBAC claim checked against BMW procedure and current selector evidence | `inconclusive` | - |
| [A113](#a113-e84-and-e92-kd91-eps-replacement-hardware-comparison) | E84 and E92 KD91 EPS replacement hardware comparison | `verified_bounded_static` | - |
| [A114](#a114-current-eps-free-activation-continuation-through-ista-p-conversion0047) | Current-EPS free activation continuation through ISTA-P conversion0047 | `inconclusive` | - |

## A001 Local tools and missing REA

Date: 2026-10-30. Historical status: `verified_static`. Workstream: `tools_setup`.

Inspected installed BMW tools, CLI metadata and decompilers; checked REA availability.

Result. EdiabasX, Inpax and NCSX supported offline inspection. Windows tools and nfsx sources existed. REA MCP and PATH executable were unavailable.

Limits. Presence of files or a generic nfsx README is not EPS programming readiness. No tool installation or car execution in this stage.

Open question at the time. Does a specific later operation have a reviewed usable host implementation?

## A002 Separate generic coding backups from actual EPS evidence

Date: 2026-10-30. Historical status: `verified_static`. Workstream: `backups_provenance`.

Inspected existing FRM/KOMBI/WORK and broad coding traces.

Result. Broad FSW trace mixed ECU families; FRM/KOMBI copies were not EPS backups. WORK contained mixed vehicle provenance.

Limits. A matching keyword or unrelated module backup does not establish this EPS state.

Open question at the time. Use authentic EPS captures for vehicle claims.

## A003 FA date versus the E92 selector

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `coding`.

Evaluated C02/C03 coding rules with date and Servotronic changes.

Result. E92 selector is byte1, e92=00 versus e92_basis=09. February2009 and adding SERVOTRONIC converge on this input; March/September2009 do not change the examined rule.

Limits. Catalogue evaluation is not car activation. MAERZ09 is March2009, distinct from forum September2009 claims.

Open question at the time. Can the installed firmware accept selector0 without new FSC?

## A004 KEPS token route

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `coding`.

Inspected exact E89AT and dictionary treatment of +KEPS.

Result. Description concerns EPS FSC for older or mixed installations. No KEPS SWTASW mapping selects an alternate EPS/DSC PSW in the inspected path.

Limits. The token may belong to measures/programming workflow. It is not demonstrated free activation or an FSC-disable flag.

Open question at the time. Is there original workflow evidence of a different KEPS role?

## A005 MAX assistance is already set

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `coding`.

Mapped original MAX field, current coding bytes and bounded firmware consumers.

Result. Captured bytes2..3 are0080, exactly the only named maximal value. Selecting it again would leave this configuration unchanged.

Limits. 0x8000 physical meaning and sentinel semantics remain unknown. No demonstrated entitlement or alternate-curve selection follows from the name.

Open question at the time. What proven input changes assistance while satisfying entitlement?

## A006 Date side effects and parser trap

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `coding`.

Compared all17 EPS functions and selected DSC rules using a corrected local analysis parser.

Result. Crossing PU08 also changes3 unrelated EPS functions. A DSC BSW rule supplies a synthetic counterexample to global-date-only-affects-EPS. Compiled helper drops predicates after the first row.

Limits. Synthetic FA flags do not represent complete real FA. Original catalogues/tools were not modified.

Open question at the time. Keep a future comparison limited to the exact selector and fitted modules. No date write executed.

## A007 Audit of claimed zero-cost coding success

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_claims`.

Read first-person 2024 forum success reports and older vehicle descriptions.

Result. One probably09/2009 E88 owner describes reversible steering change without FSC purchase/import. Another supposed2011 example has conflicting08/2009 provenance and wording suggesting recovery.

Limits. No matched EPS version, previous FSC status or proof of first entitlement. Positive coding reports cannot be transferred to this2012 E92.

Open question at the time. Find an identified matching EPS with demonstrably new activation.

## A008 Existing-entitlement repair branch

Date: 2026-10-31. Historical status: `ruled_out_for_new_entitlement`. Workstream: `entitlement_sources`.

Investigated recovery alternatives and BMW repair/retrofit delivery documentation.

Result. Repair can recover an already issued entitlement. The objective is a new entitlement, so repair alone does not solve it.

Limits. No backend VIN submission, contacts or account use. Historical free-code policy is not verified current free service.

Open question at the time. Retain repair packs only as format/source evidence unless actual prior entitlement emerges.

## A009 Firmware architecture and archive roles

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `firmware_format`.

Decoded coherent startup/control flow and checked original BMW help plus ISA references.

Result. Payload supports V850 little-endian; large code regions are plaintext.0PA is program data;0BA is NAAB boot-update data including updater and boot sector.

Limits. Exact MCU/generation and complete relocation map remain unknown. Do not relabel as C166/ST10/TriCore.

Open question at the time. Resolve exact required ISA semantics where decoding stops.

## A010 Container checks and record-type limitation

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `firmware_format`.

Validated records/checksums and retained nonempty type10 payload in working reconstruction.

Result. 22 local0PA/0BA images passed byte-count/checksum checks with no conflicting overlaps under this interpretation. Generic nfsx parser would drop nonempty type10 bytes.

Limits. Container consistency is not authenticity or hardware compatibility. Proprietary type10 semantics remain a stated assumption.

Open question at the time. Preserve record types and independently validate semantics before stronger claims.

## A011 Generic SWT and reset-bearing CheckFsc

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `diagnostic_protocol`.

Decompiled generic SWT PRG and EPS IPO workflow.

Result. Status uses real ECU requests and distinct FSC/certificate/software-signature fields. IPO CheckFsc includes reset; generic adapter metadata alone is not EPS acceptance.

Limits. Decompiler library names can be inaccurate. No execution of the reset-bearing check was performed.

Open question at the time. Use only separately audited read path and captured raw responses.

## A012 Current firmware entitlement-dependent remap

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `current_firmware`.

Traced certificate lookup through current original selector and signed-feature path.

Result. Current6855892 selector queries domain30/App00840001 and can remap coded E92 index0 to basis9 on nonzero authorization result.

Limits. Archive analysis is not live-ROM equality or a complete whole-program steering proof.

Open question at the time. Which actual inputs govern this car when coded0?

## A013 Original current-selector synthetic execution

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `current_firmware`.

Executed original selector/clamp instructions with synthetic RAM and supplied authorization return.

Result. 8 scenarios reproduce0-to9 fallback, retained9, and query skipping when synthetic skip predicate is set.

Limits. Authorization callee return was substituted; no target ECU or actual hidden-bit state was executed.

Open question at the time. Identify actual skip inputs without assuming synthetic state is the vehicle state.

## A014 FSC padding, digest and signed fields

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `fsc_validation`.

Inspected complete bounded parser/signature checks and import identifier matching.

Result. Observed complete padding/DigestInfo/16-byte MD5 checks and signed identity/AppID fields contradict easy loose-padding, unsigned-wildcard and free-AppID-relabel shortcuts.

Limits. No forged FSC or general security proof. MD5 age alone supplies no chosen-certificate signature. Later key-provenance report resolves the earlier exponent gap.

Open question at the time. Any candidate must satisfy the exact verified encoding and signature path.

## A015 Identity setter and zero-version hypotheses

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `fsc_validation`.

Examined identity-setting handler, dispatch gate and descriptor-version exception.

Result. Identity setter and version0000 acceptance branch exist. Access, persistence, descriptor writability and a genuine matching App0084 certificate were not established.

Limits. RAM residence does not imply a write primitive. Donor reuse requires an existing FSC and is not a proven new no-FSC entitlement. No changes attempted.

Open question at the time. Trace descriptor initialization and authenticated identity persistence using original sources only.

## A016 Program integrity differs from feature FSC

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `program_integrity`.

Traced official programming script and08FLASH verification adapter.

Result. Program-signature verdict is ECU-sourced in official flow. Script intends verification before normal completion; decompiled error semantics and boot enforcement were not fully proven.

Limits. Container checksums and TEST_CHECKSUMME UI option do not prove arbitrary changed-program acceptance. No programming executed.

Open question at the time. Establish actual validation reachability and installed-boot behavior before any loadability claim.

## A017 Original program signatures and RAM-only negative control

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `program_integrity`.

Recomputed original RSA/MD5 archive relationship and changed one covered bit only in host RAM.

Result. Both originals match existing signatures; changed host digest no longer matches original signature. Selector lies in examined signed range.

Limits. This mathematical result is not observed ECU rejection or per-boot enforcement. No modified firmware artifact was produced.

Open question at the time. Tie exact comparator/validation path to installed boot if that evidence becomes available.

## A018 Full normalized program-signature comparison

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `program_integrity`.

Completed cancelled comparator audit using contiguous strict decode.

Result. Candidate verifier requires normalized4-word result and compares all16 digest bytes; extra nonzero high words fail length check.

Limits. Candidate archive/runtime mapping and installed boot identity remain unconfirmed. No RSA input exploit or complete model-check.

Open question at the time. Do not repeat the disproved lower128-bits-only shortcut for this function.

## A019 Four public objects shared-divisor check

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `public_keys`.

Checked equality and GCD for6 pairs among4 fixed public objects.

Result. All objects differ and every pair is coprime.

Limits. Only these objects and this trivial hypothesis were checked. No factorization or general RSA-security/impossibility conclusion.

Open question at the time. Consider only a distinct evidence-backed hypothesis, not repeating this bounded GCD test.

## A020 FSC verification public-key provenance

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `public_keys`.

Traced candidate boot fixed-ROM initialization to current application key descriptor.

Result. Candidate initialization establishes exponent3 and a1024-bit modulus for the FSC path.

Limits. Not an observation of the physically installed boot key. Original archive/runtime mapping remains a dependency.

Open question at the time. Can candidate boot be identified from authentic retained data?

## A021 FSC key against four other public moduli

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `public_keys`.

Compared the specifically identified FSC modulus with prior4 public moduli.

Result. FSC modulus differs and is coprime with each; no shared divisor in4 comparisons.

Limits. No private material, factorization, signature or installed-ECU key evidence.

Open question at the time. This narrow shared-factor route is exhausted for these exact objects.

## A022 Initial older6792947/6776704 selectors

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `older_firmware`.

Compared original complete selectors and executed their normal paths with synthetic RAM.

Result. Older selectors retain coded0 without the newer authorization-dependent remap in the bounded routines. Six synthetic runs and checks were reproduced.

Limits. No whole-program no-FSC proof and no actual hardware compatibility. Later exact closer-family originals are separate evidence.

Open question at the time. Follow selected index into real numerical consumers and assess applicability separately.

## A023 6792947 numerical downstream consumer

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `older_firmware`.

Traced index-selected curves and executed original interpolation instructions.

Result. Selected index reaches complete numerical consumer; independent arithmetic reproduces25 versus10 for synthetic raw35.

Limits. Physical units, actuator behavior and driving assistance were not measured. Shared event/mask can suppress output.

Open question at the time. Resolve suppression provenance and avoid equating numeric difference with steering-force acceptance.

## A024 Old shared suppression-mask producers

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `older_firmware`.

Traced mask aggregation, initialization, lifecycle and53 descriptors.

Result. Mechanism is generic event suppression;4 descriptors carry0x20. No explicit App0084 lookup in examined producers.

Limits. Authorization could influence upstream events outside scope. No whole-program absence proof.

Open question at the time. Only expand a concrete upstream gap, not repeat the bounded absence claim.

## A025 Rejected alternate-decoder continuation

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `firmware_format`.

Checked old downstream decode stop41f8c against independent GNU encoding definitions.

Result. Default decode remains unresolved. Apparent v850e3v5 pushsp continuation violates fixed encoding bits and is not acceptable downstream evidence.

Limits. No complete next-function behavior. A decoder producing more text is not ISA compatibility evidence.

Open question at the time. Find correct instruction encoding/MCU evidence before continuing that function.

## A026 Historical missing-owner-identity blocker

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `identity`.

Searched bounded local artifacts and prepared exact needed EPS identification evidence.

Result. Initial search found no trustworthy owner EPS identity. That historic blocker was later removed by actual EPS reads.

Limits. Historical unresolved status must not be reported as current. VIN, FRM and archive filenames never established installed EPS identity.

Open question at the time. Use subsequent actual captures as current reported identity.

## A027 Initial real EPS reads and transport recovery

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `vehicle_reads`.

After parked/ignition confirmation, captured IDENT,AIF,coding,STATUS_EPS and fault reads; adjusted host receive timeouts after failures.

Result. Reported application6855892/C03/reference0512IC0F780A; coding byte1=09. Reads succeeded after local timing adjustment and disconnected.

Limits. Timeout recovery changed host waits only. Reported program identity is not full-ROM equality; early failed attempts are retained.

Open question at the time. No coding or activation occurred; use separate physical-hardware read for rack applicability.

## A028 Actual missing App00840001 FSC

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `vehicle_reads`.

Captured actual SWTGetStatus and decoded saved reply offline with original PRG.

Result. ECU reports00840001 FSC and FSC certificate NICHT_VORHANDEN; software signature AKZEPTIERT.

Limits. Accepted software signature is distinct from feature entitlement. Status does not prove historical entitlement absence.

Open question at the time. A successful target outcome requires new entitlement or independently proven free activation for this ECU.

## A029 Normal-session FLASH read preflight

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `protected_reads`.

Audited original SPEICHER_LESEN request and current service23 handler.

Result. Generic Default-mode metadata does not guarantee FLASH access. Current handler has explicit gate; ROMI/LAR do not supply an alternate mapping here.

Limits. No car action in this audit. Handler conclusions inherit archive mapping and are not universal over every mode.

Open question at the time. One separately authorized minimal actual probe can distinguish current access; its saved result isA030.

## A030 Actual normal-session FLASH read denied

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `protected_reads`.

Sent one16-byte FLASH read at10000 in segment06 without unlock or session change.

Result. Raw7F2333 with valid checksum, securityAccessDenied; zero program bytes.

Limits. No retry/unlock/write. Denial is for this actual request/session, not proof that all possible read paths are impossible.

Open question at the time. Do not repeat the identical probe without a new demonstrated prerequisite.

## A031 System-state namespace correction

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `protected_reads`.

Mapped captured DID0004 word and exact original PRG decoder branches.

Result. Captured state2 means DriveDown;3 means Factorytest;7 means DiagMode. These are operating states, not interchangeable session IDs.

Limits. Historical capture does not establish current state or an entry procedure.

Open question at the time. Interpret every permission prerequisite in its actual namespace.

## A032 EEPROM read prerequisite, no live probe

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `protected_reads`.

Audited EEPROM_LESEN structured input and segment02 backend.

Result. Original helper requires operating state7; captured state2 fails before storage backend.34 instruction checks and capture validation passed.

Limits. Static assessment completed; EEPROM vehicle probe was not executed. No EEPROM dump or actual live denial was obtained.

Open question at the time. Do not call this an EEPROM read result or enter a state experimentally.

## A033 Factory authentication client dependencies

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `factory_auth`.

Audited EPSPL2 script,08FLASH routines and original host dependencies.

Result. Factory client uses31/07 and31/08 asymmetric workflow; a27 SecurityAccess workflow was not demonstrated. Host response preparation is a dependency.

Limits. No authentication challenge/response execution, credential extraction or unlock.

Open question at the time. Does the original host expose a supported neutral provider invocation?

## A034 Open provider authentication stub

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `factory_auth`.

Inspected compiled NCSX CABI authentication functions and Wine availability.

Result. Authentication response/random functions are stubs with empty data. Wine exists but original WinKFP runtime was not tested.

Limits. Stub success is not ECU authentication. This does not prove original WinKFP lacks implementation.

Open question at the time. Assess original host binding rather than treating stub as functional.

## A035 Original WinKFP provider binding

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `factory_auth`.

Followed original EXE name/pointer table and direct calls beyond embedded strings.

Result. Original host contains internally bound authentication implementation; no demonstrated standalone exported API. CABI language DLLs have no PE exports.

Limits. IPO external-function mapping, native ABI and initialized runtime are not proved. No original process launched.

Open question at the time. Find a supported host invocation with initialization and inert inputs before readiness claims.

## A036 Authentication-to-FLASH permission relationship

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `factory_auth`.

Traced dispatch, queued tasks and actual indirect boot-provider call.

Result. Concrete service/task/provider path exists. Successful factory auth to requested FLASH-read permission was not established.

Limits. Unknown relation is not proof of independence. Candidate installed boot pairing is missing.

Open question at the time. Trace a concrete permission consumer or identify target boot; do not assume auth success grants read.

## A037 Candidate boot provider direct side effects

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `factory_auth`.

Decoded complete direct-callee normal-success closure.

Result. 15 bodies,960 instructions and22 direct call sites constrain writes to stack,digest/arithmetic work buffers; no direct permission-state update in closure.

Limits. Installed boot not identified and application callbacks are outside this result. No broad impossibility conclusion.

Open question at the time. Use callback resultA038 and distinct unresolved permission provenance.

## A038 Authentication persistence callbacks

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `factory_auth`.

Traced asynchronous record destination and completion chain.

Result. Auth-success byte reaches recordRAM0f77 and completion writes0f80; neither directly matches known gate inputs.

Limits. Bounded normal path does not exclude indirect later consumers influencing permission.

Open question at the time. Locate an actual downstream consumer rather than inventing a direct unlock effect.

## A039 Programming-mode transition withheld

Date: 2026-10-31. Historical status: `not_executed`. Workstream: `factory_auth`.

Inspected DIAGNOSE_MODE metadata and reset prerequisite.

Result. ECUProgrammingMode requires reset/recovery; it is not a neutral read. No mode transition was executed.

Limits. No runtime post-reset permission result. Success31/08 and boot diagnostic availability are separate events.

Open question at the time. Any future mode change is a separate scoped operation, not implied by ordinary-read authorization.

## A040 Isolated host capability test

Date: 2026-10-31. Historical status: `host_check_verified`. Workstream: `tools_setup`.

Ran bubblewrap namespace/device/network boundary check and read simulation/compile documentation.

Result. Live host test saw only loopback and private pseudodevices, without real serial/CAN/X11. EDIABAS simulation is documented; no SIM fixture or neutral provider runner established.

Limits. No BMW/Wine process launched. Host isolation test is not provider functionality or car acceptance.

Open question at the time. Recheck boundaries if a private prefix/config or launcher is added.

## A041 Same-family missing intermediate original

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `oem_acquisition`.

Audited local HIS,HWH and exact original transition references.

Result. 6851800 is immediate history predecessor of6855892 and shares a row, making it a useful missing artifact lead. Neither local tree contains6851800A.0pa.

Limits. History is not supported downgrade, expected filename proof or FSC absence.

Open question at the time. Find period assembly-to-file mapping and original bytes rather than assuming assembly equals filename.

## A042 Bounded v41/v50.2 acquisition

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_acquisition`.

Fetched ZIP indices and selected EPSPL2 ranges from public mirrors.

Result. Acquired original-format6798892/0512300F580A with period sidecars. Complete2 package inventories lack6851800 filename.

Limits. Public mirror provenance is not independent BMW authenticity. Absence applies only to inventoried packages. No multiGB download or firmware execution.

Open question at the time. Assess acquired exact revision and seek distinct intermediate source only if relevant.

## A043 2010 v41 candidate retains current gate

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `older_firmware`.

Compared exact original selector,extraction,descriptor,remap and clamp spans; ran bounded synthetic cases.

Result. 6798892/0512300F580A spans are identical to current and reproduce entitlement-result0-to9 fallback. This candidate is not the proposed old-selector escape.

Limits. Does not prove reverse installation compatibility or all states. Same public key is not approval.

Open question at the time. Do not generalize this finding to every051230 revision.

## A044 Bounded v38/v39 acquisition

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_acquisition`.

Inventoried full ZIP filenames and obtained selected original-format applications plus4 period sidecars each.

Result. Found6793465=0511N00F360A and6794011=0512300F400A. v39 6798892 matches v41 bytes. Both inventories lack6851800/6797547 filenames.

Limits. Record/signature consistency does not certify actual hardware acceptance. No complete package download or target execution.

Open question at the time. Evaluate exact originals, preserving F400/F580 behavior distinction.

## A045 Closer earlier originals omit current selector remap

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `older_firmware`.

Compared original6793465 and6794011 complete selectors and executed actual instructions with no authorization stub.

Result. Both retain0 and9 normally in4 synthetic runs. They differ materially from later6798892 despite shared051230 prefix for one revision.

Limits. Bounded selector result is not full missing-FSC operation or compatible downgrade.

Open question at the time. Trace the same active output into consumers and keep hardware proof separate.

## A046 Earlier selector-to-calibration consumption

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `older_firmware`.

Executed each original selector then full identified consumer while retaining synthetic output.

Result. 4 runs,550 consumer instructions each, no external stub;0 and9 reach distinct original arrays and inverse pairs.

Limits. Scheduler excerpts are static; whole startup,missing-FSC behavior,hardware and physical steering remain unproved.

Open question at the time. Can applicability and full operating context be established without experimental installation?

## A047 Exact calibration-family comparison

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `older_firmware`.

Compared complete bounded consumer and every curve of selected families across3 originals.

Result. Index0 family and index9 family each remain byte-identical across6793465,6794011,current6855892;0 differs from9.

Limits. 212 data bytes per index for one consumer do not prove full-controller calibration compatibility or physical steering.

Open question at the time. Do not substitute bounded data identity for full application/hardware compatibility.

## A048 Boot transition declarations

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Acquired3 original transition archives as data and validated directives/CRC/hash/records.

Result. Edges are051120->0511N0,0512DK->0511N0 and0511N0->051230. None declares installed0512IC as source. Local16-edge graph supplies no supported reverse path.

Limits. No missing-edge universal impossibility or assumption that every app change needs a boot update. No programming.

Open question at the time. Seek affirmative exact applicability evidence rather than reversing arrows or lexical reference order.

## A049 Original HWH/help/manual compatibility semantics

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Read installed original help and acquired full2004 WinKFPT manual as data.

Result. HWH explicitly concerns compatible hardware history in series; markers/row grammar/reverse approval are undefined. Manual reference mismatch is not an absolute tool prohibition and does not establish safety.

Limits. Historical manual is not current hardware approval. Shared row or selectable file is insufficient downgrade proof.

Open question at the time. Need explicit applicability or complete matched hardware/boot contract evidence.

## A050 Dedicated physical hardware identification

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `vehicle_reads`.

Prepared exact guarded read scope, then read after fresh parked/ignition confirmation.

Result. 3 actual requests positively report physicalHW6851800 and hardware reference0512IC0 alongside application6855892/C03; checksums pass and disconnect.

Limits. Triplicated fields within one reply are not3 independent observations; physical rack label and older-app compatibility remain unproved.

Open question at the time. Use actual physical/reference identity for every subsequent candidate assessment.

## A051 Supplier backup ZIF read

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `vehicle_reads`.

Reviewed exact guard and read ZIF_BACKUP_LESEN while readiness authorization still applied.

Result. 2 read requests succeed; backup program reference and hardware number are all zeros. No earlier installed-program identity obtained.

Limits. Zero backup is not boot identity or proof no previous software ever existed. No writes/reset.

Open question at the time. Do not infer a downgrade target or boot version from this empty backup.

## A052 Final ordinary diagnostic snapshot

Date: 2026-10-31. Historical status: `vehicle_read_verified`. Workstream: `vehicle_reads`.

Completed16 additional jobs using18 positive identification/data reads before disconnecting.

Result. Retained supplier serial/reference,VIN,status/sensors,offset,flash metadata,coding index and test stamp. Current ZIF agrees with0512IC0F780A/6855892.

Limits. Stationary snapshots are not driving/sensor-accuracy tests,program memory dump or flash permission. No later readiness follows from this session.

Open question at the time. Continue offline; any future vehicle session needs fresh readiness and concrete missing evidence.

## A053 IDENT software tuple does not identify boot

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `identity`.

Mapped saved raw version triplets to original serializer sources.

Result. MCV0.29.124,FSV6.7.0,OSV4.0.4,RES0.0.0 all come directly from application ROM. OSV cannot fingerprint installed boot.

Limits. Other boot metadata access in same serializer does not change version-tuple provenance. No live-ROM read.

Open question at the time. Do not claim installed boot identity from OSV or application reference.

## A054 Narrow original app-to-boot contract

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Compared entry vectors,startup windows and fixed service-table slot across earlier/current originals.

Result. Examined vectors and actual20E0 service use support a shared narrow interface; no concrete incompatibility within those windows.

Limits. Shared interface is not whole RAM/driver/hardware compatibility. Boot addresses depend on candidate50000 displacement; installed boot unknown.

Open question at the time. Resolve full validation and applicability before any recommendation.

## A055 Candidate normal boot handoff acceptance

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `oem_compatibility`.

Traced startup selection closure and checked application image-end word in3 originals.

Result. Inspected handoff condition does not compare textual app/hardware references. All3 archive locations haveFFFFFFFF, including current original.

Limits. Archive word state is not physically installed memory state; proves neither older acceptance nor rejection.

Open question at the time. Tie subsequent normal main flow to actual validation and input provenance.

## A056 Registered normal-start validation task

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `oem_compatibility`.

Continued normal initialization and neighboring checker analysis.

Result. Checker is registered as task2. Initial lists select0 or3; actual scheduling of2 and2 helper contracts remain unresolved. Same inspected header branch covers3 originals.

Limits. Registration is not execution. Different-reference branches cannot be used to reject these originals when their common header takes another branch.

Open question at the time. Resolve activation of task2 and exact helper contracts; installed boot still needs identification.

## A057 Remaining midrange archive leads

Date: 2026-10-31. Historical status: `access_limited`. Workstream: `oem_acquisition`.

Searched distinct v42-v46 package leads after v38/v39/v41/v50.2 inventories.

Result. 2015 v46.1 thread is indexed but direct page returned403. Other leads were historical or coding-only; no new full-package source verified.

Limits. No attachment acquired; content/relevance unknown. v42 lite is not evidence of flash-app availability. This is bounded search,not global absence.

Open question at the time. Only pursue a public accessible full package with relevant period mapping.

## A058 Bounded local own-entitlement search

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `entitlement_sources`.

Searched named BMW roots,small ZIP indices and bounded text/extension candidates.

Result. No own VIN-matched FSC/repair pack or authenticated factorySA216 evidence identified. Two FA traces omit216 but have weak provenance.

Limits. Excluded dependencies/browser/generated paths and files above2MB from text scan. No historical-entitlement impossibility conclusion.

Open question at the time. New entitlement remains target; local generic FSC source code is not a personal licence.

## A059 Public F30 repair archive leads

Date: 2026-10-31. Historical status: `access_limited`. Workstream: `entitlement_sources`.

Checked FSC_K652168.zip andJ730734.zip forum references.

Result. First attachment listing concernsF30 App0083; no exposed download. Second indexed repair success is inaccessible directly with403. Neither archive obtained or parsed.

Limits. No ZIP hashes,actual AppID/VIN fields,signature metadata or E92 acceptance evidence. Account requirement not established just from missing link.

Open question at the time. Need an actual lawful accessible sample before format conclusions; anotherVIN/App0083 is not newE92 App0084.

## A060 VIN-only/offline generator claims

Date: 2026-10-31. Historical status: `not_demonstrated_for_target`. Workstream: `entitlement_sources`.

Audited3 concrete generator claims and primary BMW portal/ordering documents.

Result. CIC source targets navigation1B maps; IAS claims head-unit generation; MDG1 post listsDME IDs without0084. No demonstrated new EPS00840001 generator candidate found.

Limits. Ruled out means these reviewed tools as supplied,not all imaginable free methods. No target tool execution,VIN submission or activation.2019 source supersedes old ASAP wording but not verified2026 portal state.

Open question at the time. Require explicit EPS0084/index0001 source/input evidence and matching unmodified-EPS acceptance.

## A061 Hidden skip predicates and actual observability

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `current_firmware`.

Traced both skip predicates and audited saved status/metadata serializers.

Result. FF/FF predicate is false in actual captures. RAM359e bit0 remains unknown after8-DID and4 metadata-source audits. Default/shared field evidence is not actual bit value.

Limits. Active9 plus missing FSC does not predict coding0 outcome. Shared field has broad consumers; no healthy persistent coding-only skip route proved.

Open question at the time. Find an exact observable source or authorized nonexperimental evidence for the bit; do not infer from zeros/test stamp.

## A062 Durable offline snapshot

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `backups_provenance`.

Saved car captures,research,diagnostic definitions and original reference files outside scratch and verified copied hashes.

Result. Snapshot location is recorded in offline-snapshot-location.json and final capture report. It is a material backup of investigation evidence.

Limits. Not full individual flash/EEPROM/RAM or whole-car dump. Retained metadata records location; this inventory pass did not rehash external snapshot.

Open question at the time. Preserve canonical project and snapshot; validate hashes before relying on a future restored copy.

## A063 Non-research entry

Date: 2026-10-31. Historical status: `non_research_placeholder`. Workstream: `record_scope`.

Non-research entry; no technical content.

Result. ID retained for numbering.

Limits. No vehicle experiment or activation evidence.

Open question at the time. None.

## A064 Uncompleted memory-access investigation

Date: 2026-10-31. Historical status: `not_completed_or_administrative`. Workstream: `operations`.

The proposed memory-access analysis was not completed.

Result. The proposed memory-access analysis produced no verified result.

Limits. No additional controller behavior or activation result follows from this record.

Open question at the time. Use completed technical reports rather than infer a result from this entry.

## A065 Interrupted research and replacement analysis

Date: not recorded. Historical status: `not_completed_or_administrative`. Workstream: `operations`.

Some analysis was interrupted before producing a completed result.

Result. Some research runs were interrupted. Later reports, rather than cancelled work, supply the completed evidence.

Limits. No additional controller behavior or activation result follows from this record.

Open question at the time. Use completed technical reports rather than infer a result from this entry.

## A066 Non-research entry

Date: 2026-10-31. Historical status: `non_research_placeholder`. Workstream: `record_scope`.

Non-research entry; no technical content.

Result. ID retained for numbering.

Limits. No vehicle experiment or activation evidence.

Open question at the time. None.

## A067 Host receive timeouts and recovery

Date: 2026-10-31. Historical status: `failed_then_recovered`. Workstream: `vehicle_read_failures`.

Attempted early ordinary EPS reads and retained their timeout errors.

Result. Two sessions recorded Send and receive timed out; later reads succeeded after reviewed host timing changes.

Limits. A host timeout is not an ECU rejection or proof that the requested feature is unavailable.

Open question at the time. Keep successful raw captures and do not repeat a failed transport setup without cause.

## A068 Host job execution type error

Date: 2026-10-31. Historical status: `failed_then_recovered`. Workstream: `vehicle_read_failures`.

Recorded the early value.trimEnd is not a function failure with partial successful captures.

Result. The host job failed; the raw/decoded results already obtained were retained, and later AIF evidence was captured.

Limits. This record does not claim every underlying interpreter/string-formatting issue is fixed. It is not a vehicle fault.

Open question at the time. Check raw bytes against the original definition where displayed strings are incomplete.

## A069 USB adapter absent after disconnection

Date: 2026-10-31. Historical status: `failed_then_recovered`. Workstream: `vehicle_read_failures`.

Attempted a session while the adapter port was absent; preserved the error.

Result. The device path could not be opened. The user later confirmed reconnection and subsequent reads succeeded.

Limits. Port absence is not a firmware or licence result. No command reached the ECU in that failed open.

Open question at the time. Fresh readiness is still required for any future session.

## A070 Permanent private project and recovery record

Date: 2026-10-31. Historical status: `preservation_verified`. Workstream: `preservation`.

Moved the complete research/environment to the local private project, preserved references and attachments, and exported visible history.

Result. Canonical project, attempt ledger, append-only decisions, restart instructions and evidence manifest are established.

Limits. The frozen export has a cutoff and excludes internal reasoning. The evidence remains an EPS diagnostic collection, not a complete car/installed-memory dump.

Open question at the time. Append every meaningful future result, update current status and verify preserved evidence.

## A071 Captured coding format versus earlier original C03 applications

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Compared preserved C02/C03 definitions, all three complete original coding loaders, actual coding capture and original coding-index identification paths.

Result. Both earlier originals declare C03. The saved25-byte block has the required zero XOR and the same examined field positions. All234 loader instructions align after explicitly checked relocation; no coding-format incompatibility established.

Limits. The leading83 byte is feature data, not a version header. A narrow format match does not prove identical feature semantics, storage/EEPROM migration, hardware compatibility, activation or steering response. No alternate coding data or installation procedure was produced.

Open question at the time. What original evidence establishes complete driver/shared-state and storage compatibility with the reported6851800/0512IC0?

## A072 Original boot integrity and marker-helper contracts

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Linked the first normal-checker helper to the prior signature proof and resolved the second helper argument/status contract with conditional original driver provenance.

Result. First helper uses program-signature integrity and existing earlier signatures verify for stated archive spans. Second helper is write-like marker processing under the examined initialized-object condition, not a demonstrated tail-equality rejection. No app/boot reference-equality predicate was established inside the inspected contracts.

Limits. Runtime hash-start words03ff1088/108c, actual initialized driver/callback state, task scheduling and installed boot identity remain unproved. Neither helper result predicts real acceptance or safety.

Open question at the time. Establish original runtime hash-start and driver initialization provenance, while keeping candidate-source evidence separate from installed ECU behavior.

## A073 Candidate boot hash-start initialization provenance

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Traced original startup copy descriptor and tables to the two hash-start words, then independently checked source bytes, helpers and initializer table overlaps.

Result. Conditional candidate boot initialization writes10000 and10100 to RAM03ff1088/108c. No later operation within the examined initializer tables overwrites them. Initial spans match the earlier original-signature arithmetic.

Limits. Does not prove preservation until verification, actual validation-task scheduling or installed-boot identity. The source exploration is static, not complete CPU execution.

Open question at the time. Can original scheduling and later writes establish the hash inputs actually used by the validation task?

## A074 Original application peripheral and RAM initialization delta

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Compared four startup function families across three originals and independently decoded all three copy callbacks; checked exact transfer rows and overlap with the candidate boot FSC object.

Result. One peripheral helper is byte-identical.6793465 initializes an interval covering the current boot FSC public-key object;6794011/current avoid that particular overlap. Stack and data intervals differ.

Limits. Overlap alone does not prove an incompatible object lifetime. Avoiding it does not prove overall compatibility. No activation, driver acceptance or physical response established.

Open question at the time. Determine the relevant shared-object lifetimes and the remaining boot-service and hardware-facing contracts before any compatibility conclusion.

## A075 Original host interpreter and buffer prerequisites

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `original_provider`.

Traced original function-table registration and seven adapter argument-resolution calls to interpreter and host-buffer state; independently checked selected instruction patterns.

Result. Provider adapter depends on active interpreter state and buffer registry, beyond DLL discovery. Name/code registration is observed; raw table offset is not proved IPO ordinal. No documented neutral runner or new-FSC linkage found in the bounded source scope.

Limits. Complete IPO symbol resolution and initialized lifecycle remain unproved. Static prerequisites are not a working provider or new entitlement.

Open question at the time. Before additional provider integration, establish a concrete connection to a needed observation or entitlement condition; otherwise prioritize the application compatibility gaps.

## A076 Physical hardware versus catalogue program identifier

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Checked original HW/ZB definitions against separate physical-ID labels and the actual current DAT row; revisited A049 history semantics without claiming them new.

Result. Catalogue HW number denotes the program dataset. Physical6851800 alone does not require6851800A.0pa; current DAT uses program6855892. Missing6851800 remains a historical-artifact lead, not a demonstrated obligatory hardware image.

Limits. Terminology correction and forward ancestry do not establish reverse6794011 applicability. Existing HWH/HIS findings are revalidated prior results.

Open question at the time. Seek evidence of actual earlier-program applicability and shared-state/driver contracts rather than relying on physical-id filename equality.

## A077 Registered validation task activator and handoff order

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Identified task2 activation routine, extended the initial task0/task3 chain to task4, checked its indirect callback and original initial value, and verified the direct handoff construction.

Result. Routine69b8 queues validation task2. Initial tasksqueue4; task4callbackslot109c initializeszero. Candidate startup has a direct10110handoff branch before dispatcher initialization. Normal activation of2 and later state remain unproved.

Limits. Registered validation is not established as mandatory before every handoff. Actual selected path, prior lifecycle validation, callback writers and installedboot identity remain unknown.

Open question at the time. Prove relevant normal-path callback/helper provenance and hash preservation, or obtain authoritative installed-boot evidence.

## A078 Exact6794011 SWT task and numerical inhibition delta

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Compared a concrete current domain30 SWT task against aligned old code and candidate task arrays; mapped exact6794011 numerical suppression.

Result. Current1a080 SWT task occupies an additional code interval between matching helpers; current array has11 pointers versus candidateold10. Exactoldconsumer has generic event-mask suppression, with no second directFSCcheck proved in the inspected closure.

Limits. Old scheduler binding and any relocated or differently implemented licensing manager remain unproved. Negative byte searches are locator failures, not whole-program absence proof. No completecompatibility established.

Open question at the time. Trace actualoldtask-array binding and service31/1f registration before claiming absenceofoldFSCenforcement.

## A079 Exact older scheduler table binding

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Traced old task-index pointer load and transfer trampoline, checked activation sentinels and compared priority metadata with the current configuration.

Result. The older14274 table is actually used by the scheduler. Its configured ten tasks correspond to eleven current tasks with the additional current SWT slot removed.

Limits. Configured sentinel/count is not a general invalid-index guard. Other old task semantics and whole-program licensing absence remain unresolved.

Open question at the time. Assess remaining shared-state/driver applicability and possible alternative old licensing mechanisms; do not repeat the now-proved table-binding check.

## A080 Registered older service31 rejects current SWT status route

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `oem_compatibility`.

Traced old service31 registration into its complete handler, compared the actual current1f/F6 path, and executed the original old handler prefix with explicit synthetic requests.

Result. Old registered handler routes1f,F6 to NRC12. Each examined prefix executes31 instructions without external calls or stubs, stopping before the error helper. Current handler queues SWT task6 and dispatchesF6 to the status serializer.

Limits. Synthetic execution does not transmit a full response or run the complete dispatcher/physical ECU. Absence of the current registered route does not exclude another old licensing implementation or prove hardware compatibility.

Open question at the time. Resolve older whole-program missing-FSC behavior and hardware/boot applicability without treating diagnostic-interface absence as an activation result.

## A081 Older reference comparison predicts non-normal programming status

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `oem_compatibility`.

Traced a real hardware-reference consumer and its registered diagnostic caller, executed the original comparison suffix with captured and matching references, and freshly parsed the original status definition.

Result. Captured0512IC0 versus old0512300F400A yields payload0x0c in74 original instructions; matching0512300 yields0x01 in87. Zero calls/stubs. Original routine31/0a is programming-status read;0x0c means program absent/incomplete and0x01 normal operation.

Limits. Earlier asynchronous-read, flag and triple-copy prerequisites were not executed. Conditional status mismatch is not proof of ordinary steering inhibition, unconditional tool abortion or hardware incompatibility. Assumes captured reference metadata retained.

Open question at the time. Establish a coherent OEM application/boot/hardware-reference pairing before considering the older application a compatible route.

## A082 Rooted additional hardware-initialization leaf equivalence

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Followed original initialization wrappers to another hardware-facing leaf and compared full bytes, immediate constants and ordered MMIO effects.

Result. Old4b0d8/current4ef1c leaves are byte-identical42-byte,12-instruction routines with seven ordered MMIO operations. Rooted direct call anchors verify.

Limits. Peripheral identity unknown; do not label ADC/motor/sensor. Equal incoming state and preceding callees returning are unproved. A short shared leaf does not resolve reference mismatch or whole hardware compatibility.

Open question at the time. Prioritize the concrete reference/pairing inconsistency over accumulating additional small code matches.

## A083 Original earlier boot-prefix pair and retained transition graph

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `oem_compatibility`.

Parsed all16 retained boot declarations plus three duplicate v38 copies; compared old230/currentIC metadata, application prefixes and mapped-byte differences.

Result. Original230 boot payload matches old6794011 six-character reference prefix. Raw templates are not complete populated runtime metadata. Retained graph has230-to-IC but no declaration sourced fromIC and no directed reverse path.

Limits. Prefix coherence and small mapped difference count do not prove boot equivalence, physical applicability, installed identity or approved rollback. Negative graph scope is retained originals only.

Open question at the time. Require affirmative applicability and populated-metadata provenance for the exact earlier pair rather than assuming a reverse transition.

## A084 Exact skip bit paired-data provenance and scope correction

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `current_software_configuration`.

Mapped actual default-copy block indices306/307 to target rows273/278, checked defaults and paired descriptors, and separated exact bit16 from other low-byte consumers.

Result. Byte359e bit0 is bit16 of field359c. Default03fc0000 clears it. Conditional paired blocks include the field, which participates in integrity input. Wider effects of other low-byte bits do not establish effects of bit16.

Limits. Actual bit value, startup block selection, manufacturer name, healthy production meaning and complete indirect-consumer coverage remain unknown. No isolated coding activation mode established.

Open question at the time. Find primary production semantics or actual read-only evidence for this exact bit; do not infer effects from other bits or pursue blocked operational writes.

## A085 Ordinary coding and primary-name feasibility boundary

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `current_software_configuration`.

Mapped ordinary coding feature fields, bounded consumers and original catalogue names; inspected the retained schema and source excerpts.

Result. Ordinary feature fields directly decode to3198/35e2 rather than359c. No explicit coding-to-skip-bit transfer or primary healthy-production definition was established.

Limits. Not all eleven separately analyzed source windows were independently rerun. Other indirect dataflow remains possible; missing local names are not global absence proof.

Open question at the time. Requires a new address-specific primary definition or discriminating runtime evidence; do not repeat the same coding catalogue analysis.

## A086 Exact identifier public-case search and diminishing-return checkpoint

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_research`.

Ran eight public search queries and read the relevant two-page2022 owner thread and2013 owner report; audited the practical value of continued autonomous analysis.

Result. No matched-car free-new-entitlement demonstration obtained. The2022 owner already hadFSC;2013 report concerns persistent hardware failure. Further fan-out is gated on new primary evidence or a critical discriminating test.

Limits. Bounded search does not establish impossibility or universal absence. Goal remains active, not achieved or paused.

Open question at the time. Resume substantive exploration only with new evidence capable of changing the activation assessment.

## A087 Historical original-item catalogue check

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_research`.

Checked original-item listings for the model and entitlement item.

Result. A catalogue listing included E92 LCI 318i KD91/N43. It did not establish a free activation method.

Limits. Historical generic catalogue applicability does not establish an installed quote, exact vehicle eligibility, or successful entitlement provisioning.

Open question at the time. Does primary retrofit documentation establish exact eligibility and a legitimate provisioning workflow?

## A088 User-linked Dutch and E90Post follow-up with broader forum triage

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_research`.

Checked prior coverage, read all15 visible posts in1069188, retrieved Dutch indexed discussion, triaged retained138 search items and read relevant EPS/FSC and conversion pages through October2026.

Result. Dutch reply quotes mecale reporting failed VO/date change; matching E90Post username seeks0084/0001 and receives a private ASAP-related code offer, without public activation proof. Conversion reports do not demonstrate missing-FSC6855892 activation.

Limits. Dutch content is search-index text; cross-forum identity is inferred. Selected windows of six-page conversion thread, failed fetches and private messages prevent exhaustive coverage. No car operations or verified new entitlement.

Open question at the time. Does any public case provide exact6855892 identity, initially absentFSC and verified new free activation?

## A089 E90Post lighter-steering search and interrupted thread triage

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_research`.

Inventoried 14 public search-result pages and triaged linked forum pages, including a 2012 E91 EPS replacement discussion. Page coverage remained incomplete in this pass.

Result. 138 distinct result threads inventoried; 82 thread URLs attempted, 80 recognizable pages and two timeouts. A conversion user subjectively preferred an E90 EPS; a 2012 E91 replacement report remained unresolved. Neither demonstrates a compatible lighter setup for the owner.

Limits. Only one linked page per triaged thread, limited extracted snippets, not full reading. 56 result threads unattempted and two timed out. Some pages could not be opened in this pass. No vehicle access, test, transmission or activation.

Open question at the time. Examine remaining results and relevant multipage EPS alternatives, including donor calibration fit and steering diagnostics.

## A090 Complete E90Post result-page triage

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `public_research`.

Completed the remaining result-page triage after the earlier interruption.

Result. All 55 opened as recognizable thread pages. Together with earlier 80 pages and three directly read results, all 138 results were reached at one linked page each. The conversion author attributes his preferred E90 setting to VARIANTENCODIERUNG_1 on an earlier donor EPS.

Limits. Search-page inventory is not a whole-site census; one linked page per result is not reading all multipage posts. Reports are anecdotal and the donor is not the owner car. No vehicle access.

Open question at the time. Identify whether the current EPS basis variants have distinct relevant calibration and establish its physical meaning.

## A091 Compare current EPS basis variant calibration objects

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `offline_research`.

Compared indices 9 and 13 in two pointer tables used by the archived 6855892 numerical consumer, with original hash, record checksum and overlap checks.

Result. The 0x185c8 six-point objects differ; the 0x18210 ten-point objects are byte-identical. The captured coding is index 9 and catalogue index 13 is E90 basis.

Limits. Selected objects only, no physical units, no full behavior or safety inference. Conditional remap and hypothetical actual selection not established; archive parser assumes type16 handling. No vehicle writing or steering measurement.

Open question at the time. Determine the object input/output physical meaning and runtime variant selection before assessing a compatible intervention.

## A092 Complete current EPS profile selection matrix

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `independent_eps_calibration`.

Reparsed22 original C03 names and executed complete current selector/clamp in230 synthetic contexts plus44 earlier-original cases.

Result. E90_basis13 survives all tested authorization-return and skip classes in normal mode; E90/E914/5 maps13 on nonzero helper return. No universal fallback to E92_basis9.

Limits. Authorization helper return is substituted. No full startup, coding acceptance, rack applicability or lighter physical steering proved.

Open question at the time. Does the independently retained alternative profile provide a suitable lower-effort response?

## A093 Complete profile calibration families and original numerical execution

Date: 2026-10-31. Historical status: `verified_synthetic`. Workstream: `independent_eps_calibration`.

Decoded22 profiles/198 numerical objects/127 auxiliary curves; executed original consumers and zero-speed interpolation; inventoried29 archives and matched22 objects across9 distinct applications.

Result. E90_basis13 differs from E92_basis9 in4of9 numerical objects and6of6 curves. Original calculations differ with no external stubs. Curves cross, so no uniform increase;22 selected objects occur in5of9 applications.

Limits. Bounded synthetic inputs and intermediate results do not prove physical effort. Decoder stops at47b9a in next consumer. Content matches are not runtime or hardware compatibility.

Open question at the time. Resolve downstream physical meaning using a valid decoder or exact primary calibration definition; steering effort remains unmeasured.

## A094 Independent EPS flags and diagnostic provenance of calibration inputs

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `independent_eps_calibration`.

Traced original flag consumers and calibrated-input producers/serializers; checked20 instruction windows,8 settings and7 saved captures.

Result. Speed, corrected steering angle and handwheel torque input units established. STATUS_EPS enable bits are configuration readback. No proven comfort-gain flag; DriveDown capture cannot diagnose loaded derating.

Limits. Road-feedback57fc8 and crossjoint4c06c decoder gaps remain. No new RAM readback, loaded operation or steering-force comparison.

Open question at the time. What are the complete physical effects of unresolved terms under valid operating conditions?

## A095 Original OEM documentation explicitly supports older program datasets

Date: 2026-10-31. Historical status: `verified_static`. Workstream: `downgrade_feasibility`.

Verified nine retained help topics against original WinKFPT CHM,14 documentary claims,three catalogue sets and222 reconstructed-script conditions.

Result. Original help explicitly documents programming old program datasets. Auto-latest catalogue selection is distinct from generic manual programming. No blanket host chronological prohibition established; no target EPS acceptance demonstrated.

Limits. Historical Version2.0 help with1997-2012copyright is generic capability, not current OEM approval. Reconstructed script has known decompiler defects; installed boot and exact earlier-pair applicability remain unproved.

Open question at the time. What affirmative evidence establishes exact earlier application acceptance and normal-operation compatibility for capturedEPS hardware/reference?

## A096 Bounded public search for confirmed EPS reverse-flash outcomes

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `downgrade_feasibility`.

Ran 20 targeted EPS/Servotronic/version downgrade queries, read four new candidate pages, and added OEM applicability searches.

Result. No matched successful EPSPL2/E9x downgrade found. Closest first-person E90 source explicitly did not flash; Z4 report is a forward update; BMW i3 bulletin is a different-generation forward update.

Limits. Indexed-public-web search is not exhaustive and absence is not impossibility. No owner contacted or VIN submitted; old2022/2013 cases were not counted as new success.

Open question at the time. Seek a documented exact-controller reverse transition with before/after identity and normal post-flash behavior.

## A097 Current basis profiles traced into requested motor torque

Date: 2026-10-31. Historical status: `verified_bounded_synthetic`. Workstream: `current_profile_scope`.

Scanned direct selector consumers and original final torque provenance; executed actual array producer and torque consumer in112 cases for indices9..15 at0/15kmh.

Result. 14/15 increase the tested standstill contribution;13 is lower at ordinary small inputs. New18190 and184c8 changes prevent assuming E84 suitability.

Limits. Explicit function entries with zero extra terms; no whole scheduler, final combination execution or car behavior.

Open question at the time. Resolve18190 role and exact-rack applicability before a profile trial.

## A098 Operational effect of conditional reference mismatch and host predicate correction

Date: 2026-10-31. Historical status: `verified_bounded_synthetic`. Workstream: `downgrade_compatibility`.

Extended strict original checker/caller execution for matching and retainedIC references; freshly parsed original host IPO and evaluated16 predicate cases.

Result. Mismatch returns a positive status read with payload12 and no inhibit writes in examined suffix. Final host error handler is called for12 plus zeroBSUTIME.

Limits. Prerequisites supplied; direct-reference coverage is not whole-program. Error-handler termination and ordinary operation unproved. Corrects reconstructedIPS grouping and any unconditional final12-acceptance implication.

Open question at the time. What affirmative evidence establishes normal operation and exact app/boot/hardware coherence?

## A099 Exact downgrade regression and improvement assessment

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `firmware_regressions`.

Compared original release headers and prior bounded deltas;16 new focused live queries and dated OEM training/bulletin assessment.

Result. No exact6794011-to6855892 changelog or named lost fix found. Diagnostic/task changes and conditional abnormal status are concrete concerns;2009 documentation already describes major assistance/protection functions.

Limits. Search is bounded; no exact software-equivalence, safety, acceptance or physical behavior proof.

Open question at the time. Obtain exact supplier release/applicability evidence rather than attribute unrelated model fixes.

## A100 Exact floating-point dialect specification search for unresolved profile scalar

Date: 2026-10-31. Historical status: `inconclusive`. Workstream: `decoder_limit`.

Retrieved official PHO3 hardware manual and located primary operating-precautions reference to U16374EJ1V0UM00 FPU architecture manual.

Result. Required instruction semantics not obtained; scalar18190 remains unresolved. No decoder error skipped or assigned invented semantics.

Limits. Official manual does not prove installed CPU; float interpretation of data does not identify physical units.

Open question at the time. Obtain exact FPU architecture specification or trustworthy supplier calibration definition.

## A101 Fresh EPS coding read and write readiness

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

With fresh parked and ignition confirmation, read EPS identification and coding block 3000 using a narrowed copy of the prior guarded reader; inspected local write-tool documentation.

Result. IDENT returned 6855892 and C03; C_C_LESEN returned 25 bytes identical to the previous backup, variant 09 e92_basis, zero XOR. The USB diagnostic interface and read path worked. Local NCSX describes SG_CODIEREN and EPS PRG exposes C_C_SCHREIBEN, but an end-to-end EPS write and recovery path are not demonstrated.

Limits. No coding write, recovery trial, confirmed E84 rack applicability or physical steering test. Local write tooling presence is not demonstrated readiness.

Open question at the time. Establish exact EPS write path, input and recovery behavior offline, and supported E84 calibration applicability.

## A102 Primary E1F decoder source resolves torque-domain profile scalar path

Date: 2026-11-01. Historical status: `verified_static`. Workstream: `current_profile_scope`.

Retrieved pinned official HexRays E1F decoder source; ported bounded encodings and decoded101-instruction scalar function plus caller with no skipped unknowns.

Result. 18190 value participates in positive/negative comparisons and arithmetic on handwheel-plus-crossjoint torque scaled1/68; stateful output returns into2f72, an extra torque-consumer term. No direct hardware-ratio meaning established.

Limits. No floating execution, full flag/rounding model, whole controller, exact-rack applicability or vehicle write. Prior zero-extra-term results do not predict full changed profile.

Open question at the time. What is the dynamic effect of the torque-domain threshold/state term under correct E1F semantics, and what establishes exact-rack applicability?

## A103 Trace and simulate E90 basis coding write path

Date: 2026-11-01. Historical status: `verified_synthetic`. Workstream: `coding`.

Mapped E89 SGFAM EPS to A_E65 and EPS_90, decompiled original IPO and ran original C_C_AUFTRAG against SimulationInterface with E90 basis and adjusted XOR, stopping at first attempted send.

Result. SG_CODIEREN dispatches C_C_AUFTRAG; simulated interpreter generated service 2E coding request. Local NCSX implements IPO-based coding with optional reread. No vehicle write occurred.

Limits. First outgoing request only; full IPO, real ECU acceptance, recovery, rack compatibility and physical steering behavior not verified.

Open question at the time. Establish exact full EPS IPO and recovery behavior before applying any road-critical coding.

## A104 Conditional float32 dynamics of newly decoded torque correction

Date: 2026-11-01. Historical status: `verified_synthetic`. Workstream: `current_profile_scope`.

Read original constants and inferred bounded recurrence from decoded scalar function; ran192 cases of1000ticks from zero state for9/13/14/15,0/15kmh and both enables.

Result. Modeled extra term stays zero for absolute input up to3Nm from zero state; previous small-input standstill contribution lead survives this conditional context.14 raises and15 lowers the inferred torque threshold. Inferred output cap reaches zero at10kmh.

Limits. Arithmetic recurrence with conventional SUBF/TRFF assumptions, not original-instruction execution. Carryover state, full feedback, exact-rack applicability and road behavior unproved. No car operation.

Open question at the time. Independently validate early-FPU execution semantics and whole-controller dynamic effects before claiming an applicable profile trial.

## A105 EPS C_CI_LESEN live and original IPO replay

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

With fresh user confirmation, read EPS identification and C_CI_LESEN with a restricted diagnostic allowlist; simulated original A_E65 dispatcher with integer result 3.

Result. Both jobs return index 3. C_CI_LESEN gets NRC12 for 1A9B, falls back to 1A80 and returns 3. IPO simulation publishes 03.

Limits. The earlier browser C64 run was not captured; cause remains unproved. No vehicle write or restoration performed.

Open question at the time. Reproduce the NCSX read with logged response and verify any fix on the same surface.

## A106 Owner-triggered NCSX E84 basis write with immediate ECU readback

Date: 2026-11-01. Historical status: `vehicle_write_partial_completion`. Workstream: `coding`.

Inspected browser log after owner clicked Apply; original checksum and C_C_AUFTRAG executed on actual EPS.

Result. Coding write and immediate readback confirm variant 0E/checksum 0A. Subsequent C_AEI_AUFTRAG failed ERROR_NUMBER_ARGUMENT; later IDENT timed out. Owner reported temporary steering warning then disappearance.

Limits. Full SG_CODIEREN completion, subsequent independent read, stored faults, physical benefit and rack suitability remain unverified. No free Servotronic activation demonstrated.

Open question at the time. Confirm current coding with read-only operation and explain metadata-argument failure separately.

## A107 Read-only postcoding EPS health snapshot

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

Released browser serial port, read original IDENT, STATUS_EPS, C_C_LESEN and FS_LESEN through request allowlist, disconnected.

Result. All jobs OKAY; zero stored faults; variant E84 ohne SA216, coding0E/checksum0A; supply okay and no output-driver fault. System status DriveDown.

Limits. Stationary diagnostic snapshot, no road suitability or measured improvement proof; no reset or fault clearing.

Open question at the time. Physical comparative behavior and separately incomplete AEI metadata step.

## A108 All22 profile contribution comparison and FA badge interpretation

Date: 2026-11-01. Historical status: `verified_bounded_synthetic`. Workstream: `current_profile_scope`.

Extended existing original-function harness to22 profile indices, verified prior112 cases, built comparison with direct and known-remap views.

Result. 352 bounded cases completed; all prior112 matched. E84 variants14/15 tie at tested standstill inputs, differ at15kmh. E89 raw curves must not be confused with known missing-licence selection remap. FA badge tests configuration predicates, not licence.

Limits. One torque contribution, not whole controller or measured effort; all22 were not coded on car. Remap conditional on examined selector path.

Open question at the time. Physical comparative behavior and suitability, not larger isolated curve alone.

## A109 Live E92 coding00 selects reported E92 basis09

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

Inspected owner-triggered write log, then read only IDENT/status/coding/fault memory with fresh stationary ignition confirmation.

Result. Stored coding00/checksum04 accepted; actual status reports active09 E92 ohne SA216; zero faults, supply okay and no output-driver fault.

Limits. Stationary DriveDown snapshot, not road validation, measured steering benefit or exhaustive licensing check. Owner initiated write, subsequent inspection was read-only.

Open question at the time. No new activation claim; resolve existing NCSX metadata error separately.

## A110 Current stored E84 basis but active E92 basis in DiagMode

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

Read only current IDENT/status/coding/faults after owner-reported incomplete IPO write.

Result. Stored0E/checksum0A; active09 E92 ohne SA216, DiagMode; zero faults, supply okay, no output-driver fault. All jobs OKAY, reader disconnected.

Limits. Active14 not demonstrated in this diagnostic-mode snapshot; no restart/reset/write/clear during the read-only inspection.

Open question at the time. Observe active profile after owner-controlled diagnostic exit/restart, if requested.

## A111 E84 basis retained and active after ignition cycle

Date: 2026-11-01. Historical status: `vehicle_read_verified`. Workstream: `coding`.

After owner-reported ignition cycle read IDENT, STATUS_EPS, C_C_LESEN and FS_LESEN through existing strict read allowlist.

Result. Stored0E/checksum0A; active0E E84 ohne SA216; DriveDown; zero faults; supply okay and no output-driver fault. All jobs OKAY, reader disconnected.

Limits. Stationary snapshot after owner-reported ignition cycle; no measured steering benefit, road suitability or licensed activation claim.

Open question at the time. Physical behavior remains unmeasured; NCSX AEI metadata failure is separate unresolved work.

## A112 Reddit IBAC claim checked against BMW procedure and current selector evidence

Date: 2026-11-01. Historical status: `inconclusive`. Workstream: `licence`.

Read user thread and reply permalinks, same-author older IBAC claim, BMW-authored ISTA/P manual and period-specific catalogue; reviewed existing selector/skip evidence.

Result. One consistent2009 IBAC activation claimant, no exact EPS identity or2012 success proof. BMW manual treats IBAC permission and required SWT enabling code separately. Known selector bypass conditions remain unverified operationally. Corrected prior E89 visual mapping to15 after original clamp.

Limits. Public visible comments only; no ISTA/P retrofit rule data or final report, matched new entitlement, vehicle experiment, modified image or accepted patch. E89 correction supersedes A108 visualization remap, not original raw outputs.

Open question at the time. Obtain exact EPS/ISTA-P retrofit-rule or final-report evidence for claimed IBAC route before more car changes.

## A113 E84 and E92 KD91 EPS replacement hardware comparison

Date: 2026-11-01. Historical status: `verified_bounded_static`. Workstream: `current_profile_scope`.

Compared public BMW replacement-parts applicability for the target E92 and E84 model variants.

Result. Catalogue fit intersection32106793457 for KD91/VL31 supports physical hardware relationship, not exact fitted rack or calibration suitability.6851800 is ECU identity, not complete assembly number.

Limits. Exact production month, LHD/option-filtered fit, installed rack/motor/ratio and E84basis applicability unverified; no vehicle action.

Open question at the time. Physical rack label or exact filtered part applicability, without expanding into repeated software matches.

## A114 Current-EPS free activation continuation through ISTA-P conversion0047

Date: 2026-11-01. Historical status: `inconclusive`. Workstream: `licence`.

Read newly available indexed2015 loader/IBAC discussion and live2012 plan reports; checked existing firmware signature and metadata conclusions without rerunning closed experiments.

Result. Specific conversion0047 and loader manual lead recovered, but direct page403 and solutionpost14 unread; no exact6855892 plan, newFSC or patch proof. Production year alone insufficient; new free activation remains unproved.

Limits. Indexed visible portions and one live forum page; no original ISTA/P retrofit package/final report, accepted new credential, firmware change or vehicle action.

Open question at the time. Exact ISTA/P EPS retrofit-rule/final-report evidence showing internal0084 provisioning versus mere VO/coding.
