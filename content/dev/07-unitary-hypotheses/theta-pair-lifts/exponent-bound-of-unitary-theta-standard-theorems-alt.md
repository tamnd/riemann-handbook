---
id: exponent-bound-of-unitary-theta-standard-theorems-alt
title: The exponent bound from eight named hypotheses
kind: theorem
decl: GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExponentBoundOfUnitaryThetaStandardTheorems
covers: 3718
status: drafted
drafted_by: writer@claude
---
This theorem proves the exponent statement about the record objects of a family from eight named hypotheses. It is the content behind [`expSt_of_base_change_and_crystalline_lattices`](/entry/exp-st-of-base-change-and-crystalline-lattices/), a copy, which [`ontoX_of_hypotheses_alt_alt`](/entry/onto-x-of-hypotheses-alt-alt/) uses in branch 2 of the [unitary hypotheses node](/proof/unitary-hypotheses/). Below this theorem are 3,718 declarations.

## Statement

**Theorem.** Assume the following eight propositions: `ClozelCohomological`, `HeckeLAdicCharacter`, `ChebotarevDegreeOne`, `CuspUAlt`, `BaseChangeDefiniteUnitaryGroup`, `BhattScholzeCrystallineLattices`, `HeckeLAdicCharacterAbove` and [`RecTExists`](/step/rect-exists-def/). Then `ExponentStatement` holds.

The caller takes all eight as its own hypotheses. They are named after published results, in the manner of the [input record](/step/unitary-group-third-place-hypotheses-def/). Two of them are unfolded in [the entry on the model statement](/entry/model-st-of-small-frame-gal/).

`ExponentStatement` has the form `ForallRecordObjects Q` of [the geometric statement](/entry/geo-st-of-page-st-alt/): for small $\varepsilon$, for large families, for large constant records, eventually at points, for each recorded object $O$. Its predicate is: for all reals $C, C_H$, `HasExpBound N O`, where $N$ is the number record of the point at $(C, C_H)$. `HasExpBound N O` says:

1. $J_0(\mu_w, w, j) \ge 0$ for each twisted place $w$ and each index $j$;
2. there are weights $J_p(j, \ell) \ge 0$, one for each index $j$ and each natural number $\ell$, with $J_0(\mu_w, w, j) \le J_p(j, \ell_w)$, where $\ell_w$ is the residue characteristic of $w$;
3. for each $j$ and each finite set $Q$ of primes, $\sum_{\ell \in Q} J_p(j, \ell) \log \ell \le 30\, T_2\, m\, b\, x_e^2 + 2 m b$.

So the exponents $J_0$ are bounded place by place, and the bounds have a controlled weighted sum.

## Proof

The proof is one term. It calls [`expSt_of_num_sumExp_model`](/entry/exp-st-of-num-sum-exp-model/) with four inputs:

1. `ExCut`, from `weylLattice_exact_exponent_block_cut`, with no hypothesis;
2. `NumStAlt`, from `numSt_alt`, with no hypothesis;
3. `ExponentSumStatement`, from `sum_expansion'`, with no hypothesis;
4. `ModelStatement`, from [`model_statement_of_crystalline_chebotarev_frame_gal`](/entry/model-statement-of-crystalline-chebotarev-frame-gal/). Its inputs are `BhattScholzeCrystallineLattices`, `ChebotarevDegreeOne`, the smallness condition `small_estimate`, the frame statement `frame_statement_of_small_statement small_estimate`, and the Galois statement `galois_frame_compatibility_alt`. The last takes all eight hypotheses and `small_estimate`.

So the eight hypotheses enter only through the model statement.

## In the Lean code

The theorem is in [ExponentBoundOfUnitaryThetaStandardTheorems.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExponentBoundOfUnitaryThetaStandardTheorems.lean#L20). `ExponentStatement` is in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L43), and `HasExpBound` is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L82).

- `galois_frame_compatibility_alt` is a copy of `galois_steinberg_local_alt` in [GaloisAtPlaceOfAutomorphicAtPlace.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisAtPlaceOfAutomorphicAtPlace.lean#L154). That proof passes the eight hypotheses to `galois_side_of_compatible_systems_alt`, which we have not unfolded. Six of the eight (all except the Bhatt-Scholze and Chebotarev hypotheses) are used only there.
- The name says "unitary theta standard theorems". No hypothesis and no part of the conclusion is about a theta correspondence.
