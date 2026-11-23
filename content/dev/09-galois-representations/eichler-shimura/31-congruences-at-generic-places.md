---
title: Congruences at generic places
decls:
  - UpperTheory.Gal.Int.Cong.congUWG_of
  - UpperTheory.Gal.Int.Cong.congFinG_of_step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Congruences at generic places

The limit theorem of Section 25 needs a congruence statement: the Hecke eigenvalues of a space $U$ on $\mathrm{U}(a)$ are $\ell$-adic limits of those of spaces $U'$ with a prescribed type at $w_0$, a lacunary weight at $v'$ and generic Satake parameters at a given finite set of places. This section proves such a statement from a *step statement*, which changes the weight at $v'$ and the type at $w_0$ for one family of Hecke operators. Genericity comes from the density of generic forms (Section 28). The results are [the congruence theorem](/entry/cong-uwg-of/) and [its case for the parameters of Section 24](/entry/cong-fin-g-of-step/). The step statement is proved in Section 32 from the weight change theorem of Section 30.

We keep the notation of Sections 25 and 28 to 30.

### Types, genericity and approximation

**Definition 3.32.1 (Type at $w_0$).** An automorphic space $U$ has *type $\mathrm{Ty}_\ell$ at $w_0$* if there are $m \geq 0$, an open compact subgroup $J \subset \mathrm{GL}_a(E_{w_0})$ without elements of finite order other than $1$, a homomorphism $\theta$ from $J$ onto $\mathbb{Z}/\ell^m$ and a character $\chi \neq 1$ of $\mathbb{Z}/\ell^m$ such that: every smooth irreducible $\sigma$ of $\mathrm{GL}_a(E_{w_0})$ with a vector $v \neq 0$ on which $J$ acts by $\chi \circ \theta$ is cuspidal; and some $\varphi \in U$, $\varphi \neq 0$, has $R(x) \varphi = \chi(\theta(c_{w_0}(x))) \varphi$ for every $x \in G_{w_0}$ with $c_{w_0}(x) \in J$.

Lean: `GlobalTheory.CongW.TyEll`.

So the local component of $U$ at $w_0$ is supercuspidal.

**Definition 3.32.2 (Generic polynomial).** For $a \geq 1$, let $D_a \in \mathbb{Z}[X_1, \dots, X_a]$ be the product of the factors $X_i^k - X_j^k$ for $i \neq j$ and $1 \leq k \leq a$; the factors $X_i X_k - X_j^2$ for $j \notin \{i, k\}$; and the factors $X^m - X_1 \cdots X_a$ for $m = (m_1, \dots, m_a)$ with $0 \leq m_i \leq a$, $\sum m_i = a$ and $m \neq (1, \dots, 1)$. For a family $D = (D_a)$, a Satake parameter $B$ is *$D$-generic* if $D_a(\alpha) \neq 0$ for every ordering $\alpha = (\alpha_1, \dots, \alpha_a)$ of $B$, and $U$ is *$D$-generic at $w$* if each Satake parameter of $U$ at $w$ is $D$-generic.

Lean: `GlobalTheory.CongL.DGen` (also `GlobalTheory.CongW.GenOf`, `GlobalTheory.CongL.GenAtU`).

A generic parameter has no two entries with equal $k$-th powers for $k \leq a$, no entry whose square is the product of two others, and no monomial relation of degree $a$ with the product of all entries.

**Definition 3.32.3 (Lacunary weight).** A space $U'$ has a *lacunary weight relative to $U$* at $v'$ if $U'$ has the weights of $U$ at each $\tau$ all of whose places lie apart from $w_0$ and $v'$, and there is $\tau_0$ over $v'$ such that every weight of $U'$ at $\tau_0$ satisfies the gap condition.

Lean: `GlobalTheory.CongL.WtLac` (also `GlobalTheory.CongL.SameWtOff`).

**Lemma 3.32.4 (Polynomial approximation).** Let $k$ be a normed field, $\theta \in k^J$ and $S, T \subset k^J$.

1. If $\theta$ is polynomially approximated by $S$ and $i : J_1 \to J$, then $\theta \circ i$ is polynomially approximated by $\{\eta \circ i : \eta \in S\}$.
2. Let $Q \in \mathbb{Z}[X_j : j \in J]$. If $\theta$ is polynomially approximated by $S$ and each $\eta \in S$ has $Q(\eta) \neq 0$ and is polynomially approximated by $T$, then $\theta$ is polynomially approximated by $\{\eta \in T : Q(\eta) \neq 0\}$.

