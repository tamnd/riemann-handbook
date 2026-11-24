---
title: Mahler measures and vertical Chow terms
decls:
  - GlobalTheory.CompanionTheory.Ar.Short.mahlerSection
  - GlobalTheory.CompanionTheory.Ar.Short.defectConstDim
  - GlobalTheory.T.mahler_minus_cone_integral_indep
  - GlobalTheory.CompanionTheory.Ar.Short.Crofton.defect_eq_of_linForm_notMem
  - GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.full
  - GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_freeParAlgIndep
  - GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_chartPoint_secPoint_specChart
  - GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_remaining
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mahler measures and vertical Chow terms

This section proves the two local formulas that compute the height of a cycle when we cut it by a linear form. At the archimedean place, the Mahler measure of a Chow form after we replace one group of its variables by a fixed vector $u$ is the Mahler measure of the form plus a constant and an integral of the Fubini-Study logarithm of $u$ over the cycle. At a finite place $v$, the change of the Gauss norm is a sum over the components of the cut that lie over $v$. Both formulas are used in [the covolume bound](/entry/top-covol-slim2-use-alt-alt/) and in [the vertical Chow term of the heights chapter](/entry/heights-chow-form-section-vertical-full/). For the Mahler measure see [the section on Mahler measure](/learn/combinatorics/#mahler-measure-and-the-size-of-polynomials), and for heights see [the section on heights](/learn/arakelov/#heights).

### Chow forms and Mahler measures

Let $F$ be a field and let $n \geq 1$. A polynomial $f$ in $k$ groups $u_1, \dots, u_k$ of $n$ variables is multihomogeneous of degree $\delta$ if it is homogeneous of degree $\delta$ in each group. For a vector $u \in F^n$ we write $\ell_u = \sum_j u_j x_j$, and $f_u$ is the polynomial in $k - 1$ groups that we get when we put $u$ for the first group and move the other groups down by one.

**Definition 5.11.1 (Chow form).** Let $I$ be an ideal of $F[x_1, \dots, x_n]$. The incidence set of $I$ with $k$ groups is the set of $(u_1, \dots, u_k)$ over the algebraic closure of $F$ for which there is a point $x \neq 0$ in the zero set of $I$ with $u_i \cdot x = 0$ for all $i$. A polynomial $f$ in $k$ groups is a Chow form of $I$ if $f \neq 0$ and, for every $g$, the polynomial $g$ vanishes on the incidence set exactly when $f$ divides $g$. The Chow degree of $I$ is the least $\delta$ for which $I$ has a multihomogeneous Chow form of degree $\delta$. For a finite cycle $Z = \sum_W Z_W W$ of ideals, $f$ is a Chow form of $Z$ if $f = c \prod_W g_W^{Z_W}$ with $c \neq 0$ and each $g_W$ a Chow form of $W$.

An ideal is a projective prime if it is prime, homogeneous and does not contain all the variables $x_j$.

**Definition 5.11.2 (Mahler measure).** A hermitian norm on $\mathbb{C}^n$ is an invertible matrix $A$, with norm $\|u\| = |Au|$, dual norm $\|y\|^* = |(A^{T})^{-1} y|$ and point map $y \mapsto A^{T} y$. For $f$ in $k$ groups over $\mathbb{C}$, the Mahler measure $m_k(f)$ is the mean of $\log |f(u_1/\|u_1\|, \dots, u_k/\|u_k\|)|$ over the set of $(u_1, \dots, u_k)$ with $\|u_i\| < 1$ for all $i$, for the Lebesgue measure.

**Definition 5.11.3 (Cone integral).** For $u \in \mathbb{C}^n$, the Fubini-Study logarithm is $\lambda_u(y) = \log(|u \cdot y| / \|y\|^*)$. For an ideal $J$ and a function $g$, the cone integral $\int_{J, e} g$ is the integral of $g(A^{T}y)$ over the points $y$ with $|y| < 1$ whose image $A^{T}y$ is a zero of $J$, for the Hausdorff measure of dimension $2(e+1)$, divided by the volume of the unit ball of $\mathbb{C}^{e+1}$. For a cycle $Z$ we put $\int_{Z, e} g = \sum_W Z_W \int_{W, e} g$.

The defect of a Chow form $f$ of $Z$ with $e + 1$ groups at $u$ is
$$
D(u) = m_e(f_u) - \int_{Z, e} \lambda_u .
$$
We say that $u$ is admissible for $Z$ if $\ell_u \notin W$ for every $W$ in the support of $Z$.

**Theorem 5.11.4 (Crofton defect).** Let $W$ be a projective prime of $\mathbb{C}[x]$, and let $g$ be a Chow form of $W$ with $e + 1$ groups, multihomogeneous of degree $\delta$. If $\ell_u \notin W$ and $\ell_{u'} \notin W$, then
$$
m_e(g_u) - \int_{W, e} \lambda_u = m_e(g_{u'}) - \int_{W, e} \lambda_{u'} .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Short.Crofton.defect_eq_of_linForm_notMem` (also `GlobalTheory.T.mahler_minus_cone_integral_indep`, a second name).

*Proof.* Let $\gamma$ be the Gaussian measure on matrices with $e + 1$ rows in $\mathbb{C}^n$; its mass is positive and finite. For a matrix $\pi$, a finite set $P(\pi)$ of points of the cone of $W$ is attached to $\pi$ (we do not unfold it), and for almost every $\pi$ its number of points is the degree. For almost every $\pi$ the value of $g_u$ at the normalized rows of $\pi$ is not zero, and the fibre specialization of the Chow form gives a constant $c \neq 0$, which does not depend on $u$, with
$$
g_u(\pi) = c \prod_{y \in P(\pi)} u \cdot A^{T} y .
$$
Write $S_u(\pi)$ for the sum of $\lambda_u(A^{T} y)$ over $P(\pi)$. Since $\|A^{T}y\|^* = |y|$, the identity above gives
$$
\log |g_u(\pi)| - S_u(\pi) = \log |c| + \sum_{y \in P(\pi)} \log |y| ,
$$
and the right side does not depend on $u$. So the left side is the same for $u$ and $u'$ for almost every $\pi$. We integrate against $\gamma$. The Gaussian integral of the first term is the mass of $\gamma$ times $m_e(g_u)$, by the mean over normalized groups, and the Gaussian integral of $S_u$ is the mass times $\int_{W, e} \lambda_u$, by the Crofton formula for the cone. We cancel the mass. $\square$

**Theorem 5.11.5 (Constant defect).** Let $Z$ be a cycle of projective primes of $\mathbb{C}[x]$, and let $f$ be a Chow form of $Z$ with $e + 1$ groups, multihomogeneous of degree $\delta$. If $u$ and $u'$ are admissible for $Z$, then $D(u) = D(u')$.

Lean: `GlobalTheory.CompanionTheory.Ar.Short.defectConstDim`.

*Proof.* Write $f = c \prod_W g_W^{Z_W}$. Each $g_W$ is multihomogeneous of some degree $d_W$, and $f_u = c \prod_W (g_W)_u^{Z_W}$ with $(g_W)_u \neq 0$ when $u$ is admissible. The Mahler measure of a product is the sum of the Mahler measures, and the measure of the constant $c$ is $\log|c|$. So
$$
\begin{aligned}
D(u) = \log |c| + \sum_W Z_W \Big( & m_e((g_W)_u) \\
& - \int_{W, e} \lambda_u \Big) .
\end{aligned}
$$
By the Crofton defect, each bracket is the same at $u$ and at $u'$. $\square$

**Theorem 5.11.6 (Mahler section).** Let $Z$ be a cycle of projective primes of $\mathbb{C}[x_1, \dots, x_n]$, let $f$ be a Chow form of $Z$ with $e + 1$ groups, multihomogeneous of degree $\delta$, and let $u$ be admissible for $Z$. Then
$$
\begin{aligned}
m_e(f_u) = m_{e+1}(f) &+ \frac{\delta H_{n-1}}{2} \\
&+ \int_{Z, e} \lambda_u ,
\end{aligned}
$$
where $H_{n-1} = 1 + \frac{1}{2} + \dots + \frac{1}{n-1}$.

Lean: `GlobalTheory.CompanionTheory.Ar.Short.mahlerSection`.

*Proof.* The left side minus the integral is $D(u)$. The mean of $D$ over the normalized points of the unit ball is $m_{e+1}(f) + \delta H_{n-1}/2$, and almost every point of the ball is admissible. Since $D$ is constant on admissible vectors by the constant defect, $D(u)$ is equal to this mean. $\square$

### The vertical term at a finite place

Let $K$ be a number field with ring of integers $O_K$. For a finite place $v$, the Gauss norm $\|f\|_v$ of a polynomial over $K$ is the largest $v$-adic absolute value of its coefficients, and $N(v)$ is the norm of the prime of $v$. For an ideal $I$ of $K[x]$, the integral model $I_O$ is the set of polynomials over $O_K$ whose image in $K[x]$ lies in $I$. For $u \in O_K^n$, the vertical components $V(I, u, v)$ are the minimal primes $W$ of $I_O + (\ell_u)$ that do not contain all the variables and meet $O_K$ in the prime of $v$. The multiplicity $\mu(W)$ is the length of the localization at $W$ of the quotient by $I_O + (\ell_u)$, and $\bar W$ is the image of $W$ over the residue field of $v$. The vertical term is
$$
\begin{aligned}
T_v(I, u) = \sum_{W \in V(I, u, v)} & \mu(W) \, \deg_{e+1}(\bar W) \\
& \cdot \log N(v) ,
\end{aligned}
$$
where $\deg_{e+1}$ is the Chow degree with $e + 1$ groups. The sum is taken as zero if the set is infinite.

**Theorem 5.11.7 (Vertical Chow term).** Let $I$ be a projective prime of $K[x_1, \dots, x_n]$, let $f$ be a Chow form of $I$ with $e + 1$ groups, and let $u \in O_K^n$ with $\ell_u \notin I$. Then for every finite place $v$,
$$
\log \|f\|_v - \log \|f_u\|_v = T_v(I, u) .
$$

Lean: `GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.full`.

We prove it by three reductions.

**Theorem 5.11.8 (Vertical term from five inputs).** Assume the following five statements. Over a perfect field $k$, for a projective prime $Q$ with a Chow form $g$ with $e + 1$ groups, the generic section field of $Q$ is separable over the field of generic parameters. For a Dedekind domain $O$ with fraction field $F$, a prime $P$ of $O[x]$ with $P \cap O = 0$, a place $v$ and a maximal ideal $W$ that is minimal over $P + v$, the generic fibre of $P$ over $F$ has Krull dimension zero. For $Q$ and $g$ as above, the kernel of the map from $k[x]$ to the generic section quotient is $Q$. A statement on local charts holds (we do not unfold it). For a discrete valuation ring $R$, a finite $R$-algebra $B$ and a non-zero-divisor $b$ of $B$, the order of $b$ at each maximal ideal is finite. Then the vertical Chow term holds.

Lean: `GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_remaining`.

*Proof.* From the inputs we get the norm form of the Chow form on the generic section, its degree, the injectivity of the linear section, the dimensions of the fibre and special components, the maximality and residue fields of the special points, and their lengths. With these, the order of the specialized form in the discrete valuation ring of parameters is a vertical degree $\nu$. After we scale $f$ by a constant to a polynomial over $O_K$ with a coefficient that is a unit at $v$, this gives $\|f\|_v = 1$ and $\|f_u\|_v \, N(v)^{\nu} = 1$. The constant cancels in the difference of logarithms, and $T_v(I, u) = \nu \log N(v)$. $\square$

**Theorem 5.11.9 (Vertical term from chart points).** Assume that a point of a projective prime with a Chow form has chart transcendence degree at most $e$, that the section points are separable over the field of generic parameters, and the statement on local charts. Then the vertical Chow term holds.

Lean: `GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_chartPoint_secPoint_specChart`.

*Proof.* The first two assumptions give the separability of the generic section, and the statements on fibres, kernels and orders are proved; the theorem from five inputs then applies. $\square$

**Theorem 5.11.10 (Vertical term from free parameters).** Assume that, over a perfect field, the generic parameters of a section are algebraically independent over the field of the affine coordinates of a point. Then the vertical Chow term holds.

Lean: `GroundTheory.Heights₂.Heights.Vertical.ChowFormSectionVertical.of_freeParAlgIndep`.

*Proof.* The assumption gives the separability of section points, and the bound on chart transcendence degrees and the statement on local charts are proved, so the theorem from chart points applies. $\square$

*Proof of the vertical Chow term.* The statement on free parameters is proved, so the theorem from free parameters applies. $\square$

**Remark 5.11.11 (Formalization).** The cone dimension statement for Chow forms is built three times, in [OfFreeParAlgIndep.lean](lean:GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/OfFreeParAlgIndep.lean#L12), in [OfChartPointSecPointSpecChart.lean](lean:GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/OfChartPointSecPointSpecChart.lean#L18) and in [Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/Assembly.lean#L92). The statements of the Gauss, order and vertical term identities are declared in [IntToFracInjective.lean](lean:GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/IntToFracInjective.lean#L96), a file named for another lemma. The averaging step of the Mahler section is proved in [TargetsProjRegularDens.lean](lean:GroundTheory/HeightsAndTheta/Heights/LocalFiniteness/TargetsProjRegularDens.lean#L16), and we did not open its inputs on the mean of the defect and on admissible points. We did not open the Gaussian, fibre and Crofton lemmas.

## Notes and references

This chapter feeds the main proof in four places. The degree formula for good metrics replaces Mumford's theorem in [the good Chern-Weil theorem from the literature](/entry/good-chern-weil-of-literature/), which is used in the step [published results in arithmetic geometry](/step/published-results-arithmetic/) and in [Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem). The degree formula for line bundles and the seminegativity of Lie algebras of semi-abelian schemes are used in the step [every character from the literature](/step/every-character-of-literature/). The [Chern number relations](/entry/top-rel-relations/), with [the last link of their chain](/entry/stage5/), feed [the Hodge lattice flag bound](/entry/model-on-hodge-of-family-pos/). The later sections supply [the frames of CM points](/entry/exists-cm-point-loc-basis-frames/), [the values at points](/entry/value-at-point/) and the terms of [the covolume bound](/entry/top-covol-slim2-use-alt-alt/).

For Chern-Weil theory see Milnor and Stasheff and Griffiths and Harris. The splitting principle and the Chern classes of a flag bundle are in Fulton. The extension of Chern-Weil theory to good metrics with logarithmic growth is due to Mumford; the boundary behaviour of semi-abelian degenerations is in Faltings and Chai and in Moret-Bailly. For ampleness see Kleiman, for degrees Hartshorne, and for power sums Macdonald. Raynaud classified group schemes of type $(p, \dots, p)$ with a field action; Tate introduced $p$-divisible groups, and the Hodge-Tate description of divisible groups over $\mathbb{C}_p$ is due to Fargues and to Scholze and Weinstein. The Mahler measure of a polynomial in several variables is due to Mahler. Chow forms go back to Chow and van der Waerden. Heights of cycles through Mahler measures of Chow forms are due to Philippon and to Bost, Gillet and Soulé. The arithmetic intersection theory behind the heights is due to Gillet and Soulé.

- J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974, §14.
- P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978, Chapter 0, §5, and Chapter 3, §2.
- W. Fulton, *Intersection Theory*, Springer, 1984, Chapter 2 and Chapter 3, §3.2.
- D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergebnisse der Mathematik 22, Springer, 1990, Chapter III.
- L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129, 1985.
- S. L. Kleiman, "Toward a numerical theory of ampleness", Ann. of Math. 84 (1966), 293 to 344.
- R. Hartshorne, *Algebraic Geometry*, Springer, 1977, Chapter I, §7.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Oxford University Press, Chapter I.
- M. Raynaud, "Schémas en groupes de type $(p, \dots, p)$", Bull. Soc. Math. France 102 (1974), 241 to 280.
- J. Tate, "$p$-divisible groups", in *Proceedings of a Conference on Local Fields*, Springer, 1967, 158 to 183.
- L. Fargues, "L'isomorphisme entre les tours de Lubin-Tate et de Drinfeld et applications cohomologiques", in *L'isomorphisme entre les tours de Lubin-Tate et de Drinfeld*, Progr. Math. 262, Birkhäuser, 2008.
- P. Scholze and J. Weinstein, "Moduli of $p$-divisible groups", Camb. J. Math. 1 (2013), 145 to 237.
- K. Mahler, "On some inequalities for polynomials in several variables", J. London Math. Soc. 37 (1962), 341 to 344.
- W.-L. Chow and B. L. van der Waerden, "Zur algebraischen Geometrie IX", Math. Ann. 113 (1937), 692 to 704.
- P. Philippon, "Sur des hauteurs alternatives I", Math. Ann. 289 (1991), 255 to 283.
- J.-B. Bost, H. Gillet and C. Soulé, "Heights of projective varieties and positive Green forms", J. Amer. Math. Soc. 7 (1994), 903 to 1027.
- H. Gillet and C. Soulé, "Arithmetic intersection theory", Publ. Math. IHÉS 72 (1990), 93 to 174.
