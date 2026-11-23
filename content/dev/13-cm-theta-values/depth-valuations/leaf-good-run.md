---
id: leaf-good-run
title: The depth bound at good places, for the leaf objects of a run
kind: theorem
decl: GlobalTheory.GoodDepth.leafGood_run
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthLeafGoodPrimesOfPointData
covers: 921
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `LeafDepthGood` at the good places of a leaf object that is tied to a datum $D$, given the package statements `PkgSt`. It is a specialization: it applies the general bound `LeafGoodSt` with $C_1 = 100$ to the data that $D$ and its core give, and checks the hypotheses. Its alias [`depthLeaf_goodPrimes_of_point_data`](/entry/depth-leaf-good-primes-of-point-data/) gives the result to [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/). The real content is below, in [`depthTable_goodPrimeLeaf`](/entry/depth-table-good-prime-leaf/) and its proof [`leafGood`](/entry/leaf-good/).

## Statement

The statement is that of [the alias](/entry/depth-leaf-good-primes-of-point-data/): there is $C_0$ such that `LeafDepthGood N O` holds under `LawsM T`, `RunTie`, `PkgSt` at each $j$, $C_0 \le C$, `LeafPage O`, `LeafSizes O`, $10 \le C_{nW}$, $3 \le x^{e_z/5}$, $x \ge 3$, $k b' \le b$ and the content condition.

`LeafGoodSt` says: for each $C_1 \ge 0$ there is $C_0$ such that, for each family of moduli schemes $X_j$ with a coefficient field, depth data, a leaf object $O$, a numerical datum $N$ and a map $p_l$ of places to embeddings, the bound `LeafDepthGood` holds if $C_0 \le C$ and a list of ties holds: the depths and constants of $O$ are those of the depth data, `PiSplit` and `LevelQ` hold, charts exist, `PkgSt` holds at each $j$, $p_l$ satisfies `PlaceTie`, each $j$ has a good page (`GoodPage`), $O$ and $N$ are tied (`NumTie`, `TiePrimes`), and `LeafPage` and the content condition hold.

## Proof

Take $C_0$ from `depthTable_goodPrimeLeaf` with $C_1 = 100$. Apply it to the field $E$, the host, the level, the data and the moduli schemes of the core $T$, the depth data `depOf T EX Tp hK`, the numerical datum `numOf D L`, and $p_l(z) = \tau_D(\mathrm{pl}_D(z))$. Then check the ties.

1. The depths, constants and bad primes of $O$ come from the fields of `RunTie`. `PiSplit` and `LevelQ` come from `piSplit_depDataOf` and `levelQ_depDataOf`. Charts exist by `exists_integral_chart_integral_framed_point`.
2. `PlaceTie` is `realPlaces_match_cmTypeFrobenius`.
3. For each $j$: the range $1 \le \iota(j) \le m$ from `RunTie`, the signature from the pins of $T$, dominance from `dom_wtA`, and `GoodPage` from `goodPrimeWeightHypotheses_of_depthParameters`. Here $b$ and $L$ of $O$ are those of $D$, and $\log k \le L$ comes from `LeafSizes`.
4. `NumTie`: $k, m, f$ and the thresholds from `RunTie`; $S_c + \eta$ is at most $S_e$ of $O$ by `numOf_sizes_le`; $\sum_z w_j(z) \le 2fb$ by `firstRows_bound_and_sizes_bounds`; and the bound on $\mathrm{DF}$ through `weightExponents_embeddings_degree`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [DepthLeafGoodPrimesOfPointData.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthLeafGoodPrimesOfPointData.lean#L47). The lemmas it calls:

- `GlobalTheory.T.depthTable_goodPrimeLeaf`, an alias of `GoodDepth.leafGood`;
- `numOf_sizes_le` (line 18) and `card_RPl` (line 42), in the same file;
- `GlobalTheory.T.goodPrimeWeightHypotheses_of_depthParameters`, `realPlaces_match_cmTypeFrobenius`, `firstRows_bound_and_sizes_bounds`, `weightExponents_embeddings_degree` and `exists_integral_chart_integral_framed_point`;
- `piSplit_depDataOf` and `levelQ_depDataOf` in [DepthTie.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/DepthTie.lean#L255), and `dom_wtA`.

`LeafGoodSt`, `GoodPage`, `NumTie` and `PlaceTie` are in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L198). The package hypothesis is passed on unchanged. The five equalities of `RunTie` for $g_1, g_2, q_1, d$ and $s_m$ are given twice, once for the ties of $O$ and once for `TiePrimes`. `LeafSizes` is used only for $\log k \le L$. We have not unfolded `TiePrimes`, `PiSplit`, `LevelQ` or `depOf`.
