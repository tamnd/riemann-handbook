---
title: The top degree identity
decls:
  - Formalism.FourierDecayAlt.P.degree_top
  - Formalism.FourierDecayAlt.P.polynomial_top
  - Formalism.FourierDecayAlt.P.VandermondePolynomialIntegral.polyTop_of
  - Formalism.FourierDecayAlt.P.VandermondePolynomialIntegral.pt_poly
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The top degree identity

The bound at the infinite places compares the energy of a word with the energy of words that carry extra top letters. This section proves the identity behind that comparison. If one applies the top raising operator with parameter $y$ to a function $G$ and takes the local vector at a point $q$, the result is a polynomial in $y$ whose degree is fixed by $q$ and whose leading coefficient is an explicit multiple of the vector of $G$. Lagrange interpolation at a grid of values of $y$ then writes the vector of $G$ as a finite combination of vectors of words with top letters. The identity is the input "degree top" of [the built bounds](/entry/built-bounds-compact-of-leaves/). For the facts on polynomials and determinants that we use, see [polynomials](/learn/algebra/#polynomials-and-power-series) and [matrices](/learn/algebra/#matrices).

**Definition 3.9.1 (Local points).** A *local point* is a finite list $q = ((s_1, t_1), \dots, (s_m, t_m))$ of pairs of a positive integer and a nonzero complex number. Its *size* is $s_1 + \dots + s_m$, and $q$ is a local point of size $r + 1$ if its size is $r + 1$. We write $q = h \cdot (s, t)$ when the last pair of $q$ is $(s, t)$, and then $i_0 = \mathrm{size}(h)$ satisfies $i_0 + s = r + 1$.

**Definition 3.9.2 (Top raising operator).** Let real place data $(z, z', \pi, \pi')$ be given, and let $A(u)$ be the raising operator of Capelli type at the level $r$, a differential operator on the real group $G_V$ that depends polynomially on $u \in \mathbb{C}$. Let $D(g)$ be the last of the principal minors attached to $(z, z')$. For $y \in \mathbb{R}$ and a function $F$ on $G_V$ with values in $\mathrm{Hom}(W_q, W_p)$, the *top raising operator* is
$$A_{\mathrm{top}}(y) F(g) = D(g)^{-1}\, \Big(A\Big(y + \frac{2r + k}{2}\Big) F\Big)(g).$$

For a place $p$ above the real place data, with auxiliary data $(\nu', m_0)$, the *local vector* $V(G, q)$ of a function $G$ at a local point $q$ is defined as follows. If there is $\gamma \in G_V$ whose matrix $\widehat{Z}(\gamma)$ is the normal form matrix of $q$ and which is a frame for $(\nu', m_0)$, and the function $G_f(\gamma)$ of the point is positive, then
$$V(G, q) = \int_{U_W(z) \times N} \theta_L(x)\, \psi(x_2)\, \pi(x_1)\, K_r G\big(x_1^{-1} x_2^{-1} \gamma\big)\; d(\mu_W \times \mu_N)(x),$$
where $K_r$ is the kernel operator of the level $r$, $N$ is the unipotent radical, $\psi$ is a character of $N$ and $\theta_L$ is a weight. Otherwise $V(G, q) = 0$. We only use that $V$ is linear in $G$ and has this integral form.

A function $G$ has *compactly supported coefficients* if its coefficients are smooth and vanish outside a set of the form $\{g : \|g_N\| \leq R\}$.

**Lemma 3.9.3 (Integrals of polynomials).** Let $(X, \mu)$ be a measure space, $E$ a Banach space, $d \in \mathbb{N}$, and let $I : \mathbb{R} \times X \to E$ and $T : X \to E$ with $I(y, \cdot)$ integrable for each $y$. Assume that for almost every $x$ there are $c_0(x), \dots, c_d(x) \in E$ with $c_d(x) = T(x)$ and $I(y, x) = \sum_{n=0}^d y^n c_n(x)$ for all $y$. Then $T$ is integrable, and there are $c_0, \dots, c_d \in E$ with $c_d = \int T\, d\mu$ and
$$\int_X I(y, x)\, d\mu(x) = \sum_{n=0}^d y^n c_n \quad \text{for all } y \in \mathbb{R}.$$

*Proof.* Let $V = (m^n)_{0 \leq m, n \leq d}$ be the Vandermonde matrix of the points $0, 1, \dots, d$. It is invertible, since the points are distinct. For almost every $x$ the values $I(m, x) = \sum_n m^n c_n(x)$ determine the coefficients: $c_n(x) = \sum_m (V^{-1})_{nm}\, I(m, x)$. Define $C_n(x) = \sum_m (V^{-1})_{nm}\, I(m, x)$ for all $x$. Each $C_n$ is a finite combination of integrable functions, so it is integrable, and $C_n = c_n$ almost everywhere. In particular $T = C_d$ almost everywhere, so $T$ is integrable. Put $c_n = \int C_n\, d\mu$. For each $y$, $I(y, x) = \sum_n y^n C_n(x)$ for almost every $x$, and integration gives the claim, with $c_d = \int C_d\, d\mu = \int T\, d\mu$. $\square$

**Proposition 3.9.4 (Pointwise polynomial).** Assume that the kernel operator commutes with the raising operator: $K_r(A(u) F) = A(u)(K_r F)$ on $G_V$ for all $F$ with compactly supported coefficients and all $u \in \mathbb{C}$. Let $G$ have compactly supported coefficients, let $q = h \cdot (s, t)$ be a local point of size $r + 1$ with $s \geq 2$, and let $\gamma \in G_V$ with $\widehat{Z}(\gamma)$ the normal form matrix of $q$ and $G_f(\gamma) > 0$. Let $x_1 \in U_W(z)$, $x_2 \in N$, and put $\sigma = x_1^{-1} x_2^{-1}$. Then there are $c_0, \dots, c_{i_0}$ with
$$c_{i_0} = \frac{(-1)^{s-1}}{t}\, K_r G(\sigma\gamma), \qquad K_r\big(A_{\mathrm{top}}(y) G\big)(\sigma\gamma) = \sum_{n=0}^{i_0} y^n c_n$$
for all $y \in \mathbb{R}$.

Lean: `Formalism.FourierDecayAlt.P.VandermondePolynomialIntegral.pt_poly`.

*Proof.* Put $G_\sigma(g) = G(\sigma g)$. Left translation by $\sigma$ keeps compactly supported coefficients, since $x_1$ lies in a compact group and $x_2$ in $N$, and it keeps the minors: $D(\sigma g) = D(g)$. It commutes with $A(u)$, which is built from right derivatives. So it suffices to treat $\sigma = 1$, with $G_\sigma$ in place of $G$. By the commutation hypothesis, $K_r(A_{\mathrm{top}}(y) G)(\gamma) = D(\gamma)^{-1} A(u)(K_r G)(\gamma)$ with $u = y + (2r + k)/2$. The function $K = K_r G$ is smooth and is an eigenfunction of the unipotent derivatives $E_{pq}$ that enter $A(u)$, with eigenvalues given by the derivative of $\psi$. At the point $\gamma$, which is in normal form, $A(u) K(\gamma)$ is the determinant of a matrix with a corner block $h_h$ of size $i_0$, with $\det h_h \neq 0$, and $s$ further rows. Expanding the determinant, $A(u) K(\gamma)$ is a polynomial in $u$ of degree at most $i_0$, and its top coefficient is $(-1)^{s-1} t^{-1}$ times $D(\gamma) K(\gamma)$; the sign comes from moving the $s$ rows past the corner, and $t$ is the entry that links the corner to the rest. A shift $u = y + c$ keeps the degree and the top coefficient. Dividing by $D(\gamma)$ gives the claim. $\square$

**Theorem 3.9.5 (Polynomial top).** Let $p$ be a place above real place data, let $G$ have compactly supported coefficients, and let $q = h \cdot (s, t)$ be a local point of size $r + 1$ with $s \geq 2$. Then there are $c_0, \dots, c_{i_0} \in \mathrm{Hom}(W_q, W_p)$, where $i_0 = \mathrm{size}(h)$, with
$$c_{i_0} = \frac{(-1)^{s-1}}{t}\, V(G, q), \qquad V\big(A_{\mathrm{top}}(y) G, q\big) = \sum_{n=0}^{i_0} y^n c_n \quad \text{for all } y \in \mathbb{R}.$$

Lean: `Formalism.FourierDecayAlt.P.polynomial_top` (also `Formalism.FourierDecayAlt.P.VandermondePolynomialIntegral.polyTop_of`, the form with the commutation of $K_r$ and $A(u)$ as hypothesis).

*Proof.* The kernel operator commutes with the raising operator; this is a relation between raising and lowering operators, and it holds for functions with compactly supported coefficients. If there is no point $\gamma$ as in the definition of $V$, or if $G_f(\gamma) \leq 0$, then both vectors are $0$ and $c = 0$ works. Otherwise fix $\gamma$. The top raising operator keeps compactly supported coefficients, so $V(A_{\mathrm{top}}(y) G, q)$ is the integral over $U_W(z) \times N$ of
$$I(y, x) = \theta_L(x)\, \psi(x_2)\, \pi(x_1)\, K_r\big(A_{\mathrm{top}}(y) G\big)\big(x_1^{-1} x_2^{-1}\gamma\big),$$
and each $I(y, \cdot)$ is integrable. For almost every $x$, $x_1 \in U_W(z)$ and $x_2 \in N$, since the Haar measures are carried by these groups. For such $x$ the Proposition gives coefficients $c_n(x)$, and multiplying by the scalar $\theta_L(x)\psi(x_2)$ and applying the linear map $\pi(x_1) \circ (\cdot)$ keeps the polynomial form and the top coefficient. So $I(y, x)$ is a polynomial in $y$ of degree at most $i_0$ with top coefficient $T(x) = \frac{(-1)^{s-1}}{t}\theta_L(x)\psi(x_2)\pi(x_1) K_r G(x_1^{-1}x_2^{-1}\gamma)$. The Lemma on integrals of polynomials, with $d = i_0$, gives the claim, since $\int T = \frac{(-1)^{s-1}}{t} V(G, q)$. $\square$

For points $y_0, \dots, y_d$ that are pairwise distinct, put
$$\ell_j(y_0, \dots, y_d) = \prod_{i \neq j} (y_j - y_i)^{-1}.$$
If $P(y) = \sum_{n=0}^d c_n y^n$, then $c_d = \sum_{j=0}^d \ell_j\, P(y_j)$. Indeed, by Lagrange interpolation
$$P(y) = \sum_j P(y_j) \prod_{i \neq j} \frac{y - y_i}{y_j - y_i},$$
and the coefficient of $y^d$ on the right is $\sum_j \ell_j\, P(y_j)$.

**Theorem 3.9.6 (Degree top).** Let $p$ be a place with a family $\Theta$ of word operators that satisfies the standing bounds with constant $C_b$, let $F$ have compactly supported coefficients, let $w$ be a word, and let $q = h \cdot (s, t)$ be a local point of size $r + 1$ with $s \geq 2$. Let $K \in \mathbb{N}$, and for $a = 1, \dots, K$ let $y^a = (y^a_0, \dots, y^a_{i_0})$ be pairwise distinct reals such that the word $(y^1_{n_1}, \dots, y^K_{n_K}) \cdot w$ is a cut word for every choice of indices $n$. Then
$$\begin{aligned} \Big(\frac{(-1)^{s-1}}{t}\Big)^K V(\Theta_w F, q) = \sum_{n} \Big(\prod_{a=1}^K \ell_{n_a}(y^a)\Big)\, V\big(\Theta_{(y^1_{n_1}, \dots, y^K_{n_K}) \cdot w} F, q\big), \end{aligned}$$
where $n$ runs over all maps $\{1, \dots, K\} \to \{0, \dots, i_0\}$.

Lean: `Formalism.FourierDecayAlt.P.degree_top`.

*Proof.* We use induction on $K$. For $K = 0$ both sides are $V(\Theta_w F, q)$. The operator of a word with a top letter $y$ in front is the top raising operator: $\Theta_{(y) \cdot w'} F = A_{\mathrm{top}}(y)\, \Theta_{w'} F$, and $\Theta_{w'} F$ has compactly supported coefficients. Let $K \geq 1$, and put $w' = (y^2_{n_2}, \dots, y^K_{n_K}) \cdot w$ for a fixed choice of $n_2, \dots, n_K$. By the Theorem on the polynomial top, $y \mapsto V(A_{\mathrm{top}}(y) \Theta_{w'} F, q)$ is a polynomial of degree at most $i_0$ with top coefficient $\frac{(-1)^{s-1}}{t} V(\Theta_{w'} F, q)$. The interpolation formula at the points $y^1$ gives
$$\frac{(-1)^{s-1}}{t}\, V(\Theta_{w'} F, q) = \sum_{n_1} \ell_{n_1}(y^1)\, V\big(\Theta_{(y^1_{n_1}) \cdot w'} F, q\big).$$
Apply the induction hypothesis to the $K - 1$ grids $y^2, \dots, y^K$, multiply by $\frac{(-1)^{s-1}}{t}$, and replace each $\frac{(-1)^{s-1}}{t} V(\Theta_{w'} F, q)$ by the formula above. $\square$

In the application the grids lie in boxes of length larger than $2$, as in [Lemma E](/entry/lemma-e-closed/), so the numbers $\ell_j$ are bounded, and the identity bounds the vector of a word by the vectors of words with $K$ more top letters. These are the words whose energy the model controls.

**Remark 3.9.7 (Formalization).** `degree_top` ([DegreeTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/DegreeTop.lean#L6)) is `pb_degTop_of_polyTop polynomial_top`, and proves `KB.DegTop` ([RealInputsClosedAdmissibleSettings.lean](lean:Formalism/HermitianCurvature/RealInputsClosedAdmissibleSettings.lean#L280)); the numbers $\ell_j$ are `F7.lagCo` (LevelRecursionCondNeeded.lean, line 51). We did not read `pb_degTop_of_polyTop`, and our induction is our own. `polynomial_top` is in [RaisingLoweringRelations.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RaisingLoweringRelations.lean#L21), as `polyTop_of raising_lowering_relations`, where `raising_lowering_relations` (line 9) proves the commutation `KrAA` ([SmoothOnHOfLoc.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SmoothOnHOfLoc.lean#L13)); the file name describes the input, not the theorem. `PBN.PolyTop` is in [StatementHeads.lean](lean:Formalism/HermitianCurvature/StatementHeads.lean#L88), with `aaTop` at line 72. `polyTop_of` ([PolyTopOf.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/PolyTopOf.lean#L24)) follows the proof above, with the integral form of the local vector taken from `vecV_split` and the Lemma on integrals of polynomials being `poly_integral` (CoeffOfValues.lean, line 38), which uses the Vandermonde matrix of $0, \dots, d$ as we do. `pt_poly` (SmoothOnHOfLoc.lean, line 33) reduces to `top_poly` (CornerMatrixRightTranslate.lean, line 91), the determinant statement at a point in normal form; our account of the determinant expansion is a paraphrase of its hypotheses, since we did not read its proof. A second theorem named `pt_poly`, with a different statement, is in CutGCoreGTRTopActCut.lean (line 38), in another namespace.
