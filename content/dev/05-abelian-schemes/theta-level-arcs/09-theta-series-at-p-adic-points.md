---
title: Theta series at p-adic points
decls:
  - GlobalTheory.T.theta_series_at_point_integral_of_period_valuation
  - GlobalTheory.ZH.SeriesAtPoint.main
  - GlobalTheory.T.uniformisedModel_adaptedBasis_is_modelWithSeries
  - GlobalTheory.ZH.utest_nonempty_mod
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta series at p-adic points

The second part of this chapter extends an abelian scheme with a theta structure over an open set of a projective model to a semi-abelian scheme over the whole model. Its local input is the behaviour of the theta coordinates at $p$-adic points. In this section we prove that, at a point of a uniformised semi-abelian scheme over $\overline{\mathbb{Q}}_p$, the theta coordinates are sums of series whose terms have sizes given by the quadratic form of the degeneration and by a linear form $\nu$, the *period valuation* of the point. When $\nu$ comes from the lattice, the point is integral. With this we prove that a uniformised test with an adapted basis is a model with series, which is the local input of [the geometric tests](/entry/has-geo-of-has-u/). For the background see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) and [the algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions) in Volume 1.

### Theta systems and uniformised tests

Let $o \subset \Omega$ be an *arithmetic base*: $o$ is a Dedekind domain of finite type over $\mathbb{Z}$, $\Omega$ is a field of characteristic $0$, and $o \to \Omega$ is injective. Write $\overline{\mathbb{Q}}_p$ for the algebraic closure of $\mathbb{Q}_p$ with its absolute value, $\mathcal{O}_p$ for its valuation ring, and $\eta : \operatorname{Spec} \overline{\mathbb{Q}}_p \to \operatorname{Spec} \mathcal{O}_p$ for the generic point.

**Definition 6.9.1 (Theta system).** A *theta system* $S$ over $(o, \Omega)$ consists of integers $g$, $N \geq 2$ and $r \geq 1$ with $rN$ a unit in $o$, a primitive root of unity $\zeta \in o$ of order $(rN)^2$, a finite nonempty set $J$, a projective representation $\rho_S$ of $\Gamma = (\mathbb{Z}/rN)^{2g}$ on $o^J$ with multipliers powers of $\zeta$, theta values $\vartheta : \Gamma \to \Omega$ and values $\operatorname{ev} : \Gamma \times J \to \Omega$, and a finitely generated $o$-subalgebra $R$ of $\Omega$ with fraction field $\Omega$ that contains all these values, such that the support of $\vartheta$ generates $\Gamma$.

Lean: `GlobalTheory.ZH.ThetaSys`.

A *realisation* $\rho$ of $S$ is a polarized abelian scheme $(A, L)$ of relative dimension $g$ over $\operatorname{Spec} R$, an odd prime $n$ and integers $k \geq 2$, $j \geq 1$ with $N = n^{2k}$ and $r = n^j$, sections $P_a$ of order dividing $rN$ for $a \in \Gamma$ that give all the $rN$-torsion with the standard Weil pairing, a section $\theta_1$ of $L$ with values $\vartheta(a)$ at the $P_a$, and a basis $(s_i)_{i \in J}$ of the sections of $L^N$ with values $\operatorname{ev}$ on which the theta group acts by $\rho_S$. The Lean name is `GlobalTheory.ZH.ThetaSys.Real`.

**Definition 6.9.2 (Uniformised test).** Let $p$ be a prime and $y_0 : R \to \overline{\mathbb{Q}}_p$. A *uniformised test* $u$ of $\rho$ at $(p, y_0)$ consists of a complete discrete valuation ring $V$ with a map $\operatorname{Frac} V \to \overline{\mathbb{Q}}_p$ under which $V$ is exactly the set of elements of norm at most $1$, a factorisation of $y_0$ through $\operatorname{Frac} V$, the pullback $A_u$ of $A$ to $\operatorname{Frac} V$, a semi-abelian scheme $G$ over $V$, degeneration data $D$ over $V$ with character lattice $\mathsf{X}$, and a uniformisation of $A_u$ by $D$ with $G$ as its group.

Lean: `GlobalTheory.ZH.ThetaSys.Real.UTest`.

We write $j_u : V \to \mathcal{O}_p$ for the induced map and $H_k$ for the line bundle $L^k$ on $G$ given by the uniformisation.

