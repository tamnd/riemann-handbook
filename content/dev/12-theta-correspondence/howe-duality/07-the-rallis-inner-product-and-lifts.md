---
title: The Rallis inner product and lifts
decls:
  - GlobalTheory.IndexCount.indexSum_of_rank
  - GlobalTheory.IndexCount.indexSum_holds
  - GlobalTheory.RawLift.Eu.innerNe_main
  - GlobalTheory.RawLift.innerNe_spherical
  - GlobalTheory.RawLift.rawLift_main
  - GlobalTheory.DownLift.liftRows_injective_and_typeProperties_of_nonvanishing
  - GlobalTheory.T.liftInj_and_properties_of_rallis_of_nonVan
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Rallis inner product and lifts

This section studies the theta lift from forms on a definite unitary group $U(V)$ to [[cusp forms|A50Y012RBP]] on $U(W)$, in the stable range $2 \operatorname{rank} W + 5 \leq \operatorname{rank} V$. It first bounds the local lattice index sums that make an Euler product of local operators converge, then shows that the adjoint of a raw theta lift multiplies inner products by a nonzero scalar on each Hecke eigenpart, which is the shape of the [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula). The section ends with the properties of theta lifts that the [real lift splitting](/entry/at-real-lift-splits-locally/) of the [unitary hypotheses chapter](/proof/unitary-hypotheses/) uses: a good eigenvector whose theta lift vanishes is zero, and the Satake parameters correspond at the good places.

### The setting

Let $R$ be a real datum over a CM field: for each index $i$ it gives a positive definite Hermitian space $V_i$ and a Hermitian space $W_i$ with $\operatorname{rank} V_i = r + t$ and $\operatorname{rank} W_i = r$, where $r + 5 \leq t$. For each $i$ and each type $t'$ it gives a Weil representation $\omega$ of $U(V_i)(\mathbb{A}) \times U(W_i)(\mathbb{A})$, a finite-dimensional Hilbert space $H_V$ of theta vectors, a finite-dimensional Hilbert space $H_W$ embedded isometrically in the cusp forms $\mathcal{W}_i$ of a fixed level and central character, and a theta map $\theta \colon H_V \to \mathcal{W}_i$. A *raw lift* is a linear map $\vartheta \colon H_V \to H_W$ whose composite with the embedding is $\theta$. For a system $c$ of [[Hecke|5J2P2AGY4N]] eigenvalues, $H_W(c)$ is the part of $H_W$ that maps into the joint $c$-eigenspace. A *face* $F$ of the datum and a list of *laws* fix the levels, the group, the family, the models and the theta data; we keep them fixed throughout.

For a finite place $v$ of the base field put $q_v = N v$, and for $g \in U(W)(F_v)$ let $\operatorname{idx}(g)$ be the index of the lattice $g L_v$ relative to the standard lattice $L_v$, as in the [lattice index](/entry/witt-mod-pow/) of the first section.

**Definition 2.7.1.** Let $W$ be a Hermitian space and $n \geq 0$. We say that *index sums are small for $(W, n)$* if there is a summable function $s$ on the finite places with $s(v) < 1$ for all $v$ such that, for every finite place $v$ with its local idempotent, and every finite set $C$ of elements of $U(W)(F_v)$ in the support of the local test function, outside the spherical subgroup and lying in pairwise distinct cosets of it,
$$\sum_{g \in C} \operatorname{idx}(g)^{-n/2} \leq s(v).$$

### Index sums in the stable range

**Theorem 2.7.2 (Index sums from the rank).** Let $W$ be a Hermitian space and $n$ an integer with $2 \operatorname{rank} W + 5 \leq n$. Then index sums are small for $(W, n)$.

Lean: `GlobalTheory.IndexCount.indexSum_of_rank`

