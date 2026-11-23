---
title: Satake parameters, Schur sums and the cell decomposition
decls:
  - GlobalTheory.CellDec.cell_lintegral
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Satake parameters, Schur sums and the cell decomposition

This section sets up the objects of the chapter: the Satake parameters of a cuspidal representation, the partial Rankin-Selberg L-function, its logarithm, and the Dirichlet series built from Schur polynomials that the unfolding of a Rankin-Selberg integral produces. It ends with the cell decomposition of an integral over $N(E) \backslash \mathrm{GL}_n(\mathbb{A}_E)$, where $N$ is the upper unitriangular group. The Euler product of [the unfolded Whittaker integral](/entry/unfolded-whittaker-integral-eq-euler-product-schur-sums/) comes from this decomposition, one cell at a time.

Throughout, $E$ is a totally complex number field, $\mathbb{A} = \mathbb{A}_E$ is its ring of [adeles](/learn/number-fields/#adeles-and-ideles), and $w$ runs over the finite places of $E$, that is, the nonzero prime ideals of $\mathcal{O}_E$. For each $w$ we write $E_w$ for the completion, $\mathcal{O}_w$ for its ring of integers, $\varpi_w$ for a uniformizer, $Nw = |\mathcal{O}_E / w|$ and $K_w = \mathrm{GL}_a(\mathcal{O}_w)$. A *cuspidal representation* of $\mathrm{GL}_a$ over $E$ is an isomorphism class of irreducible spaces of cusp forms on $\mathrm{GL}_a(E) \backslash \mathrm{GL}_a(\mathbb{A})$, see [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms). It is *unitary* if its central character is a unitary [[Hecke character|KPYFGB342X]].

**Definition 8.1.1 (Satake parameters).** Let $\pi$ be a cuspidal representation of $\mathrm{GL}_a$ over $E$, let $\pi_w$ be its local component at $w$, and let $B$ be a multiset of $a$ nonzero complex numbers. Then $B$ is a *Satake parameter of $\pi$ at $w$* if $\pi_w$ has a nonzero $K_w$-fixed vector, and every nonzero $K_w$-fixed vector $v$ satisfies $T_j v = \lambda_j(B) v$ for $0 \le j \le a$. Here $T_j$ is the $j$-th standard [[Hecke operator|S4SV3QZ8B1]] of $\mathrm{GL}_a(E_w)$ and $\lambda_j(B)$ is the eigenvalue that the Satake transform attaches to $B$.

The parameter is unique when it exists. We write $\mathrm{sat}(\pi, w)$ for it, and we put $\mathrm{sat}(\pi, w) = \emptyset$ when $\pi_w$ has no parameter. We say that $\pi$ is *unramified outside* a finite set $T$ of places if $\pi$ has a Satake parameter at every $w \notin T$. See [unramified representations](/learn/representations/#unramified-representations).

**Definition 8.1.2 (Local factor and partial L-function).** For an integer $q > 1$, two finite multisets $A, B$ of nonzero complex numbers and $s \in \mathbb{C}$, put
$$L_q(A, B, s) = \prod_{\alpha \in A} \prod_{\beta \in B} (1 - \alpha \beta q^{-s})^{-1}.$$
Let $\sigma$ and $\sigma'$ be cuspidal representations of $\mathrm{GL}_a$ and $\mathrm{GL}_b$, both unramified outside $T$. Their *partial Rankin-Selberg L-function* is the [[Euler product|0C3PN4075R]]
$$L^T(s, \sigma \times \bar\sigma') = \prod_{w \notin T} L_{Nw}\big(\mathrm{sat}(\sigma, w), \overline{\mathrm{sat}(\sigma', w)}, s\big),$$
where the bar conjugates each element of the multiset. We write $\ell_w(\sigma, \sigma', s)$ for the factor at $w$.

The second argument is conjugated. For unitary $\sigma'$ this is the classical $L^T(s, \sigma \times \tilde\sigma')$ of Jacquet, Piatetski-Shapiro and Shalika, but in this chapter the conjugate is the definition. All the analysis is on the real half line $s = x > 1$.

**Definition 8.1.3 (Power sums and the Rankin-Selberg logarithm).** For a finite multiset $A$ and $k \ge 1$ let $p_k(A) = \sum_{\alpha \in A} \alpha^k$ be the $k$-th [[power sum|0ZNXZB4HNB]]. For $\sigma, \sigma'$ unramified outside $T$ and $x \in \mathbb{R}$ put
$$\log L^T(x, \sigma, \sigma') = \sum_{w \notin T} \sum_{k \ge 1} \frac{p_k(\mathrm{sat}(\sigma, w))\, \overline{p_k(\mathrm{sat}(\sigma', w))}\, Nw^{-kx}}{k},$$
whenever the double series converges absolutely.

The next two results say that this series is a logarithm of the partial L-function for $x > 1$. The first is the input from the theory of Rankin-Selberg integrals that this chapter does not reprove.

