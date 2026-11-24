---
title: Truncation and the non-elliptic terms
decls:
  - PositivityTheory.Rg.BcB.CV.locVanish
  - PositivityTheory.Rg.BcB.CV.classVanish_of_steps
  - PositivityTheory.Rg.BcB.CV.classVanish
  - PositivityTheory.Rg.BcB.CV.classVanish2
  - PositivityTheory.Rg.BcB.CV.ellFormula2J
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Truncation and the non-elliptic terms

This section computes the geometric side of a truncated twisted trace formula for $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ over a CM field. The test functions are very cuspidal at the archimedean places. For such functions, and for a truncation parameter that is large compared with the support, the truncated trace is the sum of the twisted orbital integrals over the regular elliptic classes. The non-elliptic regular classes give zero. The source of the vanishing is a local fact at one complex place: the twisted orbital integral of a very cuspidal function against a weight that is invariant under a unipotent radical is zero. The result is the input of [the elliptic terms](/entry/global-character-of-finite-inputs/) on the general linear side. For the twisted trace formula in general see [the twisted trace formula and base change](/learn/trace-formula/#the-twisted-trace-formula-and-base-change) and Arthur and Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*, Annals of Math. Studies 120 (1989).

Let $E$ be a CM field with complex conjugation $c$, let $\mathbb{A}$ be its adele ring, and write $G = \mathrm{GL}_n$. Let $\theta(g) = {}^t\bar g^{-1}$, where the bar is $c$ on $E$ and on $\mathbb{A}$, and complex conjugation on $\mathrm{GL}_n(\mathbb{C})$. The twisted conjugate of $\delta$ by $x$ is $x^{-1}\delta\theta(x)$, and the twisted centralizer $C_\delta$ is the group of $x$ with $x\delta = \delta\theta(x)$. The norm of $\delta$ is $N\delta = \delta\theta(\delta)$.

**Definition 7.6.1 (Quotient integral).** Let $H$ be a closed subgroup of a locally compact group $G$, with Haar measures $\mu$ on $G$ and $\mu_H$ on $H$. A normalizer is a nonnegative measurable $\rho$ on $G$ with $\int_H \rho(hg)\,d\mu_H(h) = 1$ for all $g$. For $F$ on $G$ invariant on the left under $H$, the quotient integral is $\int_{H\backslash G} F = \int_G F\rho\,d\mu$. We fix one normalizer for each pair $(H, \mu_H)$. If no normalizer exists, the quotient integral is defined to be $0$.

**Definition 7.6.2 (Regular and regular elliptic).** An element $\delta \in \mathrm{GL}_n(E)$ is regular if the characteristic polynomial of $N\delta$ is separable. It is regular elliptic if it is regular and, for every embedding $E \to \mathbb{C}$, every root of the image of that polynomial has absolute value $1$.

**Definition 7.6.3 (Isotropic flag).** Let $d \in \mathrm{GL}_n(\mathbb{C})$. For a subspace $W \subset \mathbb{C}^n$ let $W^{\perp_d} = d\,W^\perp$, where $W^\perp$ is the orthogonal complement for the form $\sum_i \bar x_i y_i$. A $d$-isotropic flag is a pair $0 \ne W_1 \subseteq W_2$ with $W_1^{\perp_d} = W_2$ and $W_2^{\perp_d} = W_1$. Its nilradical $\mathfrak{n}(W_1, W_2)$ is the space of matrices $X$ with $X\mathbb{C}^n \subseteq W_2$, $XW_2 \subseteq W_1$ and $XW_1 = 0$. Write $u_X = 1 + X$.

**Definition 7.6.4 (Very cuspidal).** A function $f$ on $\mathrm{GL}_n(\mathbb{C})$ is very cuspidal if:

1. $f(k^{-1}d\theta(k)) = f(d)$ for every $k$ with $\theta(k) = k$, that is $k \in U(n)$;
2. for every $d$, every $d$-isotropic flag $(W_1, W_2)$ and every Haar measure $\nu$ on $\mathfrak{n}(W_1, W_2)$, $\int f(u_X d)\,d\nu(X) = 0$.

A function $\varphi$ on $\mathrm{GL}_n(\mathbb{A})$ is very cuspidal at a complex place $v$ if, for every $g$ whose component at $v$ is $1$, the function $d \mapsto \varphi(d\,g)$ on $\mathrm{GL}_n(E_v) = \mathrm{GL}_n(\mathbb{C})$ is very cuspidal.

Condition 2 is a twisted form of the vanishing of constant terms (see [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms)). It is a condition at every $d$, not only along a fixed parabolic subgroup.

**Theorem 7.6.5 (Local vanishing).** Let $f$ be continuous, compactly supported and very cuspidal on $\mathrm{GL}_n(\mathbb{C})$. Let $d$ be regular, in the sense that $N d$ has separable characteristic polynomial, and let $(W_1, W_2)$ be a $d$-isotropic flag. Let $u$ be a measurable function, bounded on compact sets, with $u(xk) = u(x)$ for $k \in U(n)$, $u(tx) = u(x)$ for $t \in C_d$, and $u(mx) = u(x)$ for every $m$ with $m - 1 \in \mathfrak{n}(W_1, W_2)$. Then
$$\int_{C_d\backslash \mathrm{GL}_n(\mathbb{C})} f(x^{-1}d\theta(x))\,u(x)\,dx = 0.$$

Lean: `PositivityTheory.Rg.BcB.CV.locVanish`.

*Proof.* Put $F(x) = f(x^{-1}d\theta(x))u(x)$. It is invariant on the left under $C_d$ and on the right under $U(n)$, by condition 1. We use two facts from the companion development. First, there is a continuous map $\Phi$ of $\mathfrak{n}(W_1, W_2)$ to itself with
$$u_{\Phi(X)} = u_X^{-1}\,d\,\theta(u_X)\,d^{-1},$$
and $\Phi$ maps a Haar measure to a multiple of itself. Second, a function $F$ with these two invariance properties has quotient integral $0$ if $\int F(u_X q)\,d\nu(X) = 0$ for every $q$ and every Haar measure $\nu$ on $\mathfrak{n}(W_1, W_2)$. To check this condition, use the invariance of $u$ to write $F(u_X q) = u(q)\,f(q^{-1}u_X^{-1}d\theta(u_X)\theta(q))$. By the first fact, $u_X^{-1} d\theta(u_X) = u_{\Phi(X)}d$, and the change of variables $Y = \Phi(X)$ turns the integral over $X$ into a multiple of $\int f(q^{-1}u_Y d\theta(q))\,d\nu(Y)$. This is the integral of condition 2 for the twisted conjugate $q^{-1}d\theta(q)$ and the flag $(q^{-1}W_1, q^{-1}W_2)$, so it is $0$. $\square$

Now we come to the global objects. Let $x \in \mathrm{GL}_n(\mathbb{A})$. For a subspace $W \subseteq E^n$ with basis matrix $M$, let $A = x^{-1}M$ and put
$$\deg_x W = -\Big(\sum_{v \mid \infty}\log\det(A_v^*A_v) + \sum_{w < \infty}\log\max_s|\det A_{w,s}|_w\Big),$$
where $A_{w,s}$ runs over the square submatrices of maximal size. This does not depend on the basis.

**Definition 7.6.6 (Truncation).** For $\tau \in \mathbb{R}$, the set $\mathcal{C}_\tau$ consists of the $x$ with $\deg_x W \le \tau k(2n + 1 - k)$ for every subspace $W$ of dimension $k$, and $\deg_x E^n \ge -\tau$. Let $\chi_\tau$ be its indicator. For a test function $\varphi$ (continuous, compactly supported, bi-invariant under an open subgroup at the finite places) let $K(x,y) = \sum_{\delta \in \mathrm{GL}_n(E)}\varphi(x^{-1}\delta\theta(y))$. With $\mathcal{F}$ a fundamental domain for $\mathrm{GL}_n(E)$, the truncated twisted trace is
$$T_\tau(\varphi) = \int_{\mathcal F}\chi_\tau(x)K(x,x)\,dx,$$
and the cut term of $\delta \in \mathrm{GL}_n(E)$ is
$$J_\tau(\varphi, \delta) = \int_{C_\delta(E)\backslash \mathrm{GL}_n(\mathbb{A})}\chi_\tau(x)\,\varphi(x^{-1}\delta\theta(x))\,dx.$$
Set $\ell(g) = \sum_v \log^+\max_{i,j}|g_{ij}|_v + \sum_v\log^+\max_{i,j}|(g^{-1})_{ij}|_v$, with the square of the absolute value at the complex places. We say $\varphi$ has size at most $r$ if $\ell(g) \le r$ on the support of $\varphi$. The orbital term $O(\varphi, \delta)$ is $J_\tau(\varphi, \delta)$ without the factor $\chi_\tau$.

The set $\mathcal{C}_\tau$ is cut out by bounds on the degrees of all rational subspaces. The profile $\tau k(2n + 1 - k)$ grows with $\tau$, so the sets $\mathcal{C}_\tau$ grow with $\tau$.

**Theorem 7.6.7 (Vanishing of non-elliptic classes, conditional form).** Assume that $E$ has at least two archimedean places. Assume the following inputs:

1. the Local vanishing theorem above, and a properness statement: for $d$ regular and $C$ compact, the set of $x$ with $x^{-1}d\theta(x) \in C$ lies in $C_d\,C'$ for a compact $C'$;
2. for $\delta$ regular and not elliptic, there are a complex place $v$ and a $\delta_v$-isotropic flag in $\mathbb{C}^n$;
3. the description of $\chi_\tau(tx)$, for $t$ in the adelic twisted centralizer and $\tau$ larger than a constant times $1 + \ell(x^{-1}\delta\theta(x))$, by an explicit chain function of the numbers $\tau k(2n+1-k) - \deg_x W$ over the $\delta$-stable isotropic rational subspaces $W$;
4. standard facts on the degree, on the discreteness of rational centralizers in adelic ones, on the finiteness of the kernel sum, on Mahler compactness, and on the decomposition $\mathrm{GL}_n(\mathbb{A}) = \mathrm{GL}_n(\mathbb{C}) \times G'$ at one or two complex places.

Then there is a constant $C$ with the following property. Let $\varphi$ be a test function of size at most $r$, very cuspidal at every complex place, and let $\tau \ge C(1 + r)$. If $\delta$ is regular and not elliptic, then $J_\tau(\varphi, \delta) = 0$.

Lean: `PositivityTheory.Rg.BcB.CV.classVanish_of_steps`.

*Proof.* Write the cut term as an iterated integral: first over $C_\delta(E)\backslash C_\delta(\mathbb{A})$, then over $C_\delta(\mathbb{A})\backslash\mathrm{GL}_n(\mathbb{A})$. By input 3, the inner integral of $\chi_\tau(tx)$ over $t$ is a function $V$ of the vector of numbers $\tau k(2n+1-k) - \deg_x W$, where $W$ runs over the $\delta$-stable isotropic subspaces. If there is no such $W$, the cut term is a multiple of the orbital integral of $\varphi$ over $C_\delta(\mathbb{A})\backslash \mathrm{GL}_n(\mathbb{A})$. By input 2 there is a complex place $v$ with an isotropic flag. Split off the factor at $v$ and apply the Local vanishing theorem at $v$ with $u = 1$; the orbital integral is $0$. If there are such subspaces, $V$ changes along the directions of the flags, and we use the differences of $V$. Each difference is a weight $u$ that satisfies the invariance hypotheses of the Local vanishing theorem at one complex place, or at two distinct complex places for the terms that involve two flags. This is where we use the two archimedean places. Each term then vanishes by the Local vanishing theorem and by properness, which makes the integrals converge. The constant $C$ is the maximum of the constants of inputs 3 and 4. $\square$

**Theorem 7.6.8 (Vanishing of non-elliptic classes).** Assume that $E$ has at least two archimedean places. There is a constant $C$ such that $J_\tau(\varphi, \delta) = 0$ for every test function $\varphi$ of size at most $r$ that is very cuspidal at every complex place, every $\tau \ge C(1 + r)$, and every regular $\delta$ that is not elliptic.

Lean: `PositivityTheory.Rg.BcB.CV.classVanish`.

*Proof.* This is the conditional form applied to the Local vanishing theorem and to the inputs 1 to 4, which are proved in the companion development. $\square$

The hypothesis on the archimedean places holds in our setting. If every finite place of $E$ is unramified over its maximal real subfield $F$, then $F \ne \mathbb{Q}$, because $\mathbb{Q}$ has no nontrivial extension unramified at every finite place. So $E$ has at least two complex places.

For the group $\mathrm{GL}_a \times \mathrm{GL}_b$ we use the same notation with pairs. A test function $\varphi$ on $\mathrm{GL}_a(\mathbb{A}) \times \mathrm{GL}_b(\mathbb{A})$ of size at most $r$ is a continuous, compactly supported function, bi-invariant under an open subgroup at the finite places, of size at most $r$ in each variable, such that for every fixed value of one variable it is a test function in the other variable that is very cuspidal at the complex places and supported on regular classes. The cut term $J_\tau(\varphi, \delta_1, \delta_2)$ uses $\chi_\tau(x_1)\chi_\tau(x_2)$.

**Corollary 7.6.9 (Pairs).** Assume that $E$ has at least two archimedean places. There is a constant $C$ such that, for every test function $\varphi$ of size at most $r$ on $\mathrm{GL}_a \times \mathrm{GL}_b$, every $\tau \ge C(1 + r)$ and all regular $\delta_1$, $\delta_2$ that are not both elliptic, $J_\tau(\varphi, \delta_1, \delta_2) = 0$.

Lean: `PositivityTheory.Rg.BcB.CV.classVanish2`.

*Proof.* Let $C_a$ and $C_b$ be the constants of the Theorem for $\mathrm{GL}_a$ and $\mathrm{GL}_b$, and let $C = \max(0, C_a, C_b)$. If $1 + r \ge 0$, then $\tau \ge C_a(1 + r)$ and $\tau \ge C_b(1 + r)$. Suppose $\delta_1$ is elliptic, so $\delta_2$ is not. By the slice formula, the cut term is the quotient integral over $x_1$ of $\chi_\tau(x_1)$ times the cut term for $\mathrm{GL}_b$ of the function $g \mapsto \varphi(x_1^{-1}\delta_1\theta(x_1), g)$. That function is a test function of size at most $r$ and very cuspidal, so its cut term at $\delta_2$ vanishes by the Theorem. Hence the integrand is $0$. If $\delta_1$ is not elliptic, slice in the other order. If $1 + r < 0$, the support of $\varphi$ is empty because $\ell \ge 0$, and the cut term is $0$. $\square$

**Theorem 7.6.10 (Elliptic expansion for pairs).** Assume that $E$ has at least two archimedean places. There is a constant $C \ge 0$ such that, for every test function $\varphi$ of size at most $r \ge 0$ on $\mathrm{GL}_a \times \mathrm{GL}_b$ and every $\tau \ge C(1 + r)$,
$$T_\tau(\varphi) = \sum_{(\delta_1, \delta_2)} O(\varphi, \delta_1, \delta_2),$$
where the sum runs over the pairs of twisted conjugacy classes in $\mathrm{GL}_a(E)$ and $\mathrm{GL}_b(E)$ that are both regular elliptic.

Lean: `PositivityTheory.Rg.BcB.CV.ellFormula2J`.

*Proof.* We use two inputs from the companion development. The first is the unfolding: the truncated trace is the finite sum of the cut terms over the pairs of twisted classes. The second is the elliptic truncation bound: there is a constant $C_1$ such that, if $\delta$ is regular elliptic and $\tau \ge C_1(1 + \ell(x^{-1}\delta\theta(x)))$, then $x \in \mathcal{C}_\tau$. Let $C$ be the maximum of $0$, the elliptic constants for $a$ and $b$, and the constant of the Corollary. Take one pair of classes. If both are regular elliptic, then at each $x$ where the integrand is not $0$, the size bound gives $\ell(x_i^{-1}\delta_i\theta(x_i)) \le r$, so $x_1$ and $x_2$ lie in the truncation sets, and the cut term equals the orbital term. If both are regular but not both elliptic, the cut term is $0$ by the Corollary. If one of them is not regular, the integrand is $0$ because $\varphi$ is supported on regular classes. $\square$

**Remark 7.6.11 (Formalization).** The statements are `LocVanish` (OnlyIsotropic.lean:88), `ClassVanish` (OnlyIsotropic.lean:113) and `ClassVanish2`, `EllFormula2J` (QuotIntegralZero.lean:40 and 46). The quotient integral is `quotIntegral` (InvTransposeGLInvTransposeGL.lean:388); it returns $0$ when no normalizer exists, as in the Definition, so a statement that a quotient integral is $0$ is weaker than it looks unless a normalizer is known to exist. `locVanish` (QuotVanishL.lean:18) is `locVanish_of nilChange_of_flag quotVanishL`; the two facts in its proof are `NilChange` and `QuotVanish`. `classVanish_of_steps` (ClassVanishOfSteps.lean:19) takes 18 hypotheses and chains intermediate steps (`OneVanish`, `TwoVanish`, `Glob1`, `Glob2`, `ChiGam` and others); its proof above follows the shape of these steps, not unfolded proofs. `classVanish` (ClassVanish.lean:24) supplies the hypotheses. `classVanish2` and `ellFormula2J` (EllFormula2J.lean:10 and 12) apply `classVanish2_of` and `ellFormula2_of`, with the slice formula and the unfolding from `GlobalTheory.CompanionTheory`. The statement `TwoPlaces` (OnlyIsotropic.lean) records the argument about two archimedean places. Two different statements named `SplitAt` exist, one in NonEllFlag.lean:73 and one in BaseChangeIsobaricOf.lean:31, in different namespaces.
