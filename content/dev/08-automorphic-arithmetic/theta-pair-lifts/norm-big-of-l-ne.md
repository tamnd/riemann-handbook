---
id: norm-big-of-l-ne
title: The norm of a large bottom pair is a fixed multiple of an L-value product, second name
kind: theorem
decl: GlobalTheory.T.normBig_of_lNe
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.NormBigOfNonvanishing
covers: 385
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves `NormBig`, which [the joined estimates of the square top term](/entry/square-top-term-joined-estimates/) give to `bottomTheta_nonvanishing` and to `square_ratio_valuation_without_norm_formula`. The proof only applies [`normBig_alt`](/entry/norm-big-alt/), and that entry has the real content.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), the record `Inp D` for every datum $D$, and `LNe`. Then `NormBig` holds.

`LNe` says that for each $t$ some L-function of the character $\nu_H(t, i, j)$ has no zero at the integers from $1 - e_0$ to the half rank, and that each member of a second family has an L-function with no zero at the positive integers. `NormBig` says: for all $\delta, t_0, i, j$ there is $A \neq 0$ such that for every $t$, every bottom pair $(P, P')$ at $t$ and every L-function $\Lambda$ of the character $\nu_H(t, i, j)$,
$$\|P\| = A \prod_{s = 1 - e_0}^{h_0} \Lambda(s).$$
The notation is that of [the child entry](/entry/norm-big-alt/). We have not unfolded `Inp D`.

## Proof

The proof is `first | exact normBig_alt | ...`. The first branch closes the goal, since the two statements are the same.

## In the Lean code

The theorem is in [NormBigOfNonvanishing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/NormBigOfNonvanishing.lean#L48). `NormBig` and `LNe` are in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L114). The one use is at [SquareTopTermJoinedEstimates.lean line 29](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SquareTopTermJoinedEstimates.lean#L29).

The name mentions only `LNe`, but the theorem also needs `ThetaLocalInputs` and the records `Inp D`.
