---
title: Iwahori functions and the matching criterion
decls:
  - UpperTheory.ConvolutionTheory.H.core
  - UpperTheory.ConvolutionTheory.H.deepAbs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Iwahori functions and the matching criterion

The proof of [matching with an auxiliary factor](/entry/deep-hecke/) used a criterion: two linear functionals on the Hecke algebras of $\mathrm{GL}_n(E)$ and $\mathrm{GL}_n(k)$ take the same value on a pair of spherical functions as soon as they agree on the normalized Iwahori double coset functions with strictly decreasing exponent and vanish on commutators. This section proves that criterion. The first step writes a spherical function, modulo commutators, as a finite combination of Iwahori functions. The second step chooses the auxiliary factor $g$ so that only strictly decreasing exponents occur.

Throughout, $k$ is a nonarchimedean local field with ring of integers $\mathcal{O}$, uniformizer $\varpi$ and residue field of order $q$. Let $K = \mathrm{GL}_n(\mathcal{O})$, and let $\mu$ be the Haar measure on $\mathrm{GL}_n(k)$ with $\mu(K) = 1$. Convolution with respect to $\mu$ is written $*$. We use the Satake transform $\mathcal{S}$ and the maps $b_l$ of [Section 7.9.3](/entry/deep-hecke/).

**Definition 7.17.1 (Iwahori functions).** The Iwahori subgroup $I \subset K$ is the set of $g \in K$ whose reduction modulo $\varpi$ is upper triangular. For $a \in \mathbb{Z}^n$ let $\varpi^a = \mathrm{diag}(\varpi^{a_1}, \dots, \varpi^{a_n})$ and let $\delta^{1/2}(a)$ be the square root of the modulus character of the upper triangular Borel subgroup at $\varpi^a$. The normalized Iwahori function is
$$\theta(a) = \frac{\delta^{1/2}(a)}{\mu(I)}\,\mathbf{1}_{I\varpi^aI}.$$
For a Laurent polynomial $r = \sum_a c_a x^a$ in $x_1, \dots, x_n$ put $\theta(r) = \sum_a c_a\,\theta(a)$.

We call $a \in \mathbb{Z}^n$ dominant if $a_1 \ge a_2 \ge \dots \ge a_n$ and strictly decreasing if $a_1 > a_2 > \dots > a_n$. A Laurent polynomial is dominant (strictly dominant) if every exponent in its support is dominant (strictly decreasing). For $m \in \mathbb{N}$, we say that $a$ has gap $m$ if $a_j + m \le a_i$ for all $i < j$.

**Definition 7.17.2 (Weyl factor and symmetrization).** For $t \in \mathbb{C}$ let
$$\Delta_t = \prod_{i < j} (x_i - t\,x_j).$$
For a Laurent polynomial $y$ let $\mathrm{Sym}(y) = \sum_{\sigma \in S_n} \sigma \cdot y$, where $S_n$ permutes the variables. Let $v_n(t) = \prod_{k=1}^{n} (1 - t^k)/(1 - t)$, the Poincare polynomial of $S_n$.

The product $\Delta_{q^{-1}}$ is the numerator of the Macdonald formula for the spherical function. The factor $\Delta_1$ is the Vandermonde product.

**Definition 7.17.3 (Commutator space).** Let $\mathcal{C}$ be the complex span of all functions $a * b - b * a$, where $b$ is locally constant with compact support on $\mathrm{GL}_n(k)$, and $a$ is either $\mathbf{1}_K$ or $\mathbf{1}_{I\varpi^lI}$ for a dominant $l$.

Orbital integrals and twisted orbital integrals vanish on $\mathcal{C}$, so $\mathcal{C}$ is the right space to work modulo.

We use three facts on the Iwahori-Hecke algebra.

1. (Multiplicativity.) If $r$ and $s$ are dominant, then $\theta(r)$ is bi-$I$-invariant, locally constant with compact support, and $\theta(r) * \theta(s) = \theta(rs)$.
2. (Sandwich identity.) There are $\nu_1, \nu_2 \in \mathbb{Z}^n$, both with gap $n$, such that
$$v_n(q^{-1}) \sum_{S} \epsilon(S)\, \theta(\nu_1 + e_L(S)) * \mathbf{1}_K * \theta(\nu_2 + e_R(S)) = \theta(x^{\nu_1 + \nu_2}\Delta_{q^{-1}}).$$
Here $S$ runs over the subsets of the set $\Pi$ of pairs $(i,j)$ with $i < j$, $e_L(S) = \sum_{(i,j) \in S} e_i$, $e_R(S) = \sum_{(i,j) \notin S} e_j$, and $\epsilon(S) = (-1)^{|\Pi \setminus S|}$.
3. (Satake average.) If $r$ is a Laurent polynomial with $r\Delta_1$ dominant and $h$ is spherical with $\mathcal{S}(h) = \mathrm{Sym}(r\Delta_{q^{-1}})$, then $v_n(q^{-1})\,\mathbf{1}_K * \theta(r\Delta_1) * \mathbf{1}_K = h$.