**Theorem 8.1.4 (Pole at $s = 1$).** Let $\pi$ be a unitary cuspidal representation of $\mathrm{GL}_a$ over $E$, with $a \ge 1$, unramified outside $T$. Then there is a function $L$ on $(1, \infty)$, continuous, with $L(x) \ge 1$, such that $\prod_{w \notin T} \ell_w(\pi, \pi, x)$ converges to $L(x)$ for every $x > 1$, and $(x - 1) L(x) \to c$ as $x \to 1^+$ for some $c > 0$.

Lean: `GlobalTheory.T.rankinSelberg_partialL_pole_at_one_conj`.

*Proof.* This is the simple pole of $L(s, \pi \times \tilde\pi)$ at $s = 1$, from Jacquet and Shalika, *On Euler products and the classification of automorphic representations I*. We take it as given. $\square$

**Lemma 8.1.5 (Logarithm of the partial L-function).** (1) Let $q > 1$, let $A, B$ be finite multisets and $s \in \mathbb{C}$ with $|\alpha\beta| q^{-\operatorname{Re} s} < 1$ for all $\alpha \in A$, $\beta \in B$. Then $L_q(A, B, s) = \exp \sum_{k \ge 1} p_k(A) p_k(B) q^{-ks}/k$, and the series converges. (2) Let $\sigma, \sigma'$ be unitary cuspidal representations of $\mathrm{GL}_a$ and $\mathrm{GL}_b$, unramified outside $T$, and let $x > 1$. Then the double series of $\log L^T(x, \sigma, \sigma')$ converges absolutely, and $\prod_{w \notin T} \ell_w(\sigma, \sigma', x)$ converges to $\exp \log L^T(x, \sigma, \sigma')$.

Lean: `GlobalTheory.T.localRankinSelberg_logarithm_formula` (also `GlobalTheory.JSLog.logRankinSelberg`).

*Proof.* (1) Expand $-\log(1 - z) = \sum_k z^k / k$ for $z = \alpha\beta q^{-s}$ and sum over the pairs; $\sum_{\alpha, \beta} (\alpha\beta)^k = p_k(A) p_k(B)$. (2) Each Satake parameter $\alpha$ of a unitary $\sigma$ outside $T$ has $|\alpha|^2 \le Nw$. So part (1) applies at $s = x > 1$. Take first $\sigma' = \sigma$. Then every term $|p_k|^2 Nw^{-kx}/k$ is $\ge 0$, each local factor is $e^{L_w}$ with $L_w \ge 0$, and the product of the $e^{L_w}$ converges by the pole theorem above. A product of numbers $e^{L_w} \ge 1$ that converges has $\sum_w L_w < \infty$. So the diagonal series converges. For general $\sigma, \sigma'$ the inequality $|p_k \bar p'_k| \le \frac12 (|p_k|^2 + |p'_k|^2)$ bounds the double series by the two diagonal ones. Absolute convergence then lets us exponentiate term by term. $\square$

Next come the Schur polynomials. A *partition of length at most $n$* is a sequence $\lambda = (\lambda_1 \ge \dots \ge \lambda_n \ge 0)$ of integers, and $|\lambda| = \sum_i \lambda_i$.

**Definition 8.1.6 (Schur polynomial).** For a partition $\lambda$ of length at most $n$ and $\alpha = (\alpha_1, \dots, \alpha_n)$ put
$$s_\lambda(\alpha) = \det\big(h_{\lambda_i - i + j}(\alpha)\big)_{1 \le i, j \le n},$$
where $h_k$ is the complete homogeneous symmetric polynomial of degree $k$, with $h_0 = 1$ and $h_k = 0$ for $k < 0$.

