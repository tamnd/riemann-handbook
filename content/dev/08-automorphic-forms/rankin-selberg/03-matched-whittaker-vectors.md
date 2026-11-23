---
title: Matched Whittaker vectors
decls:
  - GlobalTheory.SchurExt.exists_ext
  - GlobalTheory.T.exists_whittaker_bump_extension_schur_complement
  - GlobalTheory.JSW.MatchedVec.matched_vectors
  - GlobalTheory.T.exists_matchedWhittakerVectors_shintaniRelations
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Matched Whittaker vectors

The Rankin-Selberg integral for $\mathrm{GL}_n \times \mathrm{GL}_m$ with $m < n$ pairs a cusp form $\phi$ on $\mathrm{GL}_n$, restricted to $\mathrm{GL}_m$, with a cusp form $\phi'$ on $\mathrm{GL}_m$. To compute it we need a pair of vectors whose Whittaker functions agree along the embedded $\mathrm{GL}_m$, up to a nonnegative weight, and which obey Shintani's formula at the places outside a finite set. This section constructs such a pair. There are two steps. First, a function on $\mathrm{GL}_m(\mathbb{A})$ of Whittaker type extends to $\mathrm{GL}_n(\mathbb{A})$ by a Schur complement construction. Second, the [Kirillov bump lemma](/entry/kirillov-semilocal-smooth-bump/) realizes the extension as the Whittaker function of a vector in the smooth span of the cuspidal representation. The result is used in [the $\mathrm{GL}_n \times \mathrm{GL}_m$ integral](/entry/rs-nm-partial-l-eq-div/).

We keep the notation of the previous sections. So $E$ is a totally complex number field, $\mathbb{A}$ its adeles, $\psi$ the standard additive character of $\mathbb{A}/E$, and, for $a \ge 1$, $N_a$ is the upper unitriangular subgroup of $\mathrm{GL}_a$ and $\psi_N(u) = \psi(u_{12} + \dots + u_{a-1,a})$ on $N_a(\mathbb{A})$. Let $S$ be a finite set of finite places.

**Definition 8.3.1 (Functions supported at $S$).** Let $G_a(S)$ be the set of $g \in \mathrm{GL}_a(\mathbb{A})$ with $g_w = 1$ for every finite place $w \notin S$. Let $P_a(S)$ be the set of $g \in G_a(S)$ whose last row is $(0, \dots, 0, 1)$.

So $G_a(S)$ is the product of $\mathrm{GL}_a$ over the archimedean places and the places in $S$, and $P_a(S)$ is its mirabolic part. For $m, r \ge 0$ let $\iota \colon \mathrm{GL}_{m+1} \to \mathrm{GL}_{m+r+2}$ be the block embedding $\iota(h) = \mathrm{diag}(h, 1_{r+1})$. It maps $G_{m+1}(S)$ into $P_{m+r+2}(S)$.

**Definition 8.3.2 (Whittaker bump).** Let $X \subseteq \mathrm{GL}_a(\mathbb{A})$. A function $\beta \colon \mathrm{GL}_a(\mathbb{A}) \to \mathbb{C}$ is a *Whittaker bump on $X$* if:

1. $\beta(ug) = \psi_N(u)\beta(g)$ for $u \in N_a(\mathbb{A})$ and all $g$;
2. there is a compact set $C$ such that every $h \in X$ with $\beta(h) \neq 0$ lies in $N_a(\mathbb{A}) C$;
3. there is an open subgroup $U$ of $\mathrm{GL}_a(\mathbb{A}_f)$ with $\beta(gu) = \beta(g)$ for all $u \in U$ and all $g$;
4. for every $g$, the function $y \mapsto \beta(gy)$ is $C^\infty$ on $\mathrm{GL}_a(\mathbb{A}_\infty)$, viewed as an open subset of the real vector space $M_a(\mathbb{A}_\infty)$.

Condition 1 is the transformation law of a Whittaker function, and conditions 2 to 4 say that $\beta$ is smooth and compactly supported modulo $N_a$ on $X$. A function of this kind on the mirabolic part is what the Kirillov model of a generic representation contains: the [Kirillov bump lemma](/entry/kirillov-semilocal-smooth-bump/) says that each Whittaker bump on $P_a(S)$ is the restriction to $P_a(S)$ of the Whittaker function $W_F$ of a vector $F$ in the smooth span of a cuspidal representation, as soon as some vector of the representation has a Whittaker function that is nonzero on $G_a(S)$.

