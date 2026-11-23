---
title: Theta jets at split primes
decls:
  - Formalism.L2.AlgTh.etLoc
  - Formalism.L2.AlgTh.split_place_scaled_bound
  - Formalism.L2.AlgTh.jetAtSplit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta jets at split primes

This section bounds the $p$-adic size of the Taylor jets of Hermitian theta functions with complex multiplication. The first theorem treats translates of a theta function by torsion points of order prime to $p$. The second treats a twisted average of translates at a prime $p$ that splits in $K$. The third applies the second to the theta kernel of a pair of self-dual lattices. The input from the rest of this chapter is the integrality of torsion points on a curve with good reduction. The last theorem is the input of [the jet bound for the ambient kernel of a seam](/entry/jet-at-split-amb-of/).

### Setting

**Definition 7.7.1 (CM datum).** A *CM datum* is $(a_0, b_0, c_0, d)$ with $a_0 > 0$ odd, $d$ a prime with $d \equiv 7 \pmod 8$, and $4 a_0 c_0 = b_0^2 + d$. Put $\theta_0 = (b_0 + i\sqrt d)/2$. For $\lambda \ne 0$ let $L$ be the lattice $\lambda(\mathbb{Z} a_0 + \mathbb{Z}\theta_0)$, and for a prime $p$ and a field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_p$ let $C$ be the curve $y^2 = x^3 - \frac{\iota g_2(L)}{4} x - \frac{\iota g_3(L)}{4}$.

Since $b_0$ is odd, $\theta_0 - \omega_K \in \mathbb{Z}$, so $L$ has complex multiplication by $\mathcal{O}_K$, $K = \mathbb{Q}(\sqrt{-d})$. We say that $C$ is *integral* if its coefficients have absolute value at most $1$ and its discriminant has absolute value $1$.

Let $h$ be an $n \times n$ positive definite Hermitian matrix, $H(z, w) = z^* h w$ on $\mathbb{C}^n$, and $\Lambda \subset \mathbb{C}^n$ a lattice that is self-dual for $H$ and stable under multiplication by $\theta_0$. Let $\alpha(x) = \exp(\pi i \frac{\sqrt d}{2} \operatorname{Re} H(x, x))$. For $x \in \mathbb{C}^n$ and a function $F$ put
$$(U_x F)(z) = F(z + x)\, \exp\bigl(-\pi H(z, x) - \tfrac{\pi}{2} H(x, x)\bigr).$$
A *theta function* for $(H, \alpha, \Lambda)$ is an entire function $\theta$ on $\mathbb{C}^n$ that is fixed by the operators $U_x$ twisted by $\alpha(x)$, for $x \in \Lambda$.

**Definition 7.7.2 (Local normalization).** The theta function $\theta$ is *normalized at* $(p, \iota)$ if there are a linear isomorphism $g$ of $\mathbb{C}^{4n}$, which carries the form of $\operatorname{diag}(h, h, h, h)$ to the standard form of $L$, and $\varepsilon \in \mathbb{C}$ with $|\iota\varepsilon| \le 1$, such that the index of $g(\Lambda^4)$ in the standard lattice $L^{4n}$ is finite, nonzero and prime to $p$, and
$$\theta(z_1)\theta(z_2)\theta(z_3)\theta(z_4) = \varepsilon\, \kappa(g(z_1, z_2, z_3, z_4)),$$
where $\kappa$ is the standard theta kernel of $L$ on $\mathbb{C}^{4n}$.

For a function $F$ on $\mathbb{C}^n$ let $T(F)$ be its Taylor series at $0$. For a matrix $B$ with entries in $\mathbb{C}_p$, let $T_B(F)$ be the series obtained from $T(F)$ by applying $\iota$ to the coefficients and substituting $z = B w$. A power series $S$ in variables $w_\nu$ has *integral jets* if $|\mu!\, S_\mu| \le 1$ for every multi-index $\mu$, where $S_\mu$ is the coefficient of $w^\mu$.

### Translates by torsion points

**Theorem 7.7.3 (Jets of torsion translates).** Let $(a_0, b_0, c_0, d)$ be a CM datum, $\lambda \ne 0$, and $h, \Lambda, \theta$ as above. Let $p \ne 2$ be a prime with $p \nmid d$ and let $\iota$ be such that $C$ is integral and $\theta$ is normalized at $(p, \iota)$. Let $r_k \in \mathbb{C}_p$ with $|r_k| \le 1$, $t_k \in \mathbb{C}^n$, $\beta \in \mathbb{Z}[\omega_K]$ with $|\iota\beta| = 1$, and $M > 0$, with $\beta t_k \in \Lambda$ and $M t_k \in \Lambda$ for all $k$. Let $v_j \in \mathbb{C}^n$ with $L v_j \subseteq \Lambda$ and $A_{j\nu} \in \mathbb{C}_p$ with $|A_{j\nu}| \le |M|$, and let $B_{i\nu} = \sum_j \iota(v_{j,i}) A_{j\nu}$. Then the series
$$S = \sum_k r_k\, T_B(U_{t_k}\theta)$$
has integral jets, and $\bigl|\sum_\mu P_\mu\, \mu!\, S_\mu\bigr| \le 1$ for every polynomial $P = \sum_\mu P_\mu w^\mu$ with $|P_\mu| \le 1$.

