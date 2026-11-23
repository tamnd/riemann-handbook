---
id: exists-deg-from-of-trait
title: Tautological degeneration data along a trait
kind: theorem
decl: GlobalTheory.TChart.exists_degFrom_of_trait
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDegenerationDataTautologicalChartOfTrait
covers: 406
status: drafted
drafted_by: writer@claude
---
This theorem is step 3 of the proof of [`exists_chart_at`](/entry/exists-chart-at/). After a finite extension of a trait, it puts the degeneration data in the tautological form of a chart: the abelian part comes from a smaller Siegel family, and the periods are monomials $\prod_k s_k^{n\varepsilon_k}$. `exists_chart_at` calls the [statement entry](/entry/exists-degeneration-data-tautological-chart-of-trait/), a word for word copy.

## Statement

Use $g$, $n$, $\Lambda$, $\varphi$ with `IsPolFan` and the Siegel family $F$ of [`exists_chart_at`](/entry/exists-chart-at/).

A *trait* $T$ of $F$ (`Poinc.Trait`) has, among other fields: a complete discrete valuation ring $V$ of characteristic zero; a point $y \colon \operatorname{Spec}\operatorname{Frac}(V) \to F.X$; a semi-abelian $G$ over $V$ with a uniformisation $U$ by degeneration data $D$ (abelian part $P$, lattice $X$, points $c$), with generic fibre $y^*$ of the universal abelian scheme. Let $b \colon \Lambda \to V$ be a ring map compatible with $y$.

A *lower base* $L$ (`LowBase`) has: a Siegel family $F_L$ of genus $h$; a complete noetherian local ring $W$ with a map $u$ to the $r$-fold fibre power of the universal abelian scheme of $F_L$, which is an étale completion; the pullback $B$ of the universal abelian scheme along $u$; the tautological points $c_0 \colon \mathbb{Z}^r \to B(W)$ given by the coordinates of $u$; and trivialisations $\tau_0(a, a')$.

**Theorem.** There are a lower base $L$, a basis $\varepsilon_1, \dots, \varepsilon_{m+N}$ of the symmetric integral forms on $\mathbb{Z}^r$, a local domain $V'$ with maps $f \colon V \to V'$ and $\kappa \colon W \to V'$, elements $s_k \in V'$, data $D'$ over $V'$ and a uniformised $G'$ over $V'$, such that:

1. $h + r = g$;
2. $\varepsilon_1, \dots, \varepsilon_m$ span a cone of $\varphi$, and for each $x \neq 0$ there is $k \leq m$ with $\varepsilon_k(x, x) > 0$;
3. $V'$ is a complete discrete valuation ring of characteristic zero; $f$ is injective, finite and local; $\kappa$ is local; $\kappa \circ b_L = f \circ b$;
4. $s_k$ is a nonzero element of the maximal ideal for $k \leq m$, and a unit for $k > m$;
5. $G'$ and its uniformisation by $D'$ are the pullbacks of $G$ and $U$ along $f$, compatible with $y$ (`IsUnifAlong`);
6. `DegFrom`: $D'$ refines data with abelian part $B \otimes_\kappa V'$, points $a \mapsto c_0(na)$, and periods $\tau(a, a') = \prod_k s_k^{\,n\varepsilon_k(a,a')} \cdot \tau_0(na, na')$.

## Proof

1. [`exists_lower_base_of_trait_abelian_part`](/entry/exists-lower-base-of-trait-abelian-part/), for $P$ and $c$ in a basis of $X$: after a finite extension $V \to V_1$, $P$ and $B$ become one abelian scheme, and $c(a)$ and $c_0(na)$ become one point. So $r = \operatorname{rk} X$.
2. `Poinc.Trait.dim_add_rank`: $\dim P + \operatorname{rk} X = g$, so $h + r = g$.
3. `T.exists_pulledBack_periods_basePeriods_constForm`: there is a symmetric bimultiplicative $q$ on $\mathbb{Z}^r$, with $q(a, a)$ in the maximal ideal for $a \neq 0$, such that $q = \prod_k s_k^{n\varepsilon_k}$ in an extension gives clause 6.
4. `PerRoot.exists_roots_of_periods`, the one step that uses `IsPolFan`, writes the valuation of $q$, a positive definite form, as a positive combination of the generators of a cone of $\varphi$, completes them to a basis $\varepsilon$, and adjoins $n$-th roots in a finite extension $V_2$.
5. `TraitExt.exists_unifAlong_pullTo`: pull $G$, $D$ and $U$ back to $V_2$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsDegenerationDataTautologicalChartOfTrait.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDegenerationDataTautologicalChartOfTrait.lean#L18). The lemmas of steps 2 to 5 have no entry. We read their statements, and the proof of step 4.

The hypothesis `hb : T.y ≫ F.s = jK T.V ≫ spMap b` is never used after `intro`. So $b$ can be any ring map $\Lambda \to V$; the clause $\kappa \circ b_L = f \circ b$ comes from step 1 alone.