**Theorem 8.3.3 (Extension by Schur complements).** Let $m, r \ge 0$ and let $\beta$ be a function on $\mathrm{GL}_{m+1}(\mathbb{A})$ that satisfies conditions 1, 3 and 4 and satisfies condition 2 on $G_{m+1}(S)$. Then there is a Whittaker bump $b$ on $P_{m+r+2}(S)$, on $\mathrm{GL}_{m+r+2}(\mathbb{A})$, such that $b(\iota(h)) = \beta(h)$ for all $h \in G_{m+1}(S)$.

Lean: `GlobalTheory.SchurExt.exists_ext` (also `GlobalTheory.T.exists_whittaker_bump_extension_schur_complement`, a wrapper).

*Proof.* Put $n = m + r + 2$ and write $g \in \mathrm{GL}_n(\mathbb{A})$ in blocks
$$g = \begin{pmatrix} A & B \\ C & D \end{pmatrix}, \qquad A \in M_{m+1}, \quad D \in M_{r+1}.$$
If $D$ is invertible, put $X = BD^{-1}$, $Y = D^{-1}C$ and $\Sigma = A - BD^{-1}C$, the Schur complement of $D$. Then
$$g = \begin{pmatrix} 1 & X \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \Sigma & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} 1 & 0 \\ Y & 1 \end{pmatrix},$$
as one checks by multiplying out, and $\Sigma$ is invertible since $\det g = \det \Sigma \det D$.

We choose three auxiliary functions. Let $b_1$ be a Whittaker bump on all of $\mathrm{GL}_{r+1}(\mathbb{A})$ with $b_1(1) = 1$. Let $\chi_\infty$ be a real $C^\infty$ bump function on $M_{(r+1) \times (m+1)}(\mathbb{A}_\infty)$, with compact support and equal to $1$ near $0$, and put $\chi(Y) = \chi_\infty(Y_\infty)\mathbf{1}(Y_f \text{ integral})$. Let $\Phi$ be a function on $\mathrm{GL}_n(\mathbb{A})$ with $\Phi(1) = 1$ that satisfies conditions 1 and 3. Define
$$s(g) = \psi(X_{m+1, 1})\, \beta(\Sigma)\, b_1(D)\, \chi(Y)$$
if $D$ is invertible, and $s(g) = 0$ otherwise. Here $X_{m+1,1}$ is the entry of $X$ in position $(m+1, m+2)$ of $g$, the one superdiagonal entry that lies outside both diagonal blocks. Split each $g$ as $g = g_S g^S$, where $g_S$ has the components of $g$ at the archimedean places and at $S$ and $1$ elsewhere, and $g^S$ has the other components. Put $b(g) = s(g_S)\Phi(g^S)$.

Condition 1. Let $u \in N_n(\mathbb{A})$ have diagonal blocks $u_1, u_2$ and upper right block $z$. Then $ug$ has the blocks $\Sigma' = u_1\Sigma$, $D' = u_2 D$, $Y' = Y$, and $X'$ differs from $u_1 X u_2^{-1}$ by $z u_2^{-1}$. A comparison of the $(m+1, 1)$ entries gives $s(ug) = \psi_N(u)s(g)$, from condition 1 for $\beta$ and $b_1$. Since $u_S$ and $u^S$ are again unitriangular and $\psi_N(u) = \psi_N(u_S)\psi_N(u^S)$, condition 1 holds for $b$.

Condition 2. For $p \in P_n(S)$ we have $p^S = 1$, so $b(p) = s(p)$, and the blocks of $p$ satisfy $\Sigma, D \in G(S)$. If $s(p) \neq 0$, then $\Sigma \in N_{m+1}(\mathbb{A})C_1$ and $D \in N_{r+1}(\mathbb{A})C_2$ for compact sets $C_1, C_2$ given by condition 2 for $\beta$ and $b_1$, and $Y$ lies in the compact set $\operatorname{supp}\chi_\infty \times \prod_w M(\mathcal{O}_w)$. Write $\Sigma = u_1c_1$ and $D = u_2c_2$. The factorization gives $p = u\, \mathrm{diag}(c_1, c_2) \begin{pmatrix} 1 & 0 \\ Y & 1 \end{pmatrix}$ with $u \in N_n(\mathbb{A})$, and the last two factors range over a compact set.

Condition 3. Right translation by a small open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$ changes $g_S$ and $g^S$ by elements close to $1$. For $g_S$ such a change moves $\Sigma$ and $D$ by right translations near $1$ and keeps $Y_f$ integral. So $s$ is invariant under a small open subgroup; $\Phi$ is invariant under another; their intersection works for $b$.

