---
id: up-inj
title: The scalar formula for the theta lift, and injectivity of its adjoint
kind: theorem
decl: GlobalTheory.Core.Rk.UpInjRow.upInj
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ThetaLiftAdjointScalarFormulaInjective
covers: 1230
status: drafted
drafted_by: writer@claude
---
This theorem proves two facts about the theta map $\Theta_t$ at the top of a chain of theta lifts: $\Theta_t \Theta_t^*$ acts on each Hecke eigenspace by a positive constant times a product of $L$-values, and $\Theta_t^*$ is injective. Its only user is [the statement form](/entry/theta-lift-adjoint-scalar-formula-injective/), which sits in branch 1 of the [unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

Let $R$ be a real datum (`RealDat D A Ks`) with a face $F$. For each index $t \in T$, $R$ gives a linear map $\Theta_t \colon H_X(t) \to H_E$ (`R.Th t`) between finite-dimensional complex inner product spaces. For the finite sets $P_g$ and $Q_t$ of places of $E$ in $R$, let $S_t$ be the set of places of $F$ below $P_g \cup Q_t$ (`badPl R t`). For an eigensystem $c$ and a finite set $S$ of places of $F$, let $E_c^S \subseteq H_E$ be the $c$-part of $H_E$ away from $S$ (`EEc R S c`, the preimage of `partDual`, which we have not unfolded).

Call $z > 0$ an *$L$-value at $(i, t, c)$* (`IsLval`) if there is a family of parameters $B$ for $c$ away from $S_t$ (`IsSysParamD`) such that the partial $L$-function $L^{S_t}(s, B, \mu_{t,i+1})$ (`LSD`) converges at $s_0 = (1 + t_D)/2$ and has the value $z$ there. Here $\mu_{t,j}$ is a character that $R$ gives, and $t_D$ is the number `D.R.t`.

**Theorem.** Assume ten named propositions: `DiscreteSeriesCover`, `HarishChandraFinite`, `HarishChandraModules`, `CasselmanWallach`, `CuspRapidDecay`, `HoweUnram`, `WeilSiegelFormulaUnitary`, `HeckeFormNS D'` for every $D'$, `SiegelEisensteinContinuation`, `UnramifiedDoublingGL`. Assume:

1. `Given R F`: the core conditions `Hk3.Core R F`, a parameter choice for $D$, irreducible characters in `A.X`, and three further conditions (`GoodTypes`, `QGuard` and a gap condition);
2. the ideal $\mathfrak c_K$ of the host datum (`D.host.ccK`) is the unit ideal;
3. the set `R.Sb` equals $P_g$;
4. at each place $P$ of $E$ that is fixed by conjugation and good for $t$ (no place of $P_g \cup Q_t$ equals $P$ or is conjugate to it), the Weil representations of the chain fix their vacuum vectors at $P$ (`FixAll R t P`; we have not unfolded `VacFix`).

Let $S$ be the set of places of $F$ below $P_g$ (`IsSF R S`). Then:

- (`BForm R S`) there is $\kappa_0 > 0$ such that for all $t$, $c$ and $z_1, \dots, z_m$ with $z_i$ an $L$-value at $(i, t, c)$, $\Theta_t \Theta_t^* x = \kappa_0 \prod_i z_i \cdot x$ for every $x \in E_c^S$;
- (`UpInj R`) $\Theta_t^*$ is injective for every $t$.

## Proof

1. [`thetaChainStep_positive_scalar_standingHypotheses`](/entry/theta-chain-step-positive-scalar-standing-hypotheses/) gives [`Scalars R`](/entry/scalars/): each step of the chain multiplies inner products by $\kappa_j$ times an $L$-value, with $\kappa_j > 0$.
2. `thetaLift_adjoint_keeps_spherical_parts_off_tuple` (a relay to `KeptRows.kept`) gives `Kept R`: $\Theta_t \Theta_t^*$ maps $E_c^{S_t}$ into itself. It uses `CuspRapidDecay`, `HoweUnram`, the core conditions and hypothesis 4.
3. `schurAll_of_cuspRapidDecay` gives `SchurAll R`, a Schur multiplicity condition at each stage.
4. `ChainScalar.bForm` gives `BForm R S` with $\kappa_0 = \prod_{i=1}^{m} \kappa_i$. It composes the step scalars of item 1 along the chain.
5. `upInj_of_bForm` gives `UpInj R`. The spaces $E_c^S$ span $H_E$ (`exists_opsE`). On each of them $\Theta_t \Theta_t^*$ is a nonzero scalar, so the range of $\Theta_t$ is all of $H_E$. Then $\ker \Theta_t^* = (\operatorname{im} \Theta_t)^\perp = 0$ (`adjoint_inj_of_parts`).

## In the Lean code

The theorem is in [ThetaLiftAdjointScalarFormulaInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjective.lean#L32). `ChainScalar.bForm` is in [LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean#L350) and `upInj_of_bForm` in [UpInjOfBForm.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UpInjOfBForm.lean#L52).

Four hypotheses do no work. The hypothesis `R.Sb = R.Pg` is bound as `_hSb` and never used. `WeilSiegelFormulaUnitary`, `SiegelEisensteinContinuation` and $\mathfrak c_K = \mathcal O_K$ go only to `thetaChainStep_positive_scalar_standingHypotheses`, whose proof [`scalars`](/entry/scalars/) discards them. Also, `upInj_of_bForm` takes the irreducibility of the characters as `hI` and never uses it.
