---
title: Short vectors near a maximum
decls:
  - ReciprocityTheory.ChartRestriction.G.FD.shortVectorBound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Short vectors near a maximum

Let $P$ be a cusp form on a unitary group of signature $(p_0, r - p_0)$ over a CM field. This section studies frames $z_0$ at which a Fourier-Jacobi coefficient of $P$ along an isotropic vector $\xi$ nearly reaches its maximum. At such a frame, no lattice vector orthogonal to $\xi$ is short in the directions orthogonal to the plane of $\xi$. The bound is explicit in the degree and discriminant of the field, the level, and the weight. The [next section](/entry/orthonormal-short-vector-bound-of/) uses the bound to build a reduced basis of the orthogonal complement of $\xi$. Both results serve the [nonvanishing of a Fourier-Jacobi coefficient at a split point](/entry/exists-fj-ne-zero-at-split-point-prime/) in a later volume.

### The setting

Let $E$ be a CM field of degree $2f$ over $\mathbb{Q}$, with discriminant $d_E$, and let $\Psi$ be a CM type of $E$. Let $G \in M_r(E)$ be Hermitian and invertible, and let $h(x, y) = \sum_{a, b} x_a G_{ab} \overline{y_b}$ on $E^r$. For $\tau \in \Psi$, $h_\tau$ is the form of $\tau(G)$ on $\mathbb{C}^r$, and it has signature $(p_0, r - p_0)$. The data also contain:

1. a lattice $\Lambda \subseteq E^r$ and an arithmetic group $\Gamma$ that preserves $h$ and $\Lambda$, with a character $\chi_\lambda$ of $\Gamma$ for each weight $\lambda$;
2. a second lattice $L'$, self-dual for $h$, and integers $N_A, N_C \geq 1$ with $N_A \Lambda \subseteq L'$ and $N_C L' \subseteq \Lambda$;
3. a level $g \geq 1$ such that $\Gamma$ contains every element that preserves $h$ and $\Lambda$ and is $1$ modulo $g \Lambda$;
4. an element $\xi_0 \in E$ with $\overline{\xi_0} = -\xi_0$, and the constants $c_\tau = 2 |\tau(\xi_0)|$.

The other fields of the data are not used in this section, and we do not unfold them.

A *frame* is a family $x = (x_\tau)_{\tau \in \Psi}$ of matrices in $\mathrm{GL}_r(\mathbb{C})$. The domain $\mathcal{D}$ is the set of frames whose leading principal minors of the Gram matrices have the signs of the signature. For $x \in \mathcal{D}$ and $\tau \in \Psi$, let $p_{x, \tau}$ be the $h_\tau$-orthogonal projection onto the span of the first $p_0$ columns of $x_\tau$.

**Definition 1.15.1 (Majorant).** For a frame $x$, $\tau \in \Psi$ and $v \in \mathbb{C}^r$, the *majorant* is
$$m_{x, \tau}(v) = 2 \, h_\tau(p_{x, \tau} v, p_{x, \tau} v) - \operatorname{Re} h_\tau(v, v).$$

Lean: `ReciprocityTheory.ChartRestriction.G.FD.Data.maj`.

The majorant is the positive definite form that agrees with $h_\tau$ on the positive span and with $-h_\tau$ on its orthogonal complement.

Let $\xi \in \Lambda$ be nonzero and isotropic. Let $H_{x, \tau}(u, w) = h_\tau(2 p_{x, \tau} u - u, w)$. For $u = (u_\tau)_\tau$, let
$$u^\perp_x = u - \Bigl( \frac{H_{x, \tau}(u_\tau, \tau \xi)}{H_{x, \tau}(\tau \xi, \tau \xi)} \, \tau \xi \Bigr)_\tau$$
be the component of $u$ orthogonal to the line of $\xi$ for the majorant. For $v \in E^r$ we write $v^\perp_x$ for the component of $(\tau v)_\tau$.

The *frames over $\xi$* are the $x \in \mathcal{D}$ with $c_\tau \, m_{x, \tau}(\tau \xi) = 1$ for all $\tau$. For a weight $\lambda$ and a function $Q$ on frames, $\widehat{N}_\lambda(Q)(x)$ is the supremum of the weighted norm of $Q$ over the frames in $\mathcal{D}$ with the same flag of positive spans as $x$. For a weight $\lambda$, an index $\nu = (\nu_\tau)$ and a function $P$, $F_{\xi, \nu}(P)$ is the Fourier-Jacobi coefficient of $P$ of index $\nu$ along $\xi$: the average of $P$ along the flow in the direction of $\xi$ over a fundamental domain of the period lattice, times a character of index $\nu$. We do not unfold the weighted norm and the flow.

