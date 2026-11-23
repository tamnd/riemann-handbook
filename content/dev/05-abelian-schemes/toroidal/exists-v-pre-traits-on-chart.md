---
id: exists-v-pre-traits-on-chart
title: A raw Fourier system from a theta setup, with traits and a member
kind: theorem
decl: GlobalTheory.GSep.exists_vPre_traitsOn_chart
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryFourierSystemTraitsChart
covers: 329
status: drafted
drafted_by: writer@claude
---
This theorem builds a raw Fourier system on a theta setup over the compactification. One index of the system is the given monomial family, and the other indices are the traits of $X_F$ through an open set. It is the proof of [the chart statement](/entry/exists-unitary-fourier-system-traits-chart/), which [the normalization step](/entry/exists-system-with-traits-and-family/) uses. Below it are 329 declarations.

## Statement

The statement is that of [the chart statement](/entry/exists-unitary-fourier-system-traits-chart/). Two conditions there need words. Let $N_1 = (n^j)^2$ and let $A = \mathcal{O}_{M, z_1}$.

- `Exact`: for each index $y$, each class $\kappa$ of $X_y$ modulo $N_1$ and each label $c$, the sum of the terms $u_y(\mu, c) \prod_k t_{y,k}^{\delta_{y,k}(\mu,\mu)}$ over $\mu \equiv \kappa$ converges in $V_y$ to the image of an element of $A$.
- `ClassSums`: for each index $y_0$ and each $N_0$, there are a level $N \geq N_0$ with $N_1 \mid N$, a finite Galois extension $L$ of the fraction field of $A$, and elements $f(\kappa, c)$ of the integral closure of $A$ in $L$, whose images are the class sums of level $N$ at every index. Each Galois element that fixes a chosen maximal ideal acts on the $f(\kappa, c)$ through a linear map $\gamma$ of $X_{y_0}$ with $\gamma \equiv 1 \bmod N_1$ and $\det \gamma \equiv 1 \bmod N$.

## Proof

1. `exists_linked_thetaSystem_regular_monomialFamily` gives $j \geq j_0$, a theta setup $X_1$ of level $(n^j)^2$ linked to $X$ (`ULink`), a normal cover $M \to Z_o$ at a point $z_1$, a complete local domain $V_1$ with a finite injective map $\rho_1 \colon V \to V_1$, a local map $A \to V_1$ that agrees with $\xi$, and square roots $r_k \in V_1$ of $\rho_1(s_k)$.
2. `exists_nonempty_open_thetaRing_regular` gives a nonempty open $U \subseteq M$ on which the theta ring is regular.
3. `thetaMember_of_unitary_monomial_uniformisation` makes the family a member (`GMem`) over $V_1$, with elements $r_k$ and forms $M'\delta_k$. A member is a uniformization of the abelian variety at the point by degeneration data, compatible with the theta setup and with the action of $\mathcal{O}_E$.
4. For each trait $T$ whose image lies in $U$, `exists_finite_ext_sqrt_uniformiser_complete_dvr` adjoins a square root of $\varpi$, and the lemma `nonempty_gMem_trait` of the same file makes $T$ a member through step 3 again.
5. The index set is $\{\ast\} \sqcup \{\text{traits}\}$. The index $\ast$ carries the family, and each trait carries $m = 1$, $t = \sqrt{\varpi}$ and $\delta = \beta$. `thetaMember_exists_integral_terms_unit_shift` gives the coefficients $u$, with $u(0, c_0)$ a unit for the label $c_0$ of the theta divisor.
6. `thetaMember_terms_isThetaTerms_torsionFrames` gives the theta terms at $\ast$. `fourierTermSystem_exact_of_geometric_uniformisation` gives `Exact`. `fourierTermSystem_class_sums_unbounded_levels_one_index` gives `ClassSums`; it uses the deep towers of `thetaSystem_universalUnitary_deep_towers`.

Only $\ast$ can have $m \neq 1$, by construction. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsUnitaryFourierSystemTraitsChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryFourierSystemTraitsChart.lean#L113). The same file has `posW_one`, `projective_of_free`, `jK_spMap`, `isUnit_natCast_of_spec` and `nonempty_gMem_trait`. `GSet`, `GMem` and `HasTraitsOn` are in [HasTraitsOnOfHasTraitsP.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasTraitsOnOfHasTraitsP.lean#L19). `Exact` and `ClassSums` are in [IsChartMemberP.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMemberP.lean#L102).

The index set is `Option Tr`, where `Tr` is a sigma type over all traits, so $Y$ lives in `Type 1`. The isomorphisms $e$ and $h$ of the member are identities. We have not unfolded `ThetaSys`, `RatModel`, `Unif` or `Deep`, so "theta setup", "uniformization" and "deep towers" follow the names.
