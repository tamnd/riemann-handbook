---
id: lift-inj-and-non-van-type-nz-of-given
title: Injectivity and nonvanishing of the downward theta lifts, restated
kind: theorem
decl: GlobalTheory.T.liftInj_and_nonVan_typeNZ_of_given
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.LiftInjNonVanTypeNZOfPrints
covers: 4221
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`liftInj_nonVan_typeNZ_of_hypotheses_alt`](/entry/lift-inj-non-van-type-nz-of-hypotheses-alt/) under a second name. It says that the theta lifts of a real datum are injective on good eigenvectors and do not vanish on nonzero eigenvectors. It has two users, `DownLift.nonvanishing_of_down_lift` and `ontoC_of_hypotheses_alt`, both below [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/) in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 4,221 declarations, one more than below the copy.

## Statement

The statement is the statement of the copy, word for word. Assume five named inputs: `CuspRapidDecay`, `DoublingMethodLocalZetaIntegrals`, `UnramifiedDoublingGL`, `HeckeLPartialContinuation` and `HoweUnram`. Let $D$ be a datum, $G$ a finite group, $A$ a family (`FamIn`), $K_s$ a number field, $R$ a real datum over $A$ and $K_s$, and $F$ a face of $A$. Assume `Given R F` (a record: a core condition, a choice of parameters, absolute irreducibility of the characters of $A$, good types, a guard, and a gap $\lambda_n - \lambda_{n+1} \ge 100 r^4$ between consecutive values of `lamAt`) and `R.FullP` (each Weil representation $\omega_P(i,t)$ of $R$ is full). Then:

1. `LiftInj R`: at $t = \mu_0$, let $x$ and $y$ be eigenvectors with the same Hecke eigenvalues, with $\theta(x) \neq 0$ and $y$ good. If $\theta(y) = 0$, then $y = 0$.
2. For all $i$ and $t$, `NonVan R i t`: each nonzero eigenvector $y$ has a theta function $f$, a functional $l$ and a point $g$ at which the theta integral of $y$ against $f$ is not $0$.
3. For all $i$ and $t$, `TypeNZ R i t`: a good eigenvector $y$ with $\theta(y) = 0$ is $0$.

We have not unfolded `FamIn`, `RealDat`, `Face` or the theta maps.

## Proof

The proof is `exact liftInj_nonVan_typeNZ_of_hypotheses_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content. The [entry of the copy](/entry/lift-inj-non-van-type-nz-of-hypotheses-alt/) has the proof.

## In the Lean code

The theorem is at [LiftInjNonVanTypeNZOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/LiftInjNonVanTypeNZOfPrints.lean#L51), and the copy at line 14 of the same file. It sits in the namespace `GlobalTheory.T` and the copy in `GlobalTheory.Core.Rk.LiftOnto`.

The word "prints" in the file name matches no object in the statement.