*Proof.* Let $r = \operatorname{rank} W$. Each $q_v$ is the norm of a nonzero prime, so $q_v \geq 2$. Put
$$z(v) = \Bigl(\prod_{i=0}^{r-1} \bigl(1 - q_v^{\,i - n/2}\bigr)^{-1}\Bigr)^2 - 1.$$
The hypothesis gives $n/2 \geq r + 5/2$, so every exponent $i - n/2$ is at most $-7/2$; a direct estimate of the product then gives $z(v) < 1$ and $z(v) \leq 16 q_v^{-3}$. Since $q_v \geq 2$ we also have $8 q_v^{-4} \leq 8 q_v^{-3}$ and $8 q_v^{-4} \leq 8 \cdot 2^{-4} = 1/2$. Take
$$s(v) = \max\bigl(z(v),\, 8 q_v^{-4}\bigr).$$
Then $0 \leq s(v) \leq 16 q_v^{-3}$, and $\sum_v q_v^{-3}$ converges, being dominated by the [[Dedekind zeta|KXS5DQDFYD]] value $\zeta_F(3)$; so $s$ is summable, and $s(v) < 1$. A finite place is either split, where the local idempotent decomposes, or inert. At a split place the index sum is bounded by $z(v)$: the sum over cosets is dominated by the square of a local zeta factor of $GL_r$, minus the term of the trivial coset. At an inert place the index sum is bounded by $8 q_v^{-4}$. In both cases it is at most $s(v)$. $\square$

**Theorem 2.7.3 (Index sums for a real datum).** For a real datum $R$ with a face $F$ satisfying the laws, and every index $i$, index sums are small for $(W_i, \operatorname{rank} V_i)$.

Lean: `GlobalTheory.IndexCount.indexSum_holds`

*Proof.* We have $2 \operatorname{rank} W_i + 5 = 2r + 5 \leq r + t = \operatorname{rank} V_i$ since $r + 5 \leq t$. Apply the previous theorem with $n = \operatorname{rank} V_i$. $\square$

### A scalar inner product on eigenparts

**Lemma 2.7.4.** Let $H$ be a complex inner product space, $P \subseteq H$ a subspace and $T$ an injective operator on $H$ such that every $y \in P$ satisfies $T y = z_y y$ for some $z_y \in \mathbb{C}$. Then there is $\lambda \neq 0$ with $T x = \lambda x$ for every $x \in P$.

Lean: `GlobalTheory.RawLift.Eu.scalar_of_eigen`

*Proof.* If $P = 0$ take $\lambda = 1$. Otherwise fix $x_0 \neq 0$ in $P$ with $T x_0 = \lambda x_0$; then $\lambda \neq 0$ since $T$ is injective. For $x \in P$ write $T x = \mu x$ and $T(x + x_0) = m (x + x_0)$, so $(m - \mu) x = (\lambda - m) x_0$. If $m = \mu$ then $(\lambda - m) x_0 = 0$, so $\mu = m = \lambda$. If $m \neq \mu$ then $x$ is a multiple of $x_0$, and $T x = \lambda x$. $\square$

**Theorem 2.7.5 (Inner products of a raw lift on eigenparts).** Let $R$, $F$ satisfy the laws, and fix $i$ and a type. Assume the finite sum formula for the raw lift, local multiplicity one, the level fixing of the theta vector, nonvanishing of the theta vector, small local coefficients, support of the bad places, the level product formula and the translation laws. Then for every raw lift $\vartheta$ and every eigensystem $c$ there is $\lambda \neq 0$ in $\mathbb{C}$ such that
$$\langle \vartheta^* x, \vartheta^* y \rangle = \lambda \langle x, y \rangle \qquad (x \in H_W(c),\ y \in H_W).$$

Lean: `GlobalTheory.RawLift.Eu.innerNe_main` (also `GlobalTheory.RawLift.innerNe_spherical`, a second name)

*Proof.* Choose a measure of covolume one on the space of the Weil representation; the matrix coefficient $c_v$ of the theta vector is then left invariant under the level group. The finite sum formula gives a constant $a > 0$ with
$$\langle \vartheta^* x, \vartheta^* y \rangle = a \sum_{\gamma} c_v(\gamma) \langle x, T_\gamma y \rangle,$$
the sum running over families of local cosets $\gamma = (\gamma_v)$ that are trivial at almost all $v$, and $T_\gamma$ the product of the corresponding right translations. At each place the sum over $\gamma_v$ defines a local operator $Z_v$, and by small local coefficients its part off the trivial coset has norm at most $s(v)$, with $s$ summable and $s(v) < 1$. Hence the Euler product $T = \prod_v Z_v$ converges, it is injective, and $\langle \vartheta^* x, \vartheta^* y \rangle = a \langle x, T y \rangle$. On the eigenpart $H_W(c)$ every local operator $Z_v$ acts by a scalar, since it is a combination of Hecke operators at the spherical place $v$; so every $y \in H_W(c)$ is an eigenvector of $T$. The lemma gives $l \neq 0$ with $T x = l x$ on $H_W(c)$, and then $\lambda = a \bar{l}$ works. $\square$

