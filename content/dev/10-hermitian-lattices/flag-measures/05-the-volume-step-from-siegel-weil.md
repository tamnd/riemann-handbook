---
title: The volume step from the Siegel-Weil formula
decls:
  - GlobalTheory.GaussMean.volumeStep_of_siegelWeil
  - GlobalTheory.GaussMean.Step.volumeStep_of_siegelMean
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The volume step from the Siegel-Weil formula

This section proves the volume step: the gauge volume of a unitary group of rank $n$ is the gauge volume of a unitary group of rank $n - 1$ times an explicit factor. The proof compares two computations of the mean over the adelic quotient of a Gaussian sum over the vectors of length $\pm 1$. The Siegel-Weil formula gives the mean as a product of local densities. An unfolding along the stabiliser of one vector gives the same mean as a gauge volume of the smaller group. The volume step gives the volume ratio of the fourth section, and through it the flag measure bound and the counting theorem.

### The volume step

We keep the global setting of the fourth section, with gauge volume $\operatorname{vol}_c(G)$ and the factor $L_E(M)$. For $n \ge 1$ put
$$m_E(n) = \frac{\big((n-1)!\,(v_E/\pi)^n\big)^f}{\sqrt{(2 v_E)^f}}\, L_E(n).$$

**Definition 3.5.1 (Volume step).** The *volume step* is the following statement. Let $G$ be the unitary group of $J$ of size $n \ge 3$, with signature $(P, Q)$ at every infinite place, and let $\pm$ be a sign with $P \ge 1$ for $+$ and $Q \ge 1$ for $-$. Then there are a unitary group $G'$ of a form $J'$ of size $n - 1$ over the same field, with a star compatible isomorphism of fields, a vector $x \in E^n$ and an $n \times (n-1)$ matrix $A$, such that
$$x^* J x = \pm 1, \qquad x^* J A = 0, \qquad A^* J A = J',$$
$G'$ has signature $(P - 1, Q)$ for $+$ and $(P, Q - 1)$ for $-$, and for all gauge constants $c$, $c'$ and Haar measures
$$\frac{\operatorname{vol}_c(G)}{V(n)^f} = \frac{\operatorname{vol}_{c'}(G')}{V(n-1)^f}\, m_E(n).$$

Here $V$ is the function of the first section. The factor $m_E(n)$ is the ratio of the masses in the [mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups) for ranks $n$ and $n-1$.

### Gaussian sums

For a sign vector $\varepsilon$ of length $n$ put $q_\varepsilon(y) = \sum_i \varepsilon(i) |y_i|^2$ and $g(y) = \exp(-\sum_i |y_i|^2)$ for $y \in \mathbb{C}^n$. Let
$$\gamma_\varepsilon(\beta) = \frac{d}{dt}\Big|_{t = \beta} \int_{q_\varepsilon(y) \le t} g(y)\, dy$$
be the density of the Gaussian on the level sets of $q_\varepsilon$.

**Definition 3.5.2 (Gaussian sum).** For $x \in G_{\mathbb{A}}$ and $\beta \in E$ let
$$\Theta_\beta(x) = \sum_{\substack{y \in \Lambda_x \\ y^* J y = \beta}} \prod_v g\big(x_v^{-1} P_v^{-1} \varphi_v(y)\big).$$

**Definition 3.5.3 (Siegel mean).** Put
$$C_E(n) = \frac{(2 v_E)^{f/2}}{v_E^{nf}\, L_E(n)}.$$
The *Siegel mean* is the statement: for $n \ge 3$, a sign $\pm$, a Haar measure $\mu_f$ and a fundamental domain $D$ for $\Gamma$ in $G_{\mathbb{A}}$, we have $\mu_{\mathbb{A}}(D) < \infty$ and
$$\int_D \Theta_{\pm 1}\, d\mu_{\mathbb{A}} = \mu_{\mathbb{A}}(D)\, C_E(n) \prod_v \gamma_{\varepsilon_v}(\pm 1).$$

So the Gaussian sum has mean $C_E(n) \prod_v \gamma_{\varepsilon_v}(\pm 1)$ over the quotient, a product of an archimedean density and a constant that collects the local densities at the finite places.

### From the Siegel mean to the volume step

**Theorem 3.5.4 (Volume step from the Siegel mean).** The Siegel mean implies the volume step.

Lean: `GlobalTheory.GaussMean.Step.volumeStep_of_siegelMean`.

*Proof.* Let $G$ have size $n \ge 3$ and signature $(P,Q)$, and fix the sign. The proof has six steps.

