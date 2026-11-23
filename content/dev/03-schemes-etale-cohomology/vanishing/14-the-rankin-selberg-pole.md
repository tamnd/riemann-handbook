---
title: The pole of the Rankin-Selberg L-function
decls:
  - PositivityTheory.jumpWindows.mirabolic_induction_step_holds
  - PositivityTheory.AdelicQuotientData.rsPole
  - PositivityTheory.AdelicQuotientData.rsPole_of_inputs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The pole of the Rankin-Selberg L-function

This section is about the partial Rankin-Selberg $L$-function $L^S(s, \pi \times \tilde\pi')$ of two cuspidal representations near $s = 1$. The main result writes $(s - 1) L^S(s)$, times a factor that does not vanish on a chosen vertical line, as a function that is holomorphic on $\operatorname{Re} s > 0$, and this function vanishes at $s = 1$ when the two representations are not equivalent. So the pole at $s = 1$ has order at most one, and there is no pole when $\pi \not\cong \pi'$. The result is used in the step [EveryCharacter](/step/every-character/), where it gives strong multiplicity one and the rigidity of cuspidal representations. The proof is the Rankin-Selberg method. One analytic input is proved here in full: a cut-off construction at the infinite places, which produces vectors whose Whittaker functionals are controlled along the mirabolic subgroup. See [automorphic representations](/learn/automorphic-forms/#automorphic-representations), [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms) and [generic representations and local factors](/learn/representations/#generic-representations-and-local-factors).

### The mirabolic step at the infinite places

Let $\iota$ be a finite set and $R = \mathbb{C}^\iota$, with the product of the complex topologies. For a totally complex field $E$, the product $\prod_{v \mid \infty} E_v$ is a ring of this form. We write $\mathrm{GL}_a(R)$ for the invertible $a \times a$ matrices over $R$, an open subset of the real vector space $\mathrm{M}_a(R)$.

**Definition 9.14.1 (Smooth vectors).** Let $X$ be a complex Banach space and $\rho : \mathrm{GL}_a(R) \to \mathrm{End}(X)$ a homomorphism into the bounded operators. We say that $\rho$ has *moderate growth* if there are $C \geq 0$ and $N \geq 0$ with
$$\|\rho(g)x\| \leq C\,(1 + \|g\| + \|g^{-1}\|)^N \|x\| \quad \text{for all } g, x.$$
A vector $v \in X$ is *smooth* if the map $M \mapsto \rho(M)v$, on the open set $\mathrm{GL}_a(R) \subseteq \mathrm{M}_a(R)$, is infinitely differentiable.

We do not ask that $\rho$ be continuous. The smooth vectors are the vectors on which the Lie algebra acts, and they are the natural domain for the integrals below.

**Definition 9.14.2 (Mirabolic subgroup and the column group).** Let $1 \leq n < a$. Let $G_n \subseteq \mathrm{GL}_a(R)$ be the matrices $h$ with $h_{ik} = \delta_{ik}$ when $i > n$ or $k > n$: this is $\mathrm{GL}_n(R)$ in the upper left corner. Let $P_n \subseteq G_n$ be the *mirabolic subgroup*, the matrices in $G_n$ whose row $n$ is $(0, \ldots, 0, 1, 0, \ldots, 0)$. For $y \in R^n$ let
$$u(y) = 1 + \sum_{i=1}^{n} y_i E_{i, n+1},$$
the unipotent matrix with $y$ above the diagonal in column $n + 1$. A continuous additive character $\chi : R \to \mathbb{C}^\times$ with $|\chi| = 1$ is *nondegenerate* if $\chi(zw) = 1$ for all $w \in R$ implies $z = 0$.

For $h \in G_n$ we have $h\,u(y) = u(hy)\,h$, where $hy$ is the product of the upper left block of $h$ with the column $y$. The last coordinate of $hy$ is $\sum_k h_{nk} y_k$. So the character $y \mapsto \chi(y_n)$ of the column group is moved by $h$ to the character $y \mapsto \chi(\sum_k h_{nk} y_k)$, which depends only on row $n$ of $h$.

**Proposition 9.14.3 (Mirabolic step).** Let $1 \leq n < a$, let $X$ be a complex Banach space, and let $\rho : \mathrm{GL}_a(R) \to \mathrm{End}(X)$ have moderate growth. Let $\chi$ be a nondegenerate character of $R$ and let $U$ be a neighbourhood of $1$ in $\mathrm{GL}_a(R)$. Then there are functions $\eta : \mathrm{GL}_a(R) \to \mathbb{C}$ and $r : \mathrm{GL}_a(R) \to \mathrm{GL}_a(R)$ with the following properties.

1. $\eta(1) \neq 0$, $r(1) = 1$, and $\eta$ takes values in $[0, \infty)$.
2. If $h \in G_n$ and $\eta(h) \neq 0$, then $r(h) \in P_n$.
3. There is a compact set $C \subseteq U \cap G_n$ such that each $h \in G_n$ with $\eta(h) \neq 0$ is $h = r(h)\,c$ with $c \in C$.
4. For each smooth $v \in X$ there is a smooth $v' \in X$ with this property. Let $Y \subseteq X$ be a closed subspace, stable under $\rho$, with $v \in Y$. Then $v' \in Y$. If $\Lambda : X \to \mathbb{C}$ is a continuous linear form with $\Lambda(\rho(u(y))x) = \chi(y_n)\Lambda(x)$ for all $x \in Y$ and $y \in R^n$, then
$$\Lambda(\rho(h)v') = \eta(h)\,\Lambda(\rho(r(h))v) \quad \text{for all } h \in G_n.$$

Lean: `PositivityTheory.jumpWindows.mirabolic_induction_step_holds`.

*Proof.* We use five facts of analysis, which are proved in the development and which we take as given here. (i) The smooth vectors form a subspace that is stable under each $\rho(g)$. (ii) Let $V$ be a finite-dimensional real vector space with Haar measure, and $L : V \to \mathrm{M}_a(R)$ a linear map with $(1 + L(y))^{-1} = 1 - L(y)$. If $G : V \to X$ is a rapidly decreasing family of the kind in (iii), then $\int_V \rho(1 + L(y))G(y)\,dy$ converges and is smooth. (iii) Let $\beta$ be a nondegenerate real bilinear form on $V$, $O \subseteq V$ open, and $\sigma : O \to \mathrm{GL}_a(R)$ smooth. Then the Fourier transforms $\hat F(y) = \int_V e^{-i\beta(x,y)} F(x)\,dx$ of the functions $F(x) = f(x)\rho(\sigma(x))w$, with $f$ smooth with compact support in $O$ and $w$ smooth, lie in such a family. (iv) Fourier inversion: there is $c \neq 0$ with $\int_V e^{i\beta(\xi,y)}\hat\varphi(y)\,dy = c\,\varphi(\xi)$ for each smooth $\varphi : V \to \mathbb{C}$ with compact support. (v) Each continuous character $\chi$ of $R$ with $|\chi| = 1$ is $\chi(z) = e^{i\ell(z)}$ for a real linear form $\ell$.

Let $V = R^n$ and $\beta(x, y) = \ell(\sum_k x_k y_k)$. If $\beta(x, y) = 0$ for all $x$, then $\chi(z y_k) = 1$ for all $z$ and $k$, so $y = 0$ because $\chi$ is nondegenerate. Let $O \subseteq V$ be the open set of $x$ such that $x_n$ is a unit of $R$. For $x \in O$ let $g(x) \in G_n$ be the identity matrix with row $n$ replaced by $(x_1, \ldots, x_n, 0, \ldots, 0)$, and let $g(x) = 1$ for $x \notin O$. Then $g$ is continuous on $O$, $g(e_n) = 1$, and $e_n\,g(x) = x$ as row vectors. For $h \in \mathrm{GL}_a(R)$ let $\xi(h) = (h_{n1}, \ldots, h_{nn})$.

The set $O \cap g^{-1}(U)$ is a neighbourhood of $e_n$. Choose a smooth function $f : V \to [0, 1]$ with compact support in it and $f(e_n) = 1$. Put $\eta(h) = f(\xi(h))$ and $r(h) = h\,g(\xi(h))^{-1}$. Then (1) holds since $\xi(1) = e_n$. If $h \in G_n$ and $\eta(h) \neq 0$, then $\xi(h) \in O$ and row $n$ of $r(h)$ is $\xi(h)\,g(\xi(h))^{-1} = e_n$, so $r(h) \in P_n$. This is (2). For (3), let $C = g(\operatorname{supp} f)$. It is compact, and it lies in $U \cap G_n$, and $h = r(h)\,g(\xi(h))$.

For (4), let $F(x) = f(x)\,\rho(g(x))^{-1}v$. It is smooth with compact support in $O$. Let
$$v' = c^{-1} \int_V \rho(u(y))\,\hat F(y)\,dy.$$
By (iii) and (ii) the integral converges and is smooth, and by (i) so is $v'$. If $Y$ is closed, stable and contains $v$, then $F(x) \in Y$ for all $x$, so $\hat F(y) \in Y$ and $v' \in Y$, because a closed subspace contains the integrals of its integrable functions. Now let $\Lambda$ be as in (4) and $h \in G_n$. Let $\varphi(x) = \Lambda(\rho(h)F(x))$, a smooth function with compact support, with $\hat\varphi(y) = \Lambda(\rho(h)\hat F(y))$. Since $h\,u(y) = u(hy)\,h$ and $\rho(h)\hat F(y) \in Y$,
$$\begin{aligned}
\Lambda\bigl(\rho(h)\rho(u(y))\hat F(y)\bigr) &= \Lambda\bigl(\rho(u(hy))\rho(h)\hat F(y)\bigr) \\
&= \chi\Bigl(\sum_k h_{nk} y_k\Bigr)\,\hat\varphi(y) = e^{i\beta(\xi(h), y)}\,\hat\varphi(y).
\end{aligned}$$
We integrate over $y$ and use (iv). This gives $\Lambda(\rho(h)v') = \varphi(\xi(h)) = f(\xi(h))\,\Lambda\bigl(\rho(h)\rho(g(\xi(h)))^{-1}v\bigr) = \eta(h)\,\Lambda(\rho(r(h))v)$. $\square$

In words: up to the weight $\eta(h)$, the functional $h \mapsto \Lambda(\rho(h)v')$ on $G_n$ is a function on the mirabolic subgroup, evaluated at $r(h)$.

### The partial Rankin-Selberg L-function

**Definition 9.14.4 (Partial Rankin-Selberg L-function).** Let $E$ be a number field and $S$ a finite set of finite places. For each finite place $w \notin S$ let $q_w = N(w)$ and let $\alpha_w \in (\mathbb{C}^\times)^m$ and $\beta_w \in (\mathbb{C}^\times)^k$. Put
$$L^S(s, \alpha, \beta) = \prod_{w \notin S} \prod_{a=1}^{m} \prod_{b=1}^{k} \bigl(1 - \alpha_{w,a}\,\overline{\beta_{w,b}}\,q_w^{-s}\bigr)^{-1},$$
where the product over $w$ is the unconditional limit over finite sets of places (and the value is $1$ when the product does not converge).

If $\alpha_w$ and $\beta_w$ are the Satake parameters of cuspidal representations $\pi$ and $\pi'$ and $\pi'$ has unitary central character, then $\overline{\beta_w}$ are the Satake parameters of the contragredient $\tilde\pi'$, and $L^S(s, \alpha, \beta)$ is the partial Rankin-Selberg $L$-function $L^S(s, \pi \times \tilde\pi')$. Each local factor is expanded by the Cauchy identity: for $k \leq m$, $|\alpha_{w,a}|, |\beta_{w,b}| \leq q_w^{1/2}$ and $\operatorname{Re} s > 1$,
$$\prod_{a,b}\bigl(1 - \alpha_a \overline{\beta_b} q^{-s}\bigr)^{-1} = \sum_{\lambda} s_\lambda(\alpha)\,\overline{s_\lambda(\beta)}\,q^{-s|\lambda|},$$
the sum over partitions $\lambda$ with at most $k$ parts, with $s_\lambda$ the Schur polynomial.

### The theorem

A cuspidal representation (as in the [previous section](/entry/jacquet-shalika-bound/)) is *normalised* if each of its forms $\varphi$ satisfies $\varphi(z_t g) = \varphi(g)$ for all $t \in \mathbb{R}$, where $z_t$ is the scalar matrix of the split centre at the infinite places with parameter $t$. It is a condition on the central character at the infinite places.

**Theorem 9.14.5 (Pole of the Rankin-Selberg L-function).** Let $E$ be a totally complex number field, $1 \leq k \leq m$, and $u \in \mathbb{R}$. Let $\pi$ be a normalised cuspidal representation of $\mathrm{GL}_m$ over $E$ and $\pi'$ a normalised cuspidal representation of $\mathrm{GL}_k$ over $E$. Then there is a finite set $S_0$ of finite places with the following property. Let $S \supseteq S_0$ be finite, and let $\alpha$ and $\beta$ be families such that, for each $w \notin S$, $\alpha_w$ lists the Satake multiset of $\pi$ at $w$ and $\beta_w$ lists that of $\pi'$. Then there are functions $Z, Z_S : \mathbb{C} \to \mathbb{C}$ and a real number $\sigma_0$ with:

1. $Z$ and $Z_S$ are holomorphic on $\operatorname{Re} s > 0$;
2. $Z_S(\sigma + iu) \neq 0$ for every $\sigma > 0$;
3. $Z(s) = (s - 1)\,Z_S(s)\,L^S(s, \alpha, \beta)$ for $\operatorname{Re} s > \sigma_0$;
4. if $m \neq k$, or $m = k$ and $\pi$ is not equivalent to $\pi'$, then $Z(1) = 0$.

Lean: `PositivityTheory.AdelicQuotientData.rsPole` (also `PositivityTheory.AdelicQuotientData.rsPole_of_inputs`, the same statement from its inputs).

*Proof.* We give the plan of the Rankin-Selberg method. Choose a standard character $\psi$ of $\mathbb{A}_E / E$. Normalised cuspidal representations have unitary central character, so the [Jacquet-Shalika bound](/entry/jacquet-shalika-bound/) gives $|\alpha_{w,a}|, |\beta_{w,b}| \leq q_w^{1/2}$ for all $w \notin S$. Choose a cusp form $\varphi'$ in $\pi'$ whose Whittaker function is the product of the spherical ones at the places outside a finite set $S_1$, and a cusp form $\varphi$ in $\pi$ whose Whittaker function is prepared at a finite set $S_2$ of places; the preparation at the infinite places is the [mirabolic step](/entry/mirabolic-induction-step-holds/) above, used inductively. Let $S_0 = S_1 \cup S_2$. From $\varphi$ and $\varphi'$ we build a function $H$ on $\mathrm{GL}_k(\mathbb{A}_E)$, invariant under $\mathrm{GL}_k(E)$ on the left: a sum over rational points of a function made from $\varphi$ (restricted to $\mathrm{GL}_k$), times $\overline{\varphi'(g)}\,|\det g|^{-(m-k)/2}$. We study $\int H(g)\,|\det g|^s\,dg$ over $\mathrm{GL}_k(E) \backslash \mathrm{GL}_k(\mathbb{A}_E)$.

First, unfolding. For $\operatorname{Re} s > \sigma_0$ the integral is $Z_S(s)\,L^S(s, \alpha, \beta)$, with $Z_S$ entire and $Z_S(\sigma + iu) \neq 0$ for all real $\sigma$. Classically the integral unfolds to an integral of a product of Whittaker functions, which factors into local integrals; at $w \notin S$ the local integral is computed by Shintani's formula and the Cauchy identity, and the bounds on the parameters give absolute convergence. The preparation of $\varphi$ is what makes the factor $Z_S$ at the places of $S$ nonzero on the line $\operatorname{Im} s = u$. This gives (2) and, with the next step, (3).

Second, continuation. The function $H$ has controlled growth relative to a second function $H_0$. Then there is $Z$, holomorphic on $\operatorname{Re} s > 0$, with $Z(s) = (s - 1)\int H(g)|\det g|^s\,dg$ for $\operatorname{Re} s > 1$, and $Z(1) = 0$ if the integral of $H_0$ over the band $1 \leq |\det g| \leq 2$ is zero. The band is a fundamental domain for the split centre, and the factor $s - 1$ absorbs the pole that comes from the part of $H$ that is invariant under the split centre. This gives (1) and (3) with $\sigma_0$ replaced by $\max(1, \sigma_0)$.

If $k < m$, $\varphi$ is restricted to $\mathrm{GL}_k$ through the corner embedding and projected along the unipotent radical, and $H_0 = 0$, so $Z(1) = 0$. If $k = m$, $\varphi$ is first cut off along the last row by a smooth function, and $H_0(g)$ is the product of a translate average of $\varphi$ with $\overline{\varphi'(g)}$. When $\pi \not\cong \pi'$, the cusp forms of $\pi$ are orthogonal to the translates of the forms of $\pi'$ over the band, so the integral of $H_0$ vanishes and $Z(1) = 0$. When $\pi \cong \pi'$, nothing is claimed about $Z(1)$. $\square$

**Example 9.14.6.** In the classical picture with $m = k = 1$, a normalised cuspidal representation of $\mathrm{GL}_1$ is a unitary Hecke character $\chi$ that is trivial on the split centre, and its Satake parameter at an unramified $w$ is $\chi(\varpi_w)$. Then $L^S(s, \alpha, \beta) = L^S(s, \chi\bar\chi')$ is a partial Hecke $L$-function. The theorem says that $(s - 1)L^S(s, \chi\bar\chi')$ is holomorphic near $s = 1$ up to a nonvanishing factor, and that it vanishes at $s = 1$ when $\chi \neq \chi'$. This is Hecke's theorem: $L(s, \chi\bar\chi')$ has a pole at $s = 1$ only when $\chi\bar\chi'$ is trivial.

**Remark 9.14.7 (Formalization).** The statement is `RSPole` in [CauchyLoc.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/CauchyLoc.lean#L46); $L^S$ is `LS` there, built from `eul` in [NewtonLow.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/NewtonLow.lean#L11), an infinite product `∏'` that is $1$ when it does not converge. The statement is weaker than the classical one in three ways: it does not say that $Z(1) \neq 0$ when $\pi \cong \pi'$ (so the pole is not proved to exist), $Z_S$ is only known to be nonzero on the one line $\operatorname{Im} s = u$, and inequivalence is the inequality of the pairs $(m, [\pi])$ and $(k, [\pi'])$. `rsPole` is `rsPole_of_inputs` applied to 22 theorems ([JacquetShalikaRigidity.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/JacquetShalikaRigidity.lean#L10)), and `rsPole_of_inputs` is about 60 steps that end in `rspole_of` ([PRSPole.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/PRSPole.lean#L35)); `rspole_of` takes `G1` as `_hG1` and does not use it. We read the statements of `E2`, `M1`, `KLt1`, `KLt2`, `KEq1`, `KEq2`, `ORT` and `KY` in [ColumnConjugationMeasure.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/ColumnConjugationMeasure.lean#L214) but not their proofs; the description of the unfolding and of the continuation above is our reading of these statements. `ORT` asks only that $\pi \neq \pi'$ as subspaces. The normalisation `IsNormalised` uses `splitCentre`, whose exponential we did not unfold. Several step names do not describe their statements: `algebraic_modulus_one_of_finiteOrder_char` proves a change of variables for the column conjugation measure, and in [ConvergenceEntriesGeneralLinearHolds.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/SmoothVectorEstimates/ConvergenceEntriesGeneralLinearHolds.lean#L1) fact (i) is `orthogonalSplitPolarizationVanishes`, fact (ii) is `addPreservesExpCongruence` and fact (iv) is `hit_valuation_bound`. In [MirabolicColumnBlock.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/SmoothVectorEstimates/MirabolicColumnBlock.lean#L18) the corner subgroup $G_n$ is a definition named `GlobalTheory`, the same word as a top namespace; the mirabolic step is `S7` (L98) and is proved by `mirabolic_induction_step_exists` in [CornerBlockIndex.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/SmoothVectorEstimates/CornerBlockIndex.lean#L12). A second, unrelated file with the name `MirabolicColumnBlock.lean` is in `Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities`.
