---
title: Weil operators on theta vacua
decls:
  - GlobalTheory.InertSign.vacuum_inert
  - GlobalTheory.T.weilRepresentation_vacuum_sign_inert_places
  - GlobalTheory.RatEqui.oddEq_of_even
  - GlobalTheory.NormSum.inp_all
  - GlobalTheory.T.cmThetaNormBoundHypotheses_satisfied
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weil operators on theta vacua

This section proves two laws for operators of Weil type on theta functions of a CM curve, and then it collects the inputs of the CM theta norm bound. The first law gives the action of a unitary element that is supported at inert primes on the theta vacuum: the result is a sign times a lattice intertwiner. The second law shows that a rational unitary element acts by a pullback times a product of characters, when both ranks are even. The first law is one of the 22 inputs, and the collection of all 22 inputs is used by the step [nonempty hypotheses](/step/nonempty-hyps/). The second law is used by [the family of curves](/entry/exists-family-of-curve/). The background is in [the Weil representation](/learn/theta/#the-weil-representation), [the Fock model](/learn/theta/#the-fock-model) and [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics).

### The setting

Fix a datum. It gives a CM field $E$ with complex conjugation $c$, a set $\mathcal{T}$ of complex embeddings of $E$, and a lattice $\Lambda_T \subset \mathbb{C}$ of a CM curve. A curve datum $(\mathfrak{c}, \delta)$ fixes the curve, and $\delta \neq 0$. Let $\mathbb{A}_E = E \otimes \mathbb{A}_f$, where $\mathbb{A}_f$ is the ring of finite adeles of $\mathbb{Q}$, and let $\widehat{\mathcal{O}}_E$ be its integral subring. For $N \ge 0$ let $U_N$ be the unitary group of the form $\sum_i x_i\, c(y_i)$ in $\mathrm{GL}_N(\mathbb{A}_E)$.

A lattice is an $\mathcal{O}_E$-submodule $L \subset E^N$. The standard lattice is $L_N = \mathcal{O}_E^N$. An element $g \in \mathrm{GL}_N(\mathbb{A}_E)$ *moves* $L_N$ to $L$ if $x \in L$ exactly when $g^{-1} x \in \widehat{\mathcal{O}}_E^N$. Then $L$ is self-dual when $g \in U_N$. Put
$$\ell(L) = \operatorname{length}_{\mathcal{O}_E}\big(L_N / (L_N \cap L)\big).$$

**Definition 1.9.1 (inert prime, inert support).** A prime $q$ is *inert* if $c$ fixes every prime of $\mathcal{O}_E$ over $q$. An element $g$ has *inert support* if $g$ is trivial at every prime $q$ that is not inert, that is, the entries of $g - 1$ vanish at $q$.

Let $V = \mathbb{C}^{\mathcal{T} \times N' \times N}$ with the hermitian form $H(z, w) = \sum z_{\tau i j}\, \overline{w_{\tau i j}} / \operatorname{area}(\Lambda_T)$. For $x \in V$ and a function $G$ on $V$ put
$$U_x G(z) = G(z + x)\, \exp\big(-\pi H(z, x) - \tfrac{\pi}{2} H(x, x)\big),$$
and let $\alpha(x) = (-1)^{m}$, where $m$ is the integer nearest to $\tfrac{\sqrt d}{2}\, \mathrm{Re}\, H(x, x)$ and $-d$ is the discriminant of the host field.

**Definition 1.9.2 (theta space, intertwiner).** For a lattice $\Lambda \subset V$, the *theta space* $\Theta(\Lambda)$ is the set of holomorphic $G$ with $\alpha(x)\, U_x G = G$ for all $x \in \Lambda$. For two lattices $\Lambda_1, \Lambda_2$, the *intertwiner* is
$$I_{\Lambda_1, \Lambda_2} G = [\Lambda_2 : \Lambda_1 \cap \Lambda_2]^{-1/2} \sum_{x \in \Lambda_2 / (\Lambda_1 \cap \Lambda_2)} \alpha(x)\, U_x G.$$

Lattices $L \subset E^N$ and $L' \subset E^{N'}$ give a lattice $\Lambda(L, L') \subset V$, spanned by the products $w \cdot A$ with $w \in \Lambda_T$ and $A$ in a module of matrices built from $L$ and $L'$. Put $\Lambda_0 = \Lambda(L_N, L_{N'})$.

**Definition 1.9.3 (Weil operator system).** Let $e_0 \in \Theta(\Lambda_0)$ be nonzero. A *Weil operator system* for $e_0$ is a family of operators $\Omega(g, g')$, for $g \in U_N$ and $g' \in U_{N'}$, on the space of holomorphic functions on $V$ that are invariant under $\alpha(x) U_x$ for $x$ in some multiple of $\Lambda_0$. It comes with unitary Hecke characters $\chi$ of level $N$ and $\chi'$ of level $N'$, with infinity types $n, n' : \mathcal{T} \to \mathbb{Z}$, and with signs $\varepsilon, \varepsilon' \in \{\pm 1\}$. The rules are:

1. $\Omega$ is linear, $\Omega(1, 1) = 1$, and $\Omega(g_1 g_2, g_1' g_2') = \Omega(g_1, g_1')\, \Omega(g_2, g_2')$;
2. $\Omega$ commutes with $U_x$, up to a change of $x$ near the image of $x$ under $(g, g')$;
3. if $k$ and $k'$ are integral and have inert support, then $\Omega(k, k') e_0 = e_0$;
4. a split law: on elements trivial at the inert primes, $\Omega(g, g') e_0$ is a value of $\chi^{\varepsilon}$ and $\chi'^{\varepsilon'}$ times $I_{\Lambda_0, \Lambda(L_1, L_1')} e_0$.

A Hecke character $\chi$ of infinity type $n$ satisfies $\chi(a) \prod_\tau \big(\tau(a)/|\tau(a)|\big)^{n_\tau} = 1$ for $a \in E^\times$.

### The sign at inert primes

**Theorem 1.9.4 (sign at inert primes).** Let $(\mathfrak{c}, \delta)$ be a curve datum, let $N N'$ be even, let $e_0 \in \Theta(\Lambda_0)$, and let $\Omega$ be a Weil operator system for $e_0$. Let $g \in U_N$ and $g' \in U_{N'}$ have inert support, and let them move the standard lattices to $L_1$ and $L_1'$. Then
$$\Omega(g, g')\, e_0 = (-1)^{N \ell(L_1') + N' \ell(L_1)}\; I_{\Lambda_0,\, \Lambda(L_1, L_1')}\, e_0.$$

Lean: `GlobalTheory.T.weilRepresentation_vacuum_sign_inert_places` (also `GlobalTheory.InertSign.vacuum_inert`, a second name).

The proof treats one factor at a time. The next lemma is the one factor case, stated in the form that the proof uses.

**Lemma 1.9.5 (one factor).** Fix $n$. Let $L \mapsto \Lambda_L$ send lattices in $E^n$ to lattices in $V$, let $\omega(h)$ be operators for $h \in U_n$, and let $\sigma^2 = 1$. Let $e_0 \in \Theta(\Lambda_{L_n})$ be nonzero. Assume the following for self-dual $L_1, L_2, L_3$:

1. $I_{\Lambda_{L_1}, \Lambda_{L_2}}$ maps $\Theta(\Lambda_{L_1})$ to $\Theta(\Lambda_{L_2})$, the reverse map inverts it, and $I_{\Lambda_L, \Lambda_L} = 1$;
2. each $\Theta(\Lambda_L)$ is a line;
3. $\omega$ is multiplicative on $e_0$, linear on theta spaces, and fixes $e_0$ under integral elements with inert support;
4. if $h$ moves $L_n$ to $L$, then $\omega(h) e_0 \in \Theta(\Lambda_L)$, and $\omega$ commutes with the intertwiners of moved lattices;
5. if $L_1 \cap L_3 \subset L_2 \subset (L_1 \cap L_2) + (L_2 \cap L_3)$, then $I_{2,3} I_{1,2} = I_{1,3}$ on nonzero vectors;
6. for a triple $A, B, C$ of neighbours at a prime $P$ that is stable under $c$ with $a - c(a) \notin P$ for some $a$, $I_{B,C} I_{A,B} = \sigma\, I_{A,C}$ on nonzero vectors.

Then $\omega(h) e_0 = \sigma^{\ell(L)}\, I_{\Lambda_{L_n}, \Lambda_L}\, e_0$ for each $h$ with inert support that moves $L_n$ to $L$.

*Proof.* Two elements with inert support that move $L_n$ to the same lattice differ by an integral element with inert support, so they give the same vector. Also $\omega(h) e_0 \neq 0$, since $\omega(h^{-1})$ undoes $\omega(h)$ on $e_0$. We use induction on $\ell(L)$.

If $\ell(L) = 0$, then $L = L_n$: otherwise a chain of neighbours from $L_n$ to $L$ gives $\ell(L) > 0$. Then $h$ is integral, $\omega(h) e_0 = e_0$, and $I_{\Lambda_{L_n}, \Lambda_{L_n}} = 1$.

Let $\ell(L) = k + 1$. The neighbour chain gives a prime $q$, a prime $P \ni q$ and a vector $x \in L_n$ with $x \notin L$, $P x \subset L$ and $\langle x, x \rangle$ integral, such that the neighbour $L^x = \{y \in L : \langle y, x\rangle \text{ integral}\} + \mathcal{O}_E x$ has $\ell(L^x) = k$. The prime $q$ is inert. If it were not, $h$ would be trivial at $q$, so $L$ and $L_n$ would agree at $q$; then $s x \in L$ for some $s$ prime to $q$, and $q x \in L$, so $x \in L$. At the inert prime $q$ there is a local unitary element that permutes three neighbours of $L$ around $P$. The line property and rule 6 then give $k_1$ with inert support that moves $L_n$ to $L^x$, with
$$\omega(h)\, e_0 = \sigma\, I_{\Lambda_{L^x}, \Lambda_L}\, \omega(k_1)\, e_0.$$
By induction, $\omega(k_1) e_0 = \sigma^{k} I_{\Lambda_{L_n}, \Lambda_{L^x}} e_0$. The lattice $L^x$ lies between $L_n$ and $L$ in the sense of rule 5, so the two intertwiners compose to $I_{\Lambda_{L_n}, \Lambda_L}$. This gives $\sigma^{k+1}$. $\square$

*Proof of the theorem.* The proof uses facts about the theta spaces that are proved elsewhere in the development: the spaces for self-dual pairs are lines; the intertwiners are unitary and invert each other; the triples of kernel lattices are self-dual; the triple constant is $1$ on distributive triples and $(-1)^r$ on neighbour triples; the operators map theta spaces of moved lattices to each other and commute with the intertwiners.

Apply the lemma to $\Lambda_L = \Lambda(L, L_{N'})$ and $\omega(h) = \Omega(h, 1)$, with $\sigma = (-1)^{N'}$. This gives
$$\Omega(g, 1)\, e_0 = (-1)^{N' \ell(L_1)}\, I_{\Lambda_0, \Lambda(L_1, L_{N'})}\, e_0.$$
Apply it again to $\Lambda_L = \Lambda(L_N, L)$ and $\omega(h) = \Omega(1, h)$, with $\sigma = (-1)^{N}$. Then
$$\begin{aligned}
\Omega(g, g')\, e_0 &= \Omega(1, g')\, \Omega(g, 1)\, e_0 \\
&= (-1)^{N' \ell(L_1)}\, I_{\Lambda(L_N, L_1'), \Lambda(L_1, L_1')}\, \Omega(1, g')\, e_0 \\
&= (-1)^{N' \ell(L_1) + N \ell(L_1')}\, I_{\Lambda(L_N, L_1'), \Lambda(L_1, L_1')}\, I_{\Lambda_0, \Lambda(L_N, L_1')}\, e_0.
\end{aligned}$$
The second line uses that $\Omega(1, g')$ commutes with the intertwiner. The triple $\Lambda_0, \Lambda(L_N, L_1'), \Lambda(L_1, L_1')$ is distributive, so the two intertwiners compose to $I_{\Lambda_0, \Lambda(L_1, L_1')}$. $\square$

The sign comes from the triple constant $(-1)^r$ of a neighbour step, with $r$ equal to the rank of the other factor.

### Rational elements

**Definition 1.9.6 (odd vacuum).** Let $t_0$ be a $2$-torsion point of the curve. A function $e_0$ is an *odd vacuum* for $(\mathfrak{c}, \delta, t_0, N, N')$ if $e_0 \in \Theta(\Lambda_0)$, its coefficients are algebraic, its norm is the norm of the genus one theta function at $t_0$ raised to a power that depends on the datum and on $N N'$, it is a theta vector up to units, and at each prime $p$ prime to the norm of $\mathfrak{c}$ it is a unit times an intertwined pullback of the genus one theta function along an orthonormal basis.

**Theorem 1.9.7 (rational elements act by pullback).** Let $(\mathfrak{c}, \delta)$ be a curve datum and $t_0$ a $2$-torsion point. Let $N$ and $N'$ both be even, and let $e_0$ be an odd vacuum for these data. Let $\Omega$ be a Weil operator system for $e_0$. Let $\gamma \in U_N(E)$ and $\gamma' \in U_{N'}(E)$ be rational, with images $\gamma_{\mathbb{A}}$ and $\gamma'_{\mathbb{A}}$. Let $a, a' : \mathcal{T} \to \mathbb{Z}$ satisfy
$$2 a'(\tau) = \varepsilon\, n(\tau) + N, \qquad 2 a(\tau) = \varepsilon'\, n'(\tau) - N'.$$
Then for each $F$ in the domain of $\Omega$,
$$\Omega(\gamma_{\mathbb{A}}, \gamma'_{\mathbb{A}})\, F(z) = \prod_\tau \tau(\det \gamma)^{-a(\tau)}\, \tau(\det \gamma')^{-a'(\tau)} \cdot F\big((\tau(\gamma')^{*}\, z_\tau\, \tau(\gamma))_\tau\big).$$

Lean: `GlobalTheory.RatEqui.oddEq_of_even`.

*Proof.* Say that $(g, g')$ *acts by pullback* along $(\gamma, \gamma')$ with factor $a$ if $\Omega(g, g') F(z) = a \cdot F(\gamma'^{*} z \gamma)$ for all $F$. This property is multiplicative in $(g, g', \gamma, \gamma', a)$. So it is enough to treat $(\gamma_{\mathbb{A}}, 1)$ and $(1, \gamma'_{\mathbb{A}})$. We treat the second one; the first one is the same.

First let $\det(1 - \gamma') \neq 0$. Then $u = \det \gamma'$ has $u\, c(u) = 1$. Put $b = 1 + u$ if $1 + u \neq 0$, and $b = \sqrt{-d}$ if $u = -1$. In both cases $b = u\, c(b)$. A function in the domain is determined by the action on the vacuum, since the rational translates of $e_0$ span the theta functions. On the vacuum, the exact constant law for even ranks gives $\Omega(1, \gamma'_{\mathbb{A}}) e_0 = \chi(b)^{\varepsilon}\, I e_0$, where $I$ is the intertwiner from $\Lambda_0$ to the lattice moved by $\gamma'_{\mathbb{A}}$. The pullback law for even ranks says that the pullback of $e_0$ along $(1, \gamma')$ is $\prod_\tau \tau(u)^{N/2}\, I e_0$. The automorphy of $\chi$ gives
$$\chi(b)^{\varepsilon} = \prod_\tau \tau(u)^{-k(\tau)} \quad\text{when } 2 k(\tau) = \varepsilon\, n(\tau),$$
since $\big(\tau(b)/|\tau(b)|\big)^2 = \tau(b)/\overline{\tau(b)} = \tau(u)$. With $k = a' - N/2$, which is an integer because $N$ is even, the factors $\prod_\tau \tau(u)^{-k(\tau)}$ and $\prod_\tau \tau(u)^{-N/2}$ combine to $\prod_\tau \tau(u)^{-a'(\tau)}$.

For general $\gamma'$, pick $z \in E$ with $z\, c(z) = 1$ that avoids the eigenvalues of $\gamma'$, and with $z \neq 1$. Then $\gamma' = (z \gamma') \cdot (c(z) \cdot 1)$, and both factors are rational unitary with $\det(1 - \cdot) \neq 0$. Multiplicativity gives the claim. $\square$

### The inputs of the norm bound

**Theorem 1.9.8 (inputs of the CM theta norm bound).** For every datum, the 22 inputs of the CM theta norm bound hold. They are:

1. the induced CM type and the trace normalisation, and the permutation of types by embeddings;
2. the unitarity of the theta intertwiners and the Gauss sum triple constant;
3. the Galois laws for the curve, for theta values and for their extension, and a $2$-torsion base point;
4. five uses of these laws: the first use, algebraicity, conjugation, norms and complex conjugation;
5. the sign at inert primes (the theorem above), the oddness condition, and the representatives $\gamma g k$ trivial at a given prime, with $\gamma$ rational and $k$ integral;
6. an integral model over the unit disc, integral torsion translates, units at $2$, integral normalised jets, and vanishing at odd split primes;
7. the exact equivariance law for odd vacua.

Lean: `GlobalTheory.T.cmThetaNormBoundHypotheses_satisfied` (also `GlobalTheory.NormSum.inp_all`, a second name).

*Proof.* Each of the 22 fields is one theorem applied to the datum. The field of item 5 on the sign is the theorem above. The fields on torsion translates and on jets are theorems of the previous section. $\square$

**Remark 1.9.9 (Formalization).** The sign theorem is in [WeilRepresentationVacuumSignInertPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/WeilRepresentationVacuumSignInertPlaces.lean#L254), and the one factor lemma is `core` at [L126](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/WeilRepresentationVacuumSignInertPlaces.lean#L126). The statement is `odd3` in [StandardLatticesGL3.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLatticesGL3.lean#L515). The proof calls `T.kernelLattices_form_selfDual_triples`, `T.thetaFunctions_all_levels_closure`, `T.thetaLattice_triples_distributive`, `theta_translation_intertwiner_unitary`, `ThetaLine.theta_line`, `T.thetaTripleConstant_eq_one_distributive`, `T.thetaTripleConstant_eq_neg_one_pow`, `T.weilRepresentation_theta_moved_lattice`, `T.weilRepresentation_comm_heisenbergIntertwiner`, `T.thetaTripleData_of_neighbourTriple` and `T.thetaTripleDiagonalData_of_selfDualNeighbourTriple`; `core` calls `T.self_dual_lattices_neighbour_chain`, `exists_move`, `T.exists_local_component_unitary_matrix` and `T.exists_traceOne_integer_conj_diff_prime_to`. We did not open these proofs. The hypothesis that $N N'$ is even is introduced as `_` at L255 and is not used. The Weil operator system is the structure `WeilO` at [L443](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLatticesGL3.lean#L443); the lattice $\Lambda(L, L')$ is `La`, built from `YYl`, which we did not unfold. The second theorem is in [OddEqOfEven.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OddEqOfEven.lean#L176), with the column and row cases `isPull_col` and `isPull_row` and the factorisation `exists_factor`. It uses `T.om_eq_mul_pull_of_om_eq_on_vacuum`, `T.theta_span_rational_translates_vacuum`, `T.weilOperator_vacuum_exact_constant_evenRank`, `T.thetaPullback_secondGroup_rationalPoint_eq_det_smul` with its first group form, and `T.exists_normOne_scalar_avoiding_matrix_eigenvalues`. Only the first part of the odd vacuum hypothesis `oddE0` is used, namely $e_0 \in \Theta(\Lambda_0)$, and the point $t_0$ is not used. The inputs are the structure `Inp` in [NormSumPairRankZeroOfCurveCoordNorm.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/NormSumPairRankZeroOfCurveCoordNorm.lean#L175), filled in [CmThetaNormBoundHypothesesSatisfied.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/CmThetaNormBoundHypothesesSatisfied.lean#L29). Twenty-one fields are `T.*` theorems; the field `eqv` is `OddRank.exact_equivariance`, not the second theorem of this section. The field `eqv` asks only that $N N'$ is even, while the second theorem asks that $N$ and $N'$ are both even.