Condition 4. An archimedean translation $y$ changes only $g_S$. On the open set where $D$ is invertible, the maps $g \mapsto \Sigma, D, X, Y$ are smooth functions of the archimedean coordinates, and $\beta$, $b_1$ and $\chi_\infty$ are smooth. Since $b_1$ is compactly supported modulo $N_{r+1}$, the factor $b_1(D)$ vanishes when $|\det D_\infty|$ is small, so $s$ vanishes near the set where $D$ is singular, and $s$ is smooth everywhere.

Finally, let $h \in G_{m+1}(S)$. Then $\iota(h)_S = \iota(h)$ and $\iota(h)^S = 1$. The blocks of $\iota(h)$ are $\Sigma = h$, $D = 1$, $X = 0$ and $Y = 0$. So $b(\iota(h)) = \beta(h) b_1(1)\chi(0)\Phi(1) = \beta(h)$. $\square$

Now we combine the extension with the Kirillov bump lemma. Recall from [the unfolding section](/entry/unfolded-whittaker-integral-eq-euler-product-schur-sums/) the Shintani value: for $q > 1$, $\alpha \in \mathbb{C}^a$ and $l \in \mathbb{N}^a$,
$$c_q(\alpha, l) = q^{-\langle \rho, l \rangle} s_l(\alpha) \text{ if } l_1 \ge \dots \ge l_a, \qquad c_q(\alpha, l) = 0 \text{ otherwise},$$
with $\langle \rho, l \rangle = \sum_i \frac{a + 1 - 2i}{2} l_i$. For $l \in \mathbb{N}^{m+1}$ let $\bar l \in \mathbb{N}^{m+r+2}$ be $l$ padded with zeros. For a family $\varpi = (\varpi_w)$ of uniformizers and a finitely supported family $l = (l_w)$ with $l_w \in \mathbb{N}^a$, let $t_l$ be the diagonal adele of the first section.

**Theorem 8.3.4 (Matched Whittaker vectors).** Let $m, r \ge 0$. Assume that for every finite $w \notin S$ the conductor of $\psi_w$ is $\mathcal{O}_w$: for $x \in E_w$, $\psi_w(xy) = 1$ for all $y \in \mathcal{O}_w$ if and only if $x \in \mathcal{O}_w$. Let $\pi$ and $\pi'$ be unitary cuspidal representations of $\mathrm{GL}_{m+r+2}$ and $\mathrm{GL}_{m+1}$ over $E$, and for $w \notin S$ let $\alpha_w \in (\mathbb{C}^\times)^{m+r+2}$ and $\beta_w \in (\mathbb{C}^\times)^{m+1}$ have as multisets of entries Satake parameters of $\pi$ and $\pi'$ at $w$. Then there are $\phi$ in the smooth span of $\pi$, $\phi'$ in the smooth span of $\pi'$ and $\kappa \colon \mathrm{GL}_{m+1}(\mathbb{A}) \to \mathbb{R}$ such that:

