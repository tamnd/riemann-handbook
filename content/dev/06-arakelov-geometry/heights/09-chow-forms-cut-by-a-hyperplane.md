---
title: Chow forms cut by a hyperplane
decls:
  - GroundTheory.Heights₂.Heights.AutoClose.MahlerSectionOfConst
  - GroundTheory.Heights₂.Heights.ChowFormSectionVertical.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chow forms cut by a hyperplane

The height of a projective variety over a number field can be defined by its Chow form: at a finite place one takes the logarithm of a Gauss norm, and at an infinite place a Mahler measure. The basic recursion of arithmetic Bézout theory compares the Chow form $f$ of a variety $V$ with the form $f(u, \cdot)$ obtained by putting a linear form $u$ in the first group of variables, which is a Chow form of the hyperplane section $V \cdot \{u = 0\}$. This section proves the two local parts of the recursion. At a finite place $v$, the drop of the logarithmic Gauss norm is the vertical part of $V \cdot \{u = 0\}$ over $v$, counted with multiplicities and degrees. At an infinite place, the Mahler measures differ by a constant and by the integral of the Green function $\log(|\langle u, y\rangle| / |y|)$ over the cycle; we prove that this formula holds once the difference is known to be constant in $u$. The finite part is used in [the covolume bound](/entry/top-covol-slim2-use-alt-alt/) of the chapter on boundary forms, and the infinite part in [the Mahler section formula](/entry/mahler-section/) of the chapter on Chern-Weil forms.

### Chow forms

Let $F$ be a field and $n \ge 1$. A projective prime of $F[X_1, \dots, X_n]$ is a homogeneous prime ideal $I$ that does not contain all the $X_j$; it defines an irreducible cone $C(I) \subseteq \bar F^n$. For $u \in F^n$ write $\ell_u = \sum_j u_j X_j$.

**Definition 4.9.1 (Chow form).** Let $k \ge 1$ and let $Y = (Y_{ij})$, $1 \le i \le k$, $1 \le j \le n$, be $k$ groups of $n$ variables. The incidence set of $I$ is the set of $u \in \bar F^{k \times n}$ for which some nonzero $x \in C(I)$ satisfies $\sum_j u_{ij} x_j = 0$ for all $i$. A Chow form of $I$ in $k$ groups is a nonzero polynomial $f \in F[Y]$ such that a polynomial $g$ vanishes on the incidence set if and only if $f$ divides $g$. A Chow form of a cycle $Z = \sum_W m_W W$ of projective primes is $f = c \prod_W f_W^{m_W}$, with $c \ne 0$ and $f_W$ a Chow form of $W$.

When $k = \dim C(I)$, the incidence set is a hypersurface, and its equation is homogeneous of the same degree $\delta$ in each group: $\delta$ is the degree of $V(I)$. For $u \in F^n$, the form $f(u, \cdot)$ is obtained by putting $u$ in the first group of variables; it has $k - 1$ groups.

**Definition 4.9.2 (Hyperplane section).** Let $I$ be a projective prime. The cycle $I \cdot \ell_u$ is $\sum_W m_W W$, the sum over the minimal primes $W$ of $I + (\ell_u)$ that are projective primes, with $m_W$ the length of the localization of $F[X]/(I + (\ell_u))$ at $W$.

When $\ell_u \notin I$ and $f$ is a Chow form of $I$ in $k$ groups, the form $f(u, \cdot)$ is a Chow form of the cycle $I \cdot \ell_u$ in $k - 1$ groups in characteristic zero. In arithmetic, the interesting part is what happens to the size of the coefficients.

### The finite places

Let $K$ be a number field with ring of integers $\mathcal{O}_K$, and $v$ a maximal ideal of $\mathcal{O}_K$, with norm $N(v)$. For a polynomial $f$ over $K$, the Gauss norm $|f|_v$ is the largest $v$-adic absolute value of a coefficient, with $|\varpi|_v = N(v)^{-1}$ for a uniformizer $\varpi$. The integral model of an ideal $I$ of $K[X]$ is $I \cap \mathcal{O}_K[X]$.

