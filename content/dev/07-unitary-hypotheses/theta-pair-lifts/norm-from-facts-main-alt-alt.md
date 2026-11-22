---
id: norm-from-facts-main-alt-alt
title: The congruence length bound from the norm choice facts, with the constant 40
kind: theorem
decl: GlobalTheory.NormFromFacts.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherLast
covers: 3257
status: drafted
drafted_by: writer@claude
---
This theorem gives one constant $C_T$ for which the bound `PairedCharacterConditionAlt D (8 C_T) C_T` holds at each datum $D$ that satisfies the norm choice facts and the four ties. It fixes $C_T = 40$, builds the local data from Bhatt-Scholze, and passes thirteen facts to [`conclusion41_of_pAdicHodge_alt`](/entry/conclusion41-of-p-adic-hodge-alt/), a copy of [`ClosingLocalInputs.main_alt_alt`](/entry/closing-local-inputs-main-alt-alt/). That theorem has the content. The user is the copy [`exists_bound_tieChi_of_prints`](/entry/exists-bound-tie-chi-of-prints/), and the bound goes on to [`ExtraFromFacts.main_alt_alt`](/entry/extra-from-facts-main-alt-alt/). Below this theorem are 3,257 declarations.

## Statement

`Hypotheses₂` (in the namespace `GlobalTheory.NLink`) is a record of seven named inputs: `FontaineBcris`, `GlobalArtinReciprocity`, `BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK`, `LocalFinitenessK` and `BhattScholzeIntegral`. We have not checked them against the literature.

`NormChoiceFacts D n` is a record of named conditions on a datum $D$ and a norm choice $n$: 14 core fields (point conditions, an admissible datum, residual irreducibility of rank $r$, weight and block parameters, depth zero and others) and 7 more. `Tie4 D` is the conjunction of `tieChi`, the existence of a pending datum $P$ with `admDZ P` and `EigSpan P`, `TieInePoly` and `SerLoc`. The statement writes `Tie4` out in full. We have not unfolded most of these fields.

**Theorem.** Assume `Hypotheses₂`. Then there is $C_T \in \mathbb N$ such that for each datum $D$ and norm choice $n$, if `NormChoiceFacts D n` and `Tie4 D` hold, then `PairedCharacterConditionAlt D (8 C_T) C_T`.

The bound says that at each local index $i$ with $\ell_i = g_k$, under conditions on jumps and on the size of $g_k$, the congruence length $\eta_i$ is at most $\sum_{\pi} m(\pi) R(\pi)$. The [entry with the content](/entry/closing-local-inputs-main-alt-alt/) states it in full.

## Proof

Take $C_T = 40$. Then $C = 8 C_T = 320$, and both conditions $C_T \ge 40$ and $8 C_T \le C$ hold by `le_rfl`. `exists_wachFunctor_comparison_of_bhattScholze` gives, from `BhattScholzeIntegral`, local data $HW$, $F$ and $Cm$ for $D$. Then `conclusion41_of_pAdicHodge_alt` gives the bound. Its twelve conditions on $D$ come from the hypotheses: `tie0`, `adm1`, `adm2_alt` and `adm5` from the admissible datum field, `provisionFortyOne` from `Conclusion1`, `ConclusionG5` and `ConclusionG6` from `Conclusion2`, residual irreducibility from `rhoBar`, `TypePrimeWildIdempotentChoice` from `duties`, and the rest from `Tie4`. The rest is bookkeeping.

## In the Lean code

The theorem is at [ImportsFurtherLast.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherLast.lean#L13). `Hypotheses₂` is at [BoundAtTwoAndThreeForFamily.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoAndThreeForFamily.lean#L18), `NormChoiceFacts` at [NormChoiceFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NormChoiceFacts.lean#L30), and `Tie4` at [RhoBar.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/RhoBar.lean#L36).

Odd points:

- The field `fin : LocalFinitenessK` of `Hypotheses₂` is not used. The proof uses the other six.
- The statement says "there is $C_T$", but the proof shows it for $C_T = 40$. The bound with $C_T = 40$ needs $g_k > 40\bigl((s+S)(n_V+1)^2 + (n_V+1)^3\bigr)$.
- The module is named `ImportsFurtherLast` and the namespace `NormFromFacts`. Neither name says what the theorem proves.
