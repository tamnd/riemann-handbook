---
title: Heights and the bound at the edge of convergence
decls:
  - GlobalTheory.CompanionTheory.SphPole.frame_bound
  - GlobalTheory.CompanionTheory.SphPole.height_bound
  - GlobalTheory.CompanionTheory.SphPole.sphBound_of_htExist
  - GlobalTheory.T.spherical_bound_of_heights
  - PositivityTheory.Rg.Rsw.sphBound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Heights and the bound at the edge of convergence

The Siegel Eisenstein series of a height converges to the right of an edge. This section proves that, as the exponent comes down to the edge, the series grows at most like the inverse of the distance to the edge. So the Eisenstein series has at most a simple pole at the edge, with a bound that is uniform on compact sets. The bound is an input of the residue functional of the Eisenstein series, which is a limit of $(\sigma - p/2)$ times the series as $\sigma \to p/2$; this section shows that the product stays bounded. Through that functional the bound reaches the residue theorem, [Theorem 5.7.3](/entry/res-core/).

We fix the setting of the whole chapter. Let $E/F$ be a CM extension of number fields, $\mathbb{A}$ the adeles of $F$ and $\mathbb{A}_E = \mathbb{A} \otimes_F E$. For $x$ a matrix over $\mathbb{A}_E$ let $x^*$ be its conjugate transpose. Let $G_n$ be the group of adelic points of the [unitary group](/learn/groups/#unitary-groups) $U(n,n)$ of the standard split form of rank $2n$. We write its elements as block matrices $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $n \times n$ blocks. The *Siegel parabolic* $P_n$ is the subgroup with $c = 0$ ([parabolic subgroups](/learn/groups/#parabolic-subgroups)). For $q \in P_n$ we call its block $a = a_q \in GL_n(\mathbb{A}_E)$ the *Levi block*. Let $|\cdot|$ be the idelic absolute value on $\mathbb{A}_E^\times$, and let $G_n(F)$ and $P_n(F)$ be the rational points.

**Convention.** A sum $\sum_{i \in I}$ over an infinite set means the sum of a summable family. When the family is not summable, we set the sum equal to $0$. Each statement below says explicitly when a family is summable.

**Definition 5.1.1 (Height).** A *height* on $G_n$ is a continuous function $H \colon G_n \to \mathbb{R}_{>0}$ with $H(qg) = |\det a_q|\, H(g)$ for all $q \in P_n$ and $g \in G_n$.

A height measures how far $g$ is from the rational points in the direction of the unipotent radical of $P_n$. Two heights $H$ and $H'$ change by the same factor under $P_n$ on the left. So $H/H'$ is a function on $P_n \backslash G_n$, and it is bounded on each compact set of this quotient.

**Definition 5.1.2 (Siegel Eisenstein sum).** For $f \colon G_n \to \mathbb{C}$ and $g \in G_n$ put
$$E(f)(g) = \sum_{\gamma \in P_n(F) \backslash G_n(F)} f(\gamma g),$$
where $\gamma$ runs through a fixed set of representatives of the cosets.

This is the [Siegel Eisenstein series](/learn/automorphic-forms/#eisenstein-series) of $f$. For $f = H^{s}$ the terms are $H(\gamma g)^{s}$, and the series converges for $s$ large. The edge of convergence for $G_p$ is the exponent $p$. We need two inputs.

**Theorem 5.1.3 (Existence of heights).** For each $n$ there is a height on $G_n$, and there is a compact set $C_0 \subset G_n$ with $G_n = P_n C_0$.

Lean: `GlobalTheory.T.height_functions_exist`.

*Proof.* We take this result as given; we do not prove it in this chapter. $\square$

The next theorem works in a more general unitary group. Let $J$ be a nondegenerate Hermitian $n \times n$ matrix over $E$, and $U(J)$ its unitary group. A *Witt frame* of rank $r+1$ is a pair $X, Y$ of $n \times (r+1)$ matrices over $E$ with
$$X^* J X = 0, \qquad Y^* J Y = 0, \qquad X^* J Y = 1,$$
such that the orthogonal complement of the columns of $X$ and $Y$ is anisotropic. An element $p$ of $U(J)(\mathbb{A})$ *scales* $X$ by $\beta \in GL_{r+1}(\mathbb{A}_E)$ if $pX = X\beta$. Let $\Gamma = U(J)(F)$, and let $\Lambda \subset \Gamma$ be the subgroup of the rational elements that scale $X$.

**Theorem 5.1.4 (Frame bound).** Let $J$, $X$, $Y$ be as above, with $X, Y$ a Witt frame of rank $r+1$. Let $K$ be the level subgroup of $U(J)(\mathbb{A})$ given by an $\mathcal{O}_E$-lattice $L$ and an element $a \in GL_n(\mathbb{A}_E)$. Let $h \colon U(J)(\mathbb{A}) \to \mathbb{R}$, and assume:

1. each $g$ can be written $g = pk$ with $k \in K$ and $p$ scaling $X$;
2. $h(pk) = |\det \beta|$ whenever $p$ scales $X$ by $\beta$ and $k \in K$.

Let $T \subset \Gamma$ be a set of representatives of $\Lambda \backslash \Gamma$: for each $\gamma \in \Gamma$ there is exactly one $t \in T$ with $\gamma t^{-1} \in \Lambda$. Then there is $B$ such that
$$\varepsilon \sum_{t \in T} h(t)^{\,n - (r+1) + \varepsilon} \le B \qquad \text{for all } 0 < \varepsilon \le 1.$$

Lean: `GlobalTheory.CompanionTheory.SphPole.frame_bound`.

*Proof.* Put $d = n - (r+1)$. A Witt frame of rank $r+1$ gives $2(r+1) \le n$, so $d > 0$. Let $\mu$ be a [Haar measure](/learn/analysis/#haar-measure) on $U(J)(\mathbb{A})$. Put $f_\varepsilon = h^{d+\varepsilon} \mathbf{1}_{h \le 1}$ and $\Phi_\varepsilon(g) = \sum_{t \in T} f_\varepsilon(tg)$.

First, let $\mathcal{F}$ be a fundamental domain for $\Gamma$ and $\mathcal{F}_\Lambda$ one for $\Lambda$. The usual unfolding of a sum over cosets gives $\int_{\mathcal{F}} \Phi_\varepsilon \, d\mu = \int_{\mathcal{F}_\Lambda} f_\varepsilon \, d\mu$.

Second, the part of $\mathcal{F}_\Lambda$ where $e^{-j-1} < h \le e^{-j}$ has measure at most $B_0 e^{dj}$ for a constant $B_0$. On this shell $f_\varepsilon \le e^{-j(d+\varepsilon)}$. Summing over $j \ge 0$ gives $\int_{\mathcal{F}_\Lambda} f_\varepsilon \le B_0 \sum_j e^{-j\varepsilon}$, and so $\varepsilon \int_{\mathcal{F}} \Phi_\varepsilon \le 2B_0$ for $0 < \varepsilon \le 1$.

Third, take a compact neighbourhood $U$ of $1$ with $\gamma U \cap U = \emptyset$ for rational $\gamma \neq 1$. Then $\int_U \Phi_\varepsilon \le \int_{\mathcal{F}} \Phi_\varepsilon$. By the decomposition $g = pk$ and the compactness of $K$ and $U$, there are $M, m \ge 1$ with $m^{-1} h(g) \le h(gu) \le M h(g)$ for $u \in U$. So each $t$ with $h(t) \le M^{-1}$ has $h(tu) \le 1$ and $h(t)^{d+\varepsilon} \le m^{d+1} f_\varepsilon(tu)$ for $u \in U$. Integration over $U$ gives
$$\varepsilon \, \mu(U)\, m^{-d-1} \sum_{h(t) \le 1/M} h(t)^{d+\varepsilon} \le 2B_0.$$

Fourth, for $h(t) > M^{-1}$ we have $h(t)^{d+\varepsilon} \le M h(t)^{d+1}$, and $\sum_t h(t)^{d+1}$ converges by the convergence of Eisenstein series of Godement type for exponents above $d$. Adding the two parts gives the bound with $B = 2B_0 m^{d+1}/\mu(U) + M \sum_t h(t)^{d+1}$. $\square$

**Theorem 5.1.5 (One good height).** For each $p \ge 1$ there are a height $H'$ on $G_p$ and a real $B$ such that for each $0 < \varepsilon \le 1$ the family $\gamma \mapsto H'(\gamma)^{p + \varepsilon}$ on $P_p(F) \backslash G_p(F)$ is summable and
$$\varepsilon \sum_{\gamma \in P_p(F) \backslash G_p(F)} H'(\gamma)^{p+\varepsilon} \le B.$$

Lean: `GlobalTheory.CompanionTheory.SphPole.height_bound`.

*Proof.* Let $A$ be the standard positive definite Hermitian space of rank $p$ and $V$ its double, a sum of $p$ hyperbolic planes. There is an isotropic Witt frame $X, Y$ of rank $p$ in $V$, and an isomorphism $\kappa \colon U(V)(\mathbb{A}) \to G_p$ that carries the stabilizer of $X$ onto $P_p$ and rational points onto rational points. For a good level $K$ we have $U(V)(\mathbb{A}) = P_X K$, and $h(qk) = |\det \beta_q|$ defines a function as in the [Theorem 5.1.4](/entry/sph-pole-frame-bound/), where $q$ scales $X$ by $\beta_q$. Put $H' = h \circ \kappa^{-1}$. The determinant of $\beta_q$ is the determinant of the Levi block of $\kappa(q)$, so $H'$ is a height. The images under $\kappa^{-1}$ of the representatives of $P_p(F) \backslash G_p(F)$ form a set of representatives of $\Lambda \backslash U(V)(F)$. Here $n = 2p$ and $r + 1 = p$, so the exponent $n - (r+1) + \varepsilon$ of the frame bound is $p + \varepsilon$. The bound is the [Theorem 5.1.4](/entry/sph-pole-frame-bound/), and summability for exponents above $p$ is the convergence of Godement type used in its proof. $\square$

**Theorem 5.1.6 (Edge bound).** Assume the conclusion of the existence of heights: each $G_n$ carries a height, and $G_n = P_n C_0$ for a compact set $C_0$. Let $p \ge 1$, let $H$ be a height on $G_p$, and let $C \subset G_p$ be compact. Then there is $B$ such that for all $\sigma$ with $p/2 < \sigma \le p/2 + 1$ and all $h \in C$, the family $\gamma \mapsto H(\gamma h)^{\sigma + p/2}$ on $P_p(F) \backslash G_p(F)$ is summable and
$$\Bigl(\sigma - \frac{p}{2}\Bigr) \sum_{\gamma \in P_p(F) \backslash G_p(F)} H(\gamma h)^{\sigma + p/2} \le B.$$

Lean: `GlobalTheory.CompanionTheory.SphPole.sphBound_of_htExist` (also `GlobalTheory.T.spherical_bound_of_heights`, a second name).

*Proof.* Put $\varepsilon = \sigma - p/2$, so that $0 < \varepsilon \le 1$ and the exponent is $p + \varepsilon$. Take $H'$ and $B'$ from [Theorem 5.1.5](/entry/height-bound/). The function $(c, h) \mapsto H(ch)/H'(c)$ is continuous and positive on $G_p \times G_p$, so it is bounded on the compact set $C_0 \times C$ by some $c_1 \ge 1$. Let $\gamma \in G_p$ and $h \in C$. Write $\gamma = qc$ with $q \in P_p$ and $c \in C_0$. Both heights change by the factor $|\det a_q|$ under $q$, so
$$H(\gamma h) = |\det a_q|\, H(ch) \le c_1 |\det a_q|\, H'(c) = c_1 H'(\gamma).$$
Since $c_1 \ge 1$ and $p + \varepsilon \le p + 1$, this gives $H(\gamma h)^{p+\varepsilon} \le c_1^{p+1} H'(\gamma)^{p+\varepsilon}$. Comparison with the summable family of $H'$ gives summability and the bound $B = c_1^{p+1} B'$. $\square$

**Corollary 5.1.7 (Edge bound).** The conclusion of the edge bound holds without hypothesis: for $p \ge 1$, a height $H$ on $G_p$ and a compact $C \subset G_p$, there is $B$ with the summability and the bound above for all $p/2 < \sigma \le p/2 + 1$ and $h \in C$.

Lean: `PositivityTheory.Rg.Rsw.sphBound`.

*Proof.* This is [Theorem 5.1.6](/entry/sph-bound-of-ht-exist/) applied to the Existence of heights above. $\square$

**Remark 5.1.8 (Formalization).** The edge bound takes the whole existence statement as a hypothesis, but the proof uses only the decomposition $G_n = P_n C_0$; it takes its height from [Theorem 5.1.5](/entry/height-bound/) and discards the height of the hypothesis ([SphericalBoundOfHeights.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SphericalBoundOfHeights.lean#L364)). The frame bound does not assert summability, so with the convention above its sum could be $0$; its proof shows summability, and the good height asserts it. The second name of the edge bound is a wrapper that tries three tactics and raises the heartbeat limit to one million for a one-line proof. The bound is stated at the representatives of $P_p(F) \backslash G_p(F)$; the proof compares $H$ and $H'$ at the same representatives.
