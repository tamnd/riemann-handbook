---
title: Whittaker averages over finite fields
decls:
  - Formalism.L2.SG.Closed.GGMatrixBoundOfLit_holds
  - Formalism.L2.SG.Closed.GGMatrixBound_holds
  - Formalism.L2.SG.Closed.TermsGGBound_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Whittaker averages over finite fields

At the places of good reduction, the term sums of the counting argument contain a matrix built from an average of a generic character over $\mathrm{GL}_k$ of a finite field. This section bounds that matrix. It is positive semidefinite, and its largest eigenvalue is at most $\prod_v (1 + 3/q_v)$ times its value at the identity. The proof reduces the bound to irreducible representations of $\mathrm{GL}_k(\mathbb{F}_q)$, where multiplicity one for [generic characters](/learn/periods/#generic-characters) and a lower bound for the dimension of generic representations give the constant. The bound feeds the estimate of each part of the term sums by its diagonal.

### The Gelfand-Graev average

Let $\mathbb{F}$ be a [finite field](/learn/algebra/#finite-fields) with $q$ elements, let $k \geq 0$, and let $\psi_0$ be a nontrivial additive character of $\mathbb{F}$. Let $U \subseteq \mathrm{GL}_k(\mathbb{F})$ be the group of upper triangular matrices with ones on the diagonal.

**Definition 5.7.1 (Generic character and average).** The *generic character* of $U$ is $\psi_U(u) = \psi_0\bigl(\sum_{i} u_{i, i+1}\bigr)$, and we extend it by zero: $\psi_N(x) = \psi_U(x)$ if $x \in U$ and $\psi_N(x) = 0$ in the other case. The *Gelfand-Graev average* is the class function
$$\gamma(x) = \frac{1}{\# U} \sum_{y \in \mathrm{GL}_k(\mathbb{F})} \psi_N(y x y^{-1}).$$
For a representation $\pi$ of $\mathrm{GL}_k(\mathbb{F})$ on $V$ let $\pi(\gamma) = \sum_x \gamma(x) \pi(x)$. A *Whittaker functional* on $V$ is a linear form $\ell$ with $\ell(\pi(u) v) = \psi_U(u) \ell(v)$ for all $u \in U$ and $v \in V$, and $\pi$ is *generic* if it has a nonzero Whittaker functional.

Lean: `Formalism.L2.SG.GGMirabolic.gam` (also `Formalism.L2.SG.GGMirabolic.Generic`, the generic representations).

Since $\psi_N(1) = 1$, the value at the identity is $\gamma(1) = \# \mathrm{GL}_k(\mathbb{F}) / \# U$, a positive real number. This is `gam_one`. The function $\gamma$ is the average over $\mathrm{GL}_k(\mathbb{F})$ of the conjugates of $\psi_N$, normalized by $\# U$. So $\pi(\gamma)$ commutes with $\pi$, and on an irreducible $\pi$ it is a scalar. Compare the [Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions) of the global theory, where the same character defines the Fourier coefficients.

We use four facts on $\mathrm{GL}_k(\mathbb{F})$. Each is a theorem of the formalization.

1. Multiplicity one: on an irreducible representation, two Whittaker functionals with the first nonzero are proportional. Compare the analogues over local fields of Gelfand and Kazhdan and of Shalika, cited at the end of the chapter.
2. The mirabolic bound: an irreducible generic representation has dimension at least $\prod_{i=1}^{k-1} (q^i - 1)$.
3. The order of $U$ is $q^{k(k-1)/2}$.
4. The numerical bound: for $q \geq 3$ and every $k$, $\prod_{i=1}^{k-1} (1 - q^{-i})^{-1} \leq 1 + 3/q$.

From the first fact, for irreducible $\pi$ on $V$,
$$\gamma(1)^{-1} \pi(\gamma) = \begin{cases} \dfrac{\# U}{\dim V} \, \mathrm{id} & \text{if } \pi \text{ is generic}, \\ 0 & \text{in the other case}. \end{cases}$$
This is `ConvScalar`. From the second and third facts, an irreducible generic $\pi$ satisfies $\# U / \dim V \leq \prod_{i=1}^{k-1} (1 - q^{-i})^{-1}$, since $q^{k(k-1)/2} = \prod_{i=1}^{k-1} q^i$. This is `GenericRatio`. With the fourth fact, the scalar of $\gamma(1)^{-1} \pi(\gamma)$ on an irreducible representation lies in $[0, 1 + 3/q]$.

### The matrix bound

Now let $\iota$ be a finite set of places, and for each $v \in \iota$ let $\mathbb{F}_v$ be a finite field with $q_v \geq 3$ elements and $\psi_v$ a nontrivial additive character of $\mathbb{F}_v$. Let $G = \prod_v \mathrm{GL}_k(\mathbb{F}_v)$ and $\gamma_G(x) = \prod_v \gamma_v(x_v)$, where $\gamma_v$ is the average for $\psi_v$. Then $\gamma_G(1) = \prod_v \gamma_v(1) > 0$. Let
$$P = \prod_{v \in \iota} \Bigl(1 + \frac{3}{q_v}\Bigr).$$

Let $X$ be a finite set with a free right action of $G$: if $j x = j$, then $x = 1$. Let $d$ be a function from $X \times X$ to $G$ with $j \, d(i, j) = i$ whenever $i$ and $j$ are in the same orbit. Since the action is free, $d(i, j)$ is unique on each orbit. Let $A$ be the matrix on $X$ with
$$A_{ij} = \begin{cases} \gamma_G(d(i, j)) & \text{if } i \in jG, \\ 0 & \text{in the other case}. \end{cases}$$

**Definition 5.7.2 (Matrix bound).** The *matrix bound* holds if for all such data $(\iota, \mathbb{F}_v, k, \psi_v, X, d)$ with $\psi_v \neq 1$ and $q_v \geq 3$, the matrix $A$ is positive semidefinite and
$$P \, \gamma_G(1) \, I - \bar A$$
is positive semidefinite, where $\bar A$ is the entrywise complex conjugate of $A$.

Lean: `Formalism.L2.SG.GGMirabolic.GGMatrixBound`.

**Theorem 5.7.3 (Matrix bound from the literature inputs).** If multiplicity one and the mirabolic bound hold, then the matrix bound holds.

Lean: `Formalism.L2.SG.Closed.GGMatrixBoundOfLit_holds`.

*Proof.* This is the [matrix bound from the literature inputs](/entry/gg-matrix-bound/). We give its structure. Let $\rho$ be the permutation representation of $G$ on the functions on $X$, $(\rho(g) f)(i) = f(i g)$, and let $\rho(\gamma_G) = \sum_{x \in G} \gamma_G(x) \rho(x)$. A direct computation shows that $\bar A$ is the matrix of $\rho(\gamma_G)$ in the basis of point functions, and that $A$ is its transpose. The matrix of $\rho(\gamma_G)$ is Hermitian, since $\gamma_G(x^{-1}) = \overline{\gamma_G(x)}$ and $x \mapsto x^{-1}$ exchanges the conditions $jx = i$ and $i x^{-1} = j$.

We bound its eigenvalues. Let $w \neq 0$ with $\rho(\gamma_G) w = \mu w$. There is a nonzero $G$-stable subspace $W$ on which $\rho(\gamma_G)$ acts by $\mu$ and on which each place operator $\sum_{y} \gamma_v(y) \rho(y_v)$, with $y$ in the factor at $v$, acts by a scalar $\mu_v$. Then $\mu = \prod_v \mu_v$, since $\gamma_G$ is a product over the places. At each place, decompose $W$ into irreducible representations of $\mathrm{GL}_k(\mathbb{F}_v)$. By `ConvScalar` and `GenericRatio`, $\mu_v = \gamma_v(1) c_v$ with $0 \leq c_v \leq 1 + 3/q_v$. So $\mu$ is real and
$$0 \leq \mu \leq P \, \gamma_G(1).$$

A Hermitian matrix with all eigenvalues in $[0, c]$ is positive semidefinite, and $c I$ minus the matrix is positive semidefinite. Apply this to the matrix of $\rho(\gamma_G)$ with $c = P \gamma_G(1)$. This gives the second claim for $\bar A$, and the first claim for $A$ follows since the transpose of a positive semidefinite matrix is positive semidefinite. $\square$

**Theorem 5.7.4 (Matrix bound).** The matrix bound holds.

Lean: `Formalism.L2.SG.Closed.GGMatrixBound_holds`.

*Proof.* This is the [matrix bound from the literature inputs](/entry/ggmatrix-bound-of-lit-holds/) applied to multiplicity one and to the mirabolic bound, which are both proved. $\square$

### The bound for the term sums

The term sums of the counting argument are organized in a record of terms. For our purpose it has an index set $X$, a matrix $\mathrm{GG}$ on $X$, and a real number $\Gamma_1$. It satisfies the *Gelfand-Graev bound* with constant $P_g$ if
$$P_g \, \Gamma_1 \, I - \mathrm{GG}$$
is positive semidefinite. The bound is used as follows. If a part of the term sum has the expansion $\|p\|^2 = \mathrm{Re} \sum_{i,j} \mathrm{GG}_{ij} \langle v_i, v_j \rangle$ with vectors $v_i$ indexed by $X$, then the Gelfand-Graev bound gives $\|p\|^2 \leq P_g \, \Gamma_1 \sum_i \|v_i\|^2$.

**Definition 5.7.5 (Term bound).** The *term bound* holds if for all data $(\iota, \mathbb{F}_v, k, \psi_v, X, d)$ as in the matrix bound, with $\psi_v \neq 1$ and $q_v \geq 3$, and for every record of terms on $X$ with
$$\mathrm{GG}_{ij} = \overline{A_{ij}} \quad \text{for all } i, j, \qquad \Gamma_1 = \mathrm{Re} \, \gamma_G(1),$$
the record satisfies the Gelfand-Graev bound with constant $P = \prod_v (1 + 3/q_v)$.

Lean: `Formalism.L2.SG.GGMirabolic.TermsGGBound`.

**Theorem 5.7.6 (Term bound).** The term bound holds.

Lean: `Formalism.L2.SG.Closed.TermsGGBound_holds`.

*Proof.* Under the two hypotheses on the record, the matrix $P \Gamma_1 I - \mathrm{GG}$ is the matrix $P \, \mathrm{Re}\,\gamma_G(1) \, I - \bar A$. Since $\gamma_G(1)$ is real, this is the second matrix of the [matrix bound](/entry/ggmatrix-bound-holds/), which is positive semidefinite. $\square$

The constant $P$ is close to $1$ when all $q_v$ are large: at $f$ places with $q_v \geq g$, it is at most $(1 + 3/g)^f$. The term sums use it in the form $(1 + 3/g_1)^f (1 + 3/g_2)^f$.

**Remark 5.7.7 (Formalization).** The three statements are in [GenericRatioOfBoundHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/GenericRatioOfBoundHolds.lean#L70), and the definitions are in [GGMirabolic.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GGMirabolic.lean#L106). The theorem from the literature inputs is `gg_matrix_bound`, which is `ggMatrixBoundOfLit_of` applied to the matrix identity `matrix_coefficient_equation`, the Hermitian property `totally_hermitian_form`, the eigenvalue bound (built from `local_place_bound`, `joint_eigenvector_exists` and `prod_formula'`), the spectral lemma `spectrum_positive_semidefinite`, and `convolution_scalar`, `generic_ratio_bound`, `mirabolic_card_unipotent`. Multiplicity one is `GelfandGraevMultOne_holds`, from `gelfand_graev_multiplicity_one` through the duality of Whittaker functionals, and the mirabolic bound is `mirabolic_bound`; both are proved in the tree, so the name "of literature" refers to the form of the statement, not to an assumption. The numerical bound is `ratio_numeric`, from `t_GGNumeric`. The field $\Gamma_1$ of the record is real, while $\gamma_G(1)$ is complex, so the term bound asks $\Gamma_1 = \mathrm{Re}\,\gamma_G(1)$. The term bound is `termsGGBound_of_matrix` applied to the matrix bound, and it uses only the second half of it. The record of terms has many more fields than the three used here; we did not unfold them, and we did not unfold the proofs of `local_place_bound` and `joint_eigenvector_exists`.
