---
title: Moving the weight at v'
decls:
  - UpperTheory.Gal.Wt.wtLacEx_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moving the weight at v'

The congruence statement of Section 25 asks for spaces $U'$ whose weight at an embedding over $v'$ is lacunary. This section proves that the Hecke eigenvalues of a space $U$ are $\ell$-adic limits of those of spaces whose weight at one embedding $\tau_0$ over $v'$ satisfies a gap condition, while the weights at the other infinite places do not change. The method multiplies a form of $U$ by a family of Section 29 of very large highest weight at $\tau_0$, and splits the result into eigenvectors. The result is [the weight change theorem](/entry/wt-lac-ex-holds/). Section 32 uses it to prove the step statement of Section 31.

We keep the notation of Sections 25, 28 and 29.

### The weight change statement

**Definition 3.31.1 (Gap condition).** A multiset $J$ of $a$ integers, sorted as $j_0 \leq \cdots \leq j_{a-1}$, satisfies the *gap condition* if $j_{i+1} - j_0 > a (j_i - j_0)$ for $0 \leq i \leq a - 2$. A dominant weight $\mu$ satisfies it if the multiset $\{\tfrac{a-1}{2} - z\}$, for $z$ in the infinitesimal character of $\mu$, does.

Lean: `GlobalTheory.CongL.GapJ` (also `UpperTheory.Gal.Int.Cong.GapWt`).

**Example 3.31.2.** For $a = 3$, the set $\{0, 1, 4\}$ satisfies the gap condition: $1 > 0$ and $4 > 3$. The set $\{0, 1, 3\}$ does not.

For a function $t : G \to \mathbb{C}$ of finite support, $R(t) \varphi = \sum_g t(g) R(g) \varphi$. A family $(t_j)_{j \in J}$ *acts on $K$-fixed vectors by $\eta$* if $R(t_j) \varphi = \eta_j(U) \varphi$ for each automorphic $U$, each $\varphi \in U$ fixed by $K$ and each $j$.

**Definition 3.31.3 (Integral operators).** An element $g \in G_f$ has *denominators at most $d$* if $\ell^d c_u(g)$ and $\ell^d c_u(g)^{-1}$ have integral entries at every place $u \mid \ell$. A function $t$ of finite support is *$\lambda$-integral* if each $g$ in its support lies in $G_f$ and has denominators at most some $d$ with $\lVert \iota^{-1} t(g) \rVert \leq \ell^{-a d \lvert \lambda \rvert}$. It is *locally $\lambda$-integral* if the same holds with $\lvert \lambda \rvert$ replaced by $\sum_u \lvert \lambda \rvert_u$, the sum over the $u \mid \ell$ with $c_u(g) \neq 1$.

Lean: `UpperTheory.Gal.Gen.IntW` (also `UpperTheory.Gal.Gen.DenomLe`, `UpperTheory.Gal.Gen.Loc.IntL`).

**Definition 3.31.4 (Framed family).** Let $W$ be a weight. A family $(t_j)$ is *framed* for $W$ if there are a set $X$ and $b : G \times X \to V_W$ such that every algebraic form $f$ of weight $W$ has bounded values $\lVert \iota^{-1} f(b(g, i))(g) \rVert$; a form with $f(b(g, i))(g) = 0$ for all $g, i$ is zero; and for each linear $F$ from $V_W$ to functions on $G$ with $\lVert \iota^{-1} F(b(g, i))(g) \rVert \leq r$ for all $g, i$, also $\lVert \iota^{-1} (R(t_j) F(b(g, i)))(g) \rVert \leq r$ for all $j, g, i$.

Lean: `UpperTheory.Gal.Gen.FramedX`.

So $b$ is an integral structure on the forms of weight $W$, and the $t_j$ preserve it.

