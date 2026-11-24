---
title: The top vector as a fibre integral
decls:
  - Formalism.FourierDecayAlt.P.pbi_sectionExists_proof
  - Formalism.FourierDecayAlt.P.SmoothExtensionClosedSet.local_smooth
  - Formalism.FourierDecayAlt.P.SmoothExtensionClosedSet.fibIntSmooth
  - Formalism.FourierDecayAlt.P.fibre_integral_smooth
  - Formalism.FourierDecayAlt.P.fibre_integral_cells
  - Formalism.FourierDecayAlt.P.phi_zero_hermitian_curvature
  - Formalism.FourierDecayAlt.P.PBH.pointStep
  - Formalism.FourierDecayAlt.P.slice_induction_level
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The top vector as a fibre integral

The [head formula](/entry/pb-head-top-of-mk-top/) expresses the top density of a normal form datum through the vector $V_p F(a)$ of a place at local points $a$ of size $r + 1$. For the density estimate we need this vector as a smooth function. This section writes $V_p F(a)$ as the twisted unipotent integral of a single smooth function $\Phi_0$ of compact support, evaluated at the monomial matrix of $a$. The function $\Phi_0$ is a fibre integral over the stabilizers of $z$ and $z'$, taken along a smooth section of the map $\gamma \mapsto \hat Z(\gamma)$. The section ends with the slice induction, which moves a local point down one level. The results are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

