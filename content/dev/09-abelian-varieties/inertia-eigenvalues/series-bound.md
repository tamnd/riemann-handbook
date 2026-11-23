---
id: series-bound
title: Theta series have bounded l-denominators uniformly in the level
kind: theorem
decl: GlobalTheory.LevelSeries.series_bound
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.SerIntAtOfSeriesRat
covers: 434
status: drafted
drafted_by: writer@claude
---
This theorem says that a theta series of an odd-rank vacuum pair has $l$-denominators bounded by $l^c$, where $c$ does not depend on the auxiliary level. It also writes the series as an $O$-combination of sections on a moduli space. It is the main input to the integrality half of [the series rationality and integrality theorem](/entry/series-rat-s-and-ser-int-of-global-artin/).

## Statement

Fix a vacuum pair `VacPair` with Weil representation $\omega$ and vacuum vector $f_0$. The space $W$ has odd rank $r = p + q$. Fix a Hecke character $\chi$ and $M_0 \neq 0$ with `ChiData`: $\chi$ is tied to the character $\chi_W$ by `ChrEq` (not unfolded here) and is unramified at primes prime to $M_0$. Fix a prime $l$ and an element $s$ with trivial archimedean component (the group `GfC V`). Then there is $c \in \mathbb N$ with the following property.

Take a level $l_2$ with $M = M_0 \cdot p_d$, where $p_d$ is prime to $M_0$ and to $l$, $M$ is prime to a fixed bad number, and $l_2$ is good at $l$. Take a moduli space $X$, a coefficient field $F$ with an embedding $\sigma$, an unfolding $U$, and the frame data that tie $X$ to $W$. Take a place $\lambda$ of $F$ above $l$, and a subring $O \subseteq \mathbb C$ that contains $\sigma(x)$ for every $x$ that is $\lambda$-integral (`ValRing`). Take a theta function $\varphi$ made from a level function $\Phi$ with values in $O$, and a harmonic polynomial $Q$ with coefficients in $O$. Then there are $\beta_1, \dots, \beta_m \in O$ and sections $f_1, \dots, f_m$ with holomorphic restriction and integral values at points over $\lambda$ (`BddAll`), such that for all $g$:
$$l^c \cdot \theta_s(g; \varphi, Q) = \sum_k \beta_k \cdot \kappa \cdot c_U(g)\, \mu(g)\, f_k(g).$$
Here $\kappa$ is the positive real number `lieFac`, a power of $2\pi x$, and $c_U$, $\mu$ are fixed scalars of the unfolding.

## Proof

The constant is $c = vK + c_f + c_a + c_3$. Each term comes from one lemma. The proof calls these lemmas before it chooses the level $l_2$, so $c$ does not depend on it.

1. `vacuum_pair_uniform_level_bound` gives $K$ with $M^K \varphi$ in the $O$-span of Heisenberg translates of $f_0$. Write $M_0 = l^v M_1$ with $l \nmid M_1$. Then $M_1 p_d$ is a unit in $O$, so $l^{vK}\varphi$ is in the span.
2. `exists_centralFlip_thetaTranslate_halfLevel` gives $c_f$. It moves the series to a half-level idempotent and a translate $s z_2 z_1$.
3. `exists_levelSeries_translate_boundedDenominator` writes the translated series as a series at $h$ of $\omega(a, 1)$, with $a$ rational and of bounded $l$-denominator.
4. `real_rational_point_acts_harmonic_substitution` gives $c_a$: $l^{c_a}\omega(a,1)$ sends the pair $(f, Q)$ to a pair $(f, Q')$ with $Q'$ integral.
5. `const_dvd` gives $c_3$. The comparison of the theta series with forms, `exists_forms_theta_short_series_identity`, has a factor (index times cardinality times a power of $2 \cdot \mathrm{disc} \cdot N$). This factor divides $l^{c_3}$ times a number prime to $l$, and the proof divides by that number in $O$.

## In the Lean code

The theorem is at [SerIntAtOfSeriesRat.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SerIntAtOfSeriesRat.lean#L137). In the same file, `serIntAt_record` uses it to prove `SerIntAt`. `ValRing` is in [ValRingLocRing.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ValRingLocRing.lean#L40). `const_dvd` is in [IsTorsionFreeIntOf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsTorsionFreeIntOf.lean#L99). We have not unfolded `VacPair`, `Unf`, `stdF` or `thetaKO`. We describe them by the role that they have in this proof.
