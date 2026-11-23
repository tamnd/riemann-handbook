---
id: semi-abelian-lie-seminegative-of-literature
title: Subbundles of the Lie algebra of a semi-abelian scheme have degree at most zero, from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.semi_abelian_lie_seminegative_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/), ignores it, and returns the theorem [`semiAbelianLieSeminegative`](/entry/semi-abelian-lie-seminegative/), which has the real content (454 of the 455 declarations below this one). It is one of the cited results that the main theorem [every character of the literature](/step/every-character-of-literature/) uses. It does not go into a bundle. The proof of the main theorem passes it directly to the volume estimate `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`.

## Statement

Let $k$ be a field of characteristic $0$. Let $C$ be a scheme over $k$ that is smooth of relative dimension $1$, projective and geometrically connected, so a smooth projective curve. Let $G$ be a semi-abelian group scheme over $C$, and let $\mathrm{Lie}\,G$ be its Lie algebra sheaf. Let $W$ be a vector bundle of rank $r$ on $C$ with a monomorphism $W \to \mathrm{Lie}\,G$. Then
$$\deg \det W \leq 0.$$

The Lean code writes the degree as the intersection number `interNum` of the one line bundle $\det W$ on $C$. I have not unfolded `interNum`. I do not know a published source for the statement in this form.

## Proof

The proof is `GlobalTheory.Nef.semiAbelianLieSeminegative`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L499). The statement `SemiAbelianLieSeminegative` is at [InterNumDetNonposSplitTorus.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/InterNumDetNonposSplitTorus.lean#L23).

- The argument $O$ is not used.
- The main theorem uses it at [line 812](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L812).
- The proof at [SemiAbelianLieSeminegativeBis.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianLieSeminegativeBis.lean#L22) moves to the algebraic closure of $k$ with `GlobalTheory.T.semiNegative_descends_fieldExtension_curve`. There it uses [the case of an algebraically closed field](/entry/lie-sheaf-semi-abelian-semi-neg-of-is-alg-closed/), with the fact that the Lie algebra commutes with base change (`lieBaseIso`).
