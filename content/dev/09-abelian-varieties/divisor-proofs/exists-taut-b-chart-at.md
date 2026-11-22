---
id: exists-taut-b-chart-at
title: A rigid tautological chart through each boundary point
kind: theorem
decl: GlobalTheory.UCanon.exists_tautB_chart_at
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPointRigidTautologicalChartUnitaryBoundary
covers: 1008
status: drafted
drafted_by: writer@claude
---
Let $S$ be a candidate compactification of a moduli scheme, with interior given by an open immersion $j$. At each boundary point $x$ of $S$, this theorem gives a formal power series chart through $x$ that carries a degenerating family with the rigidity conditions `IsTautB`. It proves [the statement form](/entry/exists-point-rigid-tautological-chart-unitary-boundary/), whose one user is [`uPre_of_boundary_pointRigid`](/entry/u-pre-of-boundary-point-rigid/).

## Statement

Fix a CM field $E$ with the data `Host E`, a hermitian datum $D$ of signature $(p, q)$ with $p + q \geq 1$, a level $l$, the moduli scheme $X^\circ$ of `Moduli D l`, and a coefficient field $F \subset \mathbb{C}$. Let $X^\circ_F$ be the base change of $X^\circ$ to $F$. Let $\varphi$ be an invariant function on forms over $\mathcal{O}_E$ with the fan conditions `IsPolFan` and `NoSelfInt` in rank $\min(p, q)$.

Let $i \colon X^\circ_F \to Z$ and $j \colon X^\circ_F \to S$ be open immersions, $\pi \colon S \to Z$ a map, $\mathcal{O}_Z$ a line bundle, $J$ an ideal sheaf on $Z$, $B$ effective Cartier data on $S$, and $N, d$ integers. Assume:

- `UPoinOnX`: $Z$ is projective and normal over $F$, $i$ is dense, $\mathcal{O}_Z$ is ample and pulls back to $(\det \omega)^{N}$ on each model over $Z$, families over local rings extend to $Z$, $\pi$ is a normalized blowup of $J$ with $j = \pi^{-1}(i)$ dense, $B$ is the pullback of $J$, valuation conditions `UValOn` hold, and $\pi^*\mathcal{O}_Z^{k}(-B)$ is ample for large $k$;
- `SepB`: a separation condition on monomial families through points of $S$.

**Theorem.** For each $x \in S$ outside the image of $j$ there are a field $k$, integers $m, e$, a monomial family $C$ over $R = k[[s_1, \dots, s_m, u_1, \dots, u_e]]$ and a map $\xi \colon \operatorname{Spec} R \to S$ such that

1. $C$ satisfies `IsTautB`;
2. the generic point of $C$ in $X^\circ_F$, followed by $j$, is $\operatorname{Spec} \operatorname{Frac}(R) \to \operatorname{Spec} R \xrightarrow{\xi} S$;
3. $\xi$ sends the closed point to $x$.

A monomial family (`MonoFam`) over a local domain $R$ is a semi-abelian scheme over $\operatorname{Spec} R$ with $\mathcal{O}_E$-action and cubical structure, a uniformization `PELUnif`, a generic point in $X^\circ_F$ that it classifies, elements $s_i$ of the maximal ideal, and forms $\delta_i$ in a cone of $\varphi$, with monomial periods (`IsMonomial`). `IsTautB` asks that the $s_i$ be the first $m$ variables, that $C$ be rigid to first order and at points, that the coordinates extend to a basis of balanced forms, and that $m + e + \operatorname{trdeg}_F k = \tfrac{[E:\mathbb{Q}]}{2} p q$. We have not unfolded `PELUnif`, `IsMonomial`, `OpenCls` or `Inj`.

## Proof

1. `exists_degenerating_monomialFamily_algClosed_residue` gives a local domain $V$ (with `Mum.Base` and an algebraically closed residue field), a monomial family over $V$ with nontrivial character lattice, and $\xi_V \colon \operatorname{Spec} V \to S$, compatible with $j$, that sends the closed point to $x$.
2. `exists_tautological_chart_versality` gives $k, m, e$, a family $C$ over $R$ with `IsTautB`, a map $\xi$ compatible with $j$, and a local homomorphism $\theta \colon R \to V$ with $\xi \circ \operatorname{Spec}\theta = \xi_V$.
3. A local homomorphism sends the closed point to the closed point (`IsLocalRing.comap_closedPoint`). So $\xi$ sends the closed point to $\xi_V(\text{closed point}) = x$.

## In the Lean code

The theorem is in [ExistsPointRigidTautologicalChartUnitaryBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPointRigidTautologicalChartUnitaryBoundary.lean#L13). It calls:

- `GlobalTheory.T.exists_degenerating_monomialFamily_algClosed_residue`, a statement form of `UChartGeo.exists_monoFam_algClosed`;
- `GlobalTheory.T.exists_tautological_chart_versality`, a statement form of `UCanon.exists_taut_through`;
- `IsLocalRing.comap_closedPoint` from Mathlib.

The conclusion drops $\theta$, so it does not state that the chart is versal.
