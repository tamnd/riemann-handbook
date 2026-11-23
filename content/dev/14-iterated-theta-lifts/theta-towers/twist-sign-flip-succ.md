---
id: twist-sign-flip-succ
title: The row lift is a multiple of the lift along the opposite path
kind: theorem
decl: GlobalTheory.FlipRun.twist_sign_flip_succ
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedLiftFlipInvariant
covers: 403
status: drafted
drafted_by: writer@claude
---
This theorem proves the flip step `StepFlip` of the row test. Its second name [`twisted_lift_flip_invariant`](/entry/twisted-lift-flip-invariant/) is the form that [the five properties of the twisted theta lifts](/entry/theta-lift-row-properties-conj/) use. The theorem collects five facts about the grid of Hermitian spaces and gives them to `flipAt_of`. That lemma moves a path of theta lifts across the squares of the grid, one square at a time.

## Statement

The grid has nodes $(i,j)$ with $0 \le i, j \le m$, where $m$ is `D.R.m`. Right arrows go from $(i,j)$ to $(i+1,j)$ and down arrows from $(i,j+1)$ to $(i,j)$. Each arrow carries a theta lift. The given path goes from $(0,m)$ down to $(0,0)$ and then right to $(m,0)$. The opposite path goes from $(0,m)$ right to $(m,m)$ and then down to $(m,0)$.

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), `LiftsCuspidal`, `WeilConvergence`, [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and `ConstK`. Then for all large admissible choices $\mathrm{ch}$ (in the sense of `Big`) there are a combination $\tau_i$ of polynomial data and units $z_t \in \mathbb{C}^\times$ in the group `xiVals` at $t$, such that for all $t$ and data $\Phi$ there is a finite tensor $\tau$ with `IsFlipFin`, and for each measure datum $M$ correct at $t$ and each $y$:

- the iterated lift along the opposite path converges on $F_y$ (`TotConv`), and
- $\theta_\chi(\Phi)(y) = \bigl(z_t\, c_{\mathrm{tot}}(t)\bigr)^{-1} \cdot \mathrm{lift}_{\mathrm{opp}}(\tau_i \otimes \tau)(F_y)$.

Here $\theta_\chi$ (`thetaChi`) is the lift along the row from $(0,0)$ to $(m,0)$, $F_y$ (`formTop`) is a form on node $(0,m)$, and $c_{\mathrm{tot}}(t) = \prod_{i,j < m} c_{ij}(t)$. `IsFlipFin` says that the sum over $\tau$ factors as a product of local flip data over the local places. We have not unfolded `WeilConvergence` or the local flip data.

## Proof

`Big.and` joins six facts for all large choices.

1. `twist_square_commutes`, from `ThetaLocalInputs`, `WeilConvergence` and `ThetaIntegralsAgree`: on each square $(i,j)$, the lift along the route through $(i+1,j+1)$ is $c_{ij}(t)$ times the lift along the route through $(i,j)$ (`CommutesWith`).
2. `flipRun_cusp_transition`: each lift along an arrow keeps cusp forms. This is [the cusp step](/entry/cusp-step-of-large-flip-run/).
3. `endCusp_leadingForm_listed`: $F_y$ is a listed cusp form on node $(0,m)$.
4. `flipSequence_initial_term`, from `ThetaLocalInputs` and `LiftsCuspidal`: the formula holds along the given path with constant $z_t^{-1}$.
5. `localFlipStage_isTensor_placeDepth`, with no hypothesis: after $k \le m^2$ local flips the local stage is still a tensor.
6. `ConstK`: each $c_{ij}(t)$ is nonzero.

Then `flipAt_of` proves `FlipAt` by induction on $k \le m^2$. After the first $k$ squares of the list `flipOrder` are flipped, there is a path $p$ on the grid and a finite tensor such that $\theta_\chi(\Phi)(y)$ is $(z_t \prod c)^{-1}$ times the lift along $p$, with the product over those $k$ squares. Fact 4 starts the induction. In the step, the path is cut at the next square, and facts 1, 2, 3 and 6 replace one route around the square by the other, which divides the constant by $c_{ij}(t)$. At $k = m^2$ the path is the opposite path (`given_opposite_gridPaths_and_determined_by_edges`), and the product is $c_{\mathrm{tot}}(t)$.

## In the Lean code

The theorem is in [TwistedLiftFlipInvariant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedLiftFlipInvariant.lean#L21). `flipAt_of` is in [FlipOfWeilConvergenceAndTheta.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FlipOfWeilConvergenceAndTheta.lean#L62) and `CommutesWith` in [ExistsNotRelZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsNotRelZero.lean#L221).

- The name says "sign" and "succ". No sign appears, and the induction on a successor is inside `flipAt_of`, not in this theorem.
- Only the half $c_{ij}(t) \neq 0$ of `ConstK` is used. The other half, `SquareNonzero`, is dropped.
- The proof is a copy of `stepFlip_of` in [the same file as `flipAt_of`](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FlipOfWeilConvergenceAndTheta.lean#L191), with `ThetaLocalInputs` in place of `Hypotheses₂`.
