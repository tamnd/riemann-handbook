---
title: The archimedean decay bound
decls:
  - GlobalTheory.ArchDecay.om_bound_arch
  - GlobalTheory.T.weilRepresentation_pointwise_archimedeanDecay_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The archimedean decay bound

This section proves a pointwise bound for the adelic Weil representation of a unitary dual pair: for a fixed Schwartz-Bruhat function $\Phi$, the function $\omega(g,h)\Phi$ decays faster than each power of the archimedean variable, uniformly up to a power of the heights of $g$ and $h$. Summed over the rational points, the bound shows that the theta function $\theta(g, h; \Phi)$ converges absolutely and has moderate growth, which is [the moderate growth of theta functions](/entry/theta-moderate-growth/). The proof turns $L^2$ bounds on derivatives into pointwise bounds by a Sobolev inequality for periodic functions.

### The setting

Let $F$ be a number field, $E/F$ a quadratic extension, $X$ a Hermitian space of dimension $n$ and $W$ a skew-Hermitian space of dimension $d$ over $E$, with a model of the Weil representation $\omega$ of $\mathrm{U}(X)(\mathbb{A}_F) \times \mathrm{U}(W)(\mathbb{A}_F)$ on functions on $\mathbb{A}_F^{\,n \times d}$, for a standard additive character and splitting characters $\chi_X, \chi_W$, as in [the density of polynomial Fock vectors](/entry/pol-dense/). Let $\mathcal{S}(\mathbb{A}_F^{\,n \times d})$ be the span of the products $f_\infty \otimes f_{\mathrm f}$ of a [[Schwartz function|GE020MY43M]] on $F_\infty^{\,n \times d}$ and a Schwartz-Bruhat function on the finite adeles. For $x \in \mathbb{A}_F^{\,n \times d}$ write $x_\infty$ for its archimedean part.

**Definition 1.7.1 (Height).** For $g \in \mathrm{GL}_k(\mathbb{A}_E)$ let $\operatorname{ht}(g) = \prod_v \operatorname{ht}_v(g_v)$, where at each place $\operatorname{ht}_v(g_v) \geq 1$ is the local height built from the entries of $g_v$ and $g_v^{-1}$, and $\operatorname{ht}_v(g_v) = 1$ for almost all $v$.

So $\operatorname{ht}(g) \geq 1$ and $\operatorname{ht}(g^{-1}) = \operatorname{ht}(g)$. We view $\mathrm{U}(X)(\mathbb{A}_F)$ and $\mathrm{U}(W)(\mathbb{A}_F)$ inside $\mathrm{GL}_n(\mathbb{A}_E)$ and $\mathrm{GL}_d(\mathbb{A}_E)$.

**Definition 1.7.2 (Periodic function).** For $m \in \mathbb{N}$ with $m > 0$, a function $f$ on $\mathbb{A}_F^{\,n \times d}$ is *$m$-periodic* if $f(x + z) = f(x)$ for each $z = ma$ with $a$ integral at all finite places and with archimedean part $0$.

**Definition 1.7.3 (Words).** An *operator* is either a derivative $\partial_v$ in the archimedean variable, for $v \in F_\infty^{\,n\times d}$, or multiplication by $\ell(x_\infty)$ for a real linear form $\ell$. Its *size* is $|v|$ or $\|\ell\|$. A *word* is a finite product of operators.

Words of operators of size at most $1$ map $\mathcal{S}(\mathbb{A}_F^{\,n \times d})$ to itself. Multiplication by $\ell(x_\infty)$ keeps $m$-periodicity, since translation by $z$ does not change $x_\infty$.

### Four inputs

The proof combines four estimates.

1. *Polynomial weights.* For each $N$ there are real linear forms $\ell_1, \dots, \ell_K$ with $\|\ell_j\| \leq 1$ and a constant $C_0$ with $(1 + |y|)^N \leq C_0\,\bigl(1 + \sum_j |\ell_j(y)|^N\bigr)$ for all $y \in F_\infty^{\,n\times d}$.
2. *Sobolev bound for periodic functions.* For a Haar measure $\mu$ there are $P$, $C_s$ and $c$ such that, if $f \in \mathcal{S}(\mathbb{A}_F^{\,n \times d})$ is $m$-periodic and $\int |Df|^2\, d\mu \leq b$ for each word $D$ of at most $P$ derivatives of size at most $1$, then $|f(x)|^2 \leq C_s\, m^c\, b$ for all $x$.
3. *Period bound.* For each $\Phi$ there are $C_1$ and $k_1$ such that each $\omega(g,h)\Phi$ is $m$-periodic for some $m$ with $0 < m \leq C_1\,(\operatorname{ht}(g)\operatorname{ht}(h))^{k_1}$.
4. *$L^2$ bound on words.* For each $\Phi$ and each $p$ there are $C_2$ and $k_2$ such that $\int |D\,\omega(g,h)\Phi|^2\, d\mu \leq C_2\,(\operatorname{ht}(g)\operatorname{ht}(h))^{k_2}$ for each word $D$ of length at most $p$ in operators of size at most $1$.

