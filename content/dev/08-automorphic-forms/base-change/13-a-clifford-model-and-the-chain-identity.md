---
title: A Clifford model and the chain identity
decls:
  - PositivityTheory.RgBcC.cxData_model
  - PositivityTheory.RgBcC.LfSt.ChainPf.chain_identity_multiplier_kernels
  - PositivityTheory.RgBcC.LfSt.chainOf'_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Clifford model and the chain identity

The Lefschetz functions of Section 07 have twisted orbital integrals equal to a character value at every elliptic element. They are built from the multipliers of [Section 7.2.7](/entry/wave-existence-speed-multiplicity/) on a special bundle over $G = \mathrm{GL}_n(\mathbb{C})$: the fibre is an exterior algebra on the Hermitian matrices tensored with two copies of a representation of highest weight $\lambda$. The character value then comes out of a homotopy argument with a Dirac-type operator. This section gives the two algebraic inputs of that argument. First, we construct the bundle with all the operators that the argument needs; this is a Clifford datum. Second, we prove the chain identity: the kernel of a multiplier intertwines the Dirac operator on the left with the Dirac operator on the right, and it commutes with the grading. The homotopy argument itself, which turns these facts into the value of the orbital integrals, is taken from the companion development.

We keep the notation of Section 02: $G = \mathrm{GL}_n(\mathbb{C})$, $K = U(n)$, $\ell$ is the length, $R_X$ is the right derivative, and for a unitary representation $(V, \tau)$ of $K$ (written $E$ in Section 02) the space $C_V$ consists of the smooth $f : G \to V$ with $f(gk) = \tau(k)^{-1}f(g)$. For a smooth $k : G \to \mathrm{End}(V)$ and $X \in M_n(\mathbb{C})$ put
$$L_Xk(y) = \frac{d}{dt}k(e^{-tX}y)\Big|_{t=0},$$
the left derivative. Let $\mathfrak{p}$ be the real vector space of Hermitian $n \times n$ matrices, with the inner product $\langle H, H'\rangle = \mathrm{tr}(HH')$, and fix an orthonormal basis $h_1, \dots, h_{n^2}$ of $\mathfrak{p}$. For a smooth $F : G \to \mathrm{End}(V)$ write $dF(X)$ for the derivative of $F$ at $1$ in the direction $X$. For a non-increasing $\lambda \in \mathbb{Z}^n$ let $\chi_\lambda$ be the parameter of the representation of highest weight $\lambda$, and for $z \in (\mathbb{C}^\times)^n$ let $\mathrm{ch}_\lambda(z)$ be its Weyl character at $\mathrm{diag}(z)$.

**Definition 7.13.1 (Clifford datum).** Let $\lambda \in \mathbb{Z}^n$ be non-increasing. A Clifford datum for $\lambda$ consists of a unitary representation $(V, \tau)$ of $K$, a smooth map $F : M_n(\mathbb{C}) \to \mathrm{End}(V)$ on $G$, real linear maps $\varepsilon, \iota : M_n(\mathbb{C}) \to \mathrm{End}(V)$, a smooth family $S(s)$, $s \in \mathbb{R}$, of operators, and operators $\Gamma$ and $T$ on $V$, with the following properties.

1. (Frame.) $F$ is a homomorphism on $G$ with $F(1) = 1$, and $F(k) = \tau(k)$ for $k \in K$.
2. (Clifford relations.) For Hermitian $H$, $H'$: $\varepsilon(H)\iota(H') + \iota(H')\varepsilon(H) = \mathrm{tr}(HH')$; for $x \in G$: $F(x)\iota(H) = \iota(xHx^*)F(x)$ and $\varepsilon(H)F(x) = F(x)\varepsilon(x^*Hx)$.
3. (Grading.) $\Gamma^2 = 1$; $\Gamma$ anticommutes with every $\varepsilon(H)$ and $\iota(H)$ and commutes with every $F(x)$, with $T$ and with every $S(s)$.
4. (Twist.) $T^2 = 1$; $T$ is an isometry; $T$ commutes with $\tau(K)$, with every $\varepsilon(H)$ and $\iota(H)$, and with $S(0)$; and $T$ anticommutes with $D_F = \sum_p\varepsilon(h_p)\,dF(h_p)$.
5. (Scaling.) $S(1) = 1$; $S(s)\varepsilon(H) = s\,\varepsilon(H)S(s)$; $S'(s) = \sum_p\varepsilon(h_p)S(s)\iota(h_p)$; $S(0)$ is an idempotent with $\Gamma S(0) = S(0)$, and it commutes with every $F(x)$; and $TF((x^*)^{-1})S(0) = F(x)TS(0)$ for $x \in G$.
6. (Eigenfunctions.) For every $v \in V$, the function $x \mapsto F(x^{-1})S(0)v$ is an eigenfunction with parameter $\chi_\lambda$.
7. (Character.) For $z \in \mathbb{C}^n$ with $|z_a| = 1$ for all $a$ and the $z_a^2$ distinct,
$$\mathrm{tr}_V\big(S(0)F(\mathrm{diag}(z))T\big) = \overline{\mathrm{ch}_\lambda(z_1^2, \dots, z_n^2)}.$$

