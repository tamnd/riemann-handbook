---
id: exists-spectral-level-objects-replaced-stages
title: Spectral level objects for replaced stages, a second name
kind: theorem
decl: GlobalTheory.T.exists_spectralLevel_objects_replacedStages
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsSpectralLevelObjectsReplacedStagesStatement
covers: 351
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`GlobalTheory.Mem.SRe.exists_sRest_top`](/entry/exists-s-rest-top/). Its statement is that theorem's statement, word for word, and its proof only applies it. Its one user is [the S-stage theorem](/entry/sre-sat-of-discrete-series/). Below it are 351 declarations.

## Statement

Assume the five spectral hypotheses and the hypotheses on $D$, $P$, $R$, $F$ and $e_E$ of [the S-stage theorem](/entry/sre-sat-of-discrete-series/), for a datum $D$ in place of a late stage. Then there are:

1. a proof that $\dim_{\mathbb{C}} HH(P.X) = D_{\mathrm{all}}$;
2. a linear isometry $j \colon EE \to EEC(P.X, P.G)$;
3. an element $t$ of the adelic group of $Y_0$ and a constant $c > 0$, with `SeeAt`, `EvalTieT` and `RowJ` for $t$, $c$ and $j$;
4. for all divisor data $(N, h)$ and all forms $F'$ on the datum `reD D ⟨P.toNew hD j, N, h⟩` with the same levels and values as $F_0$: the finiteness fact `FinX` for the restaged full data, and a restriction $S$ of the restaged pack with $S.j = j$ followed by the restaging map `eEECre`.

## Proof

The proof applies `exists_sRest_top`, which does the work. It finds $t$ (`exists_finiteAdelicPoint_carries_rowLevel`), a lowest vector $v_0$ and $c$ whose evaluation identifies the level rows (`lowestVector_evaluation_identifies_levelRows_conj`), the isometry $j$ and the dimension (`exists_rowIsometry_conjugatedGoodRows_finrank`), and the restriction $S$ (`exists_sRest_re`). We have not unfolded these lemmas.

## In the Lean code

The theorem is in [ExistsSpectralLevelObjectsReplacedStagesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralLevelObjectsReplacedStagesStatement.lean#L14). The proof is a `first | exact ... | apply ...` over three forms of the same call. `exists_sRest_top` is in [ExistsSpectralLevelObjectsReplacedStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralLevelObjectsReplacedStages.lean#L24). There each of the five hypotheses goes to at least one lemma; none is dropped.