A *labelling* $l$ of $u$ is a positive real quadratic form $q$ on $\mathsf{X}$ with $|\psi(\chi)| = e^{-q(\chi)}$ in $\overline{\mathbb{Q}}_p$, together with a surjection $\Gamma \to \mathsf{X}/rN\mathsf{X}$ that sends each $a$ to the class of the point of $D$ above $P_a$, whose kernel is the set of $a$ for which $P_a$ is integral over $V$, and with weights on the orthogonal of this kernel. The Lean name is `GlobalTheory.ZH.ThetaSys.Real.UTest.Lab`.

**Definition 6.9.3 (Adapted basis).** Let $l$ be a labelling and $k \geq 1$. A family $(\sigma_i)_{i \in J}$ of sections of $H_k$ with classes $\mathrm{cls}(i) \in \mathsf{X}$ and Fourier coefficients $f_i(\alpha)$ is an *adapted basis* if: each $\mathrm{cls}(i)$ is a shortest representative of its class modulo $k$ for $q$; classes that agree modulo $k$ are equal; every class of $\mathsf{X}/k\mathsf{X}$ is hit; $\sigma_i$ expands as $f_i$ at every level of the uniformisation; each $f_i$ comes from a family over $\operatorname{Frac} V$; $f_i(\alpha) = 0$ unless $\alpha \equiv \mathrm{cls}(i)$ modulo $k$; and for each $i_0$ the coefficients $f_i(\mathrm{cls}(i_0))$ with $\mathrm{cls}(i) = \mathrm{cls}(i_0)$ form a basis.

Lean: `GlobalTheory.ZH.ThetaSys.Real.UTest.Basis`.

The *coordinates* of a point $x$ for a family $\sigma$ are the values $w_i = c \cdot \sigma_i(x)$, read in a chart of the line bundle that contains $x$, for some unit $c$. They are defined up to a common unit.

**Definition 6.9.4 (Series with period valuation).** Let $w \in \overline{\mathbb{Q}}_p^J$ and let $\nu : \mathsf{X} \to \mathbb{R}$ be additive. We say that $w$ is a *series with period valuation $\nu$* for $(q, N, \mathrm{cls})$ if there are terms $t(\alpha, i)$ and $\kappa > 0$ such that $\sum_\alpha t(\alpha, i) = w_i$ for every $i$, $t(\alpha, i) \neq 0$ only when $\alpha \equiv \mathrm{cls}(i)$ modulo $N$, and for every $\alpha$
$$|t(\alpha, i)| \leq \kappa \exp\Bigl(-\frac{q(\alpha) - q(\mathrm{cls}(i))}{N} - \nu(\alpha)\Bigr)$$
for all $i$, with equality for some $i$.

Lean: `GlobalTheory.ZH.Ser`.

### Inputs

All the inputs assume the five bundles of laws and are stated for an arithmetic base, a theta system $S$, a realisation $\rho$ and a uniformised test $u$ at $(p, y_0)$ with labelling $l$. Their Lean proofs are elsewhere in the development. The second input in the list below also assumes the torsion statement for uniformisations, which says that the torsion points of the generic fibre of a uniformisation over a complete discrete valuation ring are the images of the points of level $k$ of the degeneration data, with the same equivalence, addition and Weil pairing.

**Theorem 6.9.5 (Dimensions).** $A_u$ has dimension $g$, the abelian part of $D$ has dimension $g - \operatorname{rk} \mathsf{X}$, $G$ is smooth of relative dimension $g$, $N \geq 4$, and the special fibre of $G$ is an extension of an abelian variety by a split torus.

Lean: `GlobalTheory.T.uniformisedTest_dimensions_and_split_fibre`.

**Theorem 6.9.6 (Torus parameters).** Every point $a$ of the generic fibre of $G$ over $\overline{\mathbb{Q}}_p$ has a *parameter*: a point $g$ of the torus extension of $D$ over $\overline{\mathbb{Q}}_p$ such that, for every generating frame $w$ at $g$, the Fourier sums of every expansion of a section of $H_N$ at $g$ equal a fixed nonzero constant times the value of the section at $a$.

Lean: `GlobalTheory.T.exists_torusExtension_parameter_genericFibrePoint`.

**Theorem 6.9.7 (Valuations of torus points).** Each point $g$ of the torus extension has a unique additive $\nu_g : \mathsf{X} \to \mathbb{R}$ with $|s_g(\chi)| = e^{-\nu_g(\chi)}$ in good charts. It is additive in $g$, and the point $\iota(y)$ has $\nu = q(y, \cdot)$, the polar form of $q$ at $y$.

