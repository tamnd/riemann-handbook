---
title: Good reduction from unramified torsion
decls:
  - UpperTheory.Lit.Nos.C6.hasGoodReduction_of_infinite_torsionUnramified
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good reduction from unramified torsion

This section proves the deep implication of [the criterion of Néron, Ogg and Shafarevich](/entry/nos-neron-ogg-shafarevich/): if the inertia group fixes the $m$-torsion of an abelian variety for infinitely many $m$ prime to the residue characteristic, then the abelian variety has good reduction. The proof passes to the inertia fixed field, where the unramified torsion points become rational. Over a strictly henselian base, many rational torsion points force good reduction by the theorem of Serre and Tate on the Néron model. Then [good reduction over the inertia fixed field](/entry/has-good-reduction-of-inertia-fixed/) descends to $R$.

### Rational torsion points over the inertia fixed field

Throughout, $R$ is a [[discrete valuation ring|MGM3CNJW9V]] with perfect residue field $k$ and fraction field $K$, $\Omega$ is a separable closure of $K$, and $V$ is a valuation ring of $\Omega$ above $R$. As in [the previous section](/entry/has-good-reduction-of-inertia-fixed/), $K' = \Omega^{I_V}$ is the inertia fixed field and $W = V \cap K'$.

**Definition 3.4.1 (Strictly henselian discrete valuation ring).** A discrete valuation ring $S$ with fraction field $L$ is *strictly henselian* if it is a henselian local ring and its residue field is algebraically closed.

