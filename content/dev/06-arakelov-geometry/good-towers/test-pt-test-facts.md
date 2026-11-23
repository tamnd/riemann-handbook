---
id: test-pt-test-facts
title: The lattice facts at a test point
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.FamEx.TestPt.testFacts
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.OrdinaryCurveHodgePrime
covers: 1031
status: drafted
drafted_by: writer@claude
---
This theorem proves the test clause of the lattice families: on one open chart, after base change to a test point, the chart data satisfy six lattice identities. It is the content of [its second name](/entry/ordinary-curve-hodge-prime/), which [the existence of lattice families](/entry/family-exists-pos-holds/) uses for the last clause of `IsPreFamily`.

## Statement

Take the data and hypotheses of [the second name](/entry/ordinary-curve-hodge-prime/): the five inputs, a place $O$ above an odd prime $p$, the orbit data $(\Sigma, e, \varphi', F, w, \sigma)$ with $w^{p-1} = u p$ for a unit $u$, an open chart $c$ with chart ring $R$, and chart data $D$ that satisfy `Base` over $R$.

A *test point* is a subring $R_C$ of a field $C$ such that $C$ is algebraically closed, $R_C = \{v \leq 1\}$ for a valuation $v$ with $v(p) < 1$, $R_C$ is $p$-adically complete, and $R$ maps into $R_C$. A *lift* of $\sigma$ is a family of multiplicative maps $\chi_\tau \colon F \to C$ such that $\chi_\tau(a) - o$ lies in the maximal ideal of $R_C$ when $o \in O$ reduces to $\sigma_\tau(a)$.

Write $D'$ for the base change of $D$ to $R_C$. Let $\mathfrak{a}_\tau \subset C^n$ be the set of $x$ such that $a \mapsto \sum_i x_i \chi_\tau(a_i)$ lies in $M' + p R_C^{F^n}$, and let $\mathfrak{h}_\tau$ be its dual for the dot product.

**Theorem.** For each test point and each lift $\chi$, the data $D'$ satisfy `Facts`:

1. $w R_C^n \subseteq \mathfrak{a}_\tau$;
2. the image of $\Delta'_\tau \cap (\mathfrak{h}_\tau \times C^s)$ under the second projection is $\omega'_\tau$;
3. the image of $\Gamma'_\tau \cap (C^r \times \mathfrak{h}_\tau)$ under the first projection is $w^{-1}\mathrm{lie}'_\tau$;
4. for each $i$, two ideals of $C$ built from $\mathfrak{a}_\tau$ and from $M'$ are equal (`dx`);
5. a graph built from $\Theta'_\tau$ projects onto the module `kk` (`onto`);
6. the kernel part of that graph at $\varphi'(\tau)$ is the span of the $p$-th powers of the ideal of clause 4 (`inj`).

## Proof

1. From the test point, $C$ is algebraically closed of characteristic 0. `lattice_base_change_larger_ring_holds` moves `Base` from $R$ to $R_C$, and $w \neq 0$ in $C$ because $w^{p-1} = u p$.
2. `arith_variety_prime_global_relay` gives two finite Hopf orders on $R_C$ whose carriers are the test orders, with $M'$ one of them. `arith_variety_model_hodge_relay` says that the first is an abelian factor and is tight for $v$. `arith_variety_prime_hodge_total` writes each $\chi_\tau$ as a power $\sigma'^{p^{e_\tau}}$ of one fundamental character $\sigma'$.
3. `quotient_zarhin_hodge_tate_subquotient` and then `abelian_factor_tight_field_action` give the flag conclusion `FlagConcl` for $\sigma'$.
4. Clause 1 is `arith_variety_model_prime_total`. Clauses 2 and 3 come from `hodge_kernel_image_lattice`, with inputs from `arith_variety_prime_hodge_estimate` and `ordinary_curve_model_relay`.
5. Clauses 4, 5 and 6 are `PtDx.main`, `stepGraph_snd_eq_kk` and `PtInj.kernel_stepGraph`, from the flag conclusion and the facts on $\Theta$.

## In the Lean code

The theorem is in [OrdinaryCurveHodgePrime.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/OrdinaryCurveHodgePrime.lean#L54). `Facts` and the test points are in [LieLatticeData.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/LieLatticeData.lean#L139). We have not unfolded `HopfOrder`, `IsAbFactor`, `IsTight` or `FlagConcl`. `FarguesHodgeTate` is used only in `ordinary_curve_model_relay`. The file sets `maxHeartbeats` to 4000000.