### Raw lifts

**Definition 2.7.6.** The *Rallis convergence* statement says: if $V$ is positive definite with $2 \operatorname{rank} W < \operatorname{rank} V$, then for theta vectors $f_1, f_2$ and smooth cusp forms $\varphi_1, \varphi_2$ on $U(W)$, the lifts
$$\theta(f, \varphi)(h) = \int_{[U(W)]} \overline{\theta_f(h, g)}\, \varphi(g)\, dg$$
exist, all the following integrals converge, and
$$\begin{aligned} \int_{[U(V)]} \overline{\theta(f_1, \varphi_1)}\, \theta(f_2, \varphi_2) &= \operatorname{vol}([U(V)]) \\ &\quad \cdot \int_{U(W)(\mathbb{A})} \langle \omega(g) f_2, f_1 \rangle \langle \varphi_1, R(g) \varphi_2 \rangle\, dg. \end{aligned}$$

This is the first identity of the Rallis inner product formula; see S. Rallis, *Injectivity properties of liftings associated to Weil representations*, Compositio Math. 52 (1984).

**Theorem 2.7.7 (Properties of raw lifts).** Assume rapid decay of cusp forms, the laws for $R$ and $F$, the full property of $R$ and Rallis convergence. Then:

1. for each $i$, the theta map at the base type maps the span of the image of the base theta vectors onto $\mathcal{W}_i$;
2. for all $i$ and types, every raw lift $\vartheta$ has an injective adjoint $\vartheta^*$;
3. for all $i$, types and eigensystems $c$ there is a real $\lambda > 0$ with $\langle \vartheta^* x, \vartheta^* y \rangle = \lambda \langle x, y \rangle$ for $x \in H_W(c)$ and all $y$;
4. the spaces $H_W(c)$ span $H_W$.

Lean: `GlobalTheory.RawLift.rawLift_main`

*Proof.* Seven local facts follow from the laws and the full property, one lemma each: the level product formula, the translation laws (which use rapid decay), level fixing, nonvanishing of the theta vector, local multiplicity one, vanishing of the local coefficients off the level at the bad places, and small local coefficients, which come from the vanishing at the bad places, a bound on the modulus and the index sums of the previous subsection. From Rallis convergence, together with the identity between the adjoint of the downward lift and the upward theta integral, one obtains the finite sum formula used above. Injectivity of the adjoint follows from it, which is (2). The previous theorem gives a nonzero complex $\lambda$; since the left side is a positive form when $x = y \neq 0$ and $\vartheta^*$ is injective, $\lambda$ is real and positive, which is (3). In finite dimension a map with injective adjoint is onto, and with the rational span given by the laws this gives (1). Statement (4) is a separate lemma on the eigenparts of the Hecke algebra, which also uses rapid decay. $\square$

### Theta lifts with nonvanishing integrals

Fix $R$ and $F$ as above, with two theta maps on $H_{V_i}$ for each $i$ and type: $\theta_G$ into a Hecke space $H_{W_i}$ and $\theta_F$ into automorphic forms on $W_i$. A vector $y$ is *good* if a fixed averaging over a finite group fixes it.

**Definition 2.7.8.** For an index $i$ and a type, consider the statements:

