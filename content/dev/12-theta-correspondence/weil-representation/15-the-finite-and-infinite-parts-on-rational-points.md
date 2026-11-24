---
title: The finite and infinite parts on rational points
decls:
  - GlobalTheory.RatAut.scalar_const
  - GlobalTheory.RatAut.isScalar_one_of_comm
  - GlobalTheory.RatAut.of_oi_eq_subst
  - GlobalTheory.RatAut.of_oi_apply_zero
  - GlobalTheory.RatAut.automorphy_target
  - GlobalTheory.T.thetaDistribution_invariant_rationalTarget
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The finite and infinite parts on rational points

The adelic Weil representation of the next section is built as a product $\omega_{\mathrm f}\,\omega_\infty$ of a finite part and an infinite part, each defined on theta functions by its own model. This section proves that on a rational point $(\gamma, \gamma')$ the product acts on theta functions by the substitution $f \mapsto f(\gamma'^{-1}\, \cdot\, \gamma)$, with no scalar factor. Since the substitution fixes $0$, the theta distribution $f \mapsto f(0)$ is invariant under rational points. This is the automorphy of the Weil datum, used in the [theorem on the global Weil datum](/entry/exists-weil-datum-eta-tilde/). It is a second proof of Weil's invariance, which [section 08](/entry/weil-rep-rational-darboux-fixes-theta-distribution/) proves by doubling. Here the proof compares the scalar by which a rational point acts with the explicit vacuum characters of the two parts.

### The setting

Let $F$ be a totally real number field and $E/F$ a CM extension with conjugation $x \mapsto \bar x$. Let $S$ and $T$ be Hermitian spaces over $E$ with Gram matrices $G_S$ and $G_T$, of ranks $a$ and $b$. Put $\mathbb{W} = M_{b \times a}(\mathbb{A}_E)$, with the Hermitian pairing
$$h(x, y) = \operatorname{tr}\big(G_S^{-1}\, {}^t\bar y\, G_T\, x\big),$$
the symplectic form $\langle x, y \rangle = \operatorname{tr}_{\mathbb{A}_E/\mathbb{A}_F}(\xi_0\, h(x, y))$ for a fixed $\xi_0 \in E$, and $\langle x, y \rangle' = \tfrac12 \langle x, y\rangle$. Let $\psi$ be a standard additive character of $\mathbb{A}_F/F$ of sign $-1$: at the infinite places $\psi(x) = \exp(-2\pi i \sum_\rho \theta_\rho(x))$ for a family $\theta$ of embeddings over the infinite places.

