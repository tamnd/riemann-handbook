---
title: Finiteness of definite classes
decls:
  - GlobalTheory.LKDefFin.finite_of_compact
  - GlobalTheory.LKDefFin.finite_classes_fixed_gamma
  - GlobalTheory.LKDefFin.finite_classes_of_pol
  - GlobalTheory.T.finite_definitePair_classes_fixed_minpoly_degree_one
  - GlobalTheory.LKDef.FinPairs.finite_classes_irr_term_ne_zero
  - GlobalTheory.T.bi_invariant_conjugacy_classes_finite
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness of definite classes

This section proves that only finitely many classes of definite pairs with irreducible polynomial have a nonzero term. The proof has three layers. First, for fixed $\gamma$ and $c$, the classes whose trivializations meet a compact set are finite. The ratios $\beta_P \beta_1^{-1}$ are local norms up to scalars by the last section, and a global finiteness result for such elements finishes the step. Second, conjugation moves every pair with a given polynomial to one fixed $\gamma$, and $c$ is then determined up to sign. Third, only finitely many polynomials occur. The result is used in the [regrouping of the trace](/entry/regroup/), where it makes a sum over classes a finite sum.

We keep the notation of the first two sections. In this section $K^p$ is a level, $f \colon G(\mathbb{A}^p) \to \mathbb{C}$ is a test function for $(\mathrm{id}, K^p, K^p)$, $K' \subseteq G_1$ is a subgroup, and $\varphi \colon G_1 \to \mathbb{C}$ is a test function for $(\sigma, K_1, K')$. We write $T(P)$ for $T(P; K^p, f, 1, K', \varphi)$. For a trivialization $(x, t)$ of a definite pair $P$, the *image* of $(x, t)$ is $(x \gamma x^{-1}, c) \in G(\mathbb{A}^p)$.

### Inputs

**Theorem 6.3.1 (Classes modulo rational norms).** Let $L$ be a number field and $c \colon L \to L$ a $\mathbb{Q}$-algebra map with $c \circ c = \mathrm{id}$. Let $S$ be a finite set of primes and $X \subseteq L$. Assume that each $a \in X$ has $a \neq 0$, $c(a) = a$, and for each prime $\ell \notin S$ some $r \in \mathbb{Q}_\ell^\times$ and $y \in (\mathbb{Q}_\ell \otimes L)^\times$ with $1 \otimes a = r\, y\, c(y)$. Then there is a finite set $R \subseteq L$ such that each $a \in X$ is $a = q\, b\, z\, c(z)$ for some $b \in R$, $q \in \mathbb{Q}^\times$ and $z \in L^\times$.

Lean: `GlobalTheory.FixedNormCls.finite_classes_mod_rat_norms`.

*Proof.* This is proved in the development by an argument on the divisors of $L$; we take it as an input. $\square$

**Theorem 6.3.2 (Skolem and Noether).** Let $\gamma, \gamma' \in C^\times$ have the same minimal polynomial over $F$, and let it be irreducible. Then $\gamma = y \gamma' y^{-1}$ for some $y \in C^\times$.

Lean: `GlobalTheory.LKCx.units_conj_of_minpoly_eq_of_irreducible`.

*Proof.* This is the Skolem and Noether theorem for the two maps of the field $F[X]/(P_\gamma)$ into $C$ that send $X$ to $\gamma$ and to $\gamma'$. The development derives it from a conjugacy result for such maps; we take it as an input. $\square$

**Theorem 6.3.3 (Finitely many polynomials).** Assume $a = 1$, that $f(k g k') = f(g)$ for $k, k' \in K^p$, and that $\varphi(k g k') = \varphi(g)$ for $k, k' \in K'$. Then the set of polynomials $P_\gamma$ of definite pairs $P$ with $P_\gamma$ irreducible and $T(P) \neq 0$ is finite.

Lean: `GlobalTheory.T.finite_minpoly_definitePairs_term_ne_zero` (also `GlobalTheory.LKDef.FinPol.finite_pol_term_ne_zero`).

*Proof.* We outline the argument. There is an integer $N > 0$ such that $N \gamma$ and $N \gamma^{-1}$ are integral over $\mathbb{Z}$ for every definite pair with irreducible polynomial and nonzero term. This uses the compact support of $f$, a bound on the denominators of characteristic polynomials on compact sets away from $p$, and a bound at $p$ from the test function $\varphi$. Each eigenvalue $w$ of $\psi_v(\gamma)$ has $|w|^2 = c$. These two facts leave only finitely many monic polynomials of degree $n$. $\square$

### Lemmas on pairs

**Lemma 6.3.4 (Conjugate pair).** Let $P$ be a definite pair and $y \in C^\times$. There is a definite pair $P'$ with $P \sim P'$, $\gamma_{P'} = y \gamma_P y^{-1}$ and $c_{P'} = c_P$, such that for each trivialization $(x, t)$ of $P$ there is $x'$ with $(x', t)$ a trivialization of $P'$ of the same image.

Lean: `GlobalTheory.LKDefFin.exists_conj`.

*Proof.* Take $\beta_{P'} = y \beta_P y^*$ and $\gamma_{P'} = y \gamma_P y^{-1}$, related to $P$ by $y$ and $s = 1$. Conditions 1 to 4 hold for $P'$: the first three by direct computation, and the fourth because $\psi_v(y^*) = H_v^{-1} \psi_v(y)^\dagger H_v$ turns the form of $\beta_{P'}^{-1}$ at $u$ into the form of $\beta_P^{-1}$ at $\psi_v(y)^{-1} u$. Take $x' = x y^{-1}$. Then $x' \beta_{P'} x'^* = x \beta_P x^* = t$ and $x' \gamma_{P'} x'^{-1} = x \gamma_P x^{-1}$. $\square$

**Lemma 6.3.5 (The factor up to sign).** For a definite pair $P$, $N(\gamma)\, N(\gamma^*) = c^d$, where $N$ is the norm from $C$ to $\mathbb{Q}$ and $d = \dim_{\mathbb{Q}} C$. Hence if $\gamma_{P'} = \gamma_P$, then $c_{P'} = c_P$ or $c_{P'} = -c_P$.

Lean: `GlobalTheory.LKDefFin.c_eq_or_eq_neg` (also `GlobalTheory.LKDefFin.norm_sim`, the norm identity).

*Proof.* Apply $N$ to $\gamma \beta \gamma^* = c \beta$ and cancel $N(\beta) \neq 0$. If $\gamma_{P'} = \gamma_P$, then $c_{P'}^d = c_P^d$ with $d > 0$, so $c_{P'} = \pm c_P$. $\square$

**Lemma 6.3.6 (A witness of a nonzero term).** If $T(P; K^p, f, r, K, \varphi) \neq 0$ for some subgroup $K^p$, then there are a trivialization $(x, t)$ of $P$ and $g \in G(\mathbb{A}^p)$ with $f(g^{-1} (x \gamma x^{-1}, c)\, g) \neq 0$.

Lean: `GlobalTheory.LKDefFin.exists_ne_zero_of_term_ne_zero`.

*Proof.* Since the term is not $0$, it is the point sum for the fixed trivialization, and the point sum has a nonzero summand. That summand has the factor $f(g^{-1} (x \gamma x^{-1}, c)\, g)$, where $g$ is the first coordinate of the representative of a double coset. $\square$

**Lemma 6.3.7 (Change of trivialization).** Let $(x, t)$ be a trivialization of $P$ and $g = (g_1, g_2) \in G(\mathbb{A}^p)$. Then $(g_1^{-1} x, t g_2^{-1})$ is a trivialization of $P$, and its image is $g^{-1} (x \gamma x^{-1}, c)\, g$.

Lean: `GlobalTheory.LKDefFin.exists_triv_toAf_eq_conj`.

*Proof.* From $g_1 g_1^* = g_2$ we get $g_1^{-1} (g_1^*)^{-1} = g_2^{-1}$, so $(g_1^{-1} x) \beta (g_1^{-1} x)^* = g_1^{-1} t (g_1^*)^{-1} = t g_2^{-1}$. The first coordinate of the image is $g_1^{-1} x \gamma x^{-1} g_1$, and the second is $c = g_2^{-1} c\, g_2$. $\square$

**Lemma 6.3.8 (The ratio).** Let $P, Q$ be definite pairs with $\gamma_P = \gamma_Q$ and $c_P = c_Q$, and let $\alpha = \beta_P \beta_Q^{-1}$. Then $\alpha$ commutes with $\gamma_Q$ and $\beta_Q \alpha^* \beta_Q^{-1} = \alpha$.

Lean: `GlobalTheory.LKDefFin.quot_commute_and_fixed`.

*Proof.* The two similitude equations give $\alpha \gamma_Q \beta_Q \gamma_Q^* = c \beta_P = \gamma_Q \alpha \beta_Q \gamma_Q^*$; cancel $\beta_Q \gamma_Q^*$. Next, $\alpha^* = \beta_Q^{-1} \beta_P$, since both forms are symmetric, so $\beta_Q \alpha^* \beta_Q^{-1} = \alpha$. $\square$

**Lemma 6.3.9 (Related by a ratio).** Let $P, Q, P_1$ be definite pairs with $\gamma_P = \gamma_Q = \gamma_1$. Let $y \in C^\times$ commute with $\gamma_1$ and with $\beta_P \beta_1^{-1}$, and let $s \in \mathbb{Q}$, $s > 0$, with
$$\beta_Q \beta_1^{-1} = s\, (\beta_P \beta_1^{-1})\, y\, \beta_1 y^* \beta_1^{-1}.$$
Then $P \sim Q$.

Lean: `GlobalTheory.LKDefFin.rel_of_ratio`.

*Proof.* Multiply on the right by $\beta_1$: $\beta_Q = s\, \beta_P \beta_1^{-1} y \beta_1 y^* = s\, y \beta_P y^*$, since $y$ commutes with $\beta_P \beta_1^{-1}$. Also $\gamma_Q = y \gamma_P y^{-1}$, since $y$ commutes with $\gamma_1$. $\square$

**Lemma 6.3.10 (Compact support).** There is a compact $\Omega \subseteq G(\mathbb{A}^p)$ with $f(g) \neq 0 \Rightarrow g \in \Omega$.

Lean: `GlobalTheory.LKDefFin.supp_compact`.

*Proof.* The support of $f$ lies in a finite union of double cosets $K^p s K^p$, and each is the image of the compact set $K^p \times K^p$ under $(k, k') \mapsto k s k'$. $\square$

### Finite sets of classes

**Theorem 6.3.11 (Classes in a compact set).** Let $\Omega \subseteq G(\mathbb{A}^p)$ be compact, $\gamma_0 \in C^\times$ with $P_{\gamma_0}$ irreducible, and $c_0 \in \mathbb{Q}^\times$. Then there are only finitely many classes $[P]$ of definite pairs $P$ with $\gamma_P = \gamma_0$, $c_P = c_0$, and a trivialization whose image lies in $\Omega$.

Lean: `GlobalTheory.LKDefFin.finite_of_compact`.

*Proof.* Let $Y$ be the set of such pairs. If $Y$ is empty there is nothing to prove, so fix $P_1 \in Y$. The theorem on the centralizer field for $(\beta_1, \gamma_0, c_0)$ gives $L$, $\iota$ and $c$ with $c \circ c = \mathrm{id}$. The theorem on ratios gives a finite set $S$ of primes. For $P \in Y$, the lemma on the ratio shows that $\beta_P \beta_1^{-1}$ commutes with $\gamma_0$, so $\beta_P \beta_1^{-1} = \iota(a_P)$ for some $a_P \in L$. Let $X$ be the set of these $a_P$. Each $a_P$ is not $0$, since $\beta_P \beta_1^{-1}$ is a unit. It is fixed by $c$, by the second part of the lemma on the ratio and the injectivity of $\iota$. It satisfies the local condition outside $S$, by the theorem on ratios. The theorem on classes modulo rational norms gives a finite $R \subseteq L$.

For $b \in R$ and a sign $\epsilon \in \{+, -\}$, choose, if possible, $P_{b, \epsilon} \in Y$ with $a_{P_{b,\epsilon}} = q' b z' c(z')$, $q' \in \mathbb{Q}^\times$ of sign $\epsilon$, $z' \in L^\times$. We show that each $P \in Y$ is related to one of these pairs, so there are at most $2|R|$ classes. Write $a_P = q b z c(z)$ with $b \in R$, and let $\epsilon$ be the sign of $q$. Then $P' = P_{b, \epsilon}$ exists. Let $w = z / z'$ and $y = \iota(w)$. Then $a_P = (q / q')\, a_{P'}\, w\, c(w)$ and $q / q' > 0$. The unit $y$ commutes with $\gamma_0$ and with $\iota(a_{P'})$, since $L$ is commutative. Apply $\iota$:
$$\beta_P \beta_1^{-1} = \tfrac{q}{q'}\, (\beta_{P'} \beta_1^{-1})\, y\, \beta_1 y^* \beta_1^{-1}.$$
The lemma on pairs related by a ratio gives $P' \sim P$. $\square$

**Theorem 6.3.12 (Classes for fixed $\gamma$).** Let $\gamma_0 \in C^\times$ with $P_{\gamma_0}$ irreducible and $c_0 \in \mathbb{Q}^\times$. Then there are only finitely many classes $[P]$ of definite pairs $P$ with $\gamma_P = \gamma_0$ and $c_P = c_0$ such that $f(g^{-1} (x \gamma_0 x^{-1}, c_0)\, g) \neq 0$ for some trivialization $(x, t)$ of $P$ and some $g \in G(\mathbb{A}^p)$.

Lean: `GlobalTheory.LKDefFin.finite_classes_fixed_gamma`.

*Proof.* Take $\Omega$ from the lemma on compact support. By the lemma on change of trivialization, $g^{-1} (x \gamma_0 x^{-1}, c_0)\, g$ is the image of a trivialization of $P$, and it lies in $\Omega$. The theorem on classes in a compact set applies. $\square$

**Theorem 6.3.13 (Classes for a fixed polynomial).** Assume $a = 1$, that $f(k g k') = f(g)$ for $k, k' \in K^p$, and that $\varphi(k g k') = \varphi(g)$ for $k, k' \in K'$. Let $P_0 \in F[X]$. Then there are only finitely many classes whose representative $Q$ has $P_{\gamma_Q} = P_0$ irreducible and $T(Q) \neq 0$.

Lean: `GlobalTheory.LKDefFin.finite_classes_of_pol`.

*Proof.* If there is no such class, there is nothing to prove. Otherwise fix one, with representative $Q_0$, and let $\gamma_0 = \gamma_{Q_0}$ and $c_0 = c_{Q_0}$. We show that each such class lies in the union of the two finite sets of the last theorem for $(\gamma_0, c_0)$ and $(\gamma_0, -c_0)$. Let $Q$ be the representative of such a class. The lemma on a witness gives $(x, t)$ and $g$ with $f(g^{-1}(x \gamma_Q x^{-1}, c_Q)\, g) \neq 0$. Since $P_{\gamma_Q} = P_{\gamma_0}$ is irreducible, the theorem of Skolem and Noether gives $y$ with $\gamma_0 = y \gamma_Q y^{-1}$. The lemma on the conjugate pair gives $P' \sim Q$ with $\gamma_{P'} = \gamma_0$, $c_{P'} = c_Q$, and a trivialization of $P'$ with the same image as $(x, t)$. So $[P'] = [Q]$, and $f$ is not $0$ at the conjugate by $g$ of this image. By the lemma on the factor, $c_{P'} = c_0$ or $c_{P'} = -c_0$. $\square$

**Theorem 6.3.14 (Finite definite classes for a fixed polynomial).** Under the assumptions of the last theorem, for each $P_0 \in F[X]$ there are only finitely many classes whose representative $Q$ has $P_{\gamma_Q} = P_0$ irreducible and $T(Q) \neq 0$.

Lean: `GlobalTheory.T.finite_definitePair_classes_fixed_minpoly_degree_one`.

*Proof.* This is the theorem on classes for a fixed polynomial. $\square$

**Theorem 6.3.15 (Finitely many classes with a nonzero term).** Under the same assumptions, there are only finitely many classes whose representative $Q$ has $P_{\gamma_Q}$ irreducible and $T(Q) \neq 0$.

Lean: `GlobalTheory.LKDef.FinPairs.finite_classes_irr_term_ne_zero`.

*Proof.* By the theorem on finitely many polynomials, the polynomials $P_{\gamma_Q}$ of these representatives form a finite set. Each class lies in the set of the last theorem for its own polynomial. A finite union of finite sets is finite. $\square$

**Corollary 6.3.16 (Finiteness for the trace).** Under the same assumptions, there are only finitely many classes whose representative $Q$ has $P_{\gamma_Q}$ irreducible and $T(Q) \neq 0$.

Lean: `GlobalTheory.T.bi_invariant_conjugacy_classes_finite`.

*Proof.* This is the theorem on finitely many classes with a nonzero term. $\square$

**Remark 6.3.17 (Formalization).** In [FiniteDefinitePairClassesFixedMinpolyDegreeOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteDefinitePairClassesFixedMinpolyDegreeOne.lean#L212) the representatives $P_{b, \epsilon}$ are chosen by `Exists.choose`, with the index set $R \times$ `Bool`, and the default value $P_1$ when no pair exists. The theorem on classes for a fixed polynomial (line 293) takes four hypotheses that its proof never uses: $a = 1$, the bi-invariance of $f$, the test property of $\varphi$ and the bi-invariance of $\varphi$. Its proof uses only that $f$ is a test function and that the term is not $0$. The theorem on finitely many polynomials, in FiniteMinpolyDefinitePairsTermNeZero.lean, also leaves $a = 1$ and both bi-invariance hypotheses unused (line 268). The name of the wrapper `GlobalTheory.T.finite_definitePair_classes_fixed_minpoly_degree_one` refers to degree one, but the statement has no condition of degree one. The name of the wrapper `GlobalTheory.T.bi_invariant_conjugacy_classes_finite` refers to conjugacy classes, but the statement is about classes of definite pairs. Both wrappers have the same statement as the result they wrap. The theorem on finitely many classes is in HaarConjugateSubgroupIndexRatio.lean, a file name unrelated to its content. We read only the outline of the proof of the theorem on finitely many polynomials, and only the statement of the theorem on classes modulo rational norms. The Skolem and Noether theorem is proved in SkolemNoetherConjugacy.lean from `GroundTheory.Brauer.exists_unit_conj`, whose proof we did not open.
