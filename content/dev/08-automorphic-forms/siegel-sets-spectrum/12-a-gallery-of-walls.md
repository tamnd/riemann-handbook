---
title: A gallery of walls for Eisenstein series
decls:
  - GlobalTheory.CompanionTheory.RgEisGal.gallery
  - GlobalTheory.T.gallery_of_tubes_and_crossing
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A gallery of walls for Eisenstein series

This section proves a functional equation $y \mapsto N - y$ for a degenerate Eisenstein series $E_S(y h)$ attached to a parabolic $S$. The method is the one of Langlands: the degenerate series is the value at $l_1 = 0$ of an [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) in two variables $l = (l_1, l_2)$; each rank one functional equation, called a wall, continues the two variable series across one line in the $l$-plane; and a gallery of four walls leads from the chamber where $E_S(yh)$ converges to the chamber where $E_S((N - y)h)$ converges. Holomorphic functions on tubes over convex regions are glued along the gallery to one entire function of $l$. The theorem is the induction step of the [continuation of Siegel Eisenstein series](/entry/gallery-of/) that is used in the theta correspondence. Everything is stated for an abstract locally compact group, so the [arithmetic of Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets) enters only through the convergence hypotheses.

### Setting

Let $G$ be a locally compact Hausdorff group that is first countable, $K \subseteq G$ a compact subgroup, $\rho$ a continuous representation of $K$ on a finite dimensional complex space $W$, and $\Gamma \subseteq G$ a subgroup.

**Definition 3.12.1 (Parabolic data, heights).** A parabolic datum is a closed subgroup $P$ with $G = PK$ and a function $c$ on $G$ whose restriction to $P$ is a continuous unitary character, trivial on $\Gamma \cap P$. A height for $P$ is a continuous function $\eta : G \to \mathbb{R}$ with $\eta(pg) = \eta(p) + \eta(g)$ for $p \in P$, $\eta(gk) = \eta(g)$ for $k \in K$, and $\eta(\gamma) = 0$ for $\gamma \in \Gamma \cap P$.

Heights form a real vector space, and a height for $Q$ is a height for every $P \subseteq Q$. The section space of $(P, c)$ is $W_P = \{w : c(k)\rho(k) w = w \text{ for } k \in K \cap P\}$, and the section is $\sigma_P(pk) w = c(p) \rho(k)^{-1} w$ for $w \in W_P$.

**Definition 3.12.2 (Eisenstein series).** For a function $\Lambda : G \to \mathbb{C}$, $g \in G$ and $w \in W_P$,
$$E_P(\Lambda)(g) w = \sum_{\gamma \in (\Gamma \cap P) \backslash \Gamma} e^{\Lambda(\gamma g)}\, \sigma_P(\gamma g) w.$$
A real function $\lambda$ is convergent for $P$ if $\sum_{\gamma} e^{\lambda(\gamma g)}$ converges for every $g$.

If $\Lambda = \sum_j z_j \eta_j$ with heights $\eta_j$ and $\operatorname{Re}\Lambda$ convergent, the series converges absolutely. A function $f$ of one complex variable is strip entire if it is entire and bounded on every vertical strip; it is left good at $a$ if it is holomorphic on $\operatorname{Re} z < a$ and bounded on the vertical strips inside that half plane.

