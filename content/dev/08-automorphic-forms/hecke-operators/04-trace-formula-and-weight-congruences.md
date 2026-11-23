---
title: The trace formula and congruences between weights
decls:
  - UpperTheory.Esk.dAx
  - UpperTheory.Esk.linear_trace_identity_holds
  - UpperTheory.Esk.s_TF
  - UpperTheory.Esk.holWC_of
  - UpperTheory.Esk.holWC
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The trace formula and congruences between weights

This section proves that an ordinary Hilbert eigenform of weight $k_0$ is congruent, modulo the maximal ideal of $\bar{\mathbb{Z}}_l$, to an eigenform of weight $k_0 + 2t$ on a chosen set of real places, for $t$ as large as we like and divisible by $l - 1$. This is a form of the theorem of Hida and Wiles that ordinary forms move in $l$-adic families. It is used in [the mixed seed](/entry/mix-seed-of-alt/), together with the Eisenstein series of the previous section. The proof compares the traces of Hecke operators in the two weights through a trace formula, and then lifts an eigenvector by a lemma of Deligne and Serre.

### Hilbert modular forms of level $c$

Let $F$ be a totally real field of degree $r \ge 2$ and let $c = (c_w)$ be exponents at the finite places, almost all $0$. Let $\mathfrak{H}$ be the upper half-plane and $X = \mathfrak{H}^r$, with one factor for each real place. Let $H_c \subseteq \mathrm{GL}_2(\mathbb{A}_{F,f})$ be the product of the groups $K_1(\mathfrak{p}_w^{c_w})$ of the previous section with the finite ideles, viewed as scalars. Let $\chi$ be a character of finite order of $H_c$. For a weight $k = (k_v)$, let $M_k$ be the space of functions $f$ on $X \times \mathrm{GL}_2(\mathbb{A}_{F,f})$, holomorphic in the first variable, with
$$f(\gamma z, \gamma x h) = \chi(h)^{-1} \prod_v j(\gamma_v, z_v)^{k_v} f(z, x)$$
for $\gamma \in \mathrm{GL}_2(F)$ (totally positive determinant) and $h \in H_c$, and bounded at the cusps. These are the classical Hilbert modular forms of weight $k$ and level $c$, written on all components at once. A finite family $a_1, \dots, a_n$ of elements of $\mathrm{GL}_2(\mathbb{A}_{F,f})$ defines the operator
$$T_a f(z, x) = \sum_{i=1}^{n} f(z, x a_i).$$
For a finite list $W$ of finite places, the operator $\prod_{w \in W} U_w$ (with $U_w$ the double coset operator of $\begin{pmatrix} \varpi_w & 0 \\ 0 & 1 \end{pmatrix}$, which is $T_w$ when $c_w = 0$) is of this form for suitable $a_i$.

The forms are cut out by a height function. For $s \in F^2 \setminus 0$ and $x \in \mathrm{GL}_2(\mathbb{A}_{F,f})$, let $n(s, x) = \prod_w \max(|(s x)_1|_w, |(s x)_2|_w)$ and $h(s, x) = |\det x| / n(s, x)^2$. Combined with the imaginary parts of $z$, this measures how far $(z, x)$ is in the cusp attached to the row $s$.

**Lemma 6.4.1 (Axioms of the height).** Let $c$ have finite support and let $\chi$ have finite order. Then the data above satisfy the geometric axioms used by the trace formula: the set of components is countable and each Hecke orbit of a coset is finite; $h(s, x) > 0$, with the transformation rules $h(s, \gamma x) \prod_v |\det \gamma|_v = h(s\gamma, x)$ and $h(as, x) = h(s, x) \prod_v a_v^2$; $h$ is invariant under $H_c$ and changes by a bounded factor under right translation; $h(s, x) h(s', x) \le \prod_v \det(s, s')_v^2$ for independent rows; a Minkowski bound; a reduction to the standard cusp; and a count of the group elements that move a point by a small distance, linear in the height.

