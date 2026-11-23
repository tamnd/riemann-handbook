---
title: Reduced sections and completeness of theta functions
decls:
  - GlobalTheory.CompanionTheory.RSecPf.rSec_of_htExist
  - GlobalTheory.T.regular_section_of_heights
  - PositivityTheory.Rg.Rsw.rSec
  - GlobalTheory.CompanionTheory.ThTot.thTotal
  - GlobalTheory.T.theta_total_of_hecke_eta
  - PositivityTheory.Rg.Rsw.thTotal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reduced sections and completeness of theta functions

The previous section wrote the Fourier-Jacobi coefficient of a Siegel Eisenstein series on $G_n$ as an Eisenstein series on $G_p$ of a reduced section $R(f, g, \Omega)$. This section proves two facts that make that identity useful. First, when $f$ runs through a holomorphic family of sections built from a height, the reduced sections form a holomorphic family of sections on $G_p$, in a half plane that is larger than the half plane of convergence. Second, the theta functions are complete: a bounded continuous function on $M_{\rho \times p}(\mathbb{A}_E)$ that is orthogonal to all $\Omega(1, \cdot)$ in the theta class is zero. The residue functional and the polar part identity use both facts, and through them they reach [Theorem 5.7.3](/entry/res-core/).

We keep the notation of the two previous sections. In particular $\rho + p = n$, $\psi$ is an additive character, $\vartheta$ is the fixed archimedean family, and $W$, $R$ and the theta class $\mathrm{Th}(\psi, \chi', b_0)$ are as defined there.

**Definition 5.3.1 (Height family).** Let $H$ be a height on $G_n$, $s_1 \in \mathbb{C}$ and $\varphi \colon G_n \to \mathbb{C}$. The *height family* of $\varphi$ is
$$f_z(g) = H(g)^{z - s_1}\, \varphi(g), \qquad z \in \mathbb{C},\ g \in G_n.$$

If $\varphi$ is a section of degree $s_1$ for $\chi$, then $f_z$ is a section of degree $z$ for $\chi$, since $H(qg)^{z - s_1} = |\det a_q|^{z - s_1} H(g)^{z - s_1}$. So the height family moves the degree of a fixed section, and $f_{s_1} = \varphi$. This is the usual way to put a section into a holomorphic family ([Siegel Eisenstein series](/learn/automorphic-forms/#eisenstein-series)).

**Theorem 5.3.2 (Reduced sections of height families).** Assume the conclusion of the existence of heights. Let $\psi$ be an additive character, $b_0 \in \mathrm{Herm}_\rho(E)$ with $\det b_0 \neq 0$, $\chi$ and $\chi'$ Hecke characters, and $\Omega \in \mathrm{Th}(\psi, \chi', b_0)$. Let $H$ be a height on $G_n$, $s_1 \in \mathbb{C}$, $\varphi$ a continuous section of degree $s_1$ for $\chi$, and $f_z$ its height family. Fix $g \in G_n$ and put $\Pi = \{ z \in \mathbb{C} : \operatorname{Re} z > (\rho - p)/2 \}$. Then:

1. the function $(z, h) \mapsto R(f_z, g, \Omega)(h)$ is continuous on $\Pi \times G_p$;
2. for each $h \in G_p$, the function $z \mapsto R(f_z, g, \Omega)(h)$ is holomorphic on $\Pi$;
3. for each $z \in \Pi$, the function $R(f_z, g, \Omega)$ is a section of degree $z$ for $\chi \chi'^{-1}$ on $G_p$.

Lean: `GlobalTheory.CompanionTheory.RSecPf.rSec_of_htExist` (also `GlobalTheory.T.regular_section_of_heights`, a second name).

*Proof.* We use the compact set $C_0$ with $G_n = P_n C_0$ from the existence of heights.

First, a bound on the family. The function $\varphi / H^{s_1 + n/2}$ is invariant under $P_n$ on the left in absolute value, so it is bounded by its maximum on $C_0$. Hence there is $B \ge 0$ with $|f_z(g)| \le B\, H(g)^{\operatorname{Re} z + n/2}$ for all $z$ and $g$.

Second, continuity and holomorphy. Fix $z_0 \in \Pi$ and $h_0 \in G_p$. There are a neighbourhood $V$ of $z_0$ and reals $\rho < \tau_1 \le \tau_2$ with $\tau_1 \le \operatorname{Re} z + n/2 \le \tau_2$ for $z \in V$; this is possible because $\operatorname{Re} z_0 + n/2 > \rho$ exactly when $z_0 \in \Pi$. Let $N$ be a compact neighbourhood of $h_0$. A height changes by a bounded factor under right translation by a compact set, so there is $\kappa \ge 1$ with $H(x c) \le \kappa H(x)$ for $c \in \iota(N) g$. The theta class gives a Schwartz function $\Phi$ with $|\Omega(h, y)| \le |\Phi(y)|$ for $h \in N$. For each $\tau \ge 0$ there is an integrable $W_\tau$ on $M_{\rho \times p}(\mathbb{A}_E)$ with $H(x\, \mathbf{s}(y))^\tau |\Phi(y)| \le W_\tau(y) H(x)^\tau$. For $\tau > \rho$ the function $\zeta \mapsto H(w\, \mathbf{n}(\zeta, 0))^\tau$ is integrable on $\mathrm{Herm}_\rho(\mathbb{A}_E)$. Since $|\psi_{b_0}| = 1$, these bounds give, for $z \in V$ and $h \in N$,
$$\begin{aligned} &\bigl|W(f_z)(\mathbf{s}(y)\, \iota(h)\, g)\bigr|\, |\Omega(h, y)| \\ &\quad \le B \kappa^{\tau_2} \bigl(W_{\tau_1}(y) + W_{\tau_2}(y)\bigr) \int \bigl(H(w\, \mathbf{n}(\zeta, 0))^{\tau_1} + H(w\, \mathbf{n}(\zeta, 0))^{\tau_2}\bigr)\, d\lambda(\zeta). \end{aligned}$$
Here we used $r^\tau \le r^{\tau_1} + r^{\tau_2}$ for $r > 0$ and $\tau_1 \le \tau \le \tau_2$. The right side is an integrable function of $y$ that does not depend on $z$ and $h$. The same argument, one level down, shows that $(z, x) \mapsto W(f_z)(x)$ is continuous and holomorphic in $z$. So the theorem on integrals that depend on a parameter, with a dominating integrable function, gives parts 1 and 2.

Third, the law. Each $q \in P_p$ is a product $q = u m$ of $u = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$ and $m = \mathrm{diag}(a, (a^*)^{-1})$, so it is enough to treat $u$ and $m$. For $m$, we have $\mathbf{s}(y)\, \iota(m) = \iota(m)\, \mathbf{s}(ya)$, and $W(f_z)(\iota(m) x) = \chi(\det a) |\det a|^{z + n/2} W(f_z)(x)$. The theta class gives $\Omega(mh, y) = \chi'(\det a) |\det a|^{\rho/2} \Omega(h, ya)$, and the change of variables $y \mapsto ya$ in the integral over $y$ contributes the factor $|\det a|^{-\rho}$. Since $n/2 + \rho/2 - \rho = p/2$, we get $R(f_z, g, \Omega)(mh) = (\chi\chi'^{-1})(\det a)\, |\det a|^{z + p/2}\, R(f_z, g, \Omega)(h)$. For $u$, we have $\mathbf{s}(y)\, \iota(u) = \mathbf{n}(z_0, x_0)\, \iota(u)\, \mathbf{s}(y)$ with $z_0 = y b y^*$, and $W(f_z)(\mathbf{n}(z_0, x_0)\, \iota(u)\, x) = \psi_{b_0}(z_0)\, W(f_z)(x)$. Now $\psi_{b_0}(z_0) = \psi(\tfrac12 \operatorname{tr}(b \langle y, y \rangle))$, which is the factor of $\Omega(uh, y)$ in the theta class. The two factors cancel in $W(f_z) \cdot \overline{\Omega}$, since $|\psi| = 1$. So $R(f_z, g, \Omega)(uh) = R(f_z, g, \Omega)(h)$. $\square$

**Corollary 5.3.3 (Reduced sections of height families).** The three conclusions of the last theorem hold under its hypotheses on $\psi$, $b_0$, $\chi$, $\chi'$, $\Omega$, $H$, $s_1$, $\varphi$ and $g$, with no further assumption.

Lean: `PositivityTheory.Rg.Rsw.rSec`.

*Proof.* This is [Theorem 5.3.2](/entry/r-sec-of-ht-exist/) applied to the existence of heights. $\square$

We turn to completeness. The quadratic extension $E/F$ has a character of the ideles that measures the norms.

**Definition 5.3.4 (Quadratic character, restriction condition).** A *quadratic character of $E/F$* is a continuous character $\eta \colon \mathbb{A}^\times \to \mathbb{C}^\times$ of absolute value $1$ that is trivial on $F^\times$ and on the norms $N_{E/F}(\mathbb{A}_E^\times)$, and is not trivial. A Hecke character $\chi$ of $\mathbb{A}_E^\times$ satisfies the *restriction condition of degree $k$* if a quadratic character of $E/F$ exists and every quadratic character $\eta$ of $E/F$ satisfies $\chi|_{\mathbb{A}^\times} = \eta^k$.

By [class field theory](/learn/class-field-theory/#hecke-characters) there is exactly one quadratic character of $E/F$. The restriction condition is the condition on the character in the [doubling method](/learn/theta/#the-doubling-method) for unitary groups: $\chi|_{\mathbb{A}^\times} = \eta^k$ is the condition for the Weil representation of a unitary group in $k$ variables. We need one input.

**Theorem 5.3.5 (Characters with a given restriction).** For each $k \ge 0$ there is a Hecke character $\chi$ of $\mathbb{A}_E^\times$ that satisfies the restriction condition of degree $k$.

Lean: `GlobalTheory.T.hecke_character_eta_condition`.

*Proof.* We take this result as given; we do not prove it in this chapter. $\square$

**Definition 5.3.6 (Complete theta class).** Let $\chi$ be a Hecke character and $b_0 \in \mathrm{Herm}_\rho(E)$. The theta class $\mathrm{Th}(\psi, \chi, b_0)$ is *complete* if each continuous bounded function $u$ on $M_{\rho \times p}(\mathbb{A}_E)$ with
$$\int u(y)\, \overline{\Omega(1, y)}\, d\mu(y) = 0 \qquad \text{for all } \Omega \in \mathrm{Th}(\psi, \chi, b_0)$$
is zero.

The proof of completeness goes by induction on $\rho$, and we take its three steps as given. Say that $b_0$ is *diagonal invertible* if it is diagonal with $\det b_0 \neq 0$. For $b = \mathrm{diag}(b_1, b_2)$ with $b_1 \in \mathrm{Herm}_r(E)$ and $b_2 \in \mathrm{Herm}_s(E)$, the space $M_{(r+s) \times p}$ is the product of $M_{r \times p}$ and $M_{s \times p}$, and the Weil representation of the sum is the tensor product of the two Weil representations.

**Theorem 5.3.7 (Completeness in low rank).** Let $\psi$ be an additive character and let the measures have covolume one.

1. If $\rho = 0$, the theta class $\mathrm{Th}(\psi, 1, b_0)$ is complete.
2. If $\rho = 1$, $\det b_0 \neq 0$ and $\chi$ is a Hecke character that satisfies the restriction condition of degree $1$, then $\mathrm{Th}(\psi, \chi, b_0)$ is complete.
3. Let $b = \mathrm{diag}(b_1, b_2)$ with $b_1$ of size $r$ and $b_2$ of size $s$, and let $\chi_1$, $\chi_2$ be characters. If $\mathrm{Th}(\psi, \chi_1, b_1)$ and $\mathrm{Th}(\psi, \chi_2, b_2)$ are complete, then $\mathrm{Th}(\psi, \chi_1 \chi_2, b)$ is complete.

Lean: `GlobalTheory.T.zero_coefficient_total` (also `GlobalTheory.T.rank_one_theta_total`, `GlobalTheory.T.step_total_of_products`).

*Proof.* We take these results as given; we do not prove them in this chapter. Part 2 rests on the continuity of the [Weil representation](/learn/theta/#the-weil-representation), its $K$-finite vectors and the Fock model; part 3 rests on the density of tensor products of Schwartz functions and on product measures. $\square$

**Theorem 5.3.8 (Completeness of theta functions).** Assume the conclusion of the theorem on characters with a given restriction. Let $\psi$ be an additive character, $b_0 \in \mathrm{Herm}_\rho(E)$ diagonal invertible, and $\chi$ a Hecke character that satisfies the restriction condition of degree $\rho$, with $\chi = 1$ if $\rho = 0$. Then $\mathrm{Th}(\psi, \chi, b_0)$ is complete.

Lean: `GlobalTheory.CompanionTheory.ThTot.thTotal` (also `GlobalTheory.T.theta_total_of_hecke_eta`, a second name).

*Proof.* We use induction on $\rho$, for all $p$, all $b_0$ and all $\chi$ at once. For $\rho = 0$ we have $\chi = 1$, and this is part 1 of the theorem on completeness in low rank.

Let $\rho \ge 0$ and let $b_0$ have size $\rho + 1$. Write $b_0 = \mathrm{diag}(b_1, b_2)$ with $b_1$ of size $\rho$ and $b_2$ of size $1$. Since $b_0$ is diagonal with nonzero determinant, so are $b_1$ and $b_2$. Choose a Hecke character $\chi_1$ with the restriction condition of degree $1$: if $\rho = 0$ take $\chi_1 = \chi$, and if $\rho \ge 1$ take $\chi_1$ from the theorem on characters with a given restriction. Then $\chi \chi_1^{-1}$ is a Hecke character, and for the quadratic character $\eta$ we have $(\chi \chi_1^{-1})|_{\mathbb{A}^\times} = \eta^{\rho + 1} \eta^{-1} = \eta^\rho$. If $\rho = 0$, then $\chi \chi_1^{-1} = 1$. So the induction hypothesis applies to $b_1$ and $\chi \chi_1^{-1}$, and $\mathrm{Th}(\psi, \chi\chi_1^{-1}, b_1)$ is complete. Part 2 of the theorem on low rank shows that $\mathrm{Th}(\psi, \chi_1, b_2)$ is complete. Part 3 then shows that $\mathrm{Th}(\psi, \chi, b_0)$ is complete, since $\chi \chi_1^{-1} \cdot \chi_1 = \chi$. In each step we use measures of covolume one on $M_{\rho \times p}$ and $M_{1 \times p}$, which exist. $\square$

**Corollary 5.3.9 (Completeness of theta functions).** Let $\psi$ be an additive character, $b_0$ diagonal invertible of size $\rho$, and $\chi$ a Hecke character with the restriction condition of degree $\rho$ and with $\chi = 1$ if $\rho = 0$. Let $u$ be a bounded continuous function on $M_{\rho \times p}(\mathbb{A}_E)$ with $\int u\, \overline{\Omega(1, \cdot)}\, d\mu = 0$ for all $\Omega \in \mathrm{Th}(\psi, \chi, b_0)$. Then $u = 0$.

Lean: `PositivityTheory.Rg.Rsw.thTotal`.

*Proof.* This is [Theorem 5.3.8](/entry/th-tot-th-total/) applied to the theorem on characters with a given restriction. $\square$

**Remark 5.3.10 (Formalization).** The theorem on reduced sections asks for $\det b_0 \neq 0$ and for $\chi$ and $\chi'$ to be Hecke characters, but its proof does not use these hypotheses; it also uses only the decomposition $G_n = P_n C_0$ from the existence of heights, not the height ([RegularSectionOfHeights.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/RegularSectionOfHeights.lean#L309)). For $\rho = 0$ the space $M_{0 \times p}$ has one point, so the completeness for $\rho = 0$ is a statement about one value. The completeness theorem needs $\chi = 1$ when $\rho = 0$; the restriction condition of degree $0$ only says that $\chi$ is trivial on $\mathbb{A}^\times$. The second names are wrappers that try three tactics, with the heartbeat limit at one million, for a one-line proof. We have not unfolded the inputs on low rank.
