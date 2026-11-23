---
title: A Crofton formula and the Chern integral of a Fubini and Study metric
decls:
  - GlobalTheory.CompanionTheory.FSCrofton.crofton
  - GlobalTheory.CompanionTheory.ChernDegree.chernInt_fsBasis_eq_inter
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Crofton formula and the Chern integral of a Fubini and Study metric

Let $Y$ be a complex projective variety of dimension $D$ and $L$ a line bundle on $Y$ with global sections $b_1, \dots, b_n$ that have no common zero. The sections give a Fubini and Study metric on $L$. This section proves that the integral of the top power of its first Chern form is the self-intersection number $\Delta^D$ of a divisor $\Delta$ of $L$. The proof is a Crofton formula. The integral is the average number of common zeros of $D$ random linear combinations of the $b_j$, with Gaussian coefficients. For almost all coefficients this number is the intersection number. The result is the main input of the [theorem on the Chern degree over the complex numbers](/entry/chern2-chern-degree-complex/), which compares the degree of a line bundle with the integral of a [Chern form](/learn/positivity-resolution/#chern-weil-forms).

Let $Y$ be a projective variety over $\mathbb{C}$ of dimension $D$ ([schemes and varieties](/learn/geometry/#schemes-and-varieties)). We write $Y(\mathbb{C})$ for its set of complex points, with the analytic topology. It is compact, Hausdorff and second countable. Let $L$ be a [line bundle](/learn/geometry/#line-bundles-and-divisors) on $Y$, with trivializations on an open cover $(U_i)$ and sections $b_1, \dots, b_n$ of $L$ with $\bigcup_j \{b_j \neq 0\} = Y$. On $U_i$ we write $b_{j,i}$ for the function that $b_j$ gives in the trivialization.

**Definition 7.10.1 (Fubini and Study weight).** The *Fubini and Study weight* of $b$ is the family of functions
$$\varphi_i(y) = \log \sum_{j=1}^n |b_{j,i}(y)|^2 \qquad (y \in U_i(\mathbb{C})).$$
Its *Chern measures* $\mu_\varphi^+$ and $\mu_\varphi^-$ are the measures on $Y(\mathbb{C})$ that, in each algebraic chart of dimension $D$, have the densities $\max(\rho, 0)$ and $\max(-\rho, 0)$, where $\rho$ is the density of $(dd^c \varphi_i)^D$ in the chart. For a set $S$ and a function $f$, the *Chern integral* is
$$\int_S f \, (dd^c \varphi)^D = \int_S f \, d\mu_\varphi^+ - \int_S f \, d\mu_\varphi^-.$$

The weight $\varphi$ is the metric $\|s\|^2 = |s_i|^2 / \sum_j |b_{j,i}|^2$ on $L$. On two charts the functions $\varphi_i$ differ by $\log$ of the square of the absolute value of a holomorphic unit, so $dd^c \varphi_i$ does not depend on $i$.

**Theorem 7.10.2 (Crofton formula).** Let $Y$ be a complex projective variety of dimension $D$, $L$ a line bundle on $Y$ and $b_1, \dots, b_n$ sections of $L$ without common zero. For a complex $D \times n$ matrix $C$ let
$$Z(C) = \Big\{ y \in Y(\mathbb{C}) : \sum_{j=1}^n C_{kj} \, b_j(y) = 0 \text{ for } k = 1, \dots, D \Big\}.$$
Then there is a probability measure $\mu$ on the space of matrices, absolutely continuous with respect to the Lebesgue measure, with
$$\int_{Y(\mathbb{C})} (dd^c \varphi)^D = \int \# Z(C) \, d\mu(C),$$
where $\# Z(C)$ is the number of points of $Z(C)$, taken as $0$ if $Z(C)$ is infinite.

Lean: `GlobalTheory.CompanionTheory.FSCrofton.crofton` (also `GlobalTheory.T.chern_integral_random_sections`, a second name).

The measure is the standard Gaussian measure, with density $\pi^{-Dn} e^{-\sum |C_{kj}|^2}$.

*Proof.* We take as given four inputs.

1. *Positivity.* The weight $\varphi$ is smooth and semipositive. So $(dd^c \varphi)^D \geq 0$ in each chart and $\mu_\varphi^- = 0$.
2. *Finite mass.* The function $1$ is integrable for $\mu_\varphi^+$ on $Y(\mathbb{C})$, so $\mu_\varphi^+(Y(\mathbb{C})) < \infty$.
3. *Disjoint refinement.* Let $(S_t)$ be a family of open sets that covers a second countable space. Then there are finitely many pairwise disjoint sets $A_1, \dots, A_m$ that cover the space, each $A_s$ is contained in some $S_t$, and each $A_s$ is a countable union of compact sets.
4. *Local zero count.* Let $A$ be contained in one chart, in one $U_i$, and in the set where one $b_{j_0}$ does not vanish, and let $A$ be a countable union of compact sets. Let $g(C) = e^{-\sum_{k,j} |C_{kj}|^2}$. Then $C \mapsto \#(Z(C) \cap A)$ is measurable, and
$$\int g(C) \, \#(Z(C) \cap A) \, dC = \pi^{Dn} \mu_\varphi^+(A).$$

The fourth input is the Crofton formula in one chart. There the zero set of $D$ random combinations is a random linear section of the image of the chart in projective space, and the Gaussian average of its counting measure is the pullback of the Fubini and Study volume form.

The sets $S_t = (\text{chart}) \cap U_i(\mathbb{C}) \cap \{b_j \neq 0\}$, for all charts, $i$ and $j$, are open and cover $Y(\mathbb{C})$, since each point is in a chart, in some $U_i$ and in some set $\{b_j \neq 0\}$. The third input gives $A_1, \dots, A_m$. Since the $A_s$ are disjoint and cover $Y(\mathbb{C})$,
$$\# Z(C) = \sum_{s=1}^m \#(Z(C) \cap A_s), \qquad \mu_\varphi^+(Y(\mathbb{C})) = \sum_{s=1}^m \mu_\varphi^+(A_s),$$
with values in $[0, \infty]$. Each $A_s$ is measurable, since it is a countable union of compact sets. The fourth input, applied to each $A_s$ and summed, gives that $\# Z$ is measurable and
$$\int g(C) \, \# Z(C) \, dC = \pi^{Dn} \mu_\varphi^+(Y(\mathbb{C})).$$

Let $\mu = \pi^{-Dn} g(C) \, dC$. We take as given that $\int g(C) \, dC = \pi^{Dn}$, the Gaussian integral on $\mathbb{C}^{Dn}$. So $\mu$ is a probability measure. It has a density with respect to the Lebesgue measure, so it is absolutely continuous. The last equation gives $\int \# Z \, d\mu = \mu_\varphi^+(Y(\mathbb{C}))$, where $\# Z$ takes values in $[0, \infty]$. By the second input this is finite, so $\# Z(C) < \infty$ for $\mu$-almost all $C$. For those $C$ the number of points is the real number $\# Z(C)$, so the integral of the real function is the same. By the first input, $\int (dd^c \varphi)^D = \mu_\varphi^+(Y(\mathbb{C})) - 0$. $\square$

The proof shows more than the statement: the integral of $(dd^c \varphi)^D$ is the Gaussian average of the number of zeros, and this average is finite.

**Theorem 7.10.3 (Chern integral and intersection number).** Let $Y$, $L$ and $b_1, \dots, b_n$ be as in the Crofton formula. Let $\Delta$ be a Cartier divisor on $Y$ that is presented by $L$ and rational functions $r_i$, in this sense: the $r_i$ form a rational section of $L$, so $r_i = g_{ij} r_j$ with the transition functions $g_{ij}$ of $L$, and $r_i$ is a local equation of $\Delta$ at each point of $U_i$. Then
$$\int_{Y(\mathbb{C})} (dd^c \varphi)^D = (\Delta^D),$$
the intersection number of $D$ copies of $\Delta$ on $Y$.

Lean: `GlobalTheory.CompanionTheory.ChernDegree.chernInt_fsBasis_eq_inter` (also `GlobalTheory.T.chern_integral_eq_intersection`, a second name).

*Proof.* We take as given the following input. *Almost every zero count is the intersection number.* Under the hypotheses of the theorem, $\# Z(C) = (\Delta^D)$ for Lebesgue almost all $D \times n$ matrices $C$. For generic $C$ the $D$ sections $\sum_j C_{kj} b_j$ meet properly and transversally, and each is a section of $L$, so its divisor is linearly equivalent to $\Delta$.

The Crofton formula gives a probability measure $\mu$, absolutely continuous with respect to the Lebesgue measure, with $\int (dd^c \varphi)^D = \int \# Z \, d\mu$. A set of Lebesgue measure zero has $\mu$-measure zero, so $\# Z(C) = (\Delta^D)$ for $\mu$-almost all $C$. Hence
$$\int \# Z \, d\mu = \int (\Delta^D) \, d\mu = (\Delta^D) \, \mu(\text{all matrices}) = (\Delta^D),$$
since $\mu$ is a probability measure. $\square$

The theorem says that the degree of $L$, computed algebraically, is the integral of the top power of the Chern form of one Fubini and Study metric.

**Remark 7.10.4 (Formalization).** The Crofton formula is in [ChernIntegralRandomSections.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ChernIntegralRandomSections.lean#L35), and the second theorem is in [ChernIntegralEqIntersection.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ChernIntegralEqIntersection.lean#L13). The weight is `Weight.fsBasis` with the identity matrix in [NoCommonZeroCombVal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NoCommonZeroCombVal.lean#L596). The Chern measures are `chernPart` with sign $\pm 1$ and the Chern integral is `chernInt`, both in [ExistsIsClosedImmersionGenericPoint.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsIsClosedImmersionGenericPoint.lean#L278). The Gaussian weight is `gW` in [JoinCol.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/JoinCol.lean#L11). The inputs are `T.sigma_compact_disjoint_refinement`, `T.measurable_local_zero_count`, `T.gaussian_weight_total_mass` and `T.ae_zero_count_eq_intersection`. The Crofton formula takes the hypothesis `Presents Δ L r` and does not use it; the divisor $\Delta$ and the sections $r$ do not occur in its conclusion. The zero count uses `Set.ncard`, which is $0$ on an infinite set, and the proof works with `encard` until the last step. In the zero set, $y$ must satisfy the equations in each trivialization $U_i$ that contains it. The two second names are wrappers that close with `first | exact ...`.
