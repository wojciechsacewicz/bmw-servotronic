# Assess whether this experiment applies to another car

This is a guide for planning and evaluating replication with an agent or qualified specialist. It is not a universal procedure for changing EPS coding. Exact applicability and recovery were not established for other racks.

## 1. Choose the outcome you want

If the goal is a newly licensed Servotronic feature, this repository has no demonstrated free method. If the goal is to investigate the different steering feel reported after E84 basis coding, continue with that distinction explicit.

## 2. Identify the actual controller and rack

Compare the read-only ECU identification against application 6855892, coding index 03, hardware 6851800, and program reference 0512IC0F780A. Save the original coding and active variant. Determine whether the target entitlement exists. Use your own tools' documented read jobs and preserve their output locally.

Identify the physical rack and relevant equipment independently. A shared replacement catalogue listing does not prove that the installed assemblies or calibrations match. A different application, coding index, physical rack, or unknown original state is a reason to stop copying this experiment and investigate the difference.

The public repository excludes the original VIN and full coding block intentionally. The author's exact packet is not a template for another car.

## 3. Establish the tool and restoration plan before a write

The original trial used NCSX and an EDIABAS-compatible diagnostic path. That records what happened, not a claim that every NCSX release or adapter is ready for this job. Tool versions, coding definitions, byte layout, checksum handling, and controller support must be checked for the new setup.

The plan needs a verified original coding backup, a documented method to restore it, suitable power/connection conditions under the tool's guidance, and qualified help if a steering warning or communication failure cannot be resolved. Do not discover the restoration method after changing the controller.

Do not treat programming mode, resets, or fault clearing as neutral read operations. None is a prerequisite established by this public guide.

## 4. Review the proposed change with the owner

The recorded EPS parameter was `VARIANTENCODIERUNG_3` in `EPS_PL2.C03`. Verify that the tool is showing the EPS module and its actual coding index. A historical GUI session initially showed `AMP_TOP.C03`, an audio module, whose `BAUREIHE` setting was unrelated. Do not select that setting.

The recorded target was the named E84_basis profile, decimal 14 or hexadecimal 0E, in the current C03 definition. The original was E92_basis 09. That information is a comparison reference, not authorization to replace byte 1 in any EPS dataset.

An agent should show the owner a specific plan based on their own evidence, describe the unresolved calibration suitability, and obtain explicit authorization for the exact operation. If applicability or recovery remains unresolved, the assessment stops before the write.

## 5. Distinguish acceptance, retention, and behavior

The original evidence sequence was an accepted write, independent coding readback, then an active-profile read after the owner reported an ignition cycle. A106 through A111 document the complications, including a metadata-job error and a temporary warning.

A new experiment needs its own observations. Preserve the original and resulting coding, active status, warnings, faults, and communication errors. Do not clear evidence to make a clean screenshot. Stop on unexpected faults, persistent warnings, inconsistent readback, or lost communication.

## 6. Evaluate suitability separately

The author's easier-parking report does not certify another car. No controlled engineering validation or whole-vehicle model is supplied here. Deciding whether a changed steering calibration is suitable requires vehicle-specific expertise and appropriate controlled assessment. The repository cannot supply that decision from identifiers alone.

## What an honest replication report looks like

State exactly which stage was reached. An offline assessment, accepted coding write, retained active profile, subjective driving report, and controlled comparison are different results. Cite the relevant attempt IDs and say what remains unknown. See [the agent assessment template](agent-guide.md).
