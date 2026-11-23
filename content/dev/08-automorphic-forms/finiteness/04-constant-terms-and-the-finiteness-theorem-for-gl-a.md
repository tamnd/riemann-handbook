---
title: Constant terms and the finiteness theorem for GL(a)
decls:
  - GlobalTheory.LeviSliceTwo.secondSlice_mem_finiteDimensional
  - GlobalTheory.T.finiteDimensional_forms_gl_of_open_level_induction
  - GlobalTheory.LeviCT.finiteDimensional_levi
  - GlobalTheory.T.finiteDimensional_automorphic_forms_GL
  - GlobalTheory.HCFct.finiteDimensional_constTerm
  - GlobalTheory.T.finiteDimensional_forms_span_level
  - GlobalTheory.HCFGLct.exists_ct_map
  - GlobalTheory.HCFGL.finiteDimensional_single
  - GlobalTheory.T.harishChandraFinitenessTotallyComplexGL_proof
  - GlobalTheory.automorphicFormsFiniteGL
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Constant terms and the finiteness theorem for GL(a)

This section proves the finiteness theorem of Harish-Chandra for $\mathrm{GL}_a$ over a totally complex field: automorphic forms of a fixed level, with fixed $K_\infty$-types and a fixed eigencharacter of the center, span a finite-dimensional space. The proof is by induction on $a$. The constant term of a form along a maximal parabolic subgroup is, on the Levi subgroup $\mathrm{GL}_r \times \mathrm{GL}_{a-r}$, a function whose slices are automorphic forms of smaller rank, so the constant terms span a finite-dimensional space by induction. A form whose constant terms all vanish is a cusp form, and [the finiteness of cusp forms](/entry/finite-dimensional-cusp-gl/) handles those. The theorem is used in [the step on every character](/step/every-character/). We keep the notation of the previous section: $E$ is totally complex, and $\mathcal{A}(L, W, X, N)$ is the set of forms of level $L$, $K_\infty$-types in $W$, and generalized eigencharacter in $X$ of order $N$.

Throughout, $0 < r < a$, $N_r$ is the unipotent radical of the standard parabolic subgroup of type $(r, a-r)$, and $M_r \cong \mathrm{GL}_r \times \mathrm{GL}_{a-r}$ is the block diagonal Levi subgroup. We write $\operatorname{diag}(m_1, m_2)$ for the block diagonal matrix. Fix a Haar measure $\mu$ on $N_r(\mathbb{A})$ and a fundamental domain $\mathcal{F}$ of $N_r(E)$ with $\mu(\mathcal{F}) = 1$. The *constant term* of $\varphi$ along $N_r$ is
$$\varphi_{N_r}(g) = \int_{\mathcal{F}} \varphi(n g)\, d\mu(n).$$
For $\varphi$ continuous and left invariant under $\mathrm{GL}_a(E)$ the integral converges, it does not depend on the choice of $\mathcal{F}$, and $\varphi_{N_r}$ is left invariant under $N_r(\mathbb{A})$.

The induction hypothesis for $a$ is:

$(\mathrm{H}_a)$ for each $b < a$, each open $L' \subseteq \mathrm{GL}_b(\mathbb{A}_f)$, each finite-dimensional $W'$, each finite $X'$ and each $N'$, the span of $\mathcal{A}(L', W', X', N')$ for $\mathrm{GL}_b$ is finite-dimensional.

### Slices of constant terms

**Lemma 1.4.1 (Functions with finite-dimensional slices).** Let $V_1$ and $V_2$ be finite-dimensional spaces of functions on sets $M_1$ and $M_2$. The functions $F$ on $M_1 \times M_2$ with $F(\cdot, m_2) \in V_1$ for every $m_2$ and $F(m_1, \cdot) \in V_2$ for every $m_1$ form a finite-dimensional space.

Lean: `GlobalTheory.LeviCT.finiteDimensional_slices`.