1. *nonvanishing*: a nonzero eigenvector whose eigensystem has a string has a theta vector $f$ with nonzero downward integral;
2. *good membership*: $e(\theta_G y) = \theta_F y$ for good $y$, with $e$ the inclusion of $H_{W_i}$;
3. *type nonvanishing*: a good eigenvector $y$ with a string and $\theta_G y = 0$ is zero;
4. *downward eigensystems*: for each eigensystem $s$ there is $c$ with $\theta_F(y)$ in the $c$-part for all $s$-eigenvectors $y$;
5. *unramified correspondence*: at each good place the Satake parameters of $s$ are those of $c$, after the fixed twists, together with a string;
6. *saturation*: for $s$ with a string there is $c$ such that each good $s$-eigenvector is $\theta_G^*(x)$ for some $x$ in the $c$-part.

*Lift injectivity* says: at the base type, if $x$ and $y$ have the same eigensystem, $\theta_G x \neq 0$, $y$ is good and $\theta_G y = 0$, then $y = 0$.

**Theorem 2.7.9 (Lifts with nonvanishing integrals).** Assume rapid decay of cusp forms, [unramified Howe duality](/entry/howe-unram-holds/), the given data for $R$ and $F$, the full property, Rallis convergence, and nonvanishing for all $i$ and types. Then lift injectivity holds, and for all $i$ and types so do type nonvanishing, good membership, downward eigensystems, the unramified correspondence at all places, and saturation.

Lean: `GlobalTheory.DownLift.liftRows_injective_and_typeProperties_of_nonvanishing` (also `GlobalTheory.T.liftInj_and_properties_of_rallis_of_nonVan`, a second name)

*Proof.* Six facts come from the given data and the full property: downward eigensystems and the [generic finite](/entry/gen-fin/) statement, both using unramified Howe duality; the [generic infinite](/entry/gen-inf/) statement; good membership; the absence of a level character on good vectors; and the existence of parameters, using rapid decay. The unramified correspondence at the places fixed by conjugation uses unramified Howe duality, and at the split places a separate argument; together they give it at all places.

For type nonvanishing, let $y \neq 0$ be good with $\theta_G y = 0$. By good membership $\theta_F y = 0$. By the generic infinite statement the downward integrals of $y$ against the theta vectors of finite type vanish; $y$ has no level character; and the generic finite statement then says $y$ has no nonzero downward integral at all, against nonvanishing. For lift injectivity, $\theta_G x \neq 0$ gives $\theta_F x \neq 0$, which by downward eigensystems, the unramified correspondence and the parameters gives a string for the eigensystem of $x$; type nonvanishing then gives $y = 0$.

For saturation, let $N$ be the space of good $s$-eigenvectors. The operator $\theta_G^* \theta_G$ preserves $N$, by unramified Howe duality, and $\theta_G$ is injective on $N$ by type nonvanishing. So $\theta_G^* \theta_G$ maps the finite-dimensional space $N$ onto itself, and each $y \in N$ is $\theta_G^*(x)$ with $x = \theta_G y'$. Downward eigensystems and good membership put $x$ in the $c$-part. The properties of raw lifts are also derived, for each $i$ and type, and passed to the saturation step. $\square$

**Remark 2.7.10 (Formalization).** The index sums are in [IndexSumOfRank.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IndexSumOfRank.lean#L37), with the version for a real datum at L71; that version takes the family, the field, the real datum, the face, the laws and the full property, and uses none of them except to name $W_i$ and $V_i$. The inner product theorem is in [InnerNeSpherical.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InnerNeSpherical.lean#L62), and its second name at L117 takes the full property without using it. The raw lift theorem is in [InnerPosOfInnerNe.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InnerPosOfInnerNe.lean#L47) and the lift theorem in [LiftRowsInjectiveAndTypePropertiesOfNonvanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftRowsInjectiveAndTypePropertiesOfNonvanishing.lean#L30). In the lift theorem, the injective adjoint from the raw lift theorem, the unramified correspondence and the parameters are passed to the saturation lemma, but that lemma discards these three arguments ([ExistsAdjointComp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsAdjointComp.lean#L313)); so Rallis convergence and the raw lift theorem do no logical work in the lift theorem, and Rallis convergence remains a hypothesis that could be removed. The second name of the lift theorem is a restatement proved by a `first | exact` tactic ([LiftRowsInjectiveAndTypePropertiesOfNonvanishingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftRowsInjectiveAndTypePropertiesOfNonvanishingStatement.lean#L17)).
