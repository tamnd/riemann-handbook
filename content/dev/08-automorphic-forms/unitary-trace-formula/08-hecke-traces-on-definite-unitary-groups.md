---
title: Hecke traces on definite unitary groups
decls:
  - GlobalTheory.BCT.trOn_forms_hop_eq_kernSum
  - GlobalTheory.T.heckeTrace_forms_eq_dim_mul_kernelSum
  - GlobalTheory.BCT.trOn_forms_hop_eq_geom
  - GlobalTheory.T.heckeTrace_weightForms_eq_dim_mul_rationalClasses
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke traces on definite unitary groups

This section proves the trace formula for a definite unitary group in its simplest form. The adelic quotient of a definite unitary group is compact modulo the finite part, so the space of automorphic forms of a given weight and level is finite-dimensional, and the trace of a Hecke operator on it is a finite sum. We prove two forms of this sum. The first is a kernel sum over the points of the finite double coset space. The second, for a test function that is regular at one place, is a sum over rational conjugacy classes of masses, archimedean characters and orbital integrals. The second form is the starting point of [the rational geometric side](/entry/geom-urat-eq-geom-u/), which turns the class sum into the stable form used in the comparison with the twisted trace formula, on the way to the step [every character](/step/every-character/). For the background, see [the trace formula for a compact quotient](/learn/trace-formula/#the-trace-formula-for-a-compact-quotient), [compact groups](/learn/representations/#compact-groups) and [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups).

### Setting

Let $E$ be a CM field with maximal totally real subfield $E^+$, and suppose that every finite place of $E$ is unramified over $E^+$. Let $c$ be complex conjugation on $E$, and $n \ge 1$. The *definite unitary group* is
$$\mathrm{U}(E) = \{\gamma \in \mathrm{GL}_n(E) : {}^t c(\gamma)\, \gamma = 1\},$$
the [[unitary group|0R9R0Y1HDK]] of the standard [[Hermitian form|8NJ7XY6F1S]] $\sum_i c(x_i) y_i$, which is positive definite at every infinite place. Let $\mathrm{U}(\mathbb{A})$ be the group of adelic points defined by the same equation, $\mathrm{U}(\mathbb{A}_f)$ its finite part, and $\mathrm{U}(\mathbb{A}_\infty)$ its infinite part, a product of compact groups $\mathrm{U}(n)$, one for each infinite place $v$ of $E$.

Fix a *section* $S$: a set of finite places of $E$ that contains exactly one place above each finite place of $E^+$. For $w \in S$ let $\mathrm{U}_w$ be the image of $\mathrm{U}(\mathbb{A}_f)$ at $w$; at an inert $w$ it is the unitary group of [the inert places](/entry/kap-orb-congruence-eq-kap-sum/), and at a split $w$ it is $\mathrm{GL}_n(E_w)$. Let $K_w = \mathrm{U}_w \cap \mathrm{GL}_n(\mathcal{O}_w)$.

**Definition 2.8.1 (Level and test functions).** A *level* is a family of open subgroups $K'_w \subseteq K_w$, $w \in S$, with $K'_w = K_w$ for almost all $w$. Its global level is $K' = \{x \in \mathrm{U}(\mathbb{A}_f) : x_w \in K'_w \text{ for all } w \in S\}$, and $K = \{x : x_w \in K_w \text{ for all } w \in S\}$. A *test function* for $K'$ is a family $f = (f_w)_{w \in S}$ with $f_w$ compactly supported and bi-$K'_w$-invariant on $\mathrm{U}_w$, and $f_w = \mathbf{1}_{K_w}$ for almost all $w$. Put $f(x) = \prod_{w \in S} f_w(x_w)$ on $\mathrm{U}(\mathbb{A}_f)$.

**Definition 2.8.2 (Forms and Hecke operators).** A *weight* $\lambda$ is a family $(\lambda_v)$ of dominant weights of $\mathrm{GL}_n$, one for each infinite place $v$. Let $W_{\lambda_v}$ be the irreducible representation of $\mathrm{GL}_n(\mathbb{C})$ of highest weight $\lambda_v$, $\chi_{\lambda_v}$ its character, and $\dim W_\lambda = \prod_v \dim W_{\lambda_v}$.

1. An *automorphic representation* of $\mathrm{U}$ is a nonzero irreducible subspace $\pi$ of the functions on $\mathrm{U}(\mathbb{A})$ that is stable under right translation, and whose elements are continuous, left invariant under $\mathrm{U}(E)$, right invariant under an open subgroup of $\mathrm{U}(\mathbb{A}_f)$, and $\mathrm{U}(\mathbb{A}_\infty)$-finite. It has *weight* $\lambda$ if for every $v$ the representation of $\mathrm{U}(n)$ at $v$ on $\pi$ contains $W_{\lambda_v}$, restricted along $v$.
2. $\mathcal{A}_\lambda(K')$ is the span of the spaces $\pi^{K'}$ of $K'$-fixed vectors, over the automorphic representations $\pi$ of weight $\lambda$.
3. The *Hecke operator* of $f$ is $R(f) = [K : K']^{-1} \sum_{x \in \mathrm{U}(\mathbb{A}_f)/K'} f(x)\, R(x)$, where $R$ is right translation. This is $\int f(x) R(x)\, dx$ for the Haar measure that gives $K$ volume $1$.

