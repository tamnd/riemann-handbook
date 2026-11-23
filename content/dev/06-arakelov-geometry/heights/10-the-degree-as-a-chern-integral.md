---
title: The degree of a divisor as a Chern integral
decls:
  - PositivityTheory.Tls2.Chern2.chernDegreeComplex
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The degree of a divisor as a Chern integral

This section proves that on a smooth projective complex variety $Y$ of dimension $d$, the integral of the top power of the first Chern form of any smooth metric on the line bundle of a Cartier divisor $\Delta$ is the self intersection number $(\Delta^d)$. Here the intersection number is defined algebraically, by Euler characteristics, and the Chern form is computed from local weights in charts. The argument reduces the general case to metrics of Fubini-Study type by a polynomial identity in the twist by a hyperplane. The result is the published statement of [the arithmetic degree entry](/entry/ar-degree-of-literature/) of Volume 15, where it gives the archimedean part of the degree of a hermitian line bundle.

### Varieties, divisors and metrics

A variety in this section is a closed subscheme $Y \subseteq \mathbb{P}^N_{\mathbb{C}}$ that is smooth of relative dimension $d$ and geometrically integral. Its Cartier divisors form a group. For a divisor $\Delta$, a presentation is a line bundle $L$, given by a cover $(U_i)$ and a cocycle $(g_{ij})$, with rational sections $r_i$ such that $r_i/r_j = g_{ij}$ on overlaps and $r_i$ is a local equation of $\Delta$ on $U_i$.

**Definition 4.10.1 (Weight, smooth weight).** A weight on a line bundle $L$ is a family of real functions $\varphi_i$ on the complex points of $U_i$ with
$$\varphi_j = \varphi_i - \log |g_{ij}|^2 \quad \text{on } U_i \cap U_j.$$
It is smooth if each $\varphi_i$ is locally a smooth function of finitely many regular functions.

A weight is the logarithm of a hermitian metric, written in the trivializations: $\varphi_i = -\log \|e_i\|^2$ for the frames $e_i$. The complex Hessian of $\varphi_i$ does not depend on $i$, because $\log |g_{ij}|^2$ is pluriharmonic.

**Definition 4.10.2 (Chern integral).** Let $\varphi$ be a smooth weight on $L$. In a holomorphic chart $z = (z_1, \dots, z_d)$ the Chern density is
$$c(\varphi)(z) = \frac{d!}{\pi^d} \det\Bigl(\frac{\partial^2 \varphi_i}{\partial z_a \partial \bar z_b}\Bigr),$$
the density of the top power of the first Chern form $\frac{i}{2\pi} \partial \bar\partial \varphi$ against Lebesgue measure. These densities glue to a signed measure $\mu_\varphi$ on $Y(\mathbb{C})$. A function $f$ is Chern integrable if it is integrable against the positive and the negative part of $\mu_\varphi$, and then $\int f\, c_1(L, \varphi)^d$ is the difference of the two integrals.

**Definition 4.10.3 (Intersection number).** For line bundles $L_1, \dots, L_d$ on $Y$, the intersection number is
$$(L_1 \cdots L_d) = \sum_{S \subseteq \{1, \dots, d\}} (-1)^{|S|}\, \chi\Bigl(\bigotimes_{i \in S} L_i^{-1}\Bigr),$$
and $(\Delta^d)$ is this number for $L_i = \mathcal{O}(\Delta)$ for all $i$.

This is Snapper's definition. It is multilinear and symmetric in the $L_i$, and for a fixed divisor $\Delta_0$ the function $m \mapsto ((\Delta + m\Delta_0)^d)$ is a polynomial in $m$ of degree at most $d$.

### The theorem

**Theorem 4.10.4 (Degree as a Chern integral).** Let $Y$ be a smooth geometrically integral projective variety over $\mathbb{C}$ of dimension $d$, let $\Delta$ be a Cartier divisor on $Y$ presented by a line bundle $L$ with rational sections $r$, and let $\varphi$ be a smooth weight on $L$. Then the constant function $1$ is Chern integrable for $\varphi$, and
$$\int_{Y(\mathbb{C})} c_1(L, \varphi)^d = (\Delta^d).$$

Lean: `PositivityTheory.Tls2.Chern2.chernDegreeComplex`

The proof combines five facts, proved elsewhere in the development. Let $H$ be the divisor of a hyperplane $\{X_i = 0\}$ that does not contain the generic point of $Y$.

**Lemma 4.10.5 (Serre twist).** For every divisor $\Delta$ and all large $m$, the divisor $\Delta + mH$ is presented by a line bundle with finitely many global sections $b_1, \dots, b_n$ without a common zero.

Lean: `GlobalTheory.T.hyperplane_twist_globally_generated`

**Lemma 4.10.6 (Fubini-Study metrics).** If $\Delta$ is presented by $L$ and $b_1, \dots, b_n$ are global sections of $L$ without a common zero, the Fubini-Study weight $\varphi_i = \log \sum_j |b_{j,i}|^2$, where $b_{j,i}$ is the function that represents $b_j$ on $U_i$, is smooth and $\int c_1(L, \varphi)^d = (\Delta^d)$.

