---
title: The regularized mass near a small set
decls:
  - GlobalTheory.CompanionTheory.VarLelong.regMassNearSmall
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The regularized mass near a small set

Let $Z(J) \subseteq \mathbb{C}^n$ be an irreducible affine variety of dimension $d+1$. The Poincaré and Lelong formula on $Z(J)$ is proved by approximation: $\log |\ell_u|$ is replaced by the smooth function $\tfrac12 \log(|\ell_u|^2 + \varepsilon)$, and one takes the limit $\varepsilon \to 0$. To control the limit, one must know that the mixed Monge and Ampère measures of the regularized functions put little mass near a set of dimension less than $d$, uniformly in $\varepsilon$. This section proves this bound. The proof covers the small set by few balls and uses a bound on the mass of one ball. The result is an input of the [literature step](/step/every-character-of-literature/).

We keep the notation of Sections 7 to 9. For $u \in \mathbb{C}^n$ let $\ell_u(x) = \sum_j u_j x_j$. For $\varepsilon > 0$ let
$$\lambda_{u,\varepsilon}(x) = \tfrac12 \log\big(|\ell_u(x)|^2 + \varepsilon\big),$$
a smooth function on $\mathbb{C}^n$. On $\mathbb{C}^n$ and on $\mathbb{C}^k$ we use the norm $|x| = \max_i |x_i|$, so a ball $B(c, r)$ is a polydisc.

**Definition 7.11.1 (Finite projection).** Let $J$ be an ideal of $\mathbb{C}[x_1, \dots, x_n]$ and $A$ a complex $k \times n$ matrix. Then $A$ is a *finite projection* for $J$ if the map $\mathbb{C}[y_1, \dots, y_k] \to \mathbb{C}[x]/J$ with $y_i \mapsto \sum_j A_{ij} x_j$ is injective and finite.

This is a Noether normalization by linear forms. If $A$ is a finite projection, the map $x \mapsto Ax$ from $Z(J)$ to $\mathbb{C}^k$ is finite and surjective, and each fibre is finite.

