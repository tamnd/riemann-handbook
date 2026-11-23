---
title: Kernels from the wave equation
decls:
  - GlobalTheory.CompanionTheory.KerFc.kerCore
  - GlobalTheory.T.kernel_regularity
  - GlobalTheory.CompanionTheory.WaveMult.asmMult_main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernels from the wave equation

On the complex group $GL_n(\mathbb{C})$, a function of the Casimir operator of the form $\int g(t) \cosh(t\sqrt{\Omega})\, dt$, with $g$ an even bump function, is a convolution operator with a smooth kernel of compact support. This is the archimedean form of the Paley-Wiener theorem, and finite propagation speed for the wave equation $\partial_t^2 u = \Omega u$ is the reason why the support is compact. This section proves two results. The first constructs the kernel from the functional calculus of $\Omega$. The second shows that finite sums of these kernels, the multipliers, form a commutative algebra under convolution that is closed under adjoints, and that they act on eigenfunctions of the centre by scalars. The first result is a step in the existence of [kernels for one bump function](/entry/asm-ker-one/). The second is the multiplier part of the theorem on [waves, propagation speed and multipliers](/entry/wave-existence-speed-multiplicity/). The background is in [representations of real groups](/learn/representations/#representations-of-real-groups) and in [the trace formula for a compact quotient](/learn/trace-formula/#the-trace-formula-for-a-compact-quotient), where such kernels are the test functions.

### Setting

Let $G = GL_n(\mathbb{C})$, viewed as the set of invertible complex $n \times n$ matrices, with a Haar measure $\mu$, and let $K = U(n)$. The length of $y \in G$ is
$$\ell(y) = \log\Bigl(1 + \sum_{a,b} \bigl(|y_{ab}|^2 + |(y^{-1})_{ab}|^2\bigr)\Bigr).$$
It is subadditive, invariant under inversion and under $K$ on both sides, and its sublevel sets are compact. A function $f$ on $G$ has compact support in this sense if $f(y) = 0$ whenever $\ell(y) > R$, for some $R$.

Let $E$ be a $K$-module: a finite dimensional Hilbert space with a continuous unitary representation $\rho$ of $K$. A section of $E$ is a smooth function $f : G \to E$ with $f(gk) = \rho(k)^{-1} f(g)$ for $k \in K$. The right derivative $R_X f(g)$ is the derivative of $f$ at $g$ in the direction $gX$. From the right derivatives one forms the holomorphic and antiholomorphic matrices of operators $E_{s,ab}$, $s \in \{+, -\}$, and the Gelfand operators $Z_{s,m} = \sum_a (E_s^m)_{aa}$, which commute with left translation. The Casimir operator is $\Omega = 2(Z_{+,2} + Z_{-,2})$.

An infinitesimal character is a pair $\chi = (\chi_+, \chi_-)$ of vectors in $\mathbb{C}^n$. A section $f$ is an eigenfunction for $\chi$ if $Z_{s,m} f = \gamma_m(\chi_s) f$ for all $s$ and $m$, where $\gamma_m(\chi_s)$ is the eigenvalue of the Gelfand element of degree $m$ at the parameter $\chi_s$. The Casimir eigenvalue is $\operatorname{cas}(\chi) = 2(\gamma_2(\chi_+) + \gamma_2(\chi_-))$. For a word $w = ((s_1, m_1), \dots, (s_r, m_r))$, write $Z_w = Z_{s_1,m_1} \cdots Z_{s_r,m_r}$ and $z_w(\chi) = \prod_i \gamma_{m_i}(\chi_{s_i})$. The character $\chi$ is Hermitian if $\chi_-(\sigma a) = -\overline{\chi_+(a)}$ for some permutation $\sigma$ and all $a$.

**Definition 3.10.1 (Waves, bumps, kernels).** A wave is a smooth family $u(t)$, $t \in \mathbb{R}$, of sections with $\partial_t^2 u(t) = \Omega u(t)$ and $\partial_t u(0) = 0$. A bump of radius $T$ is a smooth even function $g : \mathbb{R} \to \mathbb{R}$ that vanishes for $|t| > T$. A kernel for a word $w$ and a function $g$ is a smooth map $k : G \to \operatorname{End}(E)$ with compact support such that $k(k_1 y k_2) = \rho(k_1) k(y) \rho(k_2)$ for $k_1, k_2 \in K$ and, for every wave $u$ and every $x$,
$$\int_G k(y)\, u(0)(xy)\, d\mu(y) = Z_w\Bigl( \int_{\mathbb{R}} g(t)\, u(t)\, dt \Bigr)(x).$$

The left side is the action $(k * f)(x) = \int_G k(y) f(xy)\, d\mu(y)$ of $k$ on $f = u(0)$. Formally $u(t) = \cosh(t\sqrt{\Omega})\, u(0)$, so a kernel for $w$ and $g$ represents the operator $Z_w \int g(t) \cosh(t\sqrt{\Omega})\, dt$. Its value on an eigenfunction for $\chi$ is the scalar
$$z_w(\chi)\, \widehat{g}(\operatorname{cas}\chi), \qquad \widehat{g}(c) = \int_{\mathbb{R}} g(t) \cosh(t\sqrt{c})\, dt.$$
The function $\widehat g$ is entire and does not depend on the branch of the square root, since $g$ is even.

### The kernel of a wave average

**Theorem 3.10.2 (Kernel of a wave average).** Assume the analytic facts listed below about $G$: the properties of the length, unimodularity, the calculus of right derivatives, the Sobolev inequality on $G$, the algebraic estimate for regularity, finite propagation speed, existence of waves with compactly supported initial data, the fifteen facts on the functional calculus of $\Omega$, the facts on smoothing operators, and the Paley-Wiener decay. Let $g$ be a bump of radius $T$. Then there is a smooth $k : G \to \operatorname{End}(E)$ with compact support and $k(k_1 y k_2) = \rho(k_1) k(y) \rho(k_2)$, such that for every compactly supported section $f$, every wave $u$ with $u(0) = f$ and every $x \in G$,
$$(k * f)(x) = \int_{\mathbb{R}} g(t)\, u(t)(x)\, dt.$$

Lean: `GlobalTheory.CompanionTheory.KerFc.kerCore` (also `GlobalTheory.T.kernel_regularity`, a second name).

The functional calculus works on the Hilbert space $L^2(G, E)$ of square integrable functions. The facts produce:

- (Calculus.) A dense Sobolev domain $M$, the operator $\Omega$ on $M$ (symmetric), the bounded operator $T_0 = (1 + \Omega^2)^{-1}$, and a $*$-homomorphism $\Phi$ from continuous functions vanishing at infinity on $\mathbb{R}$ to bounded operators, with $\Phi\bigl((1 + y^2)^{-1}\bigr) = T_0$. There is $c$ with $\operatorname{Re}\langle \Omega f, f\rangle \le c\|f\|^2$ for Sobolev sections $f$.
- (Paley-Wiener decay.) Put $h(y) = \operatorname{cut}_c(y) \int g(t) \cosh(t\sqrt{y})\, dt$, where $\operatorname{cut}_c(y) = \max(0, \min(1, c + 1 - y))$. Then $y^m h(y)$ is continuous and vanishes at infinity for every $m$; we say $h$ is rapid.
- (Smoothing.) For rapid $h$ and every $L^2$ limit $x$ of Sobolev sections, $\Phi(h) x$ is the class of a Sobolev section $f'$, with $\|f'(1)\| \le C \|x\|$.
- (Rows.) For rapid $h$ and $v \in E$ there is a Sobolev section $r_v$ with $\langle r_v, \varphi\rangle = \langle v, (\Phi(h)\varphi)(1)\rangle$ for all Sobolev sections $\varphi$. These rows form $r_v(y) = A(y)v$ for a function $A : G \to \operatorname{End}(E)$, and $y \mapsto A(y)^*$ is smooth.
- (Left translation.) $A(k y) v = A(y) \rho(k)^{-1} v$ for $k \in K$.
- (Action.) If $f$ is a compactly supported section and $f'$ a Sobolev section that represents $\Phi(h) f$, then $\int_G A(y)^* f(xy)\, d\mu(y) = f'(x)$.
- (Waves.) For a compactly supported section $f$ there are $N \ge 1$, $b \in L^2$ and a wave $U$ with $f = T_0^N b$, $U(0) = f$ and $U(t) = \Phi\bigl(\operatorname{cut}_c(y) (1 + y^2)^{-N} \cosh(t\sqrt{y})\bigr) b$. Two waves with the same initial value are equal.
- (Resolvent.) $\Phi\bigl((1 + y^2)^{-N} h\bigr) = \Phi(h) T_0^N$.
- (Wave integral.) In the situation of the fact on waves, if $f'$ represents $\Phi\bigl((1 + y^2)^{-N} h\bigr) b$, then $\int g(t)\, U(t)(x)\, dt = f'(x)$.
- (Support of rows.) If $\Phi(h)$ is given on compactly supported sections by the wave average $\int g(t) u(t)\, dt$, there is $R$ such that every row vanishes where $\ell(y) > R$.

On the spectrum of $\Omega$, which lies in $(-\infty, c]$, the cut-off is $1$, so $\Phi(h) = \int g(t) \cosh(t\sqrt{\Omega})\, dt$. The support of rows is finite propagation speed: this operator moves supports by at most a constant times $1 + T$ in the length.

*Proof.* Let $h$ be as in the Paley-Wiener decay, and let $A$ be the matrix of rows of $\Phi(h)$. Put $k(y) = A(y)^*$. It is smooth by the fact on rows.

First we show that $\Phi(h)$ is the wave average. Let $f$ be compactly supported, $u$ a wave with $u(0) = f$, and $f'$ a Sobolev section that represents $\Phi(h) f$. Take $N$, $b$ and $U$ from the fact on waves. By uniqueness, $u = U$. By the resolvent identity, $\Phi\bigl((1 + y^2)^{-N} h\bigr) b = \Phi(h) T_0^N b = \Phi(h) f$, which $f'$ represents. The wave integral gives $\int g(t)\, u(t)(x)\, dt = f'(x)$.

By the support of rows, $A$ and hence $k$ vanish where $\ell(y) > R$. Each row is a section, so $A(y k_2) = \rho(k_2)^{-1} A(y)$, and by left translation $A(k_1 y) = A(y) \rho(k_1)^{-1}$. So $A(k_1 y k_2) = \rho(k_2)^{-1} A(y) \rho(k_1)^{-1}$. Since $\rho$ is unitary, $(\rho(k)^{-1})^* = \rho(k)$, and taking adjoints gives $k(k_1 y k_2) = \rho(k_1) k(y) \rho(k_2)$.

Finally let $f$ and $u$ be as in the theorem. The smoothing fact gives a Sobolev section $f'$ that represents $\Phi(h) f$. The fact on the action gives $(k * f)(x) = f'(x)$, and the first step gives $f'(x) = \int g(t)\, u(t)(x)\, dt$. $\square$

### The algebra of multipliers

**Definition 3.10.3 (Multiplier).** A function $k : G \to \operatorname{End}(E)$ is a multiplier of radius $T$ with value $\operatorname{val}$ if there are finitely many constants $c_i$, words $w_i$, bumps $g_i$ of radius $T$ and kernels $k_i$ for $(w_i, g_i)$ with
$$k = \sum_i c_i\, k_i \quad \text{on } G, \qquad \operatorname{val}(\chi) = \sum_i c_i\, z_{w_i}(\chi)\, \widehat{g_i}(\operatorname{cas}\chi) \quad \text{for all } \chi.$$
The convolution of $k$ and $k'$ is $(k * k')(x) = \int_G k(y)\, k'(y^{-1} x)\, d\mu(y)$.