The quotient $\mathrm{U}(E) \backslash \mathrm{U}(\mathbb{A}_f) / K'$ is finite, and for every $x$ the group $\Gamma_x = \mathrm{U}(E) \cap x K' x^{-1}$ is finite, since it is discrete in the compact group $\mathrm{U}(\mathbb{A}_\infty)$.

**Definition 2.8.3 (Kernel sum).** The *kernel sum* of $f$ in weight $\lambda$ is
$$\mathrm{KS}_\lambda(f) = [K : K']^{-1} \sum_{x \in \mathrm{U}(E) \backslash \mathrm{U}(\mathbb{A}_f) / K'} \frac{1}{|\Gamma_x|} \sum_{\gamma \in \mathrm{U}(E)} f(x^{-1} \gamma x)\, \overline{\chi_\lambda(\gamma)},$$
where $\chi_\lambda(\gamma) = \prod_v \chi_{\lambda_v}(v(\gamma))$.

### The kernel sum

**Theorem 2.8.4 (Hecke trace as a kernel sum).** Let $S$ be a section, $\lambda$ a weight, $K'$ a level and $f$ a test function for $K'$. Then the Hecke operator $R(f)$ preserves $\mathcal{A}_\lambda(K')$, and
$$\mathrm{tr}\big(R(f) \mid \mathcal{A}_\lambda(K')\big) = \dim W_\lambda \cdot \mathrm{KS}_\lambda(f).$$

Lean: `GlobalTheory.BCT.trOn_forms_hop_eq_kernSum` (also `GlobalTheory.T.heckeTrace_forms_eq_dim_mul_kernelSum`, a second name).

*Proof.* The proof has three steps.

*Step 1: scalar to vector-valued forms.* Let $W_\lambda = \bigotimes_v W_{\lambda_v}$, with $\mathrm{U}(E)$ acting through the infinite places. Let $M_\lambda(K')$ be the space of functions $F : \mathrm{U}(\mathbb{A}_f) / K' \to W_\lambda$ with $F(\gamma x) = \gamma \cdot F(x)$ for $\gamma \in \mathrm{U}(E)$. The Hecke operator acts on $M_\lambda(K')$ by the same formula. By [[Schur orthogonality|ETNDTECY97]] for the compact group $\mathrm{U}(\mathbb{A}_\infty)$, the $W_\lambda$-isotypic part of the forms is $W_\lambda \otimes M_\lambda(K')$, compatibly with $R(f)$. So the trace on $\mathcal{A}_\lambda(K')$ is $\dim W_\lambda$ times the trace on $M_\lambda(K')$.

*Step 2: the vector-valued trace.* An element of $M_\lambda(K')$ is fixed by its values at representatives $x$ of the double cosets, with $F(x)$ fixed by $\Gamma_x$. Writing the trace in this basis gives
$$\mathrm{tr}\big(R(f) \mid M_\lambda(K')\big) = [K : K']^{-1} \sum_x \frac{1}{|\Gamma_x|} \sum_{\gamma \in \mathrm{U}(E)} f(x^{-1}\gamma x)\, \mathrm{tr}\big(\gamma^{-1} \mid W_\lambda\big).$$

*Step 3: the character.* The element $v(\gamma)$ is unitary, so its eigenvalues have absolute value $1$, and the eigenvalues of $v(\gamma)^{-1}$ are their complex conjugates. So $\mathrm{tr}(\gamma^{-1} \mid W_{\lambda_v}) = \chi_{\lambda_v}(v(\gamma)^{-1}) = \overline{\chi_{\lambda_v}(v(\gamma))}$, and the product over $v$ is $\overline{\chi_\lambda(\gamma)}$. $\square$

### The class sum

For $\gamma \in \mathrm{U}(E)$ with separable characteristic polynomial, its centralizer $\mathrm{U}_\gamma$ is a torus. Let $C_\gamma \subseteq \mathrm{U}_\gamma(\mathbb{A}_f)$ be the subgroup generated by the elements that generate a relatively compact subgroup. The *mass* of $\gamma$ is
$$m(\gamma) = \frac{\big|\,\mathrm{U}_\gamma(E) \backslash \mathrm{U}_\gamma(\mathbb{A}_f) / C_\gamma\,\big|}{|\mathrm{U}_\gamma(E) \cap C_\gamma|},$$
the volume of $\mathrm{U}_\gamma(E) \backslash \mathrm{U}_\gamma(\mathbb{A}_f)$ for the Haar measure that gives $C_\gamma$ volume $1$. The *orbital integral* $O_\gamma(f)$ is the orbital integral on $\mathrm{U}(\mathbb{A}_f)$ of the [inert places section](/entry/kap-orb-congruence-eq-kap-sum/), with trivial twist and with $K$ as the compact subgroup.

**Theorem 2.8.5 (Hecke trace as a class sum).** Let $S$, $\lambda$, $K'$ and $f$ be as in the previous Theorem. Suppose that there is $w \in S$ such that every $y \in \mathrm{U}_w$ with $f_w(y) \neq 0$ has separable characteristic polynomial. Then
$$\mathrm{tr}\big(R(f) \mid \mathcal{A}_\lambda(K')\big) = \dim W_\lambda \cdot \sum_{\gamma} m(\gamma)\, \overline{\chi_\lambda(\gamma)}\, O_\gamma(f),$$
where the sum is over the conjugacy classes of $\gamma \in \mathrm{U}(E)$ with separable characteristic polynomial.

Lean: `GlobalTheory.BCT.trOn_forms_hop_eq_geom` (also `GlobalTheory.T.heckeTrace_weightForms_eq_dim_mul_rationalClasses`, a second name).

*Proof.* By the previous Theorem it is enough to compute $\mathrm{KS}_\lambda(f)$. Group the inner sum by the conjugacy class of $\gamma$ in $\mathrm{U}(E)$; the character $\chi_\lambda$ is constant on classes. If $f(x^{-1}\gamma x) \ne 0$, then $f_w(x_w^{-1}\gamma x_w) \ne 0$, so the characteristic polynomial of $\gamma$, which is that of $x_w^{-1}\gamma x_w$, is separable. So only separable classes contribute, and
$$\mathrm{KS}_\lambda(f) = \sum_\gamma \overline{\chi_\lambda(\gamma)}\, [K : K']^{-1} \sum_{x} \frac{1}{|\Gamma_{\gamma, x}|}\, f(x^{-1}\gamma x),$$
with $x$ in $\mathrm{U}_\gamma(E) \backslash \mathrm{U}(\mathbb{A}_f) / K'$ and $\Gamma_{\gamma, x} = \mathrm{U}_\gamma(E) \cap x K' x^{-1}$. For a separable class, the inner sum is the usual unfolding of an orbital integral: write $\mathrm{U}_\gamma(E) \backslash \mathrm{U}(\mathbb{A}_f)$ as $\mathrm{U}_\gamma(E) \backslash \mathrm{U}_\gamma(\mathbb{A}_f)$ times $\mathrm{U}_\gamma(\mathbb{A}_f) \backslash \mathrm{U}(\mathbb{A}_f)$, and integrate over the first factor. The first factor gives the mass $m(\gamma)$, and the second gives $O_\gamma(f)$. $\square$

The class sum is the elliptic part of the trace formula; for a definite unitary group every rational element is elliptic, and there is no other part. The regularity at one place removes the classes with repeated eigenvalues, whose centralizers are not tori. The test functions of [the matching at inert places](/entry/match-principal-congruence-inert/) and of [the split places](/entry/match-ct-mu-of-is-split-at/) are used at the other places of $S$.

**Remark 2.8.6 (Formalization).** The trace is a function that returns $0$ when the operator does not preserve the subspace ([IsUnifAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsUnifAt.lean#L19)), so the statement that $R(f)$ preserves $\mathcal{A}_\lambda(K')$ is part of the content of the proof, not of the statement. The restriction of a point to a subgroup returns $1$ when the point is not in the subgroup ([IsUnifAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsUnifAt.lean#L17)); it is used for the rational points, the local components and the finite part. The product $\prod_{w \in S} f_w(x_w)$ is a `finprod`, which is $1$ when infinitely many factors differ from $1$; for a test function this does not happen. The masses, the class sum and the kernel sum are `finsum`. The two theorems are chains of rewrites by named results for Steps 1 to 3 and for the regrouping and unfolding of the second proof ([HeckeTraceFormsEqDimMulKernelSum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeTraceFormsEqDimMulKernelSum.lean#L15), [HeckeTraceWeightFormsEqDimMulRationalClasses.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeTraceWeightFormsEqDimMulRationalClasses.lean#L14)); we did not unfold those results. The weight of $\pi$ is defined by a nonzero intertwining map from $W_{\lambda_v}$ into $\pi$ for the subgroup of $\mathrm{U}(\mathbb{A})$ supported at $v$, and the character of $W_{\lambda_v}$ is evaluated at a matrix with the given characteristic polynomial, chosen by `Classical.choose`. The second names are restatements by `first | exact …`.