Fact 1 is the Iwahori-Matsumoto relation for dominant translations. Expanding the product $\Delta_1$ gives the Vandermonde identity
$$\Delta_1 = \sum_{S \subseteq \Pi} \epsilon(S)\, x^{e_L(S) + e_R(S)},$$
since each factor $x_i - x_j$ contributes $x_i$ for $(i,j) \in S$ and $-x_j$ otherwise. If $\nu$ has gap $n$, then $\nu + e_L(S)$ and $\nu + e_R(S)$ are dominant for every $S$, and $x^\nu\Delta_t$ is dominant for every $t$: each coordinate of $e_L(S)$ or $e_R(S)$ lies between $0$ and $n - 1$.

**Theorem 7.17.4 (Spherical functions modulo commutators).** Let $\mu(K) = 1$. There is $\nu \in \mathbb{Z}^n$ with the following property. Let $r$ be a dominant Laurent polynomial, and let $h$ be a spherical function with
$$\mathcal{S}(h) = \mathrm{Sym}(x^\nu\Delta_{q^{-1}}\,r).$$
Then $\theta(x^\nu\Delta_{q^{-1}}\,r) - h \in \mathcal{C}$.

Lean: `UpperTheory.ConvolutionTheory.H.core`.

*Proof.* Take $\nu_1, \nu_2$ from the sandwich identity and $\nu = \nu_1 + \nu_2$. Write $t = q^{-1}$ and $v = v_n(t)$. For $S \subseteq \Pi$ put $A_S = r\,x^{\nu_1 + e_L(S)}$, $b_S = \nu_2 + e_R(S)$ and $C_S = x^{b_S}A_S$. These are dominant, since $r$ is dominant and the exponents $\nu_1 + e_L(S)$ and $b_S$ are dominant. By multiplicativity and the sandwich identity,
$$\begin{aligned} \theta(x^\nu\Delta_t r) &= \theta(r) * \theta(x^\nu\Delta_t) \\ &= v \sum_S \epsilon(S)\, \theta(A_S) * \mathbf{1}_K * \theta(b_S). \end{aligned}$$
On the other side, $x^\nu r\Delta_1$ is dominant and $\mathrm{Sym}(x^\nu r\Delta_t) = \mathcal{S}(h)$, so the Satake average and the Vandermonde identity give
$$h = v\,\mathbf{1}_K * \theta(x^\nu r \Delta_1) * \mathbf{1}_K = v \sum_S \epsilon(S)\, \mathbf{1}_K * \theta(C_S) * \mathbf{1}_K.$$
It remains to see that each difference $\theta(A_S) * \mathbf{1}_K * \theta(b_S) - \mathbf{1}_K * \theta(C_S) * \mathbf{1}_K$ lies in $\mathcal{C}$. Put $u = \theta(A_S) * \mathbf{1}_K$. By multiplicativity $\theta(b_S) * \theta(A_S) = \theta(C_S)$, so $\theta(b_S) * u = \theta(C_S) * \mathbf{1}_K$. Since $\mathbf{1}_K * \mathbf{1}_K = \mathbf{1}_K$ for $\mu(K) = 1$, the difference equals
$$-\big(\theta(b_S) * u - u * \theta(b_S)\big) - \big(\mathbf{1}_K * w - w * \mathbf{1}_K\big), \qquad w = \theta(C_S) * \mathbf{1}_K.$$
The first bracket is a multiple of a commutator with $\mathbf{1}_{I\varpi^{b_S}I}$, $b_S$ dominant. The second is a commutator with $\mathbf{1}_K$. Both $u$ and $w$ are locally constant with compact support. $\square$

Now let $E$ be a second nonarchimedean local field, with residue field of order $q_E$, and use the same notation with a subscript $E$.

