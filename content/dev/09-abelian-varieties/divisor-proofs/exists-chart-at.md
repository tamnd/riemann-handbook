---
id: exists-chart-at
title: A tautological chart at each point of the Siegel blowup
kind: theorem
decl: GlobalTheory.TChart.exists_chart_at
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTautologicalChartAtSiegelBlowupPoint
covers: 1212
status: drafted
drafted_by: writer@claude
---
This theorem gives a formal chart at each point of a normalised blowup $S$ of a compactified Siegel moduli scheme: a complete local ring $R$ with a Mumford family over it. The [statement entry](/entry/exists-tautological-chart-at-siegel-blowup-point/) restates it for [`chartSt5_holds`](/entry/chart-st5-holds/).

## Statement

Fix $g \geq 1$ and an odd $n \geq 3$, and let $\Lambda = \mathbb{Z}[\zeta_n, 1/n] \subset \mathbb{C}$.

- $\varphi$ is a real function on integral bilinear forms (`InvFun`). `IsPolFan id g φ` says that on lattices of rank at most $g$, $\varphi$ is homogeneous, superadditive and integral, and its cones (`IsCone`) form a fan that is finite up to $\mathrm{GL}(X)$. `NoSelfInt` says that no element of $\mathrm{GL}(X)$ maps one ray of a cone to another ray of it.
- $F$ is a Siegel family (`SFam`): a smooth quasi-projective $F.X$ over $\Lambda$ with a universal principally polarised abelian scheme with level-$n$ structure.
- `MinAt5` (on $i \colon F.X \to Z$) and `BlowAt` (on $\pi \colon S \to Z$ and $j \colon F.X \to S$) are the hypotheses of [`chartSt5_holds`](/entry/chart-st5-holds/). In short, $S$ is a normalised blowup of a normal projective compactification $Z$ of $F.X$, with order $d\,\varphi(\beta)$ along each trait (`ValOn`).

A tautological chart $C$ (`Taut`) has: a Siegel family $F'$ of genus $h = g - r$ with a complete local ring $W$ of the $r$-fold power of its universal abelian scheme; forms $\varepsilon_1, \dots, \varepsilon_{m+N}$ on $\mathbb{Z}^r$, the first $m$ spanning a cone of $\varphi$; a completion $R$ of $W[x_1, \dots, x_{m+N}]$ with $t_k = x_k$; and degeneration data $Q$ over $R$ with $\tau = \prod_k x_k^{\,n \varepsilon_k}$ times $\tau_0(na, nb)$ (`DataFrom`).

**Theorem.** For each $x \in S$ there are a chart $C$, a semi-abelian $G_1$ over $R$, maps $y \colon \operatorname{Spec} \operatorname{Frac}(R) \to F.X$ and $\xi \colon \operatorname{Spec} R \to S$, and an identification $\alpha_1$ of the generic fibre of $G_1$ with a pullback by $y$, such that:

1. `C.IsFam`: $G_1$ is abelian exactly where $t_1 \cdots t_m$ is a unit, and $(G_1, y, \alpha_1)$ is a Mumford family for $Q$;
2. $j \circ y = \xi \circ \iota$, for the generic point $\iota$ of $\operatorname{Spec} R$;
3. $\xi$ maps the closed point to $x$.

The shape is that of the toroidal charts in Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter IV. We have not compared the side conditions.

## Proof

1. `ChartHit.setup`: $S$ is separated.
2. A trait $\xi_T \colon \operatorname{Spec} V \to S$ sends the closed point to $x$ and the generic point into $j(F.X)$.
3. A lemma that uses `IsPolFan`: after a finite extension $V \to V'$, the family has degeneration data from $(F', W)$, a basis $\varepsilon$ and values $s_k \in V'$.
4. `ChartHit.chart`: the map $W[x] \to V'$, $x_k \mapsto s_k$, factors through a local map $\theta \colon R \to V'$. This gives $C$.
5. `exists_mumford_family` builds $G_1$. Three more lemmas give its level structure, the map $y$ and `C.IsFam`.
6. `exists_ext_normalised_blowup`, which uses `NoSelfInt`: $j \circ y$ extends to $\xi \colon \operatorname{Spec} R \to S$.
7. $\xi \circ \operatorname{Spec} \theta$ and the trait over $V'$ agree generically. As $S$ is separated, they are equal (`ChartHit.away_hom_ext`), so $\xi$ sends the closed point to $x$.

## In the Lean code

The theorem is in [ExistsTautologicalChartAtSiegelBlowupPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTautologicalChartAtSiegelBlowupPoint.lean#L127). The `ChartHit` lemmas are in the same file. We read the statements of the other lemmas, not their proofs.

`NoSelfInt` is used only in step 6. `IsThetaCompact` asks for an $8 \times 8$ matrix with `IsE8`, which we have not unfolded.