Here $\varepsilon$ and $\iota$ play the parts of exterior and interior multiplication by a cotangent vector of the symmetric space $G/K$, whose tangent space at the base point is $\mathfrak{p}$; $\Gamma$ is the parity of the exterior degree; $S(s)$ multiplies forms of degree $p$ by $s^p$, so that $S(0)$ is the projection onto degree $0$; and $T$ is the twist that realizes the involution $x \mapsto (x^*)^{-1}$, by property 5. The Dirac operator of the datum acts on $C_V$ by
$$Df(x) = \sum_p\varepsilon(h_p)\big(R_{h_p}f(x) + dF(h_p)f(x)\big).$$

We now build a Clifford datum for every $\lambda$. Let $c : \mathfrak{p} \to \mathbb{C}^{n^2}$ be the coordinate map, $c(H)_p = \mathrm{Re}\,\mathrm{tr}(Hh_p)$, extended to $M_n(\mathbb{C})$ by the same formula. For $y \in G$ let $M(y)$ be the matrix of $H \mapsto yHy^*$ in these coordinates. Let $\Lambda = \Lambda^\bullet(\mathbb{C}^{n^2})$ be the exterior algebra, and for $w \in \mathbb{C}^{n^2}$ let $e(w)$ be left multiplication by $w$ and $i(w)$ the contraction with the linear form $v \mapsto \sum_pw_pv_p$. For a matrix $g$ let $\Lambda(g)$ be the induced algebra map of $\Lambda$. Let $\rho_\lambda$ be the representation of $\mathrm{GL}_n(\mathbb{C})$ of highest weight $\lambda$ on a space $W$, with a fixed basis, and put $V = \Lambda \otimes W \otimes W$ with the standard inner product of the product basis. Define
$$F_0(x) = \Lambda\big(M(x^{-1})^{\mathsf{T}}\big) \otimes \big(\rho_\lambda(x)^{-1}\big)^{\mathsf{T}} \otimes \rho_\lambda(x^*)^{\mathsf{T}},$$
let $Q = \int_KF_0(k)^*F_0(k)\,dk$ for the Haar probability measure, and let $A \mapsto A^\natural = Q^{1/2}AQ^{-1/2}$. The model is
$$\begin{aligned}F(x) &= F_0(x)^\natural, & \varepsilon(H) &= (e(c(H)) \otimes 1)^\natural, & \iota(H) &= (i(c(H)) \otimes 1)^\natural,\\ S(s) &= (\Lambda(s) \otimes 1)^\natural, & \Gamma &= (\Lambda(-1) \otimes 1)^\natural, & T &= (1 \otimes \mathrm{sw})^\natural,\end{aligned}$$
where $\mathrm{sw}$ exchanges the two factors $W$, and $\tau$ is the restriction of $F$ to $K$.

**Theorem 7.13.2 (Clifford model).** For every non-increasing $\lambda \in \mathbb{Z}^n$, the data $(V, \tau, F, \varepsilon, \iota, S, \Gamma, T)$ above form a Clifford datum for $\lambda$.

Lean: `PositivityTheory.RgBcC.cxData_model`.

