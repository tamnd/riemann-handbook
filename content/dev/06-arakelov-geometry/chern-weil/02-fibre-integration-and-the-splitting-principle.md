---
title: Fibre integration and the splitting principle
decls:
  - GlobalTheory.FlagCell2.LocFib.part_preimage
  - GlobalTheory.ChernCalc.fibre_integral
  - GlobalTheory.T.flagBundle_fibreIntegral_pullback_mul_fibreClass
  - GlobalTheory.ChernCalc.chernWeilNumbers_of_chernDegreeComplex
  - GlobalTheory.T.chernWeilNumbers_of_degree_eq_chernIntegral
  - GlobalTheory.ChernDegree.chernWeilNumbers_holds
  - GlobalTheory.T.chernNumbers_eq_integral_chernForms_smoothMetric
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fibre integration and the splitting principle

This section proves that the Chern numbers of a family of vector bundles with smooth metrics on a projective variety are the integrals of their Chern forms. The proof follows the [splitting principle](/learn/positivity-resolution/#chern-weil-forms). We pull the bundles back to the bundle of full flags, where they are filtered with line bundles as quotients. A fibre integral moves the integral from the variety to the flag bundle. There the Chern forms become polynomials in the first Chern forms of the graded line bundles, and [the theorem on polynomials in first Chern forms](/entry/integral-eval-f-c1-w-eq-inter-poly/) of the previous section computes the integral. The result is used for good metrics in [the next section](/entry/good-chern-weil/).

### Frames and flag bundles

Let $F$ be a field, let $\iota$ be a finite set and let $m : \iota \to \mathbb{N}$. For a field $K$ we write $\operatorname{Mat}_m(K) = \prod_{\tau \in \iota} M_{m_\tau}(K)$.

**Definition 5.2.1 (Frames).** Let $X$ be a projective variety over $F$ and let $k : \iota \to \mathbb{N}$. For a local ring $\mathcal{O} \subseteq K(X)$, let $P_k(\mathcal{O})$ be the set of $g \in \operatorname{Mat}_m(K(X))$ with entries in $\mathcal{O}$, with $\det g$ a unit of $\mathcal{O}$, and with $(g_\tau)_{ij} = 0$ whenever $i < k_\tau$ and $i < j$. A family of frames of type $k$ is a choice, for each point $z$ of $X$, of a nonempty set $S(z) \subseteq \operatorname{Mat}_m(K(X))$, such that each $z$ has a neighbourhood and an $A$ with this property: for $z'$ in the neighbourhood, $A' \in S(z')$ if and only if $A' A^{-1} \in P_k(\mathcal{O}_{X,z'})$.

Lean: `GlobalTheory.FlagBundle.Fr` (also `GlobalTheory.FlagBundle.Par`, the sets $P_k$).

A family of type $0$ is a family of vector bundles $E_\tau$ of rank $m_\tau$, given by their frames at each point. A family of type $m$ is a family of vector bundles with full flags, since the frames may only change by lower triangular matrices.

**Definition 5.2.2 (Full flag bundle).** Let $E$ be a family of frames of type $0$ on $X$ and let $E'$ be a family of frames of type $m$ on a projective variety $Y$. Let $f : Y \to X$ be a morphism and $\phi : K(X) \to K(Y)$ an $F$-algebra map. We say that $(Y, E')$ refines $(X, E)$ along $f$ and $\phi$ if $f$ and $\phi$ are compatible with the frames, and if this lifting condition holds: for each point $x$ of $X$ with values in a field $K$ and each $h \in \operatorname{Mat}_m(K)$ that is invertible, there is a unique $K$-point of $Y$ over $x$ attached to the class of $h$ modulo lower triangular matrices.

Lean: `GlobalTheory.FlagBundle.Refines`.

So the points of $Y$ over $x$ are the full flags in the fibres of the $E_\tau$ at $x$, and $Y$ is the bundle of full flags of $E$. We do not unfold the four compatibility conditions.

**Definition 5.2.3 (Metric).** Let $E$ be a family of frames of type $0$ on $X$, let $\sigma : F \to \mathbb{C}$ and let $O$ be an open set of $X$. A metric on $E$ over $O$ is a function $H$ that assigns to a frame $A$ and a complex point $y$ a matrix $H(A, y) \in \operatorname{Mat}_m(\mathbb{C})$ with these properties, for $y \in O_\sigma(\mathbb{C})$ and $A, A' \in S(y)$: each $H(A, y)_\tau$ is positive definite; the entries depend smoothly on $y$; and
$$H(A', y) = g \, H(A, y) \, g^*, \qquad g = (A' A^{-1})(y).$$

Lean: `GlobalTheory.GoodMetric.IsMetricOn`.

So $H(A, \cdot)$ is the Gram matrix of a [[Hermitian metric|Q6X6W2N29G]] in the frame $A$.

**Definition 5.2.4 (Chern integral of a metric).** Let $H$ be a metric on $E$ over $O$. In a chart with coordinates $z_1, \dots, z_n$, $n = \dim X$, let $\Theta_\tau$ be the curvature matrix of the Gram matrix $H(A, \cdot)_\tau$, written as a matrix of linear forms in formal variables $X_{ab}$ that stand for $dz_a \wedge d\bar z_b$. The Chern polynomials $c_k(E_\tau, H)$ are the coefficients of $\det(1 + t\Theta_\tau)$. For $R \in \mathbb{R}[X_{\tau, k}]$, substitute $c_k(E_\tau, H)$ for $X_{\tau, k}$, take the alternating sum over $w \in S_n$ of the coefficients of $X_{1 w(1)} \cdots X_{n w(n)}$, and multiply its real part by $\pi^{-n}$. The positive and negative parts of this density glue to two measures $\mu^\pm$. For $t \in \mathbb{R}$ we write
$$\int_{O} R(c(E, H)) = t$$
if $\mu^+$ and $\mu^-$ are finite on $O_\sigma(\mathbb{C})$ and $\mu^+(O_\sigma(\mathbb{C})) - \mu^-(O_\sigma(\mathbb{C})) = t$.

Lean: `GlobalTheory.GoodMetric.HasChernIntegral` (also `GlobalTheory.GoodMetric.chernTop`, the density).

This is the integral of the form $R(c_1(E, H), c_2(E, H), \dots)$ of the [Chern-Weil theory](/learn/positivity-resolution/#chern-weil-forms) of Volume 1. We do not unfold the curvature or check the constant.

**Definition 5.2.5 (Roots and the fibre class).** The roots of $m$ are the pairs $(\tau, i)$ with $\tau \in \iota$ and $i < m_\tau$. Let $E'$ be a family of frames of type $m$ on $Y$. A family of divisors $(\operatorname{gr}_{\tau, i})$ on $Y$ grades $E'$ if there is a frame $B$ at the generic point such that for each point $y$ and each root $(\tau, i)$ there is a frame $A$ at $y$ for which the diagonal entry $(B A^{-1})_{\tau, ii}$ is a local equation of $\operatorname{gr}_{\tau, i}$ at $y$. The Chern root map sends $X_{\tau, k}$ to the elementary symmetric function $e_k(x_{\tau, 0}, \dots, x_{\tau, m_\tau - 1})$. The fibre class is
$$\varpi = \prod_{(\tau, i)} (-x_{\tau, i})^{m_\tau - 1 - i}.$$

Lean: `GlobalTheory.GoodMetric.IsGraded` (also `GlobalTheory.GoodMetric.chernRoots` and `GlobalTheory.GoodMetric.fibrePoint`).

So $\operatorname{gr}_{\tau, i}$ is the divisor of the $i$-th graded line bundle of the flag on $f^* E_\tau$, and the Chern root map writes $c_k(E_\tau)$ through the roots $x_{\tau, i}$ of the splitting principle.

### The fibre integral

Let $(Y, E')$ refine $(X, E)$ along $f$ and $\phi$, with $f$ compatible with the maps to $\operatorname{Spec} F$. Let $H$ be a metric on $E$ over all of $X$. Then $H$ pulls back to a metric on the flagged family $E'$, and each graded line bundle of $E'$ carries the quotient metric. We write $\gamma_{\tau, i}$ for its first Chern form on $Y_\sigma(\mathbb{C})$, and $\varpi(\gamma)$ for the form obtained by substitution of the $\gamma_{\tau, i}$ in $\varpi$. We write $\int$ for the integral of a form on the atlas of complex points, as in the previous section, and $\mu^\pm(\beta)$ for the measures of the positive and the negative part of the density of a form $\beta$.

**Lemma 5.2.6 (Local fibre integral).** Let $\alpha$ be a form on $X_\sigma(\mathbb{C})$ and put $\beta = f^* \alpha \cdot \varpi(\gamma)$. Assume that $\beta$ is a form on $Y_\sigma(\mathbb{C})$. Let $c$ be an algebraic chart of $X$, let $A$ be a frame and let $O$ be an open set in the domain of $c$ such that $A \in S(x)$ for all $x \in O$. Then for each measurable set $T \subseteq O$ and each sign $\pm$,
$$\mu^\pm(\beta)\big(f^{-1} T\big) = \mu^\pm(\alpha)(T).$$

Lean: `GlobalTheory.FlagCell2.LocFib.part_preimage`.

*Proof.* If $T$ is empty there is nothing to prove. Otherwise pick $x_0 \in T$. Since $A$ is a frame on $O$, there is a flag at the generic point that lies in the big cell of the frame $A$. Let $\operatorname{Cell}(m)$ be the set of positions $(\tau, i, j)$ above the diagonal. Then $\dim Y = \dim X + |\operatorname{Cell}(m)|$, and the cell coordinates give a bijection from the part of $f^{-1} O$ in the big cell onto $c(O) \times \mathbb{C}^{\operatorname{Cell}(m)}$.

The complement of the big cell is the complex points of the complement of a nonempty Zariski open set. It is a null set for both measures. In the cell coordinates the top density of $\beta$ is the product of the density of $\alpha$ at the base point and a fibre density on $\mathbb{C}^{\operatorname{Cell}(m)}$. The fibre density is not negative, so the positive part of $\beta$ lies over the positive part of $\alpha$, and the same holds for the negative parts. The integral of the fibre density over each fibre is $1$. Fubini's theorem now gives the claim. $\square$

**Theorem 5.2.7 (Fibre integral over the flag bundle).** Let $\alpha$ be a form on $X_\sigma(\mathbb{C})$. Then
$$\int_{Y_\sigma(\mathbb{C})} f^* \alpha \cdot \varpi(\gamma) = \int_{X_\sigma(\mathbb{C})} \alpha.$$

Lean: `GlobalTheory.ChernCalc.fibre_integral` (also `GlobalTheory.T.flagBundle_fibreIntegral_pullback_mul_fibreClass`, a second name).

*Proof.* The map $f$ is holomorphic on complex points. The graded forms $\gamma_{\tau, i}$ are smooth and $\bar\partial$-closed, since the pulled back metric is a metric on the flagged family. So $f^* \alpha \cdot \varpi(\gamma)$ is a form on $Y_\sigma(\mathbb{C})$. Each complex point of $X$ lies in an open set $O$ in the domain of a chart on which a single frame $A$ is a frame at every point. Two finite measures on $X_\sigma(\mathbb{C})$ that agree on the measurable subsets of all such $O$ are equal. The lemma gives this for the push forward of $\mu^\pm(\beta)$ and for $\mu^\pm(\alpha)$. So the two parts have the same total masses, and the integrals agree. $\square$

For a single bundle of rank $2$ the fibre class is $-x_{0}$, and the theorem says that the form $\gamma_{0}$ of the graded line bundle with index $0$ integrates to $-1$ on each fibre $\mathbb{P}^1$.

### Chern numbers for smooth metrics

**Theorem 5.2.8 (Chern numbers from the degree formula).** Assume `ChernDegreeComplex`, the [Chern integral of a divisor](/entry/chern-degree-chern-degree-complex/). Let $X$, $Y$, $E$, $E'$, $\phi$ and $f$ be as above, with $(Y, E')$ refining $(X, E)$, and let $\operatorname{gr}$ grade $E'$. Let $H$ be a metric on $E$ over all of $X$. Then for every $R \in \mathbb{R}[X_{\tau, k}]$,
$$\int_X R(c(E, H)) = \big\langle \operatorname{cr}(R) \cdot \varpi \big\rangle_{\operatorname{gr}},$$
where $\operatorname{cr}$ is the Chern root map and the right side is the intersection form of the divisors $\operatorname{gr}_{\tau, i}$ on $Y$.

Lean: `GlobalTheory.ChernCalc.chernWeilNumbers_of_chernDegreeComplex` (also `GlobalTheory.T.chernWeilNumbers_of_degree_eq_chernIntegral`, a second name).

*Proof.* By the remark after the theorem on divisors, `ChernDegreeComplex` gives `ChernDegree` over every field with an embedding into $\mathbb{C}$. The form $\alpha = R(c(E, H))$ is a form on $X_\sigma(\mathbb{C})$, and $f$ is compatible with the structure maps. For each root $(\tau, i)$ there is a line bundle $L_{\tau, i}$ on $Y$, a family of rational sections that presents $\operatorname{gr}_{\tau, i}$, and a smooth weight $\psi_{\tau, i}$ with $c_1(\psi_{\tau, i}) = \gamma_{\tau, i}$. The measures of the Chern integral of $H$ are the two parts of the density of $\alpha$, and they are finite. So it remains to compute $\int_X \alpha$. We have
$$\begin{aligned}
\int_X \alpha &= \int_Y f^* \alpha \cdot \varpi(\gamma) \\
&= \int_Y R(c(f^*E, f^*H)) \cdot \varpi(\gamma) \\
&= \int_Y \operatorname{cr}(R)(\gamma) \cdot \varpi(\gamma) \\
&= \big\langle \operatorname{cr}(R) \cdot \varpi \big\rangle_{\operatorname{gr}}.
\end{aligned}$$
The first line is the fibre integral. The second line holds because the pull back of forms commutes with polynomials in the Chern forms, and the pull back of the Chern forms of $H$ are the Chern forms of the pulled back metric. The third line is a theorem of the development: on the flag bundle, the integral does not change when $c_k(f^* E_\tau, f^* H)$ is replaced by $e_k(\gamma_{\tau, 0}, \dots, \gamma_{\tau, m_\tau - 1})$. We do not open its proof. The last line is [the theorem on polynomials in first Chern forms](/entry/integral-eval-f-c1-w-eq-inter-poly/), applied to the weights $\psi_{\tau, i}$ and the polynomial $\operatorname{cr}(R) \cdot \varpi$. $\square$

**Theorem 5.2.9 (Chern numbers for smooth metrics).** Let $X$, $Y$, $E$, $E'$, $\phi$, $f$ and $\operatorname{gr}$ be as in the previous theorem, and let $H$ be a metric on $E$ over all of $X$. Then for every $R \in \mathbb{R}[X_{\tau, k}]$,
$$\int_X R(c(E, H)) = \big\langle \operatorname{cr}(R) \cdot \varpi \big\rangle_{\operatorname{gr}}.$$

Lean: `GlobalTheory.ChernDegree.chernWeilNumbers_holds` (also `GlobalTheory.T.chernNumbers_eq_integral_chernForms_smoothMetric`, a second name).

*Proof.* This is the theorem on Chern numbers from the degree formula applied to [the Chern integral of a divisor](/entry/chern-degree-chern-degree-complex/). $\square$

The statement of this theorem is the hypothesis `ChernWeilNumbers` of the development. The right side does not depend on the metric. So the theorem also says that the Chern integral is the same for any two smooth metrics. For $\iota$ with one element, $m = 1$ and $R = X_{1}^{\dim X}$, the flag bundle is $X$ itself, the fibre class is $1$, and the theorem is the Chern integral of a line bundle.

**Remark 5.2.10 (Formalization).** The flag bundle is not constructed. It is any $(Y, E')$ that satisfies the lifting condition, and the divisors $\operatorname{gr}$ are part of the data. The polynomial $R$ need not be homogeneous; the density takes only the coefficient of top degree. The right side is an intersection number on $Y$, not on $X$, so the push forward from $Y$ to $X$ is left to [the push forward formula](/entry/flag-push-forward/) of the next section. The comparison of $c_k(f^* E_\tau, f^* H)$ with the elementary symmetric functions of the graded forms, the existence of the weights $\psi_{\tau, i}$, the factorization of the density in cell coordinates and the value $1$ of the fibre integral are separate results of the development that the proofs cite. We have not checked the sign and the order of the exponents in $\varpi$ against the orientation of the fibres.
