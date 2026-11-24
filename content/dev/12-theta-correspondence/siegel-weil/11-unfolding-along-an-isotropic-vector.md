---
title: Unfolding along an isotropic vector
decls:
  - GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.Struct.stab_structure
  - GlobalTheory.T.stabiliser_splitting_adelic
  - GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.meanP
  - GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.unfold_frames
  - GlobalTheory.T.hyperbolic_plane_unfolding_integral
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unfolding along an isotropic vector

This section proves the unfolding identity that the [hyperbolic step](/entry/hyp-step/) of the singular case uses. A theta integral over the isotropic frames of the hyperbolic extension $J^+$ is written as a theta integral over isotropic lines of $J^+$, of a function that is itself a theta integral over the isotropic frames of $J$. The proof is the classical one: sort the frames by their first vector, move the first vector to $e_0$ by a rational element, and average over the stabiliser of $e_0$, which is a semidirect product of $U_J$ and a unipotent group. The average over the unipotent part is Siegel's mean value theorem for a lattice.

We use the hyperbolic extension $J^+$, the vector $e_0$, the frames $c(a, Y)$ and the theta measure of [the section on Gram fibres](/entry/local-stages/) and [the singular case](/entry/sw-free-singular/). Let $E/F$ be a CM extension with conjugation $\sigma$, and let $J$ be a nondegenerate Hermitian matrix of size $M$, see [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms). Write $U$ for $U_{J^+}$ and $U_J$ for the unitary group of $J$, see [unitary groups](/learn/groups/#unitary-groups).

**Definition 4.11.1 (Stabiliser of the isotropic vector).** Let $P \subseteq U(\mathbb{A})$ be the stabiliser of $e_0$, and let $P(F) = P \cap U(F)$ be its rational points. Let $\operatorname{Fr}_1$ be the set of rational frames of $0_{n+1}$ for $J^+$ whose first vector is $e_0$. For $\Phi \ge 0$ on adelic $(n+1)$-tuples and $g \in U(\mathbb{A})$ put
$$\Phi_A(g) = \sum_{X \in \operatorname{Fr}_1} \Phi(g^{-1} X).$$

**Definition 4.11.2 (Covolume one).** An additive Haar measure $dA$ on $\mathbb{A}_E^n$ has covolume one if some fundamental domain for the rational points $E^n$ has measure 1.

The first theorem gives the structure of $P$. It is the adelic form of the Levi decomposition of the parabolic subgroup that fixes an isotropic line, see [parabolic subgroups](/learn/groups/#parabolic-subgroups).

**Theorem 4.11.3 (Structure of the stabiliser).** Let $E/F$ be CM and $J$ nondegenerate. There are continuous homomorphisms $\iota \colon U_J(\mathbb{A}) \to P$ and $\pi \colon P \to U_J(\mathbb{A})$ with the following properties.

1. $\pi \circ \iota$ is the identity, and $\iota$ and $\pi$ map rational points to rational points.
2. Modulo the rational elements of $\ker \pi$, the group $\ker \pi$ is covered by a compact set.
3. $\iota(u)$ acts on frames by $\iota(u) \cdot c(a, Y) = c(a, uY)$.
4. For each linearly independent rational tuple $Y$ of length $n$ there is a continuous, additive and onto map $l \colon \ker \pi \to \mathbb{A}_E^n$, rational on rational points, such that
$$m \cdot c(a, Y) = c\bigl(a + l(m), Y\bigr) \qquad (m \in \ker \pi).$$

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.Struct.stab_structure` (also `GlobalTheory.T.stabiliser_splitting_adelic`, a second name).

*Proof.* In the basis $e_0$, $f_0$, $E^M$ of $J^+$, with $f_0$ the second vector of the hyperbolic plane, an element of $P$ is block upper triangular: it fixes $e_0$, maps the orthogonal complement of $e_0$ to itself, and so induces a unitary map of $e_0^\perp / E e_0 \cong E^M$. This induced map is $\pi$. The map $\iota$ embeds $U_J$ as the block $1 \oplus 1 \oplus u$. Both are given by polynomials in the entries, so they are continuous and rational. The kernel of $\pi$ is the unipotent radical: its elements are
$$\begin{aligned} e_0 &\mapsto e_0, \\ y &\mapsto y + \langle y, x \rangle e_0, \\ f_0 &\mapsto f_0 - x + t e_0, \end{aligned}$$
with $x \in \mathbb{A}_E^M$ and $t$ fixed by $x$ up to an element of trace zero. This group is an extension of $\mathbb{A}_E^M$ by the trace zero line, and each piece is compact modulo its rational points; this gives (2). For (3), $\iota(u)$ fixes $e_0$ and the hyperbolic coordinates. For (4), $m$ sends $(a_j, 0, y_j)$ to $(a_j + \langle y_j, x \rangle, 0, y_j)$, so $l(m) = (\langle y_j, x \rangle)_j$. It is onto because the $y_j$ are linearly independent and $J$ is nondegenerate. $\square$

**Theorem 4.11.4 (Mean over the stabiliser).** Let $E/F$ be CM and $J$ nondegenerate, let $n \ge 0$, let $\mu_1$ be a Haar measure on $U_J(\mathbb{A})$ with a fundamental domain $\mathcal{F}_1$, and let $dA$ have covolume one. Let $\Phi \ge 0$ be measurable on adelic $(n+1)$-tuples and $\Psi \ge 0$ a function on adelic vectors with
$$\Psi(h e_0) = \int \int \Phi\bigl(h \, c(a, Y)\bigr) \, dA(a) \, d\Theta_{\operatorname{Fr}_J(0_n)}(Y)$$
for all $h \in U(\mathbb{A})$, where the theta measure is that of $(\mu_1, \mathcal{F}_1)$. Then there are a Haar measure $\mu_P$ on $P$ and a fundamental domain $\mathcal{F}_P$ for $P(F)$ of finite measure with
$$\frac{1}{\mu_P(\mathcal{F}_P)} \int_{\mathcal{F}_P} \Phi_A(u g) \, d\mu_P(u) = \Psi(g^{-1} e_0)$$
for every $g \in U(\mathbb{A})$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.meanP`.

*Proof.* By the structure theorem, $P$ is a split extension of $U_J(\mathbb{A})$ by $\ker \pi$, and rational points split the same way. So a fundamental domain for $P(F)$ is a product $\mathcal{F}_N \times \iota(\mathcal{F}_1)$, with $\mathcal{F}_N$ a fundamental domain for the rational points of $\ker \pi$, and a Haar measure on $P$ is a product (`split_extension_fundamental_domain`). A frame in $\operatorname{Fr}_1$ has the form $c(a, Y)$ with $a$ rational and $Y$ a rational frame of $0_n$ for $J$, so the sum $\Phi_A$ splits as a sum over $Y$ and a sum over $a \in E^n$ (`frames_sum_by_first_vector`). The volume of the product domain is the product of the volumes (`fundamental_domain_fibration_volume`). For fixed $Y$, the integral over $\mathcal{F}_N$ of the sum over $a$ is the integral over $\mathbb{A}_E^n$, by the map $l$ of the structure theorem and the covolume one property of $dA$; this is Siegel's mean value theorem for the lattice $E^n$ (`siegel_mean_value_nonnegative`). The remaining integral over $\iota(\mathcal{F}_1)$ of the sum over $Y$ is the theta measure of $\operatorname{Fr}_J(0_n)$. By the hypothesis on $\Psi$ with $h = g^{-1}$ the result is $\Psi(g^{-1} e_0)$. All functions are nonnegative, so Tonelli's theorem justifies each exchange. $\square$

**Theorem 4.11.5 (Unfolding along an isotropic vector).** Let $E/F$ be CM, $J$ nondegenerate of size $M$, and $1 \le n$ with $2n < M$. Let $\mu$ be a Haar measure on $U(\mathbb{A})$ with a fundamental domain $\mathcal{F}$, let $\mu_1$, $\mathcal{F}_1$ and $dA$ be as above, and let $\Phi$ and $\Psi$ be measurable and satisfy the hypothesis of the mean over the stabiliser. Then
$$\int \Phi \, d\Theta_{\operatorname{Fr}_{J^+}(0_{n+1})} = \int \Psi \, d\Theta_{\operatorname{Fr}_{J^+}(0_1)},$$
where both theta measures are those of $(\mu, \mathcal{F})$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypStep.Unf.unfold_frames` (also `GlobalTheory.T.hyperbolic_plane_unfolding_integral`, a second name).

*Proof.* Sort the rational isotropic frames $X$ of $J^+$ of length $n+1$ by their first vector $x_1$, a nonzero isotropic vector. By Witt's theorem $U(F)$ acts transitively on these vectors, so there is $\gamma \in U(F)$ with $\gamma e_0 = x_1$ (`global_unitary_moves_isotropic_frame`), and $\gamma^{-1} X$ lies in $\operatorname{Fr}_1$. The orbit of $e_0$ is $U(F)/P(F)$, so
$$\sum_{X \in \operatorname{Fr}_{J^+}(0_{n+1})} \Phi(h^{-1} X) = \sum_{\gamma \in U(F)/P(F)} \Phi_A(\gamma^{-1} h)$$
(`isotropic_frames_sum_by_orbit`), and $\Phi_A$ is invariant under $P(F)$ on the left (`frames_sum_invariant_under_stabiliser`). Integrating over $\mathcal{F}$ and folding the sum over $\gamma$ gives an integral over $P(F) \backslash U(\mathbb{A})$. Write it as an integral over $P \backslash U(\mathbb{A})$ of the integral over $P(F) \backslash P$ (`quotient_measure_tower`). The inner integral is the mean over the stabiliser, which is $\Psi(g^{-1} e_0)$. Unfolding the outer integral in the same way along the orbit of $e_0$ gives the theta integral of $\Psi$ over the nonzero isotropic vectors, that is over $\operatorname{Fr}_{J^+}(0_1)$. The normalisations by $\mu(\mathcal{F})$ agree on both sides. $\square$

The function $\Psi$ in the theorem is the stage integral of [the section on Gram fibres](/entry/local-stages/) against the theta measure of $J$. So the theorem reduces the free Siegel-Weil property for $(J^+, 0_{n+1})$ to the property for $(J, 0_n)$ and for $(J^+, 0_1)$. The second of these is the subject of the next section.

**Remark 4.11.6 (Formalization).** The two second names are stated with `first | exact` ([HyperbolicPlaneUnfoldingIntegralStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HyperbolicPlaneUnfoldingIntegralStatement.lean#L8), [StabiliserSplittingAdelic.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/StabiliserSplittingAdelic.lean#L230)). The mean over the stabiliser has no hypothesis on $n$ or $M$, while the unfolding theorem assumes $1 \le n$ and $2n < M$ ([HyperbolicPlaneUnfoldingIntegral.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HyperbolicPlaneUnfoldingIntegral.lean#L60), [L218](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HyperbolicPlaneUnfoldingIntegral.lean#L218)). The sum $\Phi_A$ is defined at [L52](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HyperbolicPlaneUnfoldingIntegral.lean#L52), and the stabiliser, its rational points and the frames with first vector $e_0$ are in [ActWOneApply.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ActWOneApply.lean#L49). The lemmas named in the proofs are second names in `GlobalTheory.T` that we have not opened, so the steps above follow their names and statements. The measure $dA$ is on $1 \times n$ tuples, so $a$ is a row of length $n$ and not a vector of $\mathbb{A}_E^n$ in the usual sense; this is only a choice of index type.