Lean: `UpperTheory.Gal.Gen.restrict_holds` (also `UpperTheory.Gal.Gen.combine_holds`, `UpperTheory.Gal.Gen.Restrict`, `UpperTheory.Gal.Gen.Combine`).

*Proof.* 1. For $P \in \mathbb{Z}[X_{j_1} : j_1 \in J_1]$, let $P'$ be $P$ with each $X_{j_1}$ renamed $X_{i(j_1)}$. Then $P(\eta \circ i) = P'(\eta)$, and an approximation of $P'(\theta)$ by $\sum c_\eta P'(\eta)$ is one of $P(\theta \circ i)$.

2. First let $\eta$ have $Q(\eta) \neq 0$ and be approximated by $T$. Given $\varepsilon$, choose $s \subset T$ and $c_\xi$ with $\lVert (PQ)(\eta) - \sum c_\xi (PQ)(\xi) \rVert \leq \varepsilon \lVert Q(\eta) \rVert$ for all $P$. Put $c'_\xi = c_\xi Q(\xi) / Q(\eta)$; the terms with $Q(\xi) = 0$ vanish, and dividing by $Q(\eta)$ gives $\lVert P(\eta) - \sum c'_\xi P(\xi) \rVert \leq \varepsilon$. So $\eta$ is approximated by $T_Q = \{\xi \in T : Q(\xi) \neq 0\}$. Now approximate $\theta$ by $\sum_{\eta \in s} c_\eta \eta$ to $\varepsilon / 2$, and each $\eta$ by elements of $T_Q$ to $\varepsilon / (2 (M + 1))$ with $M = \sum \lVert c_\eta \rVert$. The triangle inequality gives an approximation of $\theta$ by $T_Q$ to $\varepsilon$. $\square$

**Lemma 3.32.5 (Finite fields of eigenvalues).** Let $K$ be a level away from $w_0$ and $(t_j)$ functions whose supports lie in $G_f$ and whose values are rational. If the $t_j$ act on $K$-fixed vectors by $\eta$ and $U$ is of type $(\lambda, K)$, then all $\iota^{-1} \eta_j(U)$ lie in one finite extension of $\mathbb{Q}_\ell$.

Lean: `GlobalTheory.Cong.finU_holds` (also `GlobalTheory.Cong.FinU`).

*Proof.* Let $\varphi \in U$ be nonzero and fixed by $K$. For an automorphism $\sigma$ of $\mathbb{C}$, the conjugate $\varphi^\sigma$ is an automorphic form, and since the $t_j$ are rational, $R(t_j) \varphi^\sigma = \sigma(\eta_j(U)) \varphi^\sigma$. The conjugates of $\varphi$ span a finite dimensional space. Eigenvectors for distinct systems of eigenvalues are linearly independent, so the orbit of $(\eta_j(U))_j$ under the automorphisms of $\mathbb{C}$ is finite. A family with a finite orbit has $\iota^{-1}$ in a finite extension of $\mathbb{Q}_\ell$. $\square$

**Proposition 3.32.6 (Inputs).** Let $U$ be automorphic off $T$, and let $w_0, v'$ be split places that are apart.

