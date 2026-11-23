---
id: flag-measure-bound
title: The measure of the points with a given flag type
kind: theorem
decl: GlobalTheory.FlagMeas.Bound.flagMeasureBound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsotropicFlagProbabilityBoundOfVolumeRatio
covers: 880
status: drafted
drafted_by: writer@claude
---
Given the volume step, this theorem bounds the measure of the points of $G(F) \backslash G(\mathbb{A})$ whose lattice has a short filtration of a given type. Under the name [`isotropicFlagProbabilityBound_of_volumeRatio`](/entry/isotropic-flag-probability-bound-of-volume-ratio/) it goes to [the counting theorem from the volume step](/entry/counting-theorem-of-volume-step/), where it bounds the rare flag set.

## Statement

As in [the counting theorem](/entry/counting-theorem-of-volume-step/), $E/F$ is CM, $f = [F:\mathbb{Q}]$, $G = U(J)$ for a [[hermitian form|48P4A1CX85]] $J$ of size $n$ with self-dual lattice $L$, $K_f$ is the stabilizer of $L$, and $r_d = |d_E|^{1/2f}$. The measure is $\mu = \mu_\infty \times \mu_f$, with [[Haar measures|VY0HXD3GC4]] $\mu_\infty$, $\mu_f$.

**Flag types.** A point $x$ of $G(\mathbb{A})$ gives a lattice $\Lambda_x \subset E^n$ with a metric at each infinite place. Each pair of sublattices $S' \subset S$ has a size $\mathrm{size}(S/S')$ (`Formalism.HN.sizeQ`, not unfolded here). Let $\Lambda_x(t)$ be the sum of the nonzero sublattices whose largest size is at most $t$. Let $a \ge 1$, $j \in \mathbb{Z}_{\ge 1}^a$ and $0 < \tau_1 < \dots < \tau_a < 1/2$. Then $x$ has *type* $(j, \tau)$ if there is a chain $0 = S_0 \subsetneq S_1 \subsetneq \dots \subsetneq S_a$ with $S_i = \Lambda_x(\tau_i)$, $\mathrm{size}(S_i/S_{i-1}) = \tau_i$ and $\operatorname{rk} S_i/S_{i-1} = j_i$, such that $S_a$ is the sum of the sublattices of largest size less than $1/2$ and each $\Lambda_x(t)$ with $t < 1/2$ is one of the $S_i$. For $B \subseteq \{\tau : 0 < \tau_1 < \dots < \tau_a < 1/2\}$, let $T(j,B)$ be the set of points of some type $(j,\tau)$ with $\tau \in B$.

**Theorem.** Assume `VolumeStep`. Let $\Omega$ be a [[fundamental domain|KNJA2NEZ9F]] for $G(F)$ in $G(\mathbb{A})$. Let $J$ have signature $(p,q)$ at every real place, with $2q + 2 \le n$. Let $s = \sum_i j_i \le q$ and let $B$ be measurable as above. Then $T(j,B)$ is measurable, $0 < \mu(\Omega) < \infty$, and

$$\frac{\mu(T(j,B) \cap \Omega)}{\mu(\Omega)} \le \kappa(E,p,q,j) \int_B \mathrm{dens}(\tau)\, d\tau.$$

Here $\mathrm{dens}(\tau) = \ell(\tau) \prod_i 2 f j_i / \tau_i$, with

$$\ell(\tau) = \prod_{i<k} (\tau_i/\tau_k)^{2 j_i j_k f} (\tau_i \tau_k)^{2 j_i j_k f} \prod_i \tau_i^{2 j_i (n-2s) f + 2 j_i^2 f}.$$

The constant `kapBd` is

$$\kappa = \Bigl(\frac{r_d}{2}\Bigr)^{-f d_N/2} 2^{-f(ns - s^2 + s/2)} \Bigl(\frac{\sigma_p \sigma_q}{\sigma_{p-s} \sigma_{q-s} \prod_i \sigma_{j_i}}\Bigr)^{f} \frac{(\operatorname{res}_1 \zeta_E)^a \prod_i \prod_{l=2}^{j_i} \zeta_E(l)}{\prod_{M=n-2s+1}^{n} L(E,M)},$$

with $\sigma_i = \prod_{l=1}^{i} 2\pi^l/(l-1)!$, $d_N = 4\sum_{i<k} j_i j_k + 2s(n-2s) + \sum_i j_i^2$, and $L(E,M)$ the Euler product over the primes of $E$ in `lValEta`.

## Proof

1. `pointsOfFlagTypeSet_measurable_and_invariant` makes $T(j,B)$ measurable, left $G(F)$-invariant and right $K_f$-invariant.
2. `unitary_adelic_quotient_volume_pos_lt_top` uses `VolumeStep` and $p \ge 2$ to give $0 < \mu(\Omega) < \infty$.
3. `hermVolumeRatioSameKind_of_volumeRatioInduction` turns `VolumeStep` into `VolumeRatio`. It gives $G_0$ over the same field, of signature $(p-s, q-s)$, with gauge volumes $\mathrm{vol}(G) = \mathrm{vol}(G_0) \prod_{M=n-2s+1}^{n} r_d^{f(M-1/2)} L(E,M)$.
4. [The unfolding bound](/entry/isotropic-flag-unfolding-bound/) bounds the gauge covolume of $T(j,B)$ by $\mathrm{vol}(G_0) \int_B \mathrm{dens}$, constants and volumes of $\mathrm{GL}_{j_i}$.
5. `leftQuotientCovolume_eq_fundamentalDomain_inter` turns covolumes into measures of intersections with $\Omega$. `div_le_of_scaled` divides step 4 by step 3; the gauge constants and $\mu_f(K_f)$ cancel.
6. `genLin_tamagawa_volume` gives $\mathrm{vol}(\mathrm{GL}_{j}/E) = \operatorname{res}_1\zeta_E \cdot (r_d/2)^{f j^2} \prod_{l=2}^{j} \zeta_E(l)$. `prod_five_factors_hermitian_volume` says that the product of all constants is $\kappa$. The rest is bookkeeping.

## In the Lean code

The theorem is in [IsotropicFlagProbabilityBoundOfVolumeRatio.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsotropicFlagProbabilityBoundOfVolumeRatio.lean#L64). The statement `FlagMeasureBound` is in [SameKindIsometric.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/SameKindIsometric.lean#L95). `kapBd`, `dens` and `typeSet` are in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L22), `HasType` in [LayerProd.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LayerProd.lean#L62).

- `VolumeStep` is used only in steps 2 and 3.
- We did not open the proofs of `genLin_tamagawa_volume` and `prod_five_factors_hermitian_volume`.
