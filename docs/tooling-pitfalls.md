# Tooling mistakes worth avoiding

These observations come from the historical sessions. They are not a certification of any current tool release.

## Confirm the module before interpreting an E84 label

One GUI screen was displaying `AMP_TOP.C03`, an audio module. Its `BAUREIHE` value was unrelated to steering. The recorded EPS setting was `VARIANTENCODIERUNG_3` in `EPS_PL2.C03`. A label shared by two modules does not mean they control the same feature.

## Do not trust a displayed coding index without the underlying result

An offline NCSX investigation found a conversion defect where an integer coding index became decimal text and was then parsed as hexadecimal. That can corrupt some displayed indices. It did not by itself explain the reported `C03` to `C64` anomaly. The exact origin of that anomaly remained unresolved in the retained note.

A105 separately established that the actual EPS jobs returned coding index 3. `C_CI_LESEN` received NRC12 for one request, used its fallback identification request, and returned 3. That fallback was not a failed controller identification. Use the actual job output and definition match before selecting a schema.

The public repository does not include the tool source or claim that the issue persists today. Diagnose the reader's actual version rather than applying a historical patch blindly.

## A partial coding job is still a partial job

A106 records a positive `C_C_AUFTRAG` write and confirmed independent readback, followed by `C_AEI_AUFTRAG` failing with `ERROR_NUMBER_ARGUMENT`. Neither a blanket success claim nor a blanket claim that nothing changed fits the evidence. Preserve the exact phase that failed and confirm ECU state independently.

## A coding backup is not a full recovery image

The saved original coding block was useful evidence and a potential input to restoring coding. It was not a full installed-memory dump or proof that a failed programming session could be recovered. The normal FLASH-read attempt returned zero bytes with securityAccessDenied. See A030.

## Do offline work away from the car

Decoder research, source comparisons, tool argument inspection, and catalogue analysis do not require a connected vehicle. Historical ignition/readiness statements expired with those sessions. Re-establish the owner, tool, vehicle, and authorized operation for each new live session.
