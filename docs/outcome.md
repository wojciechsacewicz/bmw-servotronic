# The result on this car

The initial goal was to create a new, free Servotronic entitlement on an E92 whose EPS did not have the required FSC. That goal failed. No accepted new App0084/0001 credential was demonstrated.

The practical goal was easier low-speed steering. Investigation of the existing application found alternative basis profiles, including an E84 setting that could remain selected without the E92 Servotronic entitlement remap. This led to a real coding trial.

## What the saved vehicle record establishes

On 1 November 2026, the owner applied E84_basis through NCSX. The checksum job and coding-write job returned positive results. An immediate readback and a later independent coding read showed variant `0E` and checksum `0A`. The following metadata job, `C_AEI_AUFTRAG`, failed with `ERROR_NUMBER_ARGUMENT`, and identification reads initially timed out. The whole coding procedure therefore cannot be described as having completed successfully in every step. See A106.

The owner reported a temporary steering warning and then its disappearance. Subsequent read-only checks reported zero stored EPS faults, supply okay, and no output-driver fault. These observations document the state seen by diagnostics, not a full operational safety assessment.

An intervening E92 trial wrote index `00`, but the controller reported active index `09`, E92 without SA216. After E84 was selected again, an initial diagnostic-mode observation still reported active E92. Following the owner's ignition cycle, the final saved readback at 13:47:03 UTC showed both stored and active E84 index `0E`. Its reported system state was `DriveDown`. See A109 through A111.

The after-ignition result supports retention and selection. It does not provide a loaded driving trace or prove behavior across speeds and temperatures.

## What the owner reports after driving

On 16 November 2026, the owner reported daily use for roughly a week or two, possibly longer. Parking was much easier, and highway handling still felt very good. The owner described the change as a game changer.

This is a retrospective subjective report. The exact start date, mileage, driving conditions, and measured steering effort were not supplied. The saved successful selection is dated 1 November, but the duration of daily use should not be inferred from that alone.

## Why the wording matters

The contemporaneous records document a coding change selecting a profile in application 6855892. They do not establish a firmware flash.

The label `E84 ohne SA216` means E84 without the Servotronic option. A useful change in feel does not establish the original licensed feature was unlocked. The two outcomes deserve separate records.
