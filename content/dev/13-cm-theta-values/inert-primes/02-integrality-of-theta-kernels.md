---
title: Integrality of theta kernels at an inert prime
decls:
  - Formalism.L2.KerInert.oneCopyTh1S_of_isom
  - Formalism.L2.KerInert.oneCopyLoc_of_isom
  - Formalism.L2.KerInert.integral_inert_of_weakApprox
  - Formalism.L2.KerInert.integral_inert_of_approx_basis
  - Formalism.L2.KerInert.kernels_integral_inert
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integrality of theta kernels at an inert prime

This section proves that the theta kernels of pairs of self-dual Hermitian lattices, read in the logarithmic coordinates of a curve with complex multiplication, have integral Taylor coefficients at a prime $p \ge 5$ that is inert in $K$. The coordinates come from an orthonormal local basis, and the series is corrected by the sigma factor of Section 1. The proof reduces the statement in two steps: first from a general pair of lattices to the standard lattice, by weak approximation in the unitary group, and then from the standard lattice in any rank to one copy of rank $1$. The theorem is the integrality input of [the first kernel law](/entry/first-kernel-small-of-frame/) in Section 3, and it is one of the results on complex multiplication that [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/) uses.

Throughout, we assume the existence of good models, which [Theorem 5.14.6](/entry/good-model/) gives.

**Theorem 6.2.1 (Good models).** Let $d$ be a squarefree integer with $d \equiv 3 \pmod 4$, and $L$ a lattice in $\mathbb{C}$ with complex multiplication by $\mathbb{Q}(\sqrt{-d})$. Let $l \ge 5$ be a prime with $l \nmid d$ and $\iota : \mathbb{C} \to \mathbb{C}_l$ a field isomorphism. Then there are $g_2, g_3$ in the maximal unramified extension of $\mathbb{Q}_l$ in $\mathbb{C}_l$, of norm at most $1$, with $|g_2^3 - 27 g_3^2| = 1$, and $\mu \ne 0$ with $g_2 = \mu^4\,\iota g_2(L)$ and $g_3 = \mu^6\,\iota g_3(L)$.

This is the theorem of Deuring and of Serre and Tate that a curve with complex multiplication has potentially good reduction everywhere, made precise at an unramified prime (see [reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models) and Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II). All results of this section and of the next two sections assume it.

### Lattices, local bases and the corrected series

