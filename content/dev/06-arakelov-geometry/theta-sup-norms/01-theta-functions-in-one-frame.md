---
title: Theta functions in one archimedean frame
decls:
  - GlobalTheory.CompanionTheory.Ar.NForm.nform
  - GlobalTheory.T.theta_function_even_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta functions in one archimedean frame

This section bounds a theta function of level one on a principally polarized complex torus. The bound has two parts. The first part bounds the normalized value of the function at every point by its $L^2$ norm times $\exp(E)$, where $E$ is of size $g \log(1 + 1/\rho)$ plus $O(g \log 2g)$. The second part says that the function is small on average at the torsion points of large order: the sum of $-\log$ of its normalized values there grows with the number of these points. Both parts depend on one number $\rho$, which comes from a reduced period matrix. The next section applies the theorem at every complex place of a number field and combines the two parts with the product formula. For the classical theory we use [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori) and [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics).

### Frames and theta functions

Let $G$ be a commutative group scheme over a base $S$, let $P$ be a rigidified line bundle on $G$, and let $z$ be a complex point of $S$. An archimedean frame of genus $g$ at $z$ is a uniformization of the fibre of $G$ at $z$ by $\mathbb{C}^g$ modulo a lattice $\Lambda$, together with a positive definite hermitian matrix $H_m$ and a function $\chi$ on $\Lambda$, such that the pullback of $P$ has the multiplier described below. We write
$$
H(w, w') = w^{\mathsf T} H_m \overline{w'}
$$
for $w, w' \in \mathbb{C}^g$.

**Definition 10.1.1.** Let $a$ be an archimedean frame of genus $g$ with lattice $\Lambda$, form $H$ and multiplier $\chi$. A theta function of level one for $a$ is a holomorphic function $\vartheta$ on $\mathbb{C}^g$ such that for all $l \in \Lambda$ and $w \in \mathbb{C}^g$
$$
\vartheta(w + l) = \chi(l)\, \exp(\pi H(w, l) + \frac{\pi}{2} H(l, l))\, \vartheta(w).
$$
Its normalized value is $\lVert\vartheta\rVert(w) = \lvert\vartheta(w)\rvert\, \exp(-\frac{\pi}{2} \operatorname{Re} H(w, w))$. A number $b$ is the $L^2$ norm of $\vartheta$ if $b > 0$ and $b^2$ is the mean of $\lVert\vartheta\rVert^2$ over every fundamental domain of $\Lambda$.

When $\lvert\chi\rvert = 1$, the normalized value is a function on the torus $\mathbb{C}^g/\Lambda$. Indeed $\operatorname{Re} H(w + l, w + l) = \operatorname{Re} H(w, w) + 2 \operatorname{Re} H(w, l) + H(l, l)$, and this cancels the growth of $\lvert\vartheta\rvert$. So the mean over a fundamental domain does not depend on the domain.

### The theorem

The theorem needs four conditions on the frame. They say that $\operatorname{Im} H$ is an integral unimodular symplectic form on $\Lambda$ and that $\chi$ is a quadratic semicharacter for it:

