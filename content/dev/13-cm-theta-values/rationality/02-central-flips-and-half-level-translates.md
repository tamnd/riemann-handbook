---
title: Central flips and half-level translates
decls:
  - GlobalTheory.T.exists_central_flip_translate_halfPlaces_thetaPair
  - GlobalTheory.LevelSeries.exists_central_flip_step
  - GlobalTheory.T.exists_centralFlip_thetaTranslate_halfLevel
  - GlobalTheory.LevelSeries.exists_flip_theta
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Central flips and half-level translates

The bound for theta series in Section 3 starts from a Schwartz function that is a combination of Heisenberg translates of the vacuum vector. The translates are supported at a set of places $P$ of $E$, and the bound needs this set in a normal form: it must be the set of places that divide the level ideal of the cover. This section moves the support of the translates from a place $\mathfrak{P}$ to its conjugate $\overline{\mathfrak{P}}$. The tool is a central element $z$ of the finite adelic unitary group of $V$. It acts on the Schwartz space through the [Weil representation](/learn/theta/#the-weil-representation), and the price of the move is an explicit scalar. The main result gives a power $l^c$ that makes this scalar integral at $l$, with $c$ independent of the auxiliary level.

### Vacuum pairs and translate spans

Let $E$ be the CM field, $F$ its totally real subfield, $\mathbb{A}_{E,f}$ the finite adeles of $E$, and $x \mapsto \bar{x}$ the conjugation. Let $V$ and $W$ be Hermitian spaces over $E$, and $\omega$ a Weil representation of $\mathrm{U}(V)(\mathbb{A}) \times \mathrm{U}(W)(\mathbb{A})$ on the space of functions on $\mathrm{Hom}(W, V) \otimes \mathbb{A}$.

**Definition 3.2.1 (Vacuum pair).** The data $(\omega, \Lambda_V, \Lambda_W, f_0)$ form a *vacuum pair* if $\omega$ is a Weil representation for the additive character and the splitting characters $\chi_V$ and $\chi_W$, $V \neq 0$, the lattices $\Lambda_V$ and $\Lambda_W$ are the standard self-dual lattices, the archimedean frames are Cartan involutions of the Gram matrices, and $f_0$ is the vacuum vector: the characteristic function of the lattice at the finite places times the Gaussian at the archimedean places.

For a place $\mathfrak{P}$ of $E$, a *place idempotent* is the element of $\mathbb{A}_{E,f}$ that is $1$ at $\mathfrak{P}$ and $0$ elsewhere. For a finite set $P$ of places, an *idempotent sum over $P$* is the sum $e$ of the place idempotents of the places in $P$, with $e\,\bar{e} = 0$. So $P$ contains no pair of conjugate places. If the level of a cover has level ideal $\mathfrak{M}$, a *half-level idempotent* is an idempotent sum over the set of all places that divide $\mathfrak{M}$.

**Definition 3.2.2 (Translate span).** Let $e$ be an idempotent sum, $M \geq 1$ and $O \subseteq \mathbb{C}$ a subring. The *translate span* $\mathrm{Tr}(e, M, O)$ is the $O$-module spanned by the Heisenberg translates $\rho(y) f_0$ of the vacuum, where $y$ runs over the points of $\mathrm{Hom}(W, V) \otimes \mathbb{A}_{E,f}$ that are supported at $e$ and satisfy $M y \in \Lambda$, the product lattice.

So $\mathrm{Tr}(e, M, O)$ is spanned by translates by $M$-torsion points of the lattice, supported at the places of $e$.

For a finite set $T$ of places of $E$ and an odd integer $m \ge 1$ with every place of $T$ dividing $m$, let $e_T$ be an idempotent sum over $T$. The *flip element* is
$$z_{T,m} = e_T\,m + \bar{e}_T\,m^{-1} + (1 - e_T - \bar{e}_T) \in \mathbb{A}_{E,f}^\times .$$
Its norm $z\bar{z}$ is $1$, so $z_{T,m}$ is a central element of the unitary group of $V$. The *flip unit* is the unit $x$ of $\mathbb{A}_{E,f}$ with $x\,(e_T\,m^{\dim V} + 1 - e_T) = 1$, and the *flip scalar* is
$$\lambda(T, m, x) = \chi_W(x)^{-1}\,\Big(\prod_{\mathfrak{P} \in T} N\big(\mathfrak{P}^{v_\mathfrak{P}(m)}\big)^{\dim V \cdot \dim W}\Big)^{-1/2} .$$
Write $\overline{T}$ for the set of conjugates of the places of $T$.

**Lemma 3.2.3 (Central flip).** Let $(\omega, \Lambda_V, \Lambda_W, f_0)$ be a vacuum pair. For every finite set $T$ of places of $E$ and every $m \in \mathbb{N}$, there is $z$ in the finite adelic unitary group of $V$ with these properties.

1. For every prime $l$ such that no place of $T$ divides $l$, the element $z$ is $1$ at the places above $l$.
2. Let $e_T$ be an idempotent sum over $T$. Assume that $m$ is odd, prime to the bad number of the datum, and divisible by every place of $T$. Then there is a flip unit $x$ for $(e_T, m)$ such that the following holds. Let $M = m u$ with $u$ prime to the places of $T$, let $e$ be an idempotent sum over a set $P \supseteq T$, let $e'$ be an idempotent sum over $(P \setminus T) \cup \overline{T}$, and let $O$ contain the $M$-th roots of unity. Then for every $f \in \mathrm{Tr}(e, M, O)$ there is $F \in \mathrm{Tr}(e', M, O)$ with
$$\omega(z, 1)\big(\lambda(T, m, x)\,F\big) = f .$$