1. $\phi$ and $\phi'$ are right invariant under an open subgroup of $\mathrm{GL}(\mathbb{A}_f)$ and under $K_w = \mathrm{GL}(\mathcal{O}_w)$ for each finite $w \notin S$;
2. for every family $\varpi$ of uniformizers, every $l$ supported outside $S$ and every $h \in G_{m+1}(S)$,
$$\begin{aligned} W_{\phi'}(h t_l) &= \prod_w c_{Nw}(\beta_w, l_w)\, W_{\phi'}(h), \\ W_\phi(\iota(h t_l)) &= \prod_w c_{Nw}(\alpha_w, \bar l_w)\, W_\phi(\iota(h)); \end{aligned}$$
3. $W_\phi(\iota(h)) = \kappa(h) W_{\phi'}(h)$ for all $h \in G_{m+1}(S)$;
4. $\kappa$ is continuous, $\kappa \ge 0$, $\kappa(uh) = \kappa(h)$ for $u \in N_{m+1}(\mathbb{A})$, $\kappa$ is compactly supported modulo $N_{m+1}(\mathbb{A})$ on $G_{m+1}(S)$, and $\kappa$ is right invariant under an open subgroup of $\mathrm{GL}_{m+1}(\mathbb{A}_f)$;
5. there is $h_0 \in G_{m+1}(S)$ with $\kappa(h_0) > 0$ and $W_{\phi'}(h_0) \neq 0$.

Lean: `GlobalTheory.JSW.MatchedVec.matched_vectors` (also `GlobalTheory.T.exists_matchedWhittakerVectors_shintaniRelations`, a wrapper).

*Proof.* We use three facts. The first two are results on $K_w$-fixed vectors, which we take as given. First, since the conductor of $\psi_w$ is $\mathcal{O}_w$ for $w \notin S$, there is $\phi' \in \pi'$ fixed by $K_w$ for all $w \notin S$ and a point $x_0 \in G_{m+1}(S)$ with $W_{\phi'}(x_0) \neq 0$; in the same way there is $\phi_0 \in \pi$, fixed by $K_w$ for $w \notin S$, with $W_{\phi_0}$ nonzero at a point of $G_{m+r+2}(S)$. Second, Shintani's formula, applied at each $w \notin S$ to such a $K_w$-fixed vector, gives $W_{\phi'}(xt_l) = \prod_w c_{Nw}(\beta_w, l_w)W_{\phi'}(x)$ for $x \in G_{m+1}(S)$; this is the first identity of 2. The same formula on $\mathrm{GL}_{m+r+2}$ gives the analogous identity for $W_{\phi_0}$ on $G_{m+r+2}(S)$. Third, $\iota(t_l) = t_{\bar l}$ for $l$ supported outside $S$, since padding with zeros adds the entries $\varpi_w^0 = 1$.

Next choose a weight $\kappa$ with the properties of 4 (and smooth at the archimedean places) and with $\kappa(x_0) > 0$. Put $\beta(h) = \kappa(h)W_{\phi'}(h)$. Then $\beta$ satisfies conditions 1 to 4 of a Whittaker bump on $G_{m+1}(S)$: condition 1 from that of $W_{\phi'}$ and the $N$-invariance of $\kappa$, condition 2 from that of $\kappa$, condition 3 because $\phi'$ is fixed by an open subgroup and so is $\kappa$, and condition 4 because $W_{\phi'}$ is smooth at the archimedean places. The [extension theorem](/entry/exists-ext/) gives a Whittaker bump $b$ on $P_{m+r+2}(S)$ with $b \circ \iota = \beta$ on $G_{m+1}(S)$.

The [Kirillov bump lemma](/entry/kirillov-semilocal-smooth-bump/), applied to $b$, $\pi$ and $\phi_0$, gives $\phi$ in the smooth span of $\pi$ with $W_\phi = b$ on $P_{m+r+2}(S)$. The same lemma says that $\phi$ is right invariant under an open subgroup, that $\phi$ is invariant under each element $t$ with $t_\infty = 1$ and $t_w = 1$ for $w \in S$ that fixes $\phi_0$, and that $W_\phi(xt) = cW_\phi(x)$ on $G_{m+r+2}(S)$ whenever $W_{\phi_0}(xt) = cW_{\phi_0}(x)$ on $G_{m+r+2}(S)$, for such $t$. The first gives the $K_w$-invariance of 1. The second, with $t = t_{\bar l}$, gives the second identity of 2 at the point $\iota(h)$, which lies in $P_{m+r+2}(S)$. Finally, for $h \in G_{m+1}(S)$, $W_\phi(\iota(h)) = b(\iota(h)) = \kappa(h)W_{\phi'}(h)$, which is 3, and $h_0 = x_0$ gives 5. $\square$

**Remark 8.3.5 (Formalization).** The smooth span is defined in [IsRapidInf.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsRapidInf.lean#L44) as the smallest space stable under right translation and under archimedean convolution with rapidly decreasing kernels; the sets $G_a(S)$ and $P_a(S)$ are at lines 26 and 31. The function $s$ of the proof is `schurF` in [IsIdempotentElemIdemSf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsIdempotentElemIdemSf.lean#L116), and $b$ is `extB` at line 126. There, the inverse of a matrix that is not invertible is replaced by $1$ (`mkGL`, line 100); this does not change $s$, which is $0$ when $D$ is singular. The splitting $g = g_S g^S$ uses the idempotent of $\mathbb{A}$ that is $1$ at the archimedean places and at $S$. The bump $\chi_\infty$ is a `ContDiffBump` with radii $1$ and $2$, so $\chi(0) = 1$. The compactness, invariance and smoothness parts of the extension theorem are separate statements, cited by the proof; we have not opened all of them. The Kirillov bump lemma and the existence of the weight $\kappa$ are cited in the same way. The wrapper [ExistsWhittakerBumpExtensionSchurComplementStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsWhittakerBumpExtensionSchurComplementStatement.lean#L17) raises `maxHeartbeats` to 1000000. In condition 2 the extension is compactly supported modulo $N$ only on $P_{m+r+2}(S)$, not on all of $G_{m+r+2}(S)$, which is all the Kirillov lemma needs; the argument of the proof works on $G_{m+r+2}(S)$ as well.
