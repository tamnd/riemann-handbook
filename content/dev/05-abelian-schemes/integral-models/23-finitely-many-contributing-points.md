---
title: Finitely many contributing points
decls:
  - GlobalTheory.FinPtsSep.fin_cosets_away_sep
  - GlobalTheory.FinPtsSep.finite_pts_conj_fixL_sep
  - GlobalTheory.T.orbital_integral_test_function_second
  - GlobalTheory.LKCx.CxReg.finite_pts_reg
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finitely many contributing points

The proof of [the count of marked fixed points](/entry/complex-count-regular-marked-points/) uses three finiteness facts. This section proves the second: when the test function away from $p$ has regular support, only finitely many classes of points give a nonzero contribution. First we fix one element $y_0$ with separable minimal polynomial of degree $n$ and show that only finitely many points see a conjugate of $y_0$; the main input is that the $h$ with $f(h^{-1} y_0 h) \neq 0$ lie in finitely many cosets $Z r K_L$, with $Z$ the centralizer of $y_0$. Then regular support reduces the general case to this one.

### Points and test functions

We keep the notation of the group datum $G$ of that section: the CM field $F$, the central simple $F$-algebra $C$ of dimension $n^2$ with involution $x \mapsto x^*$, the maps $\psi_v : C \to M_n(\mathbb{C})$, the hermitian matrices $H_v$ and the number $a(G)$. Let $\mathbb{A}^p$ be the ring of finite adeles of $\mathbb{Q}$ away from $p$. For a $\mathbb{Q}$-algebra $R$ let $G(R)$ be the group of pairs $(g, \lambda)$ with $g \in (R \otimes_{\mathbb{Q}} C)^\times$, $\lambda \in R^\times$ and $g g^* = \lambda$. A *level* $L$ is an open compact subgroup $K_L$ of $G(\mathbb{A}^p)$. At $p$ the datum gives a group $G_1$ with a standard compact subgroup $K_{\mathrm{HT}}$ and an automorphism $\sigma$.

**Definition 8.23.1 (Test function).** Let $H$ be a group with an automorphism $\theta$ and subgroups $K_0$ and $K$. A function $\varphi : H \to \mathbb{C}$ is a *test function* for $(\theta, K_0, K)$ if $K$ is commensurable with $K_0$, $\theta(K) \subseteq K$, $\varphi(k^{-1} g \theta(k)) = \varphi(g)$ for $k \in K$ and $g \in H$, and the support of $\varphi$ lies in finitely many double cosets $K_0 s K_0$.

Lean: `GlobalTheory.LKMid.IsTest`.

Below, $f$ is a test function for $(\mathrm{id}, K_L, K_L)$, a *test function at the level* $L$, and $f'$ one for $(\sigma, K_{\mathrm{HT}}, K')$, a *test function at* $p$, with $K' \subseteq G_1$.

For $\beta \in C^\times$ let $\Gamma_\beta$ be the group of pairs $(y, \lambda)$ with $y \in C^\times$, $\lambda \in \mathbb{Q}$, $\lambda > 0$ and $y \beta y^* = \lambda \beta$. Fix $x \in (\mathbb{A}^p \otimes C)^\times$ and $t \in (\mathbb{A}^p)^\times$ with $x \beta x^* = t$. We write $y^{(p)} = (x y x^{-1}, \lambda) \in G(\mathbb{A}^p)$ and $y_p$ for the image of $y$ under a homomorphism $\Gamma_\beta \to G_1$. Fix an infinite place $v$ and put $H_{v, \beta} = H_v \psi_v(\beta^{-1})$.