Lean: `GlobalTheory.T.chern_integral_eq_intersection`

**Lemma 4.10.7 (Independence of the presentation and the metric).** If $\Delta$ is presented by $L$ and by $L'$, then $\int c_1(L, \varphi)^d = \int c_1(L', \psi)^d$ for all smooth weights $\varphi$ on $L$ and $\psi$ on $L'$.

Lean: `GlobalTheory.T.chern_integral_presentation_indep`

**Lemma 4.10.8 (Polynomial growth).** Let $\Delta$ and $\Delta_0$ be presented by $L$ and $L_0$, with smooth weights $\varphi$ and $\varphi_0$. There is a real polynomial $P$ of degree at most $d$ such that for every $m \ge 0$, the divisor $\Delta + m\Delta_0$ has a presentation with a smooth weight $\psi_m$ and $\int c_1(\psi_m)^d = P(m)$.

Lean: `GlobalTheory.T.chern_integral_polynomial_growth`

**Lemma 4.10.9 (Polynomial intersection numbers).** For divisors $\Delta$ and $\Delta_0$ there is a real polynomial $Q$ with $((\Delta + m\Delta_0)^d) = Q(m)$ for all $m \ge 0$.

Lean: `GlobalTheory.T.intersection_number_polynomial`

The independence lemma is Stokes' theorem: two weights on the same line bundle differ by a global smooth function $u$, and $c_1(\varphi + u)^d - c_1(\varphi)^d$ is $dd^c u$ times a closed form. The polynomial growth comes from the multilinear expansion of $c_1(\varphi + m\varphi_0)^d$, where $\psi_m$ is the weight $\varphi + m\varphi_0$ on the tensor product $L \otimes L_0^{m}$.

*Proof.* Integrability is proved directly from the smoothness of the weight on the compact space $Y(\mathbb{C})$. For the value, apply the Serre twist lemma with $\Delta = 0$: there is $M_0$ such that $\Delta_0 = (M_0 + 1)H$ is presented by a line bundle $L_0$ with sections $b$ without a common zero. Let $\varphi_0$ be the Fubini-Study weight of $b$; it is smooth.

Let $P$ be the polynomial of the growth lemma for $\Delta, \Delta_0, \varphi, \varphi_0$, and $Q$ the polynomial of the last lemma for $\Delta, \Delta_0$. By the Serre twist lemma for $\Delta$, there is $M$ such that for all $m' \ge M$ the divisor $\Delta + m'H$ is presented by a line bundle $L_1$ with sections $b'$ without a common zero. Let $m \ge M$. Then $m' = m(M_0 + 1) \ge M$, and $\Delta + m'H = \Delta + m\Delta_0$. So
$$\begin{aligned}
P(m) &= \int c_1(\psi_m)^d = \int c_1(L_1, \varphi_{b'})^d \\
&= \bigl((\Delta + m\Delta_0)^d\bigr) = Q(m),
\end{aligned}$$
by the independence lemma (both are presentations of $\Delta + m\Delta_0$) and the Fubini-Study lemma for $b'$. Two real polynomials that agree at infinitely many points are equal, so $P = Q$. Now take $m = 0$. The weight $\psi_0$ is a smooth weight on a presentation of $\Delta$, so by the independence lemma
$$\int c_1(L, \varphi)^d = \int c_1(\psi_0)^d = P(0) = Q(0) = (\Delta^d). \qquad \square$$

**Example 4.10.10.** For $Y = \mathbb{P}^1$, $\Delta$ a point and $\varphi$ the Fubini-Study weight $\log(1 + |z|^2)$ in the chart $z$, the Chern density is $\frac{1}{\pi}(1 + |z|^2)^{-2}$, whose integral over $\mathbb{C}$ is $1 = \deg \Delta$. For any other smooth weight $\varphi + u$ the integral of $\frac{1}{\pi}\partial_z \partial_{\bar z} u$ over the sphere is $0$, so the value $1$ does not change.

**Remark 4.10.11.** The theorem allows weights that are not positive: the Chern form may change sign, which is why the integral is the difference of two positive measures. No Kähler hypothesis is needed. The result is the case of one divisor of the comparison between Chern forms and intersection numbers in Griffiths and Harris, *Principles of Algebraic Geometry*, proved here from the algebraic side.

**Remark 4.10.12 (Formalization).** The theorem joins the five lemmas ([ChernDegreeComplex.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ChernDegreeComplex/ChernDegreeComplex.lean#L19)); the statement is the published statement ([ChernDegreeComplex.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ChernDegreeComplex.lean#L12)). Each lemma is a wrapper around a result of the companion theory, proved by the tactic `first | exact ... | ...`. The intersection number is Snapper's alternating sum of Euler characteristics. A second proof of the same statement exists as `GlobalTheory.ChernDegree.chernDegreeComplex`.
