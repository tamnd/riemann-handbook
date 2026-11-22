---
id: true-geometry-family-final-alt
title: Place laws for a rescaled tuple, the statement form
kind: theorem
decl: GlobalTheory.T.true_geometry_family_final_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LawsRescStatement
covers: 1078
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [place laws for a rescaled tuple](/entry/laws-resc-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the column side of a geometric family](/entry/col-side-alt/), which uses it for the field `laws` of `ColumnOutputCondition`.

## Statement

Assume `DiscreteSeriesCover` and `HarishChandraModules`. Let $W$ be a real package with `AllFamilyConditions W`, $u$ a word, and $a$ a geometric family with `a.Is` and `a.True`. Let a row choice and a column choice be given, with `RowOK` and `ColOK`. Fix an index $t$, a local family $F$ and a tuple $w_0$ with $F$ pinning $w_0$, and roots of unity $s_j(\alpha)$. Assume that the set of places of $w_0$ is the set of restrictions to the field `host.F` of the places in `Q t`. Then the rescaled tuple $\mathrm{resc}(w_0, s)$ satisfies `QLaw`, `QLast` and `QFin`.

[Place laws for a rescaled tuple](/entry/laws-resc-alt/) says what these predicates mean.

## Proof

The proof is `first | exact @GlobalTheory.QColLaws.laws_resc_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [LawsRescStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsRescStatement.lean#L19). It is used once, in [ColSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ColSide.lean#L195).

The name says "final", but the statement is about the place laws of one rescaled tuple. The hypothesis `a.True` is in the statement but is not used by the proof of [`laws_resc_alt`](/entry/laws-resc-alt/). A copy without `_alt`, `true_geometry_family_final`, wraps `GlobalTheory.QColLaws.laws_resc` in `AbelianVarietyTheory.Proofs.DecoratedLatticeProofs`.
