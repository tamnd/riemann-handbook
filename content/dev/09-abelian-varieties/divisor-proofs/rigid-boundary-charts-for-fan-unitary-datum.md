---
id: rigid-boundary-charts-for-fan-unitary-datum
title: Rigid boundary charts for a fan (citation)
kind: theorem
decl: GlobalTheory.T.rigidBoundaryChartsForFan_unitaryDatum
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.RigidBoundaryChartsForFanUnitaryDatumStatement
covers: 2770
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/). It proves the statement `RigidForFan`, and [the toroidal compactification with the log Kodaira-Spencer isomorphism](/entry/toroidal-for-fan-ks/) uses it as one of its two inputs. It has no content of its own. Below it are 2,770 declarations of the proof.

## Statement

`RigidForFan` holds. In words: for each CM field $E$, host $H$, Hermitian datum of signature $(p, q)$ with $p + q \geq 1$, invariant function $\varphi$ with `IsPolFan` and `NoSelfInt`, level and coefficient field $F$, the moduli scheme has a smooth projective model over $F$ with a normal crossings boundary, a Cartier divisor $B$ on the boundary with charts of the form that $\varphi$ gives, an ample line bundle $\omega^k(-B)$, and a rigid chart at each closed boundary point. The entry [rigid boundary charts for a fan](/entry/rigid-for-fan-holds/) states it in full.

## Proof

The proof is the tactic

```
first | exact @GlobalTheory.RigChart.rigidForFan_holds | exact GlobalTheory.RigChart.rigidForFan_holds | (intros; apply GlobalTheory.RigChart.rigidForFan_holds <;> assumption)
```

The first branch succeeds: the statement of `rigidForFan_holds` is the same proposition. So this theorem is `rigidForFan_holds` under another name.

## In the Lean code

The theorem is in [RigidBoundaryChartsForFanUnitaryDatumStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanUnitaryDatumStatement.lean#L16). It calls only `GlobalTheory.RigChart.rigidForFan_holds`, in [RigidBoundaryChartsForFanUnitaryDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanUnitaryDatum.lean#L19). The file opens many namespaces and sets `maxHeartbeats` to 1,000,000; neither is needed for a one-step citation. The suffix `unitaryDatum` in the name does not match any hypothesis: the statement has none.