Lean: `GlobalTheory.T.valuations_torusExtension_points`.

**Theorem 6.9.8 (Separation).** If $k \geq 4$ and $\sigma$ is an adapted basis of level $k$, then the coordinates of a point of the generic fibre are nonzero, two points with the same coordinates are equal, and every point of $G$ over $\eta$ and $j_u$ is a point of the generic fibre.

Lean: `GlobalTheory.T.crd_ne_zero_injective_surjective_of_basis`.

**Theorem 6.9.9 (Sizes of the Fourier terms).** If $k \geq 4$, $\sigma$ is an adapted basis of level $k$, $g$ is a torus point with valuation $\nu$ and $w$ is a generating frame at $g$, then there is $\kappa > 0$ such that the Fourier terms of $\sigma_i$ at $(g, w)$ vanish off $\mathrm{cls}(i) + k\mathsf{X}$ and satisfy the bound of a series with period valuation $\nu$, with equality for some $i$.

Lean: `GlobalTheory.T.adapted_basis_fourier_term_sizes_torusPoint`.

**Theorem 6.9.10 (Integral points).** A torus point $g$ with $\nu_g = 0$ is the level of an $\mathcal{O}_p$-point $c$ of $G$ over $j_u$. If $c$ is such a point and $\eta^* c$ is a point $a$ of the generic fibre, then $g$ is a parameter of $a$ at every level.

Lean: `GlobalTheory.T.exists_integralPoint_of_torusPoint_valuationZero` (also `GlobalTheory.T.torusCoord_unit_and_section_eq_expansion`, the second statement).

**Theorem 6.9.11 (Translation by the lattice).** The torus points form a group that contains $\iota(\mathsf{X})$. If $g' = g + \iota(y)$, then $g$ is a parameter of $a$ at level $k \geq 1$ if and only if $g'$ is.

Lean: `GlobalTheory.T.seriesProportional_add_iota_iff` (also `GlobalTheory.ZH.gt_add_iota_sub_exist`, the group structure).

### Theta series at a point

**Theorem 6.9.12 (Theta series at a point).** Assume the five bundles of laws and the torsion statement for uniformisations. Let $u$ be a uniformised test of $\rho$ at $(p, y_0)$ with labelling $l$, and let $\sigma$ be an adapted basis of level $N$ with classes $\mathrm{cls}$. Let $a$ be a point of $G$ over $\overline{\mathbb{Q}}_p$ that lies over $\eta$ and $j_u$, with coordinates $w$ for $\sigma$. Then there is an additive $\nu : \mathsf{X} \to \mathbb{R}$ such that $w$ is a series with period valuation $\nu$ for $(q, N, \mathrm{cls})$. If $\nu = q(m, \cdot)$ for some $m \in \mathsf{X}$, then $a = \eta^* c$ for an $\mathcal{O}_p$-point $c$ of $G$ over $j_u$.

Lean: `GlobalTheory.T.theta_series_at_point_integral_of_period_valuation` (also `GlobalTheory.ZH.SeriesAtPoint.main`, a second name).

*Proof.* By the theorem on dimensions, $N \geq 4$. By separation, $a$ is a point of the generic fibre. Let $g$ be a parameter of $a$ and let $\nu = \nu_g$. Each $f_i$ comes from a family over $\operatorname{Frac} V$, and so gives a family $s_i$ over $\overline{\mathbb{Q}}_p$ by base change. Choose a generating frame $w_0$ at $g$; it exists since a line bundle on the spectrum of a local ring has a generator. Since $g$ is a parameter, there is $\kappa_0 \neq 0$ with $\sum_\alpha \operatorname{coef}(s_i, g, w_0, \alpha) = \kappa_0 w_i$ for all $i$.

*The series.* Put $t(\alpha, i) = \kappa_0^{-1} \operatorname{coef}(s_i, g, w_0, \alpha)$. Then $\sum_\alpha t(\alpha, i) = w_i$. By the theorem on the sizes of the Fourier terms, with its constant $\kappa$, the terms vanish off $\mathrm{cls}(i) + N\mathsf{X}$ and satisfy the bound with constant $|\kappa_0|^{-1} \kappa$, with equality for some $i$. So $w$ is a series with period valuation $\nu$.

