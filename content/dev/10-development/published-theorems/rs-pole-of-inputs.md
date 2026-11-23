---
id: rs-pole-of-inputs
title: The Rankin-Selberg pole statement from 22 inputs
kind: theorem
decl: PositivityTheory.AdelicQuotientData.rsPole_of_inputs
module: Development.WeilBound.CoreStatements.PublishedTheorems.JacquetShalikaRigidity.RsPoleOfInputs
covers: 858
status: drafted
drafted_by: writer@claude
---
This theorem proves `RSPole` from 22 hypotheses about adelic groups, Whittaker functions and Euler products. [`rsPole`](/entry/rs-pole/) applies it to 22 theorems of the code and states `RSPole` in full. This entry has the proof: the Rankin-Selberg integral, written as a long chain of lemmas. Below this theorem are 858 declarations.

## Statement

Suppose that the following 22 statements hold: `G0`, `CAUCHY`, `S1`, `L7`, `lift_levelP_alt₂`, `G5`, `S7`, `MirabolicColumnBlock`, `G5b`, `S2`, `S9`, `G1`, `AlmostEverywhereSpherical`, `G2c`, `G2a`, `FourierUniquenessMirabolic`, `S4`, `S8`, `CuspidalIrreducibleSubrep`, `SmoNorm`, `JacquetShalikaBound` and `StandardCharacterExists`.

**Theorem.** `RSPole` holds.

We have not unfolded most of the 22 statements. `CAUCHY` is the convergence of the Euler product $L^S$ for $\operatorname{Re} s > 2$, and `JacquetShalikaBound` gives $|\alpha_{w,a}| \le q_w^{1/2}$ for the Satake parameters (`PRSPole.bnd`).

## Proof

The proof is about 60 `have` steps, and then one call to `rspole_of`. The steps build the analytic facts in layers: a fundamental domain (`W0`), volumes and heights (`V1`, `H0`, `K1`), Poisson summation (`P0` to `P3`), unipotent integrals (`U0` to `U2`), and the bounds on cusp forms (`M0`, `KIR`, `KSec`, `KLt1`, `KEq1`). Two statements carry the analysis.

- `E2`: if $H$ has the growth `Grow H H₀`, there is $Z$, holomorphic on $\operatorname{Re} s > 0$, with $Z(s) = (s-1) \int H(g) |\det g|^s \, dg$ for $\operatorname{Re} s > 1$. If $\int_{\text{band}} H_0 = 0$, then $Z(1) = 0$.
- `M1`: the integral of $\sum f \cdot \overline{\varphi} \cdot |\det|^{-(m-k)/2} |\det|^s$ is $Z_S(s)\, L^S(s)$, with $Z_S$ entire and $Z_S(\sigma + iu) \neq 0$ for all real $\sigma$.

`rspole_of` takes a standard character $\psi$ from `StandardCharacterExists`, a cusp form $\varphi'$ of $\pi'$ from `KSec`, and a cusp form $\varphi$ of $\pi$ from `KIR`. Then it splits.

1. **Case $k < m$.** The corner embedding of $\mathrm{GL}_k$ in $\mathrm{GL}_m$ (`CornerEmbedding`), `KLt1` and `KLt2` give the data for `M1` and the growth for `E2`. Here the condition $Z(1) = 0$ is closed by `simp`.
2. **Case $k = m$.** Let $\varphi'' = 0$ if $\pi = \pi'$, and $\varphi'' = \varphi'$ otherwise. `KY` gives a closed subspace $Y$ orthogonal to $\varphi''$. By `ORT`, cusp forms of $\pi$ are orthogonal to those of $\pi'$ when $\pi \neq \pi'$, so the forms of $\pi$ lie in $Y$. `KIR` picks $\varphi$ in $Y$, `LastRowCutoff` cuts it off, and `KEq1` and `KEq2` give the data for `M1` and `E2`. When $\pi \neq \pi'$, the vanishing part of `KY` gives $Z(1) = 0$.

In both cases $Z(s) = (s-1) Z_S(s) L^S(s)$ for $\operatorname{Re} s > \max(1, \sigma_0)$.

## In the Lean code

The theorem is in [RsPoleOfInputs.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/RsPoleOfInputs.lean#L74). `rspole_of` is in [PRSPole.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/PRSPole.lean#L35). `E2` and `M1` are in [ColumnConjugationMeasure.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/ColumnConjugationMeasure.lean#L214).

- `rspole_of` takes `G1` as `_hG1` and does not use it. The hypothesis `G1` of this theorem is still used, by `global_level_of`.
- All 22 hypotheses are used somewhere in the chain.
- Several lemmas have names from other fields. `E2` is proved by `duality_diagonalClass_of_affineProperBaseChange` ([LogBallEstimates.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/LogBallEstimates.lean#L120)), an étale cohomology name. `P3` is proved by `crystalline_clause_of_admitted` ([CubicPeriodConstant.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/CubicPeriodConstant.lean#L74)). The height bound `K1` is proved by `firstCohomologyBound_of_boundaryBound` ([EuclideanHeightMul.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/EuclideanHeightMul.lean#L155)). `K2` and `K3` come from `secondCohomologyBound_of_boundaryBound` and `koszulThree_of_det`.
