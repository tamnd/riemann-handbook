---
id: depth-oscillation-le-bound-every-prime
title: The depth oscillation bound at every prime, statement form
kind: theorem
decl: GlobalTheory.T.depthOscillation_le_bound_every_prime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DepthOscillationLeBoundEveryPrimeStatement
covers: 665
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`oscLe_eOf`](/entry/osc-le-e-of/), which has the real content. It gives the oscillation bound `OscLe` at every prime $p$, with the exponent `eOf`. Its user is [sumAt_of_sizes](/entry/sum-at-of-sizes/).

## Statement

Let $E$ be a CM field with a host, a datum, a level, moduli and coefficients. Let $f, k, m$ satisfy `Shape` and let the gaps satisfy `ExpBd` with bounds $M_b$, $S_m$ and $M$, as in [sumAt_of_sizes](/entry/sum-at-of-sizes/). Let $v_d \geq 0$, and let $S$, $R$ be finite sets of numbers such that `SplitPlaces` holds at each prime of $S$, $2 \in S$, the host number $d$ is in $R$, and no prime outside $S \cup R$ divides the discriminant of $E$. Then for every prime $p$, `OscLe` holds at $p$ with bound $e_p$, where $e_p$ is $0$ for $p > M$, and otherwise is given by `eOf` by cases: $p \in S$, $p \in R$, $mp < k$, and the rest.

## Proof

The proof is `first | exact @oscLe_eOf | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [DepthOscillationLeBoundEveryPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DepthOscillationLeBoundEveryPrimeStatement.lean#L11), and `oscLe_eOf` in [DepthOscillationLeBoundEveryPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DepthOscillationLeBoundEveryPrime.lean#L17). Its case $p \in S$ uses `depth_oscillation_le_at_two_cmField` for every $p \in S$, not only for $p = 2$, so the name is too narrow. `SplitPlaces`, in [Places.lean](lean:Development/AutomorphicArithmetic/CMTraceForms/Places.lean#L19), asks for places of $E$ above $p$ with total degree $f$ and mean depth $v_d$.