For $w_0 \in \mathbb{W}$ and a function $f$ on $\mathbb{W}$ put
$$(\rho(w_0) f)(w) = \psi(\langle w, w_0\rangle')\, f(w + w_0).$$
For $g \in \mathrm{U}(S)(\mathbb{A}_F)$ and $h \in \mathrm{U}(T)(\mathbb{A}_F)$ put $(g, h) \cdot x = h\, x\, g^{-1}$.

**Definition 1.15.1 (Theta function).** A function $f$ on $\mathbb{W}$ is a *theta function* if:

1. $f(\gamma + w) = \psi(-\langle \gamma, w\rangle')\, f(w)$ for each rational point $\gamma \in M_{b \times a}(E)$ and each $w$;
2. there is an open subgroup $U$ of $\mathbb{W}$ such that $\rho(u)f = f$ for each $u \in U$ with archimedean part $0$;
3. $f$ is continuous, and smooth along each continuous family of archimedean translations.

So a theta function is a vector of the global Heisenberg representation, read as a function on $\mathbb{W}$ that is quasi-periodic under the rational lattice. The value $f(0)$ is the *theta distribution*. For $f = \sum_\gamma \rho(\gamma)\Phi$ built from a Schwartz-Bruhat function $\Phi$, it is the theta sum $\sum_\gamma \Phi(\gamma)$ of [section 08](/entry/weil-rep-rational-darboux-fixes-theta-distribution/).

**Definition 1.15.2 (Cartan involution).** A *Cartan involution* for a Hermitian matrix $G$ is a matrix $s$ with $s^2 = 1$, $s^* G s = G$ and $Gs$ positive definite.

**Definition 1.15.3 (Finite and infinite parts).** Let $\Lambda_S$, $\Lambda_T$ be self-dual $\mathcal{O}_E$-lattices in $E^a$ and $E^b$ for the Hermitian forms, and $\chi_S, \chi_T$ Hecke characters. A *finite Weil part* is a representation $\omega_{\mathrm f}$ of $\mathrm{U}(S)(\mathbb{A}_F) \times \mathrm{U}(T)(\mathbb{A}_F)$ on functions on $\mathbb{W}$ that preserves theta functions, is continuous and unitary on them (for the $L^2$ norm over a fundamental domain of the rational lattice), acts trivially on the archimedean subgroups, satisfies $\omega_{\mathrm f}(g, h)\rho(w_0) = \rho((g,h)\cdot w_0)\,\omega_{\mathrm f}(g, h)$ on theta functions for $(g, h)$ at the finite places, transforms Heisenberg invariant functionals at split places by $r \cdot \chi_T(x)^{-1}\chi_S(y)$ with $r > 0$ and $x, y$ the determinants, and fixes the lattice vacuum at the nonsplit finite places. An *infinite Weil part* $\omega_\infty$ for the family $\theta$ is defined in the same way, with the roles of the finite and archimedean subgroups exchanged, and with the vacuum condition replaced by the following vacuum character: for Cartan involutions $s_S, s_T$ at each $\tau$ and archimedean $(g, h)$ that commute with them, and for $f$ a Fock vacuum at each $\tau$,
$$\omega_\infty(g, h) f = \prod_\tau \det\Big(\tfrac12 (1 + s_T \otimes {}^ts_S)(h_\tau \otimes {}^tg^{-1}_\tau) + \tfrac12 (1 - s_T \otimes {}^ts_S)\Big)\, f.$$

The determinant is the determinant of the action of $(g, h)$ on the $(+1)$ eigenspace of $s_T \otimes {}^ts_S$, which is the holomorphic part of the archimedean space in the Fock model. So the vacuum character is the classical character of the maximal compact subgroup on the Fock vacuum.

A Hecke character $\eta$ of $\mathbb{A}_E^\times$ is *of type $\tilde\eta$* if it is unramified everywhere, its restriction to $\mathbb{A}_F^\times$ is the quadratic character $\eta_{E/F}$ of the extension, and its infinity type at each $\tau$ is $\tfrac12$.

For $(g, h)$ write $\operatorname{sub}_{(g, h)} f = f((g, h)^{-1} \cdot\,)$, and say that $(g, h)$ *acts by the scalar $c$* if $\omega_{\mathrm f}(g, h)\,\omega_\infty(g, h) f = c\, \operatorname{sub}_{(g,h)} f$ for every theta function $f$.

In this section we fix $\psi$ standard of sign $-1$, a family $\theta$ of embeddings over the infinite places, self-dual lattices $\Lambda_S, \Lambda_T$, a character $\eta$ of type $\tilde\eta$, a finite Weil part $\omega_{\mathrm f}$ for $(\eta^a, \eta^b)$ and an infinite Weil part $\omega_\infty$ for $\theta$. We call a rational point $\gamma \in \mathrm{U}(S)(F)$ with matrix $A$ *Cartan-compatible* with $s_S$ if $s_S$ commutes with $A^\tau$ at each $\tau$.

Two facts from the earlier construction are used. For rational $(g, h)$ there is $c$ with $|c| = 1$ such that $(g, h)$ acts by the scalar $c$: a rational point acts on theta functions by the substitution up to a scalar, by the uniqueness of the Heisenberg representation. The two parts commute on theta functions, so if $p$ acts by $c$ and $q$ by $c'$ then $pq$ acts by $cc'$.

### The scalar is one

**Lemma 1.15.4 (Scalar comparison).** Fix Cartan involutions $s_S$ and $s_T$ at all $\tau$. There are $e \in \mathbb{C}$ and $s \neq 0$ with the following property. Let $g \in \mathrm{U}(S)(F)$ with matrix $A$ and $h \in \mathrm{U}(T)(F)$ such that $h^{-1}$ has matrix $B$, with $A$ and $B$ Cartan-compatible and $\det(B \otimes {}^tA - 1) \neq 0$. If $(g, h)$ acts by a scalar $c \neq 0$, then $c\, e = r\, s$ for some real $r > 0$.

Lean: `GlobalTheory.RatAut.scalar_const`.

*Proof.* Apply both sides to the vacuum. Choose a good norm, a lattice model of the finite part and a half idempotent at a split place, and a character $\kappa$ that relates $\eta$ to the split place. On the vacuum, the infinite part acts by the product of the determinants of the vacuum character, since $(g, h)$ commutes with the Cartan involutions. The finite part acts through a lattice intertwiner times the values of $\eta^a$ and $\eta^b$ on the determinants. Evaluating at $0$ turns the substitution into an integral of a Gaussian over the real points, and the hypothesis $\det(B \otimes {}^tA - 1) \neq 0$ says that $(g, h)$ has no fixed vector in $\mathbb{W}$, so this Gaussian integral is nonzero and its phase is that of the real isometry. The finite side gives a Gauss sum whose phase is the value of $\eta$ at the split place times a sign. Since $\eta$ has type $\tilde\eta$, its phase at the split place and its infinity type $\tfrac12$ cancel the phase of the determinants. So the product of $c$ with a constant $e$ (the integral of the Gaussian) is a positive real multiple of the constant $s = \eta(\kappa((-1)^{ab}))$. $\square$

**Lemma 1.15.5 (Cartan-compatible rational points act by $1$).** Let $s_S$ and $s_T$ be Cartan involutions at all $\tau$, $g \in \mathrm{U}(S)(F)$ with matrix $A$ and $h \in \mathrm{U}(T)(F)$ such that $h^{-1}$ has matrix $B$, with $A$ and $B$ Cartan-compatible. Then $(g, h)$ acts by the scalar $1$.

Lean: `GlobalTheory.RatAut.isScalar_one_of_comm`.

*Proof.* Let $(g, h)$ act by $c$ with $|c| = 1$. Take $e$ and $s$ from the [lemma](/entry/scalar-const/). The set of $t \in E$ with $t\bar t = 1$ is infinite, and for each matrix $M$ only finitely many $t$ make $\det(tM - 1) = 0$. Choose $t$ of norm $1$ with $\det(t\,B \otimes {}^tA - 1) \neq 0$ and $\det(t \cdot 1 - 1) \neq 0$. Let $k \in \mathrm{U}(T)(F)$ be the scalar matrix $t$. It commutes with everything, so $k^{-1}$ acts by a scalar $c'$ with $|c'| = 1$, and $(1, k^{-1})$ and $(g, hk^{-1})$ satisfy the hypotheses of the lemma. The lemma gives $c' e = r' s$ and $c c' e = r s$ with $r, r' > 0$, since $(g, hk^{-1})$ acts by $cc'$. Dividing, $c = r / r'$ is a positive real. Since $|c| = 1$, $c = 1$. $\square$

**Proposition 1.15.6 (Rational points act by substitution).** For $\gamma \in \mathrm{U}(S)(F)$, $\gamma' \in \mathrm{U}(T)(F)$ and each theta function $f$,
$$\omega_{\mathrm f}(\gamma, \gamma')\,\omega_\infty(\gamma, \gamma') f = f\big(\gamma'^{-1}\,\cdot\,\gamma\big).$$

Lean: `GlobalTheory.RatAut.of_oi_eq_subst`.

*Proof.* We show that $(\gamma, 1)$ and $(1, \gamma')$ act by $1$. Then $(\gamma, \gamma') = (\gamma, 1)(1, \gamma')$ acts by $1$, since the scalars multiply. At each $\tau$ there is a Cartan involution, so $(1, 1)$ acts by $1$ by the [lemma](/entry/is-scalar-one-of-comm/). The rational unitary group $\mathrm{U}(S)(F)$ is generated by the quasi-reflections
$$x \mapsto x + c\, v\, (v^* G_S\, x), \qquad v^* G_S v \neq 0,$$
which are the unitary maps $1 + c\, v v^* G_S$. For each quasi-reflection and each $\tau$ there is a Cartan involution that commutes with it: take a Cartan involution that preserves the line of $v$ and its orthogonal complement. So each quasi-reflection, paired with $1$, acts by $1$, by the lemma. Products of elements acting by $1$ act by $1$. Induction over products of quasi-reflections gives that $(\gamma, 1)$ acts by $1$. The same argument in $\mathrm{U}(T)(F)$, applied to $\gamma'^{-1}$, gives that $(1, \gamma')$ acts by $1$. $\square$

**Corollary 1.15.7 (The theta distribution is invariant).** For $\gamma \in \mathrm{U}(S)(F)$, $\gamma' \in \mathrm{U}(T)(F)$ and each theta function $f$,
$$\big(\omega_{\mathrm f}(\gamma, \gamma')\,\omega_\infty(\gamma, \gamma') f\big)(0) = f(0).$$
In particular this holds for $\gamma = 1$.

Lean: `GlobalTheory.RatAut.of_oi_apply_zero`; the case $\gamma = 1$ is `GlobalTheory.RatAut.automorphy_target` (also `GlobalTheory.T.thetaDistribution_invariant_rationalTarget`, a second name).

*Proof.* By the [proposition](/entry/of-oi-eq-subst/), the left side is $f(\gamma'^{-1} \cdot 0 \cdot \gamma) = f(0)$. $\square$

**Remark 1.15.8.** The classical theorem is A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), Chapter I: the theta distribution is invariant under the rational points of the metaplectic group, and on a dual pair the splitting characters must be Hecke characters for the invariance to descend to the unitary groups. The proof here works only with the two unitary groups and quasi-reflections, and it fixes the splitting by the type $\tilde\eta$, as in M. Harris, S. Kudla and W. J. Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), Section 1, where splitting characters are Hecke characters with restriction a power of $\eta_{E/F}$. Section 08 obtains the same invariance by the doubling method.

**Remark 1.15.9 (Formalization).** The corollary for one target point is `automorphy_target` ([ThetaDistributionInvariantRationalTarget.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaDistributionInvariantRationalTarget.lean#L364)): it states only the case $(1, \gamma')$, though `of_oi_apply_zero` at line 354 proves the case of a general rational pair, and its proof is `of_oi_apply_zero` with $\gamma = 1$. Its second name is a wrapper. The lemma on the scalar comparison (line 133) and the lemma on Cartan-compatible points (line 249) run under `maxHeartbeats 1000000`. The proof of the comparison lemma combines cited results (`integral_gaussian_real_isometry_no_fixed`, `finiteWeilRep_eq_latticeIntertwiner_mul_character`, `rationalIsometry_vacuumScalar_gaussSum_integral`, `etaTildeHeckeChar_split_mul_sign_of_norm_formula`) with an algebraic identity of phases; the proof above follows the order of these steps, and the claims on the phases are read from the names and statements of the cited results, not from their proofs. The two facts on scalars quoted before the lemmas are `exists_isScalar` and `IsScalar.mul` with `of_oi_comm`, and generation by quasi-reflections is `rat_induction` (FiniteDetSmulSubOne.lean, line 251).
