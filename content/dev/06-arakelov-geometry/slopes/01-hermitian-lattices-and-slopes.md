---
title: Hermitian lattices and slopes
decls:
  - Formalism.HN.slopeIneqMean
  - Formalism.HN.slope_inequality_general
  - Formalism.L2.Col.T2.mu_eq_log_ht
  - Formalism.L2.GlobalTheoryTheory.TraceIntegrality.mu_of_frames
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hermitian lattices and slopes

This section fixes the notation of Volume 6 for hermitian lattices and defines the slope, the maximal slope and the minimal slope in the normalization that the proof uses. Then it proves three general facts: a formula for the slope through a height, a formula for the slope through a frame (a basis of the vector space together with local bases of the lattice), and the slope inequality. The frame formula computes the slopes of the auxiliary lattices of Section 7, and the slope inequality is the main tool of the upper bound for the maximal slope there.

### Notation

Throughout, $K$ is a [[number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$ and discriminant $d_K$ ([[discriminant|3BCYVS9E17]]), as in [the chapter on number fields](/learn/number-fields/#number-fields-and-their-integers). We write $S_\infty$ for the set of infinite places of $K$ and $n_\infty$ for its number of elements. For each $v \in S_\infty$ we fix one embedding $\sigma_v : K \to \mathbb{C}$ that induces $v$. Most results assume that $K$ is totally complex. Then every $v$ is complex and $[K : \mathbb{Q}] = 2 n_\infty$. For a nonzero prime $\mathfrak{p}$ of $\mathcal{O}_K$ we write $v_{\mathfrak{p}}$ for its additive valuation on $K$ and $N\mathfrak{p}$ for its norm ([[ideal norm|M54ADM0CVF]]).

**Definition 1.1.1 (Hermitian lattice datum).** A *hermitian lattice datum* over $K$ is a tuple $A = (V, b, X, L)$ where $V$ is a $K$-vector space with a finite basis $b = (b_i)_{i \in I}$, $X = (X_v)_{v \in S_\infty}$ is a family of complex matrices indexed by $I \times I$, and $L \subseteq V$ is an $\mathcal{O}_K$-submodule. For $x = \sum_i x_i b_i$ in $V$ put $x^v = (\sigma_v(x_i))_{i \in I} \in \mathbb{C}^I$ and $f_v(x) = X_v^{-1} x^v$. The *majorant* at $v$ is
$$
\langle x, y \rangle_v = \sum_{i \in I} \overline{f_v(x)_i}\, f_v(y)_i, \qquad \|x\|_v = \langle x, x \rangle_v^{1/2}.
$$
We say that $A$ has *invertible frames* if $\det X_v \neq 0$ for every $v$. We say that $A$ is *good* if it has invertible frames, $L$ is finitely generated, and $L$ spans $V$ over $K$. For an $\mathcal{O}_K$-submodule $L' \subseteq V$ we write $A[L']$ for the datum $(V, b, X, L')$, and we often write $\mu(L')$ for $\mu(A[L'])$ when $A$ is fixed.

If the frames are invertible, then $\langle\cdot,\cdot\rangle_v$ extends to a positive definite [[hermitian form|8NJ7XY6F1S]] on $V \otimes_{K, \sigma_v} \mathbb{C}$, and the columns of $X_v$ are an orthonormal basis for it: the matrix $X_v$ is the frame of the metric at $v$. If $A$ is good, then $L$ is a finitely generated torsion-free module over the [[Dedekind domain|7NPY2CN5KB]] $\mathcal{O}_K$, so it is projective, and $L \otimes_{\mathcal{O}_K} K = V$. With the norm $\|\cdot\|_v$ at $\sigma_v$ and its conjugate at $\bar\sigma_v$, a good datum is a [hermitian lattice](/learn/arakelov/#hermitian-lattices-and-slopes) in the sense of Volume 1, together with a choice of basis that makes the metric computable.

**Definition 1.1.2 (Realization).** Let $A$ be a hermitian lattice datum. Its *realization* is the additive map
$$
\rho_A : V \to \mathbb{R}^{S_\infty \times I \times \{1, 2\}}, \qquad \rho_A(x)_{v, i, 1} = \operatorname{Re} f_v(x)_i, \quad \rho_A(x)_{v, i, 2} = \operatorname{Im} f_v(x)_i,
$$
where the target has its standard Euclidean norm. So $|\rho_A(x)|^2 = \sum_{v} \|x\|_v^2$.

**Definition 1.1.3 (Covolume, degree and slope of a $\mathbb{Z}$-module).** Let $E$ be a Euclidean space and $\Lambda \subseteq E$ a subgroup. The *covolume* $\operatorname{covol}(\Lambda)$ is the square root of the [[Gram determinant|00SPJSDT3Z]] of a $\mathbb{Z}$-basis of $\Lambda$ if $\Lambda$ is discrete, and $0$ otherwise. The *rank* $\operatorname{rk}\Lambda$ is its rank over $\mathbb{Z}$, the *degree* is $\deg \Lambda = -\log \operatorname{covol}(\Lambda)$, and the *slope* is $s(\Lambda) = \deg\Lambda / \operatorname{rk}\Lambda$. A subgroup $\Lambda' \subseteq \Lambda$ is *saturated* if every element of $\Lambda$ in the real span of $\Lambda'$ lies in $\Lambda'$. The *quotient* $\Lambda / \Lambda'$ is realized as the image of $\Lambda$ under the orthogonal projection onto the orthogonal complement of the real span of $\Lambda'$.

The degree is the arithmetic degree of a Euclidean lattice of Volume 1. A discrete subgroup is a lattice in its real span, and the quotient by a saturated subgroup is again discrete, with $\deg \Lambda = \deg \Lambda' + \deg(\Lambda/\Lambda')$.

**Definition 1.1.4 (Slopes of a hermitian lattice datum).** Let $A = (V, b, X, L)$ be a hermitian lattice datum and $\rho = \rho_A$. Put $\kappa_K = -\log 2 + \log|d_K| / [K : \mathbb{Q}]$. The *slope*, the *maximal slope* and the *minimal slope* of $A$ are
$$
\begin{aligned}
\mu(A) &= 2\, s(\rho(L)) + \kappa_K, \\
\mu_{\max}(A) &= 2 \sup \{ s(\rho(N)) : N \subseteq L \text{ an } \mathcal{O}_K\text{-submodule}, N \neq 0 \} + \kappa_K, \\
\mu_{\min}(A) &= 2 \inf \{ s(\rho(L)/\rho(N)) : N \subsetneq L,\ \rho(N) \text{ saturated in } \rho(L) \} + \kappa_K.
\end{aligned}
$$

The constant $\kappa_K$ makes the trivial line have slope zero, as the first example shows. The factor $2$ is the price of the metric $\sum_v \|x\|_v^2$, which counts each complex place once.

**Example 1.1.5.** Let $K$ be totally complex, $V = K$, $b = (1)$, $X_v = 1$ for all $v$, and $L = \mathcal{O}_K$. Then $\rho$ is the map $x \mapsto (\sigma_v(x))_v$ into $\mathbb{C}^{n_\infty} = \mathbb{R}^{2 n_\infty}$. The covolume of $\mathcal{O}_K$ there is $2^{-n_\infty}\sqrt{|d_K|}$ (Neukirch, Chapter I, Proposition 5.2, where the canonical measure is $2^{n_\infty}$ times the Lebesgue measure). So $s(\rho(\mathcal{O}_K)) = \frac12 \log 2 - \log|d_K| / (2[K:\mathbb{Q}])$ and $\mu(A) = 0$. If instead $X_v = t^{-1}$ for a real $t > 0$, then $\|1\|_v = t$, the covolume is multiplied by $t^{2 n_\infty}$, and $\mu(A) = -2 \log t$.

**Remark 1.1.6 (Comparison with Volume 1).** Let $K$ be totally complex and $A$ good, and let $\overline{E}$ be the hermitian lattice $L$ with the norms $\|\cdot\|_v$, of rank $r$ and slope $\widehat{\mu}(\overline{E})$ in the sense of Volume 1. The norm of the realization is half the trace norm $\sum_\sigma \|x\|_\sigma^2$ over all embeddings, and the trace norm gives $\mathcal{O}_K$ the covolume $\sqrt{|d_K|}$. From $\widehat{\deg}(\overline{E}) = -\log \operatorname{covol}_{\mathrm{tr}}(L) + \frac{r}{2}\log|d_K|$ one gets $s(\rho(L)) = \widehat{\mu}(\overline{E}) + \frac12 \log 2 - \log|d_K|/(2[K:\mathbb{Q}])$, hence
$$
\mu(A) = 2\,\widehat{\mu}(\overline{E}).
$$
The same holds for the maximal slopes. So every inequality of this volume between slopes is twice the corresponding inequality of Volume 1.

### The slope through a height and through a frame

**Theorem 1.1.7 (Height formula).** Let $K$ be totally complex, and let $A = (V, b, X, L)$ have invertible frames with $L$ finitely generated and $L \neq 0$. Let $r = \dim_K (K L)$ and define the *height*
$$
\operatorname{ht}(A) = 2^{n_\infty r}\, |d_K|^{-r/2} \operatorname{covol}(\rho_A(L)).
$$
Then $\mu(A) = -\log \operatorname{ht}(A) / (n_\infty r)$.

Lean: `Formalism.L2.Col.T2.mu_eq_log_ht`

*Proof.* Since the frames are invertible, $\rho_A$ is injective, and $\rho_A(L)$ is a discrete subgroup of rank $[K:\mathbb{Q}]\, r = 2 n_\infty r$ with positive covolume. Hence $-\log \operatorname{ht}(A) / (n_\infty r) = -\log 2 + \log|d_K|/(2 n_\infty) + 2 \deg \rho_A(L) / (2 n_\infty r)$, which is $\kappa_K + 2 s(\rho_A(L)) = \mu(A)$. $\square$

**Definition 1.1.8 (Frame).** Let $A = (V, b, X, L)$ be a hermitian lattice datum and $J$ a finite set. A *frame* of $A$ indexed by $J$ is a $K$-basis $e = (e_j)_{j \in J}$ of $V$ together with a matrix $\Gamma_{\mathfrak{p}} \in \mathrm{GL}_J(K)$ for every nonzero prime $\mathfrak{p}$, such that the localization $L_{\mathfrak{p}}$ equals the localization at $\mathfrak{p}$ of the $\mathcal{O}_K$-span of the vectors $e'_j = \sum_k (\Gamma_{\mathfrak{p}})_{kj}\, e_k$. Its *Gram matrices* are $G_v = (\langle e_a, e_c \rangle_v)_{a, c \in J}$.

A frame is a global basis of $V$, which controls the metric, and a local basis of $L$ at each prime, written in the global basis. The next formula splits the slope into these two contributions.

**Theorem 1.1.9 (Frame formula).** Let $K$ be totally complex, $A$ a good hermitian lattice datum, and $(e, \Gamma)$ a frame of $A$ indexed by a nonempty finite set $J$. Then $\operatorname{Re} \det G_v > 0$ for every $v \in S_\infty$, $v_{\mathfrak{p}}(\det \Gamma_{\mathfrak{p}}) = 0$ for all but finitely many $\mathfrak{p}$, and
$$
|J| \cdot \mu(A) = -\frac{1}{n_\infty} \sum_{v \in S_\infty} \log \operatorname{Re} \det G_v \;-\; 2 \sum_{\mathfrak{p}} \frac{\log N\mathfrak{p}}{[K:\mathbb{Q}]}\, v_{\mathfrak{p}}(\det \Gamma_{\mathfrak{p}}).
$$

Lean: `Formalism.L2.GlobalTheoryTheory.TraceIntegrality.mu_of_frames`

*Proof.* Let $L_e = \bigoplus_j \mathcal{O}_K e_j$. Let $F_v$ be the matrix of the vectors $f_v(e_j)$, so that $G_v = F_v^* F_v$ is the Gram matrix of a basis and $\det G_v = |\det F_v|^2 > 0$. In the coordinates $f_v$, the realization of $L_e$ is the image of $\rho(\mathcal{O}_K)^J$ under the complex linear maps $F_v$, and a complex linear map multiplies real volumes by $|\det|^2$. With the covolume of the example, $\operatorname{covol} \rho(L_e) = (2^{-n_\infty}\sqrt{|d_K|})^{|J|} \prod_v \det G_v$, and the definition of $\mu$ gives $|J|\, \mu(L_e) = -\frac{1}{n_\infty}\sum_v \log \det G_v$. The lattices $L$ and $L_e$ agree at all but finitely many primes, since $L$ is finitely generated and spans $V$. Their covolumes differ by the generalized index $[L_e : L] = \prod_{\mathfrak{p}} N\mathfrak{p}^{\,v_{\mathfrak{p}}(\det \Gamma_{\mathfrak{p}})}$, computed prime by prime from the local bases. This changes $\deg$ by $-\sum_{\mathfrak{p}} v_{\mathfrak{p}}(\det\Gamma_{\mathfrak{p}}) \log N\mathfrak{p}$ and so $|J|\,\mu$ by twice this divided by $[K:\mathbb{Q}]$. $\square$

For $L = a\mathcal{O}_K \subseteq K$ with $X_v = 1$, $e = (1)$ and $\Gamma_{\mathfrak{p}} = (a)$, the formula gives $\mu = -2 \log|N_{K/\mathbb{Q}}(a)| / [K:\mathbb{Q}]$, which is twice the slope of Volume 1.

### The slope inequality

The slope inequality is first a statement on Euclidean lattices. Let $R$ be a ring, $V$ an $R$-module, $E$ a Euclidean space and $\rho : V \to E$ an additive map. An $R$-submodule $L \subseteq V$ is a *lattice for $\rho$* if $\rho$ is injective on $L$ and $\rho(L)$ is discrete. Then $s$, $\mu_{\max}$ and $\mu_{\min}$ are defined as above without the factor $2$ and the constant $\kappa_K$, with $R$-submodules in place of $\mathcal{O}_K$-submodules.

**Theorem 1.1.10 (Slope inequality for Euclidean lattices).** Let $L \subseteq V$ be a lattice for $\rho : V \to E$ and $M \subseteq W$ a lattice for $\rho' : W \to F$. Let $\varphi : L \to M$ be $R$-linear and $C > 0$ with $|\rho'(\varphi x)| \leq C |\rho(x)|$ for all $x \in L$. If $\varphi \neq 0$, then
$$
\mu_{\min}(L) - \log C \leq \mu_{\min}(\varphi(L)), \qquad \mu_{\min}(L) \leq \mu_{\max}(M) + \log C.
$$
If $\varphi$ is injective and $L \neq 0$, then $\mu_{\max}(L) \leq \mu_{\max}(M) + \log C$.

Lean: `Formalism.HN.slope_inequality_general`

*Proof.* The map $\rho(x) \mapsto \rho'(\varphi x)$ extends to a real linear map $T$ from the span of $\rho(L)$ to $F$, of operator norm at most $C$, because the rational multiples of $\rho(L)$ are dense in the span. A real linear map of norm at most $C$ between spaces of the same dimension $d$ multiplies volumes by at most $C^d$ (Hadamard's inequality applied to its singular values). Let $N \subseteq L$ be nonzero and $\varphi$ injective. Then $\operatorname{covol} \rho'(\varphi N) \leq C^{\operatorname{rk} N} \operatorname{covol} \rho(N)$, so $s(N) \leq s(\varphi N) + \log C \leq \mu_{\max}(M) + \log C$. For the minimal slope, let $N' \subsetneq \varphi(L)$ be saturated and $N$ its preimage in $L$, which is saturated and different from $L$. Since $T$ vanishes on the span of $N$, the induced map from the quotient $L/N$ onto $\varphi(L)/N'$ is a bijection of norm at most $C$, so $\mu_{\min}(L) \leq s(L/N) \leq s(\varphi(L)/N') + \log C$. This is the first inequality. For the second take $N'$ to be zero: then $\mu_{\min}(L) \leq s(\varphi L) + \log C \leq \mu_{\max}(M) + \log C$. $\square$

For a linear map between hermitian lattice data, the norm at $v$ is the operator norm $\|\varphi\|_v$ of $\varphi$ from $\|\cdot\|_v$ to $\|\cdot\|'_v$, that is, the operator norm of the complex matrix $X'^{-1}_v\, \sigma_v(\operatorname{Mat}\varphi)\, X_v$. The *height* of $\varphi$ is the mean
$$
h(\varphi) = \frac{1}{n_\infty} \sum_{v \in S_\infty} \log \|\varphi\|_v^2.
$$

**Theorem 1.1.11 (Slope inequality).** Let $K$ be totally complex. Let $(V, b, X)$ and $(W, b', X')$ have invertible frames, and let $\varphi : V \to W$ be $K$-linear. Let $A \subseteq V$ be a finitely generated $\mathcal{O}_K$-submodule with $\varphi(A) \neq 0$. Then
$$
\mu_{\min}(A) - h(\varphi) \leq \mu_{\min}(\varphi(A)),
$$
and for every finitely generated $\mathcal{O}_K$-submodule $B \subseteq W$ with $\varphi(A) \subseteq B$,
$$
\mu_{\min}(A) \leq \mu_{\max}(B) + h(\varphi), \qquad \text{and} \qquad \mu_{\max}(A) \leq \mu_{\max}(B) + h(\varphi) \ \text{ if } \varphi \text{ is injective on } A.
$$

Lean: `Formalism.HN.slopeIneqMean`

*Proof.* Since $\varphi \neq 0$ and the frames are invertible, $\|\varphi\|_v > 0$ for every $v$. Let $s = \frac12 h(\varphi) = \frac{1}{n_\infty}\sum_v \log\|\varphi\|_v$ and $c_v = \|\varphi\|_v e^{-s}$. Replace the frames of $W$ by $c_v X'_v$. This divides the norms at $v$ by $c_v$, so in the new metric $\|\varphi x\|''_v \leq e^{s}\|x\|_v$ for every $v$, and $|\rho''(\varphi x)| \leq e^{s} |\rho(x)|$. Rescaling the frames by positive constants $c_v$ adds $\frac{1}{n_\infty}\sum_v \log c_v$ to all the Euclidean slopes of submodules of $W$. Here this mean is $s - s = 0$, so the slopes of $W$ do not change. The finitely generated submodules are lattices for the realizations, because the frames are invertible. Now apply the slope inequality for Euclidean lattices with $C = e^{s}$ and multiply by $2$: the term $2\log C$ is $h(\varphi)$, and the constants $\kappa_K$ cancel. $\square$

**Remark 1.1.12.** If $\|\varphi x\|'_v \leq C \|x\|_v$ for all $v$ and $x$, then $h(\varphi) \leq 2\log C$. So for $\varphi$ injective on $A$ the theorem gives $\mu_{\max}(A) \leq \mu_{\max}(B) + 2\log C$, which by the comparison above is the [Bost slope inequality](/learn/arakelov/#hermitian-lattices-and-slopes) of Volume 1 in this normalization. The form with the mean $h(\varphi)$ is stronger, since only the geometric mean of the norms over the places enters.

**Remark 1.1.13 (Formalization).** The covolume of a nondiscrete subgroup is $0$, the logarithm of $0$ is $0$, and $\mu_{\max}$ and $\mu_{\min}$ are a supremum and an infimum of sets of reals, which are $0$ when the set is unbounded or empty ([Statement.lean](lean:Formalism/HarderNarasimhan/Statement.lean#L29)). All results here have hypotheses that avoid these cases. A hermitian lattice datum has no condition of total complexity, but the normalizing constant $\kappa_K$ is right only for totally complex $K$, and every result on $\mu$ assumes it. The formal proof of the Euclidean slope inequality goes through a characterization of $\mu_{\max}$ and $\mu_{\min}$ as the extreme slopes of a filtration, which we did not unfold. The argument given here is the classical direct one.