**Theorem 3.10.4 (Algebra of multipliers).** Assume the properties of the length, unimodularity, the calculus of right derivatives, finite propagation speed, existence of waves, uniqueness of kernels, and the existence of a kernel for every word and every bump. Let $k$ be a multiplier of radius $T$ with value $\operatorname{val}$ and $k'$ a multiplier of radius $T'$ with value $\operatorname{val}'$. Then:

1. $k * k'$ is a multiplier of radius $T + T'$ with value $\operatorname{val} \cdot \operatorname{val}'$;
2. $k * k' = k' * k$ on $G$;
3. $y \mapsto k(y^{-1})^*$ is a multiplier of radius $T$ with a value $\operatorname{val}_1$ such that $\operatorname{val}_1(\chi) = \overline{\operatorname{val}(\chi)}$ for every Hermitian $\chi$;
4. for every eigenfunction $f$ for $\chi$, $(k * f)(x) = \operatorname{val}(\chi) f(x)$ for all $x$.

Lean: `GlobalTheory.CompanionTheory.WaveMult.asmMult_main`.

We use the following facts, taken as given.

- (Convolution of bumps.) If $g$, $g'$ are bumps of radius $T$, $T'$, then $g * g'$ is a bump of radius $T + T'$, and $\widehat{g}(c)\, \widehat{g'}(c) = \widehat{g * g'}(c)$.
- (Convolution of kernels.) If $k$ is a kernel for $(w, g)$, $k'$ a kernel for $(w', g')$, and $K$ a kernel for $(ww', g * g')$, then $k * k' = K$ on $G$.
- (Order of words.) A kernel for $(ww', g)$ is a kernel for $(w'w, g)$.
- (Bilinearity.) Convolution of continuous compactly supported kernels is bilinear in finite sums.
- (Adjoint kernels.) If $k$ is a kernel for $(w, g)$, there are finitely many constants $d_j$, words $w_j$ and kernels $K_j$ for $(w_j, g)$ with $k(y^{-1})^* = \sum_j d_j K_j(y)$ and $\overline{z_w(\chi)} = \sum_j d_j z_{w_j}(\chi)$ for Hermitian $\chi$.
- (Reality.) For Hermitian $\chi$ and a bump $g$, $\widehat g(\operatorname{cas}\chi)$ is real.
- (Eigenfunctions.) A multiplier acts on an eigenfunction for $\chi$ by its value at $\chi$.

