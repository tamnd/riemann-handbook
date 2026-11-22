---
id: core-alt-bis
title: Vanishing of ordinary adjoint classes at automorphic points
kind: theorem
decl: UpperTheory.V.Th.core_alt_bis
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ThFinal
covers: 1145
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{DenseThresholdMainCase}$ from the hypotheses $\mathrm{HypothesesH'}$ and the cohomology package $\mathrm{CohP}$. Its uses meet at [VWin from the hypotheses H and E](/proof/vwin/). This is a pass-through. The real content is in [the ordinary vanishing theorem](/entry/ordinary-vanishing-two-of-printed-hida/).

## Statement

**Theorem.** If $\mathrm{HypothesesH'}$ and $\mathrm{CohP}$ hold, then $\mathrm{DenseThresholdMainCase}$ holds.

$\mathrm{DenseThresholdMainCase}$ says the following. Let $\ell$ be a prime, $L$ a CM field with no primitive $\ell$-th root of unity, and fix a Hida setting with its level. Let $2 \le n \le 4$, let $r$ be a residual representation, and let $x$ be a point of the universal ordinary determinant ring of $r$, with a representation $\rho$. If $\rho$ is automorphic, locally generic, irreducible and has a flag at the places above $\ell$, then every ordinary continuous 1-cocycle of the adjoint of $\rho$ is a coboundary.

$\mathrm{CohP}$ collects local and global finiteness, local Tate duality, the local and global Euler characteristic formulas, the Greenberg-Wiles formula, Poitou-Tate and a tame local statement.

## Proof

The proof is one line:

```
core_of_ord_vanishing_two_phi_all (ordinary_vanishing_two_of_printed_hida hH) (W.phiAll hC)
```

`ordinary_vanishing_two_of_printed_hida` gives $\mathrm{OrdVan2Alt}$: an ordinary cocycle is a coboundary, if the image of $\rho$ spans all matrices, the determinant is regular and $\psi_i \ne \psi_j \bar\varepsilon$. `W.phiAll` turns $\mathrm{CohP}$ into $\mathrm{PhiAll}$. Then `core_of_ord_vanishing_two_phi_all` checks the hypotheses of $\mathrm{OrdVan2Alt}$ at each automorphic point. It gets the spanning condition from irreducibility, the regularity from $\mathrm{PhiAll}$ and the residual condition on $r$, and the condition on characters from the freeness of the characters $\psi_v$ and the Hida setting.

## In the Lean code

The theorem is in [ThFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThFinal.lean#L17). It calls `core_of_ord_vanishing_two_phi_all` in [TCoreOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TCoreOf.lean#L20), `ordinary_vanishing_two_of_printed_hida` and `W.phiAll`. We have not unfolded `Alg.PhiCond`, the condition inside $\mathrm{PhiAll}$. In `core_of_ord_vanishing_two_phi_all`, the hypotheses "no primitive $\ell$-th root of unity in $L$" and "$c$ is large" are bound to `_` and never used. The name `core_alt_bis` says nothing about the statement.
