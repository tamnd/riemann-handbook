---
id: integrality-from-metric-of-le
title: The local colength bound from three facts on lattices
kind: theorem
decl: GlobalTheory.TheoremAFinal.integralityFromMetric_of_le
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingOfEtaleExactDeRhamCrystallineConst
covers: 1155
status: drafted
drafted_by: writer@claude
---
This theorem says that the thirteen local inputs `Adm1` imply the local colength bound for crystalline lattices, for each constant $C \ge 160$. It does this by proving three side facts and calling [the integrality bound for large constants](/entry/integrality-from-metric-of-large-constant/), which has the real content. Its only user is [its renaming](/entry/integrality-from-metric-of-160-le/), which goes to [the closing of the local bound](/entry/theorem-a-closing/).

## Statement

**Theorem.** Let $D$ be a datum with local data $HW$, $F$, $Cm$, let $C_A, C_B, C_K$ be reals, and let $C \ge 160$. If `Adm1 D HW F Cm CA CB CK` holds, then `Conclusion1 D C` holds.

Both `Adm1` and `Conclusion1` are stated in [the closing of the local bound](/entry/theorem-a-closing/). In short: `Conclusion1 D C` bounds the $\mathcal{O}$-length of the cokernel of $Z^1_f(T_1) \to Z^1_f(T_2)$ modulo coboundaries, for a surjection $T_1 \to T_2$ of crystalline lattices over a good pair $(K, L)$ at an odd prime $\ell$. The bound is $C$ times an explicit expression in the degrees of $K$, the rank and the Hodge-Tate jumps.

## Proof

`Formalism.MainNotions.N.Ln34.integrality_from_metric_of_large_constant` has the same conclusion, with three more hypotheses. The proof supplies them.

1. `FontExAll`: for each good triple $(K, s, L)$, the Wach module functor $W$ of $HW$ is exact on short exact sequences of lattices $0 \to T_0 \to T_1 \to T_2 \to 0$. That is, $W(\iota)$ is injective, $W(\pi)$ is surjective and $\ker W(\pi) = \operatorname{im} W(\iota)$. This is `GlobalTheory.LatExact.W_exact`.
2. `DdRFull`: for a crystalline lattice $T$ over $(K, L)$ with $(K, s, L)$ good for some $s$, and each embedding $\tau$, $\dim_L D_{\mathrm{dR},\tau}(V) = \dim_L V$. This is `GlobalTheory.CrysDdR.finrank_DdRE_of_isCrys`.
3. `DiRank`: for a crystalline lattice $T$ over a good pair with $s = 1$ and each $c \in \mathbb{Z}/n$, a space `ιDi` built from the Wach module of $T$ has dimension $\dim_L V$. This is `GlobalTheory.NL.IotaLetterRank.finrank_iota_letter`. This page has not unfolded `ιDi`.

The rest is bookkeeping.

## In the Lean code

The theorem is at [LocalLiftingOfEtaleExactDeRhamCrystallineConst.lean line 16](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingOfEtaleExactDeRhamCrystallineConst.lean#L16). The called lemma is in [MainFinal.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainFinal.lean#L10). Its proof is `lifting_theorem_of_uniform_link u1link_pf`, and `lifting_theorem_of_uniform_link` in [MainPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainPf.lean#L38) applies `local_theorem_of_leaf_lemmas` to 29 leaf lemmas. This page has not unfolded them.

- The three side facts are proved outright, with no hypothesis. So this theorem has the same strength as `integrality_from_metric_of_large_constant` without its three extra hypotheses.
- In the definitions of `FontExAll` and `DiRank`, the arguments `F` and `Cm` are named `_F` and `_Cm` and are not used.
- The name `IntegralityFromMetric` does not describe the statement; see [the renaming](/entry/integrality-from-metric-of-160-le/).
