---
title: Doubling and the non-vanishing of the down lift
decls:
  - GlobalTheory.CompanionTheory.InertZetaTop.unramDoublingInert
  - GlobalTheory.Core.Rk.Exh.Top.downNe_of_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Doubling and the non-vanishing of the down lift

This section uses the residue theorem of the last section through [the doubling method](/learn/theta/#the-doubling-method). The doubling zeta integral of a cusp form $u$ is an integral of a Siegel Eisenstein series on the doubled group against $u \otimes \bar u$. At almost all places it is an Euler product of local factors, and the first part of the section computes the local factor at an unramified inert place. The second part proves that the [global theta lift](/learn/theta/#the-global-theta-lift) of $u$ from a definite unitary group of rank $r + t$ down to a unitary group of rank $r$ is not zero, when the Satake parameters of $u$ are those of a lift from rank $r$. If all lifts were zero, the residue theorem would make the residue of the zeta integral at $s = t/2$ vanish, but the Euler product has a simple pole there.

### The unramified doubling integral at an inert place

Let $L$ be a complete field with a discrete valuation, a uniformiser $\varpi$ and ring of integers $\mathcal{O}$. Let $\sigma$ be a field automorphism of $L$ with $\sigma^2 = 1$ that preserves the valuation and fixes $\varpi$, and assume that some $x \in \mathcal{O}$ has $\sigma(x) - x \in \mathcal{O}^\times$. Let $q \ge 2$ and assume that the residue field of $L$ has $q^2$ elements. So $L$ is an unramified quadratic extension of the fixed field of $\sigma$, whose residue field has $q$ elements. We call these data an *unramified inert place*. Let $\operatorname{ord}$ be the valuation, with $\operatorname{ord}(\varpi) = 1$.

Let $J_n$ be the $n \times n$ matrix with ones on the antidiagonal and zeros elsewhere. Let $U_n$ be the group of $g \in GL_n(L)$ with $\sigma(g)^{T} J_n g = J_n$, and let $K_n \subset U_n$ be the subgroup of matrices with entries in $\mathcal{O}$. Let $G$ be the unitary group of the doubled Hermitian space of $J_n$, let $P \subset G$ be the Siegel parabolic subgroup that stabilises the diagonal, with Levi map $a \colon P \to L^\times$ given by the determinant on the diagonal, let $K_G$ be the integral points of $G$, and let $\iota(g) = \iota(g, 1)$ be the embedding of the first copy of $U_n$ in $G$.

**Definition 5.8.1 (Spherical section and zonal function).** Let $\chi \colon L^\times \to \mathbb{C}^\times$ be an unramified character, that is, $\chi = 1$ on $\mathcal{O}^\times$, and let $s \in \mathbb{C}$. A *spherical section* of parameter $s$ for $\chi$ is a function $\Phi$ on $G$ with
$$\Phi(pk) = \chi(a(p))\, q^{-2 \operatorname{ord}(a(p))(s + n/2)}, \qquad p \in P,\ k \in K_G.$$
Let $\alpha = (\alpha_1, \dots, \alpha_{\lfloor n/2 \rfloor})$ be nonzero complex numbers. A *zonal function* with Satake parameter $\alpha$ is a function $w$ on $U_n$ that is left and right invariant under $K_n$, has $w(1) = 1$, and is an eigenfunction of the Hecke algebra of $(U_n, K_n)$ with the eigenvalues given by the Satake transform at $\alpha$.

Put $\varepsilon = \chi(\varpi)$, $X = \varepsilon q^{-(2s+n)}$ and $y = \varepsilon q^{-(2s+1)}$. For $m \in \mathbb{N}$ put
$$\begin{aligned} L(z, \alpha, \varepsilon) &= \prod_{i} \bigl(1 - \alpha_i \varepsilon q^{-2z}\bigr)^{-1} \bigl(1 - \alpha_i^{-1} \varepsilon q^{-2z}\bigr)^{-1} \cdot \bigl(1 - \varepsilon q^{-2z}\bigr)^{-\delta_n}, \\ d_m(s) &= \prod_{i=0}^{n-1} \bigl(1 - (-1)^{m+i} q^{-(2s+n-i)}\bigr)^{-1}, \end{aligned}$$
where $\delta_n = 1$ if $n$ is odd and $\delta_n = 0$ if $n$ is even. The first is the local standard $L$-factor of base change, and $d_m$ is a product of local factors of the powers of the quadratic character of the inert extension.

**Theorem 5.8.2 (Unramified doubling integral at an inert place).** Let $L$ be an unramified inert place, $\mu$ a Haar measure on $U_n$ with $\mu(K_n) = 1$, $\chi$ an unramified character, $s \in \mathbb{C}$, $\Phi$ a spherical section of parameter $s$ for $\chi$, and $w$ a zonal function with Satake parameter $\alpha$. Put $I = \int_{U_n} \Phi(\iota(g))\, w(g)\, d\mu(g)$.

1. If $|y| < 1$ and $|y|\,|\alpha_i|^{\pm 1} < 1$ for all $i$, then the integrand is integrable,
$$I = \prod_{j=0}^{n-1} \bigl(1 - (-q)^j X\bigr) \cdot \prod_i (1 - y\alpha_i)^{-1} (1 - y\alpha_i^{-1})^{-1} \cdot (1 - y)^{-\delta_n},$$
and $I = L(s + \tfrac12, \alpha, \varepsilon) / d_m(s)$ for each $m \in \mathbb{N}$ with $\varepsilon = (-1)^m$.
2. If $n \le 1$, then the integrand is integrable and $I = 1$.

Lean: `GlobalTheory.CompanionTheory.InertZetaTop.unramDoublingInert`.

*Proof.* Each $g \in U_n$ has a length $\ell(g) \ge 0$, read off from the elementary divisors of $g$; it depends only on the double coset $K_n g K_n$. We take as given that for $g$ of length $\ell$ there is $k \in K_G$ with $\iota(g)k \in P$ and $\operatorname{ord}(a(\iota(g)k)) = \ell$. Since $\chi$ is unramified and $\Phi$ is right invariant under $K_G$, this gives $\Phi(\iota(g)) = X^{\ell(g)}$. The integrand is right invariant under $K_n$, and $\mu(K_n) = 1$, so $I$ is the sum of $X^{\ell(g)} w(g)$ over the cosets $gK_n$, as soon as this sum converges absolutely.

For part 1 we take as given that there is a spherical function $\varphi$ on $U_n$ with Satake parameter $\alpha$ and the same Hecke eigenvalues as $w$, and that
$$\sum_{g K_n} X^{\ell(g)} \varphi(g) = \prod_{j=0}^{n-1} \bigl(1 - (-q)^j X\bigr) \cdot \prod_i (1 - y\alpha_i)^{-1} (1 - y\alpha_i^{-1})^{-1} \cdot (1 - y)^{-\delta_n}$$
in the stated domain. This generating function identity is a counting result for lattices; its inputs are the Smith normal form, index formulas for lattices and Heisenberg groups, a Levi decomposition of the cosets, and a recursion in $n$. We take these inputs as given. Since $X^{\ell}$ is bi-invariant under $K_n$ and $w$ and $\varphi$ have the same Hecke eigenvalues, a double coset swap gives the same sum with $w$ in place of $\varphi$. This proves the first formula.

For the second formula, let $\varepsilon = (-1)^m$. Then $(-q)^j X = (-1)^{m+j} q^{-(2s+n-j)}$, so the first product is $d_m(s)^{-1}$. Also $\varepsilon q^{-2(s+1/2)} = y$, so the other two factors are $L(s + \frac12, \alpha, \varepsilon)$.

For part 2, let $n \le 1$. We take as given that then every element of $U_n$ lies in $K_n$. So there is one coset, of length $0$, and $I = X^0 w(1) = 1$. $\square$

### Non-vanishing of the down lift

Now let $E/F$ be a CM extension. We take the global data of the [Theorem 8.53 of Volume 15](/entry/down-ne-k-of-hypotheses-prime/) that uses this section. In short, they are the following:

- a positive definite Hermitian space $A$ of rank $n = r + t$ and a Hermitian space $W$ of rank $r \ge 1$ with the signature condition, with characters $\chi_A$, $\chi_W$ and a Weil representation $\omega$ of the pair $(U(A), U(W))$;
- a finite set $Z$ of places, a level subgroup of $U(A)$ at $Z$, an idempotent attached to $Z$, and the condition that the places above $2$ split in $E$;
- a cusp form $u$ on $U(A)$ that is right invariant under the level subgroup, with Satake parameters $P_w$ at the places $w$ outside $Z$, such that $\chi_W$ is unramified outside $Z$;
- a Schwartz function $\Phi$ for $(A, W)$ that is spherical outside $Z$, fixed by the level subgroup, and has a nonzero archimedean pairing with $u$.

The *lift hypothesis* says that $r + 5 \le t$ and that, outside a finite set, $P_w$ is the lift of a parameter $c_w$ of size $r$ twisted by $\chi_W$ and a segment of length $t$, where each entry $b$ of $c_w$ has $|b| \le N(w)^{(r-1)/2}$ and $|\chi_W(w)| = 1$. Assume it holds for $u$.

We use four statements as hypotheses. The *doubling package* says that Siegel Eisenstein series on doubled groups continue meromorphically with finite order at each point, and that the doubling zeta integrals of cusp forms satisfy the basic identity and continue. The *residue theorem* is the statement of [Theorem 5.7.3](/entry/res-core/) for all data. The *simple pole statement* says that, under the lift hypothesis, the partial $L$-function of $P$ twisted by $\chi_W^{-1}$ is the partial $L$-function of $c$ times $t$ shifted zeta functions, and has a simple pole at $(1+t)/2$. The *Euler identity* says that for $\operatorname{Re} s > n + 1$ the doubling zeta integral of $u$ for an unramified pair of Schwartz functions is
$$\frac{L^Z(s + \tfrac12, P, \chi_W)}{d^Z(s)} \cdot \int_{\mathrm{off}\, Z} (\text{integrand}),$$
where the last integral is over the open set of $g$ whose components outside $Z$ are integral, and $d^Z$ is the product of the normalising factors outside $Z$. The local factor at an inert place is given by the theorem above.

**Theorem 5.8.3 (Non-vanishing of the down lift).** Assume the doubling package, the residue theorem and the simple pole statement, and let $E/F$ be a CM extension that satisfies the Euler identity. Take global data as above, and assume the lift hypothesis. Then the theta lift of $u$ to $U(W)$ is not zero: there are a theta function $f$ of the pair $(A, W)$ and $h \in U(W)(\mathbb{A})$ such that the theta lift of $u$ by $f$ is nonzero at $h$.

Lean: `GlobalTheory.Core.Rk.Exh.Top.downNe_of_core`.

*Proof.* Assume that all lifts of $u$ to $U(W)$ vanish. Write $B = W \oplus H$, where $H$ is a sum of $t$ hyperbolic planes, so $B$ has rank $r + 2t = n + t$. The lift hypothesis gives $r + 5 \le t$, so $r < t$ and $r + 2 < 2t$, as the residue theorem needs. Build Weil representations for the pairs $(A, H)$ and $(A, B)$ and for the doubled pairs. We take as given a vacuum vector $f_H \ne 0$ for $(A, H)$ that is fixed by the level subgroup and by the real points of $U(A)$, and whose matrix coefficient vanishes off the level subgroup. The product $\Phi_B = \Phi \otimes f_H$ is a Fock vector for $(A, B)$ and is spherical outside $Z$.

Since all lifts of $u$ to $U(W)$ vanish, an input that we take as given shows that the doubling integrals of the theta functions of the doubled pair for $W$ against $u \otimes \bar u$ vanish. The residue theorem, applied on the doubled group with the section of $\Phi_B \otimes \bar\Phi_B$, now gives a residue $E_1$ of the Siegel Eisenstein series at $s_0 = t/2$ whose doubling integral against $u \otimes \bar u$ is zero. Here $s_0 = (m_B - n)/2 = t/2$.

Let $\mathcal{Z}(s)$ be the doubling zeta integral of $u$ for $\Phi_B$. By the doubling package, $\mathcal{Z}$ is an integral over $U(A)$ for $\operatorname{Re} s > n/2$ and continues. The group $U(A)(F) \backslash U(A)(\mathbb{A})$ is compact because $A$ is definite, so $u$ is bounded and integrable. An input that we take as given identifies the coefficient of $(s - t/2)^{-1}$ in the Laurent expansion of $\mathcal{Z}$ with the doubling integral of $E_1$. So this coefficient is $0$.

On the other side, an input that we take as given shows that this last integral is a constant $C \ne 0$, independent of $s$. The Euler identity gives
$$\mathcal{Z}(s) = \frac{L^Z(s + \tfrac12, P, \chi_W)}{d^Z(s)}\, C \qquad \text{for } \operatorname{Re} s > n + 1.$$
By the simple pole statement, the right side has a simple pole at $s + \frac12 = (1 + t)/2$, that is, at $s = t/2$, and a last input that we take as given turns this into a nonzero coefficient of $(s - t/2)^{-1}$ in $\mathcal{Z}$. This is a contradiction. $\square$

**Remark 5.8.4 (Formalization).** In the theorem on the inert place, part 2 is only for $n \le 1$, where $U_n$ is compact and the result is immediate; the second formula of part 1 needs $\chi(\varpi) = (-1)^m$, so it applies only when $\chi(\varpi) = \pm 1$ ([UnramDoublingInert.lean](lean:Development/AutomorphicSpectrum/Proofs/TwistedProofs/UnramDoublingInert.lean#L109)). The doubling package has a conjunct that is the trivial statement "true" ([DmOfHyp.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinResidues/AnisotropicGlobalForms/DmOfHyp.lean#L18)). The proof of the non-vanishing theorem is a copy of an older proof in which the published regularised Siegel-Weil formula is replaced by the residue theorem and the doubling package ([Rethread.lean](lean:Development/WeilBound/RepresentationTheoryGL/RegularisedSiegelWeil/ResidueVanishing/Rethread.lean#L19), compare [EulerFactorFromDoubling.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/EulerFactorFromDoubling.lean#L60)). We describe the global data in short form, and we have not opened the proofs of the inputs named in the two proofs.

## Notes and references

The chapter feeds into two places. The residue theorem and the non-vanishing of the down lift give the [non-vanishing step](/entry/down-ne-k-of-hypotheses-prime/) of the [unitary hypotheses](/proof/unitary-hypotheses/), and the unramified doubling integral at an inert place gives the [inert local factor](/entry/triv/) of the chapter on Howe duality. The residue theorem is the first term identity of the regularised [Siegel-Weil formula](/proof/siegel-weil/), in the form that these steps use.

- S. Kudla and S. Rallis, *A regularized Siegel-Weil formula: the first term identity*, Ann. of Math. 140 (1994), 1-80, main theorem.
- A. Ichino, *A regularized Siegel-Weil formula for unitary groups*, Math. Z. 247 (2004), 241-277, main theorem.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254 (1987), Part A, the doubling method.
- J.-S. Li, *Non-vanishing theorems for the cohomology of certain arithmetic quotients*, J. Reine Angew. Math. 428 (1992), 177-217, the unramified doubling integral.
- S. Rallis, *Langlands' functoriality and the Weil representation*, Amer. J. Math. 104 (1982), 469-515, the unramified theta correspondence.
