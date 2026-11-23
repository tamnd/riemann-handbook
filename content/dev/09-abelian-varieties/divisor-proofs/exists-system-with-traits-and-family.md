---
id: exists-system-with-traits-and-family
title: Normalizing a Fourier system so that the monomial family is a member
kind: theorem
decl: GlobalTheory.USep.exists_system_with_traits_and_family
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryFourierSystemTraitsFamily
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem turns the raw Fourier system of [the chart statement](/entry/exists-unitary-fourier-system-traits-chart/) into a full system (`VSys`) whose theta terms are normalized. It is the proof of [the Fourier system with a member](/entry/exists-unitary-fourier-system-traits-family/), which [separation on the normalized blowup](/entry/sep-b-of-norm-bl/) uses. Below it are 336 declarations.

## Statement

The data and the conclusion are as in [the statement entry](/entry/exists-unitary-fourier-system-traits-family/). The objects in the conclusion are the following.

A *raw Fourier system* (`VPre`) over a local ring $A$, with weight $W = (1)$, is a family indexed by $y \in Y$. For each $y$ there are:

- a complete noetherian normal local domain $V_y$ of characteristic $0$ (`IsCN`), with a local map $\mathrm{ev}_y \colon A \to V_y$;
- a lattice $X_y$, projective over $\mathcal{O}_E$ of rank at most $\min(p, q)$;
- nonzero elements $t_{y,1}, \dots, t_{y,m_y}$ of the maximal ideal, and balanced forms $\delta_{y,k}$ on $X_y$, positive semidefinite and together positive definite;
- coefficients $u_y(\mu, c) \in V_y$ for $\mu \in X_y$ and $c$ in a label set $Q$, with a unit for each $\mu$.

The *term* is $u_y(\mu, c) \prod_k t_{y,k}^{\delta_{y,k}(\mu, \mu)}$. A *Fourier system of level $N_1$* (`VSys`) adds two conditions: `abelian₂`, a divisibility of powers of $t_y$ by elements of the maximal ideal of $A$ when $m_y = 1$; and `Four`, which says that sums of products of terms over orbits of level $N$ are approximated, for all $y$ at once, by images of one element of $A$.

A *trait* (`UTrait`) is a point of $X_F$ over the fraction field of a complete discrete valuation ring $T$ of characteristic $0$, whose degeneration is monomial in a uniformizer $\varpi$ with a form $\beta$. `HasTraitsOn` says that each trait whose closed point maps to $\operatorname{Spec} \mathcal{O}_{M, z_1}$, with image in $U$, is an index $y$ with $m_y = 1$, $T \subseteq V_y$, $t_y^2 = \varpi$ and $\delta_y = \beta$. `IsMember` says the same for the monomial family, with $\rho \colon V \to V_y$ finite and injective, $t_k^2 = \rho(s_{h(k)})$ and $\delta_k = M'\delta_{h(k)}$. The terms at $y$ must be theta terms of level $N_1$ (`IsThetaTerms`), with some term at $\mu = 0$ equal to $1$.

## Proof

1. [The chart statement](/entry/exists-unitary-fourier-system-traits-chart/), with $\max(j_0, 1)$, gives a raw system $\Phi$ of level $N_1 = (n^j)^2$ with traits, a member whose theta terms are not normalized (`IsThetaTerms₀`), a label $c_0$ with $u_{y'}(0, c_0)$ a unit for all $y'$, at most one index with $m_{y'} \neq 1$, and the conditions `Exact` and `ClassSums`.
2. Since $n \geq 3$ and $j \geq 1$, $N_1 \geq 3$. `fourierTermSystem_lam_of_exact_class_sums` gives `abelian₂` from `Exact`. `fourierTermSystem_four_of_galois_class_sums` gives `Four` from `ClassSums`; it needs the local ring to be integrally closed, which `modelStalk_normal_noetherian_fractionRing` gives.
3. Let $v_{y'} = u_{y'}(0, c_0)^{-1}$. `fourierTermSystem_indexZero_coefficient_approx` approximates $u_{y'}(0, c_0)$ by images of one element of $A$, for all $y'$ at once. `fourierTermSystem_four_rescale_approximated_units` then keeps `Four` for the system with all coefficients multiplied by $v$.
4. The rescaled system is a `VSys`. Traits do not involve the coefficients, so they stay. At $\mu = 0$ the term times $v_y$ is $1$, so `isThetaTerms_of_mul_index_zero_term_eq_one` gives normalized theta terms.

## In the Lean code

The theorem is in [ExistsUnitaryFourierSystemTraitsFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryFourierSystemTraitsFamily.lean#L22). `VPre`, `abelian₂`, `Four`, `Exact`, `ClassSums` and `rescale` are in [IsChartMemberP.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMemberP.lean#L16). `VSys` is in [OrdGeOfForall.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/OrdGeOfForall.lean#L53), `IsMember` in [SepAtBIff.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SepAtBIff.lean#L38) and `IsThetaTerms` in [IsChartMember.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMember.lean#L34). We have not unfolded `IsCoef`, `orbit` or `IsUnimodMod`, so the words "theta terms" and "orbits" follow the names. In this proof the prime $n$ only enters through $N_1 \geq 3$; [the caller](/entry/sep-b-of-norm-bl/) takes $n = 3$.