The identity for $\widehat g$ is the product formula $\cosh a \cosh b = \tfrac12(\cosh(a+b) + \cosh(a-b))$. With $\lambda = \sqrt{c}$,
$$\widehat g(c)\,\widehat{g'}(c) = \tfrac12 \iint g(t) g'(s) \bigl(\cosh((t+s)\lambda) + \cosh((t-s)\lambda)\bigr)\, ds\, dt,$$
and since $g'$ is even, the substitution $s \mapsto -s$ makes the two terms equal. So the product is $\iint g(t) g'(s) \cosh((t+s)\lambda)\, ds\, dt = \int (g * g')(r) \cosh(r\lambda)\, dr$. The convolution of kernels reflects the semigroup property of the wave propagator in the same way.

*Proof.* Write $k = \sum_i c_i k_i$ and $k' = \sum_j c'_j k'_j$ with kernels $k_i$ for $(w_i, g_i)$ and $k'_j$ for $(w'_j, g'_j)$. For each pair $(i, j)$, $g_i * g'_j$ is a bump of radius $T + T'$; choose a kernel $K_{ij}$ for $(w_i w'_j, g_i * g'_j)$.

1. By bilinearity and the convolution of kernels, $k * k' = \sum_{i,j} c_i c'_j K_{ij}$. Its value is
$$\sum_{i,j} c_i c'_j\, z_{w_i w'_j}(\chi)\, \widehat{g_i * g'_j}(\operatorname{cas}\chi) = \sum_{i,j} c_i z_{w_i}(\chi) \widehat{g_i}(\operatorname{cas}\chi) \cdot c'_j z_{w'_j}(\chi) \widehat{g'_j}(\operatorname{cas}\chi) = \operatorname{val}(\chi)\operatorname{val}'(\chi),$$
since $z$ of a concatenated word is the product and by the product formula for $\widehat g$.
2. By the order of words, $K_{ij}$ is a kernel for $(w'_j w_i, g'_j * g_i)$, since $g'_j * g_i = g_i * g'_j$. The convolution of kernels then gives $k'_j * k_i = K_{ij}$, and bilinearity gives $k' * k = \sum c_i c'_j K_{ij} = k * k'$.
3. By the fact on adjoint kernels, $k(y^{-1})^* = \sum_i \overline{c_i} \sum_j d_{ij} K_{ij}(y)$, a multiplier of radius $T$. Its value $\operatorname{val}_1(\chi) = \sum_{i,j} \overline{c_i} d_{ij}\, z_{w_{ij}}(\chi)\, \widehat{g_i}(\operatorname{cas}\chi)$ is, for Hermitian $\chi$, equal to $\sum_i \overline{c_i}\, \overline{z_{w_i}(\chi)}\, \widehat{g_i}(\operatorname{cas}\chi)$. By reality this is $\overline{\operatorname{val}(\chi)}$.
4. This is the fact on eigenfunctions. $\square$

Part 4 makes the map $k \mapsto \operatorname{val}$ an algebra homomorphism on the eigenfunctions, and part 3 says that it respects adjoints on the Hermitian characters. For a unitary representation, the characters that occur are Hermitian.

**Remark 3.10.5 (Formalization).** The first theorem is a proposition whose hypotheses are the analytic facts, among them the fifteen-fold conjunction of facts on the functional calculus; the theorem itself is proved by the lemma `kerCore_of`, which takes ten more facts of the form `GlobalTheory.T.*` (`kernel_row_exists`, `kernel_row_matrix`, `kernel_adjoint_smooth`, `kernel_row_left_invariant`, `kernel_action_formula`, `wave_representation`, `wave_uniqueness`, `phi_resolvent_identity`, `wave_integral_identity`, `kernel_row_support`). It is at line 116 of [KernelRegularity.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/KernelRegularity.lean#L116), with `kerCore_of` at line 52; the proposition is defined in [CalcSteps.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ArchimedeanGelfandKernels/FriedrichsKernels/CalcSteps.lean#L37). The second theorem proves a proposition of the form "hypotheses imply the algebra of multipliers", with the facts `bump_convolution_support`, `cosh_transform_convolution`, `wave_kernel_convolution`, `wave_kernel_word_order_swap`, `kernel_multiplier_linear`, `wave_kernel_decomposition`, `cosh_transform_casimir_real` and `kernel_multiplier_on_eigenfunction`; see [AsmMultMain.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AsmMultMain.lean#L25). The eigenvalues $\gamma_m$ of the Gelfand elements are defined in a file about abelian varieties, `AbelianVarietyTheory/Definitions/SemilocalFrames/PosPartUnitaryMul.lean`.
