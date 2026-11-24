---
title: Existence of Weil representations
decls:
  - PositivityTheory.ThKW.datumEta
  - PositivityTheory.ThKW.S.exists_isWeilDatumOF
  - PositivityTheory.ThKW.S.exists_isUWeilPair_cm
  - PositivityTheory.ThKW.S.exists_isWeil
  - PositivityTheory.ThKW.S.weilEx
  - PositivityTheory.ThKR.realMetaplecticRepresentation_holds
  - PositivityTheory.ThKR.lieSecond2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Existence of Weil representations

This section constructs the global [[Weil representation|H3Q2703KKV]] of a unitary dual pair over a CM extension, normalized by a pair of [[Hecke characters|KPYFGB342X]], and proves two facts at the real places: the real [[metaplectic group|8B0JM2YDE2]] acts on $L^2(\mathbb{R}^l)$ with the expected properties, and the second member of the pair acts on Fock vectors through its Lie algebra with the weight fixed by the character. The existence theorem is passed by the [literature step](/step/every-character-of-literature/) to the theta integrals of the next section, and the Lie statement is used by the [step on every character](/step/every-character/). The background is the [Weil representation](/learn/theta/#the-weil-representation), the [Schrödinger model](/learn/theta/#the-schrdinger-model) and the [Fock model](/learn/theta/#the-fock-model).

### Weil representations of a unitary pair

Let $E/F$ be a CM extension of number fields with complex conjugation $\sigma$, let $\mathbb{A}_F$ be the adeles of $F$ and $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$. Fix a standard [[additive character|2WMYTJD33F]] $\psi$ of $\mathbb{A}_F / F$. Let $J_A$ be an $a \times a$ Hermitian matrix and $J_B$ a $b \times b$ matrix over $\mathbb{A}_E$, and let $\xi \in E$ with $\sigma(\xi) = -\xi$. On $\mathbb{W} = M_{a \times b}(\mathbb{A}_E)$ put
$$\langle x, y \rangle = \operatorname{tr}_{\mathbb{A}_E / \mathbb{A}_F}\bigl(\xi\, h(x, y)\bigr),$$
where $h$ is the Hermitian tensor form of $J_A$ and $J_B$. This is a symplectic form over $\mathbb{A}_F$. A Darboux basis $d$ identifies $\mathbb{W}$ with $\mathbb{A}_F^{\kappa} \times \mathbb{A}_F^{\kappa}$, and gives the Heisenberg operators $\rho_\psi(x)$ on functions on $\mathbb{A}_F^{\kappa}$, as in the [[Heisenberg group|ZZYCV5EX9J]] picture of the [Stone-von Neumann theorem](/learn/theta/#the-stone-von-neumann-theorem).

**Definition 2.5.1.** Let $\chi_A$, $\chi_B$ be characters of $\mathbb{A}_E^{\times}$. A homomorphism $\omega$ from $U(J_A) \times U(J_B)$ to the operators on functions on $\mathbb{A}_F^{\kappa}$ is a *Weil representation for $(\chi_A, \chi_B)$* if:

1. the restriction of $\omega$ to $U(J_B)$ is unitary on [[Schwartz functions|GE020MY43M]] and satisfies $\omega(h) \rho_\psi(x) \omega(h)^{-1} = \rho_\psi(x h^{\mathsf{T}})$;
2. on the doubled space for $J_B \oplus (-J_B)$ there is a compatible representation, which agrees with $\omega$ on $U(J_B) \times 1$ on product functions, and which obeys the *Siegel rule*: on a functional invariant under the Heisenberg operators of the diagonal Lagrangian, an element of $U(J_B \oplus -J_B)$ that stabilizes the diagonal and acts on it by $t$ acts by the scalar $\chi_A(\det t)\, |N \det t|^{a/2}$;
3. the same holds for $U(J_A)$ with the transposed basis and the character $\chi_B$;
4. the matrix coefficients $g \mapsto \lambda(\omega(g) \varphi)$ are continuous for admissible functionals $\lambda$.

Condition 2 is the usual normalization of the splitting of the metaplectic cover over a unitary group: the splitting is fixed by its value on the Siegel parabolic of the doubled group. For a character $\chi$ of $\mathbb{A}_E^{\times} / E^{\times}$ and $n \geq 0$ we say that *$\chi$ restricts to $\eta^n$* if, for $a \in \mathbb{A}_F^{\times}$, $\chi(a) = 1$ when $a$ lies in $F^{\times} N(\mathbb{A}_E^{\times})$ and $\chi(a) = (-1)^n$ otherwise; that is, $\chi|_{\mathbb{A}_F^{\times}} = \eta_{E/F}^{n}$ for the quadratic character $\eta_{E/F}$ of $E/F$.

### Construction for powers of one character

**Theorem 2.5.2 (Weil datum for powers of $\eta$).** Let $J_S$ and $J_T$ be nondegenerate Hermitian matrices over $E$ of sizes $n_S$ and $n_T$, let $\xi_0 \neq 0$ in $E$ with $\sigma(\xi_0) = -\xi_0$, and let $\Lambda \subset M_{n_T \times n_S}(E)$ be a good lattice that is rationally self-dual for the form of $\xi_0$. Suppose given a lattice representation of the adelic unitary groups on the theta functions of $\Lambda$. Let $\eta$ be a Hecke character of $E$ that restricts to $\eta_{E/F}$, has exponent $1$ at every infinite place, and is unramified at the inert places. Then there is a Weil datum $\omega$ for the pair $(\eta^{n_S}, \eta^{n_T})$.

Lean: `PositivityTheory.ThKW.datumEta`

*Proof.* A trace character $\theta$ and a real chart of $\mathbb{A}_E$ give a context in which local operators can be built. The character $\eta$ gives signs $\varepsilon_v$ with product $1$ over all places. At the finite places, the local Weil operators are produced from the lattice representation, twisted by $\eta^{n}$; at the infinite places, they are produced from the Schrödinger model, with the vacuum fixed. The finite and infinite parts commute, so their product is a representation of the adelic group. To see that it is a Weil datum, one checks that the rational points act on the theta functions by the scalar $1$; on each piece this scalar is computed from the product formula for the $\varepsilon_v$, and the lemma that a commuting scalar on a rational element equals $1$ finishes the check. Evaluating at $0$ shows the action of a rational pair on a function $f$ is $f$ itself. $\square$

**Theorem 2.5.3 (Weil datum for a pair of characters).** Let $J_S$, $J_T$, $\xi_0$ be as above, and suppose that a self-dual lattice exists for $(J_S, J_T, \xi_0)$. Let $\chi_S$, $\chi_T$ be Hecke characters of $E$ such that $\chi_S$ restricts to $\eta^{n_S}$ and $\chi_T$ restricts to $\eta^{n_T}$. Then there is a Weil datum for $(\chi_S, \chi_T)$.

Lean: `PositivityTheory.ThKW.S.exists_isWeilDatumOF`

*Proof.* Choose a Hecke character $\eta$ with the properties of the previous theorem. The theta functions of the lattice are invariant under the Heisenberg group, and they carry a lattice representation. The previous theorem gives a datum $\omega$ for $(\eta^{n_S}, \eta^{n_T})$. The characters $(\eta^{n_S})^{-1} \chi_S$ and $(\eta^{n_T})^{-1} \chi_T$ are Hecke characters that are trivial on $\mathbb{A}_F^{\times}$, and twisting a Weil datum by such a pair of characters gives a Weil datum for the product characters. Since $\eta^{n_S} \cdot (\eta^{n_S})^{-1} \chi_S = \chi_S$, the twisted datum is the one required. $\square$

**Theorem 2.5.4 (Transport to the adelic Schwartz space).** Let $J_S$, $J_T$ be nondegenerate Hermitian over $E$ and $\xi_0$ as above, with a self-dual lattice, and let $\chi_S$, $\chi_T$ be Hecke characters restricting to $\eta^{n_S}$ and $\eta^{n_T}$. Put $\xi = -1$, $J_A = J_T^{\mathsf{T}}$ and $J_B = -\xi_0 J_S^{-1}$, so that $\xi J_B = \xi_0 J_S^{-1}$. Then there are a Darboux basis $d$ of $M_{n_T \times n_S}(\mathbb{A}_E)$ and a Weil representation for $(\chi_T, \chi_S)$ on the adelic Schwartz space in the sense of the definition above.

Lean: `PositivityTheory.ThKW.S.exists_isUWeilPair_cm`

*Proof.* The previous theorem gives a Weil datum. With $J_A = J_T^{\mathsf{T}}$ and $\xi J_B = \xi_0 J_S^{-1}$ the symplectic form of the datum matches the form $\langle\,,\rangle$, so a Darboux basis for one is a Darboux basis for the other. The datum is transported along this basis to the adelic Schwartz space, and the four conditions of the definition are read off from the properties of the datum: the Heisenberg relation from the datum, the Siegel rule from its character, and continuity from the continuity of the local pieces. $\square$

**Theorem 2.5.5 (Existence of the Weil representation).** Let $X$ be an $n$-dimensional Hermitian space over $E$ of signature $(r, s)$ and $W$ a $d$-dimensional skew-Hermitian space of signature $(r', s')$, and let $M$ be a good tensor model for $X \otimes W$. Let $\chi_X$ and $\chi_W$ be Hecke characters such that $\chi_X$ restricts to $\eta^{n}$ and $\chi_W$ restricts to $\eta^{d}$. Then there is a Weil representation $\omega$ of $U(X) \times U(W)$ on the model $M$ for $(\chi_X, \chi_W)$.

Lean: `PositivityTheory.ThKW.S.exists_isWeil` (also `PositivityTheory.ThKW.S.weilEx`, a second name)

*Proof.* Since $E/F$ is CM there is $\xi_0 \neq 0$ in $E$ with $\sigma(\xi_0) = -\xi_0$. Put $J_S = -\xi_0 J_W^{-1}$ and $J_T = J_X^{\mathsf{T}}$; both are Hermitian and nondegenerate. The good tensor model gives a self-dual lattice for this pair. The previous theorem, applied with $\chi_S = \chi_W$ and $\chi_T = \chi_X$, gives a Weil representation with $J_A = J_T^{\mathsf{T}} = J_X$ and $J_B = -\xi_0 J_S^{-1} = J_W$, and with $\xi = -1$ this is the symplectic form of the model $M$. So it is a Weil representation on $M$. $\square$

This is the existence part of the theory of Kudla and of Harris, Kudla and Sweet on splittings of the metaplectic cover over unitary groups, here proved for the global pair at once. A copy of the theorem with a different goodness hypothesis is [the version used for theta integrals](/entry/weil-ex-k/), whose [proof entry](/entry/exists-is-weil-k/) gives the eight steps in detail.

### The real metaplectic group

For a finite set $l$, let $Sp_{2l}(\mathbb{R})$ act on $\mathbb{R}^l \times \mathbb{R}^l$ and let $\rho(w)$ be the Heisenberg operators on $L^2(\mathbb{R}^l)$.

**Theorem 2.5.6 (Real metaplectic representation).** For every nonempty finite $l$ there are a topological group $\widetilde{Sp}$, a continuous homomorphism $\mathrm{pr} : \widetilde{Sp} \to Sp_{2l}(\mathbb{R})$ and a unitary representation $\omega$ of $\widetilde{Sp}$ on $L^2(\mathbb{R}^l)$ with an action $\omega_S$ on Schwartz functions, such that:

1. $\mathrm{pr}$ is a surjective covering map whose kernel is $\{1, \epsilon\}$ with $\epsilon \neq 1$ and $\omega(\epsilon) = -1$;
2. $g \mapsto \omega(g) f$ is continuous for each $f$;
3. $\omega(g) \rho(w) = \rho(\mathrm{pr}(g) w) \omega(g)$;
4. $\omega(g) f = \omega_S(g) f$ for Schwartz $f$;
5. the orbit maps of Schwartz vectors are smooth;
6. for each $X$ in the Lie algebra $\mathfrak{sp}_{2l}(\mathbb{R})$ there is a one-parameter subgroup $\gamma$ with $\mathrm{pr}(\gamma(t)) = \exp(t X)$ and $\frac{d}{dt}\big|_{t=0} \omega(\gamma(t)) f = Q_X f$, where $Q_X$ is the explicit second-order operator of $X$.

Lean: `PositivityTheory.ThKR.realMetaplecticRepresentation_holds`

*Proof.* Take for $\widetilde{Sp}$ the group of triples $(s, U, U_S)$ with $s \in Sp_{2l}(\mathbb{R})$, $U$ a unitary operator of $L^2$ and $U_S$ an invertible operator of the Schwartz space, such that $U$ and $U_S$ agree on Schwartz functions, both implement $s$ on the Heisenberg operators, and $U_S$ satisfies a normalization of its value at $0$ that pins it down up to sign. Give it the topology induced from $Sp_{2l}(\mathbb{R})$ and the strong topology. Properties 2 to 4 hold by construction. For an $s$ whose upper left block is invertible, an explicit integral operator gives a section with a scalar that is $1$ when the determinant of that block is positive; this gives surjectivity of $\mathrm{pr}$ and the description of the kernel as $\{1, \epsilon\}$ with $\epsilon$ acting by $-1$. Near $1$ the action agrees with the explicit section, which gives the covering property, the smoothness of orbits, and the one-parameter subgroups with derivative $Q_X$. $\square$

### The Lie algebra action on Fock vectors

**Theorem 2.5.7 (Lie action of the second member).** Assume that for every $X \in \mathfrak{sp}_{2l}(\mathbb{R})$ there is a local lift of $t \mapsto \exp(t X)$ to the Schwartz space, defined for $|t| < \varepsilon$, implementing $\exp(t X)$ on the Heisenberg operators and with derivative $Q_X + c$ at $0$ for a constant $c$; and assume that the Heisenberg lines $t \mapsto \rho_\psi(t u)$ along real directions $u$ have the explicit derivatives of the Schrödinger model. Let $\omega$ be the $U(J_B)$ part of a Weil representation for $\chi$, let $\Phi$ be the Fock map of a framing of the real places, and let $\chi$ have exponent $m(w)$ at each infinite place $w$. Then the derivative of $\omega$ along the compact part of $U(J_B)$ at $w$ acts on the image of $\Phi$ as the standard action on polynomial tensors plus the scalar $m(w)/2$.

Lean: `PositivityTheory.ThKR.lieSecond2`

*Proof.* The local lift, applied to the frame of $J_B$ at each $w$, gives a constant $c(w)$ such that the derivative acts on Fock vectors as the standard action plus $c(w)$. Applied to the frame of the doubled matrix $J_B \oplus (-J_B)$ it gives a constant $c'(w)$ for the doubled representation. Testing both on a box function $f \otimes f$ with $f(0) = 1$, and using the compatibility of the doubled representation on product functions, gives $\sum_w c(w) \operatorname{tr} Y_w = \sum_w c'(w) \operatorname{tr} Y_w$ for every admissible $Y$. The Siegel rule on the doubled space evaluates the doubled constant through the character $\chi$, and its exponent at $w$ gives $c'(w) = m(w)/2$. Hence $c(w) = m(w)/2$. $\square$

In classical terms, the $K_\infty$-types of the Fock vectors are those of the [Fock model](/learn/theta/#the-fock-model) shifted by the weight $m/2$ of the splitting character; see the computations of Kashiwara and Vergne for the real symplectic case.

**Remark 2.5.8 (Formalization).** The existence theorem is in [WeilEx.lean](lean:Development/WeilBound/ThetaLifts/Reductions/WeilPairs/WeilPairExistence/WeilEx.lean#L21), with the second name at L49. The construction for powers of $\eta$ is at [IsScalarOneOfComm.lean](lean:Development/WeilBound/ThetaLifts/Reductions/WeilPairs/IsScalarOneOfComm.lean#L302). The real metaplectic group is the subgroup `G` of [ContinuousPair.lean](lean:Development/WeilBound/ThetaLifts/Reductions/MetaplecticDerivatives/ContinuousPair.lean#L84), and its theorem is at [RealMetaplecticRepresentationHolds.lean](lean:Development/WeilBound/ThetaLifts/Reductions/MetaplecticDerivatives/RealMetaplecticRepresentationHolds.lean#L9). The Lie theorem [LieScalar2.lean](lean:Development/WeilBound/ThetaLifts/Reductions/LieScalar2.lean#L14) takes the local lift and the derivatives of Heisenberg lines as hypotheses, so it is a reduction, not an unconditional statement. The condition "restricts to $\eta^n$" is the predicate `ResEtaPow`, whose subgroup is the image of $F^{\times}$; the Weil representation is the predicate `IsUWeilPair`, in which a Siegel rule replaces any explicit formula for the splitting.