1. There are a unitary group $G'$ of size $n - 1$ over the same field, a point $x_f$, a vector $x \in \Lambda_{x_f}$ with $x^* J x = \pm 1$ and a matrix $A$ with $x^* J A = 0$ and $A^* J A = J'$, such that the lattice of $G'$ is the set of $y$ with $A y \in \Lambda_{x_f}$. The signature of $G'$ is as in the volume step.
2. Take a fundamental domain $D$ for $\Gamma$ in $G_{\mathbb{A}}$. Unfold the integral of $\Theta_{\pm 1}$ along the orbits of $\Gamma$ on the vectors of length $\pm 1$. The stabiliser of $x$ is the group $G'$, and the integral over the orbit of a vector is a gauge volume of $G'$ times a local Gaussian integral. This gives
$$\frac{\prod_v c_v \int_D \Theta_{\pm 1}\, d\mu_{\mathbb{A}}}{\mu_f(K_f)} = \operatorname{vol}_{c'}(G')\, 2^{nf} \prod_v \gamma_{\varepsilon_v}(\pm 1).$$
3. The Siegel mean gives the left side as $\prod_v c_v\, \mu_{\mathbb{A}}(D)\, C_E(n) \prod_v \gamma_{\varepsilon_v}(\pm 1) / \mu_f(K_f)$, which is $\operatorname{vol}_c(G)\, C_E(n) \prod_v \gamma_{\varepsilon_v}(\pm 1)$, since $\mu_{\mathbb{A}}(D)$ is the covolume of $\Gamma$.
4. The factors are positive and finite: $L_E(n) > 0$, and $\gamma_{\varepsilon_v}(\pm 1) > 0$ because the density is continuous and positive on the level sets that are not empty. The level set for $+1$ needs $P \ge 1$ and the one for $-1$ needs $Q \ge 1$.
5. So $\operatorname{vol}_c(G)\, C_E(n) = 2^{nf} \operatorname{vol}_{c'}(G')$. With $r_E(n) = (2 v_E)^{f(n - 1/2)} L_E(n)$ from the fourth section, $r_E(n)\, C_E(n) = 2^{nf}$, so $\operatorname{vol}_c(G) = r_E(n) \operatorname{vol}_{c'}(G')$.
6. The identity $m_E(n)\, V(n)^f = r_E(n)\, V(n-1)^f$ turns this into the volume step. $\square$

### From the Siegel-Weil formula to the Siegel mean

The Siegel-Weil formula in its convergent range is due to Weil (Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), 1-87). For a CM extension $E/F$ with nontrivial automorphism $\sigma$, a nondegenerate Hermitian form $J$ of size $M$, and a nondegenerate Hermitian matrix $T$ of size $m$ with $2m < M$, it states two things. The adelic quotient of the unitary group of $J$ has finite volume. For a Schwartz function $\Phi = \Phi_\infty \otimes \Phi_f$ on $(\mathbb{A}_E^{M})^m$, the mean over the quotient of the theta series
$$x \mapsto \sum_{X \in E^{M \times m},\ X^* J X = T} \Phi(x^{-1} X)$$
is the product $g_\infty(T) \prod_v g_v(T)$ of continuous local densities of the Gram map, and this product converges.

**Theorem 3.5.5 (Volume step from the Siegel-Weil formula).** Assume the Siegel-Weil formula in its convergent range for all CM extensions and all nondegenerate Hermitian forms. Then the volume step holds.

Lean: `GlobalTheory.GaussMean.volumeStep_of_siegelWeil`.

*Proof.* The proof has four steps.

1. Take $m = 1$ in the Siegel-Weil formula. For $M \ge 3$ the condition $2m < M$ holds. This gives the formula for one vector $X$ with $X^* J X = \beta$, $\beta \ne 0$, for test functions with compactly supported archimedean part.
2. Take the finite part to be the indicator of the lattice. The finite densities collect into $C_E(n)$, and the archimedean density of a smooth compactly supported $\phi_v \ge 0$ at $\pm 1$ is its density $D_v(\pm 1)$ on the level set. This gives the Siegel mean for such $\phi_v$ in place of the Gaussian.
3. The Gaussian is the increasing limit of smooth compactly supported functions. Their sums over the lattice and their densities converge to those of the Gaussian, by monotone convergence. This gives the Siegel mean.
4. Apply the theorem on the volume step from the Siegel mean. $\square$

**Remark 3.5.6 (Formalization).** The Siegel-Weil formula is the hypothesis `HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent` (SiegelWeilUnitaryConvergent.lean, line 46); it is assumed, not proved. The volume step is `VolumeStep` (SameKindIsometric.lean, line 32), the Siegel mean is `SiegelMean` (GaugeUnfold.lean, line 29), $C_E$ is `meanConst`, $m_E$ is `massRatioRightSide`, $\Theta_\beta$ is `gaussSum`, $\gamma_\varepsilon$ is `gaussDens` and $V$ is `volU`. The theorem from the Siegel-Weil formula is a pure composition of four results (VolumeStepOfSiegelWeil.lean, line 13): `oneVectorCc_of_siegelWeil`, `siegelMeanCc_of_oneVectorCc`, `siegelMean_of_cc` and `volumeStep_of_siegelMean`; the first three are not unfolded here, and steps 1 to 3 above follow their names and the intermediate statements `OneVectorCc` and `SiegelMeanCc`. The proof from the Siegel mean uses `exists_unit_vector_orthogonal_instance_rank_three`, `gaussianSum_stabiliserUnfolding`, `gaussianQuadricDensity_exists_pos_continuous`, `mass_ratio_rank_factor` and the algebraic lemma `ennreal_volume_ratio_step_cancel`.
