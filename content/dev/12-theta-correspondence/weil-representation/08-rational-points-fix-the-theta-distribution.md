---
title: Rational points fix the theta distribution
decls:
  - GlobalTheory.WeilThetaRat.dbl_rat
  - GlobalTheory.WeilThetaRat.member_rat
  - GlobalTheory.WeilThetaRat.thetaSum_om_rat
  - GlobalTheory.T.weilRep_rationalDarboux_fixes_thetaDistribution
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rational points fix the theta distribution

This section proves Weil's theorem for a unitary dual pair over a CM field: the theta distribution $\Phi \mapsto \sum_{\xi} \Phi(\xi)$, the sum over the rational points, is invariant under $\omega(\gamma, \gamma')$ for rational $\gamma \in \mathrm{U}(X)(F)$ and $\gamma' \in \mathrm{U}(W)(F)$. So the theta function $\theta(g, h; \Phi) = \sum_\xi \omega(g,h)\Phi(\xi)$ is left invariant under the rational points of both groups, which is [the invariance of the theta sum under rational points](/entry/theta-sum-omega-rational/) used to define [theta kernels](/learn/theta/#theta-kernels) and the [global theta lift](/learn/theta/#the-global-theta-lift). The proof is by doubling: the action of one group is embedded in the doubled unitary group, where the rational points are products of elements that fix one of two Lagrangians.

### The setting

Let $F$ be a totally real number field and $E/F$ a CM extension with complex conjugation $\sigma$. Let $\psi$ be a standard additive character of $\mathbb{A}_F / F$. For a matrix $J$ over $E$ with $\sigma({}^tJ) = \pm J$ and $\det J \neq 0$, write $\mathrm{U}(J)$ for its unitary group over $\mathbb{A}_F$ and $\mathrm{U}(J)(F)$ for the rational points, the elements whose entries lie in $E$.

Let $J_A$ (of size $a$) and $J_B$ (of size $b$) be such matrices, one Hermitian and one skew-Hermitian. The space $M_{a \times b}(\mathbb{A}_E)$ carries the symplectic form built from $J_A$ and $J_B$ and the trace, and a *Darboux basis* of it is a symplectic basis indexed by $\kappa \sqcup \kappa$ with $|\kappa| = ab$. We ask that it be *rational*: each $x \in M_{a \times b}(E)$ has rational coordinates, so the coordinate map identifies $M_{a \times b}(E)$ with $F^\kappa \times F^\kappa$. Let $\mathcal{S}(\mathbb{A}_F^\kappa)$ be the adelic [[Schwartz-Bruhat space|GE020MY43M]].

**Definition 1.8.1 (Theta distribution).** For $\Phi \in \mathcal{S}(\mathbb{A}_F^\kappa)$ put $\Theta(\Phi) = \sum_{\xi \in F^\kappa} \Phi(\xi)$.

The sum converges absolutely, by the [archimedean decay bound](/entry/om-bound-arch/).

**Definition 1.8.2 (Doubled space).** The *doubled matrix* of $J_B$ is $J_B \oplus (-J_B)$, of size $2b$. In $E^b \oplus E^b$ the *diagonal* $\Delta = \{(y, y)\}$ and the *antidiagonal* $\nabla = \{(y, -y)\}$ are isotropic for the doubled form. Let $P_\Delta$ and $P_\nabla$ be their stabilizers in the doubled unitary group.

**Definition 1.8.3 (Doubled Weil datum).** A *Weil datum with doubling* for $\mathrm{U}(J_B)$ is a Weil representation $\omega$ of $\mathrm{U}(J_B)$ on $\mathcal{S}(\mathbb{A}_F^\kappa)$ for a Hecke character $\chi$, together with a Weil representation $\omega_{\mathrm d}$ of the doubled unitary group on $\mathcal{S}(\mathbb{A}_F^{\kappa \sqcup \kappa})$ for a doubled Darboux basis, such that $\omega_{\mathrm d}$ acts on $P_\Delta$ by the Siegel rule for the Lagrangian $\Delta$, and such that for each $g \in \mathrm{U}(J_B)$
$$\omega_{\mathrm d}\bigl(\operatorname{diag}(g, 1)\bigr)(\Phi_1 \otimes \Phi_2) = \omega(g)\Phi_1 \otimes \Phi_2.$$