*Proof.* Since $V_2$ is finite-dimensional, there is a finite set $s \subseteq M_2$ such that each $w \in V_2$ that vanishes on $s$ is $0$: choose $s$ so that the subspace of $V_2$ of functions vanishing on $s$ is minimal; it is then $0$. The map $F \mapsto (F(\cdot, j))_{j \in s}$ goes into $V_1^s$. It is injective: if $F(\cdot, j) = 0$ for all $j \in s$, then each slice $F(m_1, \cdot) \in V_2$ vanishes on $s$, so it is $0$. $\square$

The next lemma is linear algebra. Let $\mathcal{Z}$ be a commutative algebra of operators on a space $V$ and $\psi \in V$. A vector $u \neq 0$ is an *eigenvector* of $\mathcal{Z}$ with eigencharacter $\chi'$ if $z u = \chi'(z) u$ for all $z \in \mathcal{Z}$.

**Lemma 1.4.2 (Decomposition into generalized eigenvectors).** Suppose that $\mathcal{Z}\psi$ is finite-dimensional of dimension at most $D$, and that each eigencharacter of an eigenvector in $\mathcal{Z}\psi$ agrees on $\mathcal{Z}$ with an element of a set $X'$. Then $\psi$ is a sum of vectors $\psi' \in \mathcal{Z}\psi$ such that, for some $\chi \in X'$, $(z_1 - \chi(z_1)) \cdots (z_D - \chi(z_D))\psi' = 0$ for all $z_i \in \mathcal{Z}$.

Lean: `GlobalTheory.T.mem_span_genEigen_of_finiteDimensional_orbit_alt`.

*Proof.* The commuting operators $\mathcal{Z}$ act on the finite-dimensional space $\mathcal{Z}\psi$, so this space is the direct sum of the generalized eigenspaces of $\mathcal{Z}$. Each of them has dimension at most $D$, so any $D$ operators $z_i - \chi(z_i)$ kill it, and each contains an eigenvector, whose character lies in $X'$ by hypothesis. $\square$

**Proposition 1.4.3 (Second slices of constant terms).** Assume $(\mathrm{H}_a)$. Let $L \subseteq \mathrm{GL}_a(\mathbb{A}_f)$ be open, $W$ finite-dimensional, $X$ finite and $N \ge 0$. Fix $t \in \mathrm{GL}_a(\mathbb{A}_f)$ and $\kappa \in K_\infty$. There is a finite-dimensional space $V_2$ of functions on $\mathrm{GL}_{a-r}(\mathbb{A})$ such that, for every $\varphi$ in the span of $\mathcal{A}(L, W, X, N)$ and every $m_1 \in \mathrm{GL}_r(\mathbb{A})$,
$$m_2 \longmapsto \varphi_{N_r}\big(\operatorname{diag}(m_1, m_2)\, t\, \kappa\big)$$
lies in $V_2$.

Lean: `GlobalTheory.LeviSliceTwo.secondSlice_mem_finiteDimensional` (also `GlobalTheory.T.finiteDimensional_forms_gl_of_open_level_induction`, a second name).