Let $E$ be the CM field of the fixed datum, with $K \subset E$, and let $\mathrm{Tau}$ be the finite set of embeddings $\tau$ of $E$ into $\mathbb{C}$ that the datum fixes. For $N \ge 1$ let $L \subset E^N$ and $L' \subset E^{N'}$ be $\mathcal{O}_E$-lattices. The pair $(N, N', L, L')$ is *admitted* if $N$ and $N'$ are even and $L$ and $L'$ are self-dual for the standard Hermitian form (see [lattices in quadratic and Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces)). Let $Y(L, L')$ be the $\mathcal{O}_E$-span of the matrices $aA$, with $a$ in a fixed ideal $\mathfrak{a}_0$ and $A$ a homomorphism from $L$ to $L'$, and put
$$h_Y(x, y) = \mathrm{Tr}_{E/K} \sum_{i,j} x_{ij}\,\overline{y_{ij}} .$$

**Definition 6.2.2 (Local basis).** A family $b_1, \dots, b_r$ of $N' \times N$ matrices over $E$ is a *local basis of $Y$ at $p$* if it is linearly independent over $K$, if $s b_i \in Y$ for some $s$ prime to $p$, and if for every $y \in Y$ there is $s$ prime to $p$ with $s y$ in the $\mathcal{O}_K$-span of the $b_i$. It is *orthonormal* if $h_Y(b_i, b_j) = \delta_{ij}$.

So a local basis is a basis of the localization $Y \otimes \mathbb{Z}_{(p)}$ over $\mathcal{O}_K \otimes \mathbb{Z}_{(p)}$. Now fix $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$, a Weierstrass model $C$ of the lattice of the datum with discriminant exactly $1$, and a parameter series $w$. Let $\ell$ be the formal logarithm and $u$ the scale of $C$, as in Section 1. For a series $F$ in variables $X_{\tau, j, k}$ ($\tau \in \mathrm{Tau}$, $j \le N'$, $k \le N$) and a local basis $b$, the *logarithmic substitution* replaces $X_{\tau, j, k}$ by
$$\sum_{i = 1}^{r} u^{-1}\,\lambda\tau(b_{i, jk})\,\ell(X_i) .$$
We write $F_b$ for the result, a series in $X_1, \dots, X_r$. The *sigma factor* is $e(X) = \prod_{i \le r} \Phi(X_i)^{-1}$, where $\Phi(X) = \sigma^*(\varepsilon\ell(X))/(\varepsilon X)$ is the function whose logarithm is the sigma series of Section 1.

Let $\Theta_{L_1, L_1'}$ be the theta kernel of an admitted pair, attached to a character $\chi$ of the ideals of $K$ that is multiplicative and satisfies $\chi((z)) = \prod \tau(z)^{-1}$ for unitary $z$ (see [theta kernels](/learn/theta/#theta-kernels)). For a torsion point $t$, $U_t$ is the translate by $t$, and $\lambda$ applied to Taylor coefficients turns a kernel into a series over $\mathbb{C}_p$.

**Definition 6.2.3 (Combination of translates).** A series $F$ is a *combination of translates* for $(L, L')$ at $p$ if
$$F = \sum_k r_k\,\lambda\bigl(U_{t_k}\Theta_{L_{1k}, L_{1k}'}\bigr),$$
where each $r_k$ is integral, each $t_k$ is a torsion point of order prime to $p$ in the lattice of $(L, L')$, and each pair $(L_{1k}, L_{1k}')$ is admitted and equals $(L, L')$ after multiplication by an integer prime to $p$.

**Theorem 6.2.4 (Integrality at an inert prime).** Let $\mathfrak{c}$ be a curve ideal, $\delta$ a twelfth root for $\mathfrak{c}$, and fix the theta data built on $\Lambda(\mathfrak{c}, \delta)$. Let $\chi$ be as above, $p \ge 5$ a prime with $\left(\frac{-d}{p}\right) = -1$, and $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ any ring map. Let $(N, N', L, L')$ be admitted. Then for every combination of translates $F$ for $(L, L')$ at $p$, every model $C$ with discriminant $1$, every parameter series $w$, and every orthonormal local basis $b$ of $Y(L, L')$ at $p$, the series $F_b \cdot e$ has integral coefficients.

Lean: `Formalism.L2.KerInert.kernels_integral_inert`

### Reduction to one copy

The proof of the theorem has three inputs, which we state first.

**Definition 6.2.5 (Weak approximation at $p$).** *Weak approximation at $p$* is the statement: for every CM field $E$ that is unramified in the sense of the datum, every prime $p$, every $n$ and every lattice $L \subset E^n$, if for each prime $P$ of $E$ above $p$ some isometry $g_P$ of the standard Hermitian form carries the standard lattice to $L$ at $P$, then a single isometry $\gamma$ carries the standard lattice to $L$ at every $P$ above $p$.

This is the shape of the weak approximation theorem for the unitary group over the places above $p$ (see [local classification](/learn/hermitian-lattices/#local-classification) and [genus, class and spinor genus](/learn/hermitian-lattices/#genus-class-and-spinor-genus)).

**Definition 6.2.6 (One-copy local basis).** A *one-copy local basis* at an inert $p \ge 5$ and $\lambda$ is a local basis $b$ of $Y(L_1, L_1)$ at $p$, for the standard lattice $L_1$ of rank $1$, with $|\mathrm{Tau}|$ elements, such that the matrix $\lambda h_Y(b_m, b_n)$ has a determinant of norm $1$ and the matrix $\lambda\tau(b_{\tau'})$ is invertible.

**Definition 6.2.7 (Orthonormal frame).** An *orthonormal frame* at $(p, \lambda, \iota)$, where $\iota : \mathbb{C} \to \mathbb{C}_p$ is a field isomorphism that extends $\lambda$, consists of a complex linear automorphism $g_1$ of $\mathbb{C}^{4 \times \mathrm{Tau}}$ and a scalar $e$ with $|\iota e| \le 1$, such that $g_1$ carries the Hermitian form of four copies of the one-copy form to the standard form, the index of the image of four copies of the lattice in the standard lattice is finite, nonzero and prime to $p$, and the fourfold tensor of the one-copy kernel is $e$ times the pullback by $g_1$ of the kernel of the standard form. It also contains a Frobenius $\sigma$ of the unramified extension, a matrix $B'$ tied to $g_1$ and $\sigma$, and an isometry $\sigma_p$ of $\mathbb{C}_p$ with $\sigma_p\lambda(x) = \lambda(\bar x)$ for $x \in K$, such that the rows of $B'$ form a local orthonormal frame of $Y(L_1, L_1)$ for $\sigma_p$.

The *one-copy integrality* is the theorem of the next definition. It says that for one copy of the standard lattice of rank $1$, there is a normalized model over the unramified ring and a local orthonormal frame in which all torsion translates of the kernel, corrected by the sigma factor, are integral.

**Definition 6.2.8 (One-copy integrality).** *One-copy integrality* holds if, for all data as in the theorem and every $\iota$ that extends $\lambda$, there are $c \ne 0$, elements $g_2, g_3, \varepsilon, s_2$ of the maximal unramified extension with $|g_2|, |g_3| \le 1$, $|g_2^3 - 27 g_3^2| = 1$ and $|\varepsilon| = 1$, which give a Lubin-Tate normalization of the lattice scaled by $c$ and an integral theta series, and there are $\sigma$ and a local orthonormal frame $v$ of $Y(L_1, L_1)$ as above, such that for every $t$ with $N t$ in the lattice for some $N > 0$ prime to $p$, the product of $\exp$ of the sum of the sigma series and the translate $U_t$ of the one-copy kernel, read in the coordinates $(\iota c)^{-1} v$, is integral.

**Proposition 6.2.9 (One copy from an orthonormal frame).** If an orthonormal frame exists for all data as in the theorem, then one-copy integrality holds.

Lean: `Formalism.L2.KerInert.oneCopyTh1S_of_isom`

*Proof.* Two facts proved elsewhere in the development are used. The first gives a scaling $c$ with normalized invariants $g_2, g_3, \varepsilon, s_2$ as in the definition, together with a norm relation of the sigma series for every Frobenius $\sigma$ of the unramified extension and every unit $\alpha$ with $\sigma^2\alpha = \alpha$. The second says: for such a scaling, the isometry $g_1$ and the scalar $e$ of an orthonormal frame, a Frobenius $\sigma$ with this norm relation, and the matrices of the frame, the corrected translates are integral. The frame gives $g_1$, $e$, $\sigma$, $B'$ and $\sigma_p$; the first fact gives the scaling and the norm relation; the second fact gives the integrality. $\square$

**Proposition 6.2.10 (Local one-copy integrality).** Assume that orthonormal frames exist and that the values at zero of the torsion translates of the standard kernels are algebraic. Then there are $\sigma$, $r$ and a local orthonormal frame $v$ of $Y(L_1, L_1)$ such that, for every torsion point $s$ of order prime to $p$, the series $\lambda(U_s \Theta_{L_1, L_1})$ is integral after the logarithmic substitution along $v$ and multiplication by the sigma factor, for every model with discriminant $1$ and every parameter series.

Lean: `Formalism.L2.KerInert.oneCopyLoc_of_isom`

*Proof.* Start from [the one-copy integrality](/entry/one-copy-th1-s-of-isom/), with an isomorphism $\iota$ that extends $\lambda$. The argument then combines four facts proved elsewhere in the development: such an extension $\iota$ exists; the algebraicity of the values at zero ties the coordinates $(\iota c)^{-1} v$ to the coordinates over $\lambda$; the model series of the curve is algebraic; and a change of the Weierstrass parameters by a constant scale changes the substitution only by that scale. So the integrality passes from the normalized model to any model with discriminant $1$. $\square$

**Theorem 6.2.11 (Integrality from weak approximation).** Assume weak approximation at $p$, the existence of an orthogonal one-copy basis (a local basis $e_i$ of $Y(L_1, L_1)$ with $h_Y(e_i, e_j) = 0$ for $i \ne j$ and $h_Y(e_i, e_i) = u_i$ a positive rational $p$-unit), and the existence of orthonormal frames. Then the conclusion of the theorem on integrality holds.

Lean: `Formalism.L2.KerInert.integral_inert_of_weakApprox`

*Proof.* Let $F$ be a combination of translates for an admitted pair $(L, L')$. The argument combines the following facts. Weak approximation gives one isometry $\gamma$ that carries the standard lattices to $L$ and $L'$ at all primes above $p$ at once. Pullback by $\gamma$ carries torsion points of order prime to $p$ to such points and kernels to kernels. If an admitted pair $(M, M')$ agrees with the standard pair up to integers prime to $p$, then each translate of its kernel by a torsion point of order prime to $p$ is a finite sum $\sum_k c_k\,U_{s_k}\Theta_{\mathrm{std}}$, with $c_k$ algebraic, $\lambda(c_k)$ integral, and $s_k$ torsion points of order prime to $p$ for the standard pair. So the claim for $(L, L')$ follows from the claim for the standard pair. Combinations of translates are stable under this pullback, and the logarithmic substitution is linear in $F$, so it is enough to treat one translate. The values of the kernels are algebraic. A local basis can be changed by a unit substitution of the coordinates without loss of integrality. For the standard pair, $Y$ is built from matrix units, and the orthogonal one-copy basis gives a global orthonormal basis for four copies. With these facts, the integrality of the fourfold product reduces to [the local one-copy integrality](/entry/one-copy-loc-of-isom/), applied with the algebraicity of the values at zero, which is proved. $\square$

**Theorem 6.2.12 (Integrality from a local basis).** Weak approximation at $p$ and the existence of a one-copy local basis imply the conclusion of the theorem on integrality.

Lean: `Formalism.L2.KerInert.integral_inert_of_approx_basis`

*Proof.* The orthogonal one-copy basis exists; this is proved in the development. A one-copy local basis gives an orthonormal frame. For this, three more facts are used, all proved: at an inert prime, conjugation of $K$ extends to an isometry $\sigma_p$ of $\mathbb{C}_p$ with $\sigma_p\lambda(x) = \lambda(\bar x)$; the frame has rational coordinates; and every element $y$ of the unramified extension with $\sigma^2 y = y$, for a Frobenius $\sigma$, lies in the closure of $\lambda(K)$ and satisfies $\sigma_p(y) = \sigma(y)$ for every such $\sigma_p$. Now apply [the theorem on weak approximation](/entry/integral-inert-of-weak-approx/). $\square$

*Proof of the theorem on integrality.* Weak approximation at $p$ and the existence of a one-copy local basis are both proved in the development. This is [the theorem on a local basis](/entry/integral-inert-of-approx-basis/) applied to them. $\square$

**Remark 6.2.13 (Formalization).** Every result of this section is stated under `variable [Fact CM2] in`, so the theorem on good models is an instance argument, not a visible hypothesis ([KernelsIntegralInert.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/KernelsIntegralInert.lean#L7)). The parent theorem supplies it. The ring map $\lambda$ in the theorem is arbitrary; nothing ties it to the curve. Models must have discriminant exactly $1$, not a unit (`IsModel`). The map `lamC` sends a complex number outside $\overline{\mathbb{Q}}$ to $0$. The sigma factor is $1$ at $p = 2$, a case the theorem excludes. The assembly lemma `intInert_of` has an unused argument `_hA` ([IntAsm.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/IntAsm.lean#L79)). We have not unfolded `IsLTNorm`, `thetaS`, `ReadTh1`, `IsFrameH` and `UnrOK`; the text describes them only by their role.
