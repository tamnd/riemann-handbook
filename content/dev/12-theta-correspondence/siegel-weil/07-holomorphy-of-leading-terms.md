---
title: Holomorphy of leading terms below the middle
decls:
  - PositivityTheory.Rg.Sw.HSt.holLeadB
  - PositivityTheory.Rg.Sw.HSt.asmH
  - PositivityTheory.Rg.Sw.HSt.locTau
  - PositivityTheory.Rg.Sw.HSt.crux
  - PositivityTheory.Rg.Sw.HSt.crLem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Holomorphy of leading terms below the middle

This section treats a Siegel Eisenstein series on $U(n,n)$ whose section has, at a real place, the holomorphic type $(m, 0)$ or $(0, m)$ with $1 \le m < n$. It proves that the first nonvanishing derivative in $z$ at $s_0$ is, as a function on the real group, a holomorphic (or antiholomorphic) function of the Siegel variable, as soon as its integrals against singular test functions vanish. The tools are the Cauchy-Riemann equations on $U(n,n)(\mathbb{R})$ and a local identity that writes the lowering operator as a combination of test operators. The result is used in the case $m < n$ of the Siegel-Weil formula, in [EveryCharacter](/step/every-character/) and in Step 5 of [the Siegel-Weil chapter of the proof](/proof/siegel-weil/).

We keep the real group $G_n(\mathbb{R}) = \{ y \in \mathrm{GL}_{2n}(\mathbb{C}) : y^H J_n y = J_n \}$ of [the previous section](/entry/gaussian-law-of-weil/), with $y = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ in blocks. Put
$$u_1(y) = iC + D, \qquad u_2(y) = -iC + D.$$
For integers $p, q \ge 0$ and $e$, put $f_{p,q}(y) = \det u_1(y)^{-p} \det u_2(y)^{-q}$ and $F_{p,q,e}(y) = \det(y)^e f_{p,q}(y)$. Put $h(y) = |\det u_1(y)|^{-2}$; this is the local height. The Siegel point of $y$ is $Z(y) = (iA + B) \, u_1(y)^{-1}$, so $Z(y) = y \cdot i$ in the notation of the previous section.

**Definition 4.7.1 (Holomorphic type).** A function $\varphi$ on $G_n(\mathbb{R})$ is of holomorphic type $(p, q, e)$ if there is a function $\Phi$, holomorphic on the Siegel set $\{ Z : -\tfrac i2 (Z - Z^H) > 0 \}$, such that
$$\varphi(y) = F_{p,q,e}(y) \, \Phi\bigl(Z^\ast(y)\bigr),$$
where $Z^\ast(y) = Z(y)$ if $q = 0$ and $Z^\ast(y) = -Z(y)^H$ if $q > 0$.

So a function of type $(m, 0, e)$ is a holomorphic function of the Siegel point times the factor of weight $m$, as for a holomorphic Siegel modular form.

**Definition 4.7.2 (Singular test function).** For a real $n \times n$ matrix $x$ let $\operatorname{herm}(x) = \tfrac12(x + {}^t x) + \tfrac i2 (x - {}^t x)$, a Hermitian matrix. A function $\psi$ on real $n \times n$ matrices is a singular test function if it is continuous with compact support and
$$\int \psi(x) \exp\bigl(2 \pi i \operatorname{tr}(\beta \operatorname{herm}(x))\bigr) \, dx = 0$$
for all Hermitian $\beta$ with $\det \beta = 0$.

A singular test function sees only the nondegenerate Fourier coefficients. If $\int F(g \, n(\operatorname{herm} x)) \psi(x) \, dx = 0$ for all singular tests, then the degenerate coefficients of $F$ carry all of $F$ along $N$.

