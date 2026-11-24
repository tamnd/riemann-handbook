---
title: Iwahori eigenvectors at an inert place
decls:
  - PositivityTheory.SphericalProduct.extremeU
  - PositivityTheory.Rg.BcB.F.Eig.absEig
  - PositivityTheory.Rg.BcB.F.Eig.eigInert
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Iwahori eigenvectors at an inert place

At a finite place that is inert in the CM extension, the comparison of trace formulas uses Iwahori-Hecke operators, not only spherical ones, because their eigenvalues separate the Satake parameters by size. This section proves that an unramified irreducible representation of a unitary group at an inert place has a nonzero Iwahori fixed vector that is a common eigenvector of the Hecke operators of strictly dominant elements. The eigenvalues are monomials in a reordering $\beta$ of the Satake parameters with $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$. The result feeds [frame existence from finiteness](/entry/frame-ex-of-fin/), which leads to the step [BaseChangeN](/step/base-change-n/). The background is in [unramified representations](/learn/representations/#unramified-representations), [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module) and [unitary groups](/learn/groups/#unitary-groups).

**Definition 7.3.1 (Unramified involution).** Let $L$ be a field, complete for a discrete valuation $v$ with valuation ring $\mathcal{O}$. An unramified involution of $L$ with uniformizer $\varpi$ and residue order $q$ is a field automorphism $x \mapsto \bar x$ with $\bar{\bar x} = x$ and $v(\bar x) = v(x)$, such that $\bar\varpi = \varpi$, $\varpi$ is a uniformizer, some $x \in \mathcal{O}$ has $\bar x - x$ a unit (so the involution is nontrivial on the residue field), $q \ge 2$, and the residue field has $q^2$ elements.

So $L$ is the unramified quadratic extension of the fixed field $L_0$, the involution is its Galois conjugation, and $q$ is the order of the residue field of $L_0$.

Let $n \ge 1$, let $m = \lfloor n/2 \rfloor$, let $J$ be the antidiagonal matrix with entries $1$, and write $g^* = \bar g^{\mathsf T}$. Put
$$G = \{g \in \mathrm{GL}_n(L) : g^* J g = J\}, \qquad K = G \cap \mathrm{GL}_n(\mathcal{O}).$$
This is the quasi-split unitary group of the Hermitian form $J$, and $K$ is a hyperspecial maximal compact subgroup. Let $I \subset K$ be its Iwahori subgroup: the elements of $K$ whose reduction is upper triangular. The diagonal elements of $G$ have the form $t = \mathrm{diag}(t_1, \dots, t_n)$ with $t_{n+1-i} = \bar t_i^{-1}$. For $t$ diagonal put $a_i = v(t_i)$, and call $t$ strictly dominant if $a_1 > a_2 > \dots > a_n$.

**Definition 7.3.2 (Hecke operator of an element).** Let $\rho$ be a smooth representation of $G$ on $V$, and let $g \in G$. An operator $T$ on $V^I$ is a Hecke operator of $g$ if $\lambda(\rho(g)v) = \lambda(Tv)$ for every $v \in V^I$ and every $I$-invariant linear form $\lambda$ on $V$.

If $e_I$ is the projection onto $V^I$ given by averaging over $I$, then $T = e_I\rho(g)$ is a Hecke operator of $g$. Up to the factor $[IgI : I]$, it is the action of the characteristic function of $IgI$.

**Definition 7.3.3 (Principal series and Weyl conjugates).** For $\beta \in (\mathbb{C}^\times)^m$ and $t$ diagonal put
$$\chi_\beta(t) = \prod_{i=1}^{m}\beta_i^{a_i}\,q^{-(n+1-2i)a_i}.$$
Let $I(\beta)$ be the space of locally constant functions $\varphi$ on $G$ with $\varphi(bg) = \chi_\beta(b)\varphi(g)$ for upper triangular $b \in G$, where $\chi_\beta$ is extended to the Borel subgroup through its diagonal part, with $G$ acting by right translation. We say that $\beta$ is a Weyl conjugate of $\alpha \in (\mathbb{C}^\times)^m$ if $\beta$ comes from $\alpha$ by a permutation of the entries followed by the inversion of some entries.

The factor $q^{-(n+1-2i)a_i}$ is the square root of the modulus character of the Borel subgroup, so $I(\beta)$ is the normalized principal series with Satake parameter $\beta$. The Weyl conjugates are the orbit of $\alpha$ under the Weyl group of $G$, a group of type $C_m$ or $BC_m$.

**Theorem 7.3.4 (Extremal embedding).** Let $\rho$ be an irreducible admissible representation of $G$ on $V$ that is spherical for $K$ with Satake parameters $\alpha \in (\mathbb{C}^\times)^m$. Then there is a Weyl conjugate $\beta$ of $\alpha$ with $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$ and an injective $G$-map $V \to I(\beta)$.

Lean: `PositivityTheory.SphericalProduct.extremeU`.

*Proof.* Let $J_N(V)$ be the span of the vectors $\rho(u)v - v$ for upper unipotent $u \in G$. The Jacquet module $V/J_N(V)$ is nonzero: some vector outside $J_N(V)$ is fixed, modulo $J_N(V)$, by the diagonal elements of $K$. The diagonal torus acts on the finite-dimensional space of such vectors through commuting operators, so there is $y \notin J_N(V)$ and a character $\xi$ of the torus, trivial on its compact part, with $\rho(t)y - \xi(t)y \in J_N(V)$. A linear form that vanishes on $J_N(V)$ and is nonzero at $y$ then satisfies $\lambda(\rho(t)v) = \xi(t)\lambda(v)$. An unramified character of the torus has the form $\chi_\beta$, so $\xi = \chi_\beta$ for some $\beta$. By Frobenius reciprocity, $\lambda$ gives a nonzero $G$-map $V \to I(\beta)$, which is injective because $V$ is irreducible, and a comparison of spherical vectors shows that $\beta$ is a Weyl conjugate of $\alpha$. Last, we put $\beta$ in order. If $|\beta_i/\beta_{i+1}| < 1$ for some $i$, swap $\beta_i$ and $\beta_{i+1}$; if $|\beta_m| < 1$, invert $\beta_m$. Each move keeps an injective $G$-map into the new principal series, and after finitely many moves $\beta$ is in the required chamber. Each of these steps is proved in the companion development, and we take them as given. $\square$

**Theorem 7.3.5 (Iwahori eigenvector).** Let $\rho$ be as in the Extremal embedding theorem. Then there is a Weyl conjugate $\beta$ of $\alpha$ with $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$ and a nonzero $y \in V^I$ such that $Ty = \chi_\beta(t)y$ for every strictly dominant diagonal $t \in G$ and every Hecke operator $T$ of $t$.

Lean: `PositivityTheory.Rg.BcB.F.Eig.absEig`.

*Proof.* Take $\beta$ and an injective $G$-map $f : V \to I(\beta)$ from the [Extremal embedding theorem](/entry/extreme-u/). The Iwahori subgroup has a factorization $I = (I \cap N^-)(I \cap T_0)(I \cap N)$, in both orders, with $N$ and $N^-$ the upper and lower unipotent subgroups and $T_0$ the diagonal torus. Define a linear form on $V^I$ by $\mu(x) = f(x)(1)$. Let $t$ be dominant and let $T$ be a Hecke operator of $t$. The form $\mu$ factors through the Jacquet module for $N$, and $Tx$ and $\rho(t)x$ have the same image in the Jacquet module (this is Jacquet's lemma, and it uses the factorization of $I$ and the dominance of $t$). Since $f(\rho(t)x)(1) = \chi_\beta(t)f(x)(1)$, we get $\mu(Tx) = \chi_\beta(t)\mu(x)$. Next, $\mu \neq 0$: a nonzero $K$-fixed vector $x$ lies in $V^I$, and if $f(x)(1) = 0$ then $f(x) = 0$, since a $K$-fixed vector of $I(\beta)$ is determined by its value at $1$; this contradicts the injectivity of $f$. The space $V^I$ has finite dimension, by admissibility, and the Hecke operators of dominant elements commute with each other. A commuting family of operators on a finite-dimensional space with a common nonzero eigenform $\mu$ has a common eigenvector with the same eigenvalues. A strictly dominant element is dominant. This gives $y$. $\square$

For the Iwahori fixed vectors of unramified representations and their relation to the Jacquet module, see A. Borel, *Admissible representations of a semi-simple group over a local field with vectors fixed under an Iwahori subgroup*, Invent. Math. 35 (1976).

We now move the result to the unitary group that appears in the global setting. Let $E$ be a CM field and $w$ a finite place of $E$ that is not split over the maximal totally real subfield, and let $E_w$ carry the conjugation $x \mapsto \bar x$. Let
$$U = \{g \in \mathrm{GL}_n(E_w) : g^* g = 1\}, \qquad K_U = U \cap \mathrm{GL}_n(\mathcal{O}_w).$$
Suppose $b \in \mathrm{GL}_n(\mathcal{O}_w)$ satisfies $b^* b = J$ (a Witt basis). Then $g \mapsto b^{-1}gb$ maps $U$ onto $G$ and $K_U$ onto $K$. Let $I_0$ be the standard Iwahori subgroup of $\mathrm{GL}_n(\mathcal{O}_w)$ and $I_U = U \cap bI_0b^{-1}$. For $l \in \mathbb{Z}^m$ let
$$t_l = \mathrm{diag}(\varpi^{l_1}, \dots, \varpi^{l_m}, 1, \dots, 1, \varpi^{-l_m}, \dots, \varpi^{-l_1}),$$
with one entry $1$ in the middle if $n$ is odd and none if $n$ is even. Call $l$ a cone point if $l_i \ge 2$ and $l_i - l_{i+1} \ge 2$ for all $i$, with $l_{m+1} = 0$. For a compact open subgroup $K'$ of $K_U$ and a function $\phi$ on $U$ that is bi-invariant under $K'$, write
$$\mathcal{L}_{K'}(\phi) = \frac{1}{[K_U : K']}\sum_{g \in U/K'}\phi(g)\,\sigma(g).$$

**Theorem 7.3.6 (Iwahori eigenvalues at an inert place).** Let $\varpi$ be a uniformizer of $E_w$ with $\bar\varpi = \varpi$, and assume that conjugation is an unramified involution of $E_w$ with uniformizer $\varpi$ and residue order $q$. Let $b$ be as above. Let $\sigma$ be a smooth irreducible admissible representation of $U$ whose transport to $G$ is spherical for $K$ with Satake parameters $\alpha$. Then there is a Weyl conjugate $\beta$ of $\alpha$ with $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$ and a nonzero $y \in \sigma^{I_U}$ such that for every cone point $l$,
$$\mathcal{L}_{I_U}\big(\mathbf{1}_{I_U b t_l b^{-1} I_U}\big)\,y = \frac{1}{[K_U : I_U]}\,q^{\sum_i (n+1-2i)l_i}\prod_{i=1}^m\beta_i^{l_i}\;y.$$

Lean: `PositivityTheory.Rg.BcB.F.Eig.eigInert`.

*Proof.* Transport $\sigma$ to $G$ by conjugation with $b$. The transported representation is irreducible and admissible, $I_U$ goes to $I = G \cap I_0$, and $bt_lb^{-1}$ goes to $t_l$, which is strictly dominant since $l$ is a cone point. The [Iwahori eigenvector theorem](/entry/abs-eig/) gives $\beta$ and $y$ with $Ty = \chi_\beta(t_l)y$ for the Hecke operator $T$ of $t_l$. For a compact open subgroup $J \subset K$ and $t \in G$, the average of the characteristic function of $JtJ$ is
$$\mathcal{L}_J(\mathbf{1}_{JtJ}) = \frac{[J : J \cap tJt^{-1}]}{[K : J]}\,T,$$
since $JtJ$ is the union of $[J : J \cap tJt^{-1}]$ cosets $jtJ$ and $\sigma(j)$ acts trivially after the projection to $\sigma^J$. For a cone point the index is $[I : I \cap t_lIt_l^{-1}] = q^{2\sum_i(n+1-2i)l_i}$. Finally $\chi_\beta(t_l) = \prod_i\beta_i^{l_i}q^{-(n+1-2i)l_i}$. Multiplying gives the formula. $\square$

**Remark 7.3.7 (Formalization).** The statements `AbsEig` and `EigInert` are in UniformizerValuations/EigInert.lean, and $\chi_\beta$ is `chiDeltaU` (StatementF.lean:40), with indices from $0$, so the exponent there is $-(n-1-2i)a_i$. The unramified involution is `IsUnramInv` (StatementF.lean:14). The Satake condition `HasSatU` and the standard Iwahori subgroup `iwGL` were not unfolded. The proof of `extremeU` chains eight `GlobalTheory.T` lemmas (Jacquet module nonzero, eigenvector, equivariant form, characters, Frobenius reciprocity, chamber decomposition with swap and inversion steps), whose proofs we have not unfolded. The condition that $w$ is not split is `¬ IsSplitAt`, which we did not unfold. `absEig` is at AbsEigB.lean:269, with the eigenform argument in `main_D` at line 224; the factorization of $I$ and Jacquet's lemma are `GlobalTheory.T` inputs. `eigInert` is `eigInertOf absEig heckeSum indexU`. In `eigInertOf` (AdmissibleTransport.lean:304 to 305) the hypothesis `IsUnifAt ϖ` is bound as `_` and is never used; it says $\operatorname{ord}\varpi = 1$ and $\bar\varpi = \varpi$, which `IsUnramInv` already gives. Of the Witt condition only $b \in \mathrm{GL}_n(\mathcal{O}_w)$ is used, not $b^*b = J$. The factor $q$ appears in the statement as `dlt`, built from the square root of the norm of $w$, which `qh_eq` (AdmissibleTransport.lean:265) identifies with $q$. The cone condition is stronger than the strict dominance that the proof needs.
