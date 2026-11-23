---
id: down-ne-of-euler-right-doubling
title: Nonvanishing of the theta lift from a definite space, restated
kind: theorem
decl: GlobalTheory.T.downNe_of_eulerRight_doubling
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.EulerFactorFromDoubling
covers: 4129
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`downNe_k_of_hypotheses'`](/entry/down-ne-k-of-hypotheses-prime/) under a second name. It says that the theta lift of a suitable form on a positive definite hermitian space is not identically zero. Its only user is [`liftInj_nonVan_typeNZ_of_hypotheses_alt`](/entry/lift-inj-non-van-type-nz-of-hypotheses-alt/), step 3 of that proof. Below this theorem are 4,129 declarations, one more than below the copy.

## Statement

Assume the doubling method input `DoublingMethodLocalZetaIntegrals` and the simple pole input `SimplePole`. Let $D$ be a datum, and assume `EulerRight D`, the unramified computation of the doubling zeta integral. Then `DownNe D` holds.

`DownNe D` says the following. Let $A$ and $W$ be hermitian spaces over the CM extension of $D$, with $A$ positive definite, $W$ of positive rank and $\operatorname{rank} A = \operatorname{rank} W + t$. Let $\omega$ be a Weil representation of the pair, and let $u$ be an automorphic form on $U(A)$ that is fixed by a principal congruence subgroup, has Satake parameters off a finite set $Z$ and meets the simple pole hypothesis for these parameters. Let $\Phi$ be a Fock vector, spherical off $Z$, with a nonzero real integral of matrix coefficients against $u$. Then there are a theta function $f$ and a point $h$ with $\int_{U(A)(F) \backslash U(A)(\mathbb{A})} \theta(g, h; f)\, u(g)\, dg \neq 0$.

## Proof

The proof is `exact downNe_k_of_hypotheses'`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is at [EulerFactorFromDoubling.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/EulerFactorFromDoubling.lean#L17).

The names of the file and of the theorem speak of an Euler factor. The conclusion is a nonvanishing statement, `DownNe`. `EulerRight` is a hypothesis, not a result.
