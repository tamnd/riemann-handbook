---
title: The wave equation on GL_n(C)
decls:
  - PositivityTheory.RgBcC.Fc.asmKerOne
  - PositivityTheory.RgBcC.wave_existence_speed_multiplicity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The wave equation on $\mathrm{GL}_n(\mathbb{C})$

To isolate one archimedean representation in a trace formula one needs test functions on $\mathrm{GL}_n(\mathbb{C})$ with compact support whose spherical transforms are prescribed functions of the infinitesimal character. This section builds them from the wave equation of the Casimir operator. We prove that the wave equation has solutions, that it has finite propagation speed, and that the operators $\int g(t)\cos(t\sqrt{-\Omega})\,dt$ are given by kernels of compact support that act on eigenfunctions by explicit scalars. These kernels are the archimedean test functions of the trace identities below [the twisted trace on a K-type](/entry/core-g/), on the way to the step [EveryCharacter](/step/every-character/). The background is in [Lie groups and Lie algebras](/learn/analysis/#lie-groups-and-lie-algebras), [Haar measure](/learn/analysis/#haar-measure) and [Sobolev norms](/learn/analysis/#sobolev-norms).

Throughout, $G = \mathrm{GL}_n(\mathbb{C})$ and $K = U(n)$, and $dy$ is a Haar measure on $G$.

**Definition 7.2.1 (Length).** For $y \in G$ put
$$\ell(y) = \log\Big(1 + \sum_{a,b}\big(|y_{ab}|^2 + |(y^{-1})_{ab}|^2\big)\Big).$$

So $\ell$ is smooth, bi-invariant under $K$, satisfies $\ell(y^{-1}) = \ell(y)$ and $\ell(xy) \le \ell(x) + \ell(y)$, and its sublevel sets are compact. The ball $\{\ell \le R\}$ plays the role of a ball of radius $R$ in the Riemannian distance.

**Definition 7.2.2 (Right derivatives and the Casimir operator).** For $X \in M_n(\mathbb{C})$ and a smooth function $f$ on $G$ let $R_X f(g) = \frac{d}{dt} f(g e^{tX})|_{t=0}$. Let $e_{ab}$ be the matrix units and put
$$E_{ab} = \tfrac12\big(R_{e_{ab}} - iR_{ie_{ab}}\big), \qquad \bar E_{ab} = \tfrac12\big(R_{e_{ab}} + iR_{ie_{ab}}\big).$$
Let $\Gamma_m = \sum_a (E^m)_{aa}$ and $\bar\Gamma_m = \sum_a (\bar E^m)_{aa}$, with matrix powers as in [the previous section](/entry/core-g/), and put $\Omega = 2(\Gamma_2 + \bar\Gamma_2)$.

The operators $E_{ab}$ and $\bar E_{ab}$ are the holomorphic and antiholomorphic parts of the right derivatives. They realize the two factors of $\mathfrak{gl}_n \oplus \mathfrak{gl}_n$. The $\Gamma_m$ and $\bar\Gamma_m$ generate the algebra of bi-invariant differential operators, and $\Omega$ is the Casimir operator.

**Definition 7.2.3 (Sections).** Let $(E, \tau)$ be a finite-dimensional unitary continuous representation of $K$. Let $C_E$ be the space of smooth $f : G \to E$ with $f(gk) = \tau(k)^{-1}f(g)$ for $g \in G$ and $k \in K$.

**Definition 7.2.4 (Wave).** A wave with values in $E$ is a smooth function $u : \mathbb{R} \times G \to E$ such that $u(t, \cdot) \in C_E$ for every $t$, $\partial_t^2 u = \Omega u$, and $\partial_t u(0, \cdot) = 0$.

**Definition 7.2.5 (Kernel).** A function $g : \mathbb{R} \to \mathbb{R}$ is a bump of radius $T$ if it is smooth, even, and vanishes for $|t| > T$. Let $w$ be a finite word in the operators $\Gamma_m$ and $\bar\Gamma_m$, and let $g$ be a function on $\mathbb{R}$. A kernel for $(w, g)$ is a smooth $k : G \to \mathrm{End}(E)$ such that $k(y) = 0$ when $\ell(y)$ is large, $k(k_1 y k_2) = \tau(k_1)k(y)\tau(k_2)$ for $k_1, k_2 \in K$, and for every wave $u$ and every $x \in G$,
$$\int_G k(y)\,u(0, xy)\,dy = w\Big(\int_{\mathbb{R}} g(t)\,u(t, \cdot)\,dt\Big)(x).$$

Formally the right side is $w\,g^\wedge(\sqrt{\Omega})\,u(0, \cdot)$, where $g^\wedge(s) = \int g(t)\cosh(ts)\,dt$. So a kernel realizes a function of $\Omega$ as a convolution operator.

**Definition 7.2.6 (Multiplier).** A multiplier of radius $T$ with value $\mathrm{val}$ is a finite sum $k = \sum_i c_i k_i$, where each $k_i$ is a kernel for $(w_i, g_i)$ with $g_i$ a bump of radius $T$, and
$$\mathrm{val}(\chi) = \sum_i c_i\,w_i(\chi)\,\widehat{g_i}(\chi)$$
for each infinitesimal character $\chi$. Here $w_i(\chi)$ is the scalar by which the word $w_i$ acts on functions of infinitesimal character $\chi$, and $\widehat{g_i}(\chi) = \int g_i(t)\cosh\big(t\,c(\chi)^{1/2}\big)\,dt$, with $c(\chi)$ the value of $\Omega$.

A function $f \in C_E$ is an eigenfunction with parameter $\chi$ if $\Gamma_m f$ and $\bar\Gamma_m f$ are the scalars of $\chi^+$ and $\chi^-$ times $f$, for every $m$. A parameter $\chi$ is Hermitian if $\chi^-$ is a permutation of $-\bar\chi^+$. The convolution of two kernels is $(k * k')(x) = \int_G k(y)k'(y^{-1}x)\,dy$.

**Theorem 7.2.7 (Waves and kernels).** Let $n \ge 1$.

1. For every $E$ and every $f \in C_E$ there is a wave $u$ with $u(0, \cdot) = f$.
2. There is $c$, depending only on $n$, such that for every $E$, every wave $u$, every $t \in \mathbb{R}$ and $x \in G$: if $u(0, xy) = 0$ for all $y$ with $\ell(y) \le c(1 + |t|)$, then $u(t, x) = 0$.
3. There is $c$, depending only on $n$, such that for every Haar measure and every $E$: for every word $w$ and every bump $g$ there is a kernel for $(w, g)$; and every multiplier $k$ of radius $T \ge 0$ vanishes at each $y$ with $\ell(y) > c(1 + T)$.
4. Let $k, k'$ be multipliers of radii $T, T'$ with values $\mathrm{val}, \mathrm{val}'$. Then $k * k'$ is a multiplier of radius $T + T'$ with value $\mathrm{val}\cdot\mathrm{val}'$; $k * k' = k' * k$; the function $y \mapsto k(y^{-1})^*$ is a multiplier of radius $T$ whose value is $\overline{\mathrm{val}(\chi)}$ at each Hermitian $\chi$; and $\int_G k(y)f(xy)\,dy = \mathrm{val}(\chi)f(x)$ for each eigenfunction $f \in C_E$ with parameter $\chi$.

Lean: `PositivityTheory.RgBcC.wave_existence_speed_multiplicity`.

Part 2 is the analogue of the domain of dependence for the wave equation on a Riemannian manifold: a wave travels at bounded speed in the length $\ell$. Part 4 says that multipliers form a commutative $*$-algebra that acts on joint eigenfunctions through their values.

The proof rests on the following analytic facts about $G$, which we take as given from the companion development: the properties of $\ell$ listed above, together with a bound $|d\ell_x(x\,e_{ab})| \le C$; the left and right invariance and the inversion invariance of Haar measure; a local Sobolev inequality $\|f(x)\|^2 \le C\sum_{w \in S}\int_{\ell(y) \le r}\|R_w f(xy)\|^2\,dy$; the calculus of right derivatives (they commute with the $\Gamma_m$ and with translations, and integrate to $0$ on compactly supported functions); an algebra estimate that bounds a word in skew-adjoint operators by powers of $-\sum X_i^2$; and the uniqueness of kernels (a $K$-equivariant continuous kernel that kills all sections supported off an open $K$-stable set vanishes on that set).

**Proposition 7.2.8 (One kernel).** Assume the analytic facts above, except the uniqueness of kernels, and assume part 2 of the Theorem. Then for every Haar measure, every $E$, every word $w$ and every bump $g$ there is a kernel for $(w, g)$.

Lean: `PositivityTheory.RgBcC.Fc.asmKerOne`.

*Proof.* First, waves exist for compactly supported data. Then we build a kernel for the empty word. Consider $-\Omega$ on the Sobolev space of $E$-valued sections in $L^2(G)$. By the algebra estimate and the integration by parts formula it is symmetric and bounded below, so by the Friedrichs extension theorem it has a self-adjoint extension, and a functional calculus $h \mapsto h(-\Omega)$ for continuous $h$ vanishing at infinity. Put $h_g(y) = \chi_c(y)\int g(t)\cosh(t\sqrt{y})\,dt$, where $\chi_c(y) = \max(0, \min(1, c + 1 - y))$ is a cutoff. Since $g$ is a smooth bump, the Paley-Wiener estimate shows that $y^m h_g(y)$ is continuous and tends to $0$ at infinity for every $m$. So $h_g(-\Omega)$ maps $L^2$ sections to smooth sections, and the value at $1$ of the image is bounded by a constant times the $L^2$ norm. This gives a smooth kernel $k$, bi-equivariant under $K$, with $\int k(y)f(xy)\,dy = \int g(t)u(t, x)\,dt$ for every compactly supported $f \in C_E$ and every wave $u$ with $u(0, \cdot) = f$. Finite propagation speed bounds the support of $k$ in $\ell$.

Second, localization. Given any wave $u$, finite propagation speed lets us replace $u(0, \cdot)$ by a compactly supported section that agrees with it near $x$, without changing either side of the identity at $x$. So $k$ is a kernel for the empty word and $g$.

Third, words. From a kernel for the empty word and $g$ one obtains a kernel for $(w, g)$, for each word $w$, using the calculus of right derivatives and the invariance of Haar measure. $\square$

*Proof of the Theorem.* Part 2 is finite propagation speed for this wave equation. We take it as given from the companion development, where it is proved from the facts on $\ell$, on Haar measure and on right derivatives. Waves exist for compactly supported data, as in the first step of the proof of the Proposition. Existence for all data, part 1, is deduced from this and part 2, also in the companion development. The first half of part 3 is the Proposition. The bound on the support of multipliers in part 3, and the four statements of part 4, are deduced in the companion development from the analytic facts, parts 1 and 2, the Proposition and the uniqueness of kernels. The reason for the last statement of part 4 is this: if $f$ is an eigenfunction with parameter $\chi$, then $t \mapsto \cosh\big(t\,c(\chi)^{1/2}\big)f$ is a wave with initial value $f$, so a kernel for $(w, g)$ multiplies $f$ by $w(\chi)\widehat{g}(\chi)$. $\square$

**Remark 7.2.9 (Formalization).** The definitions are in IsMultZero.lean (waves, kernels, multipliers, lines 68 to 120) and WaveSt.lean (the analytic facts). The scalars $w(\chi)$ and $c(\chi)$ come from `GlobalTheory.Dec.gelfVal`, which we have not unfolded. The Theorem is in WaveFinal.lean; its proof passes the six analytic facts to `GlobalTheory.T` wrappers (`finite_propagation_speed_holds`, `wave_solution_existence`, `wave_kernel_existence`) and to `GlobalTheory.CompanionTheory.WaveMult.asmMult_main`, whose proofs we have not unfolded. So the proofs of parts 1, 2 and 4 above follow the structure of the inputs, not an unfolded argument. `asmKerOne` (FriedrichsKernels/AsmKerOne.lean:38) applies `asmKerOne_of_steps` to `asmCpt`, to a bundle `calcSteps` of fifteen inputs (Fourier coefficients, a cutoff bound, the Friedrichs extension, the Casimir formula, Sobolev facts) and to five more (`smooth_operator_facts`, `paley_wiener_decay`, `kernel_regularity`, `kernel_localization`, `kernel_weight_facts`); these are the three steps of the proof of the Proposition. The first half of part 3 (`KerEx`) repeats the statement `KerOne` word for word, and `wave_kernel_existence` takes `KerOne` as an input, so that half only passes it along. Only the input to the Proposition was opened in detail. The word "multiplicity" in the name refers to the algebra of multipliers.
