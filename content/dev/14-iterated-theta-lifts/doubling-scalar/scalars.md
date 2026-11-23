---
id: scalars
title: Positive step scalars of the theta chain under the standing hypotheses
kind: theorem
decl: GlobalTheory.Core.Rk.ScalarsRow.scalars
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ThetaChainStepPositiveScalarStandingHypotheses
covers: 1171
status: drafted
drafted_by: writer@claude
---
This theorem says that each step of the chain of theta lifts of a real datum multiplies inner products by a positive constant times an $L$-value. It only drops three hypotheses and calls [`scalars_of_heckeFormNS`](/entry/scalars-of-hecke-form-ns/). The real content is in [`scalars_of_given_all`](/entry/scalars-of-given-all/). Its only user is [the statement form](/entry/theta-chain-step-positive-scalar-standing-hypotheses/), which feeds [`upInj`](/entry/up-inj/).

## Statement

Let $R$ be a real datum (`RealDat D A Ks`) with a face $F$. It gives a chain of spaces $M_0, M_1, \dots, M_{m-1}$ (the models `R.MY k`) and a top space $H_X(t)$ for each index $t$, with inner products `IsIP` on each stage. Let $S_t$ be the set of bad places of $F$ for $t$ (`badPl R t`).

*Lifts.* A vector $x$ at stage $k+1$ is a lift of $u$ at stage $k$ (`IsUp`) if $x$ lies in the space `R.CC t (k+1)` and the inner product of $x$ with each $y$ there equals the inner product of $u$ with the image of $y$ under `R.ioY t k`. For an eigensystem $c$, the reached set at stage $k$ (`reached`) is the $c$-part at stage 0 away from $S_t$ (`rowPart`) for $k = 0$, and the set of lifts of the reached set at stage $k$ for $k+1$. The top step `IsUpTop` into $H_X(t)$ is defined in the same way.

*Step scalars.* `StepScalar t c k Λ` says: each reached $u$ at stage $k$ has a lift, and for lifts $x_1, x_2$ of reached $u_1, u_2$, $\langle x_1, x_2 \rangle = \Lambda \langle u_1, u_2 \rangle$. `TopScalar` is the same for the top step.

`Scalars R` says: there are $\kappa_1, \dots, \kappa_m > 0$ such that for each $t$ and each $c$ with nonzero $c$-part at stage 0, there is a family of parameters $B$ for $c$ away from $S_t$, and for each such $B$:

- for $1 \le j < m$, step $j-1$ has the scalar $\kappa_j \ell_j$;
- the top step has the scalar $\kappa_m \ell_m$;

where $\ell_j > 0$ is the value at $(1 + t_D)/2$ of the partial $L$-function $L^{S_t}(s, B, \mu_{t,j})$, which converges there (`IsLValue`).

**Theorem.** Assume `DiscreteSeriesCover`, `HarishChandraFinite`, `HarishChandraModules`, `CasselmanWallach`, `CuspRapidDecay`, `HoweUnram`, `WeilSiegelFormulaUnitary`, `HeckeFormNS D'` for all $D'$, `SiegelEisensteinContinuation` and `UnramifiedDoublingGL`. If `Given R F` holds and `D.host.ccK = ⊤`, then `Scalars R`.

## Proof

The proof calls [`scalars_of_heckeFormNS`](/entry/scalars-of-hecke-form-ns/) with eight of the ten propositions and `Given R F`.

## In the Lean code

The theorem is in [ThetaChainStepPositiveScalarStandingHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypotheses.lean#L39). `Scalars` is in [LabelSettingScalars.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean#L74).

Three hypotheses are bound as `_` and not used: `WeilSiegelFormulaUnitary`, `SiegelEisensteinContinuation` and `D.host.ccK = ⊤`. So the theorem is a weaker form of `scalars_of_heckeFormNS`. Its callers ([`upInj`](/entry/up-inj/), through the statement form) must still supply all three.