See [henselian and strictly henselian rings](/learn/commutative-algebra/#henselian-and-strictly-henselian-rings) in Volume 1.

**Lemma 3.4.2 (The inertia fixed field is strictly henselian).** The ring $W$ is a strictly henselian discrete valuation ring with fraction field $K'$. There is a ring homomorphism $f : R \to W$ compatible with the inclusions in $\Omega$, and it sends each uniformizer of $R$ to a uniformizer of $W$.

Lean: `GlobalTheory.T.inertiaFixedField_valuationRing_strictlyHenselian`.

*Proof.* This is classical: $W$ is the strict henselization of $R$ with respect to $V$, and its residue field is the residue field of $V$, which is algebraically closed. The uniformizer statement is the unramifiedness of $K'/K$, as in the previous section. We do not unfold the proof. $\square$

**Lemma 3.4.3 (Points fixed by a subgroup).** Let $A$ be a scheme locally of finite type over a field $K$, $\Omega$ a field extension of $K$, $H$ a subgroup of $\operatorname{Aut}(\Omega/K)$, and $L = \Omega^H$. Let $x \in A(\Omega)$ with $\sigma x = x$ for every $\sigma \in H$. Then there is a unique $y \in A(L)$ whose image in $A(\Omega)$ is $x$.

Lean: `GlobalTheory.T.exists_fixedField_point_of_fixed_by_subgroup`.

*Proof.* Uniqueness holds because $\operatorname{Spec}\Omega \to \operatorname{Spec} L$ is an epimorphism of schemes, as $L \to \Omega$ is injective. For existence, let $U = \operatorname{Spec} B$ be an affine open containing the image of $x$, so $x$ is a $K$-homomorphism $\varphi : B \to \Omega$. The condition $\sigma x = x$ says $\sigma \circ \varphi = \varphi$, so the image of $\varphi$ lies in $L$, which gives $y$. $\square$

**Lemma 3.4.4 (Counting torsion over a fixed field).** Let $A$ be a group scheme locally of finite type over $K$, $H$ a subgroup of $\operatorname{Gal}(\Omega/K)$, $L = \Omega^H$, and $m \geq 0$. Assume that $\sigma x = x$ for every $\sigma \in H$ and every $x \in A(\Omega)$ with $mx = 0$. Then
$$
\#\{y \in A(L) : my = 0\} = \#\{x \in A(\Omega) : mx = 0\}.
$$

Lean: `UpperTheory.Lit.Nos.C6.card_torsion_fixedField`.

*Proof.* The $L$-points of $A$ are the same as the points of the base change $A \times_K L$ over $L$, and this identification respects the group laws. The map $A(L) \to A(\Omega)$ is a group homomorphism, and it is injective by the uniqueness in the previous lemma. It sends $m$-torsion to $m$-torsion. Each $x \in A(\Omega)$ with $mx = 0$ is fixed by $H$, so it is the image of some $y \in A(L)$, and $my$ maps to $mx = 0$, so $my = 0$ by injectivity. The map is therefore a bijection between the two sets of $m$-torsion points. $\square$

**Lemma 3.4.5 (The number of torsion points).** Let $A$ be an abelian variety of dimension $g$ over a field $K$, $\Omega$ a separably closed extension of $K$, and $m$ an integer with $m \neq 0$ in $K$. Then $A(\Omega)$ has exactly $m^{2g}$ points $x$ with $mx = 0$.

Lean: `GlobalTheory.T.card_abelianVariety_torsion_sepClosed`.

*Proof.* Multiplication by $m$ is an isogeny of degree $m^{2g}$, and it is étale when $m$ is invertible in $K$. So its kernel is a finite étale group scheme of order $m^{2g}$, and all its points are defined over the separably closed field $\Omega$ (Mumford, *Abelian Varieties*, §4). $\square$

### Good reduction over a strictly henselian base

**Theorem 3.4.6 (Good reduction from many rational torsion points).** Let $S$ be a strictly henselian discrete valuation ring with fraction field $L$ and residue field $\kappa$, and let $A$ be an abelian variety of dimension $g$ over $L$. Assume that the set of integers $m$ with $m \neq 0$ in $\kappa$ and with exactly $m^{2g}$ points $y \in A(L)$ with $my = 0$ is infinite. Then $A$ has good reduction over $S$.

Lean: `GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points`.

*Proof.* We recall the classical argument of Serre and Tate, §1, which is the subject of [its own entry](/entry/has-good-reduction-of-many-rational-torsion-points/). Let $N$ be the Néron model of $A$ over $S$. By the mapping property, $A(L) = N(S)$. For $m \neq 0$ in $\kappa$, the reduction map $N(S) \to N_\kappa(\kappa)$ is injective on $m$-torsion, since its kernel is a pro-$p$ group, or torsion free when $\kappa$ has characteristic $0$. Over the algebraically closed field $\kappa$, the identity component $N^0_\kappa$ is an extension of an abelian variety $B$ of dimension $a$ by $T \times U$, with $T$ a torus of dimension $t$ and $U$ unipotent of dimension $u$, and $a + t + u = g$. Its $m$-torsion has $m^{2a + t}$ points, and the component group $\Phi$ is finite, so
$$
m^{2g} \leq \#\Phi \cdot m^{2a+t}
$$
for infinitely many $m$. This forces $2a + t = 2g$, so $t = u = 0$ and $a = g$. Then $N^0_\kappa$ is an abelian variety and $N$ is an abelian scheme (Bosch, Lütkebohmert and Raynaud, *Néron Models*, §7.4). $\square$

**Theorem 3.4.7 (Unramified torsion gives good reduction).** Let $A$ be an abelian variety over $K$. Assume that the set of integers $m$ with $m \neq 0$ in $k$ such that the $m$-torsion of $A$ is unramified at $V$ is infinite. Then $A$ has good reduction over $R$.

Lean: `UpperTheory.Lit.Nos.C6.hasGoodReduction_of_infinite_torsionUnramified`.

*Proof.* By [good reduction over the inertia fixed field](/entry/has-good-reduction-of-inertia-fixed/), it suffices to show that $A' = A \times_K K'$ has good reduction over $W$. By the lemma on the inertia fixed field, $W$ is a strictly henselian discrete valuation ring with fraction field $K'$, and we have $f : R \to W$. Let $g$ be the dimension of $A$, so that $A$ is smooth of relative dimension $g$ over $K$. Then $A'$ is an abelian variety over $K'$, smooth of relative dimension $g$, since both properties are stable under base change.

We apply the theorem on many rational torsion points to $A'$ over $W$. Let $M$ be the infinite set of the hypothesis. We show that each $m \in M$ belongs to the set of that theorem, which is then infinite.

Let $m \in M$. Since $m \neq 0$ in $k$, the element $m$ of $R$ is not in the maximal ideal, so it is a unit of $R$. Its image $f(m) = m$ is then a unit of $W$, so $m \neq 0$ in the residue field of $W$. Also $m \neq 0$ in $K$, since $R \to K$ is injective.

Since the $m$-torsion of $A$ is unramified at $V$, every $x \in A(\Omega)$ with $mx = 0$ is fixed by $I_V$. By the lemma on counting torsion over a fixed field, with $H = I_V$ and $L = K'$,
$$
\begin{aligned}
\#\{y \in A'(K') : my = 0\} &= \#\{x \in A(\Omega) : mx = 0\} \\
&= m^{2g},
\end{aligned}
$$
where the last equality is the lemma on the number of torsion points, as $m \neq 0$ in $K$ and $\Omega$ is separably closed. So $m$ lies in the set of the theorem on many rational torsion points, and $A'$ has good reduction over $W$. $\square$

This completes the proof of $3 \Rightarrow 1$ in [the criterion of Néron, Ogg and Shafarevich](/entry/nos-neron-ogg-shafarevich/).

**Remark 3.4.8 (Formalization).** The theorem on many rational torsion points is a wrapper of `GlobalTheory.GoodRedTorsion.hasGoodReduction_of_torsion`, proved by a `first | exact` tactic ([HasGoodReductionOfManyRationalTorsionPointsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasGoodReductionOfManyRationalTorsionPointsStatement.lean#L11)); the Néron model argument above is the classical one, which we have not checked against that proof. The lemma on the inertia fixed field is likewise a wrapper of `GlobalTheory.InertiaFixedSH.inertiaFixed_strictlyHenselian`, with a raised heartbeat limit. Of the map $f : R \to W$ it gives, the proof uses only that it is a ring homomorphism: the compatibility with $\Omega$ and the statement on uniformizers are discarded ([HasGoodReductionOfInfiniteTorsionUnramified.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/HasGoodReductionOfInfiniteTorsionUnramified.lean#L95)). The lemma on counting torsion is proved in the same file ([line 50](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/HasGoodReductionOfInfiniteTorsionUnramified.lean#L50)), with the identification of points and its injectivity at lines 24 and 42; the definition of the strictly henselian condition also asks that $L$ be the fraction field of $S$.