Lean: `UpperTheory.Esk.dAx`.

*Proof.* Each axiom is proved separately. The product inequality for two rows is the adelic form of the inequality $|\det(s, s')| \le \|s\| \|s'\|$, place by place. The Minkowski bound comes from Minkowski's theorem on lattice points, and the reduction and the count are the classical reduction theory for $\mathrm{GL}_2(F)$ acting on $\mathfrak{H}^r$ ([Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets)). $\square$

### The trace formula

Let $\Gamma = \mathrm{PGL}_2(F)$, acting on $X \times \mathrm{GL}_2(\mathbb{A}_{F,f})/H_c$. A *cut function* is a function $b \ge 0$ on this space with $\sum_{\gamma \in \Gamma} b(\gamma y) = 1$ for all $y$; it plays the role of the characteristic function of a fundamental domain. The operator $T_a$ on $M_k$ is given by a kernel: there is a function $K_{k,a}(\gamma, y)$, built from the reproducing kernel of weight $k$ on $\mathfrak{H}^r$, such that the trace of $T_a$ is the integral of $\sum_\gamma K_{k,a}(\gamma, y)$ on the diagonal.

**Lemma 6.4.2 (Trace of a kernel operator).** Assume that $M_k$ is finite-dimensional and stable under $T_a$, and let $b$ be a cut function. Then $y \mapsto b(y) \sum_{\gamma} K_{k,a}(\gamma, y)$ is integrable and
$$\operatorname{tr}(T_a \mid M_k) = \int b(y) \sum_{\gamma \in \Gamma} K_{k,a}(\gamma, y)\, dy.$$

Lean: `UpperTheory.Esk.linear_trace_identity_holds`.

*Proof.* Take an orthonormal basis $f_1, \dots, f_m$ of $M_k$ for the Petersson product. The reproducing kernel of $M_k$ is $\sum_j f_j(y) \overline{f_j(y')}$, and $T_a$ applied to it gives the kernel $K_{k,a}$ summed over $\Gamma$. Then $\operatorname{tr}(T_a) = \sum_j \langle T_a f_j, f_j \rangle$, and the Petersson product is the integral over a fundamental domain, which is the integral against $b$ over the whole space. The convergence comes from the finiteness of $\dim M_k$. $\square$

**Theorem 6.4.3 (Trace formula).** For every finite family $a$ there is a finite set $S$ of pairs (conjugacy class of $\Gamma$, component) such that for every weight $k$ with $k_v \ge 4$ for all $v$ and the compatibility and regularity conditions on $a$, and with $M_k$ finite-dimensional and stable under $T_a$,
$$\operatorname{tr}(T_a \mid M_k) = \sum_{(\gamma, \omega) \in S} \mathrm{geo}_k(a; \gamma, \omega),$$
an explicit sum of orbital integrals of the kernel.

Lean: `UpperTheory.Esk.s_TF`.

*Proof.* A cut function $b$ exists, and we start from the lemma. Split the sum over $\Gamma$ into the elliptic elements and the others. The sum of the kernel over all $\gamma$ is bounded on the quotient, so both parts are integrable against $b$. The non-elliptic part integrates to $0$: after a truncation in the cusp, the unipotent terms vanish, and the other terms are controlled by a bound on the trace of the kernel. For the elliptic part, the integral of a sum over $\Gamma$ against $b$ is a sum over pairs (conjugacy class, component) of orbital integrals over the centralizers, by a Fubini formula for cut functions. Only finitely many pairs give a nonzero term, and they depend on $a$ and not on $k$. They form $S$. $\square$

The point is the order of the quantifiers: $S$ is chosen before $k$. So the traces in all weights are given by the same finitely many terms, and each term depends on $k$ through explicit expressions in the eigenvalues of $\gamma$ at the real places.

### Congruences between weights

Let $l$ be an odd prime and fix an isomorphism $\iota : \bar{\mathbb{Q}}_l \to \mathbb{C}$. For $z \in \mathbb{C}$ write $|z|_\iota = |\iota^{-1}(z)|_l$. An *$l$-adic datum* is an injective map $v \mapsto \mathfrak{l}_v$ from the real places of $F$ to the places of $F$ above $l$, with embeddings $F_{\mathfrak{l}_v} \to \mathbb{C}$ compatible with $v$ and with $\iota$. For a weight $k_0$ and a finite place $w$, the normalized Hecke operator is $h_{k_0, w} = N(w)^{k_0/2 - 1}\, U_w$, acting on the space of holomorphic forms of the previous section.

**Lemma 6.4.4 (Trace congruence).** Let $k_0 \ge 4$, and let $c$, $\chi$ be as above, with $c_{\mathfrak{l}_v} = 1$ for all $v$ and $c_u \ne 0$ at some place $u$ of norm $2$. Let $(l - 1) l^N \mid t_v$ for all $v$. Let $W$ be a list of places that contains each $\mathfrak{l}_v$ at least $r' \ge 1$ times, and $a$ a family that realizes $\prod_{w \in W} U_w$. Put $n_t(w) = N(w)^{k_0/2 - 1} \prod_{\mathfrak{l}_v = w} l^{t_v}$. Then the normalized traces
$$\tau_0 = \prod_{w \in W} n_0(w)\, \operatorname{tr}(T_a \mid M_{k_0}), \qquad \tau_t = \prod_{w \in W} n_t(w)\, \operatorname{tr}(T_a \mid M_{k_0 + 2t})$$
satisfy $|\tau_0|_\iota \le 1$, $|\tau_t|_\iota \le 1$ and $|\tau_0 - \tau_t|_\iota \le \max(|l|_\iota^N, |l|_\iota^{r'})$.

*Proof.* Apply the trace formula with the same $S$ in both weights. Each elliptic term in weight $k$ is a multiple of $(\rho^{k-1} - \bar\rho^{k-1})/(\rho - \bar\rho)$ at each real place, with $\rho$, $\bar\rho$ the eigenvalues of $\gamma$. After the normalization, an eigenvalue that is a unit at $\mathfrak{l}_v$ is raised to the power $t_v$, which is $1$ modulo $l^{N}$ since $(l-1)l^N \mid t_v$. An eigenvalue that is not a unit is divisible by $\mathfrak{l}_v$, and appears to the power at least $r'$, since $\mathfrak{l}_v$ occurs $r'$ times in $W$. $\square$

**Lemma 6.4.5 (Deligne-Serre lifting).** Let $V$ and $V'$ be finite-dimensional, with commuting families of operators $T_i$ and $T'_i$ indexed by the same set, and a subset $L$ of the indices. Let $\varepsilon < |d|_\iota$ for $1 \le d \le \dim V$. Assume that for every word in the indices with at least $r$ letters in $L$, the traces of the word on $V$ and on $V'$ are integral and congruent up to $\max(\varepsilon, \rho^r)$. Then for every common eigenvector of the $T_i$ with unit eigenvalues on $L$, there is a common eigenvector of the $T'_i$ whose eigenvalues are congruent to those of the first, with $|s' - s|_\iota < 1$.

This is [Deligne-Serre, Lemme 6.11], in the form with traces. A congruence of traces of all words gives a congruence of characteristic polynomials of the commutative algebras, and so a common eigenvalue system modulo the maximal ideal.

**Theorem 6.4.6 (Weight congruence for ordinary forms).** Let $F$ be totally real with $[F:\mathbb{Q}] \ge 2$, $l$ an odd prime, $\iota$ and an $l$-adic datum as above, and $k_0 \ge 4$. Let $c$ have finite support, with $c_{\mathfrak{l}_v} = 1$ for all $v$ and $c_u \ne 0$ at some place $u$ with $N(u) = 2$. Let $\omega$ be a Hecke character of finite order and $\varphi$ a cusp form, holomorphic of weight $k_0$, level $c$ and central character $\omega$, with $h_{k_0, w}\varphi = \lambda(w)\varphi$ for all $w$ and $|\lambda(\mathfrak{l}_v)|_\iota = 1$ for all $v$. Then for every set $S$ of real places and every $B$ there are $t \ge B$ with $(l - 1) \mid t$, a nonzero cusp form $\varphi'$, holomorphic of weight $k_0 + 2t$ at the places in $S$ and $k_0$ elsewhere, of level $c$ and central character $\omega$, and numbers $\lambda'(w)$, such that $h_{k_0, w}\varphi' = \lambda'(w)\varphi'$ for all $w$ and
$$\Bigl|\, \prod_{v \in S,\ \mathfrak{l}_v = w} l^{t} \cdot \lambda'(w) - \lambda(w) \Bigr|_\iota < 1 \quad \text{for all } w.$$

Lean: `UpperTheory.Esk.holWC` (also `UpperTheory.Esk.holWC_of`, the same theorem from its inputs).

*Proof.* Let $N = \dim M_{k_0}$ and $t = (l - 1) l^N \max(B, 1)$. Put $t_v = t$ for $v \in S$ and $t_v = 0$ otherwise. Translate $\varphi$ into a function $f \in M_{k_0}$; this is a dictionary between adelic holomorphic forms and classical forms, compatible with the Hecke operators. Apply the Deligne-Serre lemma to $V = M_{k_0}$ and $V' = M_{k_0 + 2t}$, with the normalized operators $n_0(w)^{-1} h$ and $n_t(w)^{-1} h$, and $L$ the places $\mathfrak{l}_v$. The trace congruence gives the hypothesis with $\varepsilon = |l|_\iota^N$: since $N = \dim V$, every $d \le \dim V$ has $|d|_\iota \ge |l|_\iota^{N-1} > \varepsilon$. The eigenvector $f$ has unit eigenvalues at the $\mathfrak{l}_v$ by ordinarity. The lemma gives an eigenvector $f'$ in weight $k_0 + 2t$, and translating back gives $\varphi'$. The normalization $n_t(w)$ differs from $n_0(w)$ by $\prod_{\mathfrak{l}_v = w} l^{t_v}$, which is the factor in the congruence. Cuspidality of $\varphi'$ follows from the choice of the space. $\square$

**Remark 6.4.7 (Formalization).** In the theorem, the eigenvalue equation for $\varphi'$ uses the operator $h_{k_0, w}$ normalized for the old weight $k_0$, not for the new weight; the factor $l^t$ in the congruence compensates for this at the places $\mathfrak{l}_v$. In [FinalH.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalH.lean#L10) several inputs have names that do not match their statements: `hyperbolic_orbit_integral_holds` states that the character has finite order and is compatible with $\omega$, and `hyperbolic_terms_setup_holds`, `hyperbolic_terms_integrable_holds` state the dictionary between adelic and classical forms. In [FinalTF.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalTF.lean#L68), `kernel_inverse_symmetry_holds` is a statement about face maps of a simplex. The trace congruence is proved from three inputs: the congruence $u_{n+1}(\tau, \delta) \equiv \tau^n$ modulo $\delta$ for the sequence $u_0 = 0$, $u_1 = 1$, $u_{m+2} = \tau u_{m+1} - \delta u_m$ (so $u_m = (\rho^m - \bar\rho^m)/(\rho - \bar\rho)$ with $\rho + \bar\rho = \tau$, $\rho\bar\rho = \delta$), $x^t \equiv 1 \bmod l^N$ for units $x$ at $\mathfrak{l}_v$ when $(l-1)l^N \mid t$, and a unit property of the norm of ideles. We read these statements but did not unfold the kernel $K_{k,a}$, the elliptic terms, or the proof of the Deligne-Serre lemma; their descriptions above follow the statements we read.
