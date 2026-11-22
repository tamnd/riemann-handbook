---
id: volume-theorem-of-inputs
title: The volume theorem from ten inputs (statement form)
kind: theorem
decl: GlobalTheory.T.volume_theorem_of_inputs
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.VolumeTheoremOfInputsStatement
covers: 8967
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`volumeTheoremX_of_inputs`](/entry/volume-theorem-x-of-inputs/), which has the real content, and its proof applies that theorem. Its one user is [the good tower and the volume theorem](/entry/good-tower-and-volume/), which builds seven of the ten inputs and passes them in. The written proof counts its 8,967 declarations as the largest part of Step 4 of [the Weil bound](/proof/weil-bound/).

## Statement

**Theorem.** Assume the following ten statements: `Top.Given`; `PtsIntegrableStatement`; `Out.WeilSt`; the existence of constants $C_h, C_u$ with `NineGeoU` $C_h$ $C_u$; `HodgeLatticeFlagBound`; `TrivFlagOnHodge`; `Fl.FlatDegree`; `TwistAut`; `Cmp.CmpPair`; `Cmp.CmpSt`. Then `VolumeTheoremX` holds: there is $C \geq 0$ such that each good root tower over an abelian CM field, with $q \geq 1$, $3q + 1 \leq p + q$ and few bad primes, is proportional, has equal volumes on its components, and satisfies the limit formula `T1`, the asymptotic `ThmB` and the lower bounds `T2` and `MeanSlope` with the constant $C$.

The [entry of the real theorem](/entry/volume-theorem-x-of-inputs/) defines the root towers and the six conclusions.

## Proof

The statement is that of `GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs`, and the proof applies it.

## In the Lean code

The theorem is in [VolumeTheoremOfInputsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/VolumeTheoremOfInputsStatement.lean#L23). The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs | ...`, as in the other statement files of this chapter. The hypotheses are in the same order as in the real theorem.
