---
id: laws-resc-alt
title: Place laws for a rescaled tuple
kind: theorem
decl: GlobalTheory.QColLaws.laws_resc_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LawsResc
covers: 1077
status: drafted
drafted_by: writer@claude
---
This theorem proves the three place laws `QLaw`, `QLast` and `QFin` for a tuple of local data that is pinned up to roots of unity. It checks the hypotheses of [`seeSawTwistPlaceLaws_of_rootOfUnityRescaling`](/entry/see-saw-twist-place-laws-of-root-of-unity-rescaling/) for one family character and applies it. The relay [`true_geometry_family_final_alt`](/entry/true-geometry-family-final-alt/) restates it for [the column side of a geometric family](/entry/col-side-alt/).

## Statement

Let $W$, $u$, $a$ be as in [the column side of a geometric family](/entry/col-side-alt/): a real package with `AllFamilyConditions W`, a word and a geometric family with `a.Is` and `a.True`. Let $f$ = `a.fam row col` be the family character of a row choice and a column choice, with `RowOK` and `ColOK`. Write $c$ for its commuting datum, $v$ for the commuting data of $a$, and $\tau = f_t(t)$ for the tuple at an index $t$.

A tuple $w$ on $\tau$ (`VTup`) is a finite set $Q$ of places with local data at $Q$: elements $e_Q$, $d_Q$, $\varepsilon$, $\varepsilon_T$ of group algebras, scalars $s_c$, $c_Q$, $c_T$, and function spaces $F_X$, $F_Y$, $F_T$. For $s_j(\alpha) \in \mathbb C$, the rescaled tuple $\mathrm{resc}(w, s)$ has

$$d_Q(j, \alpha, \gamma) \mapsto s_j(\alpha)\, s_{j+1}(\gamma)^{-1}\, d_Q(j, \alpha, \gamma), \quad \varepsilon_j(\alpha) \mapsto s_j(\alpha)\, \varepsilon_j(\alpha), \quad \varepsilon_T(n, \beta) \mapsto s_n(\beta)\, \varepsilon_T(n, \beta),$$

and the other data of $w$.

**Theorem.** Assume `DiscreteSeriesCover` and `HarishChandraModules`. Let $F$ be a local family (`QFam`) that pins $w_0$. Let each $s_j(\alpha)$ be a root of unity. Assume that the set $Q$ of $w_0$ is the set of restrictions to the field `host.F` of the places in `Q t`. Then $w = \mathrm{resc}(w_0, s)$ satisfies:

- `QLaw v w`: for each level $j$ with $j + 2(\sigma + 1) + 2 = m$, a relation `Iter2` at the places of $Q$ between two sums of periods. One side is weighted by the coefficients of $\varepsilon_j$, the other by $c_Q(j)$ and $d_Q$;
- `QLast v w`: the same kind of identity at the last level $j + 2 = m$, with integrals over a fundamental domain $\mathcal F$ in place of periods;
- `QFin v w`: for each such $j$, a compact open subgroup $K_1$ and a finite set $T_1$ at the places of $Q$, such that $K_1$ acts by scalars $a^{-1}$ and $a$ on the vectors $e_Q * \Psi$ for vacuum vectors $\Psi$, and each $x$ where the functional `flatBF` is nonzero lies in $R\, T_1 K_1$, with $R$ the group `jacGrp`.

We have not unfolded the periods, the vacuum predicate `Vac` or `Iter2`.

## Proof

1. `famCh_is_and_tuples_is_of_colOK` (with the two named hypotheses and `pk`) gives that $c$ is good and, with `ColOK`, that $\tau$ is good.
2. `weilOK_of_rank_one_gram'` gives `WeilOK v` for $\tau$. Its rank one Gram hypothesis comes from the field `shape` of `a.Is`, and the tie from the field `tie`. The place hypothesis is the assumption on $Q$.
3. The tuple $w$ satisfies `QPinU v w` with witness $(w_0, s, F)$: it is a pinned tuple rescaled by roots of unity.
4. `seeSawTwistPlaceLaws_of_rootOfUnityRescaling` turns `c.Is`, `τ.Is`, `v.Is` (the field `vis` of `a.Is`), `WeilOK` and `QPinU` into the three laws.

## In the Lean code

The theorem is in [LawsResc.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LawsResc.lean#L19). The laws are in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L228) and the rescaling in [RescOne.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/RescOne.lean#L9).

The lemmas: `famCh_is_and_tuples_is_of_colOK`, `weilOK_of_rank_one_gram'`, `seeSawTwistPlaceLaws_of_rootOfUnityRescaling` (a relay for [`laws_of_pin_resc`](/entry/laws-of-pin-resc/)).

The hypothesis `a.True` is never used: the proof names it `_haT`. Of `AllFamilyConditions W` only the field `pk` is used. The two named hypotheses only go to step 1. A parallel copy for `RealPack`, `laws_resc`, is in [TrueGeometryFamilyFinal.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyFinal.lean#L12).