**Theorem 4.7.3 (Holomorphy of leading terms).** Let $1 \le m < n$, let $(p, q)$ be $(m, 0)$ or $(0, m)$, and let $e$ be an integer. Let $G$ be a locally compact, Hausdorff, second countable group with subgroups $P$ and $\Gamma$, let $\iota : G_n(\mathbb{R}) \to G$ be a continuous homomorphism, and let $s_0 \in \mathbb{C}$. Let $H : G \to [0, \infty)$ and $f : G \to \mathbb{C}$ split locally: for each $g$ there are $x \in G$, $y \in G_n(\mathbb{R})$, $S \in \mathbb{C}$ and $r > 0$ with $g = x \iota(y)$ and, for all $y'$,
$$H(x \iota y') = r \, h(y'), \qquad f(x \iota y') = S \, F_{p,q,e}(y').$$
Let $U$ be an open right domain containing $s_0$, $d$ a polynomial, and $\hat E(z, g)$ a function holomorphic in $z \in U$, jointly continuous on $U \times G$, and such that for $\operatorname{Re} z > t$ the series $\sum_{\gamma \in P \backslash \Gamma} H(\gamma g)^{z - s_0} f(\gamma g)$ has a summable majorant on each compact set and
$$\hat E(z, g) = d(z) \sum_{\gamma \in P \backslash \Gamma} H(\gamma g)^{z - s_0} f(\gamma g).$$
Let $j \ge 0$. Assume that $\partial_z^i \hat E(s_0, g) = 0$ for all $i < j$ and all $g$, and that
$$\int \partial_z^j \hat E\bigl(s_0, g \, \iota(a \, n(\operatorname{herm} x) \, b)\bigr) \psi(x) \, dx = 0$$
for every singular test $\psi$ and all $g$, $a$, $b$. Then for each $g$ the function $y \mapsto \partial_z^j \hat E(s_0, g \iota(y))$ is of holomorphic type $(p, q, e)$.

Lean: `PositivityTheory.Rg.Sw.HSt.holLeadB`.

*Proof.* The case $(0, m)$ follows from the case $(m, 0)$ by complex conjugation of the Siegel variable, which exchanges $u_1$ and $u_2$; this is the conjugation step. The case $(m, 0)$ is [the holomorphic case](/entry/asm-h/), applied with [the local identity](/entry/loc-tau/), the formula for the local sections below, and [the Cauchy-Riemann lemma](/entry/cr-lem/). $\square$

We now state the inputs. Let $f_z(y) = \det(y)^e \det u_1(y)^{-m} (\det u_1(y) \det \bar u_1(y))^{-z}$ be the local section of weight $m$ at the parameter $z$, defined on all $2n \times 2n$ matrices. On the group it satisfies
$$f_w(y) = F_{m,0,e}(y) \, h(y)^w,$$
which is a direct computation since $\det u_1 \det \bar u_1 = |\det u_1|^2$ on $G_n(\mathbb{R})$.

For a $2n \times 2n$ matrix $Y$ in the complexified Lie algebra, let $R_Y$ be the right derivative $R_Y F(x) = \partial_t F(x e^{t Y_1})|_0 + i \, \partial_t F(x e^{t Y_2})|_0$, where $Y = Y_1 + i Y_2$ with $Y_1, Y_2$ in the real Lie algebra. For an $n \times n$ matrix $Q$, the lowering element is $Y_Q = \begin{pmatrix} 1 & Q \\ 0 & 1 \end{pmatrix} - 1$ in the Cayley coordinates.

**Lemma 4.7.4 (Cauchy-Riemann lemma).** Let $\varphi$ be a function on $G_n(\mathbb{R})$ and $\Phi$ a smooth function on an open set $\Omega$ of $2n \times 2n$ matrices that contains the group, with $\Phi = \varphi$ on the group. Assume $\varphi(y k) = \varphi(y) F_{m,0,e}(k)$ for $k$ in the maximal compact subgroup, and $R_{Y_Q} \Phi(y) = 0$ for all $y$ in the group and all $Q$. Then $\varphi$ is of holomorphic type $(m, 0, e)$.

Lean: `PositivityTheory.Rg.Sw.HSt.crLem`.

*Proof.* The right equivariance under the compact subgroup shows that $\varphi(y) = F_{m,0,e}(y) \Phi_0(Z(y))$ for a function $\Phi_0$ on the Siegel set, since the fibres of $y \mapsto Z(y)$ are the cosets of the compact subgroup. The local section gives the factor $F_{m,0,e}$. The lowering derivatives $R_{Y_Q}$ correspond, through this factorisation, to the derivatives $\partial / \partial \bar Z_{ij}$ of $\Phi_0$. So $R_{Y_Q} \Phi = 0$ for all $Q$ is the Cauchy-Riemann system for $\Phi_0$, and $\Phi_0$ is holomorphic. $\square$

The local identity is a statement about any compact group that parametrises the maximal compact subgroup $K$. For a compact group $K_g$ with Haar measure $\mu$ and a continuous homomorphism $\iota$ onto $K$, a continuous function $\rho$ on $K_g$, a singular test $\psi$ and two group elements $a, b$, the test operator is
$$T F(x) = \int_{K_g} \rho(k) \int F\bigl(x \, \iota(k) \, a \, n(\operatorname{herm} t) \, b\bigr) \psi(t) \, dt \, d\mu(k).$$