*Integrality.* Assume $\nu = q(m, \cdot)$. The point $h = \iota(m)$ has valuation $q(m, \cdot)$, and there is $g'$ with $g = g' + h$. By additivity, $\nu = \nu_{g'} + q(m, \cdot)$, so $\nu_{g'} = 0$. By the theorem on integral points, there is an $\mathcal{O}_p$-point $c$ of $G$ over $j_u$ with level $g'$. By separation, $\eta^* c$ is a point $a'$ of the generic fibre, and $g'$ is a parameter of $a'$. By translation by the lattice, $g$ is also a parameter of $a'$. Let $w'$ be coordinates of $a'$. The Fourier sums of $s_i$ at $(g, w_0)$ are $\kappa_0 w_i$ and also $\kappa'_0 w'_i$ for some $\kappa'_0 \neq 0$. So $a$ and $a'$ have proportional coordinates, and by separation $a = a' = \eta^* c$. $\square$

### Models with series

**Definition 6.9.13 (Model with series).** Let $\sigma$ be a family of sections of $H_N$ with classes $\mathrm{cls}$. A *model with series* for $(u, \sigma)$ consists of: $G$ smooth of relative dimension $g$ and $H_N$ a line bundle; a split extension $\Phi$ over the residue field $\bar{k}$ of $\mathcal{O}_p$ with a cartesian map to the geometric special fibre of $G$; an isomorphism of its character lattice with $\mathsf{X}$; sections $F_i$ of the line bundle of $\Phi$ that satisfy the good reduction condition for $(q, N, \mathrm{cls})$; a polarization of $\Phi$ with $\dim + \operatorname{rk} = g$; the statement that coordinates for $F$ at a point of $\Phi$ are coordinates for $\sigma$ at its image; and the conclusion of the theorem on theta series at a point.

Lean: `GlobalTheory.ZH.Mod`.

We use two more inputs. The first is that a uniformised test has, for each $N \geq 1$, a geometric special fibre: a split extension $\Phi$ with a cartesian map to $G$, a polarization of the right dimension, and a reduction of sections under which every family expanding at level $0$ gives sections $F$ of $\Phi$ whose coordinates are coordinates of $\sigma$ (Lean: `GlobalTheory.T.nonempty_geometric_special_fibre_uniformised`). The second is the good reduction condition for the reductions of an adapted basis (Lean: `GlobalTheory.T.good_reduction_adapted_basis`).

**Theorem 6.9.14 (Uniformised tests are models with series).** Assume the five bundles of laws and the torsion statement for uniformisations. Let $u$ be a uniformised test with labelling $l$ and let $\sigma$ be an adapted basis of level $N$ with classes $\mathrm{cls}$. Then $(u, \sigma)$ has a model with series.

Lean: `GlobalTheory.T.uniformisedModel_adaptedBasis_is_modelWithSeries` (also `GlobalTheory.ZH.utest_nonempty_mod`, a second name).

*Proof.* The theorem on dimensions gives the smoothness of $G$ and $N \geq 4$, so $N \geq 1$. Take a geometric special fibre $\Phi$ for $N$. Since each $\sigma_i$ expands as $f_i$ at level $0$, the reduction gives sections $F_i$ of $\Phi$ whose coordinates are coordinates of $\sigma$. The theorem on good reduction gives the good reduction condition for $F$. The dimension of the polarization of $\Phi$ is the dimension of the abelian part of $D$, and the rank of the character lattice of $\Phi$ is $\operatorname{rk} \mathsf{X}$, so their sum is $g$ by the theorem on dimensions. The last field is the theorem on theta series at a point. $\square$

**Remark 6.9.15 (Formalization).** The theta series at a point are proved in [ThetaSeriesAtPointIntegralOfPeriodValuation.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ThetaSeriesAtPointIntegralOfPeriodValuation.lean#L99), with the local lemmas `secLin_of_secScal`, `exists_pull`, `exists_isGen`, `exists_frm` and `hasSum_crd` before it. The models with series are built in [UniformisedModelAdaptedBasisIsModelWithSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/UniformisedModelAdaptedBasisIsModelWithSeries.lean#L20). The torsion statement is used only through the theorem on torus parameters. At line 22 of the second file the first and the last parts of the theorem on dimensions are dropped; the split special fibre is not used, since the geometric special fibre is taken from another input. In the first proof the nonvanishing of the coordinates is dropped, and so is the first part of the theorem on valuations of torus points, on good charts. The hypothesis that $o \subset \Omega$ is an arithmetic base is only passed on to the inputs. We did not unfold the torus extension points `GtPtF`, the parameters `ParAt`, the valuations `GtN`, the levels `Lev`, `FibOf`, `Good` or the degeneration data.
