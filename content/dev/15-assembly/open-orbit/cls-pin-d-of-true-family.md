---
id: cls-pin-d-of-true-family
title: The class data of a family character, in statement form
kind: theorem
decl: GlobalTheory.T.cls_pin_d_of_true_family
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ClsPinDOfFamColStatement
covers: 532
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`clsPinD_of_famCol_of_trueW`](/entry/cls-pin-d-of-fam-col-of-true-w/). Its only user is [the column data of a true geometric family](/entry/laws-links-of-geo-rows-cols-alt/), which takes from it the class data `ClsPinD` in step 6 of its proof and turns them into the laws `KerX`, `PerX` and `RdX`. The real content is in `clsPinD_of_famCol_of_trueW`.

## Statement

The statement is word for word the statement of [`clsPinD_of_famCol_of_trueW`](/entry/cls-pin-d-of-fam-col-of-true-w/). In short: let $W$ be a real package, $u$ a word and $f$ a family character. Assume that $W$ is valid (`ValidRealPackage`), that its twisted columns are standard (`TwStdAlt`), that the leading reading `LeadingReadAt W u f.j f.g.bT` holds, that $f$ is `RowOK`, and that $f$ has the column condition `FamilyColumnCondition`. Then the tuples $f.t$ have class data: there is a good real datum $\rho$ and, for each $t$, a good kernel class datum and a good tail class datum over $\rho$.

## Proof

The proof applies `clsPinD_of_famCol_of_trueW`. Nothing else happens.

## In the Lean code

The theorem is at [ClsPinDOfFamColStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClsPinDOfFamColStatement.lean#L16). The proof is the tactic `first | exact @GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW | ...`, so the theorem only passes its hypotheses along. In [the column data](/entry/laws-links-of-geo-rows-cols-alt/) the hypotheses come from the fields `tr` and `tw` of `AllFamilyConditions W`, the field `top` of `a.Is`, the row hypotheses and the column condition. The name speaks of a "true family", but the statement is about any family character $f$: no geometric family appears in it.
