---
id: exists-chart-member-traits-r
title: Normalizing a Siegel Fourier system so that the family is a chart member
kind: theorem
decl: GlobalTheory.Poinc.Sep.exists_chartMember_traitsR
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFourierTermSystemRegularTraitsGivenChart
covers: 502
status: drafted
drafted_by: writer@claude
---
This theorem turns the raw Fourier system of [the theta model statement](/entry/exists-fourier-term-system-traits-chart-theta-model/) into a full system whose theta terms are normalized. It is the proof of [the statement entry](/entry/exists-fourier-term-system-regular-traits-given-chart/), which [separation at the centre of a chart](/entry/sep-st/) uses. It is the Siegel form of [the unitary normalization step](/entry/exists-system-with-traits-and-family/). Below it are 502 declarations.

## Statement

The data and the conclusion are as in [the statement entry](/entry/exists-fourier-term-system-regular-traits-given-chart/). The objects are the following. Let $A = \mathcal{O}_{M, z_1}$.

A *raw Fourier system* (`VPre`) over $A$ is a family indexed by $y \in Y$. For each $y$ there are a complete normal noetherian local domain $V_y$ of characteristic $0$ with a local map $\mathrm{ev}_y \colon A \to V_y$; a free lattice $X_y$ of rank at most $g$; nonzero $t_{y,1}, \dots, t_{y,m_y}$ in the maximal ideal, with symmetric forms $\delta_{y,k}$ on $X_y$ that are positive semidefinite and together positive definite; and coefficients $u_y(\mu, c) \in V_y$ for $\mu \in X_y^8$ and labels $c \in Q$, with a unit among them for each $\mu$. A *Fourier system of level $N_1$* (`VSys`) adds the conditions `abelian₂` and `Four`, as in the unitary case.

A *trait* (`Trait`) is a complete discrete valuation ring $T$ of characteristic $0$ with a point of $X$ over its fraction field, whose semi-abelian extension has degeneration data monomial in a uniformizer $\varpi$ with a form $\beta$. `HasTraitsR` says: for each trait $T$ and each local map $A \to T$ that is regular for the theta ring (`RegAt`) and lies over the point of $X$, there is an index $y$ with $m_y = 1$, $V_y$ a principal ideal ring, an injective local map $T \to V_y$ that is compatible with $\mathrm{ev}_y$, $t_y = \varpi$ and $\delta_y = \beta$.

`IsChartMember` says: $\rho \colon V \to V_y$ is finite and injective and lies over $\xi$; $t_{y,k} = \rho(t_{h(k)})$ and $\delta_{y,k} = \delta_{h(k)}$ through $e$; and there are degeneration data $D$ over $V_y$, tied to the eighth power of $Q$ by $W$ (`SharpRef`), for which the terms $u_y(\mu, c) \prod_k t_{y,k}^{q_W(\delta_{y,k})(\mu)}$ are theta terms of level $N_1$ (`IsThetaTerms`), where $q_W(\beta)(\mu) = \sum_{u,v} W_{uv} \beta(\mu_u, \mu_v)$. The last clause of `IsThetaTerms` is that one term at $\mu = 0$ equals $1$.

## Proof

1. [The theta model statement](/entry/exists-fourier-term-system-traits-chart-theta-model/), with $\max(j_0, 1)$, gives a raw system $\Phi$ with traits, a member whose theta terms need not be normalized (`IsChartMemberP`), a label $c_0$ with $u_{y'}(0, c_0)$ a unit for all $y'$, at most one index with $m_{y'} \neq 1$, and `Exact` and `ClassSums` at level $N_1 = l^{2j}$.
2. As $j \geq 1$, $N_1 \geq 3$. `fourierTermSystem_lam_of_exact_class_sums` gives `abelian₂`. `fourierTermSystem_four_of_galois_class_sums` gives `Four`; it needs $A$ to be integrally closed, which `stalk_isNoetherian_normal_fractionRing` gives.
3. Let $v_{y'} = u_{y'}(0, c_0)^{-1}$. `fourierTermSystem_indexZero_coefficient_approx` approximates the $u_{y'}(0, c_0)$ by images of one element of $A$, and `fourierTermSystem_four_rescale_approximated_units` keeps `Four` after all coefficients are multiplied by $v$.
4. Traits do not involve the coefficients, so they stay. At $\mu = 0$ the term times $v_y$ is $1$, so `isThetaTerms_of_mul_index_zero_term_eq_one` gives normalized theta terms.

## In the Lean code

The theorem is in [ExistsFourierTermSystemRegularTraitsGivenChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemRegularTraitsGivenChart.lean#L20). `VPre`, `HasTraitsR` and `IsChartMemberP` are in [IsChartMemberP.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMemberP.lean#L16), and `IsChartMember`, `SharpRef` and `IsThetaTerms` in [IsChartMember.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMember.lean#L21). `Trait` is in [IsThetaCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsThetaCompact.lean#L18).

The proof uses the integral closedness of $A$ only as an instance: it is unpacked from `stalk_isNoetherian_normal_fractionRing` and never named again. The prime $l$ enters only through $N_1 \geq 3$. We have not unfolded `IsCoef`, `IsUnimodMod` or `orbit`, so "theta terms" follows the names.