**Theorem 7.17.5 (Iwahori criterion for matching).** Let $l \ge 1$ and assume $q_E = q^l$. Let $\mu_E$ and $\mu$ be Haar measures on $\mathrm{GL}_n(E)$ and $\mathrm{GL}_n(k)$ that give $\mathrm{GL}_n(\mathcal{O}_E)$ and $\mathrm{GL}_n(\mathcal{O})$ volume 1. Let $P$ be a finite set of symmetric Laurent polynomials and let $z \in (\mathbb{C}^\times)^n$. Then there is a symmetric polynomial $g$, with no negative exponents and $g(z) \ne 0$, with the following property. Let $p$ be in the span of $P$, and let $h$ on $\mathrm{GL}_n(E)$ and $f$ on $\mathrm{GL}_n(k)$ be spherical with
$$\mathcal{S}(h) = gp, \qquad \mathcal{S}(f) = b_l(gp).$$
Let $\Lambda_E$ and $\Lambda$ be maps from functions on $\mathrm{GL}_n(E)$ and $\mathrm{GL}_n(k)$ to $\mathbb{C}$, linear on the locally constant functions of compact support, that vanish on $\mathcal{C}_E$ and $\mathcal{C}$, and that satisfy $\Lambda_E(\theta_E(a)) = \Lambda(\theta(la))$ for every strictly decreasing $a$. Then $\Lambda_E(h) = \Lambda(f)$.

Lean: `UpperTheory.ConvolutionTheory.H.deepAbs`.

*Proof.* Let $t = q^{-1}$, so that $q_E^{-1} = t^l$. Apply the [theorem on spherical functions modulo commutators](/entry/h-core/) to $E$ and to $k$; it gives exponents $\nu_E$ and $\nu$. We need a lemma on exponents: there is $m \in \mathbb{N}$ such that for every $a$ with gap $m$ and every $p \in P$, the product $y = x^a\Delta_{t^l}p$ is strictly dominant, $y = x^{\nu_E}\Delta_{t^l}r$ for a dominant $r$, and $b_l(y) = x^{\nu}\Delta_t r'$ for a dominant $r'$. The reason is that a large gap in $a$ dominates the bounded exponents of $\Delta_{t^l}p$ and of the shifts by $\nu_E$ and $\nu$. All three properties are stable under linear combinations, so they hold for every $p$ in the span of $P$. Next, since $|t^l| < 1$, there is $a$ with gap $m$ and $a_i \ge 0$ for all $i$ such that $\mathrm{Sym}(x^a\Delta_{t^l})$ does not vanish at $z$. Put $g = \mathrm{Sym}(x^a\Delta_{t^l})$. It is symmetric and has no negative exponents, since $a \ge 0$ and $\Delta_{t^l}$ is a polynomial.

Let $p$, $h$, $f$, $\Lambda_E$ and $\Lambda$ be as in the statement and $y = x^a\Delta_{t^l}p$. Since $p$ is symmetric, $\mathrm{Sym}(y) = gp$; since $b_l$ commutes with the action of $S_n$, $b_l(gp) = \mathrm{Sym}(b_l(y))$. So $\mathcal{S}(h) = \mathrm{Sym}(x^{\nu_E}\Delta_{t^l}r)$ and $\mathcal{S}(f) = \mathrm{Sym}(x^{\nu}\Delta_t r')$, and the previous theorem gives
$$\theta_E(y) - h \in \mathcal{C}_E, \qquad \theta(b_l(y)) - f \in \mathcal{C}.$$
The functionals vanish on these differences, so $\Lambda_E(h) = \Lambda_E(\theta_E(y))$ and $\Lambda(f) = \Lambda(\theta(b_l(y)))$. Write $y = \sum_b c_b x^b$. Then $\theta(b_l(y)) = \sum_b c_b\,\theta(lb)$, and each $b$ is strictly decreasing. By linearity and the hypothesis on Iwahori functions,
$$\Lambda_E(h) = \sum_b c_b\,\Lambda_E(\theta_E(b)) = \sum_b c_b\,\Lambda(\theta(lb)) = \Lambda(f). \qquad \square$$

**Remark 7.17.6.** The theorem is a form of the classical reduction of the base change fundamental lemma to Iwahori functions; see the Notes at the end of the chapter. The role of $g$ is to move all exponents into the strictly decreasing chamber, where the Iwahori functions of $E$ and $k$ can be compared one by one.

**Remark 7.17.7 (Formalization).** The three facts on the Iwahori-Hecke algebra are `thPMul`, `sandId` and `satAvg` ([ThPMul.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/ThPMul.lean#L33), [SandId.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/SandId.lean#L107), [SatAvg.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/SatAvg.lean#L167)); we did not reproduce their proofs. The proof of `sandId` takes $\nu_1 = \nu_2 = (0, -n, -2n, \dots)$. The lemma on exponents is `depth` ([MemSuppMono.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/MemSuppMono.lean#L69)) and the choice of $a$ is `nonVan` ([NonVan.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/NonVan.lean#L115)). The criterion does not assume that $E$ is an extension of $k$: it uses only $q_E = q^l$ ([DeepAbs.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/DeepAbs.lean#L115)). The functionals are arbitrary maps that are linear on the locally constant functions of compact support. The square root of the modulus character is `halfModulus`, which we did not unfold.