**Definition 3.12.3 (Wall).** Let $(P, c)$ and $(P', c)$ be parabolic data, $\eta$ a height for $P$, $\eta'$ and $\beta$ heights for $P'$, and $L \subseteq W_P$. A wall from $P$ to $P'$ on $L$ is a tuple $(R, D, \mathrm{Op}, H)$ where $R \ge 0$, $D$ is strip entire and not identically $0$, $\mathrm{Op}(z) : L \to W_{P'}$ is left good at $-R$, and $H(z, g) : L \to W$ is entire in $z$, continuous in $(z, g)$ and locally bounded on vertical strips, such that $x\eta$ is convergent for $P$ when $x > R$, $\beta - x\eta'$ is convergent for $P'$ when $x < -R$, and
$$H(z) = D(z)\, E_P(z\eta) \quad (\operatorname{Re} z > R), \qquad H(z) = E_{P'}(\beta - z\eta') \circ \mathrm{Op}(z) \quad (\operatorname{Re} z < -R).$$

A wall is a rank one functional equation in which $D$ removes the poles and $\mathrm{Op}$ is the intertwining operator.

**Definition 3.12.4 (Series in two variables).** Let $P, P' \subseteq Q$, let $\xi$ be a height for $Q$, and let $H$ be a wall for the group $\Gamma \cap Q$. For $l = (l_1, l_2) \in \mathbb{C}^2$ put
$$\hat E(l)(g) = \sum_{\gamma \in (\Gamma \cap Q) \backslash \Gamma} e^{l_2 \xi(\gamma g)}\, H(l_1, \gamma g).$$

For $\Omega \subseteq \mathbb{R}^2$, the tube over $\Omega$ is the set of $l$ with $(\operatorname{Re} l_1, \operatorname{Re} l_2) \in \Omega$. A function on a tube is good if it is holomorphic on every complex line, jointly continuous, and locally bounded over compact subsets of $\Omega$.

We use the following facts, taken as given.

- (Crossing.) Let $\Omega$ be open, and assume that every $x \in \Omega$ has $a > R$ and $b < -R$ with $b < x_1 < a$ such that $a\eta + t\xi$ is convergent for $P$ and $\beta - b\eta' + t\xi$ is convergent for $P'$ when $|t - x_2|$ is small. Then $\hat E$ converges absolutely and is good on the tube over $\Omega$. Where $\operatorname{Re} l_1 > R$ and the exponent is convergent, $\hat E(l) = D(l_1)\, E_P(l_1\eta + l_2\xi)$; where $\operatorname{Re} l_1 < -R$ and the exponent is convergent, $\hat E(l) = E_{P'}(\beta - l_1\eta' + l_2\xi) \circ \mathrm{Op}(l_1)$.
- (Identity on tubes.) Two functions holomorphic on lines over a convex open $\Omega$ that agree on the tube over a nonempty open $\Omega' \subseteq \Omega$ agree on the tube over $\Omega$.
- (Chain of tubes.) Let $F_0, \dots, F_m$ be good on tubes over convex open sets $\Omega_0, \dots, \Omega_m$, let $F_{i-1}$ and $F_i$ agree over a nonempty open subset of $\Omega_{i-1} \cap \Omega_i$, and let every point of $\mathbb{R}^2$ be the midpoint of two points of $\bigcup_i \Omega_i$. Then there is $\Phi$, good on $\mathbb{C}^2$, with $\Phi(l) = e^{l_1^2 + l_2^2} F_i(l)$ on the tube over $\Omega_i$ for every $i$.

Crossing comes from unfolding $E_P$ along $(\Gamma \cap P)\backslash(\Gamma \cap Q)$. The chain of tubes is Bochner's tube theorem in the form needed here; the Gaussian factor makes the glued function bounded on vertical strips.

### The gallery

**Theorem 3.12.5 (Gallery).** Let $S \supseteq A, B$ and $Q_1 \supseteq A$, $Q_2 \supseteq B$ be subgroups such that $(S, c)$, $(A, c)$ and $(B, c)$ are parabolic data. Let $h$ be a height for $S$, $a$ a height for $Q_1$, $h + b$ a height for $Q_2$, and $N \in \mathbb{R}$. Assume that for some $R_0$ and all $y, z, r > R_0$ the functions $y h$, $za + yh$ and $r(h + b) + yh$ are convergent for $S$, $A$ and $B$. Assume there are five walls, each for the intersection of $\Gamma$ with the named group:

1. (First wall, in $S$.) From $A$ to $B$ on $W_S$, with $\eta = a$, $\eta' = b$, $\beta = h + Nb$, such that $H(0) = a_0 \sigma_S$ with $a_0 \neq 0$, and $\mathrm{Op}(z) = z\, O(z)$ for $\operatorname{Re} z < -R$, with $O$ left good at $\frac12$.
2. (Wall $c$, in $Q_2$.) From $B$ to $B$ with $\eta = \eta' = \beta = -b$.
3. (Wall $a$, in $S$.) From $B$ to $A$ with $\eta = b$, $\eta' = a$, $\beta = Na - h$.
4. (Wall $b$, in $Q_1$.) From $A$ to $A$ with $\eta = \eta' = h - a$ and $\beta = (N - 1)(h - a)$.
5. (Last wall, in $S$.) From $A$ to $B$ on $W_A$, with $\eta = a$, $\eta' = b$, $\beta = h + Nb$, such that $D(z) = (z - N)\, d(z)$ with $d$ strip entire and $d(N) \neq 0$, and $H(N) = e^{h}\, \sigma_S \circ T$ for a linear map $T : W_A \to W_S$.

Then there is a wall from $S$ to $S$ on $W_S$ with $\eta = \eta' = h$ and $\beta = Nh$. That is, for some strip entire $D \not\equiv 0$, some left good $\mathrm{Op}$ and some entire $H$,
$$H(y) = D(y)\, E_S(yh) \quad (\operatorname{Re} y \gg 0), \qquad H(y) = E_S((N - y)h) \circ \mathrm{Op}(y) \quad (\operatorname{Re} y \ll 0).$$

Lean: `GlobalTheory.CompanionTheory.RgEisGal.gallery` (also `GlobalTheory.T.gallery_of_tubes_and_crossing`, a second name).

*Proof.* Let $R \ge 1$ exceed $|N| + 1$, $R_0$ and the constants of the five walls. All heights below are linear combinations of $h$, $a$, $b$, and convergence of each exponent follows from the convergence hypothesis.

*Five series.* Apply crossing to each wall. The first wall with $\xi = h$ gives $\hat E_0$, good over the cone $C_I = \{x_2 > 10R,\ x_1 + x_2 > 10R\}$. Wall $c$ with $\xi = h + b$ gives $\hat E_c$ over $C_C = \{x_2 - x_1 > 10R,\ x_2 + x_1 > 10R\}$. Wall $a$ with $\xi = h$ gives $\hat E_a$ over $C_A = \{x_2 - x_1 > 10R,\ x_2 > 10R\}$. Wall $b$ with $\xi = a$ gives $\hat E_b$ over $C_C$. The last wall with $\xi = h$ gives $\hat E_l$ over $C_I$. In each case the convergence condition of crossing holds on the cone because the exponents are positive combinations of the convergent ones.

*Changes of variables.* Put $y(l) = l_1 + l_2 + 1 - N$, $z(l) = l_1 + 2l_2 + 1 - N$ and
$$\begin{aligned} m_c(l) &= (y(l),\ l_2 + 1), & m_a(l) &= (z(l),\ l_2 + 1), \\ m_b(l) &= (l_2,\ 2N - 1 - l_1 - l_2), & m_l(l) &= (N - l_1,\ N - 1 - l_2). \end{aligned}$$
Let $M = 100R$. On the tubes over the four chamber pairs
$$\begin{gathered} \{x_1 < -M < M < x_1 + x_2\},\quad \{x_1 + x_2 < -M < M < x_1 + 2x_2\}, \\ \{x_1 + 2x_2 < -M < M < x_2\},\quad \{x_2 < -M,\ x_1 < -M\} \end{gathered}$$
the following identities hold, where $D_\bullet$ and $\mathrm{Op}_\bullet$ belong to the walls:
$$D_c(y)\, \hat E_0(l) = \hat E_c(m_c l) \circ \mathrm{Op}_0(l_1), \qquad D_a(z)\, \hat E_c(m_c l) = \hat E_a(m_a l) \circ \mathrm{Op}_c(y),$$
$$D_b(l_2)\, \hat E_a(m_a l) = \hat E_b(m_b l) \circ \mathrm{Op}_a(z),$$
$$-d(N - l_1)\, \hat E_b(m_b l) \circ \mathrm{Op}_a(z)\, \mathrm{Op}_c(y)\, \mathrm{Op}_0(l_1) = \hat E_l(m_l l) \circ \mathrm{Op}_b(l_2)\, \mathrm{Op}_a(z)\, \mathrm{Op}_c(y)\, O(l_1).$$
For each one, the left side is given by the left formula of crossing and the right side by the right formula, so both are Eisenstein series for the same parabolic. They agree because the exponents agree. For the first identity, the left exponent is $h + Nb - l_1 b + l_2 h$, and the right one is $-y\,b + (l_2 + 1)(h + b)$; both equal $(1 + l_2)h + (N - l_1)b$. The others are checked in the same way. In the last identity we also use $\mathrm{Op}_0(l_1) = l_1 O(l_1)$ and $D_l(N - l_1) = -l_1\, d(N - l_1)$.

*Gluing.* Put $F_0 = D_c(y) D_a(z) D_b(l_2)\, \hat E_0$, $F_1 = D_a(z) D_b(l_2)\, \hat E_c(m_c l)\, \mathrm{Op}_0(l_1)$, $F_2 = D_b(l_2)\, \hat E_a(m_a l)\, \mathrm{Op}_c(y)\, \mathrm{Op}_0(l_1)$ and $F_3 = \hat E_b(m_b l)\, \mathrm{Op}_a(z)\, \mathrm{Op}_c(y)\, \mathrm{Op}_0(l_1)$. They are good over $\Omega_0 = C_I$ and over the preimages $\Omega_1$, $\Omega_2$, $\Omega_3$ of $C_C$, $C_A$, $C_C$ under $m_c$, $m_a$, $m_b$; the operators are left good on these regions because $R$ is large. By the first three identities, $F_{i-1} = F_i$ on the chamber pair between them. The four regions are convex, and every point of $\mathbb{R}^2$ is the midpoint of two of their points. The chain of tubes gives $\Phi$, good on $\mathbb{C}^2$, with $\Phi = e^{l_1^2 + l_2^2} F_i$ over $\Omega_i$.

Let $\Omega_4$ be the preimage of $C_I$ under $m_l$, intersected with $\{x_1 < \frac12\}$, where $O$ is defined. It is convex and open, and it contains the last chamber pair, which also lies in $\Omega_3$. On the tube over $\Omega_4$ both $-d(N - l_1)\,\Phi(l)$ and $e^{l_1^2 + l_2^2}\, \hat E_l(m_l l) \circ \mathrm{Op}_b(l_2)\, \mathrm{Op}_a(z)\, \mathrm{Op}_c(y)\, O(l_1)$ are holomorphic on lines. On the last chamber pair they agree, by the last identity and $\Phi = e^{l_1^2 + l_2^2} F_3$. By the identity on tubes they agree over all of $\Omega_4$.

*Restriction to $l_1 = 0$.* Put $H(y) = \Phi(0, y)$. For $\operatorname{Re} y > 10R$, the point $(0, y)$ lies over $C_I$, and since $H_0(0) = a_0 \sigma_S$, $\hat E_0(0, y) = a_0 E_S(yh)$. So $H(y) = D(y) E_S(yh)$ with
$$D(y) = e^{y^2} D_c(y + 1 - N)\, D_a(2y + 1 - N)\, D_b(y)\, a_0.$$
It is strip entire, and it is not identically zero, as a product of nonzero entire functions. For $\operatorname{Re} y < -20R$ the point $(0, y)$ lies over $\Omega_4$, and $m_l(0, y) = (N, N - 1 - y)$. Since $H_l(N) = e^h \sigma_S \circ T$, we get $\hat E_l(N, u) = E_S((1 + u) h) \circ T$, and $1 + u = N - y$. Dividing by $-d(N) \neq 0$,
$$H(y) = E_S((N - y)h) \circ \mathrm{Op}(y), \qquad \mathrm{Op}(y) = -\frac{e^{y^2}}{d(N)}\; T\, \mathrm{Op}_b(y)\, \mathrm{Op}_a(2y + 1 - N)\, \mathrm{Op}_c(y + 1 - N)\, O(0).$$
Each factor is left good at $-20R$, so $\mathrm{Op}$ is. Convergence of $yh$ for $y > 20R$ is part of the hypothesis. So $(20R, D, \mathrm{Op}, H)$ is a wall. $\square$

At $l_1 = 0$ the first operator $\mathrm{Op}_0$ vanishes, and $O(0)$ takes its place: the degenerate series is a residue of the series in two variables, and the factor $z$ in $\mathrm{Op}_0(z) = zO(z)$ is cancelled by the zero of $D_l$ at $N$.

**Remark 3.12.6 (Formalization).** The theorem is at line 118 of [GalleryOfTubesAndCrossing.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GalleryOfTubesAndCrossing.lean#L118). It proves an implication between four propositions: the section law, the identity on tubes, the chain of tubes and crossing imply the gallery. The section law is bound to `_` on line 119 and never used. The gluing of the tubes is the lemma `core` at line 226 of `ChamberPairThreeFour.lean`, a file that also holds the cones and the changes of variables. The second name is in a statement file whose proof is the `first | exact ...` wrapper. The theorem is used as `gallery_of` in `SiegelMultOf.lean`, line 97, together with crossing, which comes from the section law and the wall law.
