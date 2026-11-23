---
id: sum-frame-class-weights-le-datum-bound
title: The weights of the frame classes in one datum, statement form
kind: theorem
decl: GlobalTheory.T.sum_frameClassWeights_le_datumBound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.SumFrameClassWeightsLeDatumBoundStatement
covers: 454
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/). Its only user is [`sum_classes_le`](/entry/sum-classes-le/), which is itself a second name for it. The content is in [`sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/).

## Statement

**Theorem.** Let $A$ be a nonempty finite set of relevant terms with one row lattice $\Lambda$, one rank $j$, one label $\delta$, one index $x$ and one lattice datum $d$, each with a chosen normal form that is adapted and is a term for $\Lambda$. Then the sum of the class weights over the frame classes of $A$ is at most $\mathrm{datBd}(k, r, \Delta_{j,\delta}, D_{b;j,\delta}, N_T, x)$.

The full statement, with all hypotheses, is in [the entry for `sum_clsOm_le_datBd`](/entry/sum-cls-om-le-dat-bd/).

## Proof

The proof is the term `GlobalTheory.TypeAsm.PerRow.sum_clsOm_le_datBd`. There is nothing else.

## In the Lean code

The theorem is at [SumFrameClassWeightsLeDatumBoundStatement.lean line 23](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/SumFrameClassWeightsLeDatumBoundStatement.lean#L23). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative already fits. The file imports `Mathlib` twice.