**Definition 4.9.3 (Vertical term).** Let $I$ be a projective prime of $K[X]$, $u \in \mathcal{O}_K^n$ and $k \ge 1$. The vertical components of $I \cdot \ell_u$ over $v$ are the projective minimal primes $W$ of $I_{\mathcal{O}} + (\ell_u)$, where $I_{\mathcal{O}}$ is the integral model, with $W \cap \mathcal{O}_K = v$. The vertical term is
$$\operatorname{vert}_v(I, k, u) = \sum_{W} m_W \cdot \delta_k(\overline{W}) \cdot \log N(v),$$
where $m_W$ is the length of the localization at $W$, $\overline{W}$ is the reduction of $W$ modulo $v$, and $\delta_k(\overline{W})$ is the least degree of a Chow form of $\overline{W}$ in $k$ groups.

**Theorem 4.9.4 (Vertical part of a hyperplane section).** Let $I$ be a projective prime of $K[X_1, \dots, X_n]$, let $f$ be a Chow form of $I$ in $e + 1$ groups, and let $u \in \mathcal{O}_K^n$ with $\ell_u \notin I$. Then for every maximal ideal $v$ of $\mathcal{O}_K$,
$$\log |f|_v - \log |f(u, \cdot)|_v = \operatorname{vert}_v(I, e + 1, u).$$

Lean: `GroundTheory.Heights₂.Heights.ChowFormSectionVertical.full` (also `GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.full`)

*Proof.* Both sides are unchanged when $f$ is multiplied by a nonzero constant: the left side because the Gauss norm is multiplicative on constants. So we may take $f = g$ with coefficients in $\mathcal{O}_K$ and at least one coefficient outside $v$; then $|g|_v = 1$, and it remains to show $-\log |g(u, \cdot)|_v = \operatorname{vert}_v$.

Introduce parameters $y_{ij}$ ($1 \le i \le e$) and $z_j$, algebraically independent, and let $D$ be the local ring of $\mathcal{O}_K[y, z]$ at the prime $v\,\mathcal{O}_K[y, z]$. It is a discrete valuation ring with uniformizer $\varpi$, and the order of a polynomial in $D$ is the $v$-adic order of its Gauss norm. Let $B$ be the quotient of $D[X]$ by the integral model of $I$, the generic linear forms $\sum_j y_{ij} X_j$ and $\sum_j z_j X_j - 1$. So $B$ is the coordinate ring of the cone cut by $e$ generic hyperplanes, on a generic affine chart. It is a finite torsion free $D$-module, and its rank is the degree of $I$.

The main identity says that, in $D$, $g(u, y)$ is a unit times the norm $N_{B/D}(\ell_u)$ of the image of $\ell_u$ in $B$. Since $g$ is a Chow form, $g(\cdot, y)$ vanishes exactly when the first linear form has a common zero with the other $e$ on the cone, and over the generic fibre the norm of $\ell_u$ is a polynomial with the same zeros and the same degree. The order of a norm is the length of the quotient: $\operatorname{ord}_D N_{B/D}(\ell_u) = \operatorname{length}_D B/\ell_u B$. Finally, $B/\ell_u B$ is the coordinate ring of $I \cdot \ell_u$ cut by the same generic hyperplanes, and its length over $D$ is the sum over the vertical components $W$ of $m_W$ times the number of points of $\overline{W}$ on a generic linear space of complementary dimension, that is $\delta_{e+1}(\overline{W})$. Hence $\operatorname{ord}_v g(u, \cdot) = \sum_W m_W\, \delta_{e+1}(\overline{W})$, and $-\log |g(u, \cdot)|_v$ is this number times $\log N(v)$. $\square$

### The infinite places

Let $A$ be an invertible complex $n \times n$ matrix, and put $|x|_A = |Ax|$ (the standard hermitian length) and $|y|^*_A = |(A^{\mathsf T})^{-1} y|$ for the dual length. Let $B_A = \{x : |x|_A < 1\}$.

