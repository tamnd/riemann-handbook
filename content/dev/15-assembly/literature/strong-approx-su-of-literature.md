---
id: strong-approx-su-of-literature
title: Strong approximation for a special unitary group, from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.strong_approx_su_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 524
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/), ignores it, and returns the theorem [`strongApproxSU`](/entry/strong-approx-su/), which has the real content (523 of the 524 declarations below this one). It is one of the cited results that the main theorem [every character of the literature](/step/every-character-of-literature/) uses. Its result fills a field of three bundles: [UnitaryGroupThirdPlaceHypotheses](/step/published-results-eigen/), [ThetaLocalInputs](/step/published-results-first/) and [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/).

## Statement

Let $E/F$ be a CM extension and $J$ a nondegenerate Hermitian matrix of size $M \geq 2$. Let $SU(J)$ be the kernel of the determinant on the [[unitary group|0R9R0Y1HDK]] $U(J)$. Let $S$ be a finite set of places of $F$, made of infinite places $S_1$ and finite places $S_2$, and let $\varepsilon$ be the adele that is $1$ at $S$ and $0$ elsewhere. Let $SU(F_S)$ be the elements $g$ of $SU(J)(\mathbb{A}_F)$ with $\varepsilon (g - 1) = g - 1$, that is, with $g = 1$ outside $S$.

If $SU(F_S)$ is not compact, then $SU(J)(F) \cdot SU(F_S)$ is dense in $SU(J)(\mathbb{A}_F)$.

This has the form of the strong approximation theorem for a simply connected group, as in Platonov and Rapinchuk, Algebraic Groups and Number Theory, chapter 7.

## Proof

The proof is `GlobalTheory.StrongApproxSUProof.strongApproxSU`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L517). The statement `StrongApproxSU` is at [NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L33).

- The argument $O$ is not used.
- The rational points `SURat` are `SUAdelic ⊓ HFinIn`. I have not unfolded `HFinIn` or `IsPlacesIdem`.
- The proof at [ImportsTailTer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailTer.lean#L14) chains three closure lemmas with `closure_minimal`.
- A second theorem with the same short name, `GlobalTheory.CompanionTheory.Hypotheses₂.strongApproxSU`, proves the same statement at [ImportsBis.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/ImportsBis.lean#L16). This theorem does not use it.