*Proof.* We use two facts on constant terms. First, there are an open $L' \subseteq \mathrm{GL}_{a-r}(\mathbb{A}_f)$ and a finite-dimensional $W'$ such that for each $\varphi \in \mathcal{A}(L, W, X, N)$ and each $m_1$ the slice $\psi$ above is a smooth function on $\mathrm{GL}_{a-r}(\mathbb{A})$ that satisfies conditions 1, 2, 3 and 5 of an automorphic form, is invariant under $L'$, and has its $K_\infty$-coefficients in $W'$. Second, there are a finite set $X'$ and $D \ge 0$ such that for each such $\psi$ the space $\mathcal{Z}\psi$ is finite-dimensional of dimension at most $D$, and every eigencharacter of an eigenvector in $\mathcal{Z}\psi$ agrees on $\mathcal{Z}$ with an element of $X'$. The second fact gives condition 4, so $\psi$ is an automorphic form. By the lemma on generalized eigenvectors, $\psi$ is a sum of elements $\psi' \in \mathcal{Z}\psi$ that are generalized eigenvectors of order $D$ for characters in $X'$. By a third fact, each element of $\mathcal{Z}\psi$ is again an automorphic form of level $L'$ with coefficients in $W'$; so $\psi' \in \mathcal{A}(L', W', X', D)$. Take $V_2$ the span of $\mathcal{A}(L', W', X', D)$ for $\mathrm{GL}_{a-r}$, which is finite-dimensional by $(\mathrm{H}_a)$. The set of $\varphi$ whose slices lie in $V_2$ is a subspace, since the constant term is linear (the integrals converge because each $\varphi$ is continuous and left invariant). $\square$

**Theorem 1.4.4 (Constant terms on the Levi subgroup).** Assume $(\mathrm{H}_a)$, and let $L$, $W$, $X$, $N$, $t$, $\kappa$ be as above. The functions
$$\operatorname{diag}(m_1, m_2) \longmapsto \varphi_{N_r}\big(\operatorname{diag}(m_1, m_2)\, t\, \kappa\big)$$
on $M_r(\mathbb{A})$, for $\varphi$ in the span of $\mathcal{A}(L, W, X, N)$, span a finite-dimensional space.

Lean: `GlobalTheory.LeviCT.finiteDimensional_levi` (also `GlobalTheory.T.finiteDimensional_automorphic_forms_GL`, a second name).

*Proof.* There is a finite-dimensional space $V_1$ of functions on $\mathrm{GL}_r(\mathbb{A})$ that contains the first slices $m_1 \mapsto \varphi_{N_r}(\operatorname{diag}(m_1, m_2) t \kappa)$ for all $\varphi$ and $m_2$, and [the proposition](/entry/second-slice-mem-finite-dimensional/) gives $V_2$ for the second slices. Write $M_r(\mathbb{A}) = \mathrm{GL}_r(\mathbb{A}) \times \mathrm{GL}_{a-r}(\mathbb{A})$. All the functions lie in the space of the lemma on slices for $V_1$ and $V_2$, which is finite-dimensional. $\square$

### The constant terms span a finite-dimensional space

**Theorem 1.4.5 (Finiteness of constant terms).** Assume $(\mathrm{H}_a)$. Let $L$ be open, $W$ finite-dimensional, $X$ finite and $N \ge 0$. Then the constant terms $\varphi_{N_r}$, for $\varphi$ in the span of $\mathcal{A}(L, W, X, N)$, span a finite-dimensional space of functions on $\mathrm{GL}_a(\mathbb{A})$.

Lean: `GlobalTheory.HCFct.finiteDimensional_constTerm`.

*Proof.* Let $V$ be the span of the constant terms. Each $f \in V$ is left invariant under $N_r(\mathbb{A})$, right invariant under $L$, and $k \mapsto f(g k)$ lies in $W$ for each $g$, since the constant term commutes with right translation. We use two facts. By the adelic Iwasawa decomposition there is a finite set $T \subseteq \mathrm{GL}_a(\mathbb{A}_f)$ with
$$\mathrm{GL}_a(\mathbb{A}) = N_r(\mathbb{A})\, M_r(\mathbb{A})\, T\, K_\infty\, L.$$
Since $W$ is finite-dimensional, there is a finite set $s \subseteq K_\infty$ such that each $w \in W$ that vanishes on $s$ is $0$. For $t \in T$ and $\kappa \in s$, let $V_{t,\kappa}$ be the span of the functions $m \mapsto f(m t \kappa)$ on $M_r(\mathbb{A})$; it is finite-dimensional by [the theorem on the Levi subgroup](/entry/finite-dimensional-levi/). The map $f \mapsto (m \mapsto f(m t \kappa))_{t, \kappa}$ from $V$ to $\bigoplus_{t, \kappa} V_{t,\kappa}$ is injective. If $f$ is in its kernel, write $g = n m t k l$ by the decomposition. Then $f(g) = f(m t k)$ by the invariance under $N_r(\mathbb{A})$ and $L$. The function $k \mapsto f(m t k)$ lies in $W$ and vanishes on $s$, so it is $0$. So $f = 0$. $\square$

**Theorem 1.4.6 (The constant term map).** Assume $(\mathrm{H}_a)$. Let $L$ be open, $W$ finite-dimensional, $\chi$ a map from operators to $\mathbb{C}$ and $N \ge 0$. There are $n$ and a linear map $T$ from smooth functions to $\mathbb{C}^n$ such that every $\varphi \in \mathcal{A}(L, W, \{\chi\}, N)$ with $T\varphi = 0$ is cuspidal.

Lean: `GlobalTheory.HCFGLct.exists_ct_map` (also `GlobalTheory.T.finiteDimensional_forms_span_level`, a second name).

*Proof.* For each $r$ with $0 < r < a$ choose $\mu_r$ and $\mathcal{F}_r$ with $\mu_r(\mathcal{F}_r) = 1$. Let $V$ be the span of $\mathcal{A}(L, W, \{\chi\}, N)$ and $\Lambda(\varphi) = (\varphi_{N_r})_r$, a linear map from $V$ to functions on the pairs $(r, g)$. By [the finiteness of constant terms](/entry/finite-dimensional-const-term/) its image lies in a finite-dimensional space. A finite-dimensional space of functions has a finite set of points that separates it, as in the proof of the lemma on slices. Let $T_0$ be the evaluation of $\Lambda$ at such a finite set, and $T$ a linear extension of $T_0$ from $V$ to all smooth functions. If $T\varphi = 0$, then $\Lambda(\varphi) = 0$, so $\int_{\mathcal{F}_r} \varphi(n g)\, d\mu_r = 0$ for all $r$ and $g$. The vanishing of this integral for one Haar measure and one fundamental domain implies it for all, since Haar measures differ by a scalar and the integral over a fundamental domain does not depend on its choice. So $\varphi$ is cuspidal. $\square$

### The finiteness theorem

**Theorem 1.4.7 (Forms of one eigencharacter).** Assume $(\mathrm{H}_a)$. Let $L \subseteq \mathrm{GL}_a(\mathbb{A}_f)$ be open, $W$ finite-dimensional, $\chi$ a map from operators to $\mathbb{C}$ and $N \ge 0$. Then the span of $\mathcal{A}(L, W, \{\chi\}, N)$ is finite-dimensional.

Lean: `GlobalTheory.HCFGL.finiteDimensional_single`.

*Proof.* Let $P$ be the span and $T : P \to \mathbb{C}^n$ the map of [the constant term map](/entry/exists-ct-map/). The set $\mathcal{A}(L, W, \{\chi\}, N)$ is itself a subspace, since all its conditions are linear for one $\chi$. So $P \cap \ker T$ consists of cuspidal elements of $\mathcal{A}(L, W, \{\chi\}, N)$, and it lies in the span $Q$ of these elements. By [the finiteness of cusp forms of one eigencharacter](/entry/finite-dimensional-cusp-span/), $Q$ is finite-dimensional; its smoothing hypothesis is supplied by a smooth function $\alpha$ with compact support in the invertible matrices that reproduces every form of $\mathcal{A}(L, W, \{\chi\}, N)$. Then $P$ is finite-dimensional, because $T(P) \subseteq \mathbb{C}^n$ and $P \cap \ker T$ are. $\square$

**Theorem 1.4.8 (Harish-Chandra finiteness for $\mathrm{GL}_a$, generalized eigenforms).** Let $E$ be a totally complex number field, $a \ge 0$, $L \subseteq \mathrm{GL}_a(\mathbb{A}_f)$ open, $W$ a finite-dimensional space of functions on $K_\infty$, $X$ a finite set of maps from operators to $\mathbb{C}$, and $N \ge 0$. Then the span of $\mathcal{A}(L, W, X, N)$ is finite-dimensional.

Lean: `GlobalTheory.HCFGL.coreFiniteGL` (also `GlobalTheory.T.harishChandraFinitenessTotallyComplexGL_proof`, a second name).

*Proof.* By strong induction on $a$; so $(\mathrm{H}_a)$ holds. Each element of $\mathcal{A}(L, W, X, N)$ lies in $\mathcal{A}(L, W, \{\chi\}, N)$ for some $\chi \in X$. So the span lies in the sum, over the finite set $X$, of the spans of $\mathcal{A}(L, W, \{\chi\}, N)$, each finite-dimensional by [the theorem for one eigencharacter](/entry/finite-dimensional-single/). $\square$

Now the published form. Let $\rho$ be a representation of $K_\infty$ on a finite-dimensional space $W_\rho$. Its *coefficient space* is the span of the functions $k \mapsto \ell(\rho(k) w)$ on $K_\infty$, for $w \in W_\rho$ and $\ell$ a linear form; it is finite-dimensional. The representation is *continuous* if these functions are continuous.

**Theorem 1.4.9 (Harish-Chandra finiteness for $\mathrm{GL}_a$).** Let $E$ be a totally complex number field, $L \subseteq \mathrm{GL}_a(\mathbb{A}_f)$ open, $\rho$ a continuous representation of $K_\infty$ on a finite-dimensional space, and $c(\tau, u) \in \mathbb{C}$ for each complex embedding $\tau$ and $u \in \mathbb{C}$. Let $\mathcal{A}(L, \rho, c)$ be the set of automorphic forms $\varphi$ invariant under $L$, with $k \mapsto \varphi(g k)$ in the coefficient space of $\rho$ for each $g$, and with $C_\tau(u)\varphi = c(\tau, u)\varphi$ for all $\tau$ and $u$. Then $\mathcal{A}(L, \rho, c)$ spans a finite-dimensional space.

Lean: `GlobalTheory.automorphicFormsFiniteGL` (also `GlobalTheory.T.harishChandra_finiteness_automorphic_GL_of_eigen`, for the step from generalized eigenforms).

*Proof.* The coefficient space $W$ of $\rho$ is finite-dimensional. Each $z \in \mathcal{Z}$ acts by one scalar $s(z)$ on all automorphic forms $\varphi$ with $C_\tau(u)\varphi = c(\tau, u)\varphi$ for all $\tau$ and $u$. Let $\chi(z) = s(z)$ when such a scalar exists and $\chi(z) = 0$ otherwise. Then $(z - \chi(z))\varphi = 0$ for $z \in \mathcal{Z}$ and $\varphi \in \mathcal{A}(L, \rho, c)$, so $\mathcal{A}(L, \rho, c) \subseteq \mathcal{A}(L, W, \{\chi\}, 1)$. Apply [the theorem for generalized eigenforms](/entry/harish-chandra-finiteness-totally-complex-gl-proof/). $\square$

**Remark 1.4.10 (Formalization).** The published theorem asks that $\rho$ be continuous; the proof does not use it. The scalar action of $\mathcal{Z}$ on eigenforms of the Capelli operators is the statement of `GlobalTheory.T.center_acts_by_scalar_on_eigenforms`, whose proof we did not open. The first slices in the proof of the theorem on the Levi subgroup come from `GlobalTheory.T.finiteDimensional_forms_gl_of_open_level`; we read its statement, not its proof. The two facts on constant terms in the proof of the second slices are the statements of `GlobalTheory.T.constant_term_finite_dimensional_span` and `GlobalTheory.T.constant_term_finite_dimensional_span_parabolic`, and the third fact is `GlobalTheory.T.finiteDimensional_forms_gl_inductive_rank`; we did not open their proofs, nor that of the decomposition into generalized eigenvectors. The Iwasawa decomposition is the statement of `GlobalTheory.T.adelicIwasawa_maximalParabolic_finiteReps`. The fact that the $K_\infty$-coefficients of a constant term lie in $W$ is called `GlobalTheory.T.fundamental_domain_measure_finite`, a name that says something different. In the theorem for one eigencharacter, the smoothing function comes from `GlobalTheory.T.harishChandra_uniform_smoothing_test_function`; it is passed to the corollary on cusp forms, which does not use it. All second names are proved by `first | exact @...`.