**Definition 4.9.5 (Mahler measure, Green integral).** For a polynomial $f$ in $k$ groups of $n$ complex variables,
$$m_A(f) = \frac{1}{\operatorname{vol}(B_A^k)} \int_{B_A^k} \log \Bigl| f\Bigl(\frac{x_1}{|x_1|_A}, \dots, \frac{x_k}{|x_k|_A}\Bigr) \Bigr|\, dx_1 \cdots dx_k.$$
For a projective prime $W$ with a cone of dimension $e + 1$ and a function $\phi$ on $\mathbb{C}^n$, let $\int_W \phi$ be the integral of $\phi$ over the points $A^{\mathsf T} y$ of the cone with $|y| < 1$, against the $2(e+1)$-dimensional Hausdorff measure in $y$, divided by the volume of the unit ball of $\mathbb{C}^{e+1}$. For a cycle $Z$ put $\int_Z \phi = \sum_W m_W \int_W \phi$. The Green function of $u \in \mathbb{C}^n$ is $\lambda_u(y) = \log\bigl(|\sum_j u_j y_j| / |y|^*_A\bigr)$.

The normalization makes $\int_W 1$ the degree of $W$. For a cycle $Z$ with Chow form $f$ in $e + 1$ groups and $u$ admissible ($\ell_u$ in no component of $Z$), the Mahler defect is
$$\Delta(u) = m_A\bigl(f(u, \cdot)\bigr) - \int_Z \lambda_u,$$
where the first Mahler measure uses $e$ groups. Write $H_m = 1 + \frac12 + \cdots + \frac1m$.

**Theorem 4.9.6 (Mahler formula from a constant defect).** Let $e \ge 0$. Assume that for all $n$, $\delta$, $A$, every cycle $Z$ of projective primes with a Chow form $f$ in $e + 1$ groups, homogeneous of degree $\delta$ in each group, the defect $\Delta(u)$ takes the same value at all admissible $u$. Then for all such data and every admissible $u$,
$$m_A\bigl(f(u, \cdot)\bigr) = m_A(f) + \frac{\delta\, H_{n-1}}{2} + \int_Z \lambda_u.$$

Lean: `GroundTheory.Heights₂.Heights.AutoClose.MahlerSectionOfConst` (also `GroundTheory.Heights₂.Heights.MahlerSectionOfConst.proof`)

The proof uses three facts proved elsewhere. The average of the defect over $u \in B_A$, with $u$ replaced by $u/|u|_A$, is $m_A(f) + \delta H_{n-1}/2$; this follows from Fubini, since averaging $m_A(f(u, \cdot))$ over the sphere gives $m_A(f)$, and from the spherical mean $-H_{n-1}/2$ of $\log|\langle x, p\rangle|$ for a unit vector $p$, applied to each point of $Z$. For almost every $x \in B_A$ the point $x/|x|_A$ is admissible, because the nonadmissible points form a finite union of proper subvarieties. The ball $B_A$ has positive and finite volume.

*Proof.* Fix the data and an admissible $u$, and let $c = \Delta(u)$. For almost every $x \in B_A$ the point $x/|x|_A$ is admissible, so $\Delta(x/|x|_A) = c$ by the hypothesis. As $0 < \operatorname{vol}(B_A) < \infty$, the average of $\Delta(x/|x|_A)$ over $B_A$ is $c$. By the averaging fact this average is $m_A(f) + \delta H_{n-1}/2$. So $m_A(f(u, \cdot)) - \int_Z \lambda_u = m_A(f) + \delta H_{n-1}/2$. $\square$

**Remark 4.9.7.** The hypothesis of the theorem is the induction step of the full proof: the constancy of the defect in dimension $e + 1$ is proved from the Mahler formula in dimension $e$, by a symmetry of the defect in two admissible points $u$ and $u'$. Both local statements together give the arithmetic Bézout recursion for Chow heights, as in Bost, Gillet and Soulé.

**Remark 4.9.8 (Formalization).** The finite part is one result of a chain of about eighty lemmas on the section algebra $B$, its norm form and the discrete valuation ring $D$ ([Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/Assembly.lean#L85)); the theorem in the chapter only renames it ([Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/Assembly.lean#L207)). The infinite part is proved from three inputs passed as hypotheses ([PMahlerSectionOfConst.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/PMahlerSectionOfConst.lean#L9)), and the named theorem applies it to the proved inputs ([TargetsProjRegularDens.lean](lean:GroundTheory/HeightsAndTheta/Heights/LocalFiniteness/TargetsProjRegularDens.lean#L16)). The matrix $A$ is only required to be invertible. The Mahler measure is written as an average over balls of the values at the normalized points, which is the average over the product of spheres.