A *bounded cusp form* of weight $\lambda$ is a holomorphic function $P$ on $\mathcal{D}$ that transforms under the Borel subgroup by the character of $\lambda$ and under $\Gamma$ by $\chi_\lambda$, whose weighted norm is bounded, and with $F_{\xi, 0}(P) = 0$ for every isotropic $\xi \in \Lambda$.

**Definition 1.15.2 (Short vector hypotheses).** The data $(\lambda, P, \xi, \nu, c_1, w, z_0)$ satisfy the *short vector hypotheses* if:

1. $\lambda$ is dominant and $P$ is a bounded cusp form of weight $\lambda$;
2. $\xi \in \Lambda$ is nonzero and isotropic, $c_1 > 0$, and $\sum_\tau \nu_\tau \leq c_1$;
3. $F_{\xi, \nu}(P)$ is not identically zero on $\mathcal{D}$;
4. $w \geq 1$, and $w$ is at least the sum over $\tau$ of the spread $\max_i \lambda_{\tau, i} - \min_i \lambda_{\tau, i}$;
5. $\chi_\lambda(\gamma) = 1$ for every $\gamma \in \Gamma$ that is $1$ modulo $g \Lambda$;
6. $z_0$ is a frame over $\xi$, and $\sup \widehat{N}_\lambda(F_{\xi, \nu}(P)) < 2 \, \widehat{N}_\lambda(F_{\xi, \nu}(P))(z_0)$, with the supremum over the frames over $\xi$.

Lean: `ReciprocityTheory.ChartRestriction.G.FD.ShortVectorHypotheses`.

Condition 6 says that $z_0$ is within a factor $2$ of the maximum.

### The short vector bound

Let $N_0 = g d_E^2$, $H = N_C^2 (2 + 4 f^4 d_E^{1/f} N_A^2)$, $K_2 = 1 + N_0 H (2 c_1 + 1)$, $N_2 = 4f$ and $R_2 = w + N_2 \log(2 K_2 N_2) + N_2 + 2$. Let
$$\varepsilon_0 = \min \Bigl( 1, \ \frac{f^2}{N_0^2 N_C^2 c_1 R_2} \Bigr).$$

**Theorem 1.15.3 (Short vector bound).** Assume the short vector hypotheses. Let $x \in L'$ with $h(x, \xi) = 0$ and $x \notin E \xi$. Then there is $\tau \in \Psi$ with
$$\varepsilon_0 \leq m_{z_0, \tau}\bigl( (x^\perp_{z_0})_\tau \bigr).$$

Lean: `ReciprocityTheory.ChartRestriction.G.FD.shortVectorBound`.

*Proof.* We use these facts, proved in another part of the development. We have opened their statements.