**Definition 8.23.2 (Points).** A *datum* is a triple $(g, g_p, z)$ with $g \in G(\mathbb{A}^p)$, $g_p \in G_1$ and $z \in \mathbb{C}^n$ with $\operatorname{Re}(z^* H_{v, \beta} z) > 0$. The datum $(g', g'_p, z')$ is *related* to $(g, g_p, z)$ if there are $y \in \Gamma_\beta$, $k \in K_L$, $k' \in K'$ and $c \in \mathbb{C}^\times$ with $g' = y^{(p)} g k$, $g'_p = y_p g_p k'$ and $z' = c \, \psi_v(y) z$. The set $\mathrm{Pts}(\beta)$ is the quotient of the set of data by the equivalence relation that this relation generates. An element $y \in \Gamma_\beta$ *fixes the line* of $z$ if $\psi_v(y) z = \mu z$ for some $\mu \in \mathbb{C}$.

Lean: `GlobalTheory.LKCx.Pts`, `GlobalTheory.LKCx.FixL`.

For a class $q$ we write $(g_q, g_{p,q}, z_q)$ for a chosen representative. An element $g \in G(\mathbb{A}^p)$ is *regular* if at some place $w \neq p$ any two elements of $\mathbb{Q}_w \otimes C$ that commute with the component $g_w$ commute with each other.

Lean: `GlobalTheory.LKCx.RegAf`.

### Finitely many cosets

**Theorem 8.23.3 (Finitely many cosets away from p).** Let $f$ be a test function at a level $L$, and let $y_0 \in \Gamma_\beta$ be such that the minimal polynomial of $y_0$ over $F$ is separable of degree $n$. Put $\gamma = y_0^{(p)}$. There is a finite set $R \subseteq G(\mathbb{A}^p)$ such that every $h \in G(\mathbb{A}^p)$ with $f(h^{-1} \gamma h) \neq 0$ can be written $h = c r k$ with $c \gamma = \gamma c$, $r \in R$ and $k \in K_L$.

Lean: `GlobalTheory.FinPtsSep.fin_cosets_away_sep`.

We use the following results.

### Inputs

1. If $\Omega \subseteq G(\mathbb{A}^p)$ is compact, then for almost all $w$ its image in $G(\mathbb{Q}_w)$ lies in the set $G(\mathbb{Z}_w)$ of points integral, with integral inverse, in a fixed basis of $C$.
2. For $y$ with separable minimal polynomial of degree $n$ and $\gamma_w = x_w y x_w^{-1}$, for almost all $w$: if $g^{-1} \gamma_w g \in G(\mathbb{Z}_w)$, then $g = c d$ with $c$ in the centralizer of $\gamma_w$ and $d \in G(\mathbb{Z}_w)$.
3. For almost all $w$, the set $G(\mathbb{Z}_w)$ is closed under products.
4. At each place $w$, for the same $y$ and a compact $\Omega_w \subseteq G(\mathbb{Q}_w)$, there is a compact $D_w$ such that $g^{-1} \gamma_w g \in \Omega_w$ implies $g = c d$ with $c$ as in result 2 and $d \in D_w$.
5. Each $G(\mathbb{Z}_w)$ is compact and closed under inverses.
6. If each $D_w \subseteq G(\mathbb{Q}_w)$ is compact and $D_w \subseteq G(\mathbb{Z}_w)$ for almost all $w$, then $\{g : g_w \in D_w \text{ for all } w\}$ is compact.
7. A family $(c_w)$ with $c_w \in G(\mathbb{Z}_w)$ for almost all $w$ is the family of components of an element of $G(\mathbb{A}^p)$, and an element of $G(\mathbb{A}^p)$ is determined by its components.

*Proof.* Let $S$ be the finite set of the definition of a test function and put $\Omega = \bigcup_{s \in S} K_L s K_L$. It is compact and contains the support of $f$. Call a place $w$ *good* if the image of $\Omega$ lies in $G(\mathbb{Z}_w)$, the conclusion of result 2 holds at $w$, and $G(\mathbb{Z}_w)$ is closed under products. By results 1, 2 and 3, almost all places are good. At a good place put $D_w = G(\mathbb{Z}_w)$; at the other places let $D_w$ be the compact set that result 4 gives for the image of $\Omega$. By result 5 every $D_w$ is compact.

Let $g$ satisfy $g^{-1} \gamma g \in \Omega$. At each place $w$ the element $g_w^{-1} \gamma_w g_w$ lies in the image of $\Omega$, so $g_w = c_w d_w$ with $c_w$ in the centralizer of $\gamma_w$ and $d_w \in D_w$; at good places this is result 2, and at the others it is result 4. By result 1 for $\{g\}$, $g_w$ is integral for almost all $w$; at such a good $w$, $c_w = g_w d_w^{-1}$ is in $G(\mathbb{Z}_w)$ by result 5 and closure under products. By result 7 there is $c \in G(\mathbb{A}^p)$ with components $c_w$, and $c$ commutes with $\gamma$. Then $d = c^{-1} g$ has all its components in the sets $D_w$.

By result 6 the set $D$ of such $d$ is compact. The open sets $d K_L$ for $d \in D$ cover $D$, so finitely many, for $d \in R$, cover it. Now let $f(h^{-1} \gamma h) \neq 0$. Then $h^{-1} \gamma h \in \Omega$, so $h = c d$ as above, and $d = r k$ with $r \in R$ and $k \in K_L$. So $h = c r k$. $\square$

**Lemma 8.23.4 (Cosets at p).** For $f'$ a test function at $p$ and $y_0$ as above, there is a finite set $R' \subseteq G_1$ such that $f'(h^{-1} y_{0,p} h) \neq 0$ implies $h = c r k$ with $c$ commuting with $y_{0,p}$, $r \in R'$ and $k \in K'$.

Lean: `GlobalTheory.FinPtsSep.exists_finset_doubleCoset_cover_of_separable`.

*Proof.* The components of $y_{0,p}$ have separable characteristic polynomials, as the minimal polynomial of $y_0$ is separable of degree $n$. A result at $p$ then gives a finite $S$ such that every $h$ with $h^{-1} y_{0,p} h$ in the support of $f'$ is $c s k$ with $c$ commuting with $y_{0,p}$, $s \in S$ and $k \in K_{\mathrm{HT}}$. As $K'$ is commensurable with $K_{\mathrm{HT}}$, finitely many $t$ give $K_{\mathrm{HT}} = \bigcup t K'$. Take $R' = \{ s t \}$. $\square$

### Points that see one conjugacy class

**Theorem 8.23.5 (Finitely many points for one class).** Let $G$ be a group datum with $a(G) = 1$, and let $v$ be the place where $H_v$ has signature $(1, n - 1)$. Let $f$ be a test function at a level $L$ and $f'$ a test function at $p$. Let $\beta \in C^\times$ with $\beta^* = \beta$, such that $\beta$ is trivialized over $\mathbb{A}^p$ by $(x, t)$ and over $\mathbb{R}$ by some $z$ with $z \beta z^* = 1$. Suppose that for all $y \in \Gamma_\beta$ and $h \in G(\mathbb{A}^p)$ with $f(h^{-1} y^{(p)} h) \neq 0$, if $y$ fixes the line of a vector $z$ with $\operatorname{Re}(z^* H_{v, \beta} z) > 0$, then the minimal polynomial of $y$ is separable of degree $n$. Then for every $y_0 \in \Gamma_\beta$ the set of $q \in \mathrm{Pts}(\beta)$ for which there is $\gamma \in \Gamma_\beta$ such that $\gamma y_0 \gamma^{-1}$ fixes the line of $z_q$ and
$$
f\bigl(g_q^{-1} (\gamma y_0 \gamma^{-1})^{(p)} g_q\bigr) \, f'\bigl(g_{p,q}^{-1} (\gamma y_0 \gamma^{-1})_p \, g_{p,q}\bigr) \neq 0
$$
is finite.

Lean: `GlobalTheory.FinPtsSep.finite_pts_conj_fixL_sep` (also `GlobalTheory.T.orbital_integral_test_function_second`, a second name).

We use the theorem on cosets away from $p$, the lemma on cosets at $p$, and the following results.

### Inputs

1. Class numbers of centralizers. For $y_0$ with separable minimal polynomial of degree $n$ and each $r \in G(\mathbb{A}^p) \times G_1$, there is a finite set $R_r$ such that every $c$ that commutes with $(y_0^{(p)}, y_{0,p})$ satisfies $c r = (y^{(p)}, y_p) \, s \, k$ for some $y \in \Gamma_\beta$ commuting with $y_0$, some $s \in R_r$ and some $k \in K_L \times K'$.
2. Uniqueness of the positive line. Under the hypotheses on $G$, $v$ and $\beta$ of the theorem, if the minimal polynomial of $y_0$ is separable of degree $n$ and $y_0$ fixes the lines of $z$ and $z'$, both of positive norm for $H_{v, \beta}$, then $z' = c z$ for some $c \in \mathbb{C}$.
3. Conjugation. Minimal polynomials are invariant under conjugation, $\psi_v(\gamma)$ preserves positive norm, and if $\gamma y \gamma^{-1}$ fixes the line of $z$, then $y$ fixes the line of $\psi_v(\gamma)^{-1} z$.

*Proof.* If no datum and $\gamma$ satisfy the condition, the set is empty. Otherwise fix such a datum $(b, b_p, z_b)$ and $\gamma_0$. The hypothesis, applied to $\gamma_0 y_0 \gamma_0^{-1}$, and result 3 show that the minimal polynomial of $y_0$ is separable of degree $n$. Put $z_0 = \psi_v(\gamma_0)^{-1} z_b$; by result 3 it has positive norm and $y_0$ fixes its line.

The theorem and the lemma on cosets give finite sets $R_1$ and $R_2$, and result 1 gives a finite set $R_r$ for each $r \in R_1 \times R_2$. Let $\mathcal{F}$ be the union of the $R_r$. We show that each $q$ in the set is the class of $(s, z_0)$ for some $s \in \mathcal{F}$.

Let $q$ be in the set, with representative $(b, b_p, z)$ and element $\gamma$. Then $f\bigl(((\gamma^{-1})^{(p)} b)^{-1} \, y_0^{(p)} \, (\gamma^{-1})^{(p)} b\bigr) \neq 0$, since this argument equals $b^{-1} (\gamma y_0 \gamma^{-1})^{(p)} b$. So $(\gamma^{-1})^{(p)} b = c_1 r_1 k_1$ with $c_1$ commuting with $y_0^{(p)}$, $r_1 \in R_1$ and $k_1 \in K_L$. In the same way $(\gamma^{-1})_p b_p = c_2 r_2 k_2$. By result 1 for $r = (r_1, r_2)$ and $c = (c_1, c_2)$ there are $y$ commuting with $y_0$, $s \in R_r$ and $k_3 \in K_L \times K'$ with $c r = (y^{(p)}, y_p) s k_3$. Hence
$$
(b, b_p) = \bigl((\gamma y)^{(p)}, (\gamma y)_p\bigr) \, s \, k_3 (k_1, k_2).
$$
By result 3, $y_0$ fixes the line of $\psi_v(\gamma)^{-1} z$, and as $y y_0 y^{-1} = y_0$, it also fixes the line of $w = \psi_v(y)^{-1} \psi_v(\gamma)^{-1} z$. Both $z_0$ and $w$ have positive norm, so result 2 gives $w = c z_0$, with $c \neq 0$. So $z = c \, \psi_v(\gamma y) z_0$. With the display, $(b, b_p, z)$ is related to $(s, z_0)$ by the element $\gamma y$, the pair $k_3 (k_1, k_2)$ and the scalar $c$. So $q$ is the class of $(s, z_0)$. $\square$

### Regular support

**Theorem 8.23.6 (Finitely many contributing points).** Let $G$, $v$, $f$, $f'$ and $\beta$ be as in the last theorem, but assume instead of its hypothesis on minimal polynomials that $f(g) \neq 0$ only for regular $g$. Then the set of $q \in \mathrm{Pts}(\beta)$ for which some $y \in \Gamma_\beta$ fixes the line of $z_q$ and
$$
f\bigl(g_q^{-1} y^{(p)} g_q\bigr) \, f'\bigl(g_{p,q}^{-1} y_p \, g_{p,q}\bigr) \neq 0
$$
is finite.

Lean: `GlobalTheory.LKCx.CxReg.finite_pts_reg`.

We use the last theorem and the following results, under the hypotheses of the theorem.

### Inputs

1. Regular elements are separable. If $y \in \Gamma_\beta$ fixes the line of a vector of positive norm and $h^{-1} y^{(p)} h$ is regular for some $h$, then the minimal polynomial of $y$ is separable of degree $n$.
2. Finitely many polynomials. The minimal polynomials of the elements $y$ that fix the line of $z_b$ for some datum $(b, b_p, z_b)$ with $f(b^{-1} y^{(p)} b) f'(b_p^{-1} y_p b_p) \neq 0$ form a finite set.
3. Finitely many classes for one polynomial. Under the hypothesis on minimal polynomials of the last theorem, for each polynomial $P$ there is a finite set $Y(P) \subseteq \Gamma_\beta$ such that every element $y$ as in result 2 with minimal polynomial $P$ is $\gamma y_0 \gamma^{-1}$ for some $y_0 \in Y(P)$ and $\gamma \in \Gamma_\beta$.

*Proof.* Let $f(h^{-1} y^{(p)} h) \neq 0$ with $y$ fixing a line of positive norm. Then $h^{-1} y^{(p)} h$ is regular by hypothesis, so result 1 shows that the minimal polynomial of $y$ is separable of degree $n$. So the hypothesis of the last theorem holds. Choose the sets $Y(P)$ of result 3 for all $P$, let $\mathcal{P}$ be the finite set of result 2, and for $y_0 \in Y(P)$ let $X(y_0)$ be the finite set of the last theorem. Our set lies in the finite union of the $X(y_0)$ over $P \in \mathcal{P}$ and $y_0 \in Y(P)$.

Indeed, let $q$ be in our set, with element $y$. The datum $(g_q, g_{p,q}, z_q)$ shows that the minimal polynomial $P$ of $y$ is in $\mathcal{P}$, and result 3 gives $y_0 \in Y(P)$ and $\gamma$ with $y = \gamma y_0 \gamma^{-1}$. So $q \in X(y_0)$. $\square$

**Remark 8.23.7 (Formalization).** The theorem on cosets is in [FiniteCosetsAndFixedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteCosetsAndFixedPoints.lean#L16), the lemma at [line 99](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteCosetsAndFixedPoints.lean#L99), and the theorem for one class at [line 160](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteCosetsAndFixedPoints.lean#L160). The theorem for one class assumes $a(G) = 1$ but does not use it. Its second name is a wrapper in [OrbitalIntegralTestFunctionSecond.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OrbitalIntegralTestFunctionSecond.lean#L7), a file that imports Mathlib twice. The theorem on regular support is in [ClassSummandEqTermOfAOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassSummandEqTermOfAOne.lean#L40), and the step from regular to separable at [line 33](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassSummandEqTermOfAOne.lean#L33). The representative of a class is picked by choice. The set $G(\mathbb{Z}_w)$ depends on a chosen basis of $C$, hence result 3 of the first theorem. We have not unfolded the group $G_1$, its subgroup $K_{\mathrm{HT}}$, the automorphism $\sigma$ or the map $y \mapsto y_p$, and their descriptions in words are ours. We read the statements of results 1 to 7 of the first theorem, results 1 to 3 of the other two, and of the two results in the proof of the lemma, not their proofs.
