---
id: scalars-of-given-all
title: Each theta step multiplies inner products by a positive multiple of an L-value
kind: theorem
decl: GlobalTheory.ChainTw.scalars_of_given_all
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ScalarsOfGivenData
covers: 1168
status: drafted
drafted_by: writer@claude
---
This theorem proves the scalar law `Scalars R` for a chain of [[theta|6WB6TKE70H]] lifts: each step of the chain multiplies inner products by a positive constant times a positive L-value. Its only user is the restatement [`thetaChain_steps_positive_multiple_of_LValue`](/entry/theta-chain-steps-positive-multiple-of-lvalue/), which [`scalars_of_heckeFormNS`](/entry/scalars-of-hecke-form-ns/) calls. Higher up, the result feeds [`member_bundles_large_unramified_exponents_alt`](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/) below the step [HypsAlt is nonempty](/step/nonempty-hyps/).

## Statement

Let $D$ be a datum (`D7`) with chain length $m$ and an integer $t$ (`D.R.t`). Let $A$ be a family of characters indexed by a type $T$, let $R$ be a real realisation of $A$ over a number field $K_s$ (`RealDat`), and let $F$ be a face. For $\tau \in T$ and an eigensystem $c$, the row part $W(\tau, c)$ is a space of forms on the first group of the chain. A vector $x$ at level $k+1$ is an *up-image* of $u$ at level $k$ if $x$ lies in the space `R.CC τ (k+1)` and $\langle x, y\rangle_{k+1} = \langle u, \iota_k y\rangle_k$ for all $y$ there. So the up map is the adjoint of the map $\iota_k$ from level $k+1$ to level $k$. Let $\mathcal R_k(\tau, c)$ be the vectors reached from $W(\tau, c)$ by $k$ up steps.

`Scalars R` says: there are reals $\kappa_j > 0$ for $1 \le j \le m$ such that, for each $\tau$ and each $c$ with $W(\tau, c) \neq 0$, $c$ has a parameter system $B$, and for each such $B$:

- for $k + 1 < m$ there is $l > 0$ with $l = L^S\bigl(\tfrac{1+t}{2}, B, \mu_{\tau,k+1}\bigr)$, such that each $u \in \mathcal R_k$ has an up-image, and up-images $x_1, x_2$ of $u_1, u_2 \in \mathcal R_k$ satisfy $\langle x_1, x_2\rangle = \kappa_{k+1}\, l\, \langle u_1, u_2\rangle$;
- the same holds at the top step, into the Hilbert space `(R.HX τ).H`, with $\kappa_m$ and the L-value at index $m$.

Here $S$ is the set of bad places of $\tau$ and $L^S$ is the partial L-function `LSD`; we have not unfolded it.

**Theorem.** Assume seven named inputs: `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `CasselmanWallach`, `HoweUnram` and `UnramifiedDoublingGL`. Assume `Given R F` (six fields: a core condition, a parameter choice, absolute irreducibility of the characters of $A$, good types, a guard, and gaps $\lambda_n - \lambda_{n+1} \ge 100 r^4$), `NodeGap D` (consecutive nodes of the highest weight data differ by at least $t + 2N^3 + 1$ for some $N > $ `rankX'`), and `HeckeFormNS D`. Then `Scalars R`.

`HeckeFormNS D` is the main analytic input. For theta lifts $\theta(\Phi, u)$ between two hermitian spaces with $t \ge 2$, it says

$$\langle \theta(\Phi_1, u_1), \theta(\Phi_2, u_2)\rangle = \mathrm{vol} \cdot \frac{L^S(\tfrac{t+1}{2})}{d^S(\tfrac t2)} \int \langle \omega(g)\Phi_1, \Phi_2\rangle \langle \pi(g) u_1, u_2\rangle \, dg,$$

with the integral over the elements that are integral off $S$. This has the shape of the Rallis inner product formula (Gan, Qiu and Takeda, Invent. Math. 198 (2014)). Here it is a hypothesis.

## Proof

1. Facts at the datum $D$. `twistedChain_stage_soft_properties` gives `SoftQ` (finite dimension and inner products at each stage). Three lemmas with no hypotheses give the level laws, the restored Euler factors and `LFull`. `twistedChain_thetaLiftUpSpan` and `chainThetaLiftsAdjoint_of_cuspRapidDecay` give span and adjoint facts, and `chain_theta_lift_up_eq_adjoint_value` combines them into `UpVal`.
2. `thetaLiftChainStep_exact_innerProduct` turns `HeckeFormNS` into `StepExactNS`: at each step the Petersson product of two lifts is $\mathrm{vol} \cdot (l/d^S)$ times a local factor times a real zeta integral times $\langle u_1, u_2\rangle$. Its other inputs come from `UnramifiedDoublingGL` and the twisted transform laws.
3. `twistedThetaChain_step_adjoint_scalar` turns this into `StepLam`: the constant is $\kappa \cdot L^S$ with $\kappa \neq 0$. It uses the parameter transfer (from `HoweUnram`) and the lower block parameter.
4. Facts at $R$, from `Given`: the range condition `RangeX`, the chain `RChain`, nonvanishing of the real zeta integrals, and uniformity in $\tau$ (`RUnif`, which uses `NodeGap`).
5. `chainStep_scalars_of_realisation` assembles these, with positivity of the first L-values, into `Scalars R`.

## In the Lean code

The theorem is at [ScalarsOfGivenData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ScalarsOfGivenData.lean#L48). `Scalars` is in [LabelSettingScalars.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean#L74), `HeckeFormNS` in [HeckeFormNSOfHeckeForm.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HeckeFormNSOfHeckeForm.lean#L202), and `StepExactNS` in [StepExactNS.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/StepExactNS.lean#L89). We have not opened the proofs of the lemmas of steps 1 to 5, nor unfolded `NormX`, `RowPar` and `IPDict`.

All ten hypotheses are used. `HoweUnram` is a hypothesis here, although `howeUnram_holds` proves it elsewhere (see [HypsAlt is nonempty](/step/nonempty-hyps/)). The term `lowerBlockParameter_of_one_nonzeroValue D soft` is built twice, at lines 60 and 66.