1. *Levels.* There are a level $K$ away from $w_0$, a level $\kappa = (\kappa_w)$ in the sense of Section 25 and an open subgroup $K_v \subset \mathrm{GL}_a(E_{v'})$ such that: $U$ has a nonzero vector fixed by $\{x \in K : c_{v'}(x) \in K_v\}$; $\kappa_{v'} = \mathrm{GL}_a(\mathcal{O}_{v'})$; $\kappa_w$ is open and compact for split $w$ apart from $w_0$; $\kappa_w = \mathrm{GL}_a(\mathcal{O}_w)$ for split $w$ apart from $v'$ where $U$ has a Satake parameter; $K$ contains each $x \in G_w$ with $c_w(x) \in \mathrm{GL}_a(\mathcal{O}_w)$, for $w$ non-split and not in $T$; and for split $w$ apart from $w_0$ and $x \in G_w$, $x \in K$ if and only if $c_w(x) \in \kappa_w$.
2. *Approximation by eigenvalues.* Let $K \subset G_f$, and let forms with a property $P$ approximate the forms of weight $W_\lambda$ fixed by $K$. Let $(t_j)$ be framed for $W_\lambda$ and act on $K$-fixed vectors by $\eta$. Then for $U$ of type $(\lambda, K)$, the family $(\iota^{-1} \eta_j(U))_j$ is polynomially approximated by the families $(\iota^{-1} \eta_j(U'))_j$ for the $U'$ of type $(\lambda, K)$ with $P(U')$.
3. *Frames.* A family of $\lambda$-integral functions is framed for $W_\lambda$.
4. *Local operators.* Let $w$ be split, $\kappa_w$ open and compact, and $f$ a function of finite support on $\mathrm{GL}_a(E_w)$ that acts on the $\kappa_w$-fixed vectors of each $\sigma$ by $z(\sigma)$. There are $t$ supported in $G_w$, with $t(g) = f(c_w(g))$, and numbers $e(U)$ such that $R(t) \varphi = e(U) \varphi$ for $\varphi \in U$ fixed by $G_w \cap c_w^{-1}(\kappa_w)$, and $e(U) = z(\sigma)$ for the component $\sigma$ of $U$ at $w$ if $U$ has a nonzero such vector.
5. *Fixed vectors.* If $U$ has a nonzero vector fixed by $G_w \cap c_w^{-1}(\kappa_w)$, each local component of $U$ at $w$ has a nonzero $\kappa_w$-fixed vector; and if $\kappa_w = \mathrm{GL}_a(\mathcal{O}_w)$, $U$ has a Satake parameter at $w$.
6. *Power sums.* For split $w$ and $n \in \mathbb{Z}$, there is $t$ supported in $G_w$ that acts by $p_n(U, w)$ on the vectors of $U$ fixed by $G_w \cap c_w^{-1}(\mathrm{GL}_a(\mathcal{O}_w))$.
7. *Test operators.* Let $K \subset G_f$ and $w$ be split, with $x \in K$ if and only if $c_w(x) \in \mathrm{GL}_a(\mathcal{O}_w)$ for $x \in G_w$. For $\Phi \in \mathbb{C}[X_1, \dots, X_a]$ there are $t$ supported in $G_w$ and numbers $e(U)$ such that $t$ acts on $K$-fixed vectors by $e$, and if $U$ has a nonzero $K$-fixed vector, $e(U) \neq 0$ if and only if $U$ is $\Phi$-generic at $w$.
8. *Scaling.* For $t$ supported in $G_f$ there is $c \neq 0$ with $c t$ both $\lambda$-integral and locally $\lambda$-integral.
9. *Embeddings.* For $v' \mid \ell$ some $\tau_0$ lies over $v'$.

Lean: `UpperTheory.Gal.Int.Cong.exists_level` (also `UpperTheory.Gal.Gen.toPolyX_holds`, `UpperTheory.Gal.Gen.frameW_holds`, `UpperTheory.Gal.Int.Cong.exists_op`, `UpperTheory.Gal.Int.Cong.fixed_ne_bot`, `UpperTheory.Gal.Int.Cong.exists_satU`, `UpperTheory.Gal.Int.Cong.exists_powOp`, `UpperTheory.Gal.Int.Cong.exists_testOp`, `UpperTheory.Gal.Int.Cong.exists_scale`, `UpperTheory.Gal.Int.Cong.exists_overPl`).

These facts are proved elsewhere in the development, and we take them as given.

### The step statement and the congruence theorem

**Definition 3.32.7 (Step statement).** The *step statement* says: let $a \geq 1$, let $w_0, v' \mid \ell$ be split and apart, $K$ a level away from $w_0$ that contains each $x \in G_{v'}$ with $c_{v'}(x) \in \mathrm{GL}_a(\mathcal{O}_{v'})$, $K_v \subset \mathrm{GL}_a(E_{v'})$ open, and $K' = \{x \in K : c_{v'}(x) \in K_v\}$. Let $(t_j)$ be $\lambda$-integral and locally $\lambda$-integral, with supports in the elements whose components at the places not apart from $w_0$, and at those not apart from $v'$, are trivial, acting on $K'$-fixed vectors by $\eta$. Let $\tau_0$ lie over $v'$. Then for each $U$ of type $(\lambda, K')$, $(\iota^{-1} \eta_j(U))_j$ is polynomially approximated by the $(\iota^{-1} \eta_j(U'))_j$ for the $U'$ for which there is $\mu$ with: $\mu_\tau = \lambda_\tau$ unless $\tau$ lies over the pair of $v'$; $\mu_{\tau_0}$ satisfies the gap condition; $U'$ is of type $(\mu, K)$; and $U'$ has type $\mathrm{Ty}_\ell$ at $w_0$.

Lean: `UpperTheory.Gal.Int.Cong.StepSt`.

**Definition 3.32.8 (Congruence statement at generic places).** Let $\mathrm{Ty}$, $\mathrm{Gen}$, $\mathrm{Wt}$ be as in Section 25. The *congruence statement at generic places* is the congruence statement of Section 25 with these changes: there is no condition $\mathrm{Rk}$ on $a \geq 1$; in clause 3, $W$ need not lie above $\ell$; and the $U'$ need be generic only at $Z$.

Lean: `UpperTheory.Gal.Int.Cong.CongUWG` (also `UpperTheory.Gal.Int.Cong.CongFinG`).

**Theorem 3.32.9 (Congruences at generic places).** Assume the step statement. Let $D = (D_a)$ be integer polynomials with $D_a \neq 0$ for all $a$. Then the congruence statement at generic places holds for the type $\mathrm{Ty}_\ell$, $D$-genericity and the lacunary weight.

Lean: `UpperTheory.Gal.Int.Cong.congUWG_of` (also `UpperTheory.Gal.Int.Cong.isLevelAway_inf`, `UpperTheory.Gal.Int.Cong.apart_of_not_mem`, `UpperTheory.Gal.Int.Cong.not_apart_of_overPair`).

*Proof.* Let $a, T, U, w_0, v'$ be given, with $w_0, v' \mid \ell$.

*Levels.* Take $K, \kappa, K_v$ from item 1, let $\lambda$ be the weight family of $U$, and $K' = \{x \in K : c_{v'}(x) \in K_v\}$. Since $c_{v'}$ is continuous and $K_v$ is open and closed, $K'$ is a level away from $w_0$, and $U$ is of type $(\lambda, K')$. For split $w$ apart from $w_0$ and $v'$ and $x \in G_w$, $c_{v'}(x) = 1$, so $x \in K'$ if and only if $c_w(x) \in \kappa_w$. Hence a space with a nonzero $K'$-fixed vector has a nonzero vector fixed by $G_w \cap c_w^{-1}(\kappa_w)$, and by item 5 it has level $\kappa$ off $w_0$ and $v'$. With item 1 this gives clauses 1 and 2. It also shows that $K'$ satisfies the hypothesis of item 7 at each split $w$ apart from $w_0, v'$ where $U$ has a Satake parameter.

*Operators.* Let $Z, W$ be given. For $p = (w, n) \in W \times \mathbb{Z}$, item 6 gives $t_p$ and item 8 a constant $c_p \neq 0$. Put $c(w, n) = c_p$ for $w \in W$ and $c(w, n) = 1$ otherwise. Let $\Phi = D_a$. For $z \in Z$, item 7 gives $t_z, e_z$, and item 8 a constant $c_z \neq 0$. Let $O = (w_j, f_j, z_j)_{j \in J}$ be local operators for $\kappa$ and $\theta$ the eigen-system of $U$. Each $w_j \nmid \ell$, so $w_j$ is apart from $w_0$ and $v'$. Item 4 gives $t_j, e_j$. By the level step, $t_j$ acts on $K'$-fixed vectors by $e_j$, and for each $U'$ with a nonzero $K'$-fixed vector, $(\iota^{-1} e_j(U'))_j$ is the eigen-system of $U'$; since local components are unique, $\theta_j = \iota^{-1} e_j(U)$. If all $f_j$ are rational, so are the $t_j$, and the lemma on finite fields gives clause 4.

*Approximation.* The family $t = (t_j, c_p t_p, c_z t_z)$ on $(J \sqcup W \times \mathbb{Z}) \sqcup Z$ acts on $K'$-fixed vectors by $\eta(U') = (e_j(U'), c_p\, p_n(U', w), c_z e_z(U'))$. Each member is supported in some $G_w$ with $w$ apart from $w_0$ and $v'$, so its support has trivial components at the places not apart from $w_0$ or from $v'$. Each member is $\lambda$-integral and locally $\lambda$-integral: for $t_j$, an element $g$ of the support has $c_u(g) = 1$ at $u \mid \ell$, so $d = 0$ and $\lVert \iota^{-1} f_j \rVert \leq 1$ suffice; for the others, by the choice of $c_p, c_z$. The set $Z$ with $\Phi$ is genericity data for $(w_0, K')$, since $D_a \neq 0$. By the density theorem of Section 28 and items 2 and 3, $\iota^{-1} \eta(U)$ is polynomially approximated by the $\iota^{-1} \eta(U_1)$ for the $U_1$ of type $(\lambda, K')$ that are generic at $Z$.

*Combination.* Let $Q = \prod_{z \in Z} X_z$. For $U_1$ with a nonzero $K'$-fixed vector, $Q(\iota^{-1} \eta(U_1)) = \iota^{-1} \prod_z c_z e_z(U_1)$, which is nonzero if and only if $U_1$ is $\Phi$-generic at all $z \in Z$. Take $\tau_0$ by item 9. Item 1 gives that $K$ contains the $x \in G_{v'}$ with $c_{v'}(x) \in \mathrm{GL}_a(\mathcal{O}_{v'})$. So the step statement applies to each $U_1$ above. Part 2 of the approximation lemma, then part 1 for $J \sqcup W \times \mathbb{Z}$, show that $(\theta, (\iota^{-1}(c(w, n)\, p_n(U, w))))$ is polynomially approximated by the same families for the $U'$ of type $(\mu, K)$ given by the step statement, with type $\mathrm{Ty}_\ell$ at $w_0$ and $Q(\iota^{-1} \eta(U')) \neq 0$.

*The conditions on $U'$.* A nonzero $K$-fixed $\varphi \in U'$ is $K'$-fixed. So $U'$ is unramified at the non-split places off $T$ (item 1), has level $\kappa$ off $w_0$ and $v'$, has a Satake parameter at $v'$ (items 1 and 5, as $\kappa_{v'} = \mathrm{GL}_a(\mathcal{O}_{v'})$), and its eigen-system is $\iota^{-1} e_j(U')$. If $\mu_\tau \neq \lambda_\tau$, then $\tau$ lies over $v'$ or its conjugate, a place not apart from $v'$. So at each $\tau$ all of whose places are apart from $w_0$ and $v'$, $U'$ has the weight $\lambda_\tau$ of $U$. By uniqueness of weights, every weight of $U'$ at $\tau_0$ is $\mu_{\tau_0}$ and satisfies the gap condition. So $U'$ has a lacunary weight relative to $U$. Finally $Q \neq 0$ at $U'$ gives $D_a(\alpha) \neq 0$ for each ordering $\alpha$ of each Satake parameter at $z \in Z$. $\square$

**Corollary 3.32.10 (Congruences for the parameters of Section 24).** The step statement implies the congruence statement at generic places for $\mathrm{Ty}_\ell$, $(D_a)$-genericity with the generic polynomials, and the lacunary weight.

Lean: `UpperTheory.Gal.Int.Cong.congFinG_of_step` (also `UpperTheory.Gal.Int.Cong.dGen_ne_zero`).

*Proof.* This is the theorem for $D_a$ the generic polynomial, which is nonzero, with the lemma on finite fields. $\square$

**Remark 3.32.11 (Formalization).** The theorem is in [NotApartOfOverPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L111), the step statement at line 35 and the congruence statement at generic places in [ApartOfNotMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/ApartOfNotMem.lean#L12). Odd points. The statement at generic places does not ask that $W$ lie above $\ell$, unlike clause 3 of Section 25; the finiteness hypothesis is used only for clause 4. The name `congFinG_of_step` refers to the step statement, not to [the one step theorem](/entry/step-holds/) of Section 28. We read `combine_pf`, `restrict_pf`, `finU_holds`, `dGen_ne_zero` and `isLevelAway_inf` in full, and only the statements of the items of the proposition; we did not open `toPolyX_pf`, `frameW_pf`, the proof of `exists_level`, or the proofs in ExistsTestOp.lean, and we did not unfold `HasWeightAt` or `infOfWeight`.
