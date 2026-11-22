---
id: ks-hodge-of-inputs
title: Hecke eigensystems occur in Dolbeault cohomology, given four inputs
kind: theorem
decl: UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_inputs
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.LefschetzSigmaSums.HodgeTraceOfLefschetzAndGroupSide
covers: 386
status: drafted
drafted_by: writer@claude
---
This theorem proves `KSHodge` from four hypotheses: the holomorphic Lefschetz formula $\mathrm{HLF}$, the fixed-point count `FixK`, and two group-side identities. [ksHodge_of_geo](/entry/ks-hodge-of-geo/) supplies the two identities and keeps the first two as its own hypotheses. The proof is a pass-through: it adds one proved fact and takes the third part of [hodgeTrace_of_lefschetz_and_groupSide](/entry/hodge-trace-of-lefschetz-and-group-side/), where the real work is.

## Statement

**Theorem.** Assume

- $\mathrm{HLF}$, the holomorphic Lefschetz formula of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/);
- `FixK`, the fixed-point count on towers of fibre powers ([FixK_holds](/entry/fix-k-holds/));
- `MarkWeightedFixedPointEqDefinitePairOdd`, the weighted count as a sum over definite pairs ([its entry](/entry/weighted-count-definite-unitary/));
- `TraceDefinitePairsEqAutomorphicTrace`, the sum over definite pairs as an automorphic trace ([its entry](/entry/cnt-trace-definite-forms-identity/)).

Then `KSHodge` holds: for each dominant weight $\lambda$ there is $k$ such that each Hecke eigensystem of weight $\lambda$ occurs in the Dolbeault cohomology of the towers `KS L gb k`, in the degrees that `IsHExp` gives. The full statement is in [ksHodge_of_geo](/entry/ks-hodge-of-geo/).

## Proof

The proof is

```
(hodgeTrace_of_lefschetz_and_groupSide hW KSProj_holds hF h₁ h₂).2.2
```

The added fact is `KSProj_holds`: each level of a tower `KS L gb k` over $\mathbb{C}$ is projective and smooth of some relative dimension. It is `kSProj_of` applied to `sPow_smooth` and `isProjOver_sPow`, facts about fibre powers that we have not unfolded. Of the three conclusions `HodgeTr`, `HodgeEig` and `KSHodge`, the proof keeps only the last.

## In the Lean code

The theorem is in [HodgeTraceOfLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceOfLefschetzAndGroupSide.lean#L53), with `KSProj_holds` at line 42. `KSProj` is in [HodgeTraceFromLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceFromLefschetzAndGroupSide.lean#L121).

This theorem and [ksHodge_of_geo](/entry/ks-hodge-of-geo/) are two pass-through layers over the same proof. The hypotheses $\mathrm{HLF}$ and `FixK` are passed along unchanged.