Here $(\Phi_1 \otimes \Phi_2)(x, y) = \Phi_1(x)\Phi_2(y)$, and $\Theta(\Phi_1 \otimes \Phi_2) = \Theta(\Phi_1)\,\Theta(\Phi_2)$ since the sum over $F^{\kappa \sqcup \kappa}$ is a product of two sums.

### The doubled group

**Lemma 1.8.4 (Rational points of the doubled group).** Each rational point $g$ of the doubled unitary group is a product $g = p\, q\, p'$ with $p, p' \in P_\Delta(F)$ and $q \in P_\nabla(F)$.

This is the rational form of the decomposition $G = P\bar P P$ for a pair of opposite parabolic subgroups, here $P_\Delta$ and $P_\nabla$, whose intersection is a Levi subgroup; see the [[Bruhat decomposition|T91E86D0RH]] of Volume 1 for the cells.

**Proposition 1.8.5 (Doubled group fixes the theta distribution).** In the setting of a Weil datum with doubling, $\Theta(\omega_{\mathrm d}(g)\varphi) = \Theta(\varphi)$ for each rational $g$ of the doubled unitary group and each $\varphi \in \mathcal{S}(\mathbb{A}_F^{\kappa \sqcup \kappa})$.

Lean: `GlobalTheory.WeilThetaRat.dbl_rat`.

*Proof.* Write $g = p q p'$ by the lemma. Then $\omega_{\mathrm d}(g)\varphi = \omega_{\mathrm d}(p)\,\omega_{\mathrm d}(q)\,\omega_{\mathrm d}(p')\varphi$, and each factor preserves the Schwartz-Bruhat space. Two facts finish the proof.

First, $\Theta \circ \omega_{\mathrm d}(p) = \Theta$ for $p \in P_\Delta(F)$. In the Schrödinger model of the Lagrangian $\Delta$, the element $p$ acts by a linear substitution of the variable by a rational matrix $t$, a factor $\chi(\det t)$ times a power of $|\det t|$, and multiplication by $\psi$ of a rational quadratic form. On rational points, $\chi$ is trivial on $E^\times$, the product formula gives $|\det t| = 1$, $\psi$ is trivial on $F$, and the substitution permutes $F^\kappa$. So the sum is unchanged.

Second, $\Theta \circ \omega_{\mathrm d}(q) = \Theta$ for $q \in P_\nabla(F)$. The Schrödinger models for $\Delta$ and for $\nabla$ are related by a partial Fourier transform, and by the Poisson summation formula this transform preserves $\Theta$. In the model of $\nabla$ the first argument applies to $q$. $\square$

### The theorem

**Proposition 1.8.6 (Rational invariance for one group).** Let $\omega$ be a Weil representation of $\mathrm{U}(J_B)$ with doubling, as above. Then $\Theta(\omega(\gamma)\Phi) = \Theta(\Phi)$ for each $\gamma \in \mathrm{U}(J_B)(F)$ and each $\Phi \in \mathcal{S}(\mathbb{A}_F^\kappa)$.

Lean: `GlobalTheory.WeilThetaRat.member_rat`.

*Proof.* The element $g_{\mathrm d} = \operatorname{diag}(\gamma, 1)$ lies in the doubled unitary group, and it is rational since $\gamma$ is. Choose $\varphi_2 \in \mathcal{S}(\mathbb{A}_F^\kappa)$ with $\Theta(\varphi_2) \neq 0$, for example a product of a Gaussian at infinity and the indicator function of a small neighborhood of $0$ at a finite place, scaled so that only $\xi = 0$ contributes. By the proposition on the doubled group, and by the compatibility of the doubling with $\operatorname{diag}(g, 1)$,
$$\Theta(\omega(\gamma)\Phi)\,\Theta(\varphi_2) = \Theta\bigl(\omega_{\mathrm d}(g_{\mathrm d})(\Phi \otimes \varphi_2)\bigr) = \Theta(\Phi \otimes \varphi_2) = \Theta(\Phi)\,\Theta(\varphi_2).$$
Divide by $\Theta(\varphi_2) \neq 0$. $\square$