*Proof.* Conjugation by $Q^{1/2}$ is an algebra automorphism of $\mathrm{End}(V)$, so every algebraic relation may be checked for the unconjugated operators. The averaged operator $Q$ is positive and invertible and satisfies $F_0(k)^*QF_0(k) = Q$ for $k \in K$, so $F$ is unitary on $K$; this makes $\tau$ a unitary representation. Since $M(xy) = M(x)M(y)$, the map $F_0$ is a homomorphism. The relation $e(w)i(w') + i(w')e(w) = \sum_pw_pw'_p$ holds in any exterior algebra, and $\sum_pc(H)_pc(H')_p = \mathrm{tr}(HH')$ because the $h_p$ are orthonormal; this gives the Clifford relation. The covariance of $\varepsilon$ and $\iota$ under $F$ is the naturality of multiplication and contraction under $\Lambda(g)$, with $g = M(x^{-1})^{\mathsf{T}}$. The map $\Lambda(-1)$ is $(-1)^{\deg}$, which anticommutes with $e$ and $i$ and commutes with every $\Lambda(g)$; the map $\Lambda(s)$ is $s^{\deg}$, which gives $S(s)e(w) = s\,e(w)S(s)$, $S(1) = 1$, $S(0)$ the projection on degree $0$, and
$$\frac{d}{ds}s^{\deg} = \deg\cdot s^{\deg - 1} = \sum_pe(h_p)\,s^{\deg}\,i(h_p),$$
since $\sum_pe(h_p)i(h_p)$ is the degree operator. The swap commutes with the first factor. On $W \otimes W$, the derivative of $F_0$ at $1$ in a Hermitian direction $X$ is $-d\rho_\lambda(X)^{\mathsf{T}} \otimes 1 + 1 \otimes d\rho_\lambda(X)^{\mathsf{T}}$, which the swap carries to its negative; together with the computation of the derivative on the exterior factor, this gives the anticommutation of $T$ with $D_F$. On degree $0$ the operator $F_0(x)$ is $(\rho_\lambda(x)^{-1})^{\mathsf{T}} \otimes \rho_\lambda(x^*)^{\mathsf{T}}$, and the swap exchanges $x$ with $(x^*)^{-1}$, which is property 5. The function $x \mapsto F(x^{-1})S(0)v$ has matrix coefficients of $\rho_\lambda$ and of its complex conjugate as entries, which are eigenfunctions with parameter $\chi_\lambda$. For the character, the conjugation does not change the trace, and $\mathrm{tr}((A \otimes B)\circ\mathrm{sw}) = \mathrm{tr}(AB)$ on $W \otimes W$. With $x = \mathrm{diag}(z)$ and $|z_a| = 1$ we have $x^* = x^{-1}$, so
$$\mathrm{tr}_V\big(S(0)F(x)T\big) = \mathrm{tr}\big(\rho_\lambda(\bar z)^{\mathsf{T}}\rho_\lambda(\bar z)^{\mathsf{T}}\big) = \mathrm{ch}_\lambda(\bar z_1^2, \dots, \bar z_n^2) = \overline{\mathrm{ch}_\lambda(z_1^2, \dots, z_n^2)}.$$
The verifications of the remaining identities (the smoothness of $F$, the eigenfunction property, the isometry of $T$ and the derivative of $F$ on the exterior factor) are taken from the companion development. $\square$

The chain identity needs four analytic facts. Two are parts 1 and 2 of [the theorem on waves and kernels](/entry/wave-existence-speed-multiplicity/). The other two are the following, which we take as given.

**Theorem 7.13.3 (Gelfand operators and uniqueness of kernels).** Let $\mathcal{D}$ be one of the operators $\Gamma_m$ or $\bar\Gamma_m$ of Section 02, applied to smooth functions on $G$ with values in a normed space.

1. $\mathcal{D}$ preserves smoothness on $G$, commutes with every right derivative $R_X$, with left and right translations, and with every continuous linear map applied pointwise.
2. Let $\mu$ be a Haar measure, $(V, \tau)$ as above and $\kappa : G \to \mathrm{End}(V)$ continuous with $\kappa(yk) = \kappa(y)\tau(k)$ for $k \in K$. If $\int_G\kappa(y)f(y)\,d\mu(y) = 0$ for every $f \in C_V$ that vanishes where $\ell$ is large, then $\kappa = 0$.

Lean: `GlobalTheory.CompanionTheory.GelC.gelComm` (also `GlobalTheory.CompanionTheory.KerZeroPf.main`, part 2).

*Proof.* Both parts come from the companion development. $\square$

**Theorem 7.13.4 (Chain identity).** Assume that every section is the initial value of a wave, that waves have finite speed, and the two parts of the previous theorem. Let $\lambda$ be non-increasing, let $(V, \tau, F, \varepsilon, \iota, S, \Gamma, T)$ be a Clifford datum for $\lambda$, $\mu$ a Haar measure, and $k$ a multiplier of some radius with some value. Then for every $y \in G$
$$\Gamma k(y) = k(y)\Gamma$$
and
$$\sum_p\varepsilon(h_p)\big(L_{h_p}k(y) + dF(h_p)k(y)\big) = \sum_p\big(-R_{h_p}k(y)\,\varepsilon(h_p) + k(y)\,\varepsilon(h_p)\,dF(h_p)\big).$$

Lean: `PositivityTheory.RgBcC.LfSt.chainOf'_holds` (also `PositivityTheory.RgBcC.LfSt.ChainPf.chain_identity_multiplier_kernels`, the same result with the unimodularity of $G$, the calculus of right derivatives and the properties of $\ell$ as hypotheses).

*Proof.* Write $k = \sum_ic_ik_i$ with $k_i$ a kernel for $(w_i, g_i)$, and let $(k \star f)(x) = \int_Gk(y)f(xy)\,dy$. Then $k$ is smooth, vanishes where $\ell$ is large, and satisfies $k(yk_2) = k(y)\tau(k_2)$, since each $k_i$ does.

First the grading. By property 3, $\Gamma$ commutes with $F(K) = \tau(K)$, so $f \mapsto \Gamma f$ maps $C_V$ to itself and waves to waves. Let $f \in C_V$ and let $u$ be a wave with $u(0) = f$. The defining identity of a kernel, applied to the waves $u$ and $\Gamma u$, gives
$$k_i \star (\Gamma f) = w_i\Big(\int g_i(t)\,\Gamma u(t)\,dt\Big) = \Gamma\,(k_i \star f),$$
because $w_i$ and the integral commute with the fixed linear map $\Gamma$ (part 1 of the previous theorem). Summing, $k \star \Gamma f = \Gamma(k \star f)$. Evaluate at $x = 1$: the function $\kappa(y) = \Gamma k(y) - k(y)\Gamma$ satisfies $\int\kappa(y)f(y)\,dy = 0$ for all compactly supported $f \in C_V$. It is continuous and $\kappa(yk_2) = \kappa(y)\tau(k_2)$, because $\Gamma$ commutes with $\tau(k_2)$. By part 2, $\kappa = 0$.

Next the Dirac operator. The operator $D$ maps $C_V$ to itself, and maps waves to waves, since it commutes with $\Omega$ by part 1; it also commutes with every word $w_i$. Differentiation under the integral in $t$ is allowed for a bump $g_i$. Hence, as above, $k_i \star Df = D(k_i \star f)$ for each $i$, and so $k \star Df = D(k \star f)$. We compute both sides at $x = 1$. Since right derivatives of $k \star f$ move onto $k$ as left derivatives,
$$D(k \star f)(1) = \sum_p\varepsilon(h_p)\Big(\int L_{h_p}k(y)f(y)\,dy + dF(h_p)\int k(y)f(y)\,dy\Big) = \int\kappa_L(y)f(y)\,dy,$$
where $\kappa_L$ is the left side of the claimed identity. On the other side, integration by parts on the unimodular group $G$ gives $\int k(y)\varepsilon(h_p)R_{h_p}f(y)\,dy = -\int R_{h_p}k(y)\,\varepsilon(h_p)f(y)\,dy$, so
$$(k \star Df)(1) = \int\kappa_R(y)f(y)\,dy,$$
where $\kappa_R$ is the right side. The difference $\kappa_L - \kappa_R$ is continuous and right $K$-equivariant, and it integrates to $0$ against every compactly supported $f \in C_V$. By part 2, $\kappa_L = \kappa_R$. $\square$

**Remark 7.13.5 (Formalization).** A Clifford datum is `PositivityTheory.RgBcC.CxData` (LeftEquivariantFunctions/SymZeroCommFrame.lean:16), the chain identity is `Chain` (line 101), and the uniqueness of kernels is `KerZero` (line 83). `ChainOf'` (ChainOf.lean:5) is the implication from `WaveEx`, `WaveSpeed`, `GelComm` and `KerZero` to `Chain`, so `chainOf'_holds` is still conditional on these four inputs; it is used in this form in LefTop.lean:24, where they are supplied. Its proof `chainOf'_of` (GLMatrixDerivatives/ChainOfDone.lean:18) never uses `WaveSpeed`: the binder is `_hWS`. The model is in ComplexMatrixCalculus/InstBorelUK.lean (lines 16 to 113) and LefRho.lean:12; $\rho_\lambda$ is `GlobalTheory.Branching.sqRep` on `nablaSq`, and we did not unfold these, nor the proofs of `cfPair`, `mtLaws`, `car`, `tdOf`, `eigOf` and the other inputs of `cxData_of`. The model takes $\lambda$ as an arbitrary function and replaces it by $0$ when it is not non-increasing (`dw`, line 51). The coordinate map uses the real part of $\mathrm{tr}(Hh_p)$ and the contraction uses a bilinear (not Hermitian) pairing. The existence form is `cxEx_model` (CxDataModel.lean). The word `Chain` here is unrelated to the chains of Section 12.