**Lemma 4.7.5 (Nonvanishing of a test operator).** Let $m < n$. For every compact group $K_g$ with Haar measure and continuous homomorphism $\iota$ onto $K$, there are $P$, a singular test $\psi$ and group elements $a, b, x$ such that, with $\rho_P$ the matrix coefficient attached to $P$,
$$\frac{d}{dz} \Bigl( T_{\rho_P, \psi, a, b} f_z(x) \Bigr)\Big|_{z = 0} \ne 0.$$

Lean: `PositivityTheory.Rg.Sw.HSt.crux`.

*Proof.* The value at $z = 0$ vanishes, since $f_0$ is a holomorphic vacuum vector and its degenerate coefficients are killed by singular tests. The derivative at 0 is a vacuum coefficient of $\partial_z f_z$, which is $\log(h)$ times $f_0$. One reduces the claim to the nonvanishing of this vacuum coefficient, using the properties of the finite dimensional representations of $K$ involved, a disjointness of their supports, a splitting of $K$, the spherical function of the unitary group and the holomorphy of $z \mapsto f_z$. $\square$

**Theorem 4.7.6 (Local identity).** Let $m < n$, let $K_g$, $\mu$ and $\iota$ be as above, and let $Q$ be an $n \times n$ matrix. There are $N$, continuous functions $\rho_l$, singular tests $\psi_l$, group elements $a_l, b_l$ ($l = 1, \dots, N$), an entire function $D$ with $D(0) \ne 0$, and entire functions $M_l$, such that for all $z$ and all $x$ in the group
$$D(z) \, R_{Y_Q} f_z(x) = \sum_{l=1}^N M_l(z) \, T_{\rho_l, \psi_l, a_l, b_l} f_z(x).$$

Lean: `PositivityTheory.Rg.Sw.HSt.locTau`.

*Proof.* Three facts and the lemma combine. First, the lowering derivative of the section is $R_{Y_Q} f_z = z \, e_Q(z)$, where $e_Q(z)$ is an explicit vector of $K$-type $\bar Q$. Second, by multiplicity one, each test operator with the coefficient $\rho_P$ maps $f_z$ to $e(c(z) P^H)$ for an entire function $c$. Third, singular tests kill the vacuum: $T f_0 = 0$, so $c(0) = 0$. By [the nonvanishing lemma](/entry/crux/), $c'(0) \ne 0$ for some choice. So $c(z) = z \, c_1(z)$ with $c_1(0) \ne 0$, and the lowering derivative is a combination of test operators with $D = c_1$. $\square$

**Theorem 4.7.7 (Holomorphic case).** Assume the local identity, the formula $f_w = F_{m,0,e} \, h^w$ on the group, and the Cauchy-Riemann lemma. Then the theorem on holomorphy of leading terms holds for $(p, q) = (m, 0)$.

Lean: `PositivityTheory.Rg.Sw.HSt.asmH`.

*Proof.* Fix $g$ and write $g = x \iota(y)$. For $\operatorname{Re} z$ large the series is a sum of translates of $r^{z - s_0} S f_{z - s_0}$, by the local splitting and the formula for the local section. The local identity applies to each term, so $D(z - s_0) R_{Y_Q} \hat E$ is a combination of test operators applied to $\hat E$ with entire coefficients, first for large $\operatorname{Re} z$ and then on all of $U$ by analytic continuation, since $U$ is connected to the right half-plane. The smoothness of $\hat E$ in $g$ along the group follows from the majorant and the joint continuity. Take $\partial_z^j$ at $s_0$. The lower derivatives vanish, so only the term with $D(0) \ne 0$ remains on the left, and the right side is a combination of singular test integrals of $\partial_z^j \hat E$, which vanish by hypothesis. So $R_{Y_Q} \partial_z^j \hat E(s_0, g \iota(\cdot)) = 0$. The right equivariance under $K$ holds term by term. The Cauchy-Riemann lemma gives the holomorphic type. $\square$

**Remark 4.7.8 (Formalization).** The nonvanishing lemma and the local identity quantify over every compact group with a continuous homomorphism onto $K$, not only over $K$ itself ([MultiplicityOneTestOperatorsAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/MultiplicityOneTestOperatorsAlt.lean#L39)). The local identity is assembled from three named facts and the nonvanishing lemma, and the assembly step and two of the facts have duplicate declarations in a second file ([DetSecondCayleyBlockNe.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/DetSecondCayleyBlockNe.lean#L154), and line 215). The proofs of the nonvanishing lemma and of the Cauchy-Riemann lemma are sketched from the names of the cited results; we have not unfolded those results.
