---
title: The mean cusp weight on a fundamental set
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.fund_set_mean_cuspW
  - GlobalTheory.T.cusp_weight_integrable_on_fundamental_set
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mean cusp weight on a fundamental set

This section bounds the mean of the cusp weight over a fundamental set of an arithmetic group acting on a product of matrix balls. The cusp weight of a hermitian lattice measures how close the lattice is to a cusp, that is how small the covolume of an isotropic sublattice is. The mean is taken against the invariant density of the ball, and the bound is linear in the rank data, with a logarithm of the root discriminant of the CM field. The result enters [the volume of a good tower](/entry/good-tower-and-volume/), where the cusp weight is a correction term in the volume of a line bundle with a singular metric.

### Lattices with CM and their cusp weight

Let $E$ be a CM field and let $\Psi$ be a CM type of $E$, given as a family $\sigma_\tau$, $\tau \in \Psi$, of embeddings of $\mathcal{O}_E$ that contains exactly one embedding of each conjugate pair. Let $\Lambda$ be an $\mathcal{O}_E$-module that is free of rank $2g$ over $\mathbb{Z}$, with an alternating unimodular integral form for which multiplication by $a$ is adjoint to multiplication by $\bar a$.

A Riemann lattice on $\Lambda$ is a map $P : \Lambda \to \mathbb{C}^g$ together with a positive definite hermitian form on $\mathbb{C}^g$ whose imaginary part on $P(\Lambda)$ is the given form, and an action of $\mathcal{O}_E$ on $\mathbb{C}^g$ compatible with $P$. Its signature is $(j, j')$ if, for each $\tau$, the eigenspace of $\sigma_\tau$ has dimension $j'$ and the eigenspace of $\bar\sigma_\tau$ has dimension $j$. For a nonzero saturated isotropic $\mathcal{O}_E$-submodule $I$ of $\Lambda$ (a cusp), let $\operatorname{nz}(I)$ be the product over $\tau$ of the Gram determinants of the $\sigma_\tau$ components of a family of generators of $I$, divided by the index of their span in $I$.

**Definition 10.3.1.** The cusp weight of a Riemann lattice $R$ is
$$
w(R) = \max\Bigl(0,\ \sup_{I \text{ cusp}} \bigl(-\log \operatorname{nz}(I)\bigr)\Bigr) .
$$

### Universal families on the ball

Let $n = \lvert\Psi\rvert\, j\, j'$, and identify $\mathbb{C}^n$ with the space of families $(Z_\tau)_{\tau \in \Psi}$ of complex $j \times j'$ matrices. The ball is
$$
\mathcal{B} = \{\, Z : 1 - Z_\tau^* Z_\tau \text{ is positive definite for all } \tau \,\} .
$$
Its potential and its density are
$$
\phi(Z) = -\sum_\tau \log \det(1 - Z_\tau^* Z_\tau), \qquad \delta(Z) = \exp((j + j')\phi(Z)) .
$$
A universal family is a holomorphic family $Z \mapsto R_Z$ of Riemann lattices of signature $(j, j')$ on $\mathcal{B}$, with a fixed form, with holomorphic eigenframes whose log Gram determinant is $\phi$, such that every Riemann lattice of signature $(j, j')$ with the same form is equivalent to $R_Z$ for exactly one $Z \in \mathcal{B}$. A subgroup $\Gamma$ of the automorphisms of $\Lambda$ is arithmetic if it preserves the form and has finite index in the group of all automorphisms that preserve the form. A fundamental set for $\Gamma$ is a measurable subset $F$ of $\mathcal{B}$ that meets every $\Gamma$-orbit in exactly one point.

Let $\operatorname{rd}_E = \lvert d_E\rvert^{1/[E:\mathbb{Q}]}$ be the root discriminant of $E$.

**Theorem 10.3.2 (Mean cusp weight).** Let $Z \mapsto R_Z$ be a universal family on $\mathcal{B}$, let $\Gamma$ be arithmetic, and let $F$ be a fundamental set for $\Gamma$. Assume $1 \leq j'$ and $3j' + 1 \leq j + j'$. Then $\delta$ and $w(R_Z)\,\delta(Z)$ are integrable on $F$, the integral of $\delta$ over $F$ is positive, and
$$
\begin{aligned}
\int_F w(R_Z)\, \delta(Z)\, dZ \leq\ & \lvert\Psi\rvert\, j' \bigl(6 + \log(2 \lvert\Psi\rvert \operatorname{rd}_E) \\
&+ \log(2 \lvert\Psi\rvert j' \operatorname{rd}_E)\bigr) \int_F \delta(Z)\, dZ .
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.fund_set_mean_cuspW` (also `GlobalTheory.T.cusp_weight_integrable_on_fundamental_set`, a second name).

*Proof.* Put $v = 2 \lvert\Psi\rvert \operatorname{rd}_E$ and $r = v^{-1/2}$. Since $\operatorname{rd}_E \geq 1$ and $\lvert\Psi\rvert \geq 1$, we have $v \geq 1$.

Step 1: a group model. There is a dictionary between the ball and an archimedean unitary group: a map $\pi$ from this group onto $\mathcal{B}$ that is compatible with the action of $\Gamma$. Let $\mu$ be a Haar measure on the group.

Step 2: a small integral basis. Since $[E : \mathbb{Q}] = 2 \lvert\Psi\rvert$, the field $E$ has an integral basis $a_1, \dots, a_{2\lvert\Psi\rvert}$ with $\lvert s(a_i)\rvert \leq v$ for every embedding $s$.

Step 3: the first minimum on a fundamental domain. Let $\lambda_1(R)$ be the length of a shortest nonzero vector of $R$. With the basis of Step 2, there is a fundamental domain $D$ in the group, of positive finite measure for $\mu$, such that
$$
\int_D \log^+ \frac{r}{\lambda_1(R_{\pi(a)})}\, d\mu(a) \leq 3\, \mu(D) .
$$
Here the condition $3j' + 1 \leq j + j'$ is used.

Step 4: from the group to the ball. There is a constant $c$, positive and finite, such that for every measurable function $f \geq 0$ on $\mathcal{B}$ that is constant on the classes of equivalent lattices,
$$
\int_F f(Z)\, \delta(Z)\, dZ = c \int_D f(\pi(a))\, d\mu(a) .
$$
With $f = 1$ this shows that the integral of $\delta$ over $F$ is $c\, \mu(D)$, which is positive and finite. The first minimum and the cusp weight depend only on the class of the lattice. So Step 3 gives
$$
\int_F \log^+ \frac{r}{\lambda_1(R_Z)}\, \delta(Z)\, dZ \leq 3 \int_F \delta(Z)\, dZ .
$$

Step 5: the cusp weight and the first minimum. The first minimum $\lambda_1(R_Z)$ is continuous and positive on $\mathcal{B}$, and the cusp weight is measurable there. For every $Z \in \mathcal{B}$
$$
0 \leq w(R_Z) \leq \lvert\Psi\rvert\, j' \Bigl(2 \log^+ \frac{1}{\lambda_1(R_Z)} + \log(2 \lvert\Psi\rvert j' \operatorname{rd}_E)\Bigr) .
$$
The reason is that a cusp of small $\operatorname{nz}$ contains a short vector, and each of the $\lvert\Psi\rvert j'$ eigen directions contributes at most one factor $\lambda_1^{-2}$.

Step 6: the mean. Since $\log(1/\lambda) = \log(r/\lambda) + \frac12 \log v$, we have
$$
2 \log^+ \frac{1}{\lambda} \leq 2 \log^+ \frac{r}{\lambda} + \log v .
$$
Integrate the bound of Step 5 against $\delta$ over $F$ and use Step 4. The mean of $2\log^+(r/\lambda_1)$ is at most $6$, so the mean of the cusp weight is at most
$$
\lvert\Psi\rvert\, j' \bigl(6 + \log v + \log(2 \lvert\Psi\rvert j' \operatorname{rd}_E)\bigr) .
$$
The same bounds give the integrability of $w(R_Z)\,\delta(Z)$, since the bound of Step 5 is integrable against $\delta$ by Step 4. $\square$

**Remark 10.3.3 (Formalization).** The second name only restates the theorem (`Development/AutomorphicSpectrum/Proofs/MetricProofs/CuspWeightIntegrableOnFundamentalSetStatement.lean`). The ball, its potential and density, universal families and fundamental sets are defined in `Development/AutomorphicSpectrum/Definitions/MetricPeriods/IsFundSet.lean` (lines 14 to 85), and Riemann lattices, $\operatorname{nz}$ and the cusp weight in `Definitions/MetricPeriods/IsEigFrames.lean` (lines 14 to 63). In the definition, $\operatorname{nz}(I)$ uses a family of generators chosen by the axiom of choice, and it is $1$ when no such family exists. The proof (`CuspWeightIntegrableOnFundamentalSet.lean`, line 230) calls `GlobalTheory.T.exists_group_dictionary`, `GlobalTheory.T.cm_field_small_integral_basis`, `GlobalTheory.T.first_minimum_integral_bound`, `GlobalTheory.T.fundamental_set_to_fundamental_domain`, `GlobalTheory.T.first_minimum_continuous_cusp_weight_measurable` and `GlobalTheory.T.first_minimum_and_cusp_weight_bounds` for Steps 1 to 5, and a local lemma `weighted_mean` for Step 6. I did not unfold these lemmas; the reasons given at the end of Steps 3 and 5 are a summary, not a reading of their proofs. The proof works with extended nonnegative integrals and extends the first minimum by $1$ and the cusp weight by $0$ outside the ball.
