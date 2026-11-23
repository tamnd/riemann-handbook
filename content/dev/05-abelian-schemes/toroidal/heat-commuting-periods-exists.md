---
id: heat-commuting-periods-exists
title: A torus-invariant heat operator that commutes with the periods
kind: theorem
decl: GlobalTheory.heat_commuting_periods_exists
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTorusInvariantHeatOperatorCommutingPeriods
covers: 537
status: drafted
drafted_by: writer@claude
---
This theorem builds, on the Raynaud extension of a degeneration over a complete local ring, a heat operator that is invariant under the torus and commutes with the shifts by the periods. It proves [the statement form](/entry/exists-torus-invariant-heat-operator-commuting-periods/), which the boundary charts of the [log Kodaira-Spencer isomorphism](/entry/has-log-ks/) use (through `exists_isKS_of_logDer` and `isConstAlong_of_ks_zero`). There the operator goes into [`isKS_of_heat`](/entry/is-ks-of-heat/), which reads the Kodaira-Spencer class off its symbol.

## Statement

We use the setting and the names of [the statement form](/entry/exists-torus-invariant-heat-operator-commuting-periods/), which defines heat operators $\mathcal H_{i,k}$ (`Heat`) and the basic ones (`IsBasic`). In short: $R$ is a complete Noetherian local domain that contains $\mathbb{Q}$, $Q$ is a degeneration datum over $R$ with abelian part $B$, line bundle $L$ and character group $X$, in the sense of Mumford (Compositio Math. 24, 1972), and $q \colon \tilde G \to B$ is the Raynaud extension, with invariant vector fields $\partial_1, \dots, \partial_n$. The *defect* $c(k, \mu, \alpha)$ of a heat operator (`HasDefect`) is the error term when it is compared with the shift by the period of $\mu \in X$, from weight $\alpha$ to weight $\alpha + k\mu$. We have not unfolded the shift relation `ShiftEq`.

**Theorem.** Suppose that $Q$ is monomial (`IsMonomial`) in nonzero $t_1, \dots, t_m \in R$: for forms $\gamma_i$ on $X$, the period of each $y \in X$ is a unit times $\prod_i t_i^{n_i}$ with $\gamma_i(y,y) = 2n_i$. Let $D$ be a derivation of $R$ with $D(t_i) \in (t_i)$ for all $i$. Then there is a basic heat operator for $D$ with defect 0.

## Proof

1. [`exists_torusInvariant_heatOperator_polynomial_defect`](/entry/exists-torus-invariant-heat-operator-polynomial-defect/) gives a basic $h$ with defect $c = 2k\,w(\mu,\alpha) + 2k^2 \pi(\mu) + 2k\,\pi'(\mu)$, with $w(\mu, \cdot)$ additive.
2. `heatOperator_period_defect_isCocycle`: the defect of any basic $h$ is a cocycle, $c(k, \mu + \mu', \alpha) = c(k, \mu, \alpha) + c(k, \mu', \alpha + k\mu)$ for $k \geq 1$.
3. `cocycle_polynomialDefect_bilinear_additive_parts`: since $R$ has characteristic 0, comparing the coefficients of $k$ and $k^2$ gives that $w$ is bi-additive and symmetric, $\pi'$ is additive, and $\pi(\mu + \mu') = \pi(\mu) + \pi(\mu') + w(\mu', \mu)$.
4. `exists_heatOperator_period_defect_zero`: with these identities, there is a basic $h'$ with defect 0. We have not opened its proof.

## In the Lean code

The theorem is in [ExistsTorusInvariantHeatOperatorCommutingPeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorCommutingPeriods.lean#L19). The definitions `Heat`, `IsBasic` and `HasDefect` are in [HasDefect.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasDefect.lean#L58).

The monomial periods and the condition on $D(t_i)$ enter only through step 1. Steps 2 to 4 hold for any basic heat operator. The statement does not say that the symbol $\Theta$ is the Kodaira-Spencer matrix of $D$; [`isKS_of_heat`](/entry/is-ks-of-heat/) makes that link.