Lean: `GlobalTheory.LevelSeries.exists_central_flip_step` (also `GlobalTheory.T.exists_central_flip_translate_halfPlaces_thetaPair`, a second name).

*Proof.* If $m = 0$, or if there is no idempotent sum over $T$, take $z = 1$. Then property 1 holds, and property 2 is empty: either $m$ is not odd, or there is no $e_T$.

Otherwise fix an idempotent sum $e_T$ over $T$. Take $z$ to be the scalar matrix $z_{T,m}$. It has trivial archimedean component, it is unitary, and it is $1$ at every place outside $T \cup \overline{T}$, which gives property 1. Two idempotent sums over the same set are equal, so the $e_T$ of property 2 is the fixed one. The element $e_T (m^{-1})^{\dim V} + (1 - e_T)$ is inverse to $e_T m^{\dim V} + (1 - e_T)$, since $e_T$ is an idempotent; this gives the flip unit $x$.

The central element acts on the vacuum by the splitting character and by a change of the lattice at the places of $T \cup \overline{T}$. The development proves that $\omega(z, 1) f_0$ is a multiple $\mu\,Y$ of a mean $Y$ of translates of $f_0$ supported at $\overline{T}$, and that $\mu$ is given by the flip scalar $\lambda(T, m, x)$, which is not $0$ since $m \ne 0$. The action of $z$ commutes with the Heisenberg translates supported away from $T \cup \overline{T}$, and it moves a translate supported at $T$ to a translate supported at $\overline{T}$. So $\omega(z, 1)$ maps $\lambda(T, m, x)\,\mathrm{Tr}(e', M, O)$ onto $\mathrm{Tr}(e, M, O)$, which is property 2. $\square$

### The flip to a half-level idempotent

Let $\chi$ be a Hecke character of $E$ and $M_0 \neq 0$. The pair $(\chi, M_0)$ is *tied to $\chi_W$* if $\chi$ agrees with the splitting character $\chi_W$ in the sense of the datum, $\chi$ is unramified at every prime not dividing $M_0$, and the local components of $\chi$ at the places of $F$ that split in $E$ are trivial.

**Theorem 3.2.4 (Flip to a half-level idempotent).** Let $(\omega, \Lambda_V, \Lambda_W, f_0)$ be a vacuum pair with $\dim W$ odd. Let $(\chi, M_0)$ be tied to $\chi_W$, with $M_0 \ne 0$, and let $l$ be a prime. Then there are a finite set $Z$ of elements of the finite adelic unitary group of $V$ and $c \in \mathbb{N}$ with the following property. Let $l_2$ be a level of a cover with $M = M_0\,p_d$, $p_d$ prime to $M_0$ and to $l$, and $M$ prime to the bad number. Let $k$ be a number field with an embedding $\sigma$ into $\mathbb{C}$, a place $\lambda$ above $l$, and a subring $O$ of $\mathbb{C}$ that contains the image of every $\lambda$-integral element and the $M$-th roots of unity. Assume that $\sigma(k)$ is stable under conjugation and that $\chi$ takes values in $\sigma(k)$ up to the weight $-1/2$. Let $e$ be an idempotent sum over a set $P$ of places that all divide $M$, and $e_2$ a half-level idempotent for $l_2$. Then there are $z_2 \in Z$ and $z_1$, equal to $1$ at the places above $l$, such that for every $f \in \mathrm{Tr}(e, M, O)$ there is $f' \in \mathrm{Tr}(e_2, M, O)$ with
$$l^{c}\,\theta(s, g; f, Q) = \theta(s\,z_2\,z_1, g; f', Q)$$
for all archimedean frames, all harmonic polynomials $Q$, all $s$ and all $g$.

Lean: `GlobalTheory.LevelSeries.exists_flip_theta` (also `GlobalTheory.T.exists_centralFlip_thetaTranslate_halfLevel`, a second name).

*Proof.* The places of $E$ that divide $M_0$ form a finite set. For each subset $T$ of this set, [the central flip](/entry/exists-central-flip-step/) gives an element $z_T$, and the development proves that there is $c_T$ with $l^{c_T}\,\lambda(T, M_0, x) \in O$ for every flip unit $x$ and every ring $O$ as in the statement. Put $Z = \{z_T\}$ and $c = \max_T c_T$. Both depend only on $M_0$ and $l$.

Now fix the level $l_2$, the ring $O$ and the idempotents. Since $M = M_0 p_d$ is odd, so are $M_0$ and $p_d$. Let $T_0$ be the set of places of $P$ that divide $M_0$ but not the level ideal, and $T_1$ the set of places of $P$ that divide $p_d$ but not the level ideal. First flip at $T_0$ with $m = M_0$, using $z_2 = z_{T_0} \in Z$. This moves the support from $P$ to $P_1 = (P \setminus T_0) \cup \overline{T_0}$, with an idempotent sum $e_1$. Then flip at $T_1$ with $m = p_d$, using a central flip $z_1$ for $T_1$. This moves the support to a set whose places all divide the level ideal, with an idempotent sum $e_3$. Since $p_d$ is prime to $l$, the element $z_1$ is $1$ above $l$, and the development proves that the flip scalar at $T_1$ is in $O$ with no power of $l$. The flip scalar at $T_0$ times $l^{c}$ is in $O$, because $c \ge c_{T_0}$.

The translates supported at $e_3$ lie in the translates supported at the half-level idempotent $e_2$, since every place of the support divides the level ideal. Combine the two flips: $\omega(z_2 z_1, 1)$ sends an element of $\mathrm{Tr}(e_2, M, O)$ to $l^c f$. The theta kernel of a moved Fock vector at a finite point is the theta kernel at the moved point, so $l^c\,\theta(s, g; f, Q) = \theta(s z_2 z_1, g; f', Q)$. $\square$

The point of the theorem is the order of the quantifiers: $Z$ and $c$ are chosen before the auxiliary level $p_d$. So the power of $l$ is uniform over the tower of covers.

**Remark 3.2.5 (Formalization).** The flip element is `flipElt` ([FlipIdxNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FlipIdxNeZero.lean#L17)); the flip unit, index and scalar are `IsFlipDet`, `flipIdx` and `flipScal` ([IsFlipDet.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsFlipDet.lean#L19)). The translate span is `trSp`, the condition that $z$ is $1$ above $l$ is `OneAt`, and the tie of $\chi$ is `ChiData` ([ValRingLocRing.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ValRingLocRing.lean#L22)). `VacPair` and the half-level idempotent `IsHalfIdem` are in [IsInertTop.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsInertTop.lean#L26); `IsIdemSum` includes the condition $e\bar{e} = 0$. In the flip lemma the default branch takes $z = 1$; the two branches are split by `by_cases` on the existence of $e_T$ with $m \neq 0$ ([ExistsCentralFlipTranslateHalfPlacesThetaPair.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsCentralFlipTranslateHalfPlacesThetaPair.lean#L25)). In the main theorem, $Z$ is the image of the power set of the places above $M_0$ under a chosen function, and $c$ is the supremum of the chosen constants ([ExistsCentralFlipThetaTranslateHalfLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsCentralFlipThetaTranslateHalfLevel.lean#L38)). The relevant lemmas `T.flipScalar_primePow_integral_at_levelPlaces`, `T.flipScalar_mem_coefficientRing_auxiliaryLevel` and `T.centralFlip_vacuum_eq_multiple_of_translate_mean` were not opened. We have not unfolded `IsVacO`, `IsHalf`, `heisO` or `ChrEq`.