Lean: `Formalism.L2.AlgTh.etLoc`

*Proof.* The product of four copies of a translate $U_{t}\theta$, after the change of variables $g$ of the normalization, equals $\varepsilon$ times a sum, with integral coefficients, of products over the coordinates of translates of the one-variable theta function of $L$ by points $s$ with $N' \beta s \in L$ and $N' M s \in L$, where $p \nmid N'$.

Lean: `Formalism.L2.AlgTh.tensZEt`

The coordinates of a point of $C$ killed by an element $\beta$ of $\mathbb{Z}[\omega_K]$ with $|\iota\beta| = 1$ are integral. This is the integrality of torsion points of [the section on torsion](/entry/tor-kur/), extended to the kernel of $\beta$.

Lean: `Formalism.L2.AlgTh.unitKerInt`

The translates of the one-variable theta function by such points have integral jets. The proof goes through the logarithmic derivative, whose jets are integral by these coordinates. Products and integral linear combinations keep integral jets.

Lean: `Formalism.L2.AlgTh.etThetaZ` (also `Formalism.L2.AlgTh.etJetsSigma`)

A scaling lemma for linear substitutions, which uses $|A_{j\nu}| \le |M|$, then gives integral jets for $S$. The bound for $P$ follows from the ultrametric inequality. $\square$

Lean: `Formalism.L2.AlgTh.linScale`

### Twisted averages at a split prime

Let $p$ split in $K$, so $p = \pi\bar\pi$ with $\pi \in \mathbb{Z}[\omega_K]$. Let $S_a$ be a set of representatives of $(\bar\pi/\pi)\Lambda$ modulo $\bar\pi\Lambda$, and $S_b$ a set of representatives of $\Lambda$ modulo $\bar\pi\Lambda$. Let $E_H(x, y) = \operatorname{Im} H(x, y)$, and let $\Psi$ be a function on $\mathbb{C}^n$. For $q > 0$ put
$$\hat\Psi(a) = \frac{1}{q} \sum_{b \in S_b} \Psi(b)\, e^{-2\pi i E_H(b, a)}, \qquad \xi(z) = \sum_{a \in S_a} \hat\Psi(a)\, \alpha(a)\, (U_a \theta)(z).$$

**Lemma 7.7.4 (Scalar constant).** If $\alpha$ is a semicharacter on $\Lambda$, $\pi\bar\pi = p$, $\bar\pi \ne \pi$, $\pi\Lambda, \bar\pi\Lambda \subseteq \Lambda$, $u\pi + w\bar\pi = 1$ for some $u, w$ that preserve $\Lambda$, and $\theta \ne 0$ lies in a space of theta functions of dimension at most one, then $|S_a| = p^n$ and there is $c$ with $c^8 = (\bar\pi/\pi)^{4n}$ such that
$$\theta\bigl(\tfrac{\pi}{\bar\pi} z\bigr) = c\, p^{-n/2} \sum_{a \in S_a} \alpha(a)\, (U_a\theta)(z).$$

Lean: `Formalism.L2.AlgTh.scalarConst` (also `Formalism.L2.AlgTh.xiSwap`)

**Theorem 7.7.5 (Scaled bound at a split place).** Let $(a_0, b_0, c_0, d)$, $\lambda$, $h$, $\Lambda$, $\theta$, $p$ and $\iota$ be as in the theorem on torsion translates. Let $\pi \in \mathbb{Z}[\omega_K]$ with $\pi\bar\pi = p$, and let $S_a$, $S_b$ be as above. Let $\Psi$ with $|\iota\Psi(b)| \le 1$ for $b \in S_b$. Let $r_k \in \mathbb{C}$ with $|\iota r_k| \le 1$, $t_k \in \mathbb{C}^n$ and $N > 0$ with $p \nmid N$ and $N t_k \in \Lambda$. Let $v_j$ with $L v_j \subseteq \Lambda$ and $A_{j\nu}$ with $|A_{j\nu}| \le |\iota\bar\pi|$, and $B$ as before. Let $\xi$ be built with $q = p^n$. Then
$$p^n \sum_k \iota(r_k)\, T_B(U_{t_k}\xi)$$
has integral jets.

Lean: `Formalism.L2.AlgTh.split_place_scaled_bound`

