---
id: integrality-from-metric-of-160-le
title: The local colength bound from its inputs, restated
kind: theorem
decl: GlobalTheory.T.integralityFromMetric_of_160_le
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingOfEtaleExactDeRhamCrystallineConstStatement
covers: 1157
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the colength bound from three local facts](/entry/integrality-from-metric-of-le/). Its only user is [the closing of the local bound](/entry/theorem-a-closing/), which applies it with the constants $C_A = 23$, $C_B = 32$, $C_K = 32$. The content is below it, in [the integrality bound for large constants](/entry/integrality-from-metric-of-large-constant/).

## Statement

**Theorem.** For each datum $D$, all local data $HW$, $F$, $Cm$ over it, all reals $C_A, C_B, C_K$ and each real $C \ge 160$: if the thirteen local inputs `Adm1 D HW F Cm CA CB CK` hold, then the local colength bound `Conclusion1 D C` holds.

Both sides are stated in [the closing of the local bound](/entry/theorem-a-closing/). In the code the implication is the definition `IntegralityFromMetric D HW F Cm CA CB CK C`.

## Proof

The proof is the term `GlobalTheory.TheoremAFinal.integralityFromMetric_of_le`. There is nothing else.

## In the Lean code

The theorem is at [LocalLiftingOfEtaleExactDeRhamCrystallineConstStatement.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingOfEtaleExactDeRhamCrystallineConstStatement.lean#L11). Its type is the type of `integralityFromMetric_of_le`, word for word.

- The name `IntegralityFromMetric` does not describe the statement. No metric occurs in it; it is "the local inputs imply the colength bound".
- The constants $C_A, C_B, C_K$ occur only in one conjunct of `Adm1`. The bound in the conclusion does not depend on them.
- The module name speaks of an étale functor, de Rham and crystalline. These words describe the three facts that the proof one level down supplies, not this statement.
