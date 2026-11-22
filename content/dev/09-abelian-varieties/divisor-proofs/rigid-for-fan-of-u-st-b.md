---
id: rigid-for-fan-of-u-st-b
title: Rigid toroidal charts from a normalized blow-up with separation
kind: theorem
decl: GlobalTheory.UChartJoin.rigidForFan_of_uStB
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.RigidBoundaryChartsForFanOfUnitarySeparation
covers: 1298
status: drafted
drafted_by: writer@claude
---
This theorem makes a smooth [toroidal compactification](/learn/geometry/#shimura-varieties-and-toroidal-compactifications) of a unitary moduli scheme, with boundary charts. Its input is a normalized blow-up $S \to Z$ of a projective compactification, with a separation property. Its [wrapper](/entry/rigid-boundary-charts-for-fan-of-unitary-separation/) feeds [`rigidForFan_holds`](/entry/rigid-for-fan-holds/).

## Statement

Fix a CM field $E$, a Hermitian $\mathcal{O}_E$-lattice $D$ of signature $(p, q)$ with $p + q \geq 1$, a level $l$, and a number field $F \subset \mathbb{C}$. Let $X_F$ be the unitary moduli scheme of $D$ at level $l$ over $F$. Let $\varphi$ be an invariant function on bilinear forms with the fan conditions `IsPolFan` and `NoSelfInt`, which we have not unfolded. A *model* is a normal scheme $Y$, flat and projective over $F$, with $X_F$ dense open, and a semi-abelian scheme with $\mathcal{O}_E$-action that extends the universal one and is abelian exactly over $X_F$. Let $\det\omega$ be the dual of the determinant of its Lie algebra.

**Theorem.** Suppose `UStB`: for all such data there are $Z$, $\mathcal{O}_Z(1)$, $N, d \geq 1$, an ideal sheaf $J$ on $Z$, a map $\pi \colon S \to Z$, an open immersion $j \colon X_F \to S$ and an effective Cartier divisor $B$ on $S$ with:

- $Z$ normal and projective over $F$, $X_F$ dense open in $Z$, $\mathcal{O}_Z(1)$ ample, and $\mathcal{O}_Z(1)$ pulls back to $(\det\omega)^N$ on each model over $Z$ where $\det\omega$ is a line bundle;
- degenerations with a PEL uniformization over local domains extend to $Z$;
- $J$ on $Z \setminus X_F$, of order $d\,\varphi(\beta)$ along each arc with monomial degeneration form $\beta$;
- $\pi$ a normalized blow-up of $J$, $\pi^{-1}(X_F) = j(X_F)$, $\mathcal{O}(-B) = \pi^{-1}J$, and $\pi^*\mathcal{O}_Z(k)(-B)$ ample for $k \geq k_0$;
- the separation property [`SepB`](/entry/u-pre-of-boundary-point-rigid/).

Then `RigidForFan` holds: for all such data there are a model $Y$, an effective Cartier divisor $B$ on $Y$ and $d, k \geq 1$ with:

- $Y$ smooth over $F$ of relative dimension $\dim D$;
- the boundary $Y \setminus X_F$ with [simple normal crossings](/learn/geometry/#line-bundles-and-divisors), and $B$ in the boundary;
- $(\det\omega)^k(-B)$ ample when $\det\omega$ is a line bundle;
- a chart at each boundary point, and a rigid chart at each closed boundary point.

A *chart* at $x$ is a map $\xi \colon \operatorname{Spec} k[[t_1, \dots, t_m, u_1, \dots, u_e]] \to Y$ through $x$, flat on local rings, with finite residue extension and $\mathfrak{m}_x$ generating the maximal ideal. In it the boundary is $t_1 \cdots t_m = 0$, the degeneration is monomial with forms $\gamma_i$ from a cone of $\varphi$, and $B = \prod t_i^{a_i}$ with $a_i = d\,\varphi(\gamma_i)$. It is *rigid* if each tangent vector at $x$ that kills all $t_i$, and along which the family is constant (`IsConstAlong`), is zero.

## Proof

1. [`T.exists_tripleChart_unitary_boundary_point`](/entry/exists-triple-chart-unitary-boundary-point/) gives a tautological chart (`UPre`) at each boundary point of $S$.
2. `T.unitary_compactification_isModel_of_charts` gives a model $Y$ and an isomorphism $\varepsilon \colon Y \cong S$ that is the identity on $X_F$.
3. `T.toroidalCompactification_smooth_snc_boundary` gives smoothness of $S$ and normal crossings of $S \setminus X_F$.
4. `UChartOf.charts_of_upre` turns each tautological chart into a chart and a rigid chart on $Y$.

Take $\varepsilon^*B$, the same $d$, and $k = Nk'$ with $k' = \max(k_0, 1)$. In the Picard group, $(\det\omega)^{Nk'}(-\varepsilon^*B)$ has the class of $\varepsilon^*(\pi^*\mathcal{O}_Z(k')(-B))$, which is ample.

## In the Lean code

The theorem is in [RigidBoundaryChartsForFanOfUnitarySeparation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanOfUnitarySeparation.lean#L21). `UStB` is in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L57), its first part `UPoinOnX` in [SpecializesGenericImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SpecializesGenericImage.lean#L153), and `RigChart.RigidForFan` in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L70). It also uses `SncIso.snc_vanishingIdeal_of_isIso` and the `CechPic` class lemmas.

The hypothesis resembles the blow-up construction in Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties* (2013). We have not checked this. `LogKSChart.RigidForFan` in [HasRigidChart.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidChart.lean#L67) has the same name and the same text, but its rigidity condition `IsRigid` uses `IsUnitPart` where this one uses `IsUnitTau`. So the two are different propositions.
