# How the investigation progressed

The main retained attempt ledger covers 30 October through 1 November 2026. The sequence below follows its stable IDs, rather than assigning missing timestamps to individual experiments.

## Establish the right target

Early work separated mixed vehicle backups from EPS evidence. A date change, a generic BMW FSC generator, and maximum-assistance coding looked promising until their actual scope was checked. The captured MAX value was already set. A repair method for a previously issued entitlement would not meet the goal of creating a new entitlement. See A001-A008.

## Trace the entitlement gate

Reference firmware analysis found the current selector querying App0084/0001 and remapping unlicensed E92 index 00 to basis index 09 under the tested conditions. Bounded original-instruction execution reproduced that behavior. FSC and program-signature analysis undermined proposed shortcut routes. None produced a working new licence. See A009-A025.

## Get real EPS observations

Read-only vehicle diagnostics established application 6855892/C03 and missing FSC and FSC certificate. A normal-session memory read was denied with 7F2333, yielding zero program bytes. Further memory-access and programming hypotheses remained limited by prerequisites and recovery concerns. See A026-A040.

## Compare older software without flashing it

Older originals sometimes omitted the current selector remap, but compatibility did not follow. Hardware-reference checks, boot/application relationships, initialization differences, and missing matched downgrade reports left the downgrade route unresolved. The reference images remained reference material. See A041-A086, A095-A100.

## Look for a useful existing calibration

Broader forum work led to the current software's basis profiles. E90 basis was a real alternative, but the examined contributions did not support a blanket lighter-steering claim. E84 profiles produced larger tested standstill contributions while also changing other controller parameters. Decoder work and conditional modeling narrowed some gaps without simulating the whole car. See A088-A104.

## Try E84 basis and check retention

Fresh reads and tool simulation preceded the owner-triggered coding change. The write was accepted, but a later metadata job failed. Independent reads, an E92 remap check, and an ignition-cycle read eventually established stored and active E84 basis. See A101-A111.

## Keep the unresolved routes separate

IBAC/ISTA-P conversion leads and parts-catalogue overlap added context but did not prove a free new EPS entitlement or exact rack compatibility. See A112-A114.

## Add the actual driving experience

On 16 November, the owner reported easier parking and good highway handling after daily use. This updates the practical outcome while leaving the failed entitlement goal and engineering uncertainties explicit.