The first is elementary: on a finite dimensional space $|y|^N$ is bounded by a multiple of $\sum_j |\ell_j(y)|^N$ for the coordinate forms and their sign changes. The second is the Sobolev inequality on $F_\infty^{\,n \times d}$, applied to each translate of the finite part; periodicity reduces the finite part to a finite quotient of size a power of $m$. The third holds since the finite part of $\Phi$ is invariant under a lattice, and $\omega(g_{\mathrm f}, h_{\mathrm f})$ moves this lattice by an amount controlled by the entries of $g$ and $h$. The fourth holds since $\omega$ is unitary on $L^2$ and each operator of a word is conjugated by $\omega(g,h)$ to a linear combination of operators whose sizes are bounded by a power of the heights.

### The theorem

**Theorem 1.7.4 (Pointwise archimedean decay).** For each $\Phi \in \mathcal{S}(\mathbb{A}_F^{\,n \times d})$ and each $N \in \mathbb{N}$ there are $C$ and $k$ such that
$$|\omega(g,h)\Phi(x)|\,(1 + |x_\infty|)^N \leq C\,\bigl(\operatorname{ht}(g)\operatorname{ht}(h)\bigr)^k$$
for all $g \in \mathrm{U}(X)(\mathbb{A}_F)$, $h \in \mathrm{U}(W)(\mathbb{A}_F)$ and $x \in \mathbb{A}_F^{\,n \times d}$.

Lean: `GlobalTheory.ArchDecay.om_bound_arch` (also `GlobalTheory.T.weilRepresentation_pointwise_archimedeanDecay_bound`, a second name).

*Proof.* Fix a Haar measure $\mu$, and take $\ell_j$, $C_0$ from input 1, $P$, $C_s$, $c$ from input 2, $C_1$, $k_1$ from input 3, and $C_2$, $k_2$ from input 4 with $p = P + N$. Put
$$A = \max\bigl(C_s\, C_1^{\,c}\, C_2,\ 1\bigr), \qquad k = k_1 c + k_2,$$
with $C_1$ replaced by $\max(C_1, 1)$ and $C_s, C_2$ by their positive parts. Fix $g$ and $h$, put $H = \operatorname{ht}(g)\operatorname{ht}(h) \geq 1$, and let $m$ be the period from input 3.

Claim: for each word $D$ of at most $N$ multiplication operators of size at most $1$, one has $|D\,\omega(g,h)\Phi(x)| \leq A H^k$ for all $x$. The function $f = D\,\omega(g,h)\Phi$ lies in $\mathcal{S}(\mathbb{A}_F^{\,n\times d})$, and it is $m$-periodic, since $\omega(g,h)\Phi$ is and multiplication operators keep periodicity. For a word $D'$ of at most $P$ derivatives of size at most $1$, the word $D'D$ has length at most $P + N$, so input 4 gives $\int |D'f|^2\, d\mu \leq C_2 H^{k_2}$. Input 2 with $b = C_2 H^{k_2}$ gives
$$|f(x)|^2 \leq C_s\, m^c\, C_2 H^{k_2} \leq C_s\, (C_1 H^{k_1})^c\, C_2 H^{k_2} \leq A H^k.$$
Since $A H^k \geq 1$, the inequality $|f(x)|^2 \leq A H^k$ gives $|f(x)| \leq A H^k$. This proves the claim.

Apply the claim to the empty word and to the words $\ell_j^N$, that is, multiplication by $\ell_j(x_\infty)^N$. This gives $|\omega(g,h)\Phi(x)| \leq AH^k$ and $|\ell_j(x_\infty)|^N |\omega(g,h)\Phi(x)| \leq AH^k$ for each $j$. By input 1,
$$\begin{aligned} |\omega(g,h)\Phi(x)|\,(1 + |x_\infty|)^N &\leq C_0 \Bigl(|\omega(g,h)\Phi(x)| + \sum_j |\ell_j(x_\infty)|^N |\omega(g,h)\Phi(x)|\Bigr) \\ &\leq C_0\,(K+1)\, A\, H^k. \end{aligned}$$
So $C = C_0 (K + 1) A$ works. $\square$

**Remark 1.7.5.** The bound is the adelic form of the estimates in A. Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), Chapter I, where the convergence of theta series is proved from the decay of $\omega(g)\Phi$. The point of the present form is that the constant depends on $g$ and $h$ only through a power of the heights, which is what a bound of moderate growth needs.

**Remark 1.7.6 (Formalization).** The theorem is `GlobalTheory.ArchDecay.om_bound_arch` (WeilRepresentationPointwiseArchimedeanDecayBound.lean, line 46). The four inputs are `one_add_norm_pow_le_sum_linearForm_pow`, `sobolev_bound_periodic_schwartz`, `weilRep_finite_periodicity_polynomial_height` and `word_action_square_integrable_bound` in `GlobalTheory.T`, wrappers of `onePlusNormPow_le_sum_linearForm_pow`, `sobolev_per`, `per_om_level` and `word_action_square_integrable` in `GlobalTheory.ArchDecay`. We have not opened their proofs, so the reasons given for them above are ours. The helpers `per_mM` (periodicity is kept by multiplication) and `norm_word_rep` (the norm of a repeated multiplication) are in the same file as the theorem. The Haar measure is the fixed `Measure.addHaar` on the Borel structure, and the height is `heightGL` (Definitions/Foundations/EventuallyNormFinLeOne.lean, line 405). Stability of the Schwartz space under $\omega$ is taken from the field `weil` of the hypothesis `IsPair`. The second name is a `first | exact ...` wrapper under `maxHeartbeats 1000000` (WeilRepresentationPointwiseArchimedeanDecayBoundStatement.lean, line 10).
