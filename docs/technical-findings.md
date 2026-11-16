# Technical findings and their limits

These findings summarize the original investigation. Attempt IDs refer to [the historical ledger](attempts.md). The public repository does not include the proprietary reference images or private diagnostic captures needed to rerun every experiment.

## Baseline identity

| Field | Saved observation |
| --- | --- |
| Working vehicle | 2012 E92 LCI 318i, N43, KD91 |
| Application | 6855892 |
| Coding index | 03 |
| Program reference | 0512IC0F780A |
| Reported ECU hardware | 6851800 |
| Hardware reference | 0512IC0 |
| Original profile | E92_basis, index 09 |
| Target entitlement | App0084, upgrade 0001 |
| Target FSC and certificate | Both absent in saved SWT response |
| Software signature | Accepted in that response |
| Coding block | 25 bytes, XOR checksum zero |
| Named MAX setting | Captured bytes 2..3 already 0080 |

The ECU hardware number is not the complete steering-rack assembly number. The working model identity was not a fresh factory-option lookup. See A002, A005, A027-A028, A076, and A113.

## Coding selects a profile; an FSC authorizes a feature

The analyzed current selector queries domain 30 and combined App00840001. Under bounded tested conditions, a nonzero authorization result changes coded E92 index 0 into E92 basis index 9. Some profiles remain unchanged. The original-instruction tests used explicit synthetic state and demonstrated local program behavior, not complete controller execution. See A012-A013 and A092.

A real later read found stored E92 00 while active status reported E92 basis 09. This is vehicle evidence consistent with the remap. The final E84 read found stored and active 0E. See A109-A111.

In the recorded GUI investigation, the EPS parameter was `VARIANTENCODIERUNG_3` in `EPS_PL2.C03`. This name is definition-specific. A similarly named E84 body setting in an audio module is unrelated.

The C03 schema includes 22 named profiles. E90 basis is decimal 13, E84 basis is decimal 14, and the other examined E84 variant is decimal 15. Decimal 14 is hexadecimal 0E. Do not confuse a schema label, a stored index, an active index, and an entitlement verdict.

## Why E84 became the practical candidate

The investigation traced profile-dependent curves into a contribution added to requested motor torque. At 1 Nm main handwheel input with other composite terms zero, the tested contribution was 125 raw counts for profile 9, 82 for profile 13, and 182 for profiles 14/15. At 2 Nm the corresponding values were 295, 184, and 448. See A097.

Those are intermediate controller outputs. They are not motor torque measurements, driver-effort percentages, or a prediction of complete steering behavior. Other profile data and stateful contributions change too. E90 and E92 curves cross, and no examined profile was uniformly larger across every condition.

The scalar at 18190 participates in a torque-domain stateful term. Decoder evidence tied its input to handwheel plus crossjoint torque scaled by 1/68. It was not identified as a direct mechanical rack ratio. A float32 recurrence model stayed at zero from zero state for absolute inputs up to 3 Nm in the modeled cases. That model has instruction-semantics and execution-context assumptions. It is not original-instruction execution. See A102 and A104.

## What the live trial proves

The owner-triggered coding write and immediate readback were positive. A later metadata job failed. Subsequent independent coding reads confirmed the change. After the ignition cycle, status reported active E84 without SA216, zero stored faults, and DriveDown. See A106-A111 and [the selected evidence reports](evidence.md).

No diagnostic observation here establishes loaded assistance health, rack suitability, thermal performance, return behavior, or highway stability. The owner's later driving report is separate evidence about perceived behavior on this car.

## Why older firmware was not the solution used

Several earlier selectors omitted the later entitlement remap. That made older software interesting, but it did not prove it could be installed safely or operate correctly with the actual hardware and loader. Hardware-reference mismatches produced a non-normal programming status in bounded code tests, and the original host workflow handled that status conditionally. No complete compatible reverse-flash demonstration was obtained. See A022-A024, A041-A046, A071-A084, and A095-A099.

Generic OEM documentation described older-program capability. It did not establish acceptance by this EPS. A shared public key or similar initialization helper did not prove whole-image compatibility. No downgrade or boot modification is documented as the successful practical outcome.

## Why the credential routes remained unsuccessful

The investigation did not find a tested public generator for a new E92 EPS App0084/0001 FSC. Navigation FSC tools target different applications. IBAC authorizes a retrofit workflow and does not by itself prove creation or acceptance of the separate EPS credential. Repairing an existing entitlement is a different problem.

Inspected validation paths checked padding, digest information, and signed identity/application fields. Altering the analyzed program changed the signed digest. Shared-divisor checks did not reveal a usable key relationship. These bounded findings rejected particular shortcuts; they did not prove every possible activation path impossible. See A014-A021, A048-A060, A087-A088, A112, and A114.
