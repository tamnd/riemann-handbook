---
id: unitary-three-automorphy-dense-of-prints
title: Three-dimensional seeds from the printed hypotheses
kind: theorem
decl: UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.UnitaryThreeInputsOfLiterature
covers: 4238
status: drafted
drafted_by: writer@claude
---
This theorem proves `UnitaryThreeAutomorphyDense` from the printed hypotheses `HypothesesH'` alone. This statement gives the three-dimensional seeds for the count $\mathrm{CountV}$ of the [window bound](/proof/vwin/). The theorem is a pass-through. The content is in [`unitary_three_automorphy_dense_of_prints_and_row`](/entry/unitary-three-automorphy-dense-of-prints-and-row/).

## Statement

**Theorem.** If `HypothesesH'` holds, then `UnitaryThreeAutomorphyDense` holds.

`UnitaryThreeAutomorphyDense` says: for each bound $B$ there is $m \ge B$ with $m \equiv j \pmod{l-1}$ and an irreducible three-dimensional representation of $G_L$ with prescribed seed data. The full statement is in [`unitary_three_automorphy_dense_of_prints_and_row`](/entry/unitary-three-automorphy-dense-of-prints-and-row/).

## Proof

The proof is

```
unitary_three_automorphy_dense_of_prints_and_row hH (Gal.SV.rowOf' hH.litN.aut.gal)
```

The second theorem needs the Galois row `RowT` as well as `hH`. The row is a field of the printed hypotheses: `hH.litN.aut.gal`. `RowT` is `Row0b` for the reciprocity condition `IsRecT`: for a CM field $E$ and a regular algebraic polarized cuspidal $\pi$ on $\mathrm{GL}_a(E)$, there is an attached $l$-adic Galois representation. The [Galois row chapter](/proof/galois-row/) treats this statement. The theorem `rowOf'` is the identity `fun h => h` on `RowT`. So this theorem adds nothing to the theorem it calls. It only takes the row from `hH`.

## In the Lean code

The theorem is in [UnitaryThreeInputsOfLiterature.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryThreeInputsOfLiterature.lean#L30). `rowOf'` is in [GaloisRepExistsTotallyRealGL2.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RankTwoPatching/GaloisRepExistsTotallyRealGL2.lean#L60), and `RowT` is in [WeakOfAtt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/WeakOfAtt.lean#L47). We have not unfolded `HypothesesH'` or `PropsB`. The theorem has three users: `ends0_alt`, `ends_u_alt` and `linkedUnlE_alt`.
