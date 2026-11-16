# Open questions and worthwhile next evidence

These questions are unresolved. Listing a path does not mean it is feasible or authorize a vehicle operation.

## Establish exact rack applicability

The controller reports hardware 6851800, and a shared replacement listing connects KD91 and VL31 model variants. The fitted rack assembly, motor revision, and calibration applicability remain unverified. Physical labels, precise production/equipment context, and primary applicability documentation would distinguish a true match from a broad catalogue overlap. Start here before treating E84 coding as transferable. See A076 and A113.

## Measure the practical effect on this car

The owner reports much easier parking with good highway feel. There is no controlled baseline comparison of steering effort, no continuous loaded diagnostic trace, and no systematic evaluation of temperature, return behavior, or fault recurrence. Evidence could include a professionally planned comparison under appropriate controlled conditions. Intermediate firmware calculations cannot fill this gap. See A097-A104 and the later owner report.

## Understand the complete profile differences

Only selected consumers and synthetic contexts were exercised. Stateful interactions, the 184c8 multiplier, protection behavior, and whole-controller dynamics remain incompletely understood. A complete profile-difference analysis would need valid instruction semantics, explicit scheduling/state assumptions, and a test capable of distinguishing competing explanations. Do not repeat the already completed selector matrix as a substitute. See A092-A104.

## Resolve the coding-tool metadata failure

C_AEI_AUFTRAG failed after an accepted coding write. Subsequent independent reads confirmed the coding, but the failed metadata stage was not fixed or demonstrated to complete. Further work should inspect that host job's signature and required arguments offline, then establish its actual significance. Do not repeat a vehicle write to diagnose a host argument mismatch. See A103, A105-A106.

## Check a legitimate new-entitlement workflow

The exact ISTA-P conversion 0047 plan for application 6855892 was not obtained. It remains unclear from the public evidence whether specific claimed procedures create an entitlement, recover an existing one, or merely change vehicle order and coding. Exact before/after FSC status and primary workflow artifacts would matter. Generic IBAC discussion or a model-year match would not. See A088, A112, and A114.

## Complete historical evidence without overclaiming

Parts of forum discussions were inaccessible, and one-page triage did not read every post in every thread. The local session search is documented in [evidence](evidence.md). Missing or private material remains a coverage gap. It is not evidence that a method works, nor proof that no method exists.

## Keep lower-priority paths in context

Earlier-program compatibility and installed-memory access were unresolved, but neither is needed to explain the recorded E84 coding result. Pursue them only for a specific new question that justifies the added complexity and has a credible non-destructive validation path. See A029-A040 and A071-A099.