**Definition 3.31.5 (Weight change statement).** Let $Q$ be a property of dominant weights. The *weight change statement for $Q$* says: let $a \geq 1$, let $w_0, v' \mid \ell$ be split and apart, $K$ a level away from $w_0$ that contains each $x \in G_{v'}$ with $c_{v'}(x) \in \mathrm{GL}_a(\mathcal{O}_{v'})$, $K_v \subset \mathrm{GL}_a(E_{v'})$ open, and $K' = \{x \in K : c_{v'}(x) \in K_v\}$. Let $(t_j)$ be locally $\lambda$-integral, with supports in the elements whose components at the places not apart from $w_0$, and at those not apart from $v'$, are trivial, acting on $K'$-fixed vectors by $\eta$. Let $\tau_0$ lie over $v'$. Then for each $U$ of type $(\lambda, K')$, $(\iota^{-1} \eta_j(U))_j$ is polynomially approximated by the $(\iota^{-1} \eta_j(U'))_j$ for the $U'$ for which there is $\mu$ with: $\mu_\tau = \lambda_\tau$ unless $\tau$ lies over the pair of $v'$; $Q(\mu_{\tau_0})$; and $U'$ is of type $(\mu, K)$.

Lean: `UpperTheory.Gal.Int.Cong.WtTo` (also `UpperTheory.Gal.Int.Cong.WtLacEx`, the case of the gap condition; `UpperTheory.Gal.Int.Cong.WtChgEx`, the case $Q = $ true).

The space $U'$ need only have a vector fixed by $K$, not by $K'$: the level at $v'$ is given up.

**Proposition 3.31.6 (Inputs on weights).** Let $a \geq 1$.

1. *Forms.* If $K \subset G_f$ and $U$ is of type $(\lambda, K)$, there is an algebraic form $f \neq 0$ of weight $W_\lambda$ with values in $U$ and fixed by $K$.
2. *Frames.* A family of functions, each $\lambda$-integral or locally $\lambda$-integral, is framed for $W_\lambda$.
3. *Decomposition.* A family $B$ near $\nu$ of level $K$ and defect $d$ is a finite sum $\sum_{V} B_V$ of families near $\nu$ of the same level and defect, with values in automorphic spaces $V$.
4. *Weights.* If $B \neq 0$ is such a family at $\tau$ with values in an automorphic space $V$, there is $\mu$ with $V$ of type $(\mu, K)$, $\mu_{\tau'} = W_{\tau'}$ at the $\tau'$ whose infinite place differs from that of $\tau$, and $\lvert \mu_{\tau, i} - \nu_i \rvert \leq 2d$ for all $i$.

Lean: `GlobalTheory.T.exists_algebraicForm_weight_level_smooth_at_place` (also `UpperTheory.Gal.Gen.Loc.frame`, `UpperTheory.Gal.Wt.famProj_holds`, `UpperTheory.Gal.Wt.famWt_holds`).

These facts are proved elsewhere in the development, and we take them as given. Item 4 reads the weight off the exponents in item 4 of the definition of a family.

**Lemma 3.31.7 (Eigenvector approximation).** Let $V$ be a complex vector space, $(e_x)_{x \in X}$ linear forms on $V$ and $(T_j)_{j \in J}$ operators with $\sup_x \lVert \iota^{-1} e_x(T_j v) \rVert \leq \sup_x \lVert \iota^{-1} e_x(v) \rVert$. Let $T_j v_0 = \theta_j v_0$ with $\lVert \iota^{-1} e_{x_0}(v_0) \rVert = 1$, and let $v_1, \dots, v_m$ have $T_j v_i = \eta_{ij} v_i$. If $\lVert \iota^{-1} e_x(v_0 + \sum_i v_i) \rVert \leq \varepsilon$ for all $x$, there are finitely many $z$ among the $(\iota^{-1} \eta_{ij})_j$ and coefficients $c_z$ with $\lVert P(\iota^{-1} \theta) - \sum_z c_z P(z) \rVert \leq \varepsilon$ for all $P \in \mathbb{Z}[X_j : j \in J]$.

Lean: `GlobalTheory.T.eigenvector_small_sub_finite_eigen_approx_inequality` (also `GlobalTheory.Cong.eigen_small_sub_finite_approx`).

*Proof.* Let $u(P) = P(\theta) v_0 + \sum_i P(\eta_i) v_i$. We show $\lVert \iota^{-1} e_x(u(P)) \rVert \leq \varepsilon$ for all $x$ by induction on $P$. For an integer $P = n$, $u(n) = n(v_0 + \sum v_i)$ and $\lVert n \rVert \leq 1$. Sums follow from the ultrametric inequality, and $u(P X_j) = T_j u(P)$ follows from the hypothesis on $T_j$. Now evaluate at $x_0$, divide by $\iota^{-1} e_{x_0}(v_0)$, and take $c = -\iota^{-1} e_{x_0}(v_i) / \iota^{-1} e_{x_0}(v_0)$ at $z = \iota^{-1} \eta_i$. $\square$

Let $\nu^0_k = -(a+1)^k$ for $0 \leq k < a$. It is decreasing, so $N \nu^0$ is a dominant weight for $N \geq 0$.

**Lemma 3.31.8 (Gap from nearness).** Let $\mu$ be a dominant weight with $\lvert \mu_k - N \nu^0_k \rvert \leq d$ for all $k$, and $(a+1)(2d + a) < N$. Then $\mu$ satisfies the gap condition.

Lean: `UpperTheory.Gal.Int.Cong.gapJ_of_near` (also `UpperTheory.Gal.Int.Cong.mu0`, `UpperTheory.Gal.Int.Cong.lacunaryBaseWeight_antitone`).

*Proof.* The multiset $\{\tfrac{a-1}{2} - z\}$ is $\{j_k = k - \mu_k\}$, and $j_k$ increases since $\mu$ decreases, so it is already sorted. Let $0 \leq i \leq a - 2$ and $P = (a+1)^i \geq 1$. Then $j_{i+1} - j_0 \geq (i + 1) + N(a+1)P - N - 2d$ and $a(j_i - j_0) \leq a i + a N P - a N + 2ad$. The difference is at least $NP + (a - 1)N + (i+1) - ai - 2d(a+1)$. Since $NP \geq N > 2d(a+1) + a(a+1)$ and $ai \leq a^2$, it is positive. $\square$

**Theorem 3.31.9 (Weight change).** The weight change statement holds for the gap condition.

Lean: `UpperTheory.Gal.Wt.wtLacEx_holds` (also `UpperTheory.Gal.Wt.top_of`).

*Proof.* Let $U$ be of type $(\lambda, K')$. By item 1 there is an algebraic form $f \neq 0$ of weight $W_\lambda$ with values in $U$, fixed by $K'$. The $t_j$ are locally $\lambda$-integral, so by item 2 they are framed for $W_\lambda$ by a map $b$, and $f(b(g_0, i_0))(g_0) = z_0 \neq 0$ for some $g_0, i_0$. Put $f_1 = f / z_0$. Given $\varepsilon$, the theorem on families with $\tau_0$ gives $d$ and $M$. Take $N = (a+1)(4d + a) + 1$, $\nu = N \nu^0$, and the family $B$ near $\nu$ for $f_1$. By item 3, $B = \sum_V B_V$ over automorphic spaces $V$, each $B_V$ a family of level $K$. Put $v_V(v)(g) = -B_V(Mg, Mg)(v)(g)$ for the $V$ with $B_V \neq 0$.

Each $v_V$ is an eigenvector of the $R(t_j)$ with eigenvalues $\eta_j(V)$: the support of $t_j$ lies in $G_f$ with trivial component at $v'$, so $M(gh) = M(g)$ there, and the values of $B_V$ are fixed by $K \supset K'$. Also $f_1$ has eigenvalues $\eta_j(U)$. By the theorem on families, all values $\lVert \iota^{-1}(f_1 + \sum_V v_V)(b(g, i))(g) \rVert$ are at most $\varepsilon$, and $\lVert \iota^{-1} f_1(b(g_0, i_0))(g_0) \rVert = 1$. The framing gives the norm hypothesis of the eigenvector lemma, so $(\iota^{-1} \eta_j(U))_j$ is approximated to $\varepsilon$ by the $(\iota^{-1} \eta_j(V))_j$.

For each such $V$, item 4 gives $\mu$ with $V$ of type $(\mu, K)$, $\mu_\tau = \lambda_\tau$ at the $\tau$ whose infinite place is not that of $\tau_0$, and $\lvert \mu_{\tau_0, k} - N \nu^0_k \rvert \leq 2d$. The lemma on gaps, with $2d$ in place of $d$, gives the gap condition for $\mu_{\tau_0}$. If $\mu_\tau \neq \lambda_\tau$, then $\tau$ has the infinite place of $\tau_0$, so $\tau = \tau_0$ or $\tau = \tau_0 \circ c$, and $\tau$ lies over the pair of $v'$. $\square$

**Remark 3.31.10 (Formalization).** The case $Q = $ true of the weight change statement, `WtChgEx` at [WtDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/WtDefs.lean#L30), is not used. The theorem is [LadicWeightEmbeddingOverPlace.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/WeightCharacters/LadicWeightEmbeddingOverPlace.lean#L73), with the proof in TopOf.lean. We read the proofs of the theorem and the two lemmas in full, and only the statements of the items of the proposition.
