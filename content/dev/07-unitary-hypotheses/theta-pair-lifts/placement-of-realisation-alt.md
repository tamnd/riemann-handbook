---
id: placement-of-realisation-alt
title: A normalised indefinite realisation extends
kind: theorem
decl: GlobalTheory.RowPlacementReal.placement_of_realisation_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PlacementOfRealisation
covers: 481
status: drafted
drafted_by: writer@claude
---
This theorem shows that a normalised indefinite realisation $Q$ has the property `IndefiniteRealisationExtends`. Through its second name [`indefinite_scale_theta_nonvanishing_alt`](/entry/indefinite-scale-theta-nonvanishing-alt/) it is used in [`row_rRows_stage0_alt`](/entry/row-r-rows-stage0-alt/). It proves one fact itself and gives the rest to [`exists_rowPlacement_finiteElement_matches_levels`](/entry/exists-row-placement-finite-element-matches-levels/), which dominates 451 of the 481 declarations below it.

## Statement

The hypothesis `DiscreteSeriesClassification` says: for each sign vector $\varepsilon \in \{0,1\}^n$ and each strictly decreasing $\lambda \in \mathbb R^n$ with $\lambda_a - \tfrac{n-1}{2} \in \mathbb Z$, there is an irreducible square integrable unitary representation $\pi(\varepsilon, \lambda)$ of `UJset ε` with infinitesimal character $\lambda$ and lowest $K$-type $\lambda + \rho_n - \rho_c$. Each such representation is isomorphic to one $\pi(\varepsilon \circ s, \mu)$. This has the shape of Harish-Chandra's classification of the discrete series (Acta Math. 116, 1966) with the lowest $K$-type of Hecht and Schmid (Invent. Math. 31, 1975). We have not checked `UJset` or the root data.

**Theorem.** Assume `DiscreteSeriesClassification`. Let $Q$ be an indefinite realisation over a datum $D$, an element `Rc` of `RecTAlt ex`, a row side family $P$, spectral ties $S$ and a number field $K_s$ with the coefficient field $L$ of $D$ as a $K_s$-algebra. Assume that $Q$ satisfies `IndefiniteRealisationNormalisation` (a structure of thirteen fields), and that the map $\iota_E$ of $S$ is the identity. Then `IndefiniteRealisationExtends Q` holds: there is an element $t$ of `GfC (Yc D 0)` with a level conjugation condition (`ConjLevel`) and a row level match (`RowLevelMatchAt`), and there is $c' \in \mathbb R$ with the evaluation tie `EvalTieT` at the element $t_S$ of $Q$. We have not unfolded `ConjLevel`, `RowLevelMatchAt` or `EvalTieT`.

## Proof

1. **The element $e_0$ is real.** `IdempotentRealFixed D` says that each coefficient of $e_0 = $ `D.ntypes.e0` is fixed by complex conjugation. `star_coeff_of_reverse` derives this from `star_coeff_eisenstein_series_reverse_poly`: for a monic $f$ over $\mathbb F_{g_k}$ with $f(0) \ne 0$, conjugation sends the coefficients of $e(f)$ to those of $e(f(0)^{-1} f^{\mathrm{rev}})$.
2. **The placement.** `exists_rowPlacement_finiteElement_matches_levels` gives the conclusion. Its inputs are the data of $Q$, step 1, the hypothesis on $\iota_E$, and three fields of the normalisation: `grpRecPin`, `tSfin` and `tSpin`. In its proof, one lemma finds $t$ with the level condition, a second gives the row level match, and `tSpin` moves both to $t_S$. Only the evaluation tie, from `goodRows_compare_by_levelMatching_evaluation`, uses `DiscreteSeriesClassification`.

## In the Lean code

The theorem is at [PlacementOfRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacementOfRealisation.lean#L18). The normalisation and `IndefiniteRealisationExtends` are at [IndefRRealPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IndefRRealPins.lean#L21) and [line 50](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IndefRRealPins.lean#L50), the hypothesis at [DiscreteSeriesClassificationIff.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/DiscreteSeriesUnitary₂/DiscreteSeriesClassificationIff.lean#L11).

`exists_rowPlacement_finiteElement_matches_levels` is a renaming of `rowPlacement_exists`.

The first part of the conclusion is the premise of the field `tSpin`. The theorem only shows that such a $t$ exists.