*Proof.* Since $\pi\bar\pi = p$ and $\pi, \bar\pi$ are coprime, exactly one of $|\iota\pi|, |\iota\bar\pi|$ is less than $1$.

If $|\iota\bar\pi| < 1$, then $|\iota\bar\pi| = |p|$ and $|A_{j\nu}| \le |p|$. Each translate $U_a\theta$ with $a \in S_a$ is a translate by a point killed by $\pi$, which is a unit at $\iota$. The factor $p^n$ clears the denominator $q$, and the theorem on torsion translates applies to these translates.

Lean: `Formalism.L2.AlgTh.xiEt`

If $|\iota\bar\pi| = 1$, the lemma on the scalar constant and a finite Fourier inversion rewrite $\xi$ as a multiple of a sum over $b \in S_b$ of translates of $\theta$ by the points $\frac{\pi}{\bar\pi}b$, evaluated at $\frac{\pi}{\bar\pi}z$. These points are killed by $\bar\pi$, a unit at $\iota$. The theorem on torsion translates then gives integral jets even without the factor $p^n$, and with $|A_{j\nu}| \le 1$. $\square$

Lean: `Formalism.L2.AlgTh.xiConn`

### The kernel at a split prime

Now let $E$ be the number field with involution, $\mathrm{Tau}$ the finite set of embeddings and $\sigma_0$ the embedding of the ambient data of the [chapter on inert primes](/entry/jet-at-split-amb-of/). Let $N, N'$ be self-dual $\mathcal{O}_E$-lattices of ranks $a, b$, and $S$ a finite set of primes of $E$. The ambient kernel of the pair has jets $J_S(N, N'; c, x, m)$, for a level $c$, a point $x$ of the space of homomorphisms from $E^a$ to $E^b$, and a multi-index $m$.

**Theorem 7.7.6 (Jets of the kernel at a split prime).** Let $p \ne 2$ be a prime with $p \nmid d$, and let $\iota : \mathbb{C} \to \mathbb{C}_p$. Assume that the kernel of $(N, N')$ is standard at $(p, \iota)$ for a CM datum $(a_0, b_0, c_0, d)$ and $\lambda \ne 0$, and that the hypotheses of the ambient kernel on $(a, b, S)$ hold. Let $\pi \in \mathbb{Z}[\omega_K]$ with $\pi\bar\pi = p$, and $p_E \in \mathcal{O}_E$ that every embedding sends to $\pi$, such that a prime $P$ of $E$ above $p$ lies in $S$ exactly when $p_E \notin P$. Then for every $c' > 0$ with $p \nmid c'$, every $x$ in the lattice of level $c'$ of homomorphisms from $N$ to $N'$ at $S$, and every multi-index $m$,
$$\bigl|\iota\sigma_0\bigl(J_S(N, N'; p c', x, m)\bigr)\bigr| \cdot |\iota\bar\pi|^{\deg m} \cdot |p|^{|\mathrm{Tau}|\, a b} \le 1 .$$

Lean: `Formalism.L2.AlgTh.jetAtSplit`

*Proof.* The proof splits the representatives of the lattice of level $pc'$ into a part of level $c'$ and a part at $p$, describes the part at $p$ through $\bar\pi$ and counts it, and expands the kernel in Taylor jets. After a diagonal linear substitution of the variables, which accounts for the factor $|\iota\bar\pi|^{\deg m}$, the jet at $x$ is given by a series of the form in the theorem on the scaled bound, with $N = c'$. That theorem gives the bound. $\square$

Lean: `Formalism.L2.AlgTh.jetAtSplit_of` (also `Formalism.L2.AlgTh.kernel_index_form`, `Formalism.L2.AlgTh.representatives_split`, `Formalism.L2.AlgTh.linear_substitution_diagonal`)

**Remark 7.7.7 (Formalization).** The theorem on jets of the kernel is in a file named for norm scaling: [LocNormScale.lean](lean:Formalism/LocalToGlobal/AlgebraicTheory/LocNormScale.lean#L12). The theorem on torsion translates is in a file named for column bounds: [ColBoundOfPaths.lean](lean:Formalism/LocalToGlobal/AlgebraicTheory/ColBoundOfPaths.lean#L26). The name of the statement of the torsion theorem is also used for an unrelated property of schemes at [LeafChartRing.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafChartRing.lean#L13). The Hermitian form of a matrix, the standard form of a lattice and the block matrix are each defined twice, at [IsUnitaryK.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/UniformGaussModels/OrthogonalGaussModels/HermitianBlockFrames/IsUnitaryK.lean#L82) and [IsSemiChar.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/IsSemiChar.lean#L98). The integrality of kernel points takes a squarefree hypothesis that it does not use: [UnitKer.lean](lean:Formalism/LocalToGlobal/AlgebraicTheory/AlgebraicTheoryProofs/UnitKer.lean#L523).
