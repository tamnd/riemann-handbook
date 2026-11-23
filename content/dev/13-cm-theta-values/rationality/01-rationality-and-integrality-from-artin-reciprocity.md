---
title: Rationality and integrality from Artin reciprocity
decls:
  - GlobalTheory.seriesRatS_and_serInt_of_globalArtin
  - GlobalTheory.T.thetaSeries_integral_uniform_prime_power
  - GlobalTheory.serInt_outright
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rationality and integrality from Artin reciprocity

This section states the two properties of theta series that the chapter is about, and proves that they hold. The first property is rationality: after a fixed phase, a theta series of a unitary dual pair is a modular form defined over the coefficient field of each good cover of the Shimura variety. The second property is integrality: at each prime $l$, a fixed power of $l$ makes the series integral at all places above $l$, uniformly over a tower of covers, and integral forms descend to the base of the tower. Rationality needs global Artin reciprocity. Integrality needs no hypothesis; its proof is the content of Sections 2 and 3. The pair of properties is an input of [the step on the nonempty hypotheses](/step/nonempty-hyps/).

### The setting

Fix a CM field $E$ with totally real subfield $F$, as in [Hecke characters](/learn/class-field-theory/#hecke-characters). A datum of the development fixes, for each index $i$ in a finite range, two Hermitian spaces $V_i$ and $W_i$ over $E$, the [Weil representation](/learn/theta/#the-weil-representation) $\omega_i$ of the adelic points of the [dual pair](/learn/theta/#reductive-dual-pairs) $(\mathrm{U}(V_i), \mathrm{U}(W_i))$, attached to an additive character $\psi$ and to two splitting characters, and a vacuum vector $f_0$ at the archimedean places. It also fixes a family of Shimura varieties for $\mathrm{U}(W_i)$ with their levels and coefficient fields (see [Shimura varieties and toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)). For a Schwartz function $f$, an element $s$ of the adelic group of $\mathrm{U}(V_i)$ with trivial archimedean component, and a vector $w$ of a space of harmonic polynomials, we write
$$\theta(s, g; f, w)$$
for the theta series of the [theta kernel](/learn/theta/#theta-kernels) of $\omega_i$ at $(s, g)$, with $f$ at the finite places and the harmonic vector $w$ at the archimedean places. It is a function of $g$ in the adelic group of $\mathrm{U}(W_i)$. A *standing law* of the datum is one of the conditions that tie the Weil representation, the models of the Shimura varieties, the frames and the lowest weight vectors $u$ together. All results below assume these laws.

A *cover* $C$ of the Shimura variety at index $i$ is a moduli space of a level $M\,p_d$, where $M$ is the fixed level and $p_d$ is an auxiliary level. It comes with a number field $F_C$ and an embedding $\sigma_C : F_C \to \mathbb{C}$. For a prime $l$, the cover is a *tower cover at $l$* if it is uniformized, $p_d$ is squarefree, and $p_d$ is prime to $l$ and to the product of the fixed bad numbers of the datum.

**Definition 3.1.1 (Rationality of theta series).** The datum has *rational theta series* if the following holds for every index $i$, every coefficient tie and every family $u$ of lowest weight vectors equal to the fixed vacuum. There is a complex number $\varphi$ with $|\varphi| = 1$ such that, for every good cover $C$, the series $\varphi\,\theta(s, g; f, w)$, its products with the determinant twists of $C$, and the same series for every Weil representation with the same splitting characters, are forms defined over $F_C$. Here $f$ runs over the level functions with values in $\sigma_C(F_C)$, and $w$ over the harmonic vectors with coefficients in $\sigma_C(F_C)$.

**Definition 3.1.2 (Integrality of theta series).** The datum has *integral theta series* if, for every index $i$, the following two conditions hold.

1. For every lowest weight family $u$ equal to the vacuum and every coefficient map $c_0$, there is $\varphi$ with $|\varphi| = 1$ with this property. For every prime $l$, every $s$ with trivial archimedean component, and every finitely generated $\mathbb{Z}$-lattice $\Lambda$ of coefficient vectors, there is $c \in \mathbb{N}$ such that the following holds. Let $C$ be a tower cover at $l$ that is pinned at the weights and whose field contains the coefficients of $\Lambda$ and a ray class field of level $M p_d$. Let $S$ be a set of places of $F_C$ above $l$, let $\xi$ be a twist character of conductor dividing $p_d$, and let $f$ be a level function whose values are integral at $S$. Then for every $v \in \Lambda$ there is a form $\phi$ in the $S$-integral forms of $C$ with
$$\phi(g) = l^{c}\,\varphi\,\xi(\det g)\,\theta(s, g; f, c_0(v)) \quad \text{for all } g.$$
2. For every prime $l$, every tower cover $C$ at $l$ that is pinned, and every set $S$ of places above $l$ at which $C$ is unramified, every $S$-integral form $\phi$ that is right invariant under the fixed compact open subgroup is a finite sum $\sum_a x_a \psi_a$, with $x_a$ integral at $S$ and $\psi_a$ integral forms of the base at the places below $S$.

The constant $c$ in condition 1 depends on $l$, $s$ and $\Lambda$, but not on the cover. This is the uniformity in the tower.

### Artin reciprocity

**Theorem 3.1.3 (Global Artin reciprocity).** Let $K$ be a number field, $\mathbb{A}_K^\times$ its idele group and $K^{\mathrm{ab}}$ its maximal abelian extension. There is a continuous surjective homomorphism $\mathbb{A}_K^\times \to \mathrm{Gal}(K^{\mathrm{ab}}/K)$ whose kernel is the closure of $K^\times$ times the connected component of the identity at the infinite places. At each finite place $v$ it sends the local units onto the inertia group of $v$, a uniformizer to a Frobenius element at $v$, and $K_v^\times$ into the decomposition group of $v$.

This is the main theorem of [global class field theory](/learn/class-field-theory/#global-class-field-theory) (Neukirch, *Algebraic Number Theory*, Chapter VI). The development takes it as a published input. It is used through ray class fields: for each nonzero modulus $\mathfrak{m}$ of $K$ there is an abelian extension $L/K$, unramified outside $\mathfrak{m}$, with an isomorphism from the ray class group modulo $\mathfrak{m}$ onto $\mathrm{Gal}(L/K)$ that sends the class of a prime $\mathfrak{p} \nmid \mathfrak{m}$ to its Frobenius element.

**Theorem 3.1.4 (Rationality and integrality).** If global Artin reciprocity holds, then every datum has rational theta series and integral theta series.

Lean: `GlobalTheory.seriesRatS_and_serInt_of_globalArtin`

*Proof.* Artin reciprocity gives the ray class fields of every number field, in the form above. The development proves that the untwisted theta series are rational on good covers; this needs no hypothesis. It also proves that rationality of the untwisted series, together with the ray class fields, gives the rationality of the series and of its products with the determinant twists. The ray class fields enter through the field condition on a good cover, which contains a ray class field of its level. This gives rational theta series. Integral theta series is [the theorem on integrality](/entry/ser-int-outright/) below, which needs no hypothesis. $\square$

**Theorem 3.1.5 (Integrality).** Every datum has integral theta series.

Lean: `GlobalTheory.serInt_outright` (also `GlobalTheory.T.thetaSeries_integral_uniform_prime_power`, a second name).

*Proof.* Fix the datum and the index $i$. Condition 2 is the unramified descent of integral forms through a tower cover, which the development proves for every datum that satisfies the standing laws. We prove condition 1.

Fix $u$ and $c_0$. The standing laws make the Weil representation, its lattices and the vacuum vector into a vacuum pair in the sense of Section 2, with $W_i$ of odd rank. Two identities fix the phase. The constants of the core datum equal the vacuum identity up to a phase $\varphi_1$, and the harmonic map sends the extremal vector to $\kappa$ times the letter polynomial, with $|\kappa| = 1$. Put $\varphi = (\kappa\,\varphi_1)^{-1}$.

Now fix $l$, $s$ and $\Lambda$. The harmonic polynomials $c_0(v)$ for $v \in \Lambda$ have coefficients with bounded denominators, since $\Lambda$ is finitely generated: there is $c_1$ such that $l^{c_1}$ times each coefficient is integral at every place above $l$. [The bound for theta series](/entry/series-bound/) gives $c_2$, which does not depend on the auxiliary level. Put $c = c_1 + c_2$.

Let $C$, $S$, $\xi$ and $f$ be as in condition 1. The uniformization of $C$ is a dictionary between the adelic group and the points of $C$, and it is compatible with the frames. The level of $C$ is $M p_d$ with $p_d$ prime to $l$, so the level is good at $l$. For each place $\lambda \in S$, take the subring $O$ of $\mathbb{C}$ of elements that are integral at $\lambda$ under $\sigma_C$. The level function and the scaled coefficients have values in $O$. The bound for theta series, applied at $\lambda$, writes $l^{c}\,\varphi\,\theta(s, g; f, c_0(v))$ as an $O$-combination of $\lambda$-integral forms of $C$. The twist $\xi(\det g)$ is a root of unity in the field of $C$, so it does not change integrality. So the function lies in the $O$-span of the $\lambda$-integral forms for every $\lambda \in S$, and the field conditions on $C$ make it a form defined over $F_C$. A form that is $\lambda$-integral for each $\lambda \in S$ is $S$-integral. $\square$

**Remark 3.1.6 (Formalization).** The rationality half of [SeriesRationalIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SeriesRationalIntegral.lean#L12) uses `GlobalArtinReciprocity.rayClassFieldSt`; the integrality half is the term `T.thetaSeries_integral_uniform_prime_power`, which does not use the hypothesis. The callers of the conjunction ([OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L34) and [PublishedInputsImplyGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PublishedInputsImplyGalois.lean#L44)) take only the rationality half. The properties are `SeriesRatS` ([SeriesRatSOf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SeriesRatSOf.lean#L14)) and `SerInt`, the conjunction of `SerIntAt` and `DescIntAt` ([TwistSeries.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/TwistSeries.lean#L88)). The hypothesis `GlobalArtinReciprocity` is in [ExistsUniqueHcharOfFiniteOrder.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean#L70). The proof of condition 1 is `LevelSeries.serIntAt_record` ([SerIntAtOfSeriesRat.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SerIntAtOfSeriesRat.lean#L274)), with $c_1$ from `exists_denom` and $c_2$ from `series_bound`; condition 2 is `T.unramified_descent_integral_forms_tower_cover`. The second name is proved by the tactic `first | exact @… | …`, as for every second name in this chapter. The files sit in a folder named after the Iwasawa decomposition, which does not occur in the statements. We have not unfolded `thetaKO`, `GoodCover`, `IsRat` or `intForms`.