This is the Jacobi-Trudi formula, Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I, (3.4). See [Schur polynomials](/learn/combinatorics/#schur-polynomials). Shintani's formula says that $s_\lambda(\alpha)$, times a power of $q$, is the value of the spherical Whittaker function of the unramified representation with parameters $\alpha$ at $\mathrm{diag}(\varpi^{\lambda_1}, \dots, \varpi^{\lambda_n})$. So the squares $|s_\lambda|^2$ are what the unfolded integral of $|W|^2$ sums.

**Definition 8.1.7 (Schur Dirichlet series).** For $q > 1$, $\alpha \in \mathbb{C}^n$ and $x \in \mathbb{R}$ put
$$D_q(\alpha, x) = \sum_{\lambda} |s_\lambda(\alpha)|^2 q^{-|\lambda| x} \in [0, \infty],$$
the sum over all partitions of length at most $n$. For a family $\alpha = (\alpha_w)_{w \notin T}$ put $D^T(\alpha, x) = \prod_{w \notin T} D_{Nw}(\alpha_w, x)$, a product in $[0, \infty]$.

For example, if $n = 1$ then $s_{(k)}(\alpha) = \alpha^k$ and $D_q(\alpha, x) = (1 - |\alpha|^2 q^{-x})^{-1}$ when $|\alpha|^2 q^{-x} < 1$. In general, if $|\alpha_i \alpha_j| q^{-x} < 1$ for all $i, j$, the Cauchy identity $\sum_\lambda s_\lambda(\alpha) s_\lambda(\beta) t^{|\lambda|} = \prod_{i,j} (1 - \alpha_i \beta_j t)^{-1}$ (Macdonald, Chapter I, (4.3)) with $\beta = \bar\alpha$ gives $D_q(\alpha, x) = L_q(\alpha, \bar\alpha, x)$, since $s_\lambda$ has real coefficients.

Now the cells. Let $N \subset \mathrm{GL}_n$ be the upper unitriangular group. For a finite set $S$ of finite places let $U_S \subset \mathrm{GL}_n(\mathbb{A})$ be the group of $k$ with $k_w \in K_w$ for every finite $w \notin S$; it has no condition at the archimedean places or at $S$. Put $C_0 = N(\mathbb{A}) U_S$. Let $\Lambda_S$ be the group of finitely supported families $l = (l_w)$ with $l_w \in \mathbb{Z}^n$ and $l_w = 0$ for $w \in S$. Fix uniformizers $\varpi_w$ and put
$$t_l = \big(\mathrm{diag}(\varpi_w^{l_{w,1}}, \dots, \varpi_w^{l_{w,n}})\big)_w \in \mathrm{GL}_n(\mathbb{A}), \qquad d(l) = \prod_{w} Nw^{\sum_{i < j} (l_{w,i} - l_{w,j})}.$$
So $d(l) = \delta(t_l)^{-1}$, where $\delta(t) = \prod_{i < j} |t_i / t_j|$ is the modulus character of the upper triangular Borel subgroup. The cell of $l$ is $t_l C_0$.

**Theorem 8.1.8 (Cell decomposition).** Let $\mu$ be a [[Haar measure|CE0V9686M8]] on $\mathrm{GL}_n(\mathbb{A})$, let $\mathcal{F}$ be a measurable [[fundamental domain|KNJA2NEZ9F]] for the left action of $N(E)$, and let $B \colon \mathrm{GL}_n(\mathbb{A}) \to [0, \infty]$ be measurable with $B(ug) = B(g)$ for all $u \in N(\mathbb{A})$. Then
$$\int_{\mathcal{F}} B \, d\mu = \sum_{l \in \Lambda_S} d(l) \int_{\mathcal{F} \cap C_0} B(t_l g)\, d\mu(g).$$

Lean: `GlobalTheory.CellDec.cell_lintegral`.

*Proof.* First, the cells $t_l C_0$, $l \in \Lambda_S$, partition $\mathrm{GL}_n(\mathbb{A})$. Every $g$ lies in some cell by the [[Iwasawa decomposition|ZYVEVYBA41]] $\mathrm{GL}_n(E_w) = B(E_w) K_w$ at each $w \notin S$: write $g_w = u_w t_w k_w$ with $t_w$ diagonal, and read off $l_w$ from the valuations of the entries of $t_w$, which are $0$ for almost all $w$. Two cells are disjoint, since the valuations of the diagonal of $t_w$ are determined by $g_w$ modulo $N(E_w)$ on the left and $K_w$ on the right. Each cell is open, so measurable.

So $B = \sum_l B \cdot \mathbf{1}_{t_l C_0}$, and the integral of a series of nonnegative measurable functions is the series of the integrals. It remains to compute one term. Substitute $g = t_l h$; the Haar measure is invariant. The conjugation $u \mapsto t_l u t_l^{-1}$ maps $N(\mathbb{A})$ into itself. Since $B$ is left $N(\mathbb{A})$-invariant, the integral of a left $N(\mathbb{A})$-invariant function over a fundamental domain for $N(E)$ is the volume of $N(E) \backslash N(\mathbb{A})$ times an integral over $N(\mathbb{A}) \backslash \mathrm{GL}_n(\mathbb{A})$. Conjugation by $t_l$ changes this volume by the modulus factor, and the result is the integral of $h \mapsto B(t_l h) \mathbf{1}_{C_0}(h)$ over $\mathcal{F}$, times $\delta(t_l)^{-1} = d(l)$. $\square$

**Remark 8.1.9 (Formalization).** The definitions are in [UnrOutside.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnrOutside.lean#L16) (the choice $\mathrm{sat}$, which returns $0$, the empty multiset, when there is no parameter; there is also an `example` at line 27 proved by `rfl`), [RsTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RsTerm.lean#L14), [SchurDir.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SchurDir.lean) (with an `example` at line 26 for the empty product) and [IsAddHaarMeasureVolumeLie.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsAddHaarMeasureVolumeLie.lean#L11). The eigenvalue $\lambda_j(B)$ is `satEig`, which we have not unfolded. The partial L-function `partialL` in UnrOutside.lean has no conjugation; every statement of this chapter writes the conjugated product directly. The pole theorem is a one-line wrapper of `RSPole.rs_pole_conj`, whose proof we did not open. The bound $|\alpha|^2 \le Nw$ in the logarithm lemma is `sq_norm_le` in [LocalRankinSelbergLogarithmFormula.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalRankinSelbergLogarithmFormula.lean#L112); its proof is by contradiction from a lemma we did not open. In the cell theorem the partition of the group into cells and the change of variables are separate lemmas, `exists_tl_inv_mul_mem_C0_off_finset`, `adelic_iwasawa_cells_disjoint_off_finset` and `lintegral_uniformizerTorus_translate_unipotentQuotient`.
