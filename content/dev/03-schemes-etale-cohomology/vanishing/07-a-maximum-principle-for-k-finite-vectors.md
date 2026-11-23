---
title: A maximum principle for K-finite vectors
decls:
  - PositivityTheory.CWB.eigen_gain_high
  - PositivityTheory.CWB.eigenspace_form_sum
  - PositivityTheory.CWB.maxPr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A maximum principle for K-finite vectors

The rest of the chapter leaves algebraic geometry. Sections 7 and 8 prove the Casselman-Wallach theorem for the unitary groups $U(p, q)$: a map of $(\mathfrak{g}, K)$-modules from the $K$-finite vectors of an irreducible unitary representation to a smooth representation of moderate growth extends to the smooth vectors. This section proves the main estimate ([Theorem 9.7.4](/entry/max-pr/)): a function on $U(p, q)$ that is built linearly from the $K$-finite vectors and has polynomial growth is bounded at the identity by a Sobolev norm, as soon as it is bounded on finitely many vectors. The proof is a maximum principle for a weighted sum of squares, with weights from the $K$-Casimir operator. For the background see [representations of real groups](/learn/representations/#representations-of-real-groups) and [$(\mathfrak{g}, K)$-modules](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules).

Fix $n \geq 1$ and a map $\epsilon : \{1, \dots, n\} \to \{\pm 1\}$, and let $J$ be the diagonal matrix with entries $\epsilon(a)$. Put
$$G = \{g \in M_n(\mathbb{C}) : g^* J g = J\}, \qquad K = \{g \in G : g \text{ unitary}, gJ = Jg\},$$
so $G \cong U(p, q)$ and $K \cong U(p) \times U(q)$. The Lie algebra $\mathfrak{g} = \{X : X^*J + JX = 0\}$ is the sum of $\mathfrak{k}$, the $X$ that commute with $J$, and $\mathfrak{p}$, the $X$ with $XJ = -JX$. A pair $(a, b)$ is *compact* if $\epsilon(a) = \epsilon(b)$ and *noncompact* otherwise; write $P$ for the set of noncompact pairs. For $g \in M_n(\mathbb{C})$ put $\|g\|^2 = \sum_{a,b} |g_{ab}|^2$.

**Definition 9.7.1 (Admissible unitary module).** Let $V$ be a complex inner product space, not necessarily complete, with linear maps $E_{ab} : V \to V$ for $1 \leq a, b \leq n$. Put
$$\Omega = \sum_{a,b} E_{ab}E_{ba}, \qquad \Omega_K = \sum_{\epsilon(a) = \epsilon(b)} E_{ab}E_{ba}, \qquad E(X) = \sum_{a,b} X_{ab} E_{ab}.$$
The family $(E_{ab})$ is an *admissible unitary module* if:

1. $[E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{da}E_{cb}$, so $V$ is a module over $\mathfrak{gl}_n(\mathbb{C}) = \mathfrak{g}_{\mathbb{C}}$;
2. $\langle E_{ab}x, y \rangle = \pm\langle x, E_{ba}y \rangle$, with the sign $+$ for compact pairs and $-$ for noncompact pairs;
3. no subspace other than $0$ and $V$ is stable under all $E_{ab}$;
4. $V$ is spanned by eigenvectors of $\Omega_K$ with real eigenvalues;
5. for each $R$, the eigenvectors with eigenvalue $\leq R$ span a finite-dimensional space.

Condition 2 says that the real form $\mathfrak{g}$ acts by skew-adjoint operators. The $K$-finite vectors of an irreducible unitary representation of $G$ give such a module, with $\Omega$ the [Casimir operator](/learn/real-groups/#the-center-of-umathfrakg-and-the-casimir-operator) ([[universal enveloping algebra|SCZ8PRVY00]]). We use four facts about an admissible unitary module, which follow from the definition by direct computation.

1. $\Omega$ acts by a real scalar $\kappa$, since it commutes with all $E_{ab}$ and $V$ is irreducible.
2. $V$ has an orthonormal basis $(b_i)$ of eigenvectors of $\Omega_K$ with eigenvalues $\mu_i \geq 0$, finitely many below each $R$. For $\varphi : \mathbb{R} \to \mathbb{R}$ we write $\varphi(\Omega_K)$ for the operator with $\varphi(\Omega_K)b_i = \varphi(\mu_i)b_i$.
3. For each $w$, $\sum_{(a,b) \in P} \|E_{ab}w\|^2 = \operatorname{Re}\langle w, \Omega_K w\rangle - \kappa\|w\|^2$. This follows from $\Omega = \Omega_K + \sum_P E_{ab}E_{ba}$ and the sign in condition 2.
4. Put $Z_{ab} = [\Omega_K, E_{ab}]$. There are $c_0 > 0$, $x_1$ and $C \geq 0$ such that for each eigenvector $v$ of $\Omega_K$ with eigenvalue $\nu \geq 0$:
$$\Big|\sum_P \langle E_{ab}v, Z_{ab}v\rangle\Big| \leq C(1+\nu)\|v\|^2, \qquad \sum_P \|[\Omega_K, Z_{ab}]v\|^2 \leq C(1+\nu)^3\|v\|^2,$$
and $\sum_P \|Z_{ab}v\|^2 \geq c_0(1+\nu)^2\|v\|^2$ if $\nu \geq x_1$.

By fact 3, $\sum_P \|E_{ab}v\|^2 = (\nu - \kappa)\|v\|^2$ for an eigenvector $v$ with eigenvalue $\nu$. The next theorem says that a weight $(1+\Omega_K)^{-s}$ on the vectors $E_{ab}v$ gains an arbitrary constant $c$. The reason is that a noncompact $E_{ab}$ moves the eigenvalue of $\Omega_K$ up and down, by fact 4, and $x \mapsto (1+x)^{-s}$ is convex.

**Theorem 9.7.2 (Gain from the noncompact directions).** Let $(E_{ab})$ be an admissible unitary module with eigenbasis $(b_i, \mu_i)$ and Casimir scalar $\kappa$, and let $c \geq 0$. There are an integer $s \geq 1$ and $x_0 \geq 0$ such that for each eigenvector $v$ of $\Omega_K$ with eigenvalue $\nu \geq x_0$:
$$(1+\nu)^{-s}(\nu - \kappa + c)\|v\|^2 \leq \sum_{(a,b) \in P} \operatorname{Re}\big\langle E_{ab}v, (1+\Omega_K)^{-s}E_{ab}v\big\rangle.$$

Lean: `PositivityTheory.CWB.eigen_gain_high`.

*Proof.* There is $c_s \geq 0$ with $(1+y)^{-s} \geq 1 - sy + \frac{s^2}{4}y^2 - c_s y^4$ for all real $y > -1$; this is the Taylor expansion of $(1+y)^{-s}$ at $0$, with $\frac{s^2}{4} \leq \frac{s(s+1)}{2}$. Choose $s \geq 4(C + c + 1)/c_0$, so that $\frac{s^2}{4}c_0 - sC \geq c + 1$, and $x_0 = \max(0, x_1, c_s C)$. Let $Y = (\Omega_K - \nu)/(1+\nu)$, so that $(1+\Omega_K)^{-s} = (1+\nu)^{-s}(1+Y)^{-s}$, and the eigenvalues of $Y$ are $> -1$. Since $\varphi \leq \psi$ on $[0, \infty)$ implies $\langle w, \varphi(\Omega_K)w\rangle \leq \langle w, \psi(\Omega_K)w\rangle$, we get for $w_{ab} = E_{ab}v$:
$$(1+\nu)^s\langle w, (1+\Omega_K)^{-s}w\rangle \geq \|w\|^2 - s\langle w, Yw\rangle + \tfrac{s^2}{4}\|Yw\|^2 - c_s\|Y^2w\|^2.$$
Now $(\Omega_K - \nu)E_{ab}v = Z_{ab}v$ and $(\Omega_K - \nu)^2E_{ab}v = [\Omega_K, Z_{ab}]v$, as $\Omega_K v = \nu v$. Sum over $P$ and use fact 3 and fact 4. The sum of the right sides is at least
$$(\nu - \kappa)\|v\|^2 - sC\|v\|^2 + \tfrac{s^2}{4}c_0\|v\|^2 - \frac{c_s C}{1+\nu}\|v\|^2 \geq (\nu - \kappa + c)\|v\|^2,$$
since $\frac{s^2}{4}c_0 - sC \geq c + 1$ and $c_s C \leq \nu < 1 + \nu$. Multiply by $(1+\nu)^{-s}$. $\square$

For an integer $s$ and $R > 0$, put $\varphi_R(x) = \max\big((1+x)^{-s} - (1+R)^{-s}, 0\big)$. It is $0$ for $x \geq R$ and increases to $(1+x)^{-s}$ as $R \to \infty$.

**Theorem 9.7.3 (The weighted sum over eigenvalues).** In the setting of the last theorem, let $c \geq 0$. There are an integer $s \geq 1$ and reals $x_0$ and $C_1 \geq 0$ such that for each $R$ and each linear form $f$ on $V$, with $S = \{i : \mu_i < R\}$ and $T = \{i : \mu_i < x_0\}$,
$$c\sum_{i \in S}\varphi_R(\mu_i)|f(b_i)|^2 - C_1\sum_{i \in T}|f(b_i)|^2 \leq \sum_{i \in S}\varphi_R(\mu_i)\Big(\sum_{(a,b) \in P}|f(E_{ab}b_i)|^2 - (\mu_i - \kappa)|f(b_i)|^2\Big).$$

Lean: `PositivityTheory.CWB.eigenspace_form_sum`.

*Proof.* Take $s$ and $x_0$ from the last theorem, and $C_1 = x_0 + |\kappa| + c$. For an operator $A$ put $\beta_A(v, w) = \sum_P \langle E_{ab}v, AE_{ab}w\rangle$. Since $\varphi_R(\mu_i) = 0$ outside $S$ and each $E_{ab}b_i$ is a finite combination of basis vectors, there is a finite set $T'$ of indices such that only the $f(b_j)$ with $j \in T'$ occur below. For each eigenvalue $\nu$ put $w_\nu = \sum_{j \in T', \mu_j = \nu}\overline{f(b_j)}\,b_j$, an eigenvector with $\|w_\nu\|^2 = \sum_{j \in T', \mu_j = \nu}|f(b_j)|^2$, and $w = \sum_\nu w_\nu$. Then $f(E_{ab}b_i) = \langle E_{ab}^*w, b_i\rangle$, and $E_{ab}^* = -E_{ba}$ for $(a, b) \in P$, so the left side below is $\operatorname{Re}\beta_{\varphi_R(\Omega_K)}(w, w)$. The operator $\sum_P E_{ab}^*\varphi_R(\Omega_K)E_{ab}$ is invariant under $\mathfrak{k}$, so it commutes with $\Omega_K$, and the forms $\beta_{\varphi_R(\Omega_K)}(w_\nu, w_{\nu'})$ vanish for $\nu \neq \nu'$. So
$$\sum_{i \in S}\varphi_R(\mu_i)\sum_P|f(E_{ab}b_i)|^2 = \sum_\nu \operatorname{Re}\beta_{\varphi_R(\Omega_K)}(w_\nu, w_\nu).$$
For an eigenvector $w$ with eigenvalue $\nu \geq 0$ we claim
$$\operatorname{Re}\beta_{\varphi_R(\Omega_K)}(w, w) \geq \big(\varphi_R(\nu)(\nu - \kappa + c) - [\nu < x_0]\,C_1\big)\|w\|^2.$$
If $\nu \geq R$, then $\varphi_R(\nu) = 0$ and the form is $\geq 0$, since $\varphi_R \geq 0$. If $x_0 \leq \nu < R$, then $\varphi_R \geq (1+x)^{-s} - (1+R)^{-s}$, so by the last theorem and fact 3 the form is at least $\big((1+\nu)^{-s}(\nu - \kappa + c) - (1+R)^{-s}(\nu - \kappa)\big)\|w\|^2 \geq \varphi_R(\nu)(\nu - \kappa + c)\|w\|^2$. If $\nu < x_0$, the form is $\geq 0$, and $\varphi_R(\nu)(\nu - \kappa + c) \leq x_0 + |\kappa| + c$, as $0 \leq \varphi_R \leq 1$. Sum the claim over $\nu$, with $w = w_\nu$, and rearrange. $\square$

**Theorem 9.7.4 (Maximum principle).** Let $(E_{ab})$ be an admissible unitary module on $V$ and $N \geq 0$. There are an integer $m$, a real $K_0 \geq 0$ and a finite set $I_0 \subseteq V$ with the following property. Let $F$ be a linear map from $V$ to the functions on $M_n(\mathbb{C})$ such that for each $v$:

1. $F(v)$ is continuous on $G$;
2. for $X \in \mathfrak{p}$ and $g \in G$, the derivative of $t \mapsto F(v)(g\exp(tX))$ at $t = 0$ is $F(E(X)v)(g)$;
3. $|F(v)(g)| \leq C_v(1 + \|g\|^2)^N$ on $G$, for a constant $C_v$.

Let $B \geq 0$ with $|F(e)(g)| \leq B(1 + \|g\|^2)^N$ on $G$ for all $e \in I_0$. Then $|F(v)(1)| \leq K_0 B\,\|(1+\Omega_K)^m v\|$ for all $v \in V$.

Lean: `PositivityTheory.CWB.maxPr`.

Typically $F(v)(g) = \lambda(\pi(g)T_0v)$ for a map $T_0$ of $(\mathfrak{g}, K)$-modules into a representation $\pi$ of moderate growth and a continuous functional $\lambda$. The theorem plays the role of the a priori estimates in the proof of Casselman and Wallach (N. Wallach, *Real Reductive Groups II*, Chapter 11).

*Proof.* Let $\kappa$ and $(b_i, \mu_i)$ be as in facts 1 and 2. For $(a, b) \in P$ let $X_{ab} = \frac{1+i}{2}e_{ab} + \frac{1-i}{2}e_{ba}$, an element of $\mathfrak{p}$.

Step 1 (a scalar maximum principle). There is $c \geq 0$ with this property: let $u : M_n(\mathbb{C}) \to \mathbb{R}$ be continuous on $G$ with $u(g) \leq C(1 + \|g\|^2)^{2N}$ on $G$, and $A \geq 0$, such that at each $g \in G$ the second derivatives $d_{ab}$ of $t \mapsto u(g\exp(tX_{ab}))$ at $0$ satisfy $c\,u(g) - A(1+\|g\|^2)^{2N} \leq \sum_P d_{ab}$. Then $u(1) \leq A(1+n)^{2N}$. This holds because the sets $\{g \in G : \|g\|^2 \leq \rho\}$ are compact, the second derivatives of the weight $(1+\|g\|^2)^{2N}$ along $X_{ab}$ are bounded by a multiple of the weight, and second derivatives are $\leq 0$ at a local maximum.

Step 2 (the constants). Take $s$, $x_0$, $C_1$ from the last theorem with $c/2$ in place of $c$. Let $T = \{i : \mu_i < x_0\}$, a finite set, $I_0 = \{b_i : i \in T\}$, $m = s$ and $K_0 = \sqrt{2C_1|T|(1+n)^{2N}}$.

Step 3 (the weighted sum). Fix $R$, put $S = \{i : \mu_i < R\}$ and $u(g) = \sum_{i \in S}\varphi_R(\mu_i)|F(b_i)(g)|^2$. Then $u$ is continuous with growth of order $2N$. By hypothesis 2, the second derivatives of $u$ satisfy
$$\sum_P d_{ab} = 2\sum_{i \in S}\varphi_R(\mu_i)\Big(\sum_P |F(E_{ab}b_i)(g)|^2 - (\mu_i - \kappa)|F(b_i)(g)|^2\Big),$$
using $\sum_P E(X_{ab})^2 = \kappa - \Omega_K$. The last theorem, for the form $f = F(\cdot)(g)$, gives $\sum_P d_{ab} \geq c\,u(g) - 2C_1\sum_{i \in T}|F(b_i)(g)|^2 \geq c\,u(g) - 2C_1|T|B^2(1+\|g\|^2)^{2N}$. By Step 1, $u(1) \leq (K_0B)^2$.

Step 4 (summation). Put $f = F(\cdot)(1)$. By Step 3, $\sum_{\mu_i < R}\varphi_R(\mu_i)|f(b_i)|^2 \leq (K_0B)^2$ for all $R$. Letting $R \to \infty$ gives $\sum_i (1+\mu_i)^{-s}|f(b_i)|^2 \leq (K_0B)^2$. By the Cauchy-Schwarz inequality, with $(1+\mu_i)^s \leq (1+\mu_i)^{2s}$,
$$|f(v)| = \Big|\sum_i \langle b_i, v\rangle f(b_i)\Big| \leq K_0B\Big(\sum_i (1+\mu_i)^{2s}|\langle b_i, v\rangle|^2\Big)^{1/2} = K_0B\,\|(1+\Omega_K)^s v\|. \qquad \square$$

**Remark 9.7.5 (Formalization).** The three theorems are one-line proofs in [EtaleCohomologyNegativeVanishingDegreeZero.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/EtaleCohomologyNegativeVanishingDegreeZero.lean#L71) from `eigen_gain_of_moments`, `basis_form_sum_of_gain` and `maxPr_of`; the module name has nothing to do with étale cohomology. In the same file several names do not match their statements: `word_filtration_basic : A0` (L35) states the Casimir identities of fact 3, `etale_cohomology_vanishing_negative_degree_zero : A9` (L61) is the first two bounds of fact 4, `hilbert_schmidt_growth : B2` (L79) is proved by `heightFunctionalStatement_of_pairingProperties`, `tateTwist_local_to_global_strictlyHenselian : B3` (L81) is the fact that second derivatives are $\leq 0$ at a local maximum, and `identity_operator_filtration : A6` (L53) is proved by `SymmetricPowerMatrix`. In [PMaxPr.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/PMaxPr.lean#L28) the hypothesis `UnitaryGroupFacts` of `maxPr_of` is bound to `_` and not used; it enters only through Step 1. Facts 1 to 4 and Step 1 are statements `A0` to `A10`, `MaximumPrincipleVar`, `SumSquaresSecondDerivative` and `B5`; we read their statements and give the classical reasons. The growth weight is `hs2 g` $= \|g\|^2$, and $\|1\|^2 = n$.
