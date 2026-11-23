---
title: Shintani descent and products of cusp forms
decls:
  - GlobalTheory.Shin.DescentAll.kills_liftAll
  - GlobalTheory.T.shintani_lift_kills_product_of_cusp_forms
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Shintani descent and products of cusp forms

The last section of the chapter is a result on finite general linear groups. It is the finite field form of base change: the Shintani lift of a class function from $GL_n(\mathbb{F}_q)$ to $GL_n(\mathbb{F}_{q^l})$, through the norm map, sends the character of a parabolically induced product of [[cuspidal|9AZ164C298]] representations into the span of the constituents of an explicit induced product over the larger field. The local types that the construction of Galois representations uses at tamely ramified places are built from such representations, and this section gives the base change of their characters. The proof is an induction on the number of cuspidal factors. Each step uses the compatibility of the Shintani lift with [Harish-Chandra induction](/learn/representations/#parabolic-induction-and-the-jacquet-module) and the computation of the lift of one cuspidal character (Shintani 1976; Green 1955).

Let $F$ be a finite field with $q$ elements, let $F'/F$ be an extension of prime degree $l$, and let $s$ be a generator of $\mathrm{Gal}(F'/F)$. All functions are complex valued functions on finite groups.

**Definition 6.8.1 (Shintani lift).** For $\delta \in GL_n(F')$ put $N(\delta) = \delta\, s(\delta) \cdots s^{l-1}(\delta)$. An element $\gamma \in GL_n(F)$ is a *norm* of $\delta$ if $\gamma$ is conjugate to $N(\delta)$ in $GL_n(F')$. For a class function $f$ on $GL_n(F)$ the *Shintani lift* is the function on $GL_n(F')$ with $\mathrm{Sh}(f)(\delta) = f(\gamma)$ if $\delta$ has a norm $\gamma$, and $\mathrm{Sh}(f)(\delta) = 0$ if not.

The value does not depend on the choice of $\gamma$: two norms of $\delta$ are conjugate in $GL_n(F')$, so by Lang's theorem they are conjugate in $GL_n(F)$, and $f$ is a class function.

**Definition 6.8.2 (Kills).** Let $G$ be a finite group and let $\phi$ and $Y$ be functions on $G$. Then $Y$ *kills* $\phi$ if for each finite-dimensional complex representation $\rho$ of $G$ with $\sum_g \overline{Y(g)}\, \operatorname{tr}\rho(g) = 0$ we have $\sum_g \overline{\phi(g)}\, \rho(g) = 0$.

When $Y$ is a character, this says that $\phi$ is orthogonal to each irreducible character that does not occur in $Y$, that is, $\phi$ is in the span of the irreducible constituents of $Y$.

**Definition 6.8.3 (Cuspidal characters and products).** Fix an injective homomorphism $\theta$ from the multiplicative group of an algebraic closure $\bar F$ to $\mathbb{C}^\times$. For $m \ge 1$ and $k \ge 0$ let $s_k(P) = \sum_\alpha \theta(\alpha)^k$, the sum over the roots of the polynomial $P$ in $\bar F$ with multiplicity. Define $\psi_k$ on endomorphisms $g$ of finite-dimensional spaces $V$ by the recursion
$$\psi_k(g) = s_k(\operatorname{charpoly} g) - \sum_{W} \psi_k(g|_W),$$
the sum over the proper $g$-invariant subspaces $W$ of $V$, and put $\mathrm{cusp}_{m,k}(x) = (-1)^{m-1}\psi_k(x)$ for $x \in GL_m(F)$. The pair $(m, k)$ is *regular* if $k q^i \not\equiv k \pmod{q^m - 1}$ for $0 < i < m$. For class functions $\alpha$ on $GL_a(F)$ and $\beta$ on $GL_b(F)$ the *Harish-Chandra product* $\alpha \circ \beta$ is the class function on $GL_{a+b}(F)$
$$(\alpha \circ \beta)(x) = \frac{1}{\lvert P \rvert} \sum_{y \in GL_{a+b}(F)} \mathbf{1}_P(y^{-1}xy)\, \alpha(\text{top block})\, \beta(\text{bottom block}),$$
where $P$ is the block upper triangular parabolic subgroup and the blocks are those of $y^{-1}xy$. For a list $L = ((m_1, k_1), \dots, (m_r, k_r))$ put $\deg L = \sum m_i$ and $J_\theta(L) = \mathrm{cusp}_{m_1,k_1} \circ (\mathrm{cusp}_{m_2,k_2} \circ \cdots)$, with $J_\theta$ of the empty list equal to $1$.

For regular $(m, k)$, $\mathrm{cusp}_{m,k}$ is the character of the irreducible cuspidal representation of $GL_m(F)$ attached to the regular character $\theta^k$ of $\mathbb{F}_{q^m}^\times$ (Green 1955), and $J_\theta(L)$ is the character of the Harish-Chandra induced representation from the Levi subgroup $GL_{m_1} \times \cdots \times GL_{m_r}$. The recursion for $\psi_k$ is a Möbius inversion over the lattice of invariant subspaces, and it removes from the root sum the part that comes from proper parabolic subgroups, as in the description of [cuspidal representations](/learn/representations/#cuspidal-representations-and-segments) by Jacquet modules.

**Definition 6.8.4 (Lifted list).** For a pair $(m, k)$ put
$$\mathrm{lift}(m, k) = \begin{cases} \bigl((m/l, k),\ (m/l, kq),\ \dots,\ (m/l, kq^{l-1})\bigr) & \text{if } l \mid m,\\ \bigl((m, k(1 + q^m + q^{2m} + \dots + q^{(l-1)m}))\bigr) & \text{if } l \nmid m,\end{cases}$$
and for a list $L$ let $\mathrm{lift}(L)$ be the concatenation of the lists $\mathrm{lift}(m_i, k_i)$.

If $l \nmid m$, the field $\mathbb{F}_{q^m}$ and $F'$ are linearly disjoint, and the character $\theta^k$ of $\mathbb{F}_{q^m}^\times$ composed with the norm from $\mathbb{F}_{q^{lm}}^\times$ is $\theta^{k(1 + q^m + \dots)}$. If $l \mid m$, the torus $\mathbb{F}_{q^m}^\times$ is the multiplicative group of an extension of degree $m/l$ of $F'$, and the base change of the cuspidal representation splits into the $l$ Galois conjugates. So $\mathrm{lift}(L)$ is the list of the base change.

**Theorem 6.8.5 (Shintani lift of a product of cusp forms).** Let $F'/F$ be an extension of finite fields of prime degree $l$, let $s \ne 1$ in $\mathrm{Gal}(F'/F)$, let $\iota$ be an $F$-embedding of $\bar F$ into $\bar F'$, and let $\theta$ be an injective homomorphism from $\bar F'^\times$ to $\mathbb{C}^\times$. Let $L$ be a list of pairs $(m, k)$ with $m > 0$ and $(m, k)$ regular for $q = \lvert F \rvert$, and let $n = \deg L$. Then the character $J_\theta(\mathrm{lift}(L))$ on $GL_n(F')$ kills the Shintani lift of $J_{\theta \circ \iota}(L)$:
$$\operatorname{Kills}\bigl(\mathrm{Sh}(J_{\theta \circ \iota}(L)),\ J_\theta(\mathrm{lift}(L))\bigr).$$

Lean: `GlobalTheory.Shin.DescentAll.kills_liftAll` (also `GlobalTheory.T.shintani_lift_kills_product_of_cusp_forms`, the same statement).

This is the character form of Shintani descent for $GL_n$ over finite fields (Shintani 1976): the Shintani lift of the character of an irreducible representation of $GL_n(\mathbb{F}_q)$ is, up to sign, the character of its base change on the coset $GL_n(\mathbb{F}_{q^l}) \rtimes s$, and the base change of a Harish-Chandra induced representation is the Harish-Chandra induced representation of the base changes.

*Proof.* Since $l$ is prime and $s \ne 1$, $s$ generates $\mathrm{Gal}(F'/F)$. We use induction on $L$.

If $L$ is empty, then $n = 0$, the group $GL_0(F')$ is trivial, and the identity has the norm $1$, so the Shintani lift of $J(L) = 1$ is $1$, and $\mathrm{lift}(L)$ is empty. A character kills itself: if $\sum_g \overline{\chi(g)}\, \operatorname{tr}\rho(g) = 0$ for a character $\chi$, then the multiplicity in $\rho$ of each constituent of $\chi$ is $0$. By Schur orthogonality the operator $\sum_g \overline{\chi(g)}\rho(g)$ is $0$ on each isotypic part of $\rho$ for an irreducible representation that does not occur in $\chi$, so it is $0$.

Let $L = (m, k) :: L_0$, and let $A = \mathrm{lift}(m, k)$, so $\mathrm{lift}(L) = A \mathbin{+\!\!+} \mathrm{lift}(L_0)$. The lifted lists have degrees $m$ and $\deg L_0$ and contain only regular pairs for $q^l = \lvert F' \rvert$, so $J_\theta(A)$ and $J_\theta(\mathrm{lift}(L_0))$ are characters, and $J_\theta(\mathrm{lift}(L)) = J_\theta(A) \circ J_\theta(\mathrm{lift}(L_0))$ by the transitivity of Harish-Chandra induction. The lift of one cuspidal character is killed by the base change list:
$$\operatorname{Kills}\bigl(\mathrm{Sh}(\mathrm{cusp}_{m,k}),\ J_\theta(A)\bigr).$$
For $l \mid m$ this is the computation for the divisible degree; for $l \nmid m$ it is the computation for the degree that is not divisible, together with $J_\theta$ of a list of one pair being $\mathrm{cusp}_{m,k'} \circ 1 = \mathrm{cusp}_{m,k'}$. The Shintani lift of a Harish-Chandra product is the twisted Harish-Chandra product of the Shintani lifts,
$$\mathrm{Sh}(\alpha \circ \beta) = \mathrm{Sh}(\alpha) \circ_s \mathrm{Sh}(\beta),$$
where $\circ_s$ conjugates by $y^{-1} x\, s(y)$ in place of $y^{-1} x y$. Finally, if $Y_1$ kills $\phi_1$ and $Y_2$ kills $\phi_2$ with characters $Y_1$ and $Y_2$, then $Y_1 \circ Y_2$ kills $\phi_1 \circ_s \phi_2$. Apply this with the single cuspidal case and the induction hypothesis for $L_0$. $\square$

The theorem uses five results on finite general linear groups as given: the lift of one cuspidal character in the two cases, the compatibility of the Shintani lift with Harish-Chandra induction, the isotypic step for the twisted product, the transitivity of Harish-Chandra products, and the fact that the lifted list keeps the degree and regularity.

**Remark 6.8.6 (Formalization).** The second form of the theorem has a one-line proof that tries three tactic forms in turn, under a heartbeat limit of 1000000 ([ShintaniLiftKillsProductOfCuspForms.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShintaniLiftKillsProductOfCuspForms.lean#L6)). The first form is in a file with the name FormalGermBaseChange, which is not about formal germs ([FormalGermBaseChange.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormalGermBaseChange.lean#L45)), and the definitions are in a file with the name OrthSubrepresentation ([OrthSubrepresentation.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OrthSubrepresentation.lean#L15)). The Shintani lift picks a norm by choice; the value is independent of the choice only for class functions ([OrthSubrepresentation.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OrthSubrepresentation.lean#L236)). The blocks of a matrix are sent to the identity when they are not invertible, and $J_\theta$ of the empty list is the constant $1$ on $GL_n(F)$ for every $n$, not only for $n = 0$ ([OrthSubrepresentation.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OrthSubrepresentation.lean#L167)). We have not opened the proofs of the five given results, so the proof above shows how the induction combines them.

## Notes and references

The chapter feeds into two parts of the construction of Galois representations. The theta lift in the stable range and the two lifts of odd size give the step that [attaches Galois representations in even rank](/entry/to-core-k/), through the odd rank groups. The Shintani descent of the last section gives the base change of the characters of the local types, through the [inertial type step](/entry/kills-all-holds/). The Siegel-Weil formula of the fourth section is the definite case of the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula), and the Rallis identity of the sixth section is the convergent case of the [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula).

- V. Bargmann, On a Hilbert space of analytic functions and an associated integral transform, Part I, *Comm. Pure Appl. Math.* 14 (1961), 187 to 214.
- W. T. Gan, Y. Qiu and S. Takeda, The regularized Siegel-Weil formula (the second term identity) and the Rallis inner product formula, *Invent. Math.* 198 (2014), 739 to 831.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254, Springer, 1987.
- J. A. Green, The characters of the finite general linear groups, *Trans. Amer. Math. Soc.* 80 (1955), 402 to 447.
- R. Howe, θ-series and invariant theory, in *Automorphic Forms, Representations and L-functions*, Proc. Sympos. Pure Math. 33, Part 1, Amer. Math. Soc., 1979.
- A. Ichino, A regularized Siegel-Weil formula for unitary groups, *Math. Z.* 247 (2004).
- M. Kashiwara and M. Vergne, On the Segal-Shale-Weil representations and harmonic polynomials, *Invent. Math.* 44 (1978), 1 to 47.
- S. Kudla, Splitting metaplectic covers of dual reductive pairs, *Israel J. Math.* 87 (1994), 361 to 401.
- S. Kudla and S. Rallis, A regularized Siegel-Weil formula: the first term identity, *Ann. of Math.* 140 (1994).
- J.-S. Li, Non-vanishing theorems for the cohomology of certain arithmetic quotients, *J. Reine Angew. Math.* 428 (1992), 177 to 217.
- A. Mínguez, Correspondance de Howe explicite: paires duales de type II, *Ann. Sci. Éc. Norm. Supér.* 41 (2008), 717 to 741.
- S. Rallis, Langlands' functoriality and the Weil representation, *Amer. J. Math.* 104 (1982).
- S. Rallis, On the Howe duality conjecture, *Compositio Math.* 51 (1984), 333 to 399.
- T. Shintani, Two remarks on irreducible characters of finite general linear groups, *J. Math. Soc. Japan* 28 (1976), 396 to 414.
- A. Weil, Sur la formule de Siegel dans la théorie des groupes classiques, *Acta Math.* 113 (1965), 1 to 87.