**Definition 7.11.2 (Sheet).** Let $A$ be a $k \times n$ matrix and $x \in Z(J)$. A *sheet of $Z(J)$ over $A$ at $x$* is a map $s : \mathbb{C}^k \to \mathbb{C}^n$ with an open set $V \ni Ax$ such that $s$ is holomorphic on $V$, $s(Ax) = x$, $A s(y) = y$ and $s(y) \in Z(J)$ for $y \in V$, and each point $x'$ of $Z(J)$ near $x$ with $Ax' \in V$ is $s(Ax')$.

So near $x$ the variety is the graph of $s$ over $V$. A sheet exists at the points of $Z(J)$ where the projection is a local biholomorphism.

**Definition 7.11.3 (Integral over the variety).** Let $A$ be a $k \times n$ matrix, $f$ a function on $\mathbb{C}^n$ and $\psi_1, \dots, \psi_k$ real functions on $\mathbb{C}^n$. For $y \in \mathbb{C}^k$, the *chart density* is
$$\rho_A(f; \psi)(y) = \sum_{x} f(x) \, M(\psi_1 \circ s_x, \dots, \psi_k \circ s_x)(y),$$
where the sum runs over the points $x \in Z(J)$ with $Ax = y$ at which a sheet $s_x$ exists, and $M(g_1, \dots, g_k)$ is the density of the mixed Monge and Ampère measure $dd^c g_1 \wedge \cdots \wedge dd^c g_k$ with respect to the Lebesgue measure on $\mathbb{C}^k$. The *chart integral* is $\int_{\mathbb{C}^k} \rho_A(f; \psi)(y) \, dy$. If $J$ has a finite projection $A$ to $\mathbb{C}^k$, the *integral over the variety* $\int_{Z(J)} f \, dd^c \psi_1 \wedge \cdots \wedge dd^c \psi_k$ is the chart integral for one chosen such $A$. If there is no finite projection, it is $0$.

A point with no sheet is a branch point of the projection. These points lie over a proper algebraic subset of $\mathbb{C}^k$, which has measure zero, so they do not change the integral.

**Theorem 7.11.4 (Regularized mass near a small set).** Let $J$ be a prime ideal of $\mathbb{C}[x_1, \dots, x_n]$ with $\dim \mathbb{C}[x]/J = d+1$, and let $u \in \mathbb{C}^n$ with $\ell_u \notin J$. Let $\varphi_1, \dots, \varphi_d$ be real functions that are smooth on an open set that contains $Z(J)$. Let $I$ be an ideal with $\dim \mathbb{C}[x]/I < d$, and let $f$ be a continuous function with compact support. Then for each $\delta > 0$ there is an open set $U \supseteq Z(I)$ with the following property. For each continuous $\chi$ with $|\chi| \leq 1$ and support in $U$, and each $\varepsilon \in (0, 1]$,
$$\Big| \int_{Z(J)} \chi f \, dd^c \lambda_{u,\varepsilon} \wedge dd^c \varphi_1 \wedge \cdots \wedge dd^c \varphi_d \Big| \leq \delta.$$

Lean: `GlobalTheory.CompanionTheory.VarLelong.regMassNearSmall`.

The set $Z(I)$ has dimension at most $d - 1$, two less than the dimension of $Z(J)$. The bound is uniform in $\varepsilon$, and this is the point. The measures $dd^c \lambda_{u,\varepsilon}$ concentrate on $\{\ell_u = 0\}$ as $\varepsilon \to 0$, but they do not put mass on sets of this small dimension.

*Proof.* If $J$ has no finite projection to $\mathbb{C}^{d+1}$, all the integrals are $0$ by definition, and $U = \mathbb{C}^n$ works. So let $A$ be the chosen finite projection. Let $K$ be the support of $f$, a compact set. Write $\eta(x) = \sum_j |x_j|^2$. We take as given three inputs.

1. *Comparison of forms.* There is $C_1 \geq 0$ such that, for each $u$, each $\varepsilon > 0$, each function $v$ and each function $w \geq 0$ with $|v| \leq w$ on $K$, and each $y$,
$$\rho^{\mathrm{abs}}_A(v f; \lambda_{u,\varepsilon}, \varphi)(y) \leq C_1 \, \rho_A(w; \lambda_{u,\varepsilon}, \eta, \dots, \eta)(y),$$
where $\rho^{\mathrm{abs}}$ is the chart density with each term replaced by its absolute value. Since the $\varphi_i$ are smooth near $Z(J)$ and $f$ is bounded with compact support, each $dd^c \varphi_i$ is bounded by a multiple of the Euclidean form $dd^c \eta$ on $K$.
2. *Mass of a ball.* There is $C_2 \geq 0$ such that, for each $\varepsilon \in (0, 1]$, each $c \in K$ and each $r \in (0, 1]$, the chart density of the indicator of $B(c, r)$ with the functions $\lambda_{u,\varepsilon}, \eta, \dots, \eta$ is integrable, and
$$\int \rho_A(\mathbf{1}_{B(c,r)}; \lambda_{u,\varepsilon}, \eta, \dots, \eta)(y) \, dy \leq C_2 \, r^{2d}.$$
This is a bound on the Lelong numbers, uniform in $\varepsilon$ and the centre.
3. *Few balls cover a small set.* There is $C_3 \geq 0$ such that for each $r \in (0, 1]$ there is a finite set $T \subseteq Z(I) \cap K$ with $Z(I) \cap K \subseteq \bigcup_{c \in T} B(c, r)$ and $|T| \, r^{2d} \leq C_3 r^2$. A set of complex dimension at most $d - 1$ is covered by about $r^{-2(d-1)}$ balls of radius $r$.

Let
$$r = \min\Big(1, \frac{\delta}{C_1 C_2 C_3 + 1}\Big),$$
so $0 < r \leq 1$. Take $T$ from the third input and let $U = \bigcup_{c \in T} B(c, r) \cup (\mathbb{C}^n \setminus K)$. It is open, since $K$ is closed. Each point of $Z(I)$ is in $K$, so in a ball, or is outside $K$. So $Z(I) \subseteq U$.

Let $\chi$ and $\varepsilon$ be as in the theorem, and let $w = \sum_{c \in T} \mathbf{1}_{B(c,r)}$. Then $w \geq 0$. Let $x \in K$. If $\chi(x) \neq 0$, then $x$ is in the support of $\chi$, so in $U$, and since $x \in K$ it is in some ball $B(c, r)$. So $|\chi(x)| \leq 1 \leq w(x)$. If $\chi(x) = 0$, then $|\chi(x)| = 0 \leq w(x)$. So the first input applies with $v = \chi$.

Each fibre of $A$ on $Z(J)$ is finite, so the chart density of $w$ is the sum over $c \in T$ of the chart densities of $\mathbf{1}_{B(c,r)}$. By the second input it is integrable, and its integral is at most $|T| \, C_2 \, r^{2d}$. Write $\psi = (\lambda_{u,\varepsilon}, \varphi)$ and $\psi' = (\lambda_{u,\varepsilon}, \eta, \dots, \eta)$. The absolute value of a sum is at most the sum of the absolute values, so
$$\Big| \int \rho_A(\chi f; \psi) \Big| \leq \int \rho^{\mathrm{abs}}_A(\chi f; \psi) \leq C_1 \int \rho_A(w; \psi') \leq C_1 C_2 \, |T| \, r^{2d} \leq C_1 C_2 C_3 \, r^2.$$
Since $r \leq 1$, this is at most $(C_1 C_2 C_3 + 1) r$, and by the choice of $r$ this is at most $\delta$. $\square$

The theorem is used for a small set $Z(I)$ inside the hyperplane section, that is, with $J + (\ell_u) \subseteq I$. A consequence of the theorem then gives a smooth cut off function $\chi$, equal to $1$ near $Z(I)$, such that both sides of the Poincaré and Lelong formula, the regularized integrals for small $\varepsilon$ and the sum over the components $W$ of $\operatorname{mult}_W(J + (\ell_u)) \int_{Z(W)} \chi f \, dd^c \varphi_1 \wedge \cdots \wedge dd^c \varphi_d$, are at most $\delta$ in absolute value.

**Remark 7.11.5 (Formalization).** The theorem is in [SheetIdentityAll.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SheetIdentityAll.lean#L397). It is `RegMassNearSmall.proof` applied to the proofs of the three inputs `RegFormCompare`, `RegBallMass` and `SmallSetBallCover`, which are themselves built from about fifteen further named statements. The statement is in [StRegMassNearSmall.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StRegMassNearSmall.lean#L13) and the proof in [PRegMassNearSmall.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PRegMassNearSmall.lean#L13). The integral over the variety is `varInt` in [StatementsCurrent.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StatementsCurrent.lean#L45). It uses `h.choose` for the finite projection, and it is $0$ if none exists, so the theorem has no content in that case; the proof uses $U = \mathbb{C}^n$ there. The chart density `chartDens` also picks its sheet with `h.choose`, and the density $M$ is `ReciprocityTheory.AnForm.maDens`. The balls are `Metric.ball` on `Fin n → ℂ`, with the sup norm. The chart integral is a Bochner integral, so it is $0$ for a density that is not integrable.
