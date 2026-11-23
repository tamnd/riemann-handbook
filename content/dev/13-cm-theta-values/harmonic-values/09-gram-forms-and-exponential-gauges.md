---
title: Gram forms and exponential gauges
decls:
  - Formalism.MainNotions.ModuliIntegralCharts.H1.frTruncFix_of
  - Formalism.MainNotions.ModuliIntegralCharts.H1.phiCMinima_holds
  - Formalism.MainNotions.ModuliIntegralCharts.H1.gram_form_phi_holds
  - Formalism.MainNotions.ModuliIntegralCharts.H1.ExpGauge.expGaugeOf_of
  - Formalism.MainNotions.ModuliIntegralCharts.H1.ExpUniqChart.expUniqTan
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gram forms and exponential gauges

The step [every character of literature](/step/every-character-of-literature/) uses three more inputs next to the bounds of the previous sections. The first input makes the frames of a chart compatible with truncation. The second gives a short basis for a hermitian lattice in terms of a constant $\phi_C$ of its Gram form. The third replaces a chart by an exponential chart, in which the formal group becomes additive and the harmonic values become plain coefficients. This section proves these inputs. The background is in [lattices in quadratic and hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces), [number fields and their integers](/learn/number-fields/#number-fields-and-their-integers), [formal group laws](/learn/formal-groups/#formal-group-laws) and [the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm).

### Truncation compatible frames

Let $E$ be a CM [[number field|MWBDFS2KJ5]] whose involution on $\mathcal{O}_E$ is complex conjugation $a \mapsto \bar a$. Let $S$ be a $\mathbb{Q}$-algebra, let $y$ be a framed point over $S$, and let $C$ be a chart at $y$ of dimension $d$, as in the [second section](/entry/exists-analytic-chart/). The chart has a formal group law $F$ in $d$ variables, an action of $\mathcal{O}_E$ by series $[a]$, and for each order $m$ a frame $e_m$: a generator of the pullback of the line bundle to the jets of order $m$ in two points. The frames of different orders need not agree under truncation.

**Definition 2.9.1 (frame ratio).** The chart has *frame ratios* if, for each $m$, there is a unit jet $U_m$ of order $m$ in two sets of $d$ variables with four properties.

1. The truncation of $e_{m+1}$ to order $m$ equals $U_m \cdot e_m$.
2. Cocycle: $U_m(F(x_0, x_1), x_2) = U_m(x_0, x_2)\, U_m(x_1, x_2)$.
3. Symmetry in the two sets of variables.
4. $\mathcal{O}_E$-balance: $U_m([a] x, x') = U_m(x, [\bar a] x')$ for $a \in \mathcal{O}_E$.

For a $d \times d$ matrix $c$, let $\mathrm{bil}(c)(x, x') = \sum_{i,j} c_{ij} \log_F(x)_i \log_F(x')_j$, where $\log_F$ is the logarithm of $F$. A matrix $c$ is *balanced* if $D[a]^{\top} c = c\, D[\bar a]$ for all $a$, where $D[a]$ is the linear part of $[a]$.

**Theorem 2.9.2 (truncation compatible frames).** Assume that every chart has frame ratios. Then every chart $C$ has a new family of frames $e'_m$ and symmetric balanced matrices $c_m$ with $c_0 = 0$ such that the following hold. The frames $e'_m$ are compatible with truncation, they agree with the rigidification at the origin, and
$$e'_m = \exp\big(-\mathrm{bil}(c_m)\big)\, e_m$$
for every $m$.
Lean: `Formalism.MainNotions.ModuliIntegralCharts.H1.frTruncFix_of`

*Proof.* Fix $m$. A unit jet with the cocycle law in the first variable is a homomorphism from the formal group $F$ to the multiplicative group, in each value of the second variable. Over a $\mathbb{Q}$-algebra such a homomorphism is $\exp$ of a linear form in $\log_F$. By symmetry the jet is also of this form in the second variable, so $U_m = \exp(\mathrm{bil}(c'_m))$ for a matrix $c'_m$. Symmetry of $U_m$ makes $c'_m$ symmetric, and balance of $U_m$ makes $c'_m$ balanced. Put $c_0 = 0$ and $c_{m+1} = c_m - c'_m$. By induction, each $c_m$ is symmetric and balanced. Put $e'_m = \exp(-\mathrm{bil}(c_m))\, e_m$. Then the truncation of $e'_{m+1}$ is
$$\exp(-\mathrm{bil}(c_{m+1}))\, U_m\, e_m = \exp(-\mathrm{bil}(c_m))\, e_m = e'_m.$$
At the origin, $\mathrm{bil}(c_m)$ vanishes, so the rigidification is unchanged. $\square$

The hypothesis holds: frame ratios exist for every chart. They come from the fact that two frames of the same line bundle differ by a unit, and the cocycle law is the biextension property of the line bundle.

### Gram forms and the constant phi

Let $E$ be a number field of degree $n$ with an involution $c \mapsto \bar c$ that is complex conjugation under every embedding, and assume that the involution is not the identity. Let $w_0 \in \mathcal{O}_E$ with $w_0 + \bar w_0 = 1$. Let $Y$ be a free $\mathbb{Z}$-module of finite rank $r$ with an action of $\mathcal{O}_E$.

**Definition 2.9.3 (hermitian Gram forms).** A *hermitian Gram form* on $Y$ is a symmetric $\mathbb{Z}$-bilinear form $\beta : Y \times Y \to \mathbb{R}$ with $\beta(ca, b) = \beta(a, \bar c b)$ for all $c \in \mathcal{O}_E$. They form a real vector space $\mathrm{Sym}(Y)$.

**Definition 2.9.4 (the constant phi).** A linear functional $l$ on $\mathrm{Sym}(Y)$ is *admissible* if it takes integer values on forms with integer values on $Y$, and positive values on nonzero positive semidefinite forms. For a form $\beta$, put
$$\phi_C(\beta) = \inf \{ l(\beta) : l \text{ admissible} \}.$$

The constant $\phi_C$ is an arithmetic minimum. Admissible functionals are the forms $l(\beta) = \sum_i \beta(x_i, x'_i)$ with $x_i, x'_i \in Y$ that are positive on the positive cone. For example, if $b_1, \dots, b_r$ is a basis, then $\beta \mapsto \sum_a \beta(w_0 b_a, b_a)$ is admissible. So $\phi_C(\beta)$ is at most $\sum_a \beta(w_0 b_a, b_a)$.

**Theorem 2.9.5 (phi minima).** Assume that $\beta$ is positive definite on $Y$. Then there are $r$ linearly independent vectors $v_1, \dots, v_r \in Y$ with
$$\frac{\beta(v_i, v_i)}{2} \le \frac{|d_E|^{2/n}}{2n}\, r^2\, \phi_C(\beta)$$
for every $i$, where $d_E$ is the [[discriminant|E0VZTNPJXA]] of $E$.
Lean: `Formalism.MainNotions.ModuliIntegralCharts.H1.phiCMinima_holds`

*Proof.* Let $l$ be admissible and let $\delta > 0$. Write $l(\gamma) = \sum_i \gamma(x_i, x'_i)$. Choose $\theta \in \mathcal{O}_E$ with $\bar\theta = -\theta$, which exists because the involution is not trivial. A Minkowski argument on $Y$, with the quadratic form $\beta$ twisted by $\theta$ and by the vectors $x_i$, gives $r$ independent vectors $v$ with
$$\beta(v, v) \le \frac{1}{2}\, l(\beta) \Big(\frac{r}{\mu_E} + \delta\Big)^2,$$
where $\mu_E^2 = n / (2 |d_E|^{2/n})$ comes from the covolume of $\mathcal{O}_E$ in $E \otimes \mathbb{R}$. Apply this first to the admissible functional $l_0(\gamma) = \sum_a \gamma(w_0 b_a, b_a)$ with $\delta = 1$. It gives a bound $B_0$ and one independent family of vectors of $\beta$-length at most $B_0$. Since $\beta$ is positive definite, there are only finitely many vectors of $\beta$-length at most $B_0$, so there are only finitely many such families. Choose the family $v$ for which the largest $\beta(v_i, v_i)$ is minimal. For every admissible $l$ and every $\delta > 0$, the family given by $l$ and $\delta$ competes with $v$, so
$$\max_i \beta(v_i, v_i) \le \frac{1}{2}\, l(\beta) \Big(\frac{r}{\mu_E} + \delta\Big)^2.$$
Let $\delta \to 0$. Since $r^2/(2\mu_E^2) = |d_E|^{2/n} r^2 / n$, this gives $\max_i \beta(v_i, v_i) \le |d_E|^{2/n} r^2\, l(\beta)/n$. Take the infimum over $l$ and divide by $2$. $\square$

**Theorem 2.9.6 (Gram form basis).** Assume that $\beta$ is positive definite on $Y$. Then $Y$ has a $\mathbb{Z}$-basis $b_1, \dots, b_r$ with
$$\frac{\beta(b_j, b_j)}{2} \le \frac{|d_E|^{2/n}}{2n}\, r^3\, \phi_C(\beta)$$
for every $j$, and with $|\beta(b_j, z)| \le 2\sqrt{r}\, \beta(z, z)/2$ for every $j$ and every $z \in Y$.
Lean: `Formalism.MainNotions.ModuliIntegralCharts.H1.gram_form_phi_holds`

*Proof.* By the phi minima theorem, $Y$ has $r$ independent vectors of $\beta$-length at most $M$, with $M$ the bound of that theorem. Embed $Y$ as a lattice in $\mathbb{R}^r$ with the inner product $\beta$. A reduced basis lemma turns $r$ independent lattice vectors with $\beta(v, v)/2 \le M$ into a basis of the lattice with $\beta(b, b)/2 \le r M$, and it gives the stated bound on the pairings. The lemma builds the basis along the flag of the independent vectors and reduces each new vector against the earlier ones. This is a version of the classical lemma that a lattice with independent vectors $v_1, \dots, v_r$ has a basis whose $j$-th vector is not much longer than the longest of $v_1, \dots, v_j$. The factor $r$ of the lemma turns $r^2$ into $r^3$. $\square$

### Exponential charts

Let $S$ be a $\mathbb{Q}$-algebra and $y$ a framed point over $S$. Let $\delta_L$ be the number of pairs $(\sigma, j)$ of an embedding and an index in the signature of the data. An *exponential chart* at $y$ is a compatible family of maps $x_m$ from the jets of order $m$ of the additive group $\mathbb{G}_a^{\delta_L}$ to the universal abelian scheme, with five properties.

1. Zero: $x_m$ sends the origin to the unit.
2. Truncation: $x_{m+1}$ restricts to $x_m$.
3. Law: $x_m$ carries the additive law to the group law.
4. Action: $x_m$ carries the diagonal action of $\mathcal{O}_E$, by the embeddings $\sigma(a)$ on the coordinate $(\sigma, j)$, to the action of $\mathcal{O}_E$ on the abelian scheme.
5. Tangent: the tangent map of $x_1$ sends the basis vector of index $(\sigma, j)$ to the vector $y.u(\sigma, j)$ of the framed point.

**Theorem 2.9.7 (uniqueness of exponential charts).** Two exponential charts at $y$ are equal.
Lean: `Formalism.MainNotions.ModuliIntegralCharts.H1.ExpUniqChart.expUniqTan`

*Proof.* Over a $\mathbb{Q}$-algebra, a homomorphism of formal groups from the additive group is determined by its tangent map, because the logarithm of the target is an isomorphism with the additive group, and a homomorphism of additive formal groups over a $\mathbb{Q}$-algebra is linear. A compatible family of maps from jets with the truncation and law properties is such a homomorphism. The tangent property fixes the tangent map. So the two charts agree. $\square$

The proof uses only the truncation, law and tangent properties. It does not use the zero and action properties.

Let $C$ be a chart at $y$ with formal group law $F$ and with directions $u$. An *exponential* for $C$ is a family $\varphi$ of $d$ series in the $\delta_L$ additive coordinates that is a homomorphism from the additive law to $F$ with tangent map $u$. Composition of $\varphi$ with the chart gives a family $x_\varphi$ of maps from the jets of the additive group.

**Definition 2.9.8 (exponential gauge).** An *exponential gauge* for an exponential chart $x$ is a family of generators $e_m$ of the pullback of the line bundle along $x_m$, compatible with truncation, rigid at the origin, and satisfying the cocycle condition of the biextension in the additive coordinates.

**Theorem 2.9.9 (exponential gauge of a chart).** Assume that every exponential $\varphi$ intertwines the action of $\mathcal{O}_E$ on $F$ with the diagonal action by the embeddings. Let $C$ be a chart whose frames are compatible with truncation, let $\varphi$ be an exponential for $C$, and assume that $x_\varphi$ is an exponential chart. Then $x_\varphi$ has an exponential gauge $e$ such that, for every $m$, $e_m = \exp(-h_L \circ \varphi)$ times the pullback of the frame of $C$ along $\varphi$. Here $h_L$ is the logarithmic part of the canonical gauge.
Lean: `Formalism.MainNotions.ModuliIntegralCharts.H1.ExpGauge.expGaugeOf_of`

*Proof.* Define $e_m$ by the formula. The frames of $C$ are compatible with truncation, and $\varphi$ is compatible with truncation, so $e$ is compatible with truncation. At the origin $h_L \circ \varphi$ vanishes, so $e$ is rigid. Composition of the frame ratio relation of $C$ with $\varphi$ gives a relation between $e_m(x + x')$ and $e_m(x)\, e_m(x')$ in the additive coordinates. The adjoint relation of the canonical gauge, together with the intertwining hypothesis, gives a bilinear form that controls the factor in this relation. The correction $\exp(-h_L \circ \varphi)$ absorbs this factor, and the cocycle condition of the chart then gives the cocycle condition of $e$. $\square$

The intertwining hypothesis holds: it follows from the linearity of the eigenvalues of the $\mathcal{O}_E$-action on the tangent space. The reason for exponential charts is that, in an exponential chart with an exponential gauge, a harmonic value of a section is a coefficient of its germ, by the identity of the [third section](/entry/harm-nab-eq-poly-deriv/). The step uses this to pass between charts.

**Remark 2.9.10 (Formalization).** The truncation compatible frames are in [CIndFrFixAsm.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/CIndFrFixAsm.lean#L45), with the conclusion in [CIndFrFix.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/CIndFrFix.lean#L35). The frame ratio hypothesis is proved in [FrRatio.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/FrRatio.lean#L258), and the closed form follows there. The constant $\phi_C$ is defined in [ModuliIntegralCharts.lean](lean:Formalism/SharpRestriction/Divisibility/ModuliIntegralCharts.lean#L47). The phi minima are in [PhiCMinima.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/PhiCMinima.lean#L27), with the statement in [PhiCSt.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/PhiCSt.lean#L20). The Gram form basis is in [GramSpace.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/GramSpace.lean#L55), and it uses the reduced basis of [ReducedBasis.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FirstCohomology/ReducedBasis.lean#L8), whose statement has the factor of the dimension. The exponential gauge is in [ExpGauge.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/ExpGauge.lean#L19). Its hypothesis is proved in the file of its statement, but the closed form in the same file still takes the linear eigenvalue statement as a hypothesis. Uniqueness of exponential charts is in [ExpUniqChart.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/ExpUniqChart.lean#L77), with exponential charts defined in [IsExpChart.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsExpChart.lean#L35). Three helper lemmas of that file use `first` combinators, and a second copy of the theorem is in a survey folder of the library.

## Notes and references

The results of this chapter feed the main line through three steps. The step [every character of literature](/step/every-character-of-literature/) uses the [harmonic values as derivatives](/entry/harm-nab-eq-poly-deriv/), the [sums over kernels](/entry/sum-hv-formal-kernel/), the [chart bound at the host field](/entry/ch-bound-host/), and the [truncation compatible frames](/entry/fr-trunc-fix-of/), [Gram form basis](/entry/gram-form-phi-holds/), [exponential gauges](/entry/exp-gauge-of-of/) and [uniqueness of exponential charts](/entry/exp-uniq-tan/) of the last section. The [theorem A](/entry/thm-a-of/) uses the [Gauss jet bound](/entry/thm-agauss/), and the step [theta local matching](/step/theta-local-matching/) uses the [one letter weight](/entry/lemma-s/). The step [every character](/step/every-character/) uses [tangent linearity](/entry/t-lin-of/).

- D. Mumford, *Abelian Varieties*, Tata Institute and Oxford University Press, 1970. Section 5 for cohomology and base change, and Section 23 for the theta group and the Heisenberg relations.
- D. Mumford, *Tata Lectures on Theta I*, Progress in Mathematics 28, Birkhäuser, 1983. Chapter II for theta functions in several variables and their derivatives.
- D. Mumford, An analytic construction of degenerating abelian varieties over complete rings, *Compositio Math.* 24 (1972), 239 to 288. The uniformization of degenerating abelian varieties used in Section 7.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergebnisse der Mathematik 22, Springer, 1990. Chapters II and III for Mumford's construction, biextensions and the degeneration data.
- J. Lubin and J. Tate, Formal complex multiplication in local fields, *Ann. of Math.* 81 (1965), 380 to 387. The formal groups with an action of a ring of integers and their logarithms.
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer, 2009. Chapter IV, Section 5, for the formal logarithm in dimension $1$.
- B. Dwork, On the zeta function of a hypersurface, *Publ. Math. IHÉS* 12 (1962), 5 to 68. The splitting function and the power series estimates behind Section 8.
- N. Koblitz, *$p$-adic Numbers, $p$-adic Analysis, and Zeta-Functions*, 2nd ed., Graduate Texts in Mathematics 58, Springer, 1984. Chapter IV, Section 2, for Dwork's lemma and the Artin-Hasse exponential.
- N. M. Katz, $p$-adic interpolation of real analytic Eisenstein series, *Ann. of Math.* 104 (1976), 459 to 571. Integrality of derivatives of modular forms at CM points, the model for harmonic values.
- J. Neukirch, *Algebraic Number Theory*, Grundlehren der mathematischen Wissenschaften 322, Springer, 1999. Chapter I, Sections 4 to 6, for lattices, Minkowski theory and the discriminant.
- J. W. S. Cassels, *An Introduction to the Geometry of Numbers*, Grundlehren der mathematischen Wissenschaften 99, Springer, 1959. Chapter V, Lemma 8, for a basis from independent lattice vectors.
- A. K. Lenstra, H. W. Lenstra and L. Lovász, Factoring polynomials with rational coefficients, *Math. Ann.* 261 (1982), 515 to 534. Reduced bases of lattices.
