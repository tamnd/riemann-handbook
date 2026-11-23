---
title: The p-th power cocycle
decls:
  - PositivityTheory.HtPt.Cocp.cocycle_p
  - PositivityTheory.HtPt.Cocp.tanpf_inj
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The p-th power cocycle

This section stays in positive characteristic. A polarization $L$ of a semi-abelian variety gives a map from tangent vectors to first-order deformations of line bundles: a tangent vector $v$ goes to the class of $t_v^* L \otimes L^{-1}$. We give a condition on the tangent space, called `TanPF`, which says that this map has no kernel on tangent vectors of $p$-torsion jets. The main result shows that `TanPF` makes a linear map $\alpha$, built from the formal group and the cubical structure of $L$, injective. The key step is a cocycle computation for the $p$-th power curve through a vector $w$. The result is used in [the covolume bound](/entry/top-covol-slim2-use-alt-alt/).

Throughout, $E$ is a CM field with host datum $H$, the star map of $\mathcal{O}_E$ is the conjugation $a \mapsto \bar a$, $X$ is a scheme and $t$ is a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action and cubical line bundle $L$ ([the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube)). Let $k$ be an algebraically closed field of characteristic $p > 0$, let $x \colon \operatorname{Spec} k \to X$ be a point, and let $G$ be the fibre of $t$ at $x$. Let $J_m = k[s]/(s^{m+1})$.

**Definition 7.10.1 (Translation difference).** Let $T$ be a scheme over $X$ and $y \colon T \to G$ a point. The *translation difference* of $L$ along $y$ is the line bundle $\mu^*(y \times \mathrm{id})^* L \otimes \mathrm{pr}_2^* L^{-1}$ on $T \times G$, where $\mu$ is the group law. In short, it is $t_y^* L \otimes L^{-1}$.

**Definition 7.10.2 (Germ matrices).** Let $g$ be a formal germ of $t$ at $x$ of dimension $d$, as in [the section on free Hodge modules](/entry/at-point/): a formal group of dimension $d$ over $k$ with an action $a \mapsto [a]$ of $\mathcal{O}_E$, a chart into $G$, and series that express the cubical structure of $L$ in the chart. Let $\varphi_1(u, x, y)$ be the first of these series, and put
$$\Phi_p(x, y) = \prod_{n=0}^{p-1} \varphi_1([n]x, x, y).$$
Define two $d \times d$ matrices over $k$:

1. $W$, with $W_{ij}$ the coefficient of $x_j^p$ in the $i$-th coordinate of $[p](x)$;
2. $A$, with $A_{ij}$ the coefficient of $x_i^p y_j$ in $\Phi_p(x, y)$.

Let $\alpha \colon k^d \to k^d \times k^d$ be the linear map $\alpha(u) = (W u, A^{\mathsf{T}} u)$.

The map $\alpha$ tests two things at the same time. The first part is the degree $p$ term of multiplication by $p$. The second part is the term of the cubical structure along $p$-th powers that is linear in $y$.

**Definition 7.10.3 (The p-th power curve).** For $w \in k^d$ let $y_w \colon \operatorname{Spec} J_p \to G$ be the jet of the chart of $g$ at order $p$, composed with the substitution $x_j \mapsto w_j s$. Let $y_w^{(1)}$ be its restriction to $\operatorname{Spec} J_1$. This is the tangent vector $w$ at the origin.

**Definition 7.10.4 (Tangent condition).** The point $x$ satisfies the *tangent condition* `TanPF` at $p$ if, for each jet $y \colon \operatorname{Spec} J_p \to G$ with $y(0) = 1$ and $y^p = 1$ such that the translation difference of $L$ along $y^{(1)}$ is trivial, we have $y^{(1)} = 1$.

Here $y^p$ is the $p$-th power in the group of points of $G$ with values in $J_p$, and a line bundle is trivial when it has a generator.

**Lemma 7.10.5 (The p-th power curve).** Let $w \in k^d$.

1. $y_w(0) = 1$.
2. If $W\,(w_1^p, \dots, w_d^p) = 0$, then $y_w^p = 1$.
3. If $y_w^{(1)} = 1$, then $w = 0$.

*Proof.* Part 1 holds since the substitution sends each $x_j$ into the maximal ideal of $J_p$. For part 2, the $p$-th power of $y_w$ is the chart applied to $[p](ws)$. In characteristic $p$ each coordinate of $[p](x)$ has no terms of degree less than $p$. Modulo $s^{p+1}$ only the terms of degree $p$ that are pure $p$-th powers remain, so the $i$-th coordinate is $\sum_j W_{ij} w_j^p s^p$, which is $0$ by hypothesis. For part 3, the chart is unique on first-order jets, so $y_w^{(1)} = 1$ forces $w_j s = 0$ in $J_1$ for all $j$, so $w = 0$. $\square$

