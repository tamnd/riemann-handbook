---
id: automorphy-of-hypotheses-alt-alt
title: The export condition at built points, restated
kind: theorem
decl: GlobalTheory.T.automorphy_of_hypotheses_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AutomorphyOfHyp
covers: 2229
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`exportF_prmR_alt_alt`](/entry/export-f-prm-r-alt-alt/) under a second name. It gives the export condition `ExportF` at the built points of the parameters of a norm choice extension. Its user is [`exists_baseLattice_of_pair_alt`](/entry/exists-base-lattice-of-pair-alt/), which passes the result to [`memberE_closing_alt_alt`](/entry/member-e-closing-alt-alt/). This is in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 2,229 declarations, one more than below the copy.

## Statement

**Theorem.** Assume the 29 named statements of [`exportF_prmR_alt_alt`](/entry/export-f-prm-r-alt-alt/) (Galois cohomology, class field theory, automorphic forms and $p$-adic Hodge theory, not unfolded here). Let $h_L$ be a proof of `RecTExists`, and assume `MemberAtLayerPoint`. Let $N$ be a norm choice extension, $S$ an S-extension and $\Gamma$ a geometry. Suppose that each element of $N$ at a point gives an element of `extensionWithLaw` at that point. Then

$$\mathrm{ExportF}\bigl(\mathrm{KPx},\ \mathrm{IsBuiltE}(s)\bigr), \qquad s = (\mathrm{parametersOfExtension}\ N\ S\ \Gamma).s.$$

`ExportF` asks, for all large contexts and each built core, for exponents and finite sets with good twists. The entry of the copy unfolds it.

## Proof

The proof is `exact exportF_prmR_alt_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

The copy also only passes hypotheses along, to [`exportF_isBuiltE_alt_alt`](/entry/export-f-is-built-e-alt-alt/). The mathematics is there and in [`series_realization_of_published_alt`](/entry/series-realization-of-published-alt/).

## In the Lean code

The theorem is in [AutomorphyOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutomorphyOfHyp.lean#L44), and the copy at [line 27](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutomorphyOfHyp.lean#L27). `ExportF` is defined in [NotBaseCondFalse.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotBaseCondFalse.lean#L55), `ExportAt` in [AmbientBaseHeq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/AmbientBaseHeq.lean#L36), and `IsBuiltE` in [ThetaChr.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ThetaChr.lean#L89).

The name is misleading. The conclusion is an export condition on twist data, not a statement of automorphy. The caller uses it only with $S = $ `SExt.none` and $\Gamma = $ `geoCl anyGeometry`, although the statement allows any $S$ and $\Gamma$.
