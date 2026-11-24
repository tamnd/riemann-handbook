---
title: The archimedean Kirillov theorem
decls:
  - GlobalTheory.JSW.MirCinf.exists_levRepInf
  - GlobalTheory.JSW.MirCinf.kirillov_cinf
  - GlobalTheory.T.kirillov_archimedean_totallyComplex_mirabolic
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The archimedean Kirillov theorem

For a generic representation of $\mathrm{GL}_n$ over a non-archimedean field, the restriction of the Whittaker model to the mirabolic subgroup contains every smooth function that is compactly supported modulo $N$ (the Kirillov model, in the theorem of Gelfand and Kazhdan; see [generic representations](/learn/representations/#generic-representations-and-local-factors)). Over $\mathbb{C}$ the space of the representation is not closed under such cut-offs, but its closure under integral operators of rapid decay is. This section proves this archimedean form for the product of the complex places of a totally complex field. The next section passes from the archimedean places to a finite set of places and then to cusp forms.

### Notation

Let $E$ be a totally complex number field. Put $E_\infty = \prod_{w \mid \infty} \mathbb{C}$, $n = m + 1$ and $G_\infty = \mathrm{GL}_n(E_\infty)$. Let $N_\infty \subset G_\infty$ be the upper unitriangular group and let
$$\psi_\infty(u) = e\Big(-\sum_{w} 2 \operatorname{Re} \sum_{i} u_{i, i+1, w}\Big), \qquad e(x) = e^{2\pi i x}.$$
The *height* of $y \in G_\infty$ is $\|y\| = 1 + |y| + |y^{-1}|$, with a fixed norm $|\cdot|$ on matrices. The *mirabolic set* $P_\infty$ is the set of $y \in G_\infty$ whose last row is $(0, \ldots, 0, 1)$.

**Definition 4.7.1 (Rapid kernel).** A *rapid kernel* is a measure space $(X, \nu)$ with $\nu$ s-finite, together with measurable maps $k \colon X \to \mathbb{C}$ and $\gamma \colon X \to G_\infty$ such that $\int_X |k(x)|\, \|\gamma(x)\|^N\, d\nu(x) < \infty$ for every $N$. Its *operator* sends a function $f$ on $G_\infty$ to
$$(T f)(y) = \int_X k(x)\, f(y\gamma(x))\, d\nu(x).$$

The operator commutes with left translation. If $f$ has moderate growth, $|f(y)| \leq C\|y\|^N$, then $Tf$ is defined and has moderate growth, since $\|y\gamma\| \leq \|y\|\,\|\gamma\|$. Rapid kernels are the archimedean replacement for the finite sums of right translates that one uses over a $p$-adic field. A compactly supported smooth function on $G_\infty$, viewed as a density, is a rapid kernel; so is a Schwartz function on the Lie algebra pushed forward by a map of polynomial growth.

**Theorem 4.7.2 (Archimedean Kirillov theorem).** Let $\beta, f \colon G_\infty \to \mathbb{C}$ satisfy $\beta(uy) = \psi_\infty(u)\beta(y)$ and $f(uy) = \psi_\infty(u) f(y)$ for $u \in N_\infty$. Assume:

1. $\beta$ is the restriction of a function $B$ on $n \times n$ matrices over $E_\infty$ that is smooth on the open set of invertible matrices;
2. there is a compact $C \subset G_\infty$ such that each $y \in P_\infty$ with $\beta(y) \neq 0$ lies in $N_\infty C$;
3. $f$ is continuous, $|f(y)| \leq C'\|y\|^N$ for some $C'$ and $N$, and $f(1) \neq 0$.

Then there is a rapid kernel $(X, \nu, k, \gamma)$ with
$$\int_X k(x)\, f(y \gamma(x))\, d\nu(x) = \beta(y) \qquad (y \in P_\infty).$$

Lean: `GlobalTheory.JSW.MirCinf.kirillov_cinf` (also `GlobalTheory.T.kirillov_archimedean_totallyComplex_mirabolic`, a second name).

So one vector $f$ of a Whittaker space with $f(1) \neq 0$ produces, by one rapid kernel, any prescribed smooth Whittaker function on the mirabolic set. The proof is an induction over a chain of sets that grows from $N_\infty$ to $P_\infty$.

### Levels

**Definition 4.7.3 (Level set).** For $0 \leq r \leq m$ let $L_r$ be the set of $g \in G_\infty$ such that at each place, for each row $i \geq r$, the entries $g_{ij}$ with $j < i$ are $0$ and $g_{ii} = 1$.

So $L_0 = N_\infty$, $L_m = P_\infty$ and $L_0 \subset L_1 \subset \cdots \subset L_m$. Each $L_r$ is stable under left multiplication by $N_\infty$.

Let $Y$ be a finite-dimensional real vector space; it carries parameters. A *kernel operator with frequencies* on $Y$ sends $W$ to the function
$$(TW)(z, g) = \int_X k(x)\, e(\eta_x(z))\, W(g\gamma(x))\, d\nu(x) \qquad (z \in Y,\ g \in G_\infty),$$
where $(X, \nu, k, \gamma)$ is rapid and $\eta_x$ is a real linear form on $Y$ that depends measurably on $x$.

**Definition 4.7.4 (Level representation).** Let $\lambda$ be a function on the space of functions on $G_\infty$, with values in $\mathbb{C}$. We say that $\lambda$ *represents level* $r$ if the following holds for each $Y$ as above. Let $B$ be a function on $Y \times M_n(E_\infty)$ that is smooth on $Y \times \mathrm{GL}_n(E_\infty)$, satisfies $B(z, ug) = \psi_\infty(u)B(z, g)$ for $u \in N_\infty$, and vanishes at $(z, g)$ with $g \in L_r$ unless $z \in D$ and $g \in N_\infty C$, for compact $D \subset Y$ and $C \subset G_\infty$. Then there is a kernel operator with frequencies $T$ such that
$$(TW)(z, g) = B(z, g)\, \lambda(W) \qquad (z \in Y,\ g \in L_r)$$
for every continuous $W$ of moderate growth with $W(ug) = \psi_\infty(u)W(g)$.

The parameter space $Y$ is what makes the induction work: the step from level $r$ to level $r + 1$ treats the new row as a parameter.

**Proposition 4.7.5 (Level representations exist).** Let $r < n$, and let $W_0$ be continuous of moderate growth with $W_0(1) \neq 0$. Then there is $\lambda$ that represents level $r$ with $\lambda(W_0) \neq 0$.

Lean: `GlobalTheory.JSW.MirCinf.exists_levRepInf`.

*Proof.* Induction on $r$.

*Level $0$.* Take $\lambda(W) = W(1)$. For $g = u \in N_\infty$, $B(z, u) = \psi_\infty(u)B(z, 1)$ and $W(u) = \psi_\infty(u)W(1)$. The function $\Phi(z) = B(z, 1)$ is smooth with compact support on $Y$, so it is a superposition of characters with a rapidly decreasing density: $\Phi(z) = \int k(x)\, e(\eta_x(z))\, d\nu(x)$ (Fourier inversion, [the Fourier transform](/learn/analysis/#the-fourier-transform)). With $\gamma = 1$ this kernel gives $(TW)(z, u) = \Phi(z) W(u) = B(z, u)\, W(1)$.

*From $r$ to $r + 1$.* Let $\rho = r$ be the new row. First choose a smooth compactly supported function $\alpha$ on matrices near $1$ such that the smoothing $S_\alpha W(g) = \int \alpha(a)\, W(ga)\, da$ keeps the value at $1$ of the given vector nonzero. The smoothing preserves moderate growth. Apply the induction hypothesis to the smoothed vector and put $\lambda'(W) = \lambda(S_\alpha W)$. Then $\lambda'(W_0) \neq 0$.

Now let $B$ be given at level $r + 1$. For $g \in L_{r+1}$, the truncated row $v(g) = (g_{\rho 0}, \ldots, g_{\rho\rho})$ at each place is invariant under left multiplication by $N_\infty$, because the rows below $\rho$ have zeros left of the diagonal, and it is nonzero, because $g$ is invertible. Choose a smooth partition of unity on the set of such rows, indexed by the choice at each place of an index $j(w) \leq \rho$ with $v_{j(w)} \neq 0$. On each piece there is a section matrix $s(v)$, affine in $v$, invertible, in $L_{r+1}$, with $g\, s(v(g))^{-1} \in L_r$. Write $B(z, g) = B(z, g s(v)^{-1} s(v))$ and treat $v$ as a new parameter, so the parameter space becomes $Y \times (\text{rows})$. The level $r$ property for the new parameter space gives a kernel operator. Right translation by the affine family $s(v)$ and the passage from $v$ back to the entries of $g$ are again kernel operators with frequencies, since $s$ is affine in $v$. The smoothing by $\alpha$ makes the translated family smooth in $v$. A finite sum of kernel operators is a kernel operator, so summing over the pieces of the partition gives $T$ with $(TW)(z, g) = B(z, g)\lambda'(W)$ for $g \in L_{r+1}$. $\square$

*Proof of the theorem.* Apply the proposition with $r = m$ and $W_0 = f$. Moderate growth in the sense of the proposition uses the product over the places of the heights of the components; the height $\|y\|$ is at most $3$ times this product, so $f$ has moderate growth in this sense too. We get $\lambda$ with $\lambda(f) \neq 0$ that represents level $m$. Take $Y$ to be a point and $B$ the smooth extension of $\beta$; conditions 1 and 2 are the hypotheses of the level representation, since $L_m = P_\infty$. The kernel operator $T$ satisfies $(Tf)(y) = \beta(y)\lambda(f)$ for $y \in P_\infty$. Divide $k$ by $\lambda(f)$. $\square$

**Remark 4.7.6 (Formalization).** In the definition of a level representation, $\lambda$ is any function on functions; it need not be linear ([OnMatInfOfIsUnit.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OnMatInfOfIsUnit.lean#L96)). The proof only evaluates $\lambda$ at $f$. The smoothness hypothesis in the theorem is written with the order $\infty$ of `ContDiffOn`; in other statements of this chain it is written with the order $\top$ of extended natural numbers coerced to `WithTop ℕ∞`. The two forms are the same. The lemmas on the section matrices and on the column translates are only summarized above.