**Theorem 1.8.7 (Weil's invariance for unitary dual pairs).** Let $J_X$ be Hermitian of size $n$ and $J_W$ skew-Hermitian of size $d$, both invertible, with a rational Darboux basis of $M_{n \times d}(\mathbb{A}_E)$, Hecke characters $\chi_X, \chi_W$, and a Weil representation $\omega$ of $\mathrm{U}(J_X) \times \mathrm{U}(J_W)$ such that each of the two factors, restricted to its group, is a Weil representation with doubling. Then
$$\Theta\bigl(\omega(\gamma, \gamma')\Phi\bigr) = \Theta(\Phi)$$
for all $\gamma \in \mathrm{U}(J_X)(F)$, $\gamma' \in \mathrm{U}(J_W)(F)$ and $\Phi \in \mathcal{S}(\mathbb{A}_F^{\,n \times d})$.

Lean: `GlobalTheory.WeilThetaRat.thetaSum_om_rat` (also `GlobalTheory.T.weilRep_rationalDarboux_fixes_thetaDistribution`, a second name).

This is the theorem of A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), that the theta distribution is invariant under the rational points of the metaplectic group, restricted to the image of $\mathrm{U}(X) \times \mathrm{U}(W)$ under the splitting of [Kudla](/entry/kudla-splitting-split-unitary-of-literature/).

*Proof.* Write $(\gamma, \gamma') = (\gamma, 1)(1, \gamma')$, so $\omega(\gamma, \gamma')\Phi = \omega(\gamma, 1)\,\omega(1, \gamma')\Phi$, and $\omega(1, \gamma')\Phi$ is again a Schwartz-Bruhat function. Apply the proposition on one group twice. For $\gamma'$ take $J_A = J_X$, $J_B = J_W$, the sign $-1$ of the skew-Hermitian matrix, and the given basis. For $\gamma$ take $J_A = J_W$, $J_B = J_X$, the sign $+1$, and the transposed basis, which is again rational since $x \mapsto {}^tx$ maps $M_{d \times n}(E)$ onto $M_{n \times d}(E)$. Then
$$\Theta(\omega(\gamma,1)\,\omega(1,\gamma')\Phi) = \Theta(\omega(1,\gamma')\Phi) = \Theta(\Phi). \qquad \square$$

**Remark 1.8.8.** The doubling replaces the classical proof, which writes $\mathrm{U}(W)(F)$ as generated by $P(F)$ and a Weyl element and checks each generator. Here only the parabolics $P_\Delta$ and $P_\nabla$ of the doubled group are used, and they act on $\Theta$ by substitution and by Poisson summation.

**Remark 1.8.9 (Formalization).** The decomposition lemma is `doubledUnitary_rational_eq_diagonalFixers_product`, the two facts in the proof of the doubled proposition are `thetaSum_doubledWeil_fixed_diagonalStabilizer` and `adelicThetaSum_doubledWeil_antidiagonal_invariant`, and the choice of $\varphi_2$ is `exists_adelicSchwartz_thetaDistributionSum_ne_zero`, all in `GlobalTheory.T`; we have not opened their proofs, so the arguments for them above are ours. The three results are at lines 16, 38 and 71 of WeilRepRationalDarbouxFixesThetaDistribution.lean, with a helper `rat_mat` between them. The doubling hypothesis is `IsUWeilB` and the pair hypothesis is `IsUWeilPair` (Definitions/Divisors/HilbertNinetyQuotientHomEqIff.lean, lines 425 and 435). In `thetaSum_om_rat` the third clause of `IsUWeilPair`, the continuity `IsContOn`, is dropped at line 73, and the rationality of the transposed basis is proved again from that of the given one. In `member_rat` the first part of the doubled splitting is dropped. The rationality of $\gamma$ is passed as an explicit matrix $\gamma_0$ with entries in $E$. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (WeilRepRationalDarbouxFixesThetaDistributionStatement.lean, line 7).
