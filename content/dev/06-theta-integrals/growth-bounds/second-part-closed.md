---
id: second-part-closed
title: The second part of the selection lemma, with the constants 1088, 1 and 10
kind: theorem
decl: Formalism.MainNotions.SelectionLemmas.Pf.secondPartClosed
module: Formalism.SharpRestriction.GrowthBounds.SegmentDegree
covers: 906
status: drafted
drafted_by: writer@claude
---
This theorem proves `SecondPartClosed D` for every datum $D$. Under the admissibility conditions `AdmB D`, it gives a large submodule with a basis of generators inside a span of generators, and a degree bound on that span. [`local_model_results`](/entry/local-model-results/) uses it as the field `p39B` of `Loc6`. The constants are $C_0 = 1088$, $C_{rk} = 1$ and $C_{\deg} = 10$.

## Statement

**Theorem.** Let $D$ be a datum of type `D7` with `AdmB D`. Then there is $C_0 > 0$ such that for all $C_\Lambda, C_k \ge C_0$ there are $C_{rk}, C_{\deg} > 0$ with `Conclusion2 D CLa Ck Crk Cdeg`.

`Conclusion2` quantifies over a prime $p \ge 13$ with an unramified quadratic setting, ranks $r \ge 2$ and $K$, frames $F$ with a block set $T$, degrees with $a \le \deg t \le 2a$, and other parameters that meet a list of inequalities. Put $k = r + K$. Let $N$ be the span of the generators `Gen` that the frames define. Put
$$\mathrm{bound} = \Bigl(1 - \frac{C_{rk}\,|T|\,r^2 k}{Y}\Bigr) \prod_{t \in T} \binom{\deg t + k - 1}{k - 1}.$$
The conclusion has two parts.

1. There is a submodule $S \le N$ with a complement and a basis of generators, such that $(p^{n'})^{-rK}\cdot \mathrm{bound} \le \operatorname{rank} S$. Also, for every field $\mathbb{F}$ with $p^{n'}$ elements, $\mathrm{bound} / n_{\mathrm{Pl}}(\mathbb{F}, k, r) \le \operatorname{rank} S$. Here $n_{\mathrm{Pl}}$ (`nPl`) is the number of $r$-dimensional subspaces of $\mathbb{F}^k$.
2. Each monomial of each element of $N$ has degree `vsDeg` at most $C_{\deg}\,|T|\,(L_a a/(pk) + a p^{-L_1} + kQ)$, with $L_a = C_\Lambda N_s^2 \log a$.

## Proof

`second_estimate_of_restrictions` reduces the theorem to `second_estimate_of_rank_bound`, which sets $C_{\deg} = 10$ and works as follows.

1. `RestDeg` gives part 2 with the constant $10$.
2. `RestSel` is a selection fact over a discrete valuation ring. A finite set $G$ of polynomials with support in a finite set contains a basis of a complemented submodule $S \le \operatorname{span} G$. The rank of $S$ is the dimension of the span of the reductions of $G$ over the residue field.
3. `RestRank 1088 1` bounds that dimension from below by $(p^{n'})^{-rK}\cdot\mathrm{bound}$. This gives the first bound of part 1.
4. For the second bound, the proof uses the sixth part of `AdmB`, `ColumnFamilyClosure`. It gives $|\mathbb{F}|^{r(k-r)} \le n_{\mathrm{Pl}}(\mathbb{F}, k, r)$, so $(p^{n'})^{rK} \le n_{\mathrm{Pl}}$. If $\mathrm{bound} \le 0$ the bound is trivial. If not, the second bound follows from the first.

`RestRank` comes from `restRank_of`, then `restCount_of`, then `restSeg_of`. Five of their inputs need `AdmB`:

- `generator_modulo_uniformiser_of_adm`;
- `restLam_of` with `restLamDeg`;
- `restMem_of`;
- `restInd`, through `restKey_of`;
- `good_path_weight`.

The others do not need it: `discriminant_nonzero_mod_uniformiser`, `restPad`, `restSum`, `restFin` and `restMon`. The last comes from `beta_ratio_bound`, `tau_degree_on_path_bound` and `residue_class_count`. We have not unfolded these lemmas.

## In the Lean code

The theorem is at [line 33 of SegmentDegree.lean](lean:Formalism/SharpRestriction/GrowthBounds/SegmentDegree.lean#L33), and the reduction is at [line 21](lean:Formalism/SharpRestriction/GrowthBounds/SegmentDegree.lean#L21). `RestDeg`, `RestSel`, `RestRank` and `second_estimate_of_rank_bound` are in [NonemptyDvrSettingOfStandard.lean](lean:Formalism/SharpRestriction/GrowthBounds/SegmentDegree/NonemptyDvrSettingOfStandard.lean#L88). `Conclusion2`, `AdmB` and `SecondPartClosed` are in [ValuationLowestDegreeRename.lean](lean:Formalism/SharpRestriction/GrowthBounds/ValuationLowestDegreeRename.lean#L274).

Some points to note:

- `Conclusion2` names its first argument `_D` and does not use it. Only `AdmB D` depends on $D$.
- `ColumnFamilyClosure` at [line 106](lean:Formalism/SharpRestriction/GrowthBounds/ValuationLowestDegreeRename.lean#L106) also ignores $D$. It is a true fact about the number of subspaces of a vector space over a finite field. Here it is taken as an admissibility condition and not proved, and its name does not describe it.
- Two other definitions named `SecondPartClosed`, with different contents, are in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L260) and [StatementOfDegreeAndBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/StatementOfDegreeAndBound.lean#L512).
