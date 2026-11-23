---
title: Hörmander's estimate on étale Stein spaces
decls:
  - ReciprocityTheory.L2DbarEstimates.hormander
  - ReciprocityTheory.L2DbarEstimates.F.hStatement_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hörmander's estimate on étale Stein spaces

This section proves the weighted $L^2$ estimate of Hörmander for the equation $\bar\partial u = \bar\partial F_0$ on a space that lies over $\mathbb{C}^n$ by a local homeomorphism and has a plurisubharmonic exhaustion. The estimate is the analytic base of the chapter. A twisted form of it gives the twisted estimate of Section 4, and through that estimate the $L^2$ extension theorem of Section 5. In the proof of the Riemann hypothesis it sits below the step [EveryCharacter from the literature](/step/every-character-of-literature/).

We recall the classical setting. For a domain $\Omega \subseteq \mathbb{C}^n$ that is pseudoconvex, a [[plurisubharmonic|FF2P7ER3QT]] weight $\varphi$ and a $\bar\partial$-closed $(0,1)$-form $g$, Hörmander finds $u$ with $\bar\partial u = g$ and $\int |u|^2 e^{-\varphi} \le \int |g|^2_{i\partial\bar\partial\varphi} e^{-\varphi}$, where the norm on the right is taken with the inverse of the Levi form. See the background on [$L^2$ estimates](/learn/positivity-resolution/#l2-estimates) and on [$L^2$ spaces](/learn/analysis/#l2-spaces-and-the-cauchy-schwarz-inequality). Here the domain is replaced by a space $M$ that is only locally a domain in $\mathbb{C}^n$, and the form $g$ is $\bar\partial F_0$ for a smooth function $F_0$.

**Definition 10.1.1 (Étale Stein space).** Let $M$ be a second countable Hausdorff space and $n \ge 0$. An *étale Stein structure* of dimension $n$ on $M$ is a pair $(z, e)$ of a local homeomorphism $z : M \to \mathbb{C}^n$ and a function $e : M \to \mathbb{R}$, such that $e$ is smooth, the Levi form of $e$ is nonnegative at each point, and each sublevel set $\{e \le c\}$ is compact.

A *chart* of $M$ is an open set $U \subseteq M$ on which $z$ is a homeomorphism onto an open subset of $\mathbb{C}^n$. A function on $M$ is *smooth* or *holomorphic* if its composite with the inverse of $z$ on each chart is smooth or holomorphic. For a function $\varphi$ of class $C^2$ on $M$, a point $x$ and $\xi \in \mathbb{C}^n$, the *Levi form* is
$$\mathcal{L}_\varphi(x)(\xi) = \sum_{j,k=1}^n \frac{\partial^2 \varphi}{\partial z_j \partial \bar z_k}(x)\, \xi_j \bar\xi_k,$$
computed in a chart at $x$. It does not depend on the chart, because each chart at $x$ has the coordinates of $z$ near $x$. For a smooth function $F$ we write $\bar\partial F(x) \cdot \bar\xi = \sum_j \frac{\partial F}{\partial \bar z_j}(x)\, \bar\xi_j$.

**Definition 10.1.2 (Fibre measure).** For a Borel set $A \subseteq M$ let
$$\operatorname{vol}(A) = \int_{\mathbb{C}^n} \#\bigl(A \cap z^{-1}(y)\bigr)\, dy,$$
the integral of the number of points of $A$ over $y$ against the Lebesgue measure. For a measurable function $f$ and a weight $\varphi$ we write $\|f\|^2_\varphi = \int_M |f|^2 e^{-\varphi}\, d\operatorname{vol}$.

On a chart $U$ the measure $\operatorname{vol}$ is the Lebesgue measure carried by $z$, so $\|\cdot\|_\varphi$ is the usual weighted norm in each chart. Countable additivity of $\operatorname{vol}$ holds because $z$ is a local homeomorphism and $M$ is second countable: $M$ is a countable union of charts, and on each chart the fibre count is the indicator of the image.

**Theorem 10.1.3 (Hörmander's estimate).** Let $(M, z, e)$ be an étale Stein space of dimension $n$. Let $\varphi$ be a smooth real function on $M$ with nonnegative Levi form, let $F_0$ be a smooth complex function on $M$, and let $h : M \to [0, \infty]$ be measurable with
$$\bigl|\bar\partial F_0(x) \cdot \bar\xi\bigr|^2 \le h(x)\, \operatorname{Re} \mathcal{L}_\varphi(x)(\xi) \quad \text{for all } x \in M,\ \xi \in \mathbb{C}^n.$$
Then there is a holomorphic function $F$ on $M$ with
$$\int_M |F_0 - F|^2 e^{-\varphi}\, d\operatorname{vol} \le \int_M h\, e^{-\varphi}\, d\operatorname{vol}.$$

Lean: `ReciprocityTheory.L2DbarEstimates.hormander`.

So $u = F_0 - F$ solves $\bar\partial u = \bar\partial F_0$ with $\|u\|^2_\varphi \le \int h e^{-\varphi}$. The pointwise condition says that $h(x)$ bounds the square of the norm of $\bar\partial F_0(x)$ measured by the Levi form of $\varphi$. Where the Levi form is zero in a direction $\xi$, the derivative $\bar\partial F_0(x) \cdot \bar\xi$ must be zero.

The proof is the duality argument of Hörmander. It rests on eight analytic facts on $\mathbb{C}^n$ and on étale Stein spaces. We list them in words.

1. *The twisted a priori inequality.* For a test form $f = (f_1, \dots, f_n)$ with compact support, a weight $\varphi$ of class $C^2$, a twist $\psi$ of class $C^1$ and $\varepsilon > 0$, the integral of $\bigl(\operatorname{Re}\mathcal{L}_\varphi(f) - (1 + 1/\varepsilon)|\partial\psi|^2 |f|^2\bigr) e^{-\varphi}$ is at most $(1 + \varepsilon)\|T^* f\|^2_\varphi$ plus a term in $\bar\partial f$.
2. *Integration by parts.* For a smooth $F$ and a test form $f$, $\langle \bar\partial F, f\rangle_\varphi = \langle F, T^* f\rangle_\varphi$, where $T^* f = -\sum_j e^{\varphi} \partial_j (e^{-\varphi} f_j)$ is the formal adjoint of $\bar\partial$.
3. *The chain rule for the Levi form*, used to pass from the exhaustion $e$ to a cutoff and a twist.
4. *Weak holomorphy.* A function in $L^1_{\mathrm{loc}}$ on an open set of $\mathbb{C}^n$ that satisfies $\bar\partial F = 0$ in the sense of distributions is almost everywhere equal to a holomorphic function.
5. to 8. *Four facts on mollification* on $\mathbb{C}^n$: on the convergence of mollified forms in the graph norm, on their smoothness, on their support, and on the standard kernel.

**Proposition 10.1.4 (Reduction to the a priori inequality).** Suppose the eight facts above hold. Then the conclusion of Hörmander's estimate holds for each étale Stein space $(M, z, e)$ of dimension $n$ and for all $\varphi$, $F_0$ and $h$ as in the theorem.

Lean: `ReciprocityTheory.L2DbarEstimates.F.hStatement_of`.

*Proof.* Put $A = \int_M h\, e^{-\varphi}\, d\operatorname{vol}$. If $A = \infty$, take $F = 0$. There is nothing to prove.

Suppose $A < \infty$. We work in the Hilbert space ([[Hilbert space|HM2HHE3J51]]) $L^2_\varphi$ of measurable functions with $\|f\|_\varphi < \infty$, and in the space of test forms with values in $\mathbb{C}^n$.

The first step is the test inequality: for each test form $f$,
$$\bigl|\langle \bar\partial F_0, f\rangle_\varphi\bigr|^2 \le A\, \|T^* f\|^2_\varphi.$$
For a test form $f$ with $\bar\partial f = 0$, the pointwise condition and the Cauchy-Schwarz inequality give $|\langle \bar\partial F_0, f\rangle_\varphi|^2 \le A \int \operatorname{Re}\mathcal{L}_\varphi(f) e^{-\varphi}$, and the a priori inequality bounds the last integral by $\|T^* f\|^2_\varphi$. The work is to remove the conditions on $f$ and to pass to the limit. The exhaustion $e$ and the chain rule give a cutoff $\chi$ and a twist $\psi$ with $|\partial\psi|$ small where $\chi$ is not constant. The a priori inequality with this twist gives a primed inequality, with a factor $1 + \varepsilon$. Mollifiers in charts and a localisation by a partition of unity give the density of test forms in the graph norm, and the closure step lets $\varepsilon \to 0$. On the part of a form that is orthogonal to the kernel of $\bar\partial$, the pairing with $\bar\partial F_0$ is zero, because $\bar\partial F_0$ is $\bar\partial$-closed.

The second step is duality. On the range of $T^*$ define $\ell(T^* f) = \langle \bar\partial F_0, f\rangle_\varphi$. By the test inequality, $\ell$ is well defined and $|\ell(T^* f)| \le A^{1/2}\|T^* f\|_\varphi$. By the Hahn-Banach theorem $\ell$ extends to the closure of the range with the same bound, and by the Riesz representation theorem there is $u \in L^2_\varphi$ with
$$\|u\|^2_\varphi \le A, \qquad \langle u, T^* f\rangle_\varphi = \langle \bar\partial F_0, f\rangle_\varphi \text{ for all test forms } f.$$

The third step is regularity. By integration by parts, $\langle F_0 - u, T^* f\rangle_\varphi = \langle \bar\partial F_0, f\rangle_\varphi - \langle \bar\partial F_0, f\rangle_\varphi = 0$ for all test forms $f$. Take $f = e^{\varphi} g\, \epsilon_j$ for a test function $g$ supported in a chart and the $j$-th unit vector $\epsilon_j$. This gives $\int (F_0 - u)\, \overline{\partial_j g}\, d\operatorname{vol} = 0$ in the chart, so $\bar\partial(F_0 - u) = 0$ in the sense of distributions. The function $F_0 - u$ is square integrable on compact sets, because $F_0$ is smooth, $u \in L^2_\varphi$ and $\varphi$ is continuous. By weak holomorphy there is a holomorphic $G$ in each chart with $G = F_0 - u$ almost everywhere. Two such functions agree on the overlap of two charts, so they define one holomorphic function $F$ on $M$. Then
$$\int_M |F_0 - F|^2 e^{-\varphi}\, d\operatorname{vol} = \|u\|^2_\varphi \le A. \qquad \square$$

*Proof of Hörmander's estimate.* This is the Proposition applied to the eight facts above, each of which is proved on $\mathbb{C}^n$ and on étale Stein spaces. $\square$

No completeness of a Kähler metric is assumed. The exhaustion $e$ plays the role of the pseudoconvexity of the domain.

**Remark 10.1.5 (Formalization).** The eight facts are the propositions `APStatement`, `TStarIbpStatement`, `ChainStatement`, `C.RegStatement` and four mollifier statements. The proof of `hormander` passes the proofs `E.ap`, `E.tStarIbp`, `chain`, `C.reg`, `B.moll_graph`, `B.moll_smooth`, `B.moll_support` and `B.kernel_std` to `F.hStatement_of`. The duality argument is `F.hormander` in HormanderEstimate/Hormander.lean, line 13. We read the statements of the test inequality (`testIneq`, `primedIneq`, `closureIneq`) and of `rieszOnRange`, not their proofs. The measure `vol n z` is defined in IsLocalHomeomorph.lean, lines 82 to 92, as the fibre count if this count is countably additive and as the zero measure otherwise. The theorem `volAdditive` (MeasurableSetImageOfIsLocalHomeomorph.lean, line 152) proves the additivity for each local homeomorphism, so the zero case does not occur. The regularity statement assumes `LocalL2Isometry (vol n z) F` (UnweightBackStatement.lean, line 58). In spite of the name, this only says that $F$ is measurable and square integrable on compact sets. The direct users of `hormander` are `skoda`, `tw`, `hormander_open`, `horm_open` and `hormander_ball`. The twisted form `tw` is the one that reaches Section 4.