1. *Isotropy.* If $x \in L'$, $h(x, \xi) = 0$, $x \notin E\xi$ and $m_{z_0, \tau}((x^\perp_{z_0})_\tau) < 1$ for all $\tau$, then $h(x, x) = 0$, and there is $\alpha \in \mathcal{O}_E$ such that $x' = x + N_A \alpha \xi$ lies in $L'$, is orthogonal to $\xi$, has $x'^\perp_{z_0} = x^\perp_{z_0}$, and satisfies $c_\tau m_{z_0, \tau}(\tau(N_C x')) \leq H$ for all $\tau$.
2. *The pair.* For such $x'$, the vectors $\xi$ and $N_C x'$ are linearly independent, isotropic, orthogonal and in $\Lambda$. The Fourier coefficients $F_\chi$ of $F_{\xi, \nu}(P)$ along this pair are defined, and $F_{\xi, \nu}(P)$ is the sum of the $F_\chi$ where the sum converges.
3. *Index bound.* Let $\varepsilon > 0$ with $m_{z_0, \tau}((x'^\perp_{z_0})_\tau) \leq \varepsilon$ for all $\tau$. Each $\chi$ with $F_\chi \neq 0$ has an index $t_\chi$ with $t_\chi \geq f^2 / (N_0^2 N_C^2 c_1 \varepsilon)$.
4. *Height bound.* For $t \geq 1$ there are at most $(K_2 t)^{4f}$ indices $\chi$ with $F_\chi \neq 0$ and $t_\chi \leq t$.
5. *Exponential sums.* Let $K, N \geq 1$ and $w \geq 0$. If all $t_j > w + N \log(2KN) + N + 2$ and at most $(K t)^N$ of the $t_j$ are at most $t$ for each $t \geq 1$, then $\sum_j e^{-\pi t_j}$ converges and $2^{w/2} \sum_j e^{-\pi t_j} < \tfrac12$.
6. *Decay.* On the frames with the flag of $z_0$, the weighted norm of $F_\chi$ is at most $2^{w/2} e^{-\pi t_\chi} S$, where $S$ is the supremum in condition 6.
7. *Sum.* The weighted norm of $F_{\xi, \nu}(P)$ at these frames is then at most $2^{w/2} \sum_\chi e^{-\pi t_\chi} \, S$.
8. $0 < \varepsilon_0 \leq 1$, and $R_2 < f^2 / (N_0^2 N_C^2 c_1 \varepsilon)$ for $0 < \varepsilon < \varepsilon_0$.

Assume that the theorem is false for $x$: $m_{z_0, \tau}((x^\perp_{z_0})_\tau) < \varepsilon_0 \leq 1$ for all $\tau$. Fact 1 gives $\alpha$ and $x'$. Since $x \notin E \xi$, also $x' \notin E \xi$. Expand $h(x', x')$: the terms $h(x, \xi)$, $h(\xi, x)$ and $h(\xi, \xi)$ vanish, and $h(x, x) = 0$, so $x'$ is isotropic. Let $\varepsilon$ be the maximum of $\varepsilon_0 / 2$ and the values $m_{z_0, \tau}((x^\perp_{z_0})_\tau)$. Then $0 < \varepsilon < \varepsilon_0$, and the same bound holds for $x'$.

Take the pair of fact 2. By facts 3 and 8, every $\chi$ with $F_\chi \neq 0$ has $t_\chi > R_2$. Fact 4 gives the counting hypothesis of fact 5 with $K = K_2$ and $N = N_2$, so
$$c := 2^{w/2} \sum_\chi e^{-\pi t_\chi} < \tfrac12.$$
By facts 6 and 7, the weighted norm of $F_{\xi, \nu}(P)$ is at most $cS$ at every frame with the flag of $z_0$, so $\widehat{N}_\lambda(F_{\xi, \nu}(P))(z_0) \leq cS$. Condition 6 gives $S < 2 \widehat{N}_\lambda(F_{\xi, \nu}(P))(z_0)$. Since $S \geq 0$,
$$\widehat{N}_\lambda(F_{\xi, \nu}(P))(z_0) \leq c S \leq \tfrac12 S < \widehat{N}_\lambda(F_{\xi, \nu}(P))(z_0),$$
which is false. $\square$

**Remark 1.15.4 (Classical form).** The short vector bound is a version of the statement that a cusp form is small near the cusps: if a Fourier-Jacobi coefficient is near its maximum at $z_0$, then $z_0$ is not deep in a cusp in the directions of the complement of $\xi$. The proof is the usual one: the Fourier expansion along an isotropic pair, the exponential decay $e^{-\pi t_\chi}$ of the terms, and a count of the indices. The constant $\varepsilon_0$ is explicit, and it depends only on $f$, $d_E$, $g$, $N_A$, $N_C$, $c_1$ and $w$.

**Remark 1.15.5 (Formalization).** The short vector bound is proved in [ShortVectorBoundOfCoefficientBounds.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/ShortVectorBoundOfCoefficientBounds.lean#L83) from seven propositions: `FourierCoefficientProperties`, `CuspCoefficientBound`, `FlowCoefficientDecay`, `CoefficientIndexLowerBound`, `CoefficientHeightBound`, `CountingExponentialSum` and `IsotropicOutsideLine`; [ShortVectorBound.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/ShortVectorBound.lean#L8) supplies their proofs. Facts 2, 7 and 8 also use `short_vector_setting_exists`, `isotropic_pair_in_lattice`, `pointwise_sum_bound` and `epsilonZero_spec`. In `pointwise_sum_bound` the expansion of $F_{\xi, \nu}(P)$ is a hypothesis only at the points where the series converges absolutely. The constant $d_E^{1/f}$ in $H$ is written as $(|d_E|^{1/(2f)})^2$ in the Lean definition `flowEpsilonBound`.