**Theorem 7.10.6 (The p-th power cocycle).** Let $g$ be a formal germ of $t$ at $x$ of dimension $d$, and let $w \in k^d$ with $\alpha(w_1^p, \dots, w_d^p) = 0$. Then the translation difference of $L$ along $y_w^{(1)}$ has a generator.

Lean: `PositivityTheory.HtPt.Cocp.cocycle_p`.

*Proof sketch.* Put $u = (w_1^p, \dots, w_d^p)$. We follow the steps of the formal proof.

1. Since $W u = 0$, the lemma gives $y_w(0) = 1$ and $y_w^p = 1$.
2. In characteristic $p$ there is a series $\Gamma(x, y)$ with $\Gamma(0, y) = \Gamma(x, 0) = 1$ and $\Phi_p(x, y) = \Gamma(x_1^p, \dots, x_d^p, y)$. The coefficient of $x_i y_j$ in $\Gamma$ is $A_{ij}$.
3. Put $D(y) = \sum_i u_i\, \partial_{x_i} \Gamma(0, y)$. Its linear part is $\sum_j (A^{\mathsf{T}} u)_j\, y_j$. Since $\alpha(u) = 0$, all partial derivatives $\partial_{y_j} D$ are $0$.
4. The fibre $G$ is integral and normal, and its function field has characteristic $p$. For a regular function $c$ on a chart of $L$ near the origin, there is a power series $F$ that expands $c$ along the germ. If all partial derivatives of $F$ are $0$, then $c$ is a $p$-th power in the function field.
5. The cubical structure and $y_w^p = 1$ give a generator $C$ of the $p$-th power of the translation difference of $L$ along $y_w$. It is $1$ along the zero section, and on the chart its top coefficient in $s$ agrees, at every finite order, with $v^p - D$ for some $v$.
6. Choose a chart of $L$ that contains the origin. Write $C = \sum_{i=0}^{p} c_i\, \delta^i$ on this chart, with $\delta$ the jet parameter. By step 5 the expansion $F$ of $c_p$ agrees at each order with $v^p - D$. The derivatives of $v^p$ are $0$ in characteristic $p$, and those of $D$ are $0$ by step 3. So the derivatives of $F$ are $0$, and $c_p$ is a $p$-th power by step 4.
7. On a normal integral scheme in characteristic $p$, a generator of the $p$-th power of the translation difference along a jet of order $p$ gives a generator of the translation difference at first order, if it is $1$ along the zero section and its top coefficient is a $p$-th power. This gives the claim. $\square$

**Theorem 7.10.7 (The tangent condition makes alpha injective).** Let $g$ be a formal germ of $t$ at $x$ of dimension $d$. If $x$ satisfies `TanPF` at $p$, then $\alpha$ is injective.

Lean: `PositivityTheory.HtPt.Cocp.tanpf_inj`.

*Proof.* Let $\alpha(u) = 0$. Since $k$ is algebraically closed, there is $w \in k^d$ with $w_i^p = u_i$ for all $i$. By the lemma, $y_w(0) = 1$, and $y_w^p = 1$ since $W u = 0$. By the theorem on the $p$-th power cocycle, the translation difference of $L$ along $y_w^{(1)}$ is trivial. `TanPF` then gives $y_w^{(1)} = 1$, and part 3 of the lemma gives $w = 0$. So $u = 0$. $\square$

The argument turns a geometric condition on tangent vectors into a rank condition on two matrices of power series coefficients. Only $p$-th powers of vectors appear in the cocycle theorem. This is why the proof of injectivity needs the $p$-th roots, and with them an algebraically closed field.

**Remark 7.10.8 (Formalization).** Both theorems are in [CocpMain.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/CocpMain.lean#L20), at lines 20 and 85. `TanPF` is in [ToFirst.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ToFirst.lean#L47), line 47, with the truncation `toFirst` at line 44. The matrix $W$ is `hw` and $\alpha$ is `alpha` in [GermComp1ZeroPointLeft.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/GermComp1ZeroPointLeft.lean#L35), lines 35 and 47; injectivity of $\alpha$ is `ConjInj`, line 104. The translation difference is `Out.translDiff` in [NonzeroLocus.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/NonzeroLocus.lean#L50). The lemma on the $p$-th power curve is `pt_of_vec` in [IsPullbackWhisker.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/IsPullbackWhisker.lean#L422), line 422. Steps 2 and 3 of the sketch are `pow_one_series_p_formula` and `alpha_kernel_derivative_vanishes`, step 4 is `formal_germ_jet_lift`, step 5 is `Coc.Pf.pfold`, and step 7 is `Qam.core_firstOrder` in [QamCore.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/QamCore.lean#L370). We did not open their proofs, and the descriptions above come from their statements. The theorem `tanpf_inj` is one line: it applies `Ce.tanpf_inj_of` (line 482 of IsPullbackWhisker.lean), which takes the cocycle theorem as a hypothesis. The cocycle theorem asks for `1 ≤ p` next to `Fact p.Prime`. The names `IsPullbackWhisker` and `formal_germ_jet_lift` do not describe the content: the second also supplies the integrality and normality of the fibre.