We use the notation of the section on the [top unipotent integral](/entry/top-unipotent-integral/): a place $p$ with base data $S$, points $z, z'$ with $T = T(z) > 0$ and $T' = T(z') > 0$, representations $\pi, \pi'$, the map $\gamma \mapsto \hat Z(\gamma)$, the base frame $(\nu', m_0)$, local points, and the monomial matrix $M(\sigma, d)$ of a local point.

### Compact coefficients

**Definition 1.12.1 (Compact coefficient).** A function $F$ on $G_V$ with values in $\operatorname{Hom}(W_q, W_p)$ is a *compact coefficient* if $F$ is smooth on $G_V$, there is $R$ with $\|g\| \le R$ on the support of $F$, and there is $\varepsilon > 0$ with $G_f(g) \ge \varepsilon$ on the support of $F$.

The last condition keeps the support away from the wall $G_f = 0$, where the orbital integral degenerates.

### The fibre integral

For an $(r + 1) \times (r + 1)$ matrix $M$ let $M'$ be its upper left $r \times r$ block, and put
$$g(M) = |\det M|^2 - T T' |\det M'|^2.$$
This is the function $\operatorname G$ of the [top unipotent integral](/entry/top-unipotent-integral/), written for any matrix: for a local point $h \cdot (1, \zeta)$ the monomial matrix has $g = |\det Z_h|^2(|\zeta|^2 - TT')$.

Let $N_0(z)$ and $N_0(z')$ be the unipotent stabilizers of $z$ and $z'$, with Haar measures $\mu_0$ and $\mu_0'$, and let $\mu_W$, $\mu_{W'}$ be the measures of the place. A point of the fibre is a quadruple $p = (p_{11}, p_{12}, p_{21}, p_{22})$ with $p_{11} \in U_W$, $p_{12} \in N_0(z)$, $p_{21} \in U_{W'}$ and $p_{22} \in N_0(z')$. For $\gamma \in G_V$ put
$$\operatorname{sgs}(p, \gamma) = p_{11}^{-1}\, p_{12}^{-1}\, \gamma\, p_{22}\, p_{21}, \qquad \beta(p, F, \gamma) = \pi(p_{11})\, F(\operatorname{sgs}(p, \gamma))\, \pi'(p_{21})^{-1}.$$

**Definition 1.12.2 (Fibre integral).** The *fibre integral* of $F$ at $\gamma$ is
$$\operatorname{fib}(\gamma) = \int \beta(p, F, \gamma)\; d\bigl((\mu_W \times \mu_0) \times (\mu_{W'} \times \mu_0')\bigr)(p).$$

**Definition 1.12.3 (Section).** A *section* is a map $s$ from the $(r + 1) \times (r + 1)$ matrices to $G_V$ that is smooth on $\{ g > 0 \}$ and such that for every $Z$ with $g(Z) > 0$: $s(Z) \in G_V$, $\hat Z(s(Z)) = Z$, and $s(Z)$ is a frame for $(\nu', m_0)$.

Given a section, put $\phi_0(Z) = \operatorname{fib}(s(Z))$ if $g(Z) > 0$ and $\phi_0(Z) = 0$ otherwise.

**Proposition 1.12.4 (Existence of a section).** For base frame data, a section exists.

Lean: `Formalism.FourierDecayAlt.P.pbi_sectionExists_proof`

*Proof.* We write down $s(Z)$ explicitly. On $\{g > 0\}$ the matrix $Z$ and the positive number $g(Z)$ determine the missing columns of an element of $G_V$: the columns are completed by the base frame vectors, and the coefficients are rational functions of the entries of $Z$, $\bar Z$ and $\sqrt{g(Z)}$. These are smooth on $\{g > 0\}$. A direct computation checks that $s(Z)$ preserves $H$, that $\hat Z(s(Z)) = Z$, and that $s(Z)$ is a frame for $(\nu', m_0)$. $\square$

**Lemma 1.12.5 (Local smoothness).** Let $s$ be a section, let $\mu_0$, $\mu_0'$ be Haar measures, and let $F$ vanish outside $\{\|g\| \le R\}$ for some $R$ and agree on $G_V$ with a smooth function on all matrices. Then $\phi_0$ is smooth at every $Z_0$ with $g(Z_0) > 0$.

Lean: `Formalism.FourierDecayAlt.P.SmoothExtensionClosedSet.local_smooth`

*Proof.* Choose a closed ball $\bar B$ around $Z_0$ inside $\{g > 0\}$. On $\bar B$ the map $s$ is smooth and $s(\bar B)$ is compact. The support of $F$ is bounded, so for $Z \in \bar B$ the integrand $\beta(p, F, s(Z))$ vanishes unless $p$ lies in a fixed compact set, by compactness of $s(\bar B)$ and of the support of $F$ in the variables that matter. Multiply the integrand by a cutoff $\varphi(p)$ that is $1$ on this compact set. Then $\phi_0$ on $\bar B$ is an integral of a smooth function of $(Z, p)$ with compact support in $p$, and differentiation under the integral sign gives smoothness at $Z_0$. $\square$

**Theorem 1.12.6 (Smoothness of the fibre integral).** Let the place have base frame data, let $\mu_0$, $\mu_0'$ be Haar measures on $N_0(z)$ and $N_0(z')$, let $s$ be a section and $F$ a compact coefficient. Then $\phi_0$ is smooth on all matrices.

Lean: `Formalism.FourierDecayAlt.P.SmoothExtensionClosedSet.fibIntSmooth` (also `Formalism.FourierDecayAlt.P.fibre_integral_smooth`, a second name).

*Proof.* Extend $F$ to a smooth function on all matrices. Let $Z_0$ be a matrix. If $g(Z_0) > 0$, use [local smoothness](/entry/local-smooth/). Otherwise let $\varepsilon > 0$ be the constant of the compact coefficient. Then $\phi_0$ vanishes on the open set $\{g < \varepsilon\}$, which contains $Z_0$. Where $g \le 0$ this is the definition. Where $0 < g(Z) < \varepsilon$, the points $\operatorname{sgs}(p, s(Z))$ lie outside the support of $F$, because $G_f \ge \varepsilon$ on that support; so the integrand is $0$. Hence $\phi_0$ is smooth near $Z_0$. $\square$

### The top vector

Let $\beta_U$ be the standard character of the [top unipotent integral](/entry/top-unipotent-integral/), and let $\Phi^{\mathrm{top}}_{\beta_U}(\sigma, d; \Phi)$ be the twisted unipotent integral of a function $\Phi$ of $(r+1) \times (r+1)$ matrices at the monomial matrix $M(\sigma, d)$.

**Theorem 1.12.7 (The top vector as a fibre integral).** There are Haar measures $\mu_0$, $\mu_0'$ on $N_0(z)$ and $N_0(z')$ and a constant $c \in \mathbb C$ with the following property. For every section $s$, every compact coefficient $F$, and every local point $a$ of size $r + 1$ whose point matrix is $M(\sigma, d)$,
$$V_p F(a) = \Phi^{\mathrm{top}}_{\beta_U}\bigl(\sigma, d;\; c\, \phi_0\bigr).$$

Lean: `Formalism.FourierDecayAlt.P.fibre_integral_cells`

*Proof.* Choose Haar measures on the stabilizers. The measure $\mu_N$ disintegrates along the fibration by the stabilizers $N_0(z)$ and $N_0(z')$, and this gives constants $c_1, c_2$ with $\mu_N = c_1 c_2 \cdot (\text{fibre measure}) \times (\text{measure on the quotient})$. Split the unipotent integral of the orbital integral accordingly: the integral over the fibre is $\operatorname{fib}(\gamma)$, and the integral over the quotient is the unipotent integral in the coordinates of the matrix $\hat Z(\gamma)$. In these coordinates the orbital integral at the frame $\gamma = s(M(\sigma, d))$ is the twisted integral $\Phi^{\mathrm{top}}_{\beta_U}$ of $\phi_0$. Put $c = c_1 c_2$. $\square$

**Theorem 1.12.8 (Smooth top vector).** Let $p$ be a place with base frame data and $F$ a compact coefficient. There is a smooth function $\Phi_0$ with compact support on the $(r+1) \times (r+1)$ matrices, with $\det \ne 0$ on its support, such that $V_p F(a) = \Phi^{\mathrm{top}}_{\beta_U}(\sigma, d; \Phi_0)$ for every local point $a$ of size $r + 1$ with point matrix $M(\sigma, d)$.

Lean: `Formalism.FourierDecayAlt.P.phi_zero_hermitian_curvature`

*Proof.* Take a [section](/entry/pbi-section-exists-proof/), the measures and the constant $c$ of the [top vector as a fibre integral](/entry/fibre-integral-cells/), and put $\Phi_0 = c\, \phi_0$. It is smooth by the [smoothness of the fibre integral](/entry/fib-int-smooth/). Its support is compact, since the support of $F$ is bounded and the fibre integral of a function with bounded support has bounded support in $Z$; and $g \ge \varepsilon$ on the support, by the argument in the proof of smoothness. On the support $g(Z) > 0$, so $|\det Z|^2 > TT'|\det Z'|^2 \ge 0$, and $\det Z \ne 0$. $\square$

### Slice induction

The vector at level $j + 1$ along a local point $h \cdot (1, c)$ reduces to the vector at level $j$ along $h$. The basic step is one variable.

**Lemma 1.12.9 (Point step).** Let $c \ne 0$ and let the integrands be integrable. Then the twisted unipotent integral with one block of size $s = 1$ at the $1 \times 1$ matrix $c$ equals
$$\int_{\mathrm{RC} \times \mathrm{RC}} \psi(z_A, R(y_1))\, \overline{\psi(z'_A, R(y_2))}\; \Phi_{s = 0}\bigl(R(y_1)^{-1}\, m(c, \gamma)\, R(y_2)\bigr)\, dy_1\, dy_2,$$
where $\Phi_{s=0}$ is the integral with no block, $R(y)$ is the radical element with coordinates $y$, $\psi$ is the character at the lower part of $z$ and $z'$, and $m(c, \gamma)$ is the block map.

Lean: `Formalism.FourierDecayAlt.P.PBH.pointStep`

*Proof.* The integral with one block runs over the radical coordinates, the unipotent coordinates of the block and the unipotent group of the rest. The unipotent measure splits into these factors, as in the [splitting of the unipotent measure](/entry/split-all/). A chain of measure preserving changes of variables, one for each factor, moves the block of size $1$ into the block map $m(c, \gamma)$; the block with $s = 1$ has no upper triangular coordinates, so only the radical coordinates remain. $\square$

**Theorem 1.12.10 (Slice induction).** Let $j + 1 \le r$, let $h$ be a local point of size $j$, let $c$ be such that $h \cdot (1, c)$ is a local point, let $F$ be a compact coefficient, and let $\gamma \in G_V(r - j - 1) \cap \Omega^+$. Then the coefficient $J_F$ at level $j + 1$ of the slice of $F$ along $h \cdot (1, c)$, at $\gamma$, equals the coefficient $J_F$ at level $j$ of the slice of $F$ along $h$, at $m(c, \gamma)$.

Lean: `Formalism.FourierDecayAlt.P.slice_induction_level`

*Proof.* The slice along $h \cdot (1, c)$ is the slice along $h$ followed by one more partial integral in the variable $c$. Apply the [point step](/entry/point-step/) to this last integral. $\square$

**Remark 1.12.11 (Formalization).** The smoothness theorem asks for base frame data, but its proof discards this hypothesis. The name of the smooth top vector says "hermitian curvature" only because of the folder of the file. We did not unfold the explicit section; its description above follows its statement. The point step is stated for one block of size $1$; the slice induction passes it through one more step that turns a point step into a step for the coefficients $J_F$.