1. $\operatorname{Im} H(l, l') \in \mathbb{Z}$ for all $l, l' \in \Lambda$;
2. if $w \in \mathbb{C}^g$ and $\operatorname{Im} H(w, l) \in \mathbb{Z}$ for all $l \in \Lambda$, then $w \in \Lambda$;
3. $\chi(l + l') = \chi(l) \chi(l')\, \exp(\pi i \operatorname{Im} H(l, l'))$ for all $l, l' \in \Lambda$;
4. $\chi(l)^2 = 1$ for all $l \in \Lambda$.

For $\rho > 0$ and a constant $C_0$ put
$$
E(\rho) = g \log\Bigl(1 + \frac{1}{\rho}\Bigr) + C_0\, g \log(2g).
$$

**Theorem 10.1.2 (Theta bound in one frame).** There is $C_0 \geq 0$ with this property. Let $a$ be an archimedean frame of genus $g \geq 1$ that satisfies conditions 1 to 4. Let $\vartheta$ be a theta function of level one for $a$ with $L^2$ norm $b$. Then there is $\rho$ with $0 < \rho \leq \sqrt{2g}$ such that:

1. $\lVert\vartheta\rVert(w) \leq b\, \exp(E(\rho))$ for every $w \in \mathbb{C}^g$;
2. for all large $m$ the following holds. Let $r_1, \dots, r_n$ be points with $m r_i \in \Lambda$ and $\vartheta(r_i) \neq 0$, one in each class modulo $\Lambda$ of such points. Then $n \geq 1$ and
$$
n \Bigl(\frac{\pi}{96 \rho^2} - E(\rho)\Bigr) \leq \sum_{i=1}^{n} -\log \frac{\lVert\vartheta\rVert(r_i)}{b} .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.NForm.nform` (also `GlobalTheory.T.theta_function_even_bound`, a second name).

*Proof.* The proof has four steps.

Step 1: a reduced period matrix. By conditions 1 and 2, $\operatorname{Im} H$ is a unimodular integral symplectic form on $\Lambda$. So $\Lambda$ has a symplectic basis. In the coordinates of this basis, $\Lambda = \mathbb{Z}^g + \Omega \mathbb{Z}^g$ with $\Omega = X + iY$ in the Siegel upper half space, and $H$ is given by $Y^{-1}$. We change the basis by a symplectic matrix so that $Y$ is reduced in the following sense. There is $\rho > 0$ with $\rho^2 \leq 2g$ such that the first diagonal entry of $Y^{-1}$ is $\rho^2$, such that $\rho^2 \leq l^{\mathsf T} Y^{-1} l$ for every nonzero integral vector $l$, and such that
$$
\det Y^{-1} \leq \rho^2 (2g)^{g - 1} .
$$
So $\rho^2$ is the first minimum of the quadratic form $Y^{-1}$ on $\mathbb{Z}^g$, it is put in the first coordinate, and the other successive minima are at most $2g$. The real part of the Gram matrix changes by an element of the symplectic group, so the new basis is again symplectic.

Step 2: the canonical form. By conditions 3 and 4, the semicharacter $\chi$ is given by a theta characteristic $(a_0, c_0)$ with entries in $\{0, \frac12\}$. The space of theta functions of level one for $a$ has dimension one. It is spanned by the classical theta function with characteristic $(a_0, c_0)$ and period matrix $\Omega$, times an exponential factor in $w$. So $\vartheta = \kappa\, \vartheta_{\mathrm{can}}$ for a constant $\kappa$. The orthogonality of the exponentials $\exp(2\pi i n^{\mathsf T} x)$ on the real torus gives
$$
b^2 = \lvert\kappa\rvert^2\, (2^g \det Y)^{-1/2} .
$$

Step 3: the pointwise bound. Write $\lVert\vartheta\rVert$ in the period coordinates of Step 1 and expand $\vartheta_{\mathrm{can}}$ as a Gaussian sum over $\mathbb{Z}^g + a_0$. Let $d(w)$ be the distance from the first real period coordinate of $w$, shifted by the first entry of $a_0$, to $\mathbb{Z}$. The terms of the sum are bounded with the reduction of Step 1. The first coordinate carries the weight $\rho^2$, and the other coordinates contribute at most the factor $\exp(E(\rho))$. This gives
$$
\lVert\vartheta\rVert(w) \leq b\, \exp\Bigl(-\frac{\pi}{2 \rho^2}\, d(w)^2 + E(\rho)\Bigr)
$$
for every $w$, with a constant $C_0$ that does not depend on the frame. Since $d(w)^2 \geq 0$, part 1 follows.

Step 4: the zero count. Let $m$ be large and let $r_1, \dots, r_n$ be as in part 2. Since $b > 0$, the function $\vartheta$ is not identically zero. Its zero set is a closed analytic subset with empty interior, so its complement contains a ball. For large $m$ the $m$-torsion points meet every ball of radius of order $1/m$, so $n \geq 1$. A bound for the order of vanishing of $\vartheta$ along its zero divisor gives
$$
n \leq 3 \cdot \#\{\, i : d(r_i) \geq \tfrac14 \,\} .
$$
So at least $n/3$ of the points have $d(r_i)^2 \geq \frac{1}{16}$, and $\sum_i d(r_i)^2 \geq \frac{n}{48}$. Take $-\log$ of the bound of Step 3 and sum over $i$:
$$
\begin{aligned}
\sum_{i} -\log \frac{\lVert\vartheta\rVert(r_i)}{b}
&\geq \frac{\pi}{2\rho^2} \sum_i d(r_i)^2 - n E(\rho) \\
&\geq n \Bigl(\frac{\pi}{96 \rho^2} - E(\rho)\Bigr) .
\end{aligned}
$$
This is part 2. $\square$

The constant $\pi/96$ comes from $\frac{\pi}{2} \cdot \frac{1}{48}$. The bound of part 2 is useful only when $\rho$ is small, that is when the torus is close to a degenerate one. Then the first coordinate is long, the theta function decays fast away from the zero locus of the first coordinate, and many torsion points lie far from it.

**Remark 10.1.3 (Formalization).** The theorem is stated for a frame of a rigidified line bundle on a commutative group scheme at a complex point. The second name is a relay that only restates the theorem; the word "even" in it matches no hypothesis and no conclusion, and the statement holds for every semicharacter with $\chi^2 = 1$ (`Development/AutomorphicSpectrum/Proofs/MetricProofs/ThetaFunctionEvenBoundStatement.lean`). The proof takes the analytic bound from `ThetaBound.full` (`AssemblyAnalytic.lean:51`) and the reduced basis from `exists_reduced` (`ThetaFunctionEvenBound.lean:98`); the reduction conditions of Step 1 are the predicate `IsReducedImaginaryPart` (`KernelsMatrix.lean:63`). The step to the reduced basis calls a lemma named `SiegelCoordinates.intersectionNumber_baseChange` (`ThetaFunctionEvenBound.lean:114`); the name says nothing about its content. I did not unfold the lemmas behind Steps 3 and 4, namely the pointwise bound in period coordinates and the jet bound for the zero divisor; the description of these two steps follows their statements. The torsion condition in part 2 is stated with an index type and a bijection to the classes modulo $\Lambda$, and the conclusion is stated with the filter of large $m$.
